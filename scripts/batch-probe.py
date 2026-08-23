#!/usr/bin/env python3
"""Wave 2 (#559): batch probe — lease-controlled clone cache + state.json.

One probe unit: acquire a lease on the (url, pin) reference clone (HIT
reuses the warm clone; MISS clones bare+blob:none under a short probe
lease, then promotes), create a throwaway worktree, walk it, release.

Outcomes recorded in batch/state.json (keyed, resumable): ``ok``,
``clone_timeout``, ``disk_budget``, ``lease_reject``, ``cache_miss_reprobe``,
``skip_wave_active``, ``auto_nogo``, ``needs_human``, ``rate_limited``,
``error``.

Wave gating is DERIVED from the corpus event log (corpus_lock) — the
caller cannot claim the wave is active (Luna r1 #14); a missing/invalid
status fails closed.

Disk budget: ``--probe-fetch-limit-mb`` bounds the bare clone;
``--max-disk-mb`` (unchanged) bounds the post-walk worktree.
``lifecycle_bytes = probe_fetch_bytes`` ONLY (no worktree/walk bytes).
Hits record bytes_saved (fetch avoided) and ZERO lifecycle fetch bytes
(Luna r1 #15 — metrics were reversed).

Usage::

  python3 scripts/batch-probe.py --url https://github.com/openwrt/packages \\
      --pin <sha> --corpus openwrt_packages --manifest-digest <sha256> \\
      --max-disk-mb 500 --probe-fetch-limit-mb 2048
"""

from __future__ import annotations

import argparse
import os
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from regexproof.admission import clone_cache  # noqa: E402
from regexproof.admission.clone import CloneError, enforce_disk_budget  # noqa: E402
from regexproof.mine import batch_state, corpus_lock, disk_admission  # noqa: E402


def _wave_status(corpus: str) -> str:
    """Derive wave status from the corpus event log (fail-closed: a
    missing/invalid status refuses to probe — Luna r1 #14)."""
    try:
        return corpus_lock.wave_status(corpus)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise SystemExit(
            f"batch-probe: cannot derive wave status for {corpus!r} from the "
            f"corpus event log ({exc}) — fail closed"
        ) from exc


def _record(
    digest: str,
    url: str,
    pin: str,
    outcome: str,
    extra: dict | None,
    state: pathlib.Path | None,
) -> None:
    # Luna r3 #2: a state-write failure must NOT be swallowed — a corrupt
    # state must not produce a successful probe with no durable outcome.
    # Propagate SystemExit so the CLI fails closed.
    batch_state.record_outcome(
        digest or "unknown", url, pin, outcome, extra=extra, path=state,
    )


def _dir_size_bytes(path: pathlib.Path) -> int:
    total = 0
    for p in path.rglob("*"):
        if p.is_file():
            try:
                total += p.stat().st_size
            except OSError:
                pass
    return total


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--url", required=True)
    ap.add_argument("--pin", required=True)
    ap.add_argument("--corpus", default="")
    ap.add_argument("--manifest-digest", default="")
    ap.add_argument("--max-disk-mb", type=int, default=500)
    ap.add_argument(
        "--probe-fetch-limit-mb", type=int, default=None,
        help="Per-clone fetch cap; defaults to --max-disk-mb (a default of "
             "2048 with a 500 max would always be refused — Luna r2 #1)",
    )
    ap.add_argument("--cache-root", type=pathlib.Path, default=None)
    ap.add_argument("--state", type=pathlib.Path, default=None)
    ap.add_argument("--worker-count", type=int, default=1, help="W for the disk semaphore")
    ap.add_argument("--walk-root", type=pathlib.Path, default=None,
                    help="Where to write the staged probe draft (default: "
                         "properties/staged_probes/)")
    ap.add_argument(
        "--skip-wave-active", action="store_true",
        help="#559: skip an E3 reprobe while a conversion wave is ACTIVE "
        "(wave status derived from the corpus event log)",
    )
    args = ap.parse_args(argv)

    probe_cap = args.probe_fetch_limit_mb or args.max_disk_mb
    # #6 (Luna r3): injected paths must be CONSISTENT — the lease registry
    # lives under the cache root (cache/<root>/leases.json), and the
    # admission registry follows the state path. Separate cache/state roots
    # must not silently conflict on leases or bypass shared admission.
    cache_root = args.cache_root
    registry_path = None if cache_root is None else cache_root / "leases.json"

    if args.skip_wave_active:
        status = _wave_status(args.corpus)
        if status == "active":
            _record(
                args.manifest_digest, args.url, args.pin, "skip_wave_active",
                {"corpus": args.corpus, "wave_status": status}, args.state,
            )
            print(f"skip_wave_active: {args.corpus} wave_status=active")
            return 0

    digest = args.manifest_digest or "unknown"
    owner = os.getpid()
    t0 = time.monotonic()
    entry = None
    wt = None
    # Begin the keyed state item (resume-safe: started_at set, completed_at
    # filled by record_outcome).
    batch_state.begin_item(digest, args.url, args.pin, path=args.state)
    admitted = disk_admission.reserve(
        worker_count=args.worker_count,
        per_clone_cap_mb=probe_cap,
        max_disk_mb=args.max_disk_mb,
        owner_pid=owner,
        path=None if args.state is None else args.state.with_name("admission.json"),
    )
    if not admitted:
        _record(digest, args.url, args.pin, "disk_budget",
                {"corpus": args.corpus, "worker_count": args.worker_count,
                 "error": "disk admission refused (W=0 or budget exhausted)"},
                args.state)
        print(f"disk_budget: admission refused W={args.worker_count} "
              f"cap={probe_cap}MB max={args.max_disk_mb}MB")
        return 2
    try:
        try:
            entry = clone_cache.cache_acquire(
                args.url, args.pin, owner_pid=owner,
                max_disk_mb=probe_cap,
                root=cache_root, registry_path=registry_path,
            )
        except SystemExit as exc:
            msg = str(exc)
            # Order matters: promote's "no live probe lease (cache_miss_reprobe)"
            # message ALSO contains "lease_reject" — check the specific
            # cache_miss_reprobe marker first (CodeRabbit #570).
            if "cache_miss_reprobe" in msg or "no live probe lease" in msg:
                outcome = "cache_miss_reprobe"
            elif "lease_reject" in msg:
                outcome = "lease_reject"
            elif "disk_budget" in msg or "probe-fetch-limit-mb" in msg:
                outcome = "disk_budget"
            else:
                outcome = "error"
            _record(digest, args.url, args.pin, outcome,
                    {"corpus": args.corpus, "error": msg[:200]}, args.state)
            print(f"{outcome}: {args.url}@{args.pin[:12]} ({msg[:120]})")
            return 2 if outcome in ("lease_reject", "disk_budget", "cache_miss_reprobe") else 3
        except CloneError as exc:
            # Clone/fetch failures surface as CloneError (Luna r1 #3: they
            # were previously uncaught → no state row, traceback).
            _record(digest, args.url, args.pin, "clone_timeout",
                    {"corpus": args.corpus, "error": str(exc)[:200]}, args.state)
            print(f"clone_timeout: {args.url}@{args.pin[:12]} ({str(exc)[:120]})")
            return 3
        except subprocess.TimeoutExpired as exc:
            _record(digest, args.url, args.pin, "clone_timeout",
                    {"corpus": args.corpus, "error": str(exc)[:200]}, args.state)
            print(f"clone_timeout: {args.url}@{args.pin[:12]} (timeout)")
            return 3

        clone_ms = int((time.monotonic() - t0) * 1000)
        cache_dir = pathlib.Path(entry["dir"])
        # Byte accounting (CodeRabbit #570 / Luna r1 #15): on a HIT the
        # probe avoided a full fetch — bytes_saved = the clone size a fresh
        # fetch would have cost; lifecycle_bytes stays ZERO (no probe fetch
        # happened). On a MISS bytes_saved = 0 and lifecycle_bytes = the
        # actual probe fetch.
        is_hit = bool(entry.get("cache_hit"))
        probe_fetch_bytes = 0 if is_hit else _dir_size_bytes(cache_dir)
        bytes_saved = _dir_size_bytes(cache_dir) if is_hit else 0

        try:
            wt = clone_cache.worktree_for(
                args.url, args.pin, owner_pid=owner, root=cache_root,
            )
            # Renew the lease AFTER the walk so a long walk can't be evicted
            # mid-use (Luna r3 #5) — done under the registry lock.
            from regexproof.mine import lease_registry

            lease_registry.renew(
                args.url, args.pin, owner_pid=owner, path=registry_path,
            )
            # Post-walk disk budget (unchanged semantics, on the worktree).
            enforce_disk_budget(wt, args.max_disk_mb)
        except (CloneError, SystemExit, subprocess.TimeoutExpired) as exc:
            # Worktree timeouts were uncaught (Luna r2 #3) — record + exit.
            _record(digest, args.url, args.pin, "disk_budget",
                    {"corpus": args.corpus, "error": str(exc)[:200]}, args.state)
            print(f"disk_budget: {str(exc)[:160]}")
            return 2

        # Metrics (Luna r1 #15 — were reversed): hits account AVOIDED fetch
        # bytes; lifecycle_bytes is probe-fetch ONLY (zero on hits).
        # Then WALK the worktree and write a staged probe draft (Luna r1
        # #2: a probe that only creates a worktree is not a probe).
        staged_root = args.walk_root or (ROOT / "properties" / "staged_probes")
        staged_root.mkdir(parents=True, exist_ok=True)
        import hashlib
        import json

        walked = 0
        for p in sorted(wt.rglob("*")):
            if p.is_file() and ".git" not in p.parts:
                walked += 1
        draft = {
            "manifest_digest": digest,
            "url": args.url,
            "pin": args.pin,
            "corpus": args.corpus,
            "cache_hit": bool(entry.get("cache_hit")),
            "clone_ms": clone_ms,
            "files_walked": walked,
            "probe_fetch_bytes": probe_fetch_bytes,
            "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }
        draft_name = hashlib.sha256(f"{digest}#{args.url}#{args.pin}".encode()).hexdigest()[:24]
        draft_path = staged_root / f"{draft_name}.draft.json"
        tmp = draft_path.with_suffix(".tmp")
        tmp.write_text(json.dumps(draft, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        os.replace(tmp, draft_path)

        _record(
            digest, args.url, args.pin, "ok",
            {
                "corpus": args.corpus,
                "cache_hit": is_hit,
                "bytes_saved": bytes_saved,          # avoided fetch (hits)
                "fetch_bytes": probe_fetch_bytes,    # actual probe fetch
                "lifecycle_bytes": probe_fetch_bytes,  # probe_fetch only
                "clone_ms": clone_ms,
                "files_walked": walked,
                "draft": str(draft_path),
            },
            args.state,
        )
        print(f"ok: {args.url}@{args.pin[:12]} hit={is_hit} "
              f"fetch={probe_fetch_bytes}B saved={bytes_saved}B walk={walked} clone_ms={clone_ms}")
        return 0
    finally:
        # Exception-safe cleanup (Luna r3 #3): a worktree_remove failure
        # must NOT skip lease + admission release. Each step is guarded.
        try:
            if wt is not None and wt.exists():
                clone_cache.worktree_remove(
                    args.url, args.pin, owner_pid=owner, root=cache_root,
                )
        except Exception:  # cleanup must never mask the result
            pass
        try:
            if entry is not None:
                clone_cache.release(
                    args.url, args.pin, owner_pid=owner,
                    registry_path=registry_path,
                )
        except Exception:
            pass
        try:
            disk_admission.release(
                owner_pid=owner,
                path=None if args.state is None else args.state.with_name("admission.json"),
            )
        except Exception:
            pass


if __name__ == "__main__":
    raise SystemExit(main())

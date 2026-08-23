#!/usr/bin/env python3
"""Wave 2 (#559): batch probe — lease-controlled clone cache + state.json.

One probe unit: acquire a lease on the (url, pin) reference clone (HIT
reuses the warm clone; MISS clones bare+blob:none under a short probe
lease, then promotes), create a throwaway worktree, walk it, release.

Outcomes recorded in batch/state.json: ``ok``, ``clone_timeout``,
``disk_budget``, ``lease_reject``, ``cache_miss_reprobe``,
``skip_wave_active``.

Disk budget: ``--probe-fetch-limit-mb`` bounds the bare clone;
``--max-disk-mb`` (unchanged) bounds the post-walk worktree.
``lifecycle_bytes = probe_fetch_bytes`` ONLY (no worktree/walk bytes).

Usage::

  python3 scripts/batch-probe.py --url https://github.com/openwrt/packages \\
      --pin <sha> --corpus openwrt_packages --manifest-digest <sha256> \\
      --max-disk-mb 500 --probe-fetch-limit-mb 2048
"""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from regexproof.admission import clone_cache  # noqa: E402
from regexproof.mine import batch_state  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--url", required=True)
    ap.add_argument("--pin", required=True)
    ap.add_argument("--corpus", default="")
    ap.add_argument("--manifest-digest", default="")
    ap.add_argument("--max-disk-mb", type=int, default=500)
    ap.add_argument("--probe-fetch-limit-mb", type=int, default=clone_cache.PROBE_FETCH_LIMIT_MB)
    ap.add_argument("--cache-root", type=pathlib.Path, default=None)
    ap.add_argument("--state", type=pathlib.Path, default=None)
    ap.add_argument("--wave-status", default="active",
                    help="corpus wave_status; skip_wave_active when not 'active'")
    args = ap.parse_args(argv)

    if args.wave_status != "active":
        batch_state.record_outcome(
            args.manifest_digest or "unknown", args.url, args.pin,
            "skip_wave_active", extra={"corpus": args.corpus},
            path=args.state,
        )
        print(f"skip_wave_active: {args.corpus} wave_status={args.wave_status}")
        return 0

    owner = os.getpid()
    t0 = time.monotonic()
    try:
        entry = clone_cache.cache_acquire(
            args.url, args.pin, owner_pid=owner,
            max_disk_mb=args.probe_fetch_limit_mb,
            root=args.cache_root,
        )
    except SystemExit as exc:
        # lease_reject / disk_budget surfaced as SystemExit — record the
        # outcome and propagate.
        msg = str(exc)
        if "lease_reject" in msg:
            outcome = "lease_reject"
        elif "disk_budget" in msg or "probe-fetch-limit-mb" in msg:
            outcome = "disk_budget"
        else:
            outcome = "clone_timeout"
        batch_state.record_outcome(
            args.manifest_digest or "unknown", args.url, args.pin,
            outcome, extra={"corpus": args.corpus, "error": msg[:200]},
            path=args.state,
        )
        print(f"{outcome}: {args.url}@{args.pin[:12]} ({msg[:120]})")
        return 2 if outcome in ("lease_reject", "disk_budget") else 3

    clone_ms = int((time.monotonic() - t0) * 1000)
    probe_fetch_bytes = 0
    cache_dir = pathlib.Path(entry["dir"])
    if cache_dir.is_dir():
        for p in cache_dir.rglob("*"):
            if p.is_file():
                try:
                    probe_fetch_bytes += p.stat().st_size
                except OSError:
                    pass

    wt = None
    try:
        wt = clone_cache.worktree_for(
            args.url, args.pin, owner_pid=owner, root=args.cache_root,
        )
        # Post-walk disk budget (unchanged semantics, on the worktree).
        from regexproof.admission.clone import enforce_disk_budget
        enforce_disk_budget(wt, args.max_disk_mb)
        batch_state.record_outcome(
            args.manifest_digest or "unknown", args.url, args.pin, "ok",
            extra={
                "corpus": args.corpus,
                "cache_hit": bool(entry.get("cache_hit")),
                "bytes_saved": 0 if entry.get("cache_hit") else probe_fetch_bytes,
                "lifecycle_bytes": probe_fetch_bytes,
                "clone_ms": clone_ms,
            },
            path=args.state,
        )
        print(f"ok: {args.url}@{args.pin[:12]} hit={entry.get('cache_hit')} "
              f"fetch={probe_fetch_bytes}B clone_ms={clone_ms}")
        return 0
    except SystemExit as exc:
        batch_state.record_outcome(
            args.manifest_digest or "unknown", args.url, args.pin,
            "disk_budget", extra={"corpus": args.corpus, "error": str(exc)[:200]},
            path=args.state,
        )
        print(f"disk_budget: {str(exc)[:160]}")
        return 2
    finally:
        import shutil
        if wt is not None and wt.exists():
            shutil.rmtree(wt, ignore_errors=True)
        clone_cache.release(args.url, args.pin, owner_pid=owner)


if __name__ == "__main__":
    raise SystemExit(main())

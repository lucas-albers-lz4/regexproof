#!/usr/bin/env python3
"""Wave 5 (#574): snapshot rank → hashed batch/manifest.json → unattended loop.

One command drains a ranked manifest (resume-safe, digest-verified). Each
item is ``scripts/batch-probe.py`` keyed on ``(manifest_digest, url, pin)``.
Auto-NO-GO is folded into the probe (not a second ``--auto`` step).

Usage::

  python3 scripts/batch-run.py --limit 10
  python3 scripts/batch-run.py --snapshot-only --limit 10
  python3 scripts/batch-run.py --manifest batch/manifest.json
"""

from __future__ import annotations

import argparse
import io
import pathlib
import sys
from contextlib import redirect_stdout
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from regexproof.mine import batch_manifest, batch_state  # noqa: E402


def _rank_ndjson(argv: list[str]) -> str:
    spec_argv = argv
    # Import the rank CLI in-process (no network unless tree-probe-budget > 0).
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "rank_mine", ROOT / "scripts" / "rank-mine-candidates.py"
    )
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    buf = io.StringIO()
    with redirect_stdout(buf):
        rc = mod.main(spec_argv)
    if rc != 0:
        raise SystemExit(f"batch-run: rank-mine-candidates exited {rc}")
    return buf.getvalue()


def _completed(digest: str, url: str, pin: str, state: pathlib.Path | None) -> bool:
    reg = batch_state.load_state(state)
    rows = reg.get("rows") or {}
    if not isinstance(rows, dict):
        return False
    row = rows.get(batch_state._row_key(digest, url, pin)) or {}
    return bool(row.get("completed_at"))


def _drain(
    doc: dict[str, Any],
    *,
    state: pathlib.Path | None,
    generated: pathlib.Path | None,
    ledger: pathlib.Path | None,
    walk_root: pathlib.Path | None,
    cache_root: pathlib.Path | None,
    max_disk_mb: int,
    probe_fetch_limit_mb: int | None,
) -> int:
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "batch_probe", ROOT / "scripts" / "batch-probe.py"
    )
    assert spec is not None and spec.loader is not None
    probe_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(probe_mod)

    digest = str(doc["digest"])
    failures = 0
    for item in doc["items"]:
        url = str(item["url"])
        pin = str(item["pin"])
        corpus = str(item.get("corpus") or batch_manifest.corpus_from_url(url))
        if _completed(digest, url, pin, state):
            print(f"skip_complete: {url}@{pin[:12]}")
            continue
        argv = [
            "--url", url,
            "--pin", pin,
            "--corpus", corpus,
            "--manifest-digest", digest,
            "--max-disk-mb", str(max_disk_mb),
        ]
        if probe_fetch_limit_mb is not None:
            argv.extend(["--probe-fetch-limit-mb", str(probe_fetch_limit_mb)])
        if state is not None:
            argv.extend(["--state", str(state)])
        if generated is not None:
            argv.extend(["--generated", str(generated)])
        if ledger is not None:
            argv.extend(["--ledger", str(ledger)])
        if walk_root is not None:
            argv.extend(["--walk-root", str(walk_root)])
        if cache_root is not None:
            argv.extend(["--cache-root", str(cache_root)])
        rc = probe_mod.main(argv)
        if rc not in (0,):
            failures += 1
            print(f"batch-run: probe rc={rc} {url}@{pin[:12]}", file=sys.stderr)
    return 0 if failures == 0 else 2


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=10, help="Rank snapshot size (0 = all)")
    ap.add_argument(
        "--allocator",
        choices=("score-v1", "score-v1.5", "score-v2"),
        default="score-v1",
        help="Live drain allocator (default score-v1; eval flip is offline-only)",
    )
    ap.add_argument("--manifest", type=pathlib.Path, default=None)
    ap.add_argument(
        "--replace-manifest",
        action="store_true",
        help="Overwrite batch/manifest.json even if a digest already exists",
    )
    ap.add_argument("--snapshot-only", action="store_true")
    ap.add_argument(
        "--from-ndjson",
        type=pathlib.Path,
        default=None,
        help="Offline rank JSONL (tests / no live rank)",
    )
    ap.add_argument("--ledger", type=pathlib.Path, default=None)
    ap.add_argument("--generated", type=pathlib.Path, default=None)
    ap.add_argument("--state", type=pathlib.Path, default=None)
    ap.add_argument("--walk-root", type=pathlib.Path, default=None)
    ap.add_argument("--cache-root", type=pathlib.Path, default=None)
    ap.add_argument("--max-disk-mb", type=int, default=500)
    ap.add_argument("--probe-fetch-limit-mb", type=int, default=None)
    args = ap.parse_args(argv)

    man_path = args.manifest or (ROOT / "batch" / "manifest.json")
    snapshot = (
        args.from_ndjson is not None
        or args.replace_manifest
        or not man_path.is_file()
    )
    if snapshot:
        if man_path.is_file() and not args.replace_manifest:
            raise SystemExit(
                f"batch-run: {man_path} exists — pass --replace-manifest to overwrite"
            )
        if args.from_ndjson is not None:
            text = args.from_ndjson.read_text(encoding="utf-8")
        else:
            rank_argv = ["--limit", str(args.limit), "--allocator", args.allocator]
            if args.generated is not None:
                rank_argv.extend(["--generated", str(args.generated)])
            text = _rank_ndjson(rank_argv)
        items = batch_manifest.items_from_rank_ndjson(text)
        doc = batch_manifest.write_manifest(
            items,
            allocator=args.allocator,
            limit=args.limit,
            path=man_path,
        )
        print(f"snapshot: {len(items)} items digest={doc['digest'][:16]}… -> {man_path}")
    else:
        doc = batch_manifest.load_and_verify(man_path)
        print(f"resume: {len(doc['items'])} items digest={doc['digest'][:16]}…")

    if args.snapshot_only:
        return 0
    return _drain(
        doc,
        state=args.state,
        generated=args.generated,
        ledger=args.ledger,
        walk_root=args.walk_root,
        cache_root=args.cache_root,
        max_disk_mb=args.max_disk_mb,
        probe_fetch_limit_mb=args.probe_fetch_limit_mb,
    )


if __name__ == "__main__":
    raise SystemExit(main())

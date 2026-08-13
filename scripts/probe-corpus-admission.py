#!/usr/bin/env python3
"""Probe a candidate repo and emit a flagged admission draft (P1 A7).

Usage:
  python scripts/probe-corpus-admission.py <path-or-url> --pin <sha> [-o out.json]
"""

from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.admission.clone import (
    CloneError,
    cleanup_clone,
    enforce_disk_budget,
    partial_clone,
)
from regexproof.admission.draft import build_draft, emit_draft_text


def _is_url(s: str) -> bool:
    return (
        s.startswith("http://")
        or s.startswith("https://")
        or s.startswith("git@")
        or s.startswith("ssh://")
        or s.startswith("git://")
    )


def _repo_name_from_target(target: str) -> str:
    """Derive corpus name from a git URL or local path (never the clone dirname ``repo``)."""
    s = target.strip().rstrip("/")
    if s.startswith("git@"):
        path = s.split(":", 1)[-1]
    elif "://" in s:
        from urllib.parse import urlparse

        path = urlparse(s).path
    else:
        return Path(s).expanduser().resolve().name
    parts = [p for p in path.split("/") if p]
    if not parts:
        return "unknown"
    name = parts[-1]
    if name.endswith(".git"):
        name = name[:-4]
    return name or "unknown"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("target", help="Local path or git URL")
    ap.add_argument("--pin", default=None, help="Commit SHA to probe (required for URL)")
    ap.add_argument("-o", "--output", type=Path, help="Write draft JSON here")
    ap.add_argument(
        "--clone-root",
        type=Path,
        default=None,
        help="Injectable temp root for clones (tests)",
    )
    ap.add_argument("--repo-name", default=None, help="Override corpus/repo name")
    ap.add_argument("--url", default="", help="candidate_url to record in the draft")
    ap.add_argument(
        "--max-disk-mb",
        type=int,
        default=500,
        help="Abort if clone exceeds this size after walk materializes blobs",
    )
    args = ap.parse_args(argv)

    target = args.target
    clone_dir: Path | None = None
    try:
        if _is_url(target):
            if not args.pin:
                ap.error("--pin is required when target is a URL")
            base = args.clone_root or Path(tempfile.mkdtemp(prefix="regexproof-probe-"))
            clone_dir = base / "repo"
            result = partial_clone(
                target, dest=clone_dir, pin=args.pin, max_disk_mb=args.max_disk_mb
            )
            root = clone_dir
            cand_url = args.url or target
            # E3 stale-pin detection: pin_mined is the SHA from the ledger/CLI;
            # pin_probed is the default-branch HEAD captured at clone time.
            # If they differ, the mined pin is stale (branch moved since mining).
            pin_mined = args.pin
            pin_probed = result.default_head
            pin_walked = result.pin
            if pin_probed != pin_walked:
                print(
                    f"warning: stale mined pin — default-branch HEAD "
                    f"({pin_probed[:12]}) differs from walked SHA ({pin_walked[:12]})",
                    file=sys.stderr,
                )
        else:
            root = Path(target).expanduser().resolve()
            if not root.is_dir():
                print(f"error: not a directory: {root}", file=sys.stderr)
                return 2
            pin_walked = args.pin or "local"
            pin_mined = args.pin
            pin_probed = pin_walked
            cand_url = args.url or f"file://{root}"

        draft = build_draft(
            root,
            pin=pin_walked,
            pin_mined=pin_mined,
            pin_probed=pin_probed,
            repo_name=args.repo_name or _repo_name_from_target(target),
            candidate_url=cand_url,
        )
        if clone_dir is not None:
            # Re-check after walk materializes blob:none content.
            enforce_disk_budget(clone_dir, args.max_disk_mb)
        text = emit_draft_text(draft)
        if args.output:
            out = args.output.expanduser().resolve()
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(text, encoding="utf-8")
        else:
            sys.stdout.write(text)
        return 0
    except CloneError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    finally:
        if clone_dir is not None:
            cleanup_clone(clone_dir.parent if args.clone_root is None else clone_dir)


if __name__ == "__main__":
    raise SystemExit(main())

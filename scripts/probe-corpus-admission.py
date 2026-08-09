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

from regexproof.admission.clone import CloneError, cleanup_clone, partial_clone
from regexproof.admission.draft import build_draft, emit_draft_text


def _is_url(s: str) -> bool:
    return s.startswith("http://") or s.startswith("https://") or s.startswith("git@")


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
    args = ap.parse_args(argv)

    target = args.target
    clone_dir: Path | None = None
    try:
        if _is_url(target):
            if not args.pin:
                ap.error("--pin is required when target is a URL")
            base = args.clone_root or Path(tempfile.mkdtemp(prefix="regexproof-probe-"))
            clone_dir = base / "repo"
            pin = partial_clone(target, dest=clone_dir, pin=args.pin)
            root = clone_dir
            cand_url = args.url or target
        else:
            root = Path(target).expanduser().resolve()
            if not root.is_dir():
                print(f"error: not a directory: {root}", file=sys.stderr)
                return 2
            pin = args.pin or "local"
            cand_url = args.url or f"file://{root}"

        draft = build_draft(
            root,
            pin=pin,
            repo_name=args.repo_name or root.name,
            candidate_url=cand_url,
        )
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

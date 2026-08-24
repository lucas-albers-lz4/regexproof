#!/usr/bin/env python3
"""Wave 9 (#578): build the post-walk probe deny-list (soft, not wont_file).

Reads committed ``*_gate_decision.json`` files and writes
``properties/generated/probe_deny_list.json``. Rank applies a soft
deprioritize when the slug matches; candidates are never dropped.
Distinct from conversion ``wont_file``.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.io_atomic import atomic_write_text  # noqa: E402
from regexproof.mine.deny_list import DENY_LIST_PATH, build_deny_doc  # noqa: E402


def load_decisions(generated: Path) -> list[dict]:
    rows = []
    for path in sorted(generated.glob("*_gate_decision.json")):
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(doc, dict):
            rows.append(doc)
    return rows


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--generated",
        type=Path,
        default=ROOT / "properties" / "generated",
    )
    ap.add_argument("--out", type=Path, default=DENY_LIST_PATH)
    args = ap.parse_args(argv)
    doc = build_deny_doc(load_decisions(args.generated.expanduser().resolve()))
    text = json.dumps(doc, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    out = args.out.expanduser().resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    atomic_write_text(out, text)
    print(f"wrote {out} slugs={len(doc['slugs'])}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

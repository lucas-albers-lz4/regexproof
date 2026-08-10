#!/usr/bin/env python3
"""Rank mined ledger candidates for the hand-probe loop (#148).

Usage:
  python scripts/rank-mine-candidates.py
  python scripts/rank-mine-candidates.py --ledger PATH --status mined --limit 10
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.mine.ledger import load_ledger
from regexproof.mine.score import SCORE_VERSION, candidate_score, rank_candidates


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--ledger",
        type=Path,
        default=ROOT / "properties" / "generated" / "candidate-ledger.json",
    )
    ap.add_argument(
        "--status",
        default="mined",
        help="Only include candidates with this status (default: mined)",
    )
    ap.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Max rows to print (default: 10; 0 = all)",
    )
    args = ap.parse_args(argv)

    ledger_path = args.ledger.expanduser().resolve()
    if not ledger_path.is_file():
        print(f"error: ledger not found: {ledger_path}", file=sys.stderr)
        return 2
    try:
        ledger = load_ledger(ledger_path)
    except (OSError, ValueError, json.JSONDecodeError) as e:
        print(f"error: cannot load ledger: {e}", file=sys.stderr)
        return 2

    status = (args.status or "").strip()
    pool = [
        c
        for c in ledger.get("candidates", [])
        if isinstance(c, dict) and (not status or c.get("status") == status)
    ]
    ranked = rank_candidates(pool)
    if args.limit and args.limit > 0:
        ranked = ranked[: args.limit]

    for cand in ranked:
        total, breakdown = candidate_score(cand)
        row = {
            "url": cand.get("url"),
            "score": total,
            "score_version": SCORE_VERSION,
            "breakdown": breakdown,
            "stars": cand.get("stars"),
            "source_query": cand.get("source_query"),
            "pushed_date": cand.get("pushed_date"),
            "status": cand.get("status"),
            "pin": cand.get("pin"),
        }
        print(json.dumps(row, sort_keys=True, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Rank mined ledger candidates for the hand-probe loop (#148).

Usage:
  python scripts/rank-mine-candidates.py
  python scripts/rank-mine-candidates.py --ledger PATH --status mined --limit 10
  python scripts/rank-mine-candidates.py --no-skip-gated --limit 10
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.mine.exclusions import load_admitted_urls, normalize_repo_url
from regexproof.mine.ledger import load_ledger
from regexproof.mine.score import SCORE_VERSION, candidate_score, rank_candidates
from regexproof.mine.tree import (
    TreeCache,
    materialize_tree_features,
)


def _http_session():
    try:
        import requests
    except ImportError:  # pragma: no cover - package dependency in live runs
        return None
    return requests.Session()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--ledger",
        type=Path,
        default=ROOT / "properties" / "generated" / "candidate-ledger.json",
    )
    ap.add_argument(
        "--status",
        default="",
        help=(
            "Only include candidates with this status (default: none — the "
            "skip-gated default excludes gated:* rows; pass --no-skip-gated "
            "to include them)"
        ),
    )
    ap.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Max rows to print (default: 10; 0 = all)",
    )
    ap.add_argument(
        "--no-skip-gated",
        action="store_false",
        dest="skip_gated",
        help=(
            "Include URLs that already have a *_gate_decision.json. "
            "By default, gated rows are excluded."
        ),
    )
    ap.add_argument(
        "--generated",
        type=Path,
        default=ROOT / "properties" / "generated",
        help="Directory of gate decisions for skip-gated "
        "(default: properties/generated)",
    )
    ap.add_argument(
        "--tree-probe-budget",
        type=int,
        default=0,
        help=(
            "Max uncached GitHub tree calls. Cached responses do not consume "
            "the budget; 0 degrades to score-v1 metadata-only ranking."
        ),
    )
    ap.add_argument(
        "--tree-cache",
        type=Path,
        default=None,
        help="Tree cache path (default: .cache/regexproof/mine-tree.json).",
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

    gated: set[str] = set()
    if args.skip_gated:
        gated = load_admitted_urls(args.generated.expanduser().resolve())

    status = (args.status or "").strip()
    pool = []
    for c in ledger.get("candidates", []):
        if not isinstance(c, dict):
            continue
        if status and c.get("status") != status:
            continue
        url = c.get("url")
        c_status = c.get("status", "")
        if args.skip_gated and c_status.startswith("gated:"):
            continue
        if gated and url and normalize_repo_url(str(url)) in gated:
            continue
        pool.append(c)
    tree_features = {}
    if args.tree_probe_budget > 0 and pool:
        tree_features, _calls = materialize_tree_features(
            _http_session(),
            pool,
            budget=args.tree_probe_budget,
            cache=TreeCache(args.tree_cache),
        )
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
            "features": {
                "fork": cand.get("fork"),
                "size": cand.get("size"),
                "language": cand.get("language"),
                "archived": cand.get("archived"),
                "tree_probe": tree_features.get(
                    (normalize_repo_url(str(cand.get("url") or "")), str(cand.get("pin_probed") or ""))
                ),
            },
        }
        print(json.dumps(row, sort_keys=True, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

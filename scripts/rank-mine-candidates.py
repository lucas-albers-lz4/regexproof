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
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.mine.deny_list import load_deny_slugs  # noqa: E402  # ROOT bootstrap above
from regexproof.mine.density import (  # noqa: E402  # ROOT bootstrap above
    DensityCache,
    materialize_density_hits,
)
from regexproof.mine.exclusions import load_admitted_urls, normalize_repo_url  # noqa: E402  # ROOT bootstrap above
from regexproof.mine.ledger import load_ledger  # noqa: E402  # ROOT bootstrap above
from regexproof.mine.score import (  # noqa: E402  # ROOT bootstrap above
    candidate_score,
    rank_candidates,
    score_version_for_allocator,
)
from regexproof.mine.tree import (  # noqa: E402  # ROOT bootstrap above
    TreeCache,
    materialize_tree_features,
)


def _http_session():
    try:
        import requests
    except ImportError:  # pragma: no cover - package dependency in live runs
        return None
    return requests.Session()


def _int_map(value):
    """Normalize a mapping to str->int (the P6 build's probe shape)."""
    if not isinstance(value, dict):
        return {}
    return {str(k): int(v) for k, v in value.items() if isinstance(v, (int, float))}


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
            "the budget; 0 disables fresh probes (score-v2 still joins the "
            "tracked mine-tree-features.json)."
        ),
    )
    ap.add_argument(
        "--tree-cache",
        type=Path,
        default=None,
        help="Tree cache path (default: .cache/regexproof/mine-tree.json).",
    )
    ap.add_argument(
        "--tree-features",
        type=Path,
        default=ROOT / "properties" / "generated" / "mine-tree-features.json",
        help="Tracked pin-aware tree features used by score-v2.",
    )
    ap.add_argument(
        "--allocator",
        choices=("score-v1", "score-v1.5", "score-v2"),
        default="score-v1",
        help="Score allocator (default: score-v1; v1.5 adds the tree overlay).",
    )
    ap.add_argument(
        "--deny-list",
        type=Path,
        default=None,
        help=(
            "Wave 9 probe deny-list JSON (default: "
            "properties/generated/probe_deny_list.json). Soft penalty only."
        ),
    )
    ap.add_argument(
        "--no-deny-list",
        action="store_true",
        help="Do not apply the post-walk deny-list (soft screen stays off).",
    )
    ap.add_argument(
        "--code-search-budget",
        type=int,
        default=0,
        help=(
            "Max uncached GitHub code-search density calls (default: 0). "
            "Rate-limit degrades to unknown, never a hard reject."
        ),
    )
    ap.add_argument(
        "--density-cache",
        type=Path,
        default=None,
        help="Density cache path (default: .cache/regexproof/mine-density.json).",
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
    # Cumulative-MCR fold (M1/M2): score-v2's probe + tree features are
    # fitted on the GATE DECISIONS' probe data, but the ledger candidates
    # carry none of it — the runtime feature vector would zero every probe
    # feature.  Join the decisions (by URL) and attach the decision-time
    # probe + pin (E3 semantics: never the ledger's mined pin).
    decisions_by_url: dict[str, dict[str, Any]] = {}
    if args.allocator == "score-v2" or not args.skip_gated:
        gen = args.generated.expanduser().resolve()
        for path in sorted(gen.glob("*_gate_decision.json")):
            try:
                dec = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            curl = str(dec.get("candidate_url") or "")
            if curl:
                decisions_by_url.setdefault(normalize_repo_url(curl), dec)

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
        dec = (
            decisions_by_url.get(normalize_repo_url(str(url)))
            if url
            else None
        )
        if args.allocator == "score-v2" and dec is not None:
            probe = dec.get("probe") if isinstance(dec.get("probe"), dict) else {}
            # Close-out gate: normalize the decision probe to the FIT's
            # shape (the P6 build writes dialect_counts; the raw decision
            # stores dialect) — otherwise probe_dialect_count_log stays
            # zero at runtime and diverges from the fitted vector.
            c["probe"] = {
                "regex_sites": int(probe.get("regex_sites") or 0),
                "dialect_counts": _int_map(probe.get("dialect")),
                "security_boundary": str(
                    probe.get("security_boundary") or "unknown"
                ),
                "predicted_buckets": _int_map(probe.get("predicted_buckets")),
            }
        if dec is not None:
            probe = dec.get("probe") if isinstance(dec.get("probe"), dict) else {}
            dec_pin = str(
                probe.get("pin_probed")
                or dec.get("corpus_pin")
                or probe.get("pin")
                or ""
            )
            # Decision-time pin is AUTHORITATIVE when a gate exists (E3).
            c["pin_probed"] = dec_pin
        elif not str(c.get("pin_probed") or ""):
            mined = str(c.get("pin") or "")
            if mined:
                c["pin_probed"] = mined
        pool.append(c)
    tree_features = {}
    if args.allocator == "score-v2" and pool:
        # score-v2 uses the committed materialized artifact by default. A
        # caller can still select a writable cache for budgeted live probes.
        cache_path = args.tree_cache or args.tree_features
        tree_features, _calls = materialize_tree_features(
            _http_session() if args.tree_probe_budget > 0 else None,
            pool,
            budget=args.tree_probe_budget,
            cache=TreeCache(cache_path),
        )
    elif args.tree_probe_budget > 0 and pool:
        tree_features, _calls = materialize_tree_features(
            _http_session(),
            pool,
            budget=args.tree_probe_budget,
            cache=TreeCache(args.tree_cache),
        )
    density_hits: dict = {}
    if pool:
        density_hits, _dcalls = materialize_density_hits(
            _http_session() if args.code_search_budget > 0 else None,
            pool,
            budget=args.code_search_budget,
            cache=DensityCache(args.density_cache),
        )
    deny_slugs = set()
    if not args.no_deny_list:
        deny_slugs = load_deny_slugs(args.deny_list)
    ranked = rank_candidates(
        pool,
        allocator=args.allocator,
        tree_features=tree_features,
        deny_slugs=deny_slugs or None,
        density_hits=density_hits or None,
    )
    if args.limit and args.limit > 0:
        ranked = ranked[: args.limit]

    for cand in ranked:
        url = str(cand.get("url") or "")
        pin = str(cand.get("pin_probed") or "")
        tree_feature = tree_features.get((normalize_repo_url(url), pin))
        hits = None
        if density_hits:
            hits = density_hits.get(normalize_repo_url(url), density_hits.get(url))
        total, breakdown = candidate_score(
            cand,
            allocator=args.allocator,
            tree_feature=tree_feature,
            deny_slugs=deny_slugs or None,
            code_search_hits=hits,
        )
        row = {
            "url": cand.get("url"),
            "score": total,
            "score_version": score_version_for_allocator(args.allocator),
            "allocator": args.allocator,
            "breakdown": breakdown,
            "stars": cand.get("stars"),
            "source_query": cand.get("source_query"),
            "pushed_date": cand.get("pushed_date"),
            "status": cand.get("status"),
            "pin": cand.get("pin"),
            "pin_probed": cand.get("pin_probed") or "",
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

#!/usr/bin/env python3
"""Wave 10 (#579): per-source density evidence for target feeds.

Reads committed ``*_gate_decision.json`` + ledger ``source_query`` families.
Does **not** raise ``DAILY_MINE_CAP``. Writes
``properties/generated/feed_density.json``.
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.io_atomic import atomic_write_text  # noqa: E402
from regexproof.mine.exclusions import github_repo_slug, normalize_repo_url  # noqa: E402
from regexproof.mine.feeds import (  # noqa: E402
    FEED_QUERIES,
    OSV_WITNESS_NOTE,
    SITE_MEDIAN_FLOOR,
    SKIP_CLASS_CAP,
    TARGET_QUERY_SHARE,
    daily_cap_unchanged,
    evidence_allows_share,
    median,
    query_share_n,
)
from regexproof.mine.features import _query_family  # noqa: E402
from regexproof.mine.queue import DEFAULT_DAILY_CAP as QUEUE_CAP  # noqa: E402
from regexproof.mine.search import DEFAULT_QUERY_BUDGET  # noqa: E402

GEN = ROOT / "properties" / "generated"
EXEMPLAR_SLUGS = (
    "yara-rules/rules",
    "semgrep/semgrep-rules",
    "coreruleset/coreruleset",
    "corazawaf/coraza-coreruleset",
    "openwrt/luci",
    "openwrt/packages",
    "validatorjs/validator.js",
)


def _decisions() -> list[dict]:
    rows = []
    for path in sorted(GEN.glob("*_gate_decision.json")):
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(doc, dict):
            rows.append(doc)
    return rows


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=GEN / "feed_density.json")
    args = ap.parse_args(argv)

    ledger = json.loads((GEN / "candidate-ledger.json").read_text(encoding="utf-8"))
    by_url: dict[str, dict] = {}
    for cand in ledger.get("candidates") or []:
        url = normalize_repo_url(str(cand.get("url") or ""))
        if url:
            by_url[url] = cand

    fam_sites: dict[str, list[int]] = defaultdict(list)
    exemplars: dict[str, dict] = {}
    for dec in _decisions():
        probe = dec.get("probe") if isinstance(dec.get("probe"), dict) else {}
        related = dec.get("related") if isinstance(dec.get("related"), dict) else {}
        if related.get("probe_failure") or dec.get("probe_failure"):
            continue
        if type(probe.get("regex_sites")) is not int:
            continue
        sites = probe["regex_sites"]
        url = str(dec.get("candidate_url") or "")
        fam = _query_family(str(by_url.get(normalize_repo_url(url), {}).get("source_query") or ""))
        fam_sites[fam].append(sites)
        slug = github_repo_slug(url).lower()
        if slug in EXEMPLAR_SLUGS:
            exemplars[slug] = {
                "regex_sites": sites,
                "status": str(dec.get("status") or dec.get("decision") or ""),
                "url": url,
            }

    families = {}
    medians: dict[str, float] = {}
    for name, xs in sorted(fam_sites.items()):
        med = median(xs)
        if med is not None:
            medians[name] = med
        families[name] = {
            "n": len(xs),
            "median_regex_sites": med,
            "mean_regex_sites": round(sum(xs) / len(xs), 1) if xs else None,
            "frac_gt_200": round(sum(1 for s in xs if s > 200) / len(xs), 6) if xs else None,
            "frac_le50": round(sum(1 for s in xs if s <= SKIP_CLASS_CAP) / len(xs), 6) if xs else None,
        }

    allow = evidence_allows_share(medians)
    share_n = query_share_n(DEFAULT_QUERY_BUDGET) if allow else 0
    art = {
        "schema_version": "1",
        "wave": 10,
        "issue": "#579",
        "site_median_floor": SITE_MEDIAN_FLOOR,
        "target_query_share": TARGET_QUERY_SHARE,
        "query_budget": DEFAULT_QUERY_BUDGET,
        "feed_query_share_n": share_n,
        "live_query_share_applied": allow,
        "daily_cap": daily_cap_unchanged(),
        "osv_witness": {"primary_drain": False, "note": OSV_WITNESS_NOTE},
        "feed_queries": [{"family": fam, "query": q} for fam, q in FEED_QUERIES],
        "families": families,
        "exemplars": {k: exemplars[k] for k in EXEMPLAR_SLUGS if k in exemplars},
        "note": (
            "Generic validators filename queries stay low-density (do not "
            "qualify). Rules-family median clears the skip-class floor, so "
            f"{share_n}/{DEFAULT_QUERY_BUDGET} query slots prepend the Wave 10 "
            "feed list. DAILY_MINE_CAP remains "
            f"{QUEUE_CAP}."
        ),
    }
    text = json.dumps(art, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    out = args.out.expanduser().resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    atomic_write_text(out, text)
    print(
        f"wrote {out} rules_median={medians.get('rules')} share={share_n} "
        f"cap={QUEUE_CAP}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

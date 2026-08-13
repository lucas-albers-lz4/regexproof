#!/usr/bin/env python3
"""Re-measure encodable fractions from FROZEN inventory NDJSON records.

Unlike ``measure-corpus-fraction.py`` (which re-extracts and can silently
fall back to the in-repo sample when the full corpus path is missing), this
consumes a committed inventory verbatim: the extraction is frozen, the
compiler is current. It is the post-compiler-change re-measurement primitive.

Writes ``properties/generated/<corpus>_encodable_fraction.json`` (same schema
as the measure script, plus a ``remeasure`` block with per-record flip counts
and samples). Use ``--dry-run`` to report without writing.

Usage:
  python scripts/remeasure-from-inventory.py --corpus gitleaks
  python scripts/remeasure-from-inventory.py --corpus coreruleset \\
      --inventory properties/generated/crs-inventory.ndjson --dry-run
"""

from __future__ import annotations

import argparse
import json
import platform
import sys
import time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import z3  # noqa: E402

from regexproof.batch.compile_records import compile_records  # noqa: E402
from regexproof.batch.measure import compiler_fingerprint  # noqa: E402
from regexproof.batch.manifests import CORPUS_MANIFESTS  # noqa: E402

OUT = ROOT / "properties" / "generated"

FLIP_SAMPLE_CAP = 10

# Extractor-level rejects persisted as ``compile_reason`` in frozen inventories
# (``unencodable_reason`` is dropped at write time). Restoring them prevents
# recompiling empty-placeholder patterns as encodable (Bugbot / PR #80).
EXTRACTOR_FROZEN_REASONS = frozenset(
    {
        "composite-pattern",
        "multi-match",
    }
)


def _compiler_fingerprint() -> str:
    return compiler_fingerprint()



def load_records(path: Path) -> list[dict]:
    records: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            records.append(json.loads(line))
    return records


def prepare_frozen_records(frozen: list[dict]) -> list[dict]:
    """Restore extractor ``unencodable_reason`` so ``compile_records`` skips them."""
    out: list[dict] = []
    for row in frozen:
        rec = dict(row)
        reason = rec.get("unencodable_reason") or rec.get("compile_reason")
        if reason in EXTRACTOR_FROZEN_REASONS and not rec.get("unencodable_reason"):
            rec["unencodable_reason"] = reason
        out.append(rec)
    return out


def remeasure(
    corpus: str,
    *,
    inventory: Path | None = None,
    dry_run: bool = False,
) -> dict:
    if corpus not in CORPUS_MANIFESTS:
        raise SystemExit(f"unknown corpus: {corpus}")
    meta = dict(CORPUS_MANIFESTS[corpus])
    inv_path = inventory or (OUT / f"{corpus}-inventory.ndjson")
    if not inv_path.exists():
        raise SystemExit(f"inventory missing: {inv_path}")
    frozen = load_records(inv_path)
    records = prepare_frozen_records(frozen)

    t0 = time.perf_counter()
    compiled = compile_records(
        records,
        lift_inline=bool(meta.get("lift_inline")),
        corpus_slug=corpus,
    )
    wall = time.perf_counter() - t0
    rows = [pair[0] for pair in compiled]

    frozen_enc = {r.get("regex_id"): bool(r.get("encodable")) for r in frozen}
    now_enc = {c.get("regex_id"): bool(c.get("encodable")) for c in rows}
    ids = [r.get("regex_id") for r in frozen if r.get("regex_id")]
    flips = [
        rid
        for rid in ids
        if rid in frozen_enc and rid in now_enc and frozen_enc[rid] != now_enc[rid]
    ]
    now_encodable = [rid for rid in flips if now_enc[rid]]
    now_rejected = [rid for rid in flips if not now_enc[rid]]
    # Baseline for the remeasure block = frozen inventory (not a prior artifact,
    # which may itself be a corrupted earlier remeasure).
    baseline_encodable = sum(1 for r in frozen if r.get("encodable"))
    baseline_n = len(frozen) or 1
    baseline_fraction = round(baseline_encodable / baseline_n, 4)

    def _samples(rids: list[str]) -> list[dict]:
        by_id = {c.get("regex_id"): c for c in rows}
        out = []
        for rid in rids[:FLIP_SAMPLE_CAP]:
            c = by_id.get(rid, {})
            out.append(
                {
                    "regex_id": rid,
                    "site": c.get("site"),
                    "pattern": c.get("pattern"),
                    "flags": c.get("flags") or "",
                    "reason": c.get("compile_reason"),
                }
            )
        return out

    reasons = Counter((c.get("compile_reason") or "ok") for c in rows)
    enc = sum(1 for c in rows if c.get("encodable"))
    n = len(rows) or 1
    fraction = enc / n
    decision = "go" if fraction >= 0.30 else "no-go"
    unclassified = reasons.get("parse-error", 0)

    # Prior fraction from the committed artifact, when present.
    art_path = OUT / f"{corpus}_encodable_fraction.json"
    prior = None
    if art_path.exists():
        try:
            prior = json.loads(art_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            prior = None

    report = {
        "schema_version": "1",
        "pilot": corpus,
        "scope": (prior or {}).get("scope", "frozen_inventory"),
        "corpus_pin": meta.get("corpus_pin"),
        "commit": meta.get("commit"),
        "compiler_fingerprint": _compiler_fingerprint(),
        "dialect": meta.get("dialect"),
        "sample_size": len(rows),
        "encodable": enc,
        "fraction": round(fraction, 4),
        "go_no_go_threshold": 0.3,
        "decision": decision,
        "decision_rule": "go iff encodable/sample_size >= 0.3",
        "reasons": dict(sorted(reasons.items())),
        "unclassified_parse_errors": unclassified,
        "complete_run": True,
        "wall_s": round(wall, 3),
        "budget": meta.get("budget"),
        "inventory_path": (
            str(inv_path.relative_to(ROOT)) if inv_path.is_relative_to(ROOT) else str(inv_path)
        ),
        "engine_versions": {
            "python": platform.python_version(),
            "z3": z3.get_version_string(),
        },
        "remeasure": {
            "from": "frozen_inventory",
            "baseline_fraction": baseline_fraction,
            "baseline_encodable": baseline_encodable,
            "prior_artifact_fraction": (prior or {}).get("fraction"),
            "prior_artifact_encodable": (prior or {}).get("encodable"),
            "prior_compiler_fingerprint": (prior or {}).get("compiler_fingerprint"),
            "flips": {
                "now_encodable": len(now_encodable),
                "now_rejected": len(now_rejected),
                "unchanged": len(ids) - len(flips),
            },
            "samples": {
                "now_encodable": _samples(now_encodable),
                "now_rejected": _samples(now_rejected),
            },
        },
    }
    if unclassified:
        report["decision_note"] = (
            f"{unclassified} unclassified parse-error rows — Phase 1 requires zero"
        )

    if not dry_run:
        OUT.mkdir(parents=True, exist_ok=True)
        art_path.write_text(
            json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    flips_summary = (
        f"flips: +{len(now_encodable)}/-{len(now_rejected)}"
        if flips
        else "flips: none"
    )
    prior_frac = (
        f" (frozen {baseline_fraction}; prior-artifact {prior.get('fraction')})"
        if prior
        else f" (frozen {baseline_fraction})"
    )
    print(
        f"{corpus}: {enc}/{len(rows)} = {fraction:.4f}{prior_frac} "
        f"decision={decision} {flips_summary} parse-error={unclassified} "
        f"wall={wall:.1f}s{' [dry-run]' if dry_run else ''}"
    )
    return report


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--corpus", required=True, choices=sorted(CORPUS_MANIFESTS))
    ap.add_argument(
        "--inventory",
        type=Path,
        help="inventory NDJSON (default: properties/generated/<corpus>-inventory.ndjson)",
    )
    ap.add_argument("--dry-run", action="store_true", help="report only, write nothing")
    args = ap.parse_args(argv)
    remeasure(args.corpus, inventory=args.inventory, dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

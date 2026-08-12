#!/usr/bin/env python3
"""Reconcile probe per-file counts against the registered extractor (P3-B).

Post-P2.5, the P1 script extracts via the REGISTERED extractor (P2c
migration), so the reconciliation compares the P3-A FROZEN probe export
(pre-P2 capture semantics) against a fresh final-semantics export of the
same tree, PER FILE, with a tolerance percentage:

    |probe_file - now_file| / probe_file  <= tolerance_pct/100

The per-file tolerance report is COMMITTED (the P3 deliverable — the plan's
reconcile step).  Exit codes: 0 = within tolerance; 1 = ≥1 file over
tolerance (the report still writes — the over-tolerance files are the
documented record; the probe doc marks the final-semantics count
authoritative when the guard fixes removed phantoms).

Usage:
    python scripts/reconcile_probe.py --probe-ndjson FROZEN.ndjson \
        --now-ndjson FRESH.ndjson --tolerance-pct 10 -o REPORT.json
"""

from __future__ import annotations

import argparse
import json
import math as _math
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _finite_percent(value: str) -> float:
    """argparse type: finite tolerance percent in (0, 100] — nan/inf/0/out-of-
    range must not fail open (a nan comparison is always False)."""
    try:
        pct = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"not a number: {value!r}")
    if not _math.isfinite(pct) or not (0 < pct <= 100.0):
        raise argparse.ArgumentTypeError(
            f"tolerance must be a finite value in (0, 100]: {value!r}")
    return pct


def _per_file_counts(ndjson_path: Path) -> dict[str, int]:
    counts: Counter[str] = Counter()
    for line in ndjson_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        counts[rec.get("file") or ""] += 1
    return dict(sorted(counts.items()))


def reconcile_per_file(
    probe_counts: dict[str, int],
    now_counts: dict[str, int],
    tolerance_pct: float = 10.0,
) -> tuple[dict, list[str]]:
    """Per-file delta report + the list of over-tolerance files."""
    report: dict[str, dict] = {}
    violations: list[str] = []
    for rel in sorted(set(probe_counts) | set(now_counts)):
        p, n = probe_counts.get(rel, 0), now_counts.get(rel, 0)
        # Plan denominator: |probe - extractor| / probe (plan.md:535) — the
        # probe count is the evidence being validated. A probe undercount of
        # 11% (90 vs 100) must FAIL a 10% tolerance.
        delta = abs(p - n) / p if p else (1.0 if n else 0.0)
        over = delta > tolerance_pct / 100.0
        report[rel] = {"probe": p, "registered": n,
                       "delta_pct": round(delta * 100.0, 2), "over": over}
        if over:
            violations.append(rel)
    return report, violations


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="reconcile_probe.py",
        description="Per-file probe-count reconciliation vs the registered "
                    "extractor (P3-B); committed tolerance report.",
    )
    ap.add_argument("--probe-ndjson", required=True, metavar="FROZEN.ndjson",
                    help="P3-A frozen probe export (P1 --dir --ndjson)")
    ap.add_argument("--now-ndjson", required=True, metavar="FRESH.ndjson",
                    help="fresh final-semantics export of the same tree")
    ap.add_argument("--tolerance-pct", type=_finite_percent, default=10.0,
                    help="per-file tolerance percent (default 10; must be a "
                         "finite value in (0, 100])")
    ap.add_argument("-o", "--output", required=True, metavar="REPORT.json")
    args = ap.parse_args(argv)

    probe = _per_file_counts(Path(args.probe_ndjson))
    now = _per_file_counts(Path(args.now_ndjson))
    report, violations = reconcile_per_file(
        probe, now, tolerance_pct=args.tolerance_pct)
    summary = {
        "probe_files": len(probe), "registered_files": len(now),
        "over_tolerance_files": len(violations),
        "over_tolerance_pct": round(
            len(violations) / max(len(set(probe) | set(now)), 1) * 100.0, 2),
    }
    out = {"schema_version": "1", "corpus": "openwrt_packages",
           "probe_ndjson": str(Path(args.probe_ndjson).name),
           "now_ndjson": str(Path(args.now_ndjson).name),
           "tolerance_pct": args.tolerance_pct,
           "summary": summary, "per_file": report}
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n",
                        encoding="utf-8")
    print(f"reconcile -> {out_path}: {summary}")
    return 1 if violations else 0


if __name__ == "__main__":
    raise SystemExit(main())

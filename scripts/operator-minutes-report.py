#!/usr/bin/env python3
"""Report seeded and measured admission operator-minutes separately."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.mine.operator_minutes import LOG_PATH, summarize  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--log", type=Path, default=LOG_PATH, help="operator minutes JSONL")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    parser.add_argument(
        "--rollout-cutoff-date",
        help="evidence-backed YYYY-MM-DD cutoff for period comparison (omitted = unclassified)",
    )
    parser.add_argument(
        "--rollout-cutoff-evidence",
        help="reference supporting the assumed cutoff, such as an ops record or run artifact",
    )
    args = parser.parse_args(argv)
    if bool(args.rollout_cutoff_date) != bool(args.rollout_cutoff_evidence):
        parser.error("--rollout-cutoff-date and --rollout-cutoff-evidence must be supplied together")
    try:
        report = summarize(
            args.log,
            rollout_cutoff_date=args.rollout_cutoff_date,
            rollout_cutoff_evidence=args.rollout_cutoff_evidence,
        )
    except ValueError as exc:
        parser.error(str(exc))
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
        return 0

    provenance = report["provenance"]
    print(
        "operator-minutes evidence: "
        f"{provenance['seed_records']} seeded rows, "
        f"{provenance['stopwatch_active_samples']} measured active samples"
    )
    for name in ("pre_cutoff", "post_cutoff", "unclassified"):
        period = report["periods"][name]
        active = period["active_minutes"]
        print(
            f"{name}: records={period['records']} "
            f"seed={period['seed_records']} stopwatch={period['stopwatch_records']} "
            f"active_n={active['n']} active_median={active['median']} "
            f"active_mean={active['mean']}"
        )
    comparison = report["pre_post_active_ratio"]
    if comparison["ratio"] is None:
        print(f"pre/post active-time ratio: unavailable ({comparison['reason']})")
    else:
        print(
            "pre/post active-time ratio (conditional on the operator-supplied "
            f"cutoff): {comparison['ratio']:.3f}x"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

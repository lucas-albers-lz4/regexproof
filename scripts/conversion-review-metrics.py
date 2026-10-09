#!/usr/bin/env python3
"""Summarize stopwatch measurements for human conversion-wave reviews."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.mine.conversion_review_minutes import (  # noqa: E402
    ConversionReviewError,
    LOG_PATH,
    summarize,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--log",
        type=Path,
        default=LOG_PATH,
        help="measurement log (default: properties/generated/conversion_review_minutes.jsonl)",
    )
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = parser.parse_args(argv)
    try:
        report = summarize(args.log)
    except (OSError, ConversionReviewError) as exc:
        print(f"conversion-review-metrics: error: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
        return 0
    if not report["waves"]:
        print("No conversion review stopwatch rows recorded yet.")
        return 0
    print("conversion review active time (median primary; skipped sites included)")
    for wave in report["waves"]:
        active = wave["active_minutes"]
        rate = wave["contracts_adopted_per_active_hour"]
        rate_text = f"{rate:.3f}" if rate is not None else "n/a"
        skip_reasons = {
            outcome.removeprefix("skipped_"): count
            for outcome, count in wave["outcome_counts"].items()
            if outcome.startswith("skipped_")
        }
        skip_text = ",".join(
            f"{reason}:{count}" for reason, count in skip_reasons.items()
        ) or "none"
        print(
            f"{wave['corpus']} / {wave['wave_id']} / {wave['idiom_bucket']}: "
            f"pin={wave['pin']} "
            f"reviewed={wave['reviewed_sites']} contracted={wave['contracted_sites']} "
            f"skipped={wave['skipped_sites']} skip_reasons={skip_text} "
            f"active_min_median={active['median']} "
            f"active_min_mean={active['mean']} active_min_total={active['total']} "
            f"contracts_per_active_hour={rate_text}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

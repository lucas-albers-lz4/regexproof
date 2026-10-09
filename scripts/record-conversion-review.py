#!/usr/bin/env python3
"""Record active time for one completed conversion-wave site review.

Start a stopwatch when opening the ranked site context. Stop after adopting a
human contract or recording a skip. Include skipped sites so the metric
reflects the reading cost of the whole rank-15 shortlist.

Example::

  python3 scripts/record-conversion-review.py \
    --corpus forge-cli --pin 0123456789abcdef0123456789abcdef01234567 \
    --wave-id forge-cli_w2 --idiom-bucket x-api-key-persistence \
    --site src/config.py:42:API_KEY_RE --rank 3 --outcome contracted \
    --question-id no-raw-secret --active-minutes 11.5
"""

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
    append_row,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--pin", required=True, help="40-char lowercase source SHA")
    parser.add_argument("--wave-id", required=True)
    parser.add_argument("--idiom-bucket", required=True)
    parser.add_argument("--site", required=True, help="ranked source site")
    parser.add_argument("--rank", required=True, type=int, help="rank 1 through 15")
    parser.add_argument(
        "--outcome",
        required=True,
        choices=(
            "contracted",
            "skipped_unreachable",
            "skipped_out_of_scope",
            "skipped_no_response",
            "skipped_duplicate",
        ),
    )
    parser.add_argument("--active-minutes", required=True, type=float)
    parser.add_argument("--question-id", help="required for --outcome contracted")
    parser.add_argument(
        "--log",
        type=Path,
        help="override the default properties/generated/conversion_review_minutes.jsonl",
    )
    args = parser.parse_args(argv)
    try:
        row = append_row(
            corpus=args.corpus,
            pin=args.pin,
            wave_id=args.wave_id,
            idiom_bucket=args.idiom_bucket,
            site=args.site,
            rank=args.rank,
            outcome=args.outcome,
            active_minutes=args.active_minutes,
            question_id=args.question_id,
            path=args.log,
        )
    except ConversionReviewError as exc:
        print(f"record-conversion-review: error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(row, sort_keys=True, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

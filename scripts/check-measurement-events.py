#!/usr/bin/env python3
"""Validate a frozen-cohort-bound processing-event log and print JSON.

The checker is deliberately read-only. It requires ``--cohort`` because event
format validity alone is not evidence that a log belongs to the measured
cohort. The cohort file must be the digest-bearing output of PR2.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.mine.measurement_events import (  # noqa: E402
    DEFAULT_LOG_PATH,
    MeasurementEventError,
    summarize,
)
from regexproof.mine.cohort_manifest import CohortManifestError, load_frozen_manifest  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        default=DEFAULT_LOG_PATH,
        help="measurement JSONL path (default: properties/generated/measurement_events.jsonl)",
    )
    parser.add_argument(
        "--cohort",
        required=True,
        type=Path,
        help="PR2 frozen cohort manifest (required for identity binding)",
    )
    args = parser.parse_args(argv)
    try:
        cohort = load_frozen_manifest(args.cohort)
        result = summarize(args.path, cohort)
    except (CohortManifestError, MeasurementEventError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

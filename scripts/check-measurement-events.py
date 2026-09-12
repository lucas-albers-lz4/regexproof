#!/usr/bin/env python3
"""Validate the separate saturation processing-event log and print JSON."""

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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        default=DEFAULT_LOG_PATH,
        help="measurement JSONL path (default: properties/generated/measurement_events.jsonl)",
    )
    args = parser.parse_args(argv)
    try:
        result = summarize(args.path)
    except (MeasurementEventError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

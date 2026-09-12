#!/usr/bin/env python3
"""Report product conversion from a strict frozen-cohort checkpoint.

The input root object is exactly ``schema_version``, ``cohort_id``,
``manifest_digest``, embedded PR2 ``cohort``, and ``rows``.  Rows require a
human contract and explicit ground-truth/disposition status.  Rule-diff,
synthesized, classification, mutation, and agent-derived rows are rejected
from this product checkpoint.  The command is read-only and exits 2 for an
invalid artifact.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.mine.conversion_checkpoint import (  # noqa: E402
    ConversionCheckpointError,
    dumps_report,
    report_from_path,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("checkpoint", type=Path, help="path to the JSON conversion checkpoint")
    args = parser.parse_args(argv)
    try:
        report = report_from_path(args.checkpoint)
    except ConversionCheckpointError as exc:
        print(f"conversion-checkpoint: error: {exc}", file=sys.stderr)
        return 2
    sys.stdout.write(dumps_report(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

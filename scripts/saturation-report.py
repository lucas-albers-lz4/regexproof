#!/usr/bin/env python3
"""Emit a deterministic, read-only saturation report from a cohort manifest.

Manifest schema (JSON):

  {
    "schema_version": "1",
    "repos": [
      {
        "repo_id": "owner/repo",
        "dialect_family": "py_re",
        "sites": 100,
        "novel_sites": 2,
        "new_reject_buckets": [],
        "properties_asked": 10,
        "properties_sat": 2,
        "properties_ground_truthed": 2,
        "properties_filed": 1,
        "properties_accepted": 0
      }
    ]
  }

  The ``repos`` list is ordered.  Each repo carries pinned ``url``/``pin``
  identity and a ``product_properties`` list. For every dialect family, ``compiler_stop``
is true only when the last two repos both have novelty strictly below 0.03 and
both have no new reject buckets.  All count fields are non-negative JSON
integers; a repo must have at least one site.  The product and target
denominators are total ``properties_asked`` and are compared with 50 and 100.
Rates are emitted as canonical decimal strings so repeated runs are byte
stable.  The command never writes the manifest or any other file.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.mine.saturation import ManifestError, dumps_report, report_from_path  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("manifest", type=Path, help="path to the JSON cohort manifest")
    args = parser.parse_args(argv)
    try:
        report = report_from_path(args.manifest)
    except ManifestError as exc:
        print(f"saturation-report: error: {exc}", file=sys.stderr)
        return 2
    sys.stdout.write(dumps_report(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

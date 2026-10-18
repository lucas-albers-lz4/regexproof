#!/usr/bin/env python3
"""Freeze adopted product identities before recording proof outcomes."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from regexproof.mine.conversion_checkpoint import (  # noqa: E402
    ConversionCheckpointError,
    build_product_roster,
)
from regexproof.mine.cohort_manifest import validate_manifest  # noqa: E402
from regexproof.io_atomic import atomic_write_text  # noqa: E402


def _read_contracts(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        rows = []
        for index, line in enumerate(text.splitlines(), 1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{index}: invalid JSON: {exc.msg}") from exc
        return rows
    if not isinstance(value, list):
        raise ValueError("contract input must be a JSON array or NDJSON rows")
    return value


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cohort", type=Path, required=True)
    parser.add_argument("--contracts", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        cohort = validate_manifest(json.loads(args.cohort.read_text(encoding="utf-8")))
        contracts = _read_contracts(args.contracts)
        roster = build_product_roster(contracts, cohort)
        atomic_write_text(
            args.out,
            json.dumps(roster, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
        )
    except (OSError, ValueError, ConversionCheckpointError) as exc:
        print(f"freeze-product-roster: error: {exc}", file=sys.stderr)
        return 2
    print(
        f"frozen {len(roster['identities'])} contract identities "
        f"for {roster['cohort_id']} ({roster['coverage_digest']})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Fit the deterministic score-v2 allocator from P6 gate labels.

The default run is offline and reads only the committed gate-label artifact.
It writes the reviewable weight artifact and prints a JSON report containing
the dev mapping decision, holdout gate, and v1-feature ablation.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.io_atomic import atomic_write_text
from regexproof.mine.score_v2 import DEFAULT_FIT_DATE, DEFAULT_SEED, fit_report, format_report


def _load_rows(path: Path) -> list[dict[str, Any]]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or not isinstance(value.get("rows"), list):
        raise ValueError("gate-label artifact must contain a rows list")
    rows = [row for row in value["rows"] if isinstance(row, dict)]
    if len(rows) != len(value["rows"]):
        raise ValueError("gate-label artifact contains a non-object row")
    return rows


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--labels",
        type=Path,
        default=ROOT / "properties" / "generated" / "gate-labels.json",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "regexproof" / "mine" / "score_v2_weights.json",
    )
    # P8 (luna gate 1): the seed is PINNED (plan D3: "seed pinned in the
    # script") — an override would allow non-reproducible committed weights.
    parser.add_argument(
        "--seed", type=int, default=DEFAULT_SEED, choices=[DEFAULT_SEED],
        help="Pinned deterministic seed (plan D3; not overrideable).",
    )
    parser.add_argument(
        "--fit-date",
        default=DEFAULT_FIT_DATE.isoformat(),
        help=f"As-of date for recency features (default: {DEFAULT_FIT_DATE.isoformat()}).",
    )
    parser.add_argument(
        "--fail-on-gate",
        action="store_true",
        help="Return non-zero when a blocking ship-gate condition fails.",
    )
    args = parser.parse_args(argv)
    labels = args.labels.expanduser().resolve()
    output = args.output.expanduser().resolve()
    if not labels.is_file():
        print(f"error: labels not found: {labels}", file=sys.stderr)
        return 2
    try:
        artifact = fit_report(_load_rows(labels), seed=args.seed, fit_date=args.fit_date)
    except (OSError, ValueError, TypeError, AssertionError, json.JSONDecodeError) as exc:
        print(f"error: score-v2 fit failed: {exc}", file=sys.stderr)
        return 2
    text = json.dumps(artifact, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    atomic_write_text(output, text)
    print(json.dumps(format_report(artifact), sort_keys=True, ensure_ascii=False))
    gate = artifact.get("evaluation", {}).get("gate", {})
    if args.fail_on_gate and not (
        (gate.get("label_reproduction_auc_ge_0_70") or gate.get("holdout_auc_ge_0_70"))
        and gate.get("ablation_beats_v1_features")
    ):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Fit the deterministic score-v2 allocator from P6 gate labels.

The default run is offline and reads only the committed gate-label artifact.
It writes the reviewable weight artifact and prints a JSON report containing
the dev mapping decision, holdout gate, and v1-feature ablation.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
LABELS_REPO_PATH = "properties/generated/gate-labels.json"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.io_atomic import atomic_write_text  # noqa: E402  # ROOT bootstrap above
from regexproof.mine.score_v2 import DEFAULT_FIT_DATE, DEFAULT_SEED, fit_report, format_report  # noqa: E402  # ROOT bootstrap above


def _load_rows(path: Path) -> list[dict[str, Any]]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or not isinstance(value.get("rows"), list):
        raise ValueError("gate-label artifact must contain a rows list")
    rows = [row for row in value["rows"] if isinstance(row, dict)]
    if len(rows) != len(value["rows"]):
        raise ValueError("gate-label artifact contains a non-object row")
    return rows


def _fit_source_commit(rows: list[dict[str, Any]], requested: str | None) -> str:
    ref = requested or "HEAD"
    result = subprocess.run(
        ["git", "rev-parse", "--verify", f"{ref}^{{commit}}"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        detail = result.stderr.strip() or result.stdout.strip()
        raise ValueError(f"cannot resolve fit-source commit {ref!r}: {detail}")
    commit = result.stdout.strip()
    snapshot = subprocess.run(
        ["git", "show", f"{commit}:{LABELS_REPO_PATH}"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if snapshot.returncode:
        detail = snapshot.stderr.strip() or snapshot.stdout.strip()
        raise ValueError(f"cannot read fit-source gate labels at {commit}: {detail}")
    try:
        value = json.loads(snapshot.stdout)
    except json.JSONDecodeError as exc:
        raise ValueError(f"fit-source gate labels at {commit} are invalid JSON") from exc
    if not isinstance(value, dict) or value.get("rows") != rows:
        raise ValueError(
            "fit input rows must exactly match the committed gate-label rows at "
            f"{commit}; commit labels before fitting"
        )
    return commit


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
        "--fit-source-commit",
        help="Commit containing the exact gate-label rows used for this fit (default: HEAD).",
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
        rows = _load_rows(labels)
        source_commit = _fit_source_commit(rows, args.fit_source_commit)
        artifact = fit_report(rows, seed=args.seed, fit_date=args.fit_date)
        artifact["training"]["fit_source_commit"] = source_commit
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

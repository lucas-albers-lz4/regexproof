#!/usr/bin/env python3
"""Verify the score-v2 fit cadence without refitting on every small append."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from regexproof.mine.score_v2 import DEFAULT_SEED, fit_report  # noqa: E402
from regexproof.mine.score_v2_gate import check_score_v2_artifact_cadence  # noqa: E402

LABELS_PATH = "properties/generated/gate-labels.json"
WEIGHTS_PATH = "regexproof/mine/score_v2_weights.json"


def _git_text(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, capture_output=True, check=False
    )
    if result.returncode:
        detail = result.stderr.strip() or result.stdout.strip()
        raise ValueError(f"git {' '.join(args)} failed: {detail}")
    return result.stdout


def _json_object(raw: str, label: str) -> dict[str, Any]:
    value = json.loads(raw)
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be a JSON object")
    return value


def _rows(value: dict[str, Any], label: str) -> list[dict[str, Any]]:
    rows = value.get("rows")
    if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
        raise ValueError(f"{label} must contain an object rows list")
    return rows


def _resolve_source_sha(value: str) -> str:
    candidate = (value or "").strip()
    if not candidate:
        raise ValueError("score-v2 weights lack training.fit_source_commit")
    try:
        _git_text("cat-file", "-e", f"{candidate}^{{commit}}")
    except ValueError:
        _git_text("fetch", "--depth", "1", "origin", candidate)
        _git_text("cat-file", "-e", f"{candidate}^{{commit}}")
    return _git_text("rev-parse", f"{candidate}^{{commit}}").strip()


def _load_snapshot(commit: str, path: str, label: str) -> dict[str, Any]:
    return _json_object(_git_text("show", f"{commit}:{path}"), label)


def main(argv: list[str] | None = None) -> int:
    argparse.ArgumentParser(description=__doc__).parse_args(argv)
    try:
        current_labels = _json_object(
            (ROOT / LABELS_PATH).read_text(encoding="utf-8"), "current gate labels"
        )
        current_weights = _json_object(
            (ROOT / WEIGHTS_PATH).read_text(encoding="utf-8"), "current score-v2 weights"
        )
        current_rows = _rows(current_labels, "current gate labels")
        training = current_weights.get("training")
        if not isinstance(training, dict):
            raise ValueError("score-v2 weights lack a training object")
        if training.get("seed") != DEFAULT_SEED:
            raise ValueError("score-v2 training seed does not match the pinned seed")
        fit_date = training.get("fit_date")
        if not isinstance(fit_date, str) or not fit_date.strip():
            raise ValueError("score-v2 weights lack training.fit_date")
        source_sha = _resolve_source_sha(str(training.get("fit_source_commit") or ""))
        source_labels = _load_snapshot(source_sha, LABELS_PATH, "fit-source gate labels")
        source_rows = _rows(source_labels, "fit-source gate labels")
        expected_source = fit_report(
            source_rows, seed=DEFAULT_SEED, fit_date=fit_date
        )
        expected_source["training"]["fit_source_commit"] = source_sha
    except (OSError, ValueError, TypeError, AssertionError, json.JSONDecodeError) as exc:
        print(f"score-v2 cadence check failed: {exc}", file=sys.stderr)
        return 2

    passed, detail = check_score_v2_artifact_cadence(
        source_rows=source_rows,
        current_rows=current_rows,
        current_weights=current_weights,
        expected_source_weights=expected_source,
    )
    outcome = "pass" if passed else "fail"
    print(f"score-v2 cadence check {outcome}: {detail}")
    if not passed:
        print(
            "Refresh score_v2_weights.json from the current labels when prior rows "
            "change or append-only growth reaches 20%.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

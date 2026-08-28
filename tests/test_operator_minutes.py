"""Wave 6 (#575): operator-minutes log."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from regexproof.mine.operator_minutes import append_row, load_rows, summarize

ROOT = Path(__file__).resolve().parent.parent
COMMITTED = ROOT / "properties" / "generated" / "operator_minutes.jsonl"
FREEZE = ROOT / "properties" / "generated" / "phase0_freeze.json"


def test_committed_baseline_has_at_least_five_rows():
    rows = load_rows(COMMITTED)
    assert len(rows) >= 5
    assert all(r["decision"] in ("go", "triage-trial") for r in rows)
    assert all(r["measurement_id"] for r in rows)
    s = summarize(COMMITTED)
    assert s["baseline_floor_met"] is True
    assert s["active_minutes"]["n"] == 0  # seed rows have no stopwatch yet


def test_append_stopwatch_row(tmp_path: Path):
    log = tmp_path / "m.jsonl"
    row = append_row(
        url="https://github.com/x/y",
        pin="a" * 40,
        decision="go",
        source="stopwatch",
        active_minutes=4.5,
        path=log,
    )
    assert row["active_minutes"] == 4.5
    assert row["wall_minutes"] is None
    loaded = load_rows(log)
    assert len(loaded) == 1
    s = summarize(log)
    assert s["active_minutes"]["median"] == 4.5
    assert s["wall_minutes"]["median"] is None


def test_stopwatch_rows_get_fresh_measurement_ids(tmp_path: Path):
    log = tmp_path / "m.jsonl"
    first = append_row(
        url="https://github.com/x/y", pin="a" * 40, decision="go",
        source="stopwatch", active_minutes=4.5, path=log,
    )
    second = append_row(
        url="https://github.com/x/y", pin="a" * 40, decision="go",
        source="stopwatch", active_minutes=9.0, path=log,
    )
    assert second["measurement_id"] != first["measurement_id"]
    assert len(load_rows(log)) == 2
    log = tmp_path / "m.jsonl"
    with pytest.raises(SystemExit, match="not a human-reviewed survivor"):
        append_row(
            url="https://x/y", pin="a" * 40, decision="no-go",
            source="stopwatch", path=log,
        )
    with pytest.raises(SystemExit, match="finite"):
        append_row(
            url="https://x/y", pin="a" * 40, decision="go",
            source="stopwatch", active_minutes=float("nan"), path=log,
        )
    with pytest.raises(SystemExit, match="finite"):
        append_row(
            url="https://x/y", pin="a" * 40, decision="go",
            source="stopwatch", active_minutes=-1, path=log,
        )
    with pytest.raises(SystemExit, match="40-char"):
        append_row(
            url="https://x/y", pin="", decision="go",
            source="stopwatch", active_minutes=1, path=log,
        )


def test_does_not_touch_freeze():
    before = FREEZE.read_bytes()
    assert json.loads(before)["dataset"]["n"] == 874
    # Loading/summarizing the minutes log must not rewrite the freeze.
    summarize(COMMITTED)
    assert FREEZE.read_bytes() == before

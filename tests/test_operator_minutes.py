"""Wave 6 (#575): operator-minutes log."""

from __future__ import annotations

import json
from datetime import date, datetime
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
    assert json.loads(before)["dataset"]["n"] == 875
    # Loading/summarizing the minutes log must not rewrite the freeze.
    summarize(COMMITTED)
    assert FREEZE.read_bytes() == before


def test_report_uses_only_stopwatch_samples_for_pre_post_speedup(tmp_path: Path):
    log = tmp_path / "m.jsonl"
    rows = [
        {
            "source": "seed-artifact-timestamps",
            "decision": "go",
            "decision_date": "2026-08-13",
            "active_minutes": None,
            "wall_minutes": None,
        },
        {
            "source": "stopwatch",
            "decision": "go",
            "decision_date": "2026-08-20",
            "active_minutes": 20.0,
            "wall_minutes": 50.0,
        },
        {
            "source": "stopwatch",
            "decision": "triage-trial",
            "decision_date": "2026-08-27",
            "active_minutes": 5.0,
            "wall_minutes": None,
        },
        {
            "source": "stopwatch",
            "decision": "go",
            "decision_date": "2026-08-24",
            "active_minutes": 100.0,
            "wall_minutes": None,
        },
        {
            "source": "stopwatch",
            "decision": "go",
            "decision_date": "2026-08-23",
            "active_minutes": 100.0,
        },
        {
            "source": "stopwatch",
            "decision": "go",
            "decision_date": "2026-08-25",
            "active_minutes": 100.0,
        },
    ]
    log.write_text("\n".join(json.dumps(row) for row in rows) + "\n")

    report = summarize(
        log,
        rollout_cutoff_date="2026-08-24",
        rollout_cutoff_evidence="test fixture rollout record",
    )

    assert report["baseline_floor_met"] is True
    assert report["provenance"]["seed_records"] == 1
    assert report["provenance"]["stopwatch_records"] == 5
    assert report["provenance"]["stopwatch_active_samples"] == 5
    assert report["provenance"]["period_cutoff_is_operator_assumption"] is True
    assert report["provenance"]["period_cutoff_evidence"] == "test fixture rollout record"
    assert report["periods"]["pre_cutoff"]["seed_records"] == 1
    assert report["periods"]["pre_cutoff"]["active_minutes"]["median"] == 20.0
    assert report["periods"]["post_cutoff"]["active_minutes"]["median"] == 5.0
    assert report["periods"]["unclassified"]["active_minutes"]["n"] == 3
    assert report["pre_post_active_ratio"] == {
        "ratio": 4.0,
        "status": "measured",
        "interpretation": "active_time_ratio_conditional_on_operator_cutoff",
    }


def test_speedup_is_unavailable_without_measured_pre_and_post_samples(tmp_path: Path):
    log = tmp_path / "m.jsonl"
    seed_rows = [
        {
            "source": "seed-artifact-timestamps",
            "decision": "go",
            "decision_date": "2026-08-13",
            "active_minutes": None,
        }
        for _ in range(5)
    ]
    log.write_text("\n".join(json.dumps(row) for row in seed_rows) + "\n")
    report = summarize(log)
    assert report["baseline_floor_met"] is True
    assert report["provenance"]["seed_records"] == 5
    assert report["provenance"]["stopwatch_active_samples"] == 0
    assert report["periods"]["unclassified"]["records"] == 5
    assert report["pre_post_active_ratio"]["ratio"] is None
    assert report["pre_post_active_ratio"]["status"] == "insufficient_measured_samples"


def test_cutoff_requires_evidence(tmp_path: Path):
    with pytest.raises(ValueError, match="evidence reference is required"):
        summarize(tmp_path / "m.jsonl", rollout_cutoff_date="2026-08-24")


@pytest.mark.parametrize(
    "cutoff", [datetime(2026, 8, 24), "20260824", "2026-08-24T00:00:00"]
)
def test_cutoff_rejects_datetime_and_noncanonical_date_strings(tmp_path: Path, cutoff):
    with pytest.raises(ValueError, match="rollout_cutoff_date"):
        summarize(
            tmp_path / "m.jsonl",
            rollout_cutoff_date=cutoff,
            rollout_cutoff_evidence="test fixture rollout record",
        )


def test_cutoff_accepts_date_object(tmp_path: Path):
    report = summarize(
        tmp_path / "m.jsonl",
        rollout_cutoff_date=date(2026, 8, 24),
        rollout_cutoff_evidence="test fixture rollout record",
    )
    assert report["provenance"]["period_cutoff_date"] == "2026-08-24"


def test_zero_post_median_does_not_emit_infinite_speedup(tmp_path: Path):
    log = tmp_path / "m.jsonl"
    rows = [
        {
            "source": "stopwatch",
            "decision": "go",
            "decision_date": "2026-08-20",
            "active_minutes": 2.0,
        },
        {
            "source": "stopwatch",
            "decision": "go",
            "decision_date": "2026-08-27",
            "active_minutes": 0.0,
        },
    ]
    log.write_text("\n".join(json.dumps(row) for row in rows) + "\n")
    report = summarize(
        log,
        rollout_cutoff_date="2026-08-24",
        rollout_cutoff_evidence="test fixture rollout record",
    )
    assert report["pre_post_active_ratio"]["ratio"] is None
    assert report["pre_post_active_ratio"]["status"] == "undefined_zero_post_median"


def test_large_finite_samples_produce_strict_json(tmp_path: Path):
    log = tmp_path / "m.jsonl"
    rows = [
        {"source": "stopwatch", "decision": "go", "decision_date": "2026-08-20",
         "active_minutes": 1e308, "wall_minutes": 1e308},
        {"source": "stopwatch", "decision": "go", "decision_date": "2026-08-20",
         "active_minutes": 1e308, "wall_minutes": 1e308},
        {"source": "stopwatch", "decision": "go", "decision_date": "2026-08-27",
         "active_minutes": 5e-324},
    ]
    log.write_text("\n".join(json.dumps(row) for row in rows) + "\n")
    report = summarize(log, rollout_cutoff_date="2026-08-24", rollout_cutoff_evidence="fixture")
    assert report["periods"]["pre_cutoff"]["active_minutes"]["median"] == 1e308
    assert report["wall_minutes"]["median"] == 1e308
    assert report["pre_post_active_ratio"]["status"] == "undefined_ratio_overflow"
    assert report["pre_post_active_ratio"]["ratio"] is None
    json.dumps(report, allow_nan=False)


def test_positive_ratio_underflow_is_not_reported_as_zero(tmp_path: Path):
    log = tmp_path / "m.jsonl"
    rows = [
        {"source": "stopwatch", "decision": "go", "decision_date": "2026-08-20",
         "active_minutes": 5e-324},
        {"source": "stopwatch", "decision": "go", "decision_date": "2026-08-27",
         "active_minutes": 1e308},
    ]
    log.write_text("\n".join(json.dumps(row) for row in rows) + "\n")
    report = summarize(log, rollout_cutoff_date="2026-08-24", rollout_cutoff_evidence="fixture")
    assert report["pre_post_active_ratio"]["status"] == "undefined_ratio_underflow"
    assert report["pre_post_active_ratio"]["ratio"] is None


@pytest.mark.parametrize("cutoff", ["0001-01-01", "9999-12-31"])
def test_cutoff_at_date_limits_is_supported(tmp_path: Path, cutoff: str):
    log = tmp_path / "m.jsonl"
    log.write_text(json.dumps({"decision_date": cutoff}) + "\n")
    report = summarize(log, rollout_cutoff_date=cutoff, rollout_cutoff_evidence="fixture")
    assert report["periods"]["unclassified"]["records"] == 1


def test_non_survivors_and_malformed_active_values_are_excluded(tmp_path: Path):
    log = tmp_path / "m.jsonl"
    rows = [
        {
            "source": "stopwatch",
            "decision": "go",
            "decision_date": "2026-08-20",
            "active_minutes": 10.0,
        },
        {
            "source": "stopwatch",
            "decision": "go",
            "decision_date": "2026-08-27",
            "active_minutes": 5.0,
        },
        {
            "source": "stopwatch",
            "decision": "no-go",
            "decision_date": "2026-08-27",
            "active_minutes": 1000.0,
        },
        *[
            {
                "source": "stopwatch",
                "decision": "go",
                "decision_date": "2026-08-27",
                "active_minutes": value,
            }
            for value in ("bad", "NaN", "Infinity", -2, True)
        ],
    ]
    log.write_text("\n".join(json.dumps(row) for row in rows) + "\n")
    report = summarize(
        log,
        rollout_cutoff_date="2026-08-24",
        rollout_cutoff_evidence="test fixture rollout record",
    )
    assert report["provenance"]["stopwatch_active_samples"] == 2
    assert report["active_minutes"]["median"] == 7.5
    assert report["provenance"]["excluded_active_values"] == {
        "non_survivor": 1,
        "invalid_value": 5,
        "not_stopwatch": 0,
    }
    assert report["pre_post_active_ratio"]["ratio"] == 2.0

"""Tests for the strict, separate processing measurement log."""

from __future__ import annotations

import json
import stat
import subprocess
import sys
from pathlib import Path

import pytest

from regexproof.mine.measurement_events import (
    MeasurementEventError,
    append_event,
    check_events_log,
    compute_event_digest,
    read_events,
    summarize,
    validate_event,
)
from regexproof.mine.cohort_manifest import build_manifest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check-measurement-events.py"
PIN = "a" * 40
ZERO = "0" * 64


def _cohort():
    return build_manifest(
        {
            "candidates": [
                {
                    "repo_id": "example/repo",
                    "url": "https://github.com/example/repo",
                    "pin": PIN,
                    "dialect_family": "py",
                    "boundary_family": "validator",
                    "score": 1,
                    "sites": 10,
                    "fork": False,
                    "duplicate_of": None,
                    "partial": False,
                }
            ]
        },
        "cohort-2026-09",
        1,
    )


def _event(sequence: int = 1, previous_digest: str = ZERO, **overrides):
    event = {
        "schema_version": "1",
        "event_id": f"event-{sequence}",
        "sequence": sequence,
        "cohort_id": "cohort-2026-09",
        "manifest_digest": _cohort()["manifest_digest"],
        "repo_id": "example/repo",
        "url": "https://github.com/example/repo",
        "pin": PIN,
        "stage": "probe",
        "status": "completed",
        "started_at": "2026-09-12T10:00:00Z",
        "ended_at": "2026-09-12T10:00:01+00:00",
        "details": {"attempt": sequence, "worker": "luna"},
        "previous_digest": previous_digest,
    }
    event.update(overrides)
    if "event_digest" not in overrides:
        event["event_digest"] = compute_event_digest(event)
    return event


def _write(path: Path, rows: list[dict]) -> None:
    path.write_text(
        "".join(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n" for row in rows),
        encoding="utf-8",
    )


def _write_cohort(path: Path):
    path.write_text(json.dumps(_cohort()), encoding="utf-8")


def test_valid_event_append_read_summary_and_private_mode(tmp_path):
    log = tmp_path / "measurement_events.jsonl"
    cohort = _cohort()
    first = append_event(_event(), log, cohort)
    second = append_event(
        _event(2, previous_digest=first["event_digest"], event_id="event-2", status="timeout"),
        log,
        cohort,
    )

    assert first["sequence"] == 1
    assert second["status"] == "timeout"
    assert read_events(log, cohort) == [first, second]
    assert check_events_log(log, cohort) == [first, second]
    assert summarize(log, cohort) == {
        "event_count": 2,
        "first_sequence": 1,
        "last_sequence": 2,
        "stages": {"probe": 2},
        "statuses": {"completed": 1, "timeout": 1},
    }
    assert stat.S_IMODE(log.stat().st_mode) == 0o600


def test_all_terminal_statuses_are_visible_in_summary(tmp_path):
    log = tmp_path / "events.jsonl"
    cohort = _cohort()
    statuses = ["unknown", "error", "partial", "retry", "cache_hit"]
    previous = ZERO
    for sequence, status in enumerate(statuses, start=1):
        event = _event(sequence, previous_digest=previous, status=status)
        append_event(event, log, cohort)
        previous = event["event_digest"]
    assert summarize(log, cohort)["statuses"] == {status: 1 for status in statuses}


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("schema_version", "2"),
        ("event_id", ""),
        ("sequence", 0),
        ("cohort_id", " "),
        ("manifest_digest", "B" * 64),
        ("pin", "A" * 40),
        ("stage", "unknown-stage"),
        ("status", "bogus"),
        ("started_at", "2026-09-12T10:00:00"),
        ("ended_at", "2026-09-12T09:59:59Z"),
        ("details", []),
        ("input_digest", "not-a-digest"),
        ("previous_digest", "0"),
        ("event_digest", "0"),
    ],
)
def test_invalid_event_fields_fail_closed(field, value):
    event = _event(**{field: value})
    with pytest.raises(MeasurementEventError):
        validate_event(event)


def test_unknown_field_and_duplicate_json_key_are_rejected(tmp_path):
    log = tmp_path / "events.jsonl"
    unknown = _event(extra="nope")
    with pytest.raises(MeasurementEventError, match="unknown field"):
        append_event(unknown, log, _cohort())
    raw = json.dumps(_event(), sort_keys=True)
    raw = raw[:-1] + ',"status":"error"}'
    log.write_text(raw + "\n", encoding="utf-8")
    with pytest.raises(MeasurementEventError, match="duplicate JSON key"):
        read_events(log, _cohort())


def test_duplicate_ids_and_sequences_and_order_are_rejected(tmp_path):
    log = tmp_path / "events.jsonl"
    _write(log, [_event(1), _event(2, previous_digest=_event(1)["event_digest"], event_id="event-1")])
    with pytest.raises(MeasurementEventError, match="duplicate event_id"):
        read_events(log, _cohort())

    _write(log, [_event(1), _event(3, previous_digest=_event(1)["event_digest"], event_id="event-3")])
    with pytest.raises(MeasurementEventError, match="append-order violation"):
        read_events(log, _cohort())

    log.write_text("", encoding="utf-8")
    append_event(_event(), log, _cohort())
    with pytest.raises(MeasurementEventError, match="expected 2"):
        append_event(_event(3, event_id="event-3"), log, _cohort())


@pytest.mark.parametrize(
    "contents",
    [
        json.dumps(_event()),
        json.dumps(_event()) + "\n\n",
        "{\"schema_version\":",
    ],
)
def test_truncated_or_blank_records_are_rejected(tmp_path, contents):
    log = tmp_path / "events.jsonl"
    log.write_text(contents, encoding="utf-8")
    with pytest.raises(MeasurementEventError):
        read_events(log, _cohort())


def test_tampered_schema_record_is_detected(tmp_path):
    log = tmp_path / "events.jsonl"
    cohort = _cohort()
    append_event(_event(), log, cohort)
    row = json.loads(log.read_text(encoding="utf-8"))
    row["manifest_digest"] = "not-a-digest"
    _write(log, [row])
    with pytest.raises(MeasurementEventError, match="manifest_digest"):
        check_events_log(log, cohort)


def test_append_does_not_mutate_input(tmp_path):
    log = tmp_path / "events.jsonl"
    event = _event(input_digest=None, output_digest=None)
    before = json.loads(json.dumps(event))
    append_event(event, log, _cohort())
    assert event == before


def test_cli_is_read_only_deterministic_and_returns_two_on_invalid(tmp_path):
    log = tmp_path / "events.jsonl"
    cohort = _cohort()
    append_event(_event(), log, cohort)
    cohort_path = tmp_path / "cohort.json"
    _write_cohort(cohort_path)
    before = log.read_bytes()
    first = subprocess.run(
        [sys.executable, str(SCRIPT), str(log), "--cohort", str(cohort_path)],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    second = subprocess.run(
        [sys.executable, str(SCRIPT), str(log), "--cohort", str(cohort_path)],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert first.returncode == second.returncode == 0
    assert first.stdout == second.stdout
    assert json.loads(first.stdout)["event_count"] == 1
    assert log.read_bytes() == before

    log.write_bytes(before[:-1])
    invalid = subprocess.run(
        [sys.executable, str(SCRIPT), str(log), "--cohort", str(cohort_path)],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert invalid.returncode == 2
    assert "truncated" in invalid.stderr


def test_missing_log_is_an_empty_valid_summary(tmp_path):
    result = summarize(tmp_path / "missing.jsonl", _cohort())
    assert result == {
        "event_count": 0,
        "first_sequence": None,
        "last_sequence": None,
        "stages": {},
        "statuses": {},
    }


def test_missing_cohort_fails_closed(tmp_path):
    log = tmp_path / "events.jsonl"
    append_event(_event(), log, _cohort())
    with pytest.raises(MeasurementEventError, match="cohort manifest is required"):
        check_events_log(log)


def test_hash_chain_detects_middle_record_rewrite(tmp_path):
    log = tmp_path / "events.jsonl"
    cohort = _cohort()
    first = _event(1)
    second = _event(2, previous_digest=first["event_digest"])
    third = _event(3, previous_digest=second["event_digest"])
    for event in (first, second, third):
        append_event(event, log, cohort)
    rows = [json.loads(line) for line in log.read_text(encoding="utf-8").splitlines()]
    rows[1]["details"]["attempt"] = 99
    rows[1]["event_digest"] = compute_event_digest(rows[1])
    _write(log, rows)
    with pytest.raises(MeasurementEventError, match="hash-chain"):
        read_events(log, cohort)


def test_event_repository_must_be_in_frozen_cohort(tmp_path):
    log = tmp_path / "events.jsonl"
    cohort = _cohort()
    event = _event(url="https://github.com/example/other")
    with pytest.raises(MeasurementEventError, match="not in the frozen cohort"):
        append_event(event, log, cohort)

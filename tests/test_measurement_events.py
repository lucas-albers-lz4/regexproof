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
    read_events,
    summarize,
    validate_event,
)

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check-measurement-events.py"
PIN = "a" * 40
DIGEST = "b" * 64


def _event(sequence: int = 1, **overrides):
    event = {
        "schema_version": "1",
        "event_id": f"event-{sequence}",
        "sequence": sequence,
        "cohort_id": "cohort-2026-09",
        "manifest_digest": DIGEST,
        "repo_id": "example/repo",
        "url": "https://github.com/example/repo",
        "pin": PIN,
        "stage": "probe",
        "status": "completed",
        "started_at": "2026-09-12T10:00:00Z",
        "ended_at": "2026-09-12T10:00:01+00:00",
        "details": {"attempt": sequence, "worker": "luna"},
    }
    event.update(overrides)
    return event


def _write(path: Path, rows: list[dict]) -> None:
    path.write_text(
        "".join(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n" for row in rows),
        encoding="utf-8",
    )


def test_valid_event_append_read_summary_and_private_mode(tmp_path):
    log = tmp_path / "measurement_events.jsonl"
    first = append_event(_event(), log)
    second = append_event(_event(2, event_id="event-2", status="timeout"), log)

    assert first["sequence"] == 1
    assert second["status"] == "timeout"
    assert read_events(log) == [first, second]
    assert check_events_log(log) == [first, second]
    assert summarize(log) == {
        "event_count": 2,
        "first_sequence": 1,
        "last_sequence": 2,
        "stages": {"probe": 2},
        "statuses": {"completed": 1, "timeout": 1},
    }
    assert stat.S_IMODE(log.stat().st_mode) == 0o600


def test_all_terminal_statuses_are_visible_in_summary(tmp_path):
    log = tmp_path / "events.jsonl"
    statuses = ["unknown", "error", "partial"]
    for sequence, status in enumerate(statuses, start=1):
        append_event(_event(sequence, status=status), log)
    assert summarize(log)["statuses"] == {status: 1 for status in statuses}


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
        append_event(unknown, log)
    raw = json.dumps(_event(), sort_keys=True)
    raw = raw[:-1] + ',"status":"error"}'
    log.write_text(raw + "\n", encoding="utf-8")
    with pytest.raises(MeasurementEventError, match="duplicate JSON key"):
        read_events(log)


def test_duplicate_ids_and_sequences_and_order_are_rejected(tmp_path):
    log = tmp_path / "events.jsonl"
    _write(log, [_event(1), _event(2, event_id="event-1")])
    with pytest.raises(MeasurementEventError, match="duplicate event_id"):
        read_events(log)

    _write(log, [_event(1), _event(3, event_id="event-3")])
    with pytest.raises(MeasurementEventError, match="append-order violation"):
        read_events(log)

    log.write_text("", encoding="utf-8")
    append_event(_event(), log)
    with pytest.raises(MeasurementEventError, match="expected 2"):
        append_event(_event(3, event_id="event-3"), log)


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
        read_events(log)


def test_tampered_schema_record_is_detected(tmp_path):
    log = tmp_path / "events.jsonl"
    append_event(_event(), log)
    row = json.loads(log.read_text(encoding="utf-8"))
    row["manifest_digest"] = "not-a-digest"
    _write(log, [row])
    with pytest.raises(MeasurementEventError, match="manifest_digest"):
        check_events_log(log)


def test_append_does_not_mutate_input(tmp_path):
    log = tmp_path / "events.jsonl"
    event = _event(input_digest=None, output_digest=None)
    before = json.loads(json.dumps(event))
    append_event(event, log)
    assert event == before


def test_cli_is_read_only_deterministic_and_returns_two_on_invalid(tmp_path):
    log = tmp_path / "events.jsonl"
    append_event(_event(), log)
    before = log.read_bytes()
    first = subprocess.run(
        [sys.executable, str(SCRIPT), str(log)],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    second = subprocess.run(
        [sys.executable, str(SCRIPT), str(log)],
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
        [sys.executable, str(SCRIPT), str(log)],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert invalid.returncode == 2
    assert "truncated" in invalid.stderr


def test_missing_log_is_an_empty_valid_summary(tmp_path):
    result = summarize(tmp_path / "missing.jsonl")
    assert result == {
        "event_count": 0,
        "first_sequence": None,
        "last_sequence": None,
        "stages": {},
        "statuses": {},
    }

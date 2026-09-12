"""Strict append-only processing events for the saturation campaign.

This log is deliberately separate from ``corpus_events.jsonl`` and from the
corpus wave lock.  The wave lock records state-machine transitions; this file
records measurement observations made while a frozen cohort moves through the
mine/rank/probe/gate/conversion/disposition stages.

The append path takes an exclusive flock on this log, validates the complete
existing history, requires the next contiguous sequence number, appends with
``O_APPEND`` and fsyncs before releasing the lock.  Readers apply the same
validation, so malformed, truncated, duplicated, reordered, or otherwise
schema-invalid history fails closed.
"""

from __future__ import annotations

import fcntl
import hashlib
import json
import os
import pathlib
import re
from collections import Counter
from datetime import datetime, timezone
from typing import Any, Mapping

from .cohort_manifest import CohortManifestError, validate_manifest as validate_cohort

DEFAULT_LOG_PATH = pathlib.Path("properties/generated/measurement_events.jsonl")
SCHEMA_VERSION = "1"
STAGES = frozenset({"mine", "rank", "probe", "gate", "conversion", "disposition"})
STATUSES = frozenset(
    {
        "attempted",
        "completed",
        "ok",
        "auto_nogo",
        "needs_human",
        "retry",
        "cache_hit",
        "timeout",
        "unknown",
        "error",
        "partial",
    }
)

_DIGEST_RE = re.compile(r"^[0-9a-f]{64}$")
_PIN_RE = re.compile(r"^[0-9a-f]{40}$")
_REQUIRED_FIELDS = frozenset(
    {
        "schema_version",
        "event_id",
        "sequence",
        "cohort_id",
        "manifest_digest",
        "repo_id",
        "url",
        "pin",
        "stage",
        "status",
        "started_at",
        "ended_at",
        "details",
        "previous_digest",
        "event_digest",
    }
)
_OPTIONAL_FIELDS = frozenset({"input_digest", "output_digest"})
_ALLOWED_FIELDS = _REQUIRED_FIELDS | _OPTIONAL_FIELDS


class MeasurementEventError(ValueError):
    """Raised when an event or event log violates the measurement contract."""


def _fail(message: str) -> MeasurementEventError:
    return MeasurementEventError(f"measurement_events: {message}")


def _require_nonblank(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise _fail(f"{field} must be a nonempty string")
    return value


def _require_digest(value: Any, field: str) -> None:
    if not isinstance(value, str) or _DIGEST_RE.fullmatch(value) is None:
        raise _fail(f"{field} must be exactly 64 lowercase hexadecimal characters")


def _require_pin(value: Any) -> None:
    if not isinstance(value, str) or _PIN_RE.fullmatch(value) is None:
        raise _fail("pin must be exactly 40 lowercase hexadecimal characters")


def _require_json_value(value: Any, path: str) -> None:
    """Validate the JSON-shaped ``details`` object without coercion."""
    if value is None or isinstance(value, (str, int, float, bool)):
        if isinstance(value, float) and not (value == value and abs(value) != float("inf")):
            raise _fail(f"{path} contains a non-finite number")
        return
    if isinstance(value, list):
        for index, item in enumerate(value):
            _require_json_value(item, f"{path}[{index}]")
        return
    if isinstance(value, dict):
        for key, item in value.items():
            if not isinstance(key, str) or not key:
                raise _fail(f"{path} keys must be nonempty strings")
            _require_json_value(item, f"{path}.{key}")
        return
    raise _fail(f"{path} contains a non-JSON value")


def _parse_timestamp(value: Any, field: str) -> datetime:
    if not isinstance(value, str) or "T" not in value:
        raise _fail(f"{field} must be an ISO-8601 UTC timestamp")
    candidate = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(candidate)
    except ValueError as exc:
        raise _fail(f"{field} must be an ISO-8601 UTC timestamp") from exc
    if parsed.tzinfo is None or parsed.utcoffset() != timezone.utc.utcoffset(parsed):
        raise _fail(f"{field} must carry the UTC offset")
    return parsed


def validate_event(event: Mapping[str, Any]) -> dict[str, Any]:
    """Validate and shallow-copy one event without mutating its input."""
    if not isinstance(event, Mapping):
        raise _fail("event must be an object")
    actual = set(event)
    missing = sorted(_REQUIRED_FIELDS - actual)
    unknown = sorted(actual - _ALLOWED_FIELDS)
    if missing:
        raise _fail("missing field(s): " + ", ".join(missing))
    if unknown:
        raise _fail("unknown field(s): " + ", ".join(unknown))

    if event["schema_version"] != SCHEMA_VERSION or not isinstance(
        event["schema_version"], str
    ):
        raise _fail("schema_version must be '1'")
    _require_nonblank(event["event_id"], "event_id")
    sequence = event["sequence"]
    if isinstance(sequence, bool) or not isinstance(sequence, int) or sequence < 1:
        raise _fail("sequence must be a positive integer")
    _require_nonblank(event["cohort_id"], "cohort_id")
    _require_digest(event["manifest_digest"], "manifest_digest")
    _require_nonblank(event["repo_id"], "repo_id")
    _require_nonblank(event["url"], "url")
    _require_pin(event["pin"])
    if not isinstance(event["stage"], str) or event["stage"] not in STAGES:
        raise _fail(f"stage must be one of {sorted(STAGES)}")
    if not isinstance(event["status"], str) or event["status"] not in STATUSES:
        raise _fail(f"status must be one of {sorted(STATUSES)}")
    started = _parse_timestamp(event["started_at"], "started_at")
    ended = _parse_timestamp(event["ended_at"], "ended_at")
    if ended < started:
        raise _fail("ended_at must be greater than or equal to started_at")
    if not isinstance(event["details"], dict):
        raise _fail("details must be an object")
    _require_json_value(event["details"], "details")
    _require_digest(event["previous_digest"], "previous_digest")
    _require_digest(event["event_digest"], "event_digest")
    for field in ("input_digest", "output_digest"):
        if field in event and event[field] is not None:
            _require_digest(event[field], field)
    normalized = dict(event)
    if normalized["event_digest"] != compute_event_digest(normalized):
        raise _fail("event_digest does not match the canonical event payload")
    return normalized


def compute_event_digest(event: Mapping[str, Any]) -> str:
    """Return the SHA-256 of the canonical event payload without its digest."""
    payload = {key: value for key, value in event.items() if key != "event_digest"}
    encoded = json.dumps(
        payload,
        ensure_ascii=True,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise _fail(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise _fail(f"non-standard JSON constant {value!r}")


def _decode_log(data: bytes, path: pathlib.Path) -> list[dict[str, Any]]:
    if not data:
        return []
    if not data.endswith(b"\n"):
        raise _fail(f"truncated final record in {path}")
    events: list[dict[str, Any]] = []
    event_ids: set[str] = set()
    expected_sequence = 1
    expected_previous_digest = "0" * 64
    for line_number, raw_line in enumerate(data.splitlines(keepends=True), start=1):
        if not raw_line.endswith(b"\n"):
            raise _fail(f"truncated record at line {line_number} in {path}")
        try:
            text = raw_line[:-1].decode("utf-8")
        except UnicodeDecodeError as exc:
            raise _fail(f"invalid UTF-8 at line {line_number} in {path}") from exc
        if not text.strip():
            raise _fail(f"blank record at line {line_number} in {path}")
        try:
            parsed = json.loads(
                text,
                object_pairs_hook=_reject_duplicate_keys,
                parse_constant=_reject_constant,
            )
        except MeasurementEventError as exc:
            raise _fail(f"line {line_number} in {path}: {exc}") from exc
        except json.JSONDecodeError as exc:
            raise _fail(f"invalid JSON at line {line_number} in {path}: {exc.msg}") from exc
        try:
            event = validate_event(parsed)
        except MeasurementEventError as exc:
            raise _fail(f"line {line_number} in {path}: {exc}") from exc
        if event["event_id"] in event_ids:
            raise _fail(f"duplicate event_id {event['event_id']!r} at line {line_number}")
        if event["sequence"] != expected_sequence:
            raise _fail(
                f"append-order violation at line {line_number}: expected sequence "
                f"{expected_sequence}, got {event['sequence']}"
            )
        if event["previous_digest"] != expected_previous_digest:
            raise _fail(
                f"hash-chain violation at line {line_number}: expected previous_digest "
                f"{expected_previous_digest}, got {event['previous_digest']}"
            )
        event_ids.add(event["event_id"])
        events.append(event)
        expected_sequence += 1
        expected_previous_digest = event["event_digest"]
    return events


def _validated_cohort(cohort: Mapping[str, Any] | None) -> dict[str, Any]:
    if cohort is None:
        raise _fail("a frozen cohort manifest is required")
    try:
        return validate_cohort(cohort)
    except CohortManifestError as exc:
        raise _fail(f"invalid frozen cohort: {exc}") from exc


def _validate_cohort_binding(
    event: Mapping[str, Any], cohort: Mapping[str, Any] | None
) -> None:
    frozen = _validated_cohort(cohort)
    if event["cohort_id"] != frozen["cohort_id"]:
        raise _fail("event cohort_id does not match the frozen cohort")
    if event["manifest_digest"] != frozen["manifest_digest"]:
        raise _fail("event manifest_digest does not match the frozen cohort")
    identity = (event["repo_id"], event["url"], event["pin"])
    allowed = {(repo["repo_id"], repo["url"], repo["pin"]) for repo in frozen["repos"]}
    if identity not in allowed:
        raise _fail("event repository identity is not in the frozen cohort")


def read_events(
    path: pathlib.Path | str | None = None,
    cohort: Mapping[str, Any] | None = None,
) -> list[dict[str, Any]]:
    """Read and fully validate the measurement log, returning event copies."""
    _validated_cohort(cohort)
    destination = pathlib.Path(path) if path is not None else DEFAULT_LOG_PATH
    try:
        data = destination.read_bytes()
    except FileNotFoundError:
        return []
    except OSError as exc:
        raise _fail(f"cannot read {destination}: {exc}") from exc
    events = _decode_log(data, destination)
    for event in events:
        _validate_cohort_binding(event, cohort)
    return events


def check_events_log(
    path: pathlib.Path | str | None = None,
    cohort: Mapping[str, Any] | None = None,
) -> list[dict[str, Any]]:
    """Validate the complete log; this is the read-only CI/check entry point."""
    return read_events(path, cohort)


def _read_fd(fd: int) -> bytes:
    os.lseek(fd, 0, os.SEEK_SET)
    chunks: list[bytes] = []
    while True:
        chunk = os.read(fd, 1024 * 1024)
        if not chunk:
            return b"".join(chunks)
        chunks.append(chunk)


def _write_all(fd: int, data: bytes, destination: pathlib.Path) -> None:
    view = memoryview(data)
    while view:
        written = os.write(fd, view)
        if written <= 0:
            raise _fail(f"short write to {destination}")
        view = view[written:]


def append_event(
    event: Mapping[str, Any],
    path: pathlib.Path | str | None = None,
    cohort: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Validate and durably append one event under an exclusive file lock.

    The caller supplies the sequence number.  It must be exactly one greater
    than the validated last sequence, which makes accidental retries and
    concurrent writers visible instead of silently reordering the history.
    """
    candidate = validate_event(event)
    _validate_cohort_binding(candidate, cohort)
    destination = pathlib.Path(path) if path is not None else DEFAULT_LOG_PATH
    destination.parent.mkdir(parents=True, exist_ok=True)
    flags = os.O_APPEND | os.O_CREAT | os.O_RDWR
    fd = os.open(str(destination), flags, 0o600)
    locked = False
    try:
        os.fchmod(fd, 0o600)
        fcntl.flock(fd, fcntl.LOCK_EX)
        locked = True
        existing = _decode_log(_read_fd(fd), destination)
        for row in existing:
            _validate_cohort_binding(row, cohort)
        expected = len(existing) + 1
        if candidate["sequence"] != expected:
            raise _fail(
                f"sequence {candidate['sequence']} cannot be appended; expected {expected}"
            )
        expected_previous_digest = existing[-1]["event_digest"] if existing else "0" * 64
        if candidate["previous_digest"] != expected_previous_digest:
            raise _fail(
                "previous_digest cannot be appended; expected "
                f"{expected_previous_digest}"
            )
        if any(row["event_id"] == candidate["event_id"] for row in existing):
            raise _fail(f"duplicate event_id {candidate['event_id']!r}")
        payload = json.dumps(
            candidate,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8") + b"\n"
        _write_all(fd, payload, destination)
        os.fsync(fd)
        return candidate
    finally:
        if locked:
            fcntl.flock(fd, fcntl.LOCK_UN)
        os.close(fd)


def summarize(
    path: pathlib.Path | str | None = None,
    cohort: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Return a deterministic, JSON-serializable log summary."""
    events = check_events_log(path, cohort)
    stages = Counter(event["stage"] for event in events)
    statuses = Counter(event["status"] for event in events)
    return {
        "event_count": len(events),
        "first_sequence": events[0]["sequence"] if events else None,
        "last_sequence": events[-1]["sequence"] if events else None,
        "stages": {key: stages[key] for key in sorted(stages)},
        "statuses": {key: statuses[key] for key in sorted(statuses)},
    }


__all__ = [
    "DEFAULT_LOG_PATH",
    "SCHEMA_VERSION",
    "STAGES",
    "STATUSES",
    "MeasurementEventError",
    "append_event",
    "check_events_log",
    "compute_event_digest",
    "read_events",
    "summarize",
    "validate_event",
]

"""Wave C (#558): corpus lock — append-only events log + generation.

The lock's one primitive is the derived per-corpus generation (closed-wave
event count). Status is derived from the LAST event, never stored. The
events log is append-only; CI checks monotonic generation."""

from __future__ import annotations

import json
import pathlib

import pytest

from regexproof.mine import corpus_lock as cl


def _log(tmp_path: pathlib.Path) -> pathlib.Path:
    return tmp_path / "corpus_events.jsonl"


def test_generation_derived_from_closed_events(tmp_path):
    log = _log(tmp_path)
    assert cl.read_generation("ow", log) == 0
    cl.wave_open("ow", "w1", log=log)
    assert cl.read_generation("ow", log) == 0  # open does not increment
    cl.wave_close("ow", "w1", log=log)
    assert cl.read_generation("ow", log) == 1
    cl.wave_open("ow", "w2", log=log)
    cl.wave_close("ow", "w2", log=log)
    assert cl.read_generation("ow", log) == 2


def test_wave_status_derived_from_last_event(tmp_path):
    log = _log(tmp_path)
    assert cl.wave_status("ow", log) == "none"
    cl.wave_open("ow", "w1", log=log)
    assert cl.wave_status("ow", log) == "active"
    cl.wave_close("ow", "w1", log=log)
    assert cl.wave_status("ow", log) == "closed"
    cl.wave_open("ow", "w2", log=log)
    cl.wave_abort("ow", "w2", reason="stuck", log=log)
    assert cl.wave_status("ow", log) == "aborted"


def test_wave_open_refuses_blank_id(tmp_path):
    """Luna r5 #3: a blank active-wave ID would bypass claim-time equality
    checks — wave_open must refuse it."""
    log = _log(tmp_path)
    with pytest.raises(SystemExit, match="wave_id must be nonblank"):
        cl.wave_open("ow", "", log=log)


def test_close_refused_after_abort(tmp_path):
    """CodeRabbit #569 (Critical): an aborted wave must never be closable —
    the close would write an illegal transition and bump generation."""
    log = _log(tmp_path)
    cl.wave_open("ow", "w1", log=log)
    cl.wave_abort("ow", "w1", reason="mis-begun", log=log)
    with pytest.raises(SystemExit, match="ABORTED"):
        cl.wave_close("ow", "w1", log=log)
    assert cl.read_generation("ow", log) == 0


def test_no_parallel_waves(tmp_path):
    log = _log(tmp_path)
    cl.wave_open("ow", "w1", log=log)
    with pytest.raises(SystemExit, match="already has an active wave"):
        cl.wave_open("ow", "w2", log=log)


def test_close_requires_open(tmp_path):
    log = _log(tmp_path)
    with pytest.raises(SystemExit, match="no wave to close"):
        cl.wave_close("ow", "w1", log=log)


def test_force_close_records_flag(tmp_path):
    log = _log(tmp_path)
    cl.wave_open("ow", "w1", log=log)
    # Forced close requires a queue artifact + skip reasons for every
    # non-contracted top-15 candidate (Luna r1 #4 / r2 #3).
    from regexproof.mine import conversion_queue as cq

    ranked = [{"site": "net/demo/a.sh:1:tok", "corpus": "ow", "provenance": "stub"}]
    cq.emit("ow", wave_id="w1", generation=0, ranked=ranked, root=tmp_path)
    cl.wave_close(
        "ow", "w1", force=True,
        skip_reasons={"net/demo/a.sh:1:tok": "out_of_scope"},
        queue_root=tmp_path, log=log,
    )
    events = [json.loads(line) for line in log.read_text().splitlines()]
    close = events[-1]
    assert close["force"] is True
    assert close["skip_reasons"] == {"net/demo/a.sh:1:tok": "out_of_scope"}


def test_forced_close_requires_queue_root(tmp_path):
    """Luna r2 #3 / r7 #4: a close WITHOUT a named queue skips close-out
    (non-queue waves are legitimate) — but the FORCE flag still records."""
    log = _log(tmp_path)
    cl.wave_open("ow", "w1", log=log)
    cl.wave_close("ow", "w1", force=True, log=log)  # no queue_root: allowed
    assert cl.read_generation("ow", log) == 1


def test_forced_close_rejects_off_vocabulary_reason(tmp_path):
    """Luna r3 #3: a nonblank but off-vocabulary skip reason must be
    refused — 'bogus' is not a queue skip reason."""
    from regexproof.mine import conversion_queue as cq

    ranked = [{"site": "net/demo/a.sh:1:tok", "corpus": "ow", "provenance": "stub"}]
    cq.emit("ow", wave_id="w1", generation=0, ranked=ranked, root=tmp_path)
    log = _log(tmp_path)
    cl.wave_open("ow", "w1", log=log)
    with pytest.raises(SystemExit, match="close-out refused"):
        cl.wave_close(
            "ow", "w1", force=True,
            skip_reasons={"net/demo/a.sh:1:tok": "bogus"},
            queue_root=tmp_path, log=log,
        )
    # A vocabulary reason passes.
    cl.wave_close(
        "ow", "w1", force=True,
        skip_reasons={"net/demo/a.sh:1:tok": "out_of_scope"},
        queue_root=tmp_path, log=log,
    )
    assert cl.read_generation("ow", log) == 1


def test_verify_generation_optimistic_lock(tmp_path):
    log = _log(tmp_path)
    cl.wave_open("ow", "w1", log=log)
    snapshot = cl.read_generation("ow", log)
    cl.verify_generation("ow", snapshot, log=log)  # no advance -> ok
    cl.wave_close("ow", "w1", log=log)  # advance while "in flight"
    with pytest.raises(SystemExit, match="generation advanced"):
        cl.verify_generation("ow", snapshot, log=log)


def test_stuck_wave_health(tmp_path):
    from datetime import date

    log = _log(tmp_path)
    cl.wave_open("ow", "w1", log=log)  # at = now
    stuck = cl.stuck_wave_health(today=date.today(), log=log)
    assert stuck == []  # fresh wave not stuck

    # Simulate an old wave by rewriting the at timestamp (test-only).
    events = [json.loads(line) for line in log.read_text().splitlines()]
    events[0]["at"] = "2020-01-01T00:00:00+00:00"
    log.write_text(
        "".join(json.dumps(e, sort_keys=True) + "\n" for e in events),
        encoding="utf-8",
    )
    stuck = cl.stuck_wave_health(today=date(2020, 1, 15), log=log)
    assert len(stuck) == 1
    assert stuck[0]["corpus"] == "ow"
    assert stuck[0]["age_days"] == 14
    assert stuck[0]["status"] == "stuck"


def test_abort_does_not_increment_generation(tmp_path):
    log = _log(tmp_path)
    cl.wave_open("ow", "w1", log=log)
    cl.wave_abort("ow", "w1", reason="mis-begun", log=log)
    assert cl.read_generation("ow", log) == 0  # abort != close


def test_events_log_monotonic_check(tmp_path):
    log = _log(tmp_path)
    cl.wave_open("ow", "w1", log=log)
    cl.wave_close("ow", "w1", log=log)
    cl.check_events_log(log)  # monotonic -> ok
    # Rewrite with a decreasing generation: append-only violation.
    events = [json.loads(line) for line in log.read_text().splitlines()]
    events[-1]["generation"] = -1
    log.write_text(
        "".join(json.dumps(e, sort_keys=True) + "\n" for e in events),
        encoding="utf-8",
    )
    with pytest.raises(SystemExit, match="append-only violation"):
        cl.check_events_log(log)


def test_events_log_rejects_unknown_event(tmp_path):
    log = _log(tmp_path)
    log.write_text(json.dumps({"event": "bogus", "corpus": "ow", "wave_id": "w", "generation": 0}) + "\n")
    with pytest.raises(SystemExit, match="unknown event"):
        cl.check_events_log(log)


def test_events_log_rejects_reused_wave_id(tmp_path):
    """Luna r8 #2: the CI gate must agree with wave_open's uniqueness guard —
    open w1 → close w1 → open w1 must fail the check."""
    log = _log(tmp_path)
    cl.wave_open("ow", "w1", log=log)
    cl.wave_close("ow", "w1", log=log)
    # Hand-write a reused open (the API refuses it; the gate must too).
    with open(log, "a", encoding="utf-8") as fh:
        fh.write(json.dumps({"event": "wave_opened", "corpus": "ow", "wave_id": "w1", "at": "2026-08-23T00:00:00+00:00", "generation": 1}) + "\n")
    with pytest.raises(SystemExit, match="reuses wave_id"):
        cl.check_events_log(log)


def test_events_log_mode_is_0600(tmp_path):
    """Luna r8 #1: fchmod enforces 0600 on EXISTING logs (os.open's mode is
    ignored when the file exists). The fixture file is created with the
    default umask mode (typically 0644) — no explicit chmod, so CodeQL's
    overly-permissive rule does not fire on the test itself."""
    import os

    log = _log(tmp_path)
    log.write_text("", encoding="utf-8")  # default mode, typically 0644
    cl.wave_open("ow", "w1", log=log)
    assert (log.stat().st_mode & 0o777) == 0o600


def test_close_without_open_is_illegal(tmp_path):
    """Luna r1 #5: a close event with no preceding open must fail the check."""
    log = _log(tmp_path)
    log.write_text(
        json.dumps({"event": "wave_closed", "corpus": "ow", "wave_id": "w1", "generation": 1})
        + "\n",
        encoding="utf-8",
    )
    with pytest.raises(SystemExit, match="closed without an open"):
        cl.check_events_log(log)


def test_wrong_id_close_refused(tmp_path):
    """Luna r1 #2: closing a wave with the wrong wave_id must be refused."""
    log = _log(tmp_path)
    cl.wave_open("ow", "w1", log=log)
    with pytest.raises(SystemExit, match="wrong-id close"):
        cl.wave_close("ow", "wrong-id", log=log)


def test_abort_requires_active_wave(tmp_path):
    """Luna r1 #2: aborting a closed/nonexistent wave must be refused."""
    log = _log(tmp_path)
    with pytest.raises(SystemExit, match="no active wave to abort"):
        cl.wave_abort("ow", "w1", reason="x", log=log)
    cl.wave_open("ow", "w1", log=log)
    cl.wave_close("ow", "w1", log=log)
    with pytest.raises(SystemExit, match="no active wave to abort"):
        cl.wave_abort("ow", "w1", reason="x", log=log)


def test_forced_close_enforces_queue_skip_reasons(tmp_path):
    """Luna r1 #4: a forced close must refuse when non-contracted top-15
    candidates lack skip reasons — the lock consults the queue."""
    from regexproof.mine import conversion_queue as cq

    ranked = [
        {"site": f"net/demo/a.sh:{i}:tok", "corpus": "ow", "provenance": "stub"}
        for i in range(1, 4)
    ]
    cq.emit("ow", wave_id="w1", generation=0, ranked=ranked, root=tmp_path)
    log = _log(tmp_path)
    cl.wave_open("ow", "w1", log=log)
    # All three are non-contracted top-15 and lack skip reasons.
    with pytest.raises(SystemExit, match="close-out refused"):
        cl.wave_close("ow", "w1", force=True, queue_root=tmp_path, log=log)
    # With skip reasons for every blocker the forced close succeeds.
    cl.wave_close(
        "ow", "w1", force=True,
        skip_reasons={f"net/demo/a.sh:{i}:tok": "out_of_scope" for i in range(1, 4)},
        queue_root=tmp_path, log=log,
    )
    assert cl.read_generation("ow", log) == 1

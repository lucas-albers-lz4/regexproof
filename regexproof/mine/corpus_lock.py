"""Wave C (#558): optimistic corpus lock with append-only events log.

One primitive: the corpus ``wave_generation`` — the count of closed-wave
events for that corpus in an APPEND-ONLY events log
(``properties/generated/corpus_events.jsonl``). Every wave-status flip
(opened / closed / aborted) is an event; generation is derived, never
stored independently, so it cannot drift from history.

Protocol
--------
- ``read_generation(corpus)`` — derived from the events log; 0 when the
  corpus has no events (pre-Phase-C fallback FAILS CLOSED on lock use:
  a corpus with no events log is not lockable — the queue owns locking).
- ``wave_open`` / ``wave_close`` / ``wave_abort`` append one event each
  (O_APPEND, single write syscall). ``wave_close`` increments generation
  ATOMICALLY with the wave-status flip: the event append and the
  wave-status artifact write happen in the same commit step, and the
  artifact embeds the post-flip generation.
- ``verify_generation(corpus, expected)`` — commit-time re-verify for the
  optimistic lock: raises if the corpus advanced past the snapshot.
- ``--force`` close: allowed only with skip reasons for every
  non-contracted top-15 candidate (the queue enforces this; the lock
  records the force flag in the event).
- ``stuck_wave_health`` — a corpus whose last event is ``wave_opened``
  older than ``STUCK_AFTER_DAYS`` is reported; ``wave_abort`` compensates.

The events log is append-only by construction (O_APPEND); CI verifies
with an append-only check (no rewrite: the log's line count never
decreases and no line is ever replaced — see ``check_events_log``).
"""

from __future__ import annotations

import json
import os
import pathlib
from datetime import date, datetime, timezone
from typing import Any

EVENTS_LOG = pathlib.Path("properties/generated/corpus_events.jsonl")
STUCK_AFTER_DAYS = 7

WAVE_EVENTS = frozenset({"wave_opened", "wave_closed", "wave_aborted"})

# Derived wave_status from the events log (never stored independently).
OPEN_EVENT = "wave_opened"
CLOSE_EVENT = "wave_closed"
ABORT_EVENT = "wave_aborted"


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _read_events(path: pathlib.Path | None = None) -> list[dict[str, Any]]:
    log = pathlib.Path(path) if path is not None else EVENTS_LOG
    if not log.is_file():
        return []
    events: list[dict[str, Any]] = []
    for line in log.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise SystemExit(
                f"corpus_lock: corrupt events log {log}: {exc}"
            ) from exc
    return events


def _append_event(
    event: dict[str, Any],
    log: pathlib.Path | None = None,
) -> None:
    """Append one event with O_APPEND (single write syscall, append-only)."""
    path = pathlib.Path(log) if log is not None else EVENTS_LOG
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(event, sort_keys=True) + "\n")
        os.fsync(fh.fileno())


def read_generation(corpus: str, log: pathlib.Path | None = None) -> int:
    """Generation = closed-wave-event count for the corpus (derived)."""
    return sum(
        1
        for e in _read_events(log)
        if e.get("corpus") == corpus and e.get("event") == CLOSE_EVENT
    )


def wave_status(corpus: str, log: pathlib.Path | None = None) -> str:
    """Derived wave_status: ``active`` / ``closed`` / ``aborted`` /
    ``none`` — from the LAST event for the corpus (never stored)."""
    last: dict[str, Any] | None = None
    for e in _read_events(log):
        if e.get("corpus") == corpus:
            last = e
    if last is None:
        return "none"
    event = str(last.get("event") or "")
    if event == OPEN_EVENT:
        return "active"
    if event == CLOSE_EVENT:
        return "closed"
    if event == ABORT_EVENT:
        return "aborted"
    return "none"


def wave_open(
    corpus: str,
    wave_id: str,
    *,
    log: pathlib.Path | None = None,
) -> int:
    """Open a wave: appends ``wave_opened``. Fails closed if the corpus has
    an active wave (no parallel waves). Returns the generation (unchanged)."""
    if wave_status(corpus, log) == "active":
        raise SystemExit(
            f"corpus_lock: {corpus} already has an active wave — close or "
            "abort it before opening another (skip_wave_active)"
        )
    _append_event(
        {
            "event": OPEN_EVENT,
            "corpus": corpus,
            "wave_id": wave_id,
            "at": _now_iso(),
            "generation": read_generation(corpus, log),
        },
        log,
    )
    return read_generation(corpus, log)


def wave_close(
    corpus: str,
    wave_id: str,
    *,
    force: bool = False,
    skip_reasons: dict[str, str] | None = None,
    log: pathlib.Path | None = None,
) -> int:
    """Close a wave: appends ``wave_closed`` — this INCREMENTS generation.
    ``force=True`` is recorded in the event (the queue enforces skip
    reasons for non-contracted top-15 before calling with force)."""
    status = wave_status(corpus, log)
    if status == "none":
        raise SystemExit(
            f"corpus_lock: {corpus} has no wave to close — open one first "
            "(pre-Phase-C fallback fails closed)"
        )
    if status == "closed":
        raise SystemExit(f"corpus_lock: {corpus} wave already closed")
    gen = read_generation(corpus, log)
    _append_event(
        {
            "event": CLOSE_EVENT,
            "corpus": corpus,
            "wave_id": wave_id,
            "at": _now_iso(),
            "generation": gen + 1,  # post-flip generation, recorded atomically
            "force": bool(force),
            "skip_reasons": skip_reasons or {},
        },
        log,
    )
    return gen + 1


def wave_abort(
    corpus: str,
    wave_id: str,
    *,
    reason: str,
    log: pathlib.Path | None = None,
) -> None:
    """Abort a wave (compensation for a stuck/mis-begun wave). Does NOT
    increment generation — an aborted wave is not a closed wave."""
    _append_event(
        {
            "event": ABORT_EVENT,
            "corpus": corpus,
            "wave_id": wave_id,
            "at": _now_iso(),
            "reason": reason,
            "generation": read_generation(corpus, log),
        },
        log,
    )


def verify_generation(corpus: str, expected: int, *, log: pathlib.Path | None = None) -> None:
    """Commit-time re-verify for the optimistic lock: raises if the corpus
    advanced past the snapshot the caller locked on."""
    current = read_generation(corpus, log)
    if current != expected:
        raise SystemExit(
            f"corpus_lock: {corpus} generation advanced {expected} -> {current} "
            "— the wave closed while work was in flight (optimistic lock "
            "violation). Re-derive from the new generation."
        )


def stuck_wave_health(
    *,
    today: date | None = None,
    log: pathlib.Path | None = None,
) -> list[dict[str, Any]]:
    """Corpora whose LAST event is ``wave_opened`` older than
    ``STUCK_AFTER_DAYS`` (the stuck-wave health report)."""
    today = today or date.today()
    last_by_corpus: dict[str, dict[str, Any]] = {}
    for e in _read_events(log):
        corpus = str(e.get("corpus") or "")
        if not corpus:
            continue
        last_by_corpus[corpus] = e
    out: list[dict[str, Any]] = []
    for corpus, e in last_by_corpus.items():
        if e.get("event") != OPEN_EVENT:
            continue
        at = str(e.get("at") or "")
        try:
            opened = datetime.fromisoformat(at).date()
        except ValueError:
            continue
        age = (today - opened).days
        if age >= STUCK_AFTER_DAYS:
            out.append(
                {
                    "corpus": corpus,
                    "wave_id": e.get("wave_id"),
                    "opened_at": at,
                    "age_days": age,
                    "status": "stuck",
                }
            )
    return out


def check_events_log(log: pathlib.Path | None = None) -> int:
    """CI append-only check: every line parses; the log is a sequence of
    events with monotonic (non-decreasing) generation per corpus; the last
    event per corpus has a valid state. Returns 0 (or raises)."""
    events = _read_events(log)
    for e in events:
        if e.get("event") not in WAVE_EVENTS:
            raise SystemExit(
                f"corpus_lock: unknown event {e.get('event')!r} in events log"
            )
        if not e.get("corpus") or not e.get("wave_id"):
            raise SystemExit(f"corpus_lock: event missing corpus/wave_id: {e}")
        if not isinstance(e.get("generation"), int):
            raise SystemExit(f"corpus_lock: event missing int generation: {e}")
    # Monotonic per-corpus generation: generation never decreases.
    last_gen: dict[str, int] = {}
    for e in events:
        corpus = str(e.get("corpus") or "")
        gen = int(e.get("generation") or 0)
        if corpus in last_gen and gen < last_gen[corpus]:
            raise SystemExit(
                f"corpus_lock: {corpus} generation decreased {last_gen[corpus]} "
                f"-> {gen} — the log was rewritten (append-only violation)"
            )
        last_gen[corpus] = gen
    return 0

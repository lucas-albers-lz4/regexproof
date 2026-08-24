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
    """Append one event durably with O_APPEND + a single ``os.write``.

    Durable: the bytes are written AND fsynced before the fd closes (a
    buffered text stream would need flush-before-fsync — this path skips
    buffering entirely)."""
    path = pathlib.Path(log) if log is not None else EVENTS_LOG
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(event, sort_keys=True) + "\n"
    # 0o600: the events log is operationally sensitive (wave transitions);
    # world-readable 0o644 was flagged by CodeQL (#569). os.open's mode is
    # ignored when the file EXISTS (Luna r8 #1: the tracked log is 0644) —
    # fchmod enforces 0600 unconditionally, new AND existing logs.
    fd = os.open(str(path), os.O_APPEND | os.O_CREAT | os.O_WRONLY, 0o600)
    try:
        os.fchmod(fd, 0o600)
        data = payload.encode("utf-8")
        view = memoryview(data)
        while view:
            n = os.write(fd, view)  # short writes are retried (Luna r2 #10)
            if n <= 0:
                raise OSError(f"corpus_lock: short write to {path}: {n}")
            view = view[n:]
        os.fsync(fd)
    finally:
        os.close(fd)


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


def _with_lock(path: pathlib.Path, fn):
    """Serialize the read/check/append sequence across processes with an
    exclusive flock on the events log (O_APPEND serializes writes, NOT the
    read/check/append transition — Luna r1 fold #2). The log is created
    with 0o600 — an ``a+`` open would otherwise create it 0644 and defeat
    the CodeQL fix (Luna r7)."""
    import fcntl
    import os

    path.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(str(path), os.O_APPEND | os.O_CREAT | os.O_RDWR, 0o600)
    try:
        os.fchmod(fd, 0o600)  # existing logs keep 0600 too (Luna r8 #1)
        fh = os.fdopen(fd, "a+", encoding="utf-8")  # fdopen owns fd from here
    except Exception:
        os.close(fd)  # no leak if fchmod/fdopen raises (Luna r9 note)
        raise
    fcntl.flock(fh.fileno(), fcntl.LOCK_EX)
    try:
        return fn()
    finally:
        fcntl.flock(fh.fileno(), fcntl.LOCK_UN)
        fh.close()


def events_lock(corpus: str, fn, *, log: pathlib.Path | None = None):
    """The corpus lock's SINGLE primitive, exported for queue operations
    (Luna r3 #1): a claim/contract/skip must hold the SAME exclusive flock
    as ``wave_close`` — a per-cluster ``.json.lock`` would be a second
    lock that does not exclude a close racing between claim validation
    and write. The events log is the one lock."""
    path = pathlib.Path(log) if log is not None else EVENTS_LOG
    return _with_lock(path, fn)


def _active_wave_id(corpus: str, log: pathlib.Path | None = None) -> str:
    """The wave_id of the corpus's last event if it is ``wave_opened``."""
    last: dict[str, Any] | None = None
    for e in _read_events(log):
        if e.get("corpus") == corpus:
            last = e
    if last is not None and last.get("event") == OPEN_EVENT:
        return str(last.get("wave_id") or "")
    return ""


def _wave_id_used(corpus: str, wave_id: str, log: pathlib.Path | None = None) -> bool:
    """True if wave_id was EVER used for this corpus (open/close/abort).

    Wave IDs must be unique per corpus (Luna r7 #3): after an abort the
    generation is unchanged, so REUSING the same id would let the aborted
    wave's stale artifact pass the binding check and become claimable."""
    return any(
        e.get("corpus") == corpus and e.get("wave_id") == wave_id
        for e in _read_events(log)
    )


def wave_open(
    corpus: str,
    wave_id: str,
    *,
    log: pathlib.Path | None = None,
) -> int:
    """Open a wave: appends ``wave_opened`` under an exclusive flock. Fails
    closed if the corpus has an active wave (no parallel waves) or if the
    wave_id was EVER used before (Luna r7 #3: reuse after an abort would
    let the stale artifact through). Returns the generation (unchanged).
    ``wave_id`` must be nonblank (Luna r5 #3)."""

    def _open() -> int:
        if not str(wave_id or "").strip():
            raise SystemExit(
                "corpus_lock: wave_open refused — wave_id must be nonblank"
            )
        if wave_status(corpus, log) == "active":
            raise SystemExit(
                f"corpus_lock: {corpus} already has an active wave — close or "
                "abort it before opening another (skip_wave_active)"
            )
        if _wave_id_used(corpus, wave_id, log):
            raise SystemExit(
                f"corpus_lock: {corpus} wave_id {wave_id!r} was used before "
                "(open/close/abort) — wave IDs must be unique per corpus; "
                "choose a fresh id (Luna r7 #3)"
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

    path = pathlib.Path(log) if log is not None else EVENTS_LOG
    return _with_lock(path, _open)


def wave_close(
    corpus: str,
    wave_id: str,
    *,
    force: bool = False,
    skip_reasons: dict[str, str] | None = None,
    queue_root: pathlib.Path | None = None,
    log: pathlib.Path | None = None,
) -> int:
    """Close a wave: appends ``wave_closed`` under an exclusive flock — this
    INCREMENTS generation. The active wave's ``wave_id`` MUST match (a
    wrong-id close is refused — Luna r1 fold #2). ``force=True`` is recorded
    in the event AND is ENFORCED against the queue: every non-contracted
    top-15 candidate must carry a skip reason (Luna r1 fold #4)."""

    def _close() -> int:
        status = wave_status(corpus, log)
        if status == "none":
            raise SystemExit(
                f"corpus_lock: {corpus} has no wave to close — open one first "
                "(pre-Phase-C fallback fails closed)"
            )
        if status == "closed":
            raise SystemExit(f"corpus_lock: {corpus} wave already closed")
        if status == "aborted":
            # CodeRabbit #569 (Critical): an aborted wave must never be
            # closable — the close would increment generation for a wave
            # that is not open (and check_events_log would then flag the
            # illegal transition).
            raise SystemExit(
                f"corpus_lock: {corpus} wave was ABORTED — closing it would "
                "write an illegal transition; open a new wave instead"
            )
        active_id = _active_wave_id(corpus, log)
        if active_id and active_id != wave_id:
            raise SystemExit(
                f"corpus_lock: {corpus} active wave is {active_id!r}, not "
                f"{wave_id!r} — refusing wrong-id close"
            )
        if queue_root is not None:
            # Close-out enforcement runs on EVERY close that names a queue
            # (Luna r7 #4: force=False must not bypass it), and the queue
            # artifact must be CURRENT (generation + wave binding — Luna r7
            # #5: a stale/empty artifact cannot satisfy close-out).
            from regexproof.mine.conversion_queue import (
                load_queue,
                non_contracted_top15,
                SKIP_REASONS,
                _write as _write_queue,
            )

            q = load_queue(corpus, root=queue_root)
            gen_raw = q.get("wave_generation")
            artifact_gen = int(gen_raw) if gen_raw is not None else -1
            if artifact_gen != read_generation(corpus, log):
                raise SystemExit(
                    f"corpus_lock: close-out refused — queue {corpus} artifact "
                    f"generation {artifact_gen} != current "
                    f"{read_generation(corpus, log)} (stale artifact)"
                )
            artifact_wave = str(q.get("wave_id") or "")
            active_id = _active_wave_id(corpus, log)
            if not artifact_wave:
                raise SystemExit(
                    f"corpus_lock: close-out refused — queue {corpus} has no "
                    "wave binding (unbound artifact cannot satisfy close-out; "
                    "Luna r8 #3)"
                )
            if artifact_wave != active_id:
                raise SystemExit(
                    f"corpus_lock: close-out refused — queue {corpus} bound "
                    f"to wave {artifact_wave!r} but active wave is {active_id!r}"
                )
            blockers = non_contracted_top15(q)
            reasons = skip_reasons or {}
            missing = []
            for r in blockers:
                reason = reasons.get(r["site"])
                if not reason or not str(reason).strip():
                    missing.append((r["site"], r.get("status")))
                    continue
                if str(reason).strip() not in SKIP_REASONS:
                    raise SystemExit(
                        f"corpus_lock: close-out refused — skip reason "
                        f"{reason!r} for {r['site']} is not in the queue "
                        f"vocabulary {sorted(SKIP_REASONS)}"
                    )
            if missing:
                raise SystemExit(
                    f"corpus_lock: close-out refused — {len(missing)} "
                    "non-contracted top-15 candidate(s) lack skip reasons: "
                    + ", ".join(f"{s} ({st})" for s, st in missing)
                )
            # Final-gate #2 (MEDIUM): close-out validates skip reasons but
            # must ALSO transition the blocker rows — a row left
            # emitted/claimed after the wave closes blocks the scheduler
            # (its queue check sees PENDING sites) indefinitely. Persist
            # the transitioned rows under the same exclusive lock, BEFORE
            # the close event (the generation bump the close records must
            # reflect the already-skipped queue).
            for r in blockers:
                reason = str(reasons.get(r["site"]) or "").strip()
                for row in q.get("candidate_sites", []):
                    if row.get("site") == r["site"]:
                        row["status"] = f"skipped_{reason}"
                        break
            _write_queue(q, root=queue_root)
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

    path = pathlib.Path(log) if log is not None else EVENTS_LOG
    return _with_lock(path, _close)


def wave_abort(
    corpus: str,
    wave_id: str,
    *,
    reason: str,
    log: pathlib.Path | None = None,
) -> None:
    """Abort a wave (compensation for a stuck/mis-begun wave). Does NOT
    increment generation. Only an ACTIVE wave with a matching wave_id may
    be aborted (a closed/nonexistent wave cannot — Luna r1 fold #2)."""

    def _abort() -> None:
        status = wave_status(corpus, log)
        if status != "active":
            raise SystemExit(
                f"corpus_lock: {corpus} has no active wave to abort "
                f"(status={status})"
            )
        active_id = _active_wave_id(corpus, log)
        if active_id and active_id != wave_id:
            raise SystemExit(
                f"corpus_lock: {corpus} active wave is {active_id!r}, not "
                f"{wave_id!r} — refusing wrong-id abort"
            )
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

    path = pathlib.Path(log) if log is not None else EVENTS_LOG
    _with_lock(path, _abort)


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
    """CI append-only + transition check. Every line parses; per-corpus
    generation is monotonic AND equals the running closed-event count; every
    transition is legal (close/abort require a preceding open; open requires
    no active wave); a close-without-open or wrong-id close is a violation.
    Returns 0 (or raises)."""
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
    # Per-corpus state machine: monotonic generation AND legal transitions.
    state: dict[str, str] = {}  # corpus -> last event kind
    closed_count: dict[str, int] = {}
    active_id: dict[str, str] = {}
    used_ids: dict[str, set[str]] = {}  # corpus -> set of used wave_ids
    for e in events:
        corpus = str(e.get("corpus") or "")
        kind = str(e.get("event") or "")
        gen = int(e.get("generation") or 0)
        wave_id = str(e.get("wave_id") or "")
        before = closed_count.get(corpus, 0)
        # A close event records the POST-flip generation (before + 1);
        # open/abort record the unchanged pre-flip count.
        expected_gen = before + 1 if kind == CLOSE_EVENT else before
        if gen != expected_gen:
            raise SystemExit(
                f"corpus_lock: {corpus} event generation {gen} != expected "
                f"{expected_gen} — the log was rewritten or miscalculated "
                "(append-only violation)"
            )
        # Wave-id uniqueness per corpus (Luna r8 #2: the CI gate must agree
        # with wave_open's guard — open w1 → close w1 → open w1 must fail).
        used = used_ids.setdefault(corpus, set())
        if kind == OPEN_EVENT:
            if wave_id in used:
                raise SystemExit(
                    f"corpus_lock: {corpus} reuses wave_id {wave_id!r} — wave "
                    "IDs must be unique per corpus (append-only violation)"
                )
        used.add(wave_id)
        if kind == OPEN_EVENT:
            if state.get(corpus) == OPEN_EVENT:
                raise SystemExit(
                    f"corpus_lock: {corpus} opened while active (wave "
                    f"{active_id.get(corpus, '?')}) — parallel waves violate "
                    "the single-primitive lock"
                )
            state[corpus] = OPEN_EVENT
            active_id[corpus] = wave_id
        elif kind == CLOSE_EVENT:
            if state.get(corpus) != OPEN_EVENT:
                raise SystemExit(
                    f"corpus_lock: {corpus} closed without an open wave — "
                    "illegal transition (append-only violation)"
                )
            if active_id.get(corpus) != wave_id:
                raise SystemExit(
                    f"corpus_lock: {corpus} closed with wrong wave_id "
                    f"{wave_id!r} (active {active_id.get(corpus, '?')!r})"
                )
            closed_count[corpus] = gen
            state[corpus] = CLOSE_EVENT
        elif kind == ABORT_EVENT:
            if state.get(corpus) != OPEN_EVENT:
                raise SystemExit(
                    f"corpus_lock: {corpus} aborted without an open wave — "
                    "illegal transition"
                )
            if active_id.get(corpus) != wave_id:
                raise SystemExit(
                    f"corpus_lock: {corpus} aborted with wrong wave_id "
                    f"{wave_id!r} (active {active_id.get(corpus, '?')!r})"
                )
            state[corpus] = ABORT_EVENT
    return 0

"""7-day escape-clause window (#576 Wave 7).

The batch projection's old ``survivor_rate`` was pooled ``ok`` / total probe
rows — a walk-outcome rate, not the shared-gate stop signal.

This module computes the live window the escape clause actually names:

- ``n`` = probe outcomes **completed** in the window (``batch/state.json``).
  Timeouts, ``disk_budget``, ``skip_wave_active``, and other non-ok outcomes
  still count. Incomplete rows (no ``completed_at``) do not.
- ``k`` = those probes whose committed gate decision is ``go`` or
  ``triage-trial`` (joined on ``(url, pin)``).

When ``n == 0`` the rate is ``None`` — never fall back to counting gate
decision files alone (that would mix the historical mine population into
the live window). The baseline itself stays the frozen Phase 0 constant.
"""

from __future__ import annotations

import datetime as dt
import json
import pathlib
from typing import Any

from regexproof.mine.batch_state import load_state
from regexproof.stats.intervals import two_proportion_test

POSITIVE = frozenset({"go", "triage-trial"})
WINDOW_DAYS = 7
GEN = pathlib.Path("properties/generated")
BASELINE_PATH = GEN / "escape_baseline.json"


def _parse_iso(value: str) -> dt.datetime | None:
    text = (value or "").strip()
    if not text:
        return None
    try:
        parsed = dt.datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        try:
            parsed = dt.datetime.strptime(text[:10], "%Y-%m-%d")
        except ValueError:
            return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.astimezone(dt.timezone.utc)


def _decision_status(payload: dict[str, Any]) -> str:
    return str(payload.get("status") or payload.get("decision") or "")


def _decision_pin(payload: dict[str, Any]) -> str:
    probe = payload.get("probe") if isinstance(payload.get("probe"), dict) else {}
    return str(payload.get("corpus_pin") or probe.get("pin") or "")


def _decision_recency(payload: dict[str, Any]) -> dt.datetime | None:
    return _parse_iso(str(payload.get("decision_date") or payload.get("updated_at") or ""))


def _index_decisions(gen: pathlib.Path) -> dict[tuple[str, str], dict[str, Any]]:
    indexed: dict[tuple[str, str], dict[str, Any]] = {}
    recency: dict[tuple[str, str], dt.datetime] = {}
    if not gen.is_dir():
        return indexed
    for path in sorted(gen.glob("*_gate_decision.json")):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            raise SystemExit(
                f"escape_window: unreadable/invalid gate decision {path}: {exc}"
            ) from exc
        url = str(payload.get("candidate_url") or "")
        pin = _decision_pin(payload)
        if not url or not pin:
            continue
        key = (url, pin)
        when = _decision_recency(payload)
        if key not in indexed:
            indexed[key] = payload
            recency[key] = when  # may be None until a duplicate appears
            continue
        if when is None or recency[key] is None:
            raise SystemExit(
                f"escape_window: duplicate (url, pin) {key} in {path} has no "
                "decision_date/updated_at — fail closed"
            )
        prev = recency[key]
        # Same policy as freeze supersession: later recency wins; equal
        # recency keeps the last file in sorted-path order (deterministic,
        # matches load_decision_population).
        if when >= prev:
            indexed[key] = payload
            recency[key] = when
    return indexed


def _load_baseline(path: pathlib.Path) -> float:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return float(payload["survivor_rate"])


def escape_window(
    *,
    state_path: pathlib.Path | None = None,
    gen: pathlib.Path | None = None,
    baseline_path: pathlib.Path | None = None,
    now: dt.datetime | None = None,
    window_days: int = WINDOW_DAYS,
) -> dict[str, Any]:
    """Compute the 7-day escape window vs the frozen baseline.

    Returns ``n_window``, ``k_window``, ``rate`` (or ``None`` when n=0),
    ``baseline``, and when n>0 the ``two_proportion_test`` fields including
    ``fires``.
    """
    clock = now or dt.datetime.now(dt.timezone.utc)
    if clock.tzinfo is None:
        clock = clock.replace(tzinfo=dt.timezone.utc)
    start = clock - dt.timedelta(days=window_days)

    reg = load_state(state_path)
    raw_rows = (
        list(reg["rows"].values())
        if isinstance(reg.get("rows"), dict)
        else list(reg.get("rows") or [])
    )
    window_rows = []
    for row in raw_rows:
        completed = _parse_iso(str(row.get("completed_at") or ""))
        if completed is None:
            continue
        if start <= completed <= clock:
            window_rows.append(row)

    n_window = len(window_rows)
    decisions = _index_decisions(gen if gen is not None else GEN)
    k_window = 0
    for row in window_rows:
        payload = decisions.get((str(row.get("url") or ""), str(row.get("pin") or "")))
        if payload is not None and _decision_status(payload) in POSITIVE:
            k_window += 1

    baseline = _load_baseline(baseline_path if baseline_path is not None else BASELINE_PATH)
    result: dict[str, Any] = {
        "n_window": n_window,
        "k_window": k_window,
        "rate": (k_window / n_window) if n_window else None,
        "baseline": baseline,
        "window_days": window_days,
        "fires": None,
    }
    if n_window > 0:
        test = two_proportion_test(k_window, n_window, baseline)
        result["fires"] = test["fires"]
        result["p_value"] = test["p_value"]
        result["z"] = test["z"]
    return result

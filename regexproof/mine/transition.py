"""P2-owned candidate status transitions (umbrella C3 / Sonnet C / D4)."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from regexproof.mine.ledger import find_candidate, load_ledger, save_ledger

# Statuses P2 creates / may transition among. P3 re-queue lands on queued.
P2_STATUSES = frozenset({"queued", "mined", "gated:go", "gated:no-go", "gated:triage-trial"})

# Decision → ledger status mapping (gate_decision.schema.json decision field).
DECISION_STATUS_MAP: dict[str, str] = {
    "go": "gated:go",
    "no-go": "gated:no-go",
    "triage-trial": "gated:triage-trial",
}

# Allowed edges: from → to (P2-owned). re-queue is any known → queued when
# explicitly requested for audit failure recovery.
_ALLOWED: dict[str, frozenset[str]] = {
    "queued": frozenset({"mined", "queued", "gated:go", "gated:no-go", "gated:triage-trial"}),
    "mined": frozenset({"queued", "gated:go", "gated:no-go", "gated:triage-trial"}),
}


class TransitionError(ValueError):
    """Illegal or missing candidate status transition."""


def transition_candidate(
    ledger_path: Path | str,
    url: str,
    *,
    to: str,
    reason: str = "",
) -> dict[str, Any]:
    """Atomically set candidate ``status`` via the P2-owned transition API.

    P3 must call this to re-queue (``to="queued"``) — it must not write
    ``status`` fields directly. Existing ``audit`` objects are preserved.
    Supports gated statuses: ``gated:go``, ``gated:no-go``, ``gated:triage-trial``.
    """
    if to not in P2_STATUSES:
        raise TransitionError(
            f"target status {to!r} is not P2-owned; expected one of {sorted(P2_STATUSES)}"
        )
    ledger = load_ledger(ledger_path)
    cand = find_candidate(ledger, url)
    if cand is None:
        raise TransitionError(f"candidate not in ledger: {url}")
    current = cand.get("status")
    if current not in _ALLOWED or to not in _ALLOWED[current]:
        raise TransitionError(
            f"illegal transition {current!r} → {to!r} for {url}"
            + (f" ({reason})" if reason else "")
        )
    # Preserve audit and all other fields; only status changes.
    cand["status"] = to
    if reason:
        audit = cand.setdefault("audit", {})
        if not isinstance(audit, dict):
            raise TransitionError("candidate audit must be an object when present")
        transitions = audit.setdefault("transitions", [])
        if not isinstance(transitions, list):
            raise TransitionError("audit.transitions must be a list")
        transitions.append({"to": to, "reason": reason})
    save_ledger(ledger_path, ledger)
    return cand


def set_status(
    ledger_path: Path | str,
    url: str,
    *,
    decision: str,
    reason: str = "",
) -> dict[str, Any]:
    """Map a gate decision string to the corresponding gated status and transition.

    ``decision`` must be one of ``"go"``, ``"no-go"``, ``"triage-trial"``.
    Convenience wrapper around :func:`transition_candidate`.
    """
    status = DECISION_STATUS_MAP.get(decision)
    if status is None:
        raise TransitionError(
            f"unknown gate decision {decision!r}; expected one of {sorted(DECISION_STATUS_MAP)}"
        )
    return transition_candidate(ledger_path, url, to=status, reason=reason or f"gate:{decision}")

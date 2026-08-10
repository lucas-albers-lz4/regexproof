"""Shared TIMEOUT hard-fail gate for shape-5 rule_diff pilots (issue #186).

AGENTS.md: TIMEOUT (unknown) = hard failure / not proven, never a silent skip.
Named allowlists are the only exception — a global rate is not auditable.
"""

from __future__ import annotations

from typing import Any, Iterable


def count_timeouts(results: Iterable[dict[str, Any]], *, result_key: str = "result") -> int:
    return sum(1 for r in results if r.get(result_key) == "timeout")


def timeout_gate(
    results: Iterable[dict[str, Any]],
    *,
    result_key: str = "result",
    allowlist: frozenset[str] | None = None,
    name_key: str = "name",
) -> tuple[bool, int, float, list[str]]:
    """Return (ok, n_timeout, timeout_rate, non_allowlisted_timeout_names).

    ok is True iff every timeout is named in *allowlist* (default: empty — zero
    timeouts required). Seeds pilot consolidation (#194).
    """
    rows = list(results)
    allow = allowlist or frozenset()
    timed_out = [r for r in rows if r.get(result_key) == "timeout"]
    n_timeout = len(timed_out)
    rate = n_timeout / len(rows) if rows else 0.0
    bad_names = [
        str(r.get(name_key) or r.get("family") or "<unnamed>")
        for r in timed_out
        if str(r.get(name_key) or r.get("family") or "") not in allow
    ]
    return (len(bad_names) == 0, n_timeout, rate, bad_names)


def fail_message(bad_names: list[str], n_timeout: int) -> str:
    return (
        f"FAIL timeout gate: {n_timeout} timeout(s) — TIMEOUT is not proven "
        f"(non-allowlisted: {', '.join(bad_names)})"
    )

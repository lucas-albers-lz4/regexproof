"""ReDoS finding schema helpers (Phase 4)."""

from __future__ import annotations

from typing import Any

REDOS_SCHEMA_VERSION = "1"
REDOS_RESULTS = frozenset({"vulnerable", "safe", "error", "timeout", "unsupported"})


def make_finding(
    *,
    regex_id: str,
    tool: str,
    tool_version: str,
    result: str,
    dialect: str,
    pattern: str,
    flags: str,
    site: str,
    severity: str | None = None,
    confidence: str | None = None,
    source: dict[str, Any] | None = None,
    error_message: str | None = None,
    detail: dict[str, Any] | None = None,
) -> dict[str, Any]:
    if result not in REDOS_RESULTS:
        raise ValueError(f"invalid result {result!r}")
    # Never coerce error/timeout/unsupported into safe — caller must pass result as-is.
    rec: dict[str, Any] = {
        "schema_version": REDOS_SCHEMA_VERSION,
        "regex_id": regex_id,
        "tool": tool,
        "tool_version": tool_version,
        "result": result,
        "severity": severity,
        "confidence": confidence,
        "dialect": dialect,
        "pattern": pattern,
        "flags": flags,
        "site": site,
        "source": source or {},
        "error_message": error_message,
    }
    if detail is not None:
        rec["detail"] = detail
    return rec

"""Shared compiler types and Z3 helpers."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import z3
from z3 import AllChar, Concat, Loop, Plus, Re, Star, Union


class Unencodable(Exception):
    """Pattern cannot be faithfully encoded; reason is the triage key."""

    def __init__(self, reason: str):
        super().__init__(reason)
        self.reason = reason


def helper_gate_missing(helper_name: str) -> dict:
    """Fail-closed gate when a dialect helper is unavailable (#172).

    Returns ``ok: False`` so existing ``if gate.get("ok") is False`` paths
    refuse to encode — never soft-open with ``ok: True``.
    """
    return {
        "ok": False,
        "helper": f"{helper_name}-missing",
        "error": f"{helper_name} helper unavailable",
    }


@dataclass
class CompileResult:
    mirror: Any | None
    unencodable_reason: str | None
    dialect: str
    call_kind: str
    flags: str
    pattern: str
    declared_domain: str  # "ascii" | "unicode"

    @property
    def encodable(self) -> bool:
        return self.mirror is not None and self.unencodable_reason is None


def any_char():
    return AllChar(Re("").sort())


def opt(r):
    """Regex optional — never z3.Opt (optimizer)."""
    return Union(r, Re(""))


def repeat_z3(body, lo: int, hi: int | None):
    """Shared ``{lo,hi}`` / ``*`` / ``+`` lowering for all dialects.

    Consolidation only (fix-wave #73) — preserves the ``lo == hi == 1``
    identity from Phase 1 / TRAPS #20 (do not re-derive that fix here).
    ``hi is None`` means unbounded.
    """
    if lo == 0 and hi == 1:
        return opt(body)
    if lo == 0 and hi is None:
        return Star(body)
    if lo == 1 and hi is None:
        return Plus(body)
    if hi is None:
        return Concat(*([body] * lo), Star(body)) if lo else Star(body)
    if lo == hi:
        if lo <= 0:
            return Re("")
        if lo == 1:
            # Z3 Concat requires ≥2 args; `{1}` / `{1,1}` is identity (TRAPS #20).
            return body
        return Concat(*([body] * lo))
    return Loop(body, lo, hi)


def wrap_call_kind(body, call_kind: str, *, trailing_dollar_nl: bool = False):
    """Apply call_kind wrapper after anchors have been translated into `body`.

    Anchors themselves are handled in the dialect translators. This only adds
    the search/match prefix/suffix Star(any) wrappers when needed.
    """
    any_c = any_char()
    if call_kind == "fullmatch":
        return body
    if call_kind == "match":
        # Prefix match: pattern || .*
        return Concat(body, Star(any_c))
    if call_kind in ("search", "exec"):
        return Concat(Star(any_c), body, Star(any_c))
    if call_kind == "substitution":
        # Bounded substitution mirrors use search-shaped membership for v1.
        return Concat(Star(any_c), body, Star(any_c))
    raise Unencodable(f"unsupported-call_kind:{call_kind}")


def python_trailing_dollar(body):
    """Python/PCRE `$` matches before a trailing newline."""
    return Concat(body, Union(Re(""), Re("\n")))

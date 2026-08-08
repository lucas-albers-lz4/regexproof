"""Complement-free shape-5 encoding: InRe(s, R2) ∧ ¬InRe(s, R1)."""

from __future__ import annotations

from typing import Any

from z3 import InRe, Length, Not, String


def shape5_constraints(
    r1_mirror: Any,
    r2_mirror: Any,
    *,
    min_len: int = 1,
    max_len: int = 64,
    string_name: str = "s",
) -> tuple[list, Any, Any]:
    """Return (constraints, bad, s) for a gap query.

    `bad` is the gap predicate itself (SAT ⇒ R2 accepts something R1 misses).
    Callers that expect UNSAT for \"no gap\" pass expect_unsat=True with this bad.
    Never builds regex Complement — uses Not(InRe(...)) only.
    """
    s = String(string_name)
    constraints = [
        Length(s) >= min_len,
        Length(s) <= max_len,
    ]
    bad = InRe(s, r2_mirror) & Not(InRe(s, r1_mirror))
    return constraints, bad, s

"""Construct counters for admission probe patterns (P1 A3)."""

from __future__ import annotations

import re
from collections import Counter

# (vocab construct key, compiled pattern). Order matters only for readability.
_CONSTRUCT_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("(?x)", re.compile(r"\(\?x\)|\(\?[^)]*x[^):]*[:)]")),
    ("(?i)", re.compile(r"\(\?i\)|\(\?[^)]*i[^):]*[:)]")),
    ("(?s)", re.compile(r"\(\?s\)|\(\?[^)]*s[^):]*[:)]")),
    ("(?m)", re.compile(r"\(\?m\)|\(\?[^)]*m[^):]*[:)]")),
    ("lookaround", re.compile(r"\(\?(?:[=!]|<=|<!)")),
    ("\\K", re.compile(r"\\K")),
    ("\\g{", re.compile(r"\\g\{")),
    ("posix-class", re.compile(r"\[\[:[a-z]+:\]\]")),
    # Numeric / named backrefs only — \\g{ is counted separately above.
    ("backref", re.compile(r"\\[1-9]|(?:\?P=)")),
]


def count_constructs(pattern: str) -> dict[str, int]:
    """Return construct → count for a single pattern string."""
    out: Counter[str] = Counter()
    for key, rx in _CONSTRUCT_PATTERNS:
        n = len(rx.findall(pattern))
        if n:
            out[key] += n
    return dict(out)


def accumulate_constructs(patterns: list[str]) -> dict[str, int]:
    """Sum construct counts across many patterns."""
    total: Counter[str] = Counter()
    for pat in patterns:
        total.update(count_constructs(pat))
    return dict(total)

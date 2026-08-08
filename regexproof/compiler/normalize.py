"""Corpus-facing normalization before dialect compile (Phase 2 pilots)."""

from __future__ import annotations

import re


_INLINE_FLAG = re.compile(r"^\(\?([imsx]+)\)")


def normalize_inline_flags(pattern: str, flags: str = "") -> tuple[str, str]:
    """Lift leading `(?i)` / `(?is)` style flags into the flags string.

    Gitleaks and many rule corpora embed case-insensitivity this way; the
    Phase-1 reject of mid-pattern inline flags still applies after the lift.
    """
    flag_set = set(flags)
    while True:
        m = _INLINE_FLAG.match(pattern)
        if not m:
            break
        flag_set.update(m.group(1))
        pattern = pattern[m.end() :]
    return pattern, "".join(sorted(flag_set))

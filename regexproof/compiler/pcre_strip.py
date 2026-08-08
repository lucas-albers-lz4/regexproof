"""Strip language-transparent regex constructs without touching char classes.

Membership (language) is unchanged by:
- atomic groups `(?>…)` → `(?:…)`
- possessive quantifiers `++` `*+` `?+` `{n,m}+` → drop the trailing `+`
- lazy quantifiers `*?` `+?` `??` `{n,m}?` → drop the trailing `?`
"""

from __future__ import annotations

import re

_REPEAT_BRACE_RE = re.compile(r"\{\d+(?:,\d*)?$")


def _closes_hex_brace(out: list[str]) -> bool:
    """True if ``out`` ends with an unclosed ``\\x{HEX`` (not a ``{n,m}`` brace)."""
    s = "".join(out)
    idx = s.rfind("\\x{")
    if idx < 0:
        return False
    mid = s[idx + 3 :]
    if "}" in mid:
        return False
    return bool(mid) and all(c in "0123456789abcdefABCDEF" for c in mid)


def _closes_repeat_brace(out: list[str]) -> bool:
    """True if ``out`` ends with an open ``{n``, ``{n,``, or ``{n,m`` quantifier."""
    return bool(_REPEAT_BRACE_RE.search("".join(out)))


def strip_atomic_and_possessive(pattern: str) -> str:
    """Replace `(?>` with `(?:` and drop possessive `+` after quantifiers.

    Only operates outside character classes so e.g. `[*+]` is unchanged.
    Does not treat ``\\x{…}+`` as possessive (the ``}`` closes a hex escape).
    """
    out: list[str] = []
    i = 0
    in_class = False
    while i < len(pattern):
        ch = pattern[i]
        if ch == "\\" and i + 1 < len(pattern):
            out.append(ch)
            out.append(pattern[i + 1])
            i += 2
            continue
        if not in_class and ch == "[":
            in_class = True
            out.append(ch)
            i += 1
            continue
        if in_class and ch == "]":
            in_class = False
            out.append(ch)
            i += 1
            continue
        if not in_class and pattern.startswith("(?>", i):
            out.append("(?:")
            i += 3
            continue
        if (
            not in_class
            and ch in "+*?}"
            and i + 1 < len(pattern)
            and pattern[i + 1] == "+"
        ):
            if ch == "}":
                if _closes_hex_brace(out):
                    out.append(ch)
                    i += 1
                    continue
                if not _closes_repeat_brace(out):
                    # Literal `}` + `+` (e.g. `a}+`) — not a possessive quantifier.
                    out.append(ch)
                    i += 1
                    continue
            # Possessive quantifier: ++, *+, ?+, {n,m}+
            out.append(ch)
            i += 2
            continue
        out.append(ch)
        i += 1
    return "".join(out)


def strip_lazy_quantifiers(pattern: str) -> str:
    """Drop lazy `?` after quantifiers outside character classes.

    `a*?` → `a*`, `a+?` → `a+`, `a??` → `a?`, `a{2,3}?` → `a{2,3}`.
    Char-class contents such as `[?]` are unchanged.
    Does not treat ``\\x{…}?`` as lazy (optional hex atom keeps its ``?``).
    """
    out: list[str] = []
    i = 0
    in_class = False
    while i < len(pattern):
        ch = pattern[i]
        if ch == "\\" and i + 1 < len(pattern):
            out.append(ch)
            out.append(pattern[i + 1])
            i += 2
            continue
        if not in_class and ch == "[":
            in_class = True
            out.append(ch)
            i += 1
            continue
        if in_class and ch == "]":
            in_class = False
            out.append(ch)
            i += 1
            continue
        if (
            not in_class
            and ch in "+*?}"
            and i + 1 < len(pattern)
            and pattern[i + 1] == "?"
        ):
            if ch == "}":
                if _closes_hex_brace(out):
                    out.append(ch)
                    i += 1
                    continue
                if not _closes_repeat_brace(out):
                    # Literal `}` + `?` — keep both (not a lazy `{n,m}?`).
                    out.append(ch)
                    i += 1
                    continue
            out.append(ch)
            i += 2  # skip lazy marker
            continue
        out.append(ch)
        i += 1
    return "".join(out)


def strip_language_transparent(pattern: str) -> str:
    """Apply all language-transparent strips (atomic/possessive, then lazy)."""
    return strip_lazy_quantifiers(strip_atomic_and_possessive(pattern))

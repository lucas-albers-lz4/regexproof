"""Strip PCRE language-transparent constructs without touching char classes."""

from __future__ import annotations


def strip_atomic_and_possessive(pattern: str) -> str:
    """Replace `(?>` with `(?:` and drop possessive `+` after quantifiers.

    Only operates outside character classes so e.g. `[*+]` is unchanged.
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
            # Possessive quantifier: ++, *+, ?+, {n,m}+
            # For `++`, first `+` is the quantifier; second is possessive.
            out.append(ch)
            i += 2
            continue
        out.append(ch)
        i += 1
    return "".join(out)

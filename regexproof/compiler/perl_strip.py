"""Perl language-transparent strips (Wave 3 / #113).

``\\K`` resets the match start without changing membership — strip it outside
character classes (same class-awareness as ``pcre_strip``).
"""

from __future__ import annotations

from regexproof.compiler.pcre_strip import strip_language_transparent


def strip_k_reset(pattern: str) -> str:
    """Remove ``\\K`` outside character classes."""
    out: list[str] = []
    i = 0
    in_class = False
    while i < len(pattern):
        ch = pattern[i]
        if ch == "\\" and i + 1 < len(pattern):
            nxt = pattern[i + 1]
            if not in_class and nxt == "K":
                i += 2
                continue
            out.append(ch)
            out.append(nxt)
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
        out.append(ch)
        i += 1
    return "".join(out)


def strip_perl_transparent(pattern: str) -> str:
    """``strip_k_reset`` ∘ ``strip_language_transparent``."""
    return strip_k_reset(strip_language_transparent(pattern))

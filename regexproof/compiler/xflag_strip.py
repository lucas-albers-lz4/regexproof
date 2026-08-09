"""Extraction-time ``(?x)`` / verbose-flag pre-pass (Corpus Wave 3 / #114).

Strips verbose whitespace and ``#``-to-EOL comments when ``x`` mode is on,
consumes ``(?±imsx)`` flag groups (lifting encountered letters), and removes
``(?#…)`` comment groups. Character-class contents are left literal.

Compilers must still reject residual ``x`` fail-closed (see ``compile_re2``).
"""

from __future__ import annotations

_FLAG_CHARS = frozenset("imsx")


def strip_verbose_x(pattern: str) -> tuple[str, str]:
    """Return ``(stripped_pattern, lifted_flags)``.

    ``lifted_flags`` is the sorted unique set of ``imsx`` letters encountered
    in consumed ``(?…)`` / ``(?-…)`` groups. ``x`` mode toggles stripping of
    unescaped whitespace and ``#`` comments outside character classes.
    """
    out: list[str] = []
    lifted: set[str] = set()
    x_mode = False
    in_class = False
    i = 0
    n = len(pattern)
    while i < n:
        ch = pattern[i]
        if ch == "\\" and i + 1 < n:
            # Escapes stay literal (including escaped whitespace / #).
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
        if not in_class and pattern.startswith("(?#", i):
            # Comment group — strip entirely (language-transparent; go-re2 rejects).
            i = _skip_paren_comment(pattern, i)
            continue
        if not in_class and pattern.startswith("(?", i):
            consumed = _try_consume_flag_group(pattern, i)
            if consumed is not None:
                end, enable, disable = consumed
                lifted.update(enable)
                lifted.update(disable)
                if "x" in enable:
                    x_mode = True
                if "x" in disable:
                    x_mode = False
                i = end
                continue
        if x_mode and not in_class:
            if ch.isspace():
                i += 1
                continue
            if ch == "#":
                # Comment to end of line (outside classes).
                while i < n and pattern[i] != "\n":
                    i += 1
                continue
        out.append(ch)
        i += 1
    return "".join(out), "".join(sorted(lifted))


def _skip_paren_comment(pattern: str, i: int) -> int:
    """Skip ``(?#…)`` starting at ``i``; return index after closing ``)``."""
    # i points at '(' of '(?#'
    j = i + 3
    n = len(pattern)
    while j < n:
        if pattern[j] == "\\" and j + 1 < n:
            j += 2
            continue
        if pattern[j] == ")":
            return j + 1
        j += 1
    return n


def _try_consume_flag_group(
    pattern: str, i: int
) -> tuple[int, set[str], set[str]] | None:
    """Parse flag-only ``(?flags)`` / ``(?-flags)`` / ``(?on-off)`` at ``i``.

    Returns ``(end_index, enable_set, disable_set)`` or ``None`` if this is
    not a flag-only group (scoped ``(?i:…)``, lookaround, non-capturing, …).
    """
    if not pattern.startswith("(?", i):
        return None
    j = i + 2
    n = len(pattern)
    if j >= n or pattern[j] not in "-imsx":
        return None
    body_chars: list[str] = []
    while j < n:
        c = pattern[j]
        if c == ")":
            break
        if c == ":":
            # Scoped inline flags — leave for the dialect compiler.
            return None
        if c in _FLAG_CHARS or c == "-":
            body_chars.append(c)
            j += 1
            continue
        return None
    if j >= n or pattern[j] != ")":
        return None
    body = "".join(body_chars)
    if not body or body == "-":
        return None
    enable: set[str] = set()
    disable: set[str] = set()
    if body.startswith("-"):
        rest = body[1:]
        if not rest or any(c not in _FLAG_CHARS for c in rest):
            return None
        disable.update(rest)
    elif "-" in body:
        on, _, off = body.partition("-")
        if not on or not off:
            return None
        if any(c not in _FLAG_CHARS for c in on + off):
            return None
        enable.update(on)
        disable.update(off)
    else:
        if any(c not in _FLAG_CHARS for c in body):
            return None
        enable.update(body)
    return j + 1, enable, disable

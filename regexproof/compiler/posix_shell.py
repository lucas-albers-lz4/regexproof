"""POSIX-shell compiler route: BRE→ERE normalize + pcre backend.

Dialect ``posix-shell`` (ONE dialect — user decision 2026-08-12).  The
BRE/ERE semantics fork is real and is carried in the record ``shell_flags``
field (``syntax``: bre | ere | bash_ksh), NOT as a dialect split.

BRE = GNU/busybox flavor (the OpenWrt target).  ``\\+`` ``\\?`` ``\\|`` are
POSIX-undefined but GNU/busybox-supported quantifiers (machine-verified on
GNU grep 3.11 + busybox 1.37, 2026-08-12).

Normalize is ENTRY-ONLY: it runs once in ``compile_pattern`` (before the
caret_in_x / trailing_alt_dollar hooks, which then see normalized ERE text)
and is NEVER re-run in ``compile_bare``/``_compile_dialect`` — a re-normalize
would round-trip BRE ``\\+`` → ``+`` → ``\\+`` and cancel the fix.  Callers
of ``_compile_dialect`` directly must pass already-normalized text.
"""

from __future__ import annotations

from regexproof.compiler.base import CompileResult, Unencodable

# Backslash-escapes whose meaning is IDENTICAL in GNU BRE and pcre — kept
# as-is.  Everything else after a backslash drops the backslash (GNU grep
# BRE treats unknown escapes as the literal char; pcre would otherwise read
# ``\d``/``\w``/``\s``/``\b`` as classes/boundaries and diverge).
_KEEP_ESCAPED = frozenset(r".*^$[]\-\\")


def normalize_shell(pattern: str, syntax: str) -> str:
    """Two-direction BRE→ERE transform (BRE) or pass-through (ERE).

    BRE-syntax records:
      - unescape BRE escapes: ``\\(`` ``\\)`` ``\\{`` ``\\}`` ``\\|``
        ``\\+`` ``\\?`` → bare group/quantifier syntax
      - literal-escape: bare ``+`` ``?`` ``{`` ``|`` ``(`` ``)`` in a BRE
        record are LITERALS (BRE has no unescaped group syntax) and are
        escaped so the ERE/pcre compile does not widen or re-parse them
      - unknown escapes drop the backslash (grep literal semantics)
      - GNU ``\\<`` ``\\>`` word boundaries → Unencodable("gnu-word-boundary")
      - BRE backrefs ``\\(...\\)\\1`` → Unencodable("backref")
    ERE-syntax records (``ere``/``bash_ksh``): pass-through with ONE
    exception — a ``(?`` sequence is Unencodable("inline-flag-like"): GNU
    grep ERE has no inline modifiers (``grep -E '(?i)foo'`` warns ``? at
    start of expression`` and matches nothing; ``grep -E '(?:foo)'`` warns
    and matches the literal text — verified GNU grep 3.11 + busybox 1.37),
    while pcre would read ``(?i)``/``(?:`` as flag/group syntax.  BRE-syntax
    ``(?i)`` is handled by the literal-escape direction (compiles to
    literal text, matching grep BRE).
    """
    if syntax in ("ere", "bash_ksh"):
        if "(?" in pattern:
            raise Unencodable("inline-flag-like")
        return pattern
    out: list[str] = []
    i, n = 0, len(pattern)
    while i < n:
        c = pattern[i]
        if c == "\\":
            if i + 1 >= n:
                out.append("\\")
                break
            nxt = pattern[i + 1]
            if nxt in "(){}|+?":
                out.append(nxt)  # unescape BRE quantifier/group
            elif nxt in "<>":
                raise Unencodable("gnu-word-boundary")
            elif nxt in "123456789":
                raise Unencodable("backref")
            elif nxt in _KEEP_ESCAPED:
                out.append(c)
                out.append(nxt)
            else:
                out.append(nxt)  # drop backslash — grep treats as literal
            i += 2
            continue  # do NOT fall through to the bottom i += 1 (net +3 skips)
        elif c in "+?{|(":
            out.append("\\")  # literal-escape: BRE bare = literal
            out.append(c)
        elif c == ")":
            out.append("\\")  # bare ) is literal in BRE; pcre errors on it
            out.append(c)
        else:
            out.append(c)
        i += 1
    return "".join(out)


def compile_posix_shell(
    pattern: str,
    flags: str = "",
    call_kind: str = "search",
    *,
    max_length: int,
    domain: str = "ascii",
) -> CompileResult:
    """Compile an ALREADY-NORMALIZED posix-shell pattern via the pcre path.

    No normalize here — entry-only rule.  The result reports the
    ``posix-shell`` dialect and the (normalized) pattern text actually
    compiled; the record keeps its own original pattern.
    """
    from regexproof.compiler.pcre import compile_pcre  # noqa: PLC0415 — lazy
    # import matches the repo's per-dialect convention (avoid loading pcre/z3
    # helpers at module import)

    result = compile_pcre(
        pattern, flags=flags, call_kind=call_kind, max_length=max_length
    )
    return CompileResult(
        mirror=result.mirror,
        unencodable_reason=result.unencodable_reason,
        dialect="posix-shell",
        call_kind=call_kind,
        flags=flags,
        pattern=pattern,
        declared_domain=result.declared_domain,
    )

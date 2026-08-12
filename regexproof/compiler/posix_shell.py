"""POSIX-shell compiler route: BRE→ERE normalize + pcre backend.

Dialect ``posix-shell`` (ONE dialect — user decision 2026-08-12).  The
BRE/ERE semantics fork is real and is carried in the record ``shell_flags``
field (``syntax``: bre | ere | bash_ksh), NOT as a dialect split.

Escape semantics are MACHINE-VERIFIED on GNU grep 3.11 + busybox 1.37
(2026-08-12, ground-truth probes committed with the tests):

- ``\\+`` ``\\?`` ``\\|`` are POSIX-undefined but GNU/busybox-supported
  quantifiers in BRE; ERE backslash-metas (``\\+`` ``\\?`` ``\\{n\\}`` …)
  are LITERALS on both engines, and pcre reads them identically.
- ``\\w \\W \\s \\S \\b \\B`` are GNU/busybox shorthand CLASSES /
  BOUNDARIES in both BRE and ERE (probe: ``grep '\\w'`` matches every line
  containing a word char; ``grep 'a\\b'`` matches ``a b``) — pcre's
  semantics differ (locale/position), so they are REJECTED
  (``gnu-extension``), not silently translated.
- ``\\< \\>`` are GNU word-boundary extensions → rejected
  (``gnu-word-boundary``).
- ``\\d`` and other unknown escapes are the LITERAL char on both engines
  (probe: ``grep 'a\\d'`` matches ``ad``, not ``a0``) — pcre would read
  ``\\d`` as a digit class, so the backslash is DROPPED to keep the two
  engines agreeing.
- BRE ``\\(...\\)\\1`` backrefs → Unencodable("backref").  ERE has no
  backrefs: ``\\1`` is the literal ``1`` (backslash dropped).
- grep ERE has no inline modifiers: ``(?i)`` warns ``? at start of
  expression`` and matches nothing; ``(?:`` warns and matches the literal
  text — a ``(?`` sequence in an ERE record is rejected
  (``inline-flag-like``) because pcre would read it as flag/group syntax.
  BRE ``(?i)`` compiles as literal text via the literal-escape direction.

Normalize is ENTRY-ONLY: it runs once in ``compile_pattern`` (inside the
try/except so rejections return a rejected ``CompileResult`` instead of
propagating — see the batch regression test), before the caret_in_x /
trailing_alt_dollar hooks (which see normalized ERE text), and is NEVER
re-run in ``compile_bare``/``_compile_dialect`` — a re-normalize would
round-trip BRE ``\\+`` → ``+`` → ``\\+`` and cancel the fix.  Callers of
``_compile_dialect`` directly must pass already-normalized text.
"""

from __future__ import annotations

from regexproof.compiler.base import CompileResult, Unencodable

# Backslash-escapes whose meaning is IDENTICAL in GNU BRE/ERE and pcre —
# kept as-is in both syntaxes.
_KEEP_IDENTICAL = frozenset(r".*^$[]\-\\")
# GNU/busybox shorthand classes/boundaries (both BRE and ERE) — rejected:
# pcre's semantics differ.
_GNU_CLASSES = frozenset("wWsSbB")
_GNU_BOUNDARIES = frozenset("<>")
# BRE-only group/quantifier escapes — unescaped to bare syntax.
_BRE_UNESCAPE = frozenset("(){}|+?")
# ERE backslash-metas that are LITERALS on grep AND in pcre — backslash kept.
_ERE_KEEP_LITERAL = frozenset(r".*^$[]\-\\+?{}()|")


def _handle_escape(nxt: str, syntax: str, out: list[str]) -> None:
    if nxt in _GNU_CLASSES:
        raise Unencodable("gnu-extension")
    if nxt in _GNU_BOUNDARIES:
        raise Unencodable("gnu-word-boundary")
    if syntax == "bre":
        if nxt in _BRE_UNESCAPE:
            out.append(nxt)  # unescape BRE quantifier/group
            return
        if nxt in "123456789":
            raise Unencodable("backref")
    elif nxt in _ERE_KEEP_LITERAL:
        out.append("\\")  # ERE backslash-meta = literal in grep AND pcre
        out.append(nxt)
        return
    elif nxt in "123456789":
        out.append(nxt)  # ERE has no backrefs: \1 = literal 1
        return
    if nxt in _KEEP_IDENTICAL:
        out.append("\\")
        out.append(nxt)
    else:
        out.append(nxt)  # drop backslash — the literal char per grep


def normalize_shell(pattern: str, syntax: str) -> str:
    """Two-direction BRE→ERE transform (BRE) or literal-preserving
    pass-through (ERE).  Single pass; escape semantics per the module
    docstring (machine-verified).
    """
    if syntax in ("ere", "bash_ksh") and "(?" in pattern:
        raise Unencodable("inline-flag-like")
    out: list[str] = []
    i, n = 0, len(pattern)
    while i < n:
        c = pattern[i]
        if c == "\\":
            if i + 1 >= n:
                out.append("\\")
                break
            _handle_escape(pattern[i + 1], syntax, out)
            i += 2
            continue  # do NOT fall through to the bottom i += 1
        if syntax == "bre":
            if c in "+?{|(":
                out.append("\\")  # literal-escape: BRE bare = literal
                out.append(c)
                i += 1
                continue
            if c == ")":
                out.append("\\")  # bare ) is literal in BRE; pcre errors
                out.append(c)
                i += 1
                continue
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

"""YARA dialect compiler — ascii-domain regex via re2/py_re path; wide via NUL-interleave."""

from __future__ import annotations

from regexproof.compiler.base import CompileResult, Unencodable, add_compiler_meta, composite_meta


def compile_yara(
    pattern: str,
    *,
    flags: str = "",
    call_kind: str = "search",
    max_length: int = 256,
    domain: str = "ascii",
) -> CompileResult:
    """Compile a YARA regex pattern to a Z3 mirror expression.

    For ascii domain: delegates to the re2 compiler (YARA uses PCRE syntax
    subset similar to RE2 for most patterns).
    For wide domain: NUL-interleaves each literal byte in the pattern.
    Fullword flag ('W') is rejected as unsupported for now.
    """
    if "W" in flags:
        return CompileResult(
            mirror=None,
            unencodable_reason="fullword-boundary",
            dialect="yara",
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain=domain,
        )

    compile_flags = flags.replace("W", "")

    if domain == "wide":
        return _compile_wide(pattern, flags=compile_flags, call_kind=call_kind, max_length=max_length)

    return _compile_ascii(pattern, flags=compile_flags, call_kind=call_kind, max_length=max_length)


def _compile_ascii(
    pattern: str,
    *,
    flags: str,
    call_kind: str,
    max_length: int,
) -> CompileResult:
    """Delegate ascii-domain YARA patterns to the re2 compiler."""
    from regexproof.compiler.re2 import compile_re2

    try:
        result = compile_re2(pattern, flags=flags, call_kind=call_kind, max_length=max_length)
        return CompileResult(
            mirror=result.mirror,
            unencodable_reason=result.unencodable_reason,
            dialect="yara",
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain="ascii",
            meta=result.meta,
        )
    except Exception as exc:
        return CompileResult(
            mirror=None,
            unencodable_reason=f"compile-error:{type(exc).__name__}",
            dialect="yara",
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain="ascii",
        )


def _compile_wide(
    pattern: str,
    *,
    flags: str,
    call_kind: str,
    max_length: int,
) -> CompileResult:
    """Wide domain: NUL-interleave literal characters for UTF-16LE encoding.

    Only supports literal patterns (re.escape output) for now.
    Complex regex patterns in wide mode are rejected.
    """
    import re

    try:
        if _is_literal_pattern(pattern):
            unescaped = _unescape_literal(pattern)
            wide_pattern = "".join(c + "\x00" for c in unescaped)
            import z3

            literal = z3.Re(z3.StringVal(wide_pattern))
            if call_kind == "fullmatch":
                mirror = literal
                wrap_kind = "fullmatch"
                fullmatch_shaped = True
            elif call_kind == "match":
                # C1 fold (luna re-gate 5): a match call is PREFIX-anchored —
                # literal followed by anything — not the search shape.
                _seq = z3.StringSort()
                _rseq = z3.ReSort(_seq)
                star = z3.Star(z3.AllChar(_rseq))
                mirror = z3.Concat(literal, star)
                wrap_kind = "match"
                fullmatch_shaped = False
            else:
                # C1 fold (luna re-gate): extracted YARA records use
                # call_kind=search and wide matching is substring-based —
                # the mirror must be the search shape, not an exact string.
                _seq = z3.StringSort()
                _rseq = z3.ReSort(_seq)
                star = z3.Star(z3.AllChar(_rseq))
                mirror = z3.Concat(star, z3.Concat(literal, star))
                wrap_kind = "search"
                fullmatch_shaped = False
            # Wide nocase is not modeled — fail closed on the exactness flag.
            nocase = "i" in flags
            meta = composite_meta(
                leading_caret=False,
                # C1 fold (luna re-gate 3): source-derived — a wide literal has
                # no $ alternative, so trailing_dollar is False even under a
                # fullmatch wrap (the whole-string shape comes from the wrap).
                trailing_dollar=False,
                word_boundary_wrap=False,
                wrap_kind=wrap_kind,
                mirror_exact=not nocase,
            )
            # Wide literal mirror is an exact-string (whole-string) language —
            # override the composite default (Union mirrors are never bare).
            meta["fullmatch_shaped"] = fullmatch_shaped
            return CompileResult(
                mirror=mirror,
                unencodable_reason=None,
                dialect="yara",
                call_kind=call_kind,
                flags=flags,
                pattern=pattern,
                declared_domain="wide",
                meta=meta,
            )
        return CompileResult(
            mirror=None,
            unencodable_reason="wide-non-literal",
            dialect="yara",
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain="wide",
        )
    except Exception as exc:
        return CompileResult(
            mirror=None,
            unencodable_reason=f"wide-compile-error:{type(exc).__name__}",
            dialect="yara",
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain="wide",
        )


def _is_literal_pattern(pattern: str) -> bool:
    """Check if a pattern is a pure literal (only escaped metacharacters)."""
    import re as _re
    unescaped = _re.sub(r"\\(.)", r"\1", pattern)
    re_escaped = _re.escape(unescaped)
    return re_escaped == pattern or not any(
        c in pattern for c in r"[](){}*+?|^$."
        if f"\\{c}" not in pattern
    )


def _unescape_literal(pattern: str) -> str:
    """Unescape a literal regex pattern back to raw string."""
    import re as _re
    return _re.sub(r"\\(.)", r"\1", pattern)

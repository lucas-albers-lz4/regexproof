"""Pattern → Z3 compilers (per dialect)."""

from __future__ import annotations

from regexproof.compiler.base import CompileResult, Unencodable
from regexproof.compiler.py_re import compile_py_re
from regexproof.compiler.trailing_alt_dollar import try_compile_trailing_alt_dollar

__all__ = ["CompileResult", "Unencodable", "compile_py_re", "compile_pattern"]


def _compile_dialect(
    pattern: str,
    flags: str,
    dialect: str,
    call_kind: str,
    *,
    max_length: int,
    domain: str = "ascii",
) -> CompileResult:
    if dialect == "py_re":
        return compile_py_re(
            pattern, flags=flags, call_kind=call_kind, max_length=max_length
        )
    if dialect == "ecma":
        from regexproof.compiler.ecma import compile_ecma

        return compile_ecma(
            pattern, flags=flags, call_kind=call_kind, max_length=max_length
        )
    if dialect == "re2":
        from regexproof.compiler.re2 import compile_re2

        return compile_re2(
            pattern, flags=flags, call_kind=call_kind, max_length=max_length
        )
    if dialect == "pcre":
        from regexproof.compiler.pcre import compile_pcre

        return compile_pcre(
            pattern, flags=flags, call_kind=call_kind, max_length=max_length
        )
    if dialect == "yara":
        from regexproof.compiler.yara import compile_yara

        return compile_yara(
            pattern,
            flags=flags,
            call_kind=call_kind,
            max_length=max_length,
            domain=domain,
        )
    raise ValueError(f"unknown dialect {dialect!r}")


def compile_pattern(
    pattern: str,
    flags: str = "",
    dialect: str = "py_re",
    call_kind: str = "search",
    *,
    max_length: int = 256,
    domain: str = "ascii",
):
    """Dispatch to a dialect compiler. Never use z3.Re(pattern_string)."""
    import z3

    def compile_bare(pat: str, fl: str, dia: str, ck: str) -> CompileResult:
        return _compile_dialect(
            pat, fl, dia, ck, max_length=max_length, domain=domain
        )

    try:
        special = try_compile_trailing_alt_dollar(
            pattern,
            flags,
            dialect,
            call_kind,
            max_length=max_length,
            compile_bare=compile_bare,
        )
        if special is not None:
            return special
        return _compile_dialect(
            pattern,
            flags,
            dialect,
            call_kind,
            max_length=max_length,
            domain=domain,
        )
    except Unencodable as exc:
        return CompileResult(
            mirror=None,
            unencodable_reason=exc.reason,
            dialect=dialect,
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain=domain,
        )
    except z3.Z3Exception:
        # REJECT-never-crash: Z3 Loop/bounds bugs must triage, not abort batch.
        return CompileResult(
            mirror=None,
            unencodable_reason="z3-exception",
            dialect=dialect,
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain=domain,
        )

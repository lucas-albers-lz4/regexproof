"""Pattern → Z3 compilers (per dialect)."""

from __future__ import annotations

from regexproof.compiler.base import CompileResult, Unencodable
from regexproof.compiler.py_re import compile_py_re

__all__ = ["CompileResult", "Unencodable", "compile_py_re", "compile_pattern"]


def compile_pattern(
    pattern: str,
    flags: str = "",
    dialect: str = "py_re",
    call_kind: str = "search",
    *,
    max_length: int = 256,
):
    """Dispatch to a dialect compiler. Never use z3.Re(pattern_string)."""
    if dialect == "py_re":
        return compile_py_re(pattern, flags=flags, call_kind=call_kind, max_length=max_length)
    if dialect == "ecma":
        from regexproof.compiler.ecma import compile_ecma

        return compile_ecma(pattern, flags=flags, call_kind=call_kind, max_length=max_length)
    if dialect == "re2":
        from regexproof.compiler.re2 import compile_re2

        return compile_re2(pattern, flags=flags, call_kind=call_kind, max_length=max_length)
    if dialect == "pcre":
        from regexproof.compiler.pcre import compile_pcre

        return compile_pcre(pattern, flags=flags, call_kind=call_kind, max_length=max_length)
    raise ValueError(f"unknown dialect {dialect!r}")

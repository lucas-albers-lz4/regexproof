"""Shared compiler types and Z3 helpers."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import z3
from z3 import AllChar, Concat, Loop, Plus, Re, Star, Union


class Unencodable(Exception):
    """Pattern cannot be faithfully encoded; reason is the triage key."""

    def __init__(self, reason: str):
        super().__init__(reason)
        self.reason = reason


def helper_gate_missing(helper_name: str) -> dict:
    """Fail-closed gate when a dialect helper is unavailable (#172).

    Returns ``ok: False`` so existing ``if gate.get("ok") is False`` paths
    refuse to encode — never soft-open with ``ok: True``.
    """
    return {
        "ok": False,
        "helper": f"{helper_name}-missing",
        "error": f"{helper_name} helper unavailable",
    }


@dataclass
class CompileResult:
    mirror: Any | None
    unencodable_reason: str | None
    dialect: str
    call_kind: str
    flags: str
    pattern: str
    declared_domain: str  # "ascii" | "unicode"

    @property
    def encodable(self) -> bool:
        return self.mirror is not None and self.unencodable_reason is None


def any_char():
    return AllChar(Re("").sort())


def opt(r):
    """Regex optional — never z3.Opt (optimizer)."""
    return Union(r, Re(""))


def repeat_z3(body, lo: int, hi: int | None):
    """Shared ``{lo,hi}`` / ``*`` / ``+`` lowering for all dialects.

    Consolidation only (fix-wave #73) — preserves the ``lo == hi == 1``
    identity from Phase 1 / TRAPS #20 (do not re-derive that fix here).
    ``hi is None`` means unbounded.
    """
    if lo == 0 and hi == 1:
        return opt(body)
    if lo == 0 and hi is None:
        return Star(body)
    if lo == 1 and hi is None:
        return Plus(body)
    if hi is None:
        return Concat(*([body] * lo), Star(body)) if lo else Star(body)
    if lo == hi:
        if lo <= 0:
            return Re("")
        if lo == 1:
            # Z3 Concat requires ≥2 args; `{1}` / `{1,1}` is identity (TRAPS #20).
            return body
        return Concat(*([body] * lo))
    return Loop(body, lo, hi)


def wrap_call_kind(body, call_kind: str, *, trailing_dollar_nl: bool = False):
    """Apply call_kind wrapper after anchors have been translated into `body`.

    Anchors themselves are handled in the dialect translators. This only adds
    the search/match prefix/suffix Star(any) wrappers when needed.
    """
    any_c = any_char()
    if call_kind == "fullmatch":
        return body
    if call_kind == "match":
        # Prefix match: pattern || .*
        return Concat(body, Star(any_c))
    if call_kind in ("search", "exec"):
        return Concat(Star(any_c), body, Star(any_c))
    if call_kind == "substitution":
        # Bounded substitution mirrors use search-shaped membership for v1.
        return Concat(Star(any_c), body, Star(any_c))
    raise Unencodable(f"unsupported-call_kind:{call_kind}")


def python_trailing_dollar(body):
    """Python/PCRE `$` matches before a trailing newline."""
    return Concat(body, Union(Re(""), Re("\n")))


@dataclass
class DialectSpec:
    """Hooks for ``compile_dialect_template`` (#198)."""

    dialect: str
    declared_domain: str = "ascii"
    default_max_length: int = 256
    terminators: frozenset | None = None
    space_chars: str = " \t\n\r\f\v"
    trailing_dollar_nl: bool = False
    allow_ascii_word_boundary: bool = True
    # Optional callables — set by dialect modules
    strip_fn: Any = None  # (pattern) -> str
    local_reject_fn: Any = None  # (pattern) -> str|None reason
    flag_reject_fn: Any = None  # (flags: str) -> None raises Unencodable
    helper_gate_fn: Any = None  # (stripped, flags) -> dict|None
    raise_from_gate_fn: Any = None  # (gate) -> None
    fold_fn: Any = None  # case-fold closure when "i" in flags
    case_fold_fn: Any = None  # always-available fold for scoped (?i:)
    digit_fn: Any = None
    space_fn: Any = None
    word_fn: Any = None
    parse_kwargs: dict | None = None  # extra parse_pattern kwargs
    preprocess_fn: Any = None  # (pattern, flags) -> (pattern, flags) before strip


def compile_dialect_template(
    pattern: str,
    flags: str,
    call_kind: str,
    *,
    spec: DialectSpec,
    max_length: int | None = None,
) -> CompileResult:
    """Shared dialect compile pipeline: reject → strip → helper → parse → lower.

    Dialect modules supply a ``DialectSpec``; semantics stay in those hooks.
    Absorbs the helper_gate fail-closed pattern (#172 / #198).
    """
    from z3 import Range, Re, Union

    from regexproof.compiler.lower import lower, space_codes_from_chars
    from regexproof.compiler.simple_parse import parse_pattern

    flags = "".join(sorted(set(flags)))
    max_len = spec.default_max_length if max_length is None else max_length
    try:
        if len(pattern) > max_len:
            raise Unencodable("pattern-too-long")
        if spec.preprocess_fn is not None:
            pattern, flags = spec.preprocess_fn(pattern, flags)
        if spec.flag_reject_fn is not None:
            spec.flag_reject_fn(flags)
        if spec.local_reject_fn is not None:
            reason = spec.local_reject_fn(pattern)
            if reason:
                raise Unencodable(reason)
        stripped = spec.strip_fn(pattern) if spec.strip_fn else pattern
        if spec.helper_gate_fn is not None:
            gate = spec.helper_gate_fn(stripped, flags)
            if gate is not None and spec.raise_from_gate_fn is not None:
                spec.raise_from_gate_fn(gate)
            elif gate is not None and gate.get("ok") is False:
                # Default fail-closed mapping when no custom raiser.
                ureason = gate.get("unencodable_reason")
                helper = str(gate.get("helper") or "")
                if ureason == "timeout":
                    raise Unencodable("timeout")
                if helper.endswith("-missing") or "helper unavailable" in str(
                    gate.get("error") or ""
                ):
                    raise Unencodable("helper-unavailable")
                if ureason:
                    raise Unencodable(ureason)
                raise Unencodable("parse-error")
        parse_kwargs = dict(spec.parse_kwargs or {})
        ast = parse_pattern(stripped, **parse_kwargs)
        fold = spec.fold_fn if ("i" in flags and spec.fold_fn is not None) else None
        case_fold = spec.case_fold_fn or spec.fold_fn
        digit = spec.digit_fn or (lambda: Range("0", "9"))
        space = spec.space_fn or (
            lambda: Union(*[Re(c) for c in spec.space_chars])
        )
        word = spec.word_fn or (
            lambda: Union(
                Range("a", "z"), Range("A", "Z"), Range("0", "9"), Re("_")
            )
        )
        terminators = spec.terminators or frozenset(["\n"])
        mirror, _meta = lower(
            ast,
            fold=fold,
            case_fold=case_fold,
            dot_terminators=terminators,
            digit=digit,
            space=space,
            word=word,
            trailing_dollar_nl=spec.trailing_dollar_nl,
            call_kind=call_kind,
            allow_ascii_word_boundary=spec.allow_ascii_word_boundary,
            space_codes=space_codes_from_chars(spec.space_chars),
        )
        return CompileResult(
            mirror=mirror,
            unencodable_reason=None,
            dialect=spec.dialect,
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain=spec.declared_domain,
        )
    except Unencodable as exc:
        return CompileResult(
            mirror=None,
            unencodable_reason=exc.reason,
            dialect=spec.dialect,
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain=spec.declared_domain,
        )

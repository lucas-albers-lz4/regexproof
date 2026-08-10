"""ECMAScript dialect compiler — regexpp parse gate + simple AST → Z3."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

from z3 import Range, Re, Union

from regexproof.compiler.base import CompileResult, Unencodable, helper_gate_missing
from regexproof.compiler.fold import js_nonsu_fold_closure
from regexproof.compiler.lower import lower, space_codes_from_chars
from regexproof.compiler.pcre_strip import strip_language_transparent
from regexproof.compiler.simple_parse import parse_pattern

HELPER = Path(__file__).resolve().parents[2] / "helpers" / "ecma"
JS_TERMINATORS = frozenset(["\n", "\r", "\u2028", "\u2029"])
_ECMA_SPACE_CHARS = " \t\n\r\f\v\u00a0\u2028\u2029"
DEFAULT_MAX_LENGTH = 256
HELPER_TIMEOUT_S = 30


def _run_regexpp(pattern: str, flags: str) -> dict:
    parse_js = HELPER / "parse.mjs"
    if not parse_js.is_file():
        return helper_gate_missing("node")
    try:
        proc = subprocess.run(
            ["node", str(parse_js), pattern, flags],
            capture_output=True,
            text=True,
            shell=False,
            timeout=HELPER_TIMEOUT_S,
            check=False,
        )
    except FileNotFoundError:
        return helper_gate_missing("node")
    except subprocess.TimeoutExpired:
        return {"ok": False, "unencodable_reason": "timeout", "error": "timeout"}
    try:
        return json.loads(proc.stdout.strip() or "{}")
    except json.JSONDecodeError:
        return {"ok": False, "unencodable_reason": "parse-error"}


def _raise_from_gate(gate: dict) -> None:
    """Fail-closed: missing helper / timeout / reject reasons all Unencodable."""
    if gate.get("ok") is not False:
        return
    err = str(gate.get("error") or "")
    helper = str(gate.get("helper") or "")
    reason = gate.get("unencodable_reason")
    if reason == "timeout" or err == "timeout":
        raise Unencodable("timeout")
    if helper.endswith("-missing") or "helper unavailable" in err:
        raise Unencodable("helper-unavailable")
    if reason:
        raise Unencodable(reason)
    raise Unencodable("parse-error")


def compile_ecma(
    pattern: str,
    flags: str = "",
    call_kind: str = "search",
    *,
    max_length: int = DEFAULT_MAX_LENGTH,
) -> CompileResult:
    flags = "".join(sorted(set(flags)))
    try:
        if len(pattern) > max_length:
            raise Unencodable("pattern-too-long")
        for f in flags:
            # Explicit reject-list — never silently ASCII-approximate these.
            # Triage: m → rewrite/IndexOf (LOOKBEHIND_REWRITE); u/v → Unicode
            # stock-Z3 limit; g/y → stateful (lastIndex) — not language membership.
            if f in "uv":
                raise Unencodable(f"{f}-flag")
            if f == "m":
                raise Unencodable("m-flag")
            if f in "gy":
                raise Unencodable("stateful")
            if f == "d":
                raise Unencodable("stateful")  # hasIndices — match metadata, not language
            if f not in "is":
                raise Unencodable(f"unknown-flag:{f}")
        # Local AST reject first so scoped `(?i:…)` stays `inline-flag`
        # (regexpp alone reports a generic parse-error).
        stripped = strip_language_transparent(pattern)
        ast = parse_pattern(stripped, allow_scoped_i=False)
        gate = _run_regexpp(pattern, flags)
        # regexpp is a required capability gate (#172 fail-closed) — never
        # soft-open on missing node / timeout.
        _raise_from_gate(gate)
        ignorecase = "i" in flags
        fold = js_nonsu_fold_closure if ignorecase else None
        mirror, _meta = lower(
            ast,
            fold=fold,
            case_fold=js_nonsu_fold_closure,
            dot_terminators=JS_TERMINATORS,
            digit=lambda: Range("0", "9"),
            space=lambda: Union(*[Re(c) for c in _ECMA_SPACE_CHARS]),
            word=lambda: Union(Range("a", "z"), Range("A", "Z"), Range("0", "9"), Re("_")),
            trailing_dollar_nl=False,
            call_kind=call_kind,
            allow_ascii_word_boundary=True,
            space_codes=space_codes_from_chars(_ECMA_SPACE_CHARS),
        )
        return CompileResult(
            mirror=mirror,
            unencodable_reason=None,
            dialect="ecma",
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain="ascii",
        )
    except Unencodable as exc:
        return CompileResult(
            mirror=None,
            unencodable_reason=exc.reason,
            dialect="ecma",
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain="ascii",
        )


def replay_argv(pattern: str, flags: str) -> list[str]:
    return ["node", str(HELPER / "match.mjs"), pattern, flags]


def helper_used_for_parse(pattern: str = "a+", flags: str = "") -> bool:
    """Acceptance: regexpp helper participates in parse (when node+deps present)."""
    gate = _run_regexpp(pattern, flags)
    return gate.get("helper") == "ecma-regexpp" and gate.get("ok") is True

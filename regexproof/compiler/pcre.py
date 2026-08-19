"""PCRE encodable-subset compiler + PCRE2 CLI helper gate."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


from regexproof.compiler.base import (
    CompileResult,
    DialectSpec,
    Unencodable,
    compile_dialect_template,
)
from regexproof.compiler.fold import python_fold_closure
from regexproof.compiler.pcre_strip import strip_language_transparent
from regexproof.compiler.reject_markers import PCRE_REJECT_MARKERS, unicode_prop_unencodable

HELPER = Path(__file__).resolve().parents[2] / "helpers" / "pcre2" / "match.py"
DEFAULT_MAX_LENGTH = 256
HELPER_TIMEOUT_S = 30
PCRE_TERMINATORS = frozenset(["\n"])
_PCRE_SPACE_CHARS = " \t\n\r\f\v"


def _local_reject(pattern: str) -> str | None:
    prop = unicode_prop_unencodable(pattern)
    if prop:
        return prop
    for marker, reason in PCRE_REJECT_MARKERS:
        if marker in pattern:
            return reason
    if re.search(r"(?<!\\)\\[1-9]", pattern):
        return "backref"
    return None


def _helper_parse(pattern: str) -> dict:
    try:
        proc = subprocess.run(
            [sys.executable, str(HELPER), "parse", pattern],
            capture_output=True,
            text=True,
            shell=False,
            check=False,
            timeout=HELPER_TIMEOUT_S,
        )
    except subprocess.TimeoutExpired:
        return {"ok": False, "unencodable_reason": "timeout"}
    try:
        return json.loads(proc.stdout.strip() or "{}")
    except json.JSONDecodeError:
        return {"ok": False, "unencodable_reason": "parse-error"}


def compile_pcre(
    pattern: str,
    flags: str = "",
    call_kind: str = "search",
    *,
    max_length: int = DEFAULT_MAX_LENGTH,
) -> CompileResult:
    def flag_reject(fl: str) -> None:
        if "m" in fl:
            raise Unencodable("m-flag")

    def helper_gate(stripped: str, _flags: str) -> dict:
        return _helper_parse(stripped)

    def raise_gate(gate: dict) -> None:
        if gate.get("ok") is not False:
            return
        ureason = gate.get("unencodable_reason")
        if ureason == "timeout":
            raise Unencodable("timeout")
        if ureason == "pcre2-helper-unavailable" or gate.get("helper") in (
            "none",
        ):
            raise Unencodable("helper-unavailable")
        raise Unencodable(ureason or "parse-error")

    def fold_fn(ch):
        return python_fold_closure(ch, ascii_only=True)

    spec = DialectSpec(
        dialect="pcre",
        declared_domain="ascii",
        default_max_length=DEFAULT_MAX_LENGTH,
        terminators=PCRE_TERMINATORS,
        space_chars=_PCRE_SPACE_CHARS,
        trailing_dollar_nl=True,
        allow_ascii_word_boundary=True,
        strip_fn=strip_language_transparent,
        local_reject_fn=_local_reject,
        flag_reject_fn=flag_reject,
        helper_gate_fn=helper_gate,
        raise_from_gate_fn=raise_gate,
        fold_fn=fold_fn,
        case_fold_fn=fold_fn,
    )
    return compile_dialect_template(
        pattern, flags, call_kind, spec=spec, max_length=max_length
    )



def replay_argv(pattern: str, flags: str) -> list[str]:
    return [sys.executable, str(HELPER), "match", pattern, flags]


def helper_used_for_parse_and_replay() -> bool:
    """True only when a real PCRE2 engine (bindings or pcre2grep) is used."""
    gate = _helper_parse("a+")
    if not gate.get("ok"):
        return False
    if gate.get("helper") not in ("pcre2-bindings", "pcre2grep"):
        return False
    try:
        proc = subprocess.run(
            [sys.executable, str(HELPER), "match", "a+", ""],
            input="aaa",
            capture_output=True,
            text=True,
            shell=False,
            check=False,
            timeout=HELPER_TIMEOUT_S,
        )
    except subprocess.TimeoutExpired:
        return False
    return proc.returncode == 0

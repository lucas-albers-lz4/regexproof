"""Fail-closed compiler for the ASCII Java Pattern subset."""

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
    helper_gate_missing,
)
from regexproof.compiler.fold import python_fold_closure

HELPER = Path(__file__).resolve().parents[2] / "helpers" / "java" / "match.py"
HELPER_TIMEOUT_S = 30
JAVA_TERMINATORS = frozenset(["\n", "\r"])
JAVA_SPACE_CHARS = " \t\n\r\f\v"


def _java_reject(pattern: str) -> str | None:
    """Reject Java constructs not represented faithfully by the shared AST."""
    if "&&" in pattern:
        return "class-intersection"
    if re.search(r"(?<!\\)(?:\\\\)*\\(?:p|P|Q|E|A|z|Z|G|R|h|H|v|V|B|C|N)", pattern):
        return "java-escape"

    in_class = False
    i = 0
    while i < len(pattern):
        ch = pattern[i]
        if ch == "\\":
            if i + 1 >= len(pattern):
                return "parse-error"
            escape = pattern[i + 1]
            if in_class and escape == "b":
                # Java uses ``\b`` as backspace inside a class; the shared
                # parser represents it as a zero-width boundary.
                return "java-escape"
            if escape not in "dDsSwWbntrx" and escape not in r"\.^$*+?()[]{}|-":
                return "java-escape"
            i += 2
            continue
        if ch == "[":
            in_class = True
        elif ch == "]":
            in_class = False
        elif ch == "$" and not in_class:
            # Java '$' accepts input before a final CR/LF; the shared lowerer
            # currently models only LF. Reject until multi-terminator support lands.
            return "java-dollar-anchor"
        i += 1
    return None


def _parse_with_helper(pattern: str, flags: str) -> dict:
    try:
        proc = subprocess.run(
            [sys.executable, str(HELPER), "parse", pattern, flags],
            capture_output=True,
            text=True,
            shell=False,
            check=False,
            timeout=HELPER_TIMEOUT_S,
        )
    except FileNotFoundError:
        return helper_gate_missing("java-pattern")
    except subprocess.TimeoutExpired:
        return {"ok": False, "unencodable_reason": "timeout", "helper": "java-pattern"}
    try:
        return json.loads(proc.stdout.strip() or "{}")
    except ValueError:
        return {"ok": False, "unencodable_reason": "parse-error", "helper": "java-pattern"}


def _raise_from_gate(gate: dict) -> None:
    if gate.get("ok") is not False:
        return
    reason = gate.get("unencodable_reason")
    if reason == "timeout":
        raise Unencodable("timeout")
    if str(gate.get("helper", "")).endswith("-missing"):
        raise Unencodable("helper-unavailable")
    raise Unencodable(reason or "parse-error")


def compile_java(
    pattern: str,
    flags: str = "",
    call_kind: str = "search",
    *,
    max_length: int = 256,
) -> CompileResult:
    def flag_reject(value: str) -> None:
        if set(value) - {"i"}:
            raise Unencodable("java-flag")

    def fold(ch: str):
        return python_fold_closure(ch, ascii_only=True)

    spec = DialectSpec(
        dialect="java",
        declared_domain="ascii",
        default_max_length=256,
        terminators=JAVA_TERMINATORS,
        space_chars=JAVA_SPACE_CHARS,
        trailing_dollar_nl=False,
        allow_ascii_word_boundary=True,
        local_reject_fn=_java_reject,
        flag_reject_fn=flag_reject,
        helper_gate_fn=_parse_with_helper,
        raise_from_gate_fn=_raise_from_gate,
        fold_fn=fold,
        case_fold_fn=fold,
    )
    return compile_dialect_template(pattern, flags, call_kind, spec=spec, max_length=max_length)


def replay_argv(pattern: str, flags: str, call_kind: str = "search") -> list[str]:
    return [sys.executable, str(HELPER), "match", pattern, flags, call_kind]

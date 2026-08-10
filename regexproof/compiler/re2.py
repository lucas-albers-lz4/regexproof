"""Go RE2 dialect compiler — go-re2 helper for parse+replay + Z3 lower."""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

from z3 import Range, Re, Union

from regexproof.compiler.base import CompileResult, Unencodable, helper_gate_missing
from regexproof.compiler.fold import re2_fold_closure
from regexproof.compiler.lower import lower, space_codes_from_chars
from regexproof.compiler.pcre_strip import strip_language_transparent
from regexproof.compiler.simple_parse import parse_pattern

HELPER_DIR = Path(__file__).resolve().parents[2] / "helpers" / "go-re2"
DEFAULT_MAX_LENGTH = 256
HELPER_TIMEOUT_S = 30
RE2_TERMINATORS = frozenset(["\n"])
_RE2_SPACE_CHARS = " \t\n\f\r"


def _helper_bin() -> Path:
    env = os.environ.get("REGEXPROOF_GO_RE2")
    if env:
        candidate = Path(env).expanduser().resolve()
        allowed = HELPER_DIR.resolve()
        if not candidate.is_relative_to(allowed):
            raise ValueError(
                f"REGEXPROOF_GO_RE2 must resolve under {allowed}, got {candidate}"
            )
        return candidate
    local = HELPER_DIR / "go-re2"
    if local.is_file():
        return local
    return HELPER_DIR / "go-re2"


def ensure_built() -> Path:
    binary = _helper_bin()
    if binary.is_file():
        return binary
    subprocess.run(
        ["go", "build", "-o", str(binary), "."],
        cwd=str(HELPER_DIR),
        check=True,
        shell=False,
        timeout=HELPER_TIMEOUT_S,
    )
    return binary


def parse_with_helper(pattern: str) -> dict:
    try:
        binary = ensure_built()
    except (FileNotFoundError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return helper_gate_missing("go-re2")
    except ValueError:
        # REGEXPROOF_GO_RE2 outside helpers/go-re2/ — treat as unavailable.
        return helper_gate_missing("go-re2")
    try:
        proc = subprocess.run(
            [str(binary), "parse", pattern],
            capture_output=True,
            text=True,
            shell=False,
            check=False,
            timeout=HELPER_TIMEOUT_S,
        )
    except subprocess.TimeoutExpired:
        return {"ok": False, "unencodable_reason": "timeout", "error": "timeout"}
    try:
        return json.loads(proc.stdout.strip() or "{}")
    except json.JSONDecodeError:
        return {"ok": False, "error": proc.stderr}


def _raise_from_gate(gate: dict) -> None:
    """Map a fail-closed helper gate to Unencodable (including timeout)."""
    if gate.get("ok") is not False:
        return
    err = str(gate.get("error") or "")
    helper = str(gate.get("helper") or "")
    ureason = gate.get("unencodable_reason")
    if ureason == "timeout" or err == "timeout":
        raise Unencodable("timeout")
    if helper.endswith("-missing") or "helper unavailable" in err:
        raise Unencodable("helper-unavailable")
    # Go RE2 caps repeats at 1000 — classify so wave gates don't treat
    # this as an unclassified parse-error (e.g. Nosey Parker `{20,1024}`).
    if "invalid repeat count" in err:
        raise Unencodable("repeat-count")
    raise Unencodable("parse-error")


def compile_re2(
    pattern: str,
    flags: str = "",
    call_kind: str = "search",
    *,
    max_length: int = DEFAULT_MAX_LENGTH,
) -> CompileResult:
    """Compile a Go-RE2 pattern to a Z3 mirror.

    Fail-closed on residual ``x`` (``x-flag-unstripped``) and ``s``
    (``s-flag``). Verbose ``(?x)`` must be stripped at extraction via
    ``strip_verbose_x``; Nosey Parker ``(?s)`` / lifted ``s`` records are
    unencodable until a rust_regex or helper-``s`` path lands — never silent.
    """
    flags = "".join(sorted(set(flags)))
    try:
        if len(pattern) > max_length:
            raise Unencodable("pattern-too-long")
        if "x" in flags:
            raise Unencodable("x-flag-unstripped")
        if "s" in flags:
            raise Unencodable("s-flag")
        if "m" in flags:
            raise Unencodable("m-flag")
        stripped = strip_language_transparent(pattern)
        gate = parse_with_helper(stripped)
        _raise_from_gate(gate)
        ast = parse_pattern(stripped)
        fold = re2_fold_closure if "i" in flags else None
        mirror, _meta = lower(
            ast,
            fold=fold,
            case_fold=re2_fold_closure,
            dot_terminators=RE2_TERMINATORS,
            digit=lambda: Range("0", "9"),
            space=lambda: Union(*[Re(c) for c in _RE2_SPACE_CHARS]),
            word=lambda: Union(Range("a", "z"), Range("A", "Z"), Range("0", "9"), Re("_")),
            trailing_dollar_nl=False,
            call_kind=call_kind,
            allow_ascii_word_boundary=True,
            space_codes=space_codes_from_chars(_RE2_SPACE_CHARS),
        )
        return CompileResult(
            mirror=mirror,
            unencodable_reason=None,
            dialect="re2",
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain="ascii",
        )
    except Unencodable as exc:
        return CompileResult(
            mirror=None,
            unencodable_reason=exc.reason,
            dialect="re2",
            call_kind=call_kind,
            flags=flags,
            pattern=pattern,
            declared_domain="ascii",
        )


def replay_argv(pattern: str, flags: str) -> list[str]:
    binary = ensure_built()
    return [str(binary), "match", pattern, flags]


def helper_used_for_parse_and_replay() -> bool:
    gate = parse_with_helper("a+")
    if gate.get("helper") != "go-re2" or gate.get("ok") is not True:
        return False
    try:
        binary = ensure_built()
    except Exception:  # noqa: BLE001
        return False
    try:
        proc = subprocess.run(
            [str(binary), "match", "a+", ""],
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

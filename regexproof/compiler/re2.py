"""Go RE2 dialect compiler — go-re2 helper for parse+replay + Z3 lower."""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path


from regexproof.compiler.base import (
    CompileResult,
    DialectSpec,
    Unencodable,
    compile_dialect_template,
    helper_gate_missing,
)
from regexproof.compiler.fold import re2_fold_closure
from regexproof.compiler.pcre_strip import strip_language_transparent
from regexproof.compiler.reject_markers import unicode_prop_unencodable

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
    except FileNotFoundError:
        return helper_gate_missing("go-re2")
    except subprocess.CalledProcessError:
        return helper_gate_missing("go-re2")
    except subprocess.TimeoutExpired:
        return {"ok": False, "unencodable_reason": "timeout", "error": "timeout"}
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

    def flag_reject(fl: str) -> None:
        if "x" in fl:
            raise Unencodable("x-flag-unstripped")
        if "s" in fl:
            raise Unencodable("s-flag")
        if "m" in fl:
            raise Unencodable("m-flag")

    def helper_gate(stripped: str, _flags: str) -> dict:
        return parse_with_helper(stripped)

    spec = DialectSpec(
        dialect="re2",
        declared_domain="ascii",
        default_max_length=DEFAULT_MAX_LENGTH,
        terminators=RE2_TERMINATORS,
        space_chars=_RE2_SPACE_CHARS,
        trailing_dollar_nl=False,
        allow_ascii_word_boundary=True,
        strip_fn=strip_language_transparent,
        local_reject_fn=unicode_prop_unencodable,
        flag_reject_fn=flag_reject,
        helper_gate_fn=helper_gate,
        raise_from_gate_fn=_raise_from_gate,
        fold_fn=re2_fold_closure,
        case_fold_fn=re2_fold_closure,
    )
    return compile_dialect_template(
        pattern, flags, call_kind, spec=spec, max_length=max_length
    )



def replay_argv(pattern: str, flags: str) -> list[str]:
    try:
        binary = ensure_built()
    except FileNotFoundError as exc:
        raise RuntimeError("go-re2 helper unavailable") from exc
    except subprocess.CalledProcessError as exc:
        raise RuntimeError("go-re2 helper build failed") from exc
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError("go-re2 helper build timed out") from exc
    except ValueError as exc:
        raise RuntimeError(str(exc)) from exc
    return [str(binary), "match", pattern, flags]


def helper_used_for_parse_and_replay() -> bool:
    gate = parse_with_helper("a+")
    if gate.get("helper") != "go-re2" or gate.get("ok") is not True:
        return False
    try:
        binary = ensure_built()
    except Exception:
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

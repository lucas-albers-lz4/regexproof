"""Counterexample and mutation guard for Mycelium's systemd argv capture."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import (
    And,
    Contains,
    IndexOf,
    InRe,
    Length,
    Not,
    Range,
    Re,
    Star,
    String,
    StringVal,
    SubString,
    Union,
)

from regexproof.groundtruth.mycelium_execstart_replay import (
    PIN,
    PATTERN,
    semicolon_drops_late_bypass,
    weakened_space_capture_drops_bypass,
)
from regexproof.harness.core import prop

FAMILY = "MY-mycelium-systemd-execstart-diagnostic"
SITE = f"mycelium0/mycelium@{PIN}:scripts/update_unit_drift_drill.sh:184:3"
_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-15-autonomous-mycelium-script-slice"
    / "contract-execstart-diagnostic.json"
)
CONTRACT = json.loads(_CONTRACT_PATH.read_text(encoding="utf-8"))

_ASCII_ARG = Union(Range(" ", "~"), Re("\t"))
_TAIL_RE = Star(_ASCII_ARG)
_SEMICOLON_PREFIX = (
    "{ path=/usr/bin/printf ; argv[]=/usr/bin/printf %s\\n --update "
    "--allowed-signers /etc/my;"
)
_PLAIN_PREFIX = (
    "{ path=/usr/bin/printf ; argv[]=/usr/bin/printf %s\\n --update "
    "--allowed-signers /etc/mycelium/allowed_signers "
)
_TRAILER = (
    " ; ignore_errors=no ; start_time=[fixture] ; "
    "stop_time=[fixture] ; pid=1 ; code=exited ; status=0 }"
)
_BYPASS = StringVal("--insecure-no-verify")


def _false_negative_formula(tail, prefix: str, separator: str):
    raw = StringVal(prefix) + tail + StringVal(_TRAILER)
    argv_marker = IndexOf(raw, StringVal("argv[]="), 0)
    argv_start = argv_marker + len("argv[]=")
    capture_end = IndexOf(raw, StringVal(separator), argv_start)
    captured = SubString(raw, argv_start, capture_end - argv_start)
    return raw, And(
        argv_marker >= 0,
        capture_end > argv_start,
        Contains(raw, _BYPASS),
        Not(Contains(captured, _BYPASS)),
    )


@prop(
    "MY-mycelium-drift-systemd-semicolon-drops-bypass",
    "Counterexample: systemd 255.4 serializes a literal argv semicolon before "
    "--insecure-no-verify, so the pinned [^;]* capture drops the flag",
    expect_unsat=False,
    kind="counterexample_finder",
    family=FAMILY,
    input_domain="ascii",
    call_kind="substitution",
    pattern=PATTERN,
    pattern_flags="",
    contract=CONTRACT,
    ground_truth=semicolon_drops_late_bypass,
)
def systemd_semicolon_drops_late_bypass():
    tail = String("execstart_tail")
    _, false_negative = _false_negative_formula(tail, _SEMICOLON_PREFIX, ";")
    return [
        tail == StringVal(
            "celium/allowed_signers --insecure-no-verify --repo-ref v1"
        ),
        InRe(tail, _TAIL_RE),
        Length(tail) <= 128,
        Not(Contains(tail, StringVal(";"))),
        Contains(tail, StringVal("--insecure-no-verify")),
        Contains(tail, StringVal("--repo-ref v1")),
    ], false_negative


@prop(
    "MY-mycelium-drift-mutated-space-capture-drops-bypass",
    "MUTATION GUARD: weakening the capture from [^;]* to [^ ]* must admit "
    "a semicolon-free argv where the real parser sees the bypass and the "
    "mutated parser loses it",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
    call_kind="substitution",
    pattern=PATTERN,
    pattern_flags="",
    ground_truth=weakened_space_capture_drops_bypass,
)
def mutated_space_capture_drops_bypass():
    tail = String("execstart_tail")
    raw, mutated_false_negative = _false_negative_formula(tail, _PLAIN_PREFIX, " ")
    original_marker = IndexOf(raw, StringVal("argv[]="), 0)
    original_start = original_marker + len("argv[]=")
    original_capture_end = IndexOf(raw, StringVal(";"), original_start)
    original_capture = SubString(
        raw, original_start, original_capture_end - original_start
    )
    return [
        tail == StringVal("--insecure-no-verify --repo-ref v1"),
        InRe(tail, _TAIL_RE),
        Length(tail) <= 128,
        Not(Contains(tail, StringVal(";"))),
        Contains(tail, StringVal("--insecure-no-verify")),
        Contains(original_capture, _BYPASS),
    ], mutated_false_negative

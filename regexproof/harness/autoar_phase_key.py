"""Path-component contract for AutoAR's pinned phase-log key sanitizer."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import And, InRe, Length, Not, Or, String, StringVal

from regexproof.compiler import compile_pattern
from regexproof.groundtruth.autoar_phase_key_replay import (
    mutation_reproduces_path_escape,
)
from regexproof.harness.core import prop

PIN = "01cd447ad3b1acfed7e0680596c2c74458a4cf06"
FAMILY = "AA-autoar-phase-log-key"
SITE = (
    f"h0tak88r/AutoAR@{PIN}:"
    "internal/utils/phase_logs.go:206:MustCompile"
)
QUESTION_ID = "AA-autoar-phase-log-module-component-safe"
PATTERN = r"[^a-zA-Z0-9_-]+"
WEAK_PATTERN = r"[^a-zA-Z0-9_./-]+"
FORBIDDEN_PATH_CHARS = (".", "/", "\\")
_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-15-autonomous-autoar-phasekey-20r2"
    / "contract.json"
)
CONTRACT = json.loads(_CONTRACT_PATH.read_text(encoding="utf-8"))


def _mirror(pattern: str):
    compiled = compile_pattern(
        pattern,
        dialect="re2",
        call_kind="substitution",
        max_length=128,
        domain="ascii",
    )
    if compiled.mirror is None:
        raise RuntimeError(
            "AutoAR Go RE2 phase-key character class is not encodable: "
            f"{compiled.unencodable_reason}"
        )
    return compiled.mirror


SOURCE_PATTERN = _mirror(PATTERN)
WEAK_SOURCE_PATTERN = _mirror(WEAK_PATTERN)


@prop(
    QUESTION_ID,
    "Every one-character ASCII path punctuation token '.', '/', and '\\\\' "
    "is matched by the pinned RE2 replacement class before filename joining",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="ascii",
    call_kind="substitution",
    pattern=PATTERN,
    pattern_flags="",
    contract=CONTRACT,
)
def autoar_phase_log_filename_replaces_path_punctuation():
    character = String("path_character")
    return [
        And(
            Length(character) == 1,
            Or(*[character == StringVal(value) for value in FORBIDDEN_PATH_CHARS]),
        )
    ], Not(InRe(character, SOURCE_PATTERN))


def _weakened_path_replays(witness: dict) -> bool:
    return (
        witness.get("path_character") == "."
        and mutation_reproduces_path_escape(witness)
    )


@prop(
    "AA-autoar-phase-log-module-component-mutated-path-escape",
    "MUTATION GUARD: allowing '.' and '/' through the pinned sanitizer class "
    "admits a dot witness and the weakened exact helper escapes phase-logs",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
    ground_truth=_weakened_path_replays,
)
def autoar_phase_log_mutated_sanitizer_allows_path_syntax():
    character = String("path_character")
    return [
        And(Length(character) == 1, character == StringVal(".")),
    ], Not(InRe(character, WEAK_SOURCE_PATTERN))


__all__ = [
    "CONTRACT",
    "FAMILY",
    "PIN",
    "QUESTION_ID",
    "SITE",
]

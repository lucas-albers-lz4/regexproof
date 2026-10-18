"""Capture-class image property for AutoAR's pinned Go RE2 extractor."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import And, InRe, Length, Or, String, StringVal

from regexproof.compiler import compile_pattern
from regexproof.groundtruth.autoar_jsendpoints_replay import mutation_reproduces_quote
from regexproof.harness.core import prop

PIN = "01cd447ad3b1acfed7e0680596c2c74458a4cf06"
FAMILY = "AA-autoar-jsendpoints"
SITE = (
    f"h0tak88r/AutoAR@{PIN}:"
    "internal/scanner/jsendpoints/jsendpoints.go:181:BASE_URL"
)
# The anchors describe the one-character projection used by this Shape-1
# query; the inner bracket expression is copied from the Go capture group.
CAPTURE_CLASS = r'''^[^"'\x60\s]$'''
MUTATED_CAPTURE_CLASS = r'''^[^'\x60\s]$'''
FORBIDDEN_ASCII = ('"', "'", "`", " ", "\t", "\n", "\f", "\r")
_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-15-autonomous-autoar-jsendpoint-20r2"
    / "contract.json"
)
CONTRACT = json.loads(_CONTRACT_PATH.read_text(encoding="utf-8"))


def _mirror(pattern: str):
    compiled = compile_pattern(
        pattern,
        dialect="re2",
        call_kind="fullmatch",
        max_length=16,
        domain="ascii",
    )
    if compiled.mirror is None:
        raise RuntimeError(
            f"AutoAR Go RE2 capture class is not encodable: {compiled.unencodable_reason}"
        )
    return compiled.mirror


SOURCE_CLASS = _mirror(CAPTURE_CLASS)
WEAK_CLASS = _mirror(MUTATED_CAPTURE_CLASS)


@prop(
    "AA-autoar-jsendpoint-assignment-capture-delimiter",
    "Every one-character ASCII member of the pinned URL-assignment capture "
    "class excludes quote, backtick, and Go RE2 whitespace delimiters",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="ascii",
    call_kind="fullmatch",
    pattern=CAPTURE_CLASS,
    pattern_flags="",
    contract=CONTRACT,
)
def autoar_jsendpoint_assignment_capture_excludes_ascii_delimiters():
    character = String("capture_character")
    return [And(Length(character) == 1, InRe(character, SOURCE_CLASS))], Or(
        *[character == StringVal(value) for value in FORBIDDEN_ASCII]
    )


def _mutated_quote_replays(witness: dict) -> bool:
    return (
        witness.get("capture_character") == '"'
        and mutation_reproduces_quote(witness)
    )


@prop(
    "AA-autoar-jsendpoint-mutated-quote-capture",
    "MUTATION GUARD: removing the double-quote exclusion admits a quote in "
    "the capture class and the weakened pinned parser must store it",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
    ground_truth=_mutated_quote_replays,
)
def autoar_jsendpoint_mutated_quote_capture():
    character = String("capture_character")
    return [
        And(Length(character) == 1, InRe(character, WEAK_CLASS)),
        character == StringVal('"'),
    ], character == StringVal('"')


__all__ = ["CONTRACT", "FAMILY", "PIN", "SITE"]

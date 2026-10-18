"""Shape-1 deny-list property for Anax organization create/delete input."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import And, InRe, Length, Not, Range, Re, String, StringVal, Union, Xor

from regexproof.compiler import compile_pattern
from regexproof.groundtruth.anax_org_validate_replay import (
    SOURCE_PATTERN,
    mutation_reproduces_question_mark,
)
from regexproof.harness.core import prop

PIN = "2f3fa5a506d6565fa68858b7963450567ddda114"
FAMILY = "AN-anax-orgname-denylist"
SITE = f"open-horizon/anax@{PIN}:cli/cliutils/cliutils.go:2277:MatchString"
PROPERTY_ID = "AN-anax-orgname-denylist-validation"
MUTATION_ID = "AN-anax-orgname-denylist-mutated-question-mark"
PROJECTION_PATTERN = r"^[_,\s\?\']$"
MUTATED_PROJECTION_PATTERN = r"^[_,\s\']$"
FORBIDDEN_ASCII = ("_", ",", " ", "\t", "\n", "\f", "\r", "?", "'")

_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-15-autonomous-anax-org-validate-20r2"
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
            f"Anax Go RE2 deny-list projection is not encodable: {compiled.unencodable_reason}"
        )
    return compiled.mirror


SOURCE_CLASS = _mirror(PROJECTION_PATTERN)
WEAK_CLASS = _mirror(MUTATED_PROJECTION_PATTERN)
EXPECTED_CLASS = Union(*[Re(character) for character in FORBIDDEN_ASCII])
ASCII_CHAR = Range("\x00", "\x7f")


@prop(
    PROPERTY_ID,
    "The pinned Go RE2 organization deny-list class matches exactly the "
    "documented invalid ASCII characters in its one-character projection",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="ascii",
    call_kind="fullmatch",
    pattern=PROJECTION_PATTERN,
    pattern_flags="",
    contract=CONTRACT,
)
def anax_orgname_denylist_matches_documented_characters():
    character = String("character")
    source_matches = InRe(character, SOURCE_CLASS)
    documented_invalid = InRe(character, EXPECTED_CLASS)
    return [And(Length(character) == 1, InRe(character, ASCII_CHAR))], Xor(
        source_matches, documented_invalid
    )


def _question_mark_mutation_replays(witness: dict) -> bool:
    return mutation_reproduces_question_mark(witness)


@prop(
    MUTATION_ID,
    "MUTATION GUARD: removing question-mark from the deny-list admits `?` "
    "and the weakened pinned ValidateOrg function must fail to reject it",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
    call_kind="fullmatch",
    pattern=MUTATED_PROJECTION_PATTERN,
    pattern_flags="",
    ground_truth=_question_mark_mutation_replays,
)
def anax_orgname_mutated_denylist_admits_question_mark():
    character = String("character")
    return [
        And(Length(character) == 1, Not(InRe(character, WEAK_CLASS))),
        character == StringVal("?"),
    ], character == StringVal("?")


__all__ = [
    "CONTRACT",
    "FAMILY",
    "FORBIDDEN_ASCII",
    "MUTATION_ID",
    "PIN",
    "PROPERTY_ID",
    "SITE",
    "SOURCE_PATTERN",
]

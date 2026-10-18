"""Shape-1 alphabet proof for Real-Router's shared segment validator."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import InRe, Length, Not, Range, Re, String, Union

from regexproof.compiler import compile_pattern
from regexproof.groundtruth.real_router_segment_replay import (
    mutation_accepts_slash_in_all_segment_testers,
)
from regexproof.harness.core import prop

PIN = "55aa7ef43a9c129beba90823cd8a4db10bb01211"
REPOSITORY = "https://github.com/greydragon888/real-router"
REPO_ID = "greydragon888/real-router"
SOURCE_FILE = "packages/route-utils/src/constants.ts"
SOURCE_PATTERN = r"^[\w.-]+$"
WEAK_PATTERN = r"^[\w.\/-]+$"
SITE = f"{REPO_ID}@{PIN}:{SOURCE_FILE}:13:column-36"
FAMILY = "RR-route-segment-alphabet"
PROPERTY_ID = "RR-route-segment-allowed-alphabet"
MUTATION_ID = "RR-route-segment-slash-allowlist-mutation"

_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-16-p2-real-router-segment"
    / "contract.json"
)
CONTRACT = json.loads(_CONTRACT_PATH.read_text(encoding="utf-8"))


def _compiled(pattern: str):
    result = compile_pattern(
        pattern,
        dialect="ecma",
        call_kind="search",
        max_length=64,
        domain="ascii",
    )
    if result.mirror is None or result.meta is None or not result.meta.get("mirror_exact"):
        raise RuntimeError(
            f"Real-Router segment pattern has no faithful ECMA mirror: "
            f"{result.unencodable_reason}"
        )
    return result.mirror


SOURCE_LANGUAGE = _compiled(SOURCE_PATTERN)
WEAK_LANGUAGE = _compiled(WEAK_PATTERN)
ALLOWED_CHAR = Union(
    Range("A", "Z"),
    Range("a", "z"),
    Range("0", "9"),
    Re("_"),
    Re("."),
    Re("-"),
)
ASCII_CHAR = Range("\x00", "\x7f")


@prop(
    PROPERTY_ID,
    "For an ASCII code unit, membership in the exact pinned segment regex "
    "implies that the code unit is an ASCII letter, digit, underscore, dot, "
    "or hyphen",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    pattern=SOURCE_PATTERN,
    pattern_flags="",
    contract=CONTRACT,
)
def real_router_segment_regex_has_only_documented_ascii_characters():
    character = String("segment_char")
    return [
        Length(character) == 1,
        InRe(character, ASCII_CHAR),
        InRe(character, SOURCE_LANGUAGE),
    ], Not(InRe(character, ALLOWED_CHAR))


@prop(
    MUTATION_ID,
    "MUTATION GUARD: adding slash to the exact pinned segment regex must "
    "admit `/` and all three exact helper functions must accept it",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    pattern=WEAK_PATTERN,
    pattern_flags="",
    ground_truth=mutation_accepts_slash_in_all_segment_testers,
)
def real_router_segment_slash_allowlist_mutation():
    character = String("segment_char")
    return [
        Length(character) == 1,
        character == "/",
        InRe(character, WEAK_LANGUAGE),
    ], character == "/"


__all__ = [
    "CONTRACT",
    "FAMILY",
    "MUTATION_ID",
    "PIN",
    "PROPERTY_ID",
    "REPO_ID",
    "REPOSITORY",
    "SITE",
    "SOURCE_FILE",
    "SOURCE_PATTERN",
]

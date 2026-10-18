"""Shape-1 proof for Real-Router's navigation parameter control filter."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import InRe, Length, Not, Range, Re, String, Union

from regexproof.compiler import compile_pattern
from regexproof.groundtruth.real_router_navigation_replay import (
    del_removal_mutation_reproduces,
)
from regexproof.harness.core import prop

PIN = "55aa7ef43a9c129beba90823cd8a4db10bb01211"
REPOSITORY = "https://github.com/greydragon888/real-router"
REPO_ID = "greydragon888/real-router"
SOURCE_FILE = "packages/validation-plugin/src/validators/navigation.ts"
SOURCE_PATTERN = r"[\u0000-\u001F\u007F]"
WEAK_PATTERN = r"[\u0000-\u001F]"
SITE = f"{REPO_ID}@{PIN}:{SOURCE_FILE}:69:column-25"
FAMILY = "RR-navigation-param-control-characters"
PROPERTY_ID = "RR-navigation-param-control-characters-rejected"
MUTATION_ID = "RR-navigation-param-del-omission-mutation"

_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-16-p2-real-router-navigation-source-review"
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
            "Real-Router navigation control regex has no faithful ECMA mirror: "
            f"{result.unencodable_reason}"
        )
    return result.mirror


SOURCE_LANGUAGE = _compiled(SOURCE_PATTERN)
WEAK_LANGUAGE = _compiled(WEAK_PATTERN)
CONTROL_CHAR = Union(Range("\x00", "\x1f"), Re("\x7f"))


@prop(
    PROPERTY_ID,
    "Every one-code-unit ASCII C0 or DEL character is matched by the exact "
    "pinned search regex used for string navigation parameter values",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    pattern=SOURCE_PATTERN,
    pattern_flags="",
    contract=CONTRACT,
)
def real_router_navigation_control_class_covers_c0_and_del():
    character = String("navigation_control_char")
    return [
        Length(character) == 1,
        InRe(character, CONTROL_CHAR),
    ], Not(InRe(character, SOURCE_LANGUAGE))


@prop(
    MUTATION_ID,
    "MUTATION GUARD: removing DEL from CONTROL_CHARS_RE must admit DEL and "
    "the exact pinned validateNavigateParams helper must then accept it",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    pattern=WEAK_PATTERN,
    pattern_flags="",
    ground_truth=del_removal_mutation_reproduces,
)
def real_router_navigation_del_omission_mutation():
    character = String("navigation_control_char")
    return [
        Length(character) == 1,
        character == "\u007f",
        Not(InRe(character, WEAK_LANGUAGE)),
    ], character == "\u007f"


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

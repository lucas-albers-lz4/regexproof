"""Tracecat nsjail environment-key separator exclusion contract."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import And, Contains, Concat, InRe, Range, Re, Star, String, StringVal, Union

from regexproof.groundtruth.tracecat_sandbox_env_key_replay import (
    MUTATION_NAME,
    PIN,
    SOURCE_PATTERN,
    equals_mutation_reproduces,
)
from regexproof.harness.core import prop

FAMILY = "TC-tracecat-sandbox-env-key"
PROPERTY_ID = "TC-sandbox-env-key-excludes-equals"
MUTATION_ID = "TC-sandbox-env-key-equals-mutation"
SITE = (
    f"TracecatHQ/tracecat@{PIN}:"
    "tracecat/sandbox/executor.py:71:re.compile"
)

_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-17-autonomous-tracecat-sandbox-env-equals"
    / "contract.json"
)
CONTRACT = json.loads(_CONTRACT_PATH.read_text(encoding="utf-8"))

FIRST_CHAR = Union(Re("_"), Range("a", "z"), Range("A", "Z"))
TAIL_CHAR = Union(FIRST_CHAR, Range("0", "9"))
BASE_NAME = Concat(FIRST_CHAR, Star(TAIL_CHAR))
# Exact CPython `$` semantics without MULTILINE: it may match before one final LF.
PYTHON_MATCH_LANGUAGE = Union(
    BASE_NAME,
    Concat(BASE_NAME, Re("\n")),
)
WEAK_TAIL_CHAR = Union(TAIL_CHAR, Re("="))
WEAK_BASE_NAME = Concat(FIRST_CHAR, Star(WEAK_TAIL_CHAR))
WEAK_MATCH_LANGUAGE = Union(
    WEAK_BASE_NAME,
    Concat(WEAK_BASE_NAME, Re("\n")),
)


@prop(
    PROPERTY_ID,
    "The exact pinned environment-key alphabet excludes the POSIX name/value "
    "separator '=' at every position (no string length bound)",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="unicode",
    call_kind="match",
    pattern=SOURCE_PATTERN,
    pattern_flags="",
    contract=CONTRACT,
)
def sandbox_env_key_excludes_equals():
    # Shape 1: every accepted key character comes from these regex classes,
    # plus the optional final LF permitted by Python '$'.
    key_char = String("sandbox_env_key_char")
    accepted_char = Union(FIRST_CHAR, Range("0", "9"), Re("\n"))
    return [InRe(key_char, accepted_char)], key_char == StringVal("=")


@prop(
    MUTATION_ID,
    "MUTATION GUARD: adding '=' to the exact pattern tail must admit a name "
    "with the POSIX name/value separator and reproduce in the source validator",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="unicode",
    call_kind="match",
    pattern=SOURCE_PATTERN,
    pattern_flags="",
    ground_truth=equals_mutation_reproduces,
)
def sandbox_env_key_equals_mutation():
    key = String("mutated_sandbox_env_key")
    return [
        key == StringVal(MUTATION_NAME),
        InRe(key, WEAK_MATCH_LANGUAGE),
    ], And(Contains(key, StringVal("=")), InRe(key, WEAK_MATCH_LANGUAGE))


__all__ = [
    "CONTRACT",
    "FAMILY",
    "MUTATION_ID",
    "PROPERTY_ID",
    "SITE",
    "SOURCE_PATTERN",
]

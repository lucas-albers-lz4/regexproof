"""Tracecat table and column identifier allowlist property."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import Concat, InRe, Length, Range, Re, Star, String, StringVal, Union

from regexproof.groundtruth.tracecat_table_identifier_replay import (
    IDENTIFIER_PATTERN,
    MUTATION_NAME,
    PIN,
    table_identifier_quote_mutation_reproduces,
)
from regexproof.harness.core import prop

FAMILY = "TC-tracecat-table-identifier"
PROPERTY_ID = "TC-table-identifier-double-quote-excluded"
MUTATION_ID = "TC-table-identifier-quote-mutation"
SITE = f"TracecatHQ/tracecat@{PIN}:tracecat/tables/schemas.py:17:re.compile"

_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-17-autonomous-tracecat-table-identifier"
    / "contract.json"
)
CONTRACT = json.loads(_CONTRACT_PATH.read_text(encoding="utf-8"))

FIRST_IDENTIFIER_CHAR = Union(Range("a", "z"), Range("A", "Z"), Re("_"))
IDENTIFIER_CHAR = Union(
    FIRST_IDENTIFIER_CHAR,
    Range("0", "9"),
)
IDENTIFIER_RE = Concat(FIRST_IDENTIFIER_CHAR, Star(IDENTIFIER_CHAR))
WEAKENED_TAIL_CHAR = Union(IDENTIFIER_CHAR, Re('"'))
WEAKENED_IDENTIFIER_RE = Concat(
    FIRST_IDENTIFIER_CHAR,
    Star(WEAKENED_TAIL_CHAR),
)


@prop(
    PROPERTY_ID,
    "A one-character value admitted by the exact pinned table/column identifier "
    "allowlist cannot contain a double quote",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="unicode",
    call_kind="search",
    pattern=IDENTIFIER_PATTERN,
    pattern_flags="",
    contract=CONTRACT,
)
def table_identifier_double_quote_excluded():
    identifier_char = String("identifier_char")
    return [Length(identifier_char) == 1, InRe(identifier_char, IDENTIFIER_RE)], (
        identifier_char == StringVal('"')
    )


@prop(
    MUTATION_ID,
    "MUTATION GUARD: admitting a double quote in the exact request-model "
    "allowlist must admit it to the model and retain the independent service rejection",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="unicode",
    call_kind="search",
    pattern=IDENTIFIER_PATTERN,
    pattern_flags="",
    ground_truth=table_identifier_quote_mutation_reproduces,
)
def table_identifier_quote_mutation():
    name = String("mutated_identifier_name")
    return [InRe(name, WEAKENED_IDENTIFIER_RE), name == StringVal(MUTATION_NAME)], (
        name == StringVal(MUTATION_NAME)
    )


__all__ = [
    "CONTRACT",
    "FAMILY",
    "IDENTIFIER_PATTERN",
    "MUTATION_ID",
    "PROPERTY_ID",
    "SITE",
]

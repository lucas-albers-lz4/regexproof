"""Tracecat custom RBAC scope-name glob-alphabet property and mutation guard."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import InRe, Length, Or, Plus, Range, Re, String, StringVal, Union

from regexproof.groundtruth.tracecat_rbac_scope_replay import (
    MUTATION_SCOPE,
    NONSTAR_GLOB_CHARS,
    PIN,
    SCOPE_PATTERN,
    rbac_scope_question_mark_mutation_reproduces,
)
from regexproof.harness.core import prop

FAMILY = "TC-tracecat-rbac-scope-pattern"
PROPERTY_ID = "TC-rbac-scope-nonstar-glob-metacharacters-excluded"
MUTATION_ID = "TC-rbac-scope-question-mark-mutation"
SITE = f"TracecatHQ/tracecat@{PIN}:tracecat/authz/controls.py:18:re.compile"

_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-16-autonomous-tracecat-rbac-scope-pattern"
    / "contract.json"
)
CONTRACT = json.loads(_CONTRACT_PATH.read_text(encoding="utf-8"))

ALLOWED_SCOPE_CHAR = Union(
    Range("a", "z"),
    Range("0", "9"),
    Re(":"),
    Re("_"),
    Re("."),
    Re("*"),
    Re("-"),
)
WEAKENED_SCOPE_CHAR = Union(ALLOWED_SCOPE_CHAR, Re("?"))


@prop(
    PROPERTY_ID,
    "A custom scope name admitted by the exact pinned request allowlist cannot "
    "contain fnmatch's question-mark or bracket metacharacters",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="unicode",
    call_kind="search",
    pattern=SCOPE_PATTERN,
    pattern_flags="",
    contract=CONTRACT,
)
def rbac_scope_nonstar_glob_metacharacters_excluded():
    scope_char = String("scope_char")
    outside_star_glob = [
        scope_char == StringVal(char) for char in sorted(NONSTAR_GLOB_CHARS)
    ]
    return [
        Length(scope_char) == 1,
        InRe(scope_char, ALLOWED_SCOPE_CHAR),
    ], Or(*outside_star_glob)


@prop(
    MUTATION_ID,
    "MUTATION GUARD: adding question mark to both exact scope allowlists must "
    "accept the scope name and broaden its fnmatch authorization pattern",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="unicode",
    call_kind="search",
    pattern=SCOPE_PATTERN,
    pattern_flags="",
    ground_truth=rbac_scope_question_mark_mutation_reproduces,
)
def rbac_scope_question_mark_mutation():
    scope_name = String("scope_name")
    return [
        InRe(scope_name, Plus(WEAKENED_SCOPE_CHAR)),
        scope_name == StringVal(MUTATION_SCOPE),
    ], scope_name == StringVal(MUTATION_SCOPE)


__all__ = [
    "CONTRACT",
    "FAMILY",
    "MUTATION_ID",
    "PROPERTY_ID",
    "SITE",
    "SCOPE_PATTERN",
]

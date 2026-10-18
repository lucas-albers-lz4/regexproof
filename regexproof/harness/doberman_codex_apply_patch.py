"""Contract-backed checks that Codex apply_patch targets are all extracted."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import (
    BoolVal, Concat, InRe, Length, Not, Plus, Range, Re, Star, String,
    StringVal, Union,
)

from regexproof.contract_adoption import contract_is_adopted
from regexproof.groundtruth.doberman_codex_apply_patch_replay import (
    FILE_PATTERN,
    MOVE_PATTERN,
    PIN,
    QUESTION_IDS,
    WEAKENED_FILE_PATTERN,
    mutation_reproduces,
)
from regexproof.harness.core import prop

FAMILY = "DB-codex-apply-patch-target-extraction"
CONTRACTS_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties/calibration/2026-10-15-p2-doberman-source-review/contracts.json"
)
CONTRACTS = json.loads(CONTRACTS_PATH.read_text(encoding="utf-8"))
_CONTRACT_BY_SITE = {item["site"]: item for item in CONTRACTS}
_QUESTION_SITES = {
    QUESTION_IDS[0]: f"fu351/Doberman-Core@{PIN}:src/doberman/hosthooks/codex.py:69:_APPLY_PATCH_FILE_RE",
    QUESTION_IDS[1]: f"fu351/Doberman-Core@{PIN}:src/doberman/hosthooks/codex.py:70:_APPLY_PATCH_MOVE_RE",
}
_CONTRACT_BY_QUESTION = {
    question_id: _CONTRACT_BY_SITE[site]
    for question_id, site in _QUESTION_SITES.items()
}
if any(not contract_is_adopted(item) for item in _CONTRACT_BY_QUESTION.values()):
    raise RuntimeError("Doberman Codex path contracts are missing valid adoption records")

_INDENT_CHAR = Union(Re(" "), Re("\t"))
_DOMAIN_INDENT = Union(
    Re(""), Re(" "), Re("\t"),
    Concat(_INDENT_CHAR, _INDENT_CHAR),
    Concat(_INDENT_CHAR, _INDENT_CHAR, _INDENT_CHAR),
)
_WHITESPACE = Union(Re(" "), Re("\t"))
_PRINTABLE_ASCII = Plus(Range(" ", "~"))
_ONE_PATH_CHAR = Range("!", "~")
_FILE_OP = Union(Re("Add"), Re("Update"), Re("Delete"))
_FILE_PREFIX = Concat(Re("*** "), _FILE_OP, Re(" File: "))
_MOVE_PREFIX = Re("*** Move to: ")
_FILE_DOMAIN = Concat(_DOMAIN_INDENT, _FILE_PREFIX, _ONE_PATH_CHAR)
_MOVE_DOMAIN = Concat(_DOMAIN_INDENT, _MOVE_PREFIX, _ONE_PATH_CHAR)
_FILE_MUTATION_DOMAIN = Concat(_DOMAIN_INDENT, _FILE_PREFIX, _PRINTABLE_ASCII)
_FILE_SOURCE_LANGUAGE = Concat(Star(_WHITESPACE), _FILE_PREFIX, _PRINTABLE_ASCII)
_MOVE_SOURCE_LANGUAGE = Concat(Star(_WHITESPACE), _MOVE_PREFIX, _PRINTABLE_ASCII)
_WEAKENED_FILE_LANGUAGE = Concat(
    Star(_WHITESPACE), Re("*** "),
    Union(Re("Add"), Re("Update")), Re(" File: "), _PRINTABLE_ASCII,
)


def _property(
    question_id: str,
    operation_regex,
    prefix_text: str,
    suffix_text: str,
    source_regex,
    pattern: str,
):
    @prop(
        question_id,
        _CONTRACT_BY_QUESTION[question_id]["declared_domain"],
        expect_unsat=True,
        kind="property",
        family=FAMILY,
        input_domain="ascii",
        call_kind="search",
        pattern=pattern,
        pattern_flags="m",
        contract=_CONTRACT_BY_QUESTION[question_id],
    )
    def _valid_directive_is_never_missed():
        indent = String(f"{question_id}_indent")
        operation = String(f"{question_id}_operation")
        path = String(f"{question_id}_path_character")
        line = Concat(
            indent, StringVal(prefix_text), operation,
            StringVal(suffix_text), path,
        )
        return [
            InRe(indent, _DOMAIN_INDENT),
            InRe(operation, operation_regex),
            Length(path) == 1,
            InRe(path, _ONE_PATH_CHAR),
        ], Not(InRe(line, source_regex))
    _valid_directive_is_never_missed.__name__ = question_id.replace("-", "_")
    return _valid_directive_is_never_missed


_property(
    QUESTION_IDS[0], _FILE_OP, "*** ", " File: ",
    _FILE_SOURCE_LANGUAGE, FILE_PATTERN,
)
_property(
    QUESTION_IDS[1], Re("Move to: "), "*** ", "",
    _MOVE_SOURCE_LANGUAGE, MOVE_PATTERN,
)


@prop(
    "DB-codex-apply-patch-weakened-file-regex-misses-delete",
    "MUTATION GUARD: removing Delete from the file-directive regex must stop extracting a documented Delete File target",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    pattern=WEAKENED_FILE_PATTERN,
    pattern_flags="m",
    ground_truth=mutation_reproduces,
)
def doberman_codex_weakened_file_regex_misses_delete():
    line = String("line")
    witness = StringVal("*** Delete File: .env")
    return [
        line == witness,
        InRe(line, _FILE_MUTATION_DOMAIN),
        Not(InRe(line, _WEAKENED_FILE_LANGUAGE)),
    ], BoolVal(True)


__all__ = ["CONTRACTS", "FAMILY", "QUESTION_IDS"]

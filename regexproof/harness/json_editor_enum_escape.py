"""Per-codepoint HTML text-image property for json-editor's EnumEditor."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import And, Contains, If, Length, Or, String, StringVal

from regexproof.groundtruth.json_editor_enum_escape_replay import mutation_reproduces
from regexproof.harness.core import prop

PIN = "b31ddabecf4ed3209d37a2f5b29956120cd8f9ce"
FAMILY = "JE-json-editor-enum-html-text-escape"
SITE = f"json-editor/json-editor@{PIN}:src/editors/enum.js:123:column-24"
PROPERTY_ID = "JE-json-editor-enum-string-html-text-codepoint-image"
MUTATION_ID = "JE-json-editor-enum-mutated-less-than-leaks"
_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-15-p2-json-editor-source-review"
    / "contract.json"
)
CONTRACT = json.loads(_CONTRACT_PATH.read_text(encoding="utf-8"))


def _mapped_codepoint(character, *, leak_less_than: bool = False):
    less_than = character if leak_less_than else StringVal("&lt;")
    return If(
        character == StringVal("&"),
        StringVal("&amp;"),
        If(
            character == StringVal("<"),
            less_than,
            If(character == StringVal(">"), StringVal("&gt;"), character),
        ),
    )


def _contains_markup_delimiter(mapped):
    return Or(
        Contains(mapped, StringVal("<")),
        Contains(mapped, StringVal(">")),
    )


@prop(
    PROPERTY_ID,
    "One Unicode codepoint passed through the pinned, ordered EnumEditor "
    "string replacements contains no raw less-than or greater-than delimiter",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="unicode",
    call_kind="substitution",
    contract=CONTRACT,
)
def json_editor_enum_string_html_text_codepoint_image():
    character = String("enum_string_codepoint")
    mapped = _mapped_codepoint(character)
    return [Length(character) == 1], _contains_markup_delimiter(mapped)


def _mutated_less_than_leaks(witness: dict) -> bool:
    character = witness.get("enum_string_codepoint", "")
    return character == "<" and mutation_reproduces(character)


@prop(
    MUTATION_ID,
    "MUTATION GUARD: weakening the pinned less-than entity replacement must "
    "admit a raw HTML delimiter and reproduce it in the modified exact source",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="unicode",
    ground_truth=_mutated_less_than_leaks,
)
def json_editor_enum_mutated_less_than_leaks():
    character = String("enum_string_codepoint")
    mapped = _mapped_codepoint(character, leak_less_than=True)
    return [
        And(Length(character) == 1, character == StringVal("<")),
    ], _contains_markup_delimiter(mapped)


__all__ = ["CONTRACT", "FAMILY", "MUTATION_ID", "PIN", "PROPERTY_ID", "SITE"]

"""Per-codepoint HTML text-image property for AutoAR's pinned escaper."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import And, Contains, Length, Or, String, StringVal, If

from regexproof.groundtruth.autoar_html_escape_replay import mutation_reproduces
from regexproof.harness.core import prop

PIN = "01cd447ad3b1acfed7e0680596c2c74458a4cf06"
FAMILY = "AA-autoar-html-text-escape"
SITE = (
    f"h0tak88r/AutoAR@{PIN}:"
    "internal/api/ui/pages/html-escape.js:2:esc"
)
_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-15-autonomous-autoar-html-text-escape-20r2"
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
            If(
                character == StringVal(">"),
                StringVal("&gt;"),
                If(
                    character == StringVal('"'),
                    StringVal("&quot;"),
                    If(character == StringVal("'"), StringVal("&#39;"), character),
                ),
            ),
        ),
    )


def _contains_html_structure(mapped):
    return Or(
        *[
            Contains(mapped, StringVal(token))
            for token in ("<", ">", '"', "'")
        ]
    )


@prop(
    "AA-autoar-html-text-escape-codepoint-image",
    "One Unicode codepoint mapped by the pinned esc helper emits no raw HTML "
    "tag or quote delimiter; full-string replacement composition is separately "
    "checked against the product helper by the exact-pin regression gate",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="unicode",
    call_kind="substitution",
    contract=CONTRACT,
)
def autoar_html_text_escape_codepoint_image():
    character = String("scan_result_codepoint")
    mapped = _mapped_codepoint(character)
    return [Length(character) == 1], _contains_html_structure(mapped)


def _mutated_less_than_leaks(witness: dict) -> bool:
    character = witness.get("scan_result_codepoint", "")
    return character == "<" and mutation_reproduces(character)


@prop(
    "AA-autoar-html-text-escape-mutated-less-than-leaks",
    "MUTATION GUARD: changing the pinned less-than entity replacement to a "
    "literal less-than must admit an unsafe HTML text token",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="unicode",
    ground_truth=_mutated_less_than_leaks,
)
def autoar_mutated_html_text_escape_less_than_leaks():
    character = String("scan_result_codepoint")
    mapped = _mapped_codepoint(character, leak_less_than=True)
    return [And(Length(character) == 1, character == StringVal("<"))], _contains_html_structure(mapped)


__all__ = ["CONTRACT", "FAMILY", "PIN", "SITE"]

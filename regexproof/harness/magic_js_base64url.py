"""Contract-backed per-token Base64URL output-image properties for Magic JS."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import And, Contains, If, InRe, Length, Or, Re, String, StringVal, Union

from regexproof.groundtruth.magic_js_base64url_replay import (
    CONTRACT_PATH,
    MUTATION_ID,
    QUESTION_IDS,
    mutation_reproduces,
)
from regexproof.contract_adoption import contract_is_adopted
from regexproof.harness.core import prop

FAMILY = "ME-base64url-output-image"
CONTRACTS = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
REVIEWS_PATH = CONTRACT_PATH.with_name("reviews.json")
REVIEWS = json.loads(REVIEWS_PATH.read_text(encoding="utf-8"))
_CONTRACT_BY_SITE = {contract["site"]: contract for contract in CONTRACTS}
_REVIEW_BY_QUESTION = {
    item["question_id"]: item
    for item in REVIEWS["reviews"]
    if item.get("decision") == "adopted"
}


def _contract_site(review_site: str) -> str:
    source_file, line, column = review_site.rsplit(":", 2)
    return f"magiclabs/magic-js@e9fb233763160316989863b4739c4656133d45b0:{source_file}:{line}:column-{column}"


_CONTRACT_BY_QUESTION = {
    question_id: _CONTRACT_BY_SITE[_contract_site(_REVIEW_BY_QUESTION[question_id]["site"])]
    for question_id in QUESTION_IDS
}
if len(_CONTRACT_BY_QUESTION) != len(QUESTION_IDS) or any(
    not contract_is_adopted(contract)
    for contract in _CONTRACT_BY_QUESTION.values()
):
    raise RuntimeError("Magic JS harness contracts are incomplete or not adopted")
_STANDARD_BASE64 = Union(*(Re(char) for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="))


def _mapped_token(token, *, leak_plus: bool = False):
    plus = token if leak_plus else StringVal("-")
    return If(
        token == StringVal("="),
        StringVal(""),
        If(
            token == StringVal("+"),
            plus,
            If(token == StringVal("/"), StringVal("_"), token),
        ),
    )


def _forbidden_base64url_symbol(value):
    return Or(
        Contains(value, StringVal("=")),
        Contains(value, StringVal("+")),
        Contains(value, StringVal("/")),
    )


for _question_id in QUESTION_IDS:
    _contract = _CONTRACT_BY_QUESTION[_question_id]
    _pattern = _REVIEW_BY_QUESTION[_question_id]["pattern"]

    def _property(question_id: str = _question_id):
        token = String(f"{question_id}_standard_base64_codepoint")
        mapped = _mapped_token(token)
        return [
            And(Length(token) == 1, InRe(token, _STANDARD_BASE64)),
        ], _forbidden_base64url_symbol(mapped)

    _property.__name__ = _question_id.replace("-", "_")
    prop(
        _question_id,
        _contract["declared_domain"],
        expect_unsat=True,
        kind="property",
        family=FAMILY,
        input_domain="ascii",
        call_kind="substitution",
        pattern=_pattern,
        contract=_contract,
    )(_property)


def _mutation_replays(witness: dict) -> bool:
    return witness.get("base64url_character") == "+" and mutation_reproduces(
        {"base64_character": "+"}
    )


@prop(
    MUTATION_ID,
    "MUTATION GUARD: weakening the pinned plus-to-hyphen replacement admits a raw plus in the Base64URL output",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
    ground_truth=_mutation_replays,
)
def magic_js_base64url_mutated_plus_leaks():
    token = String("base64url_character")
    mapped = _mapped_token(token, leak_plus=True)
    return [And(Length(token) == 1, token == StringVal("+"))], Contains(
        mapped, StringVal("+")
    )


__all__ = [
    "CONTRACTS", "FAMILY", "MUTATION_ID", "QUESTION_IDS",
    "magic_js_base64url_mutated_plus_leaks",
]

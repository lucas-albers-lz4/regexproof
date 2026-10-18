"""Capture-boundary property for Xibo's pinned OAuth consent CSRF cookie helper."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import And, InRe, Length, Range, String, StringVal, Union

from regexproof.groundtruth.xibo_csrf_cookie_replay import mutation_reproduces
from regexproof.harness.core import prop

PIN = "978def55c8e68cab3a50a7ee4725039da753f0a1"
FAMILY = "XC-xibo-csrf-cookie-capture"
SITE = (
    f"xibosignage/xibo-cms@{PIN}:"
    "frontend/src/pages/Administration/Applications/Authorize/AuthorizeApplication.tsx:42:38"
)
PATTERN = r"(?:^|;\s*)XSRF-TOKEN=([^;]*)"
QUESTION_ID = "XC-xibo-csrf-cookie-capture-isolation"
MUTATION_ID = "XC-xibo-csrf-cookie-mutated-capture-spills"
CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-15-autonomous-xibo-csrf-cookie-20r2"
    / "contract.json"
)
CONTRACT = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))

# ASCII 0x00..0x3a and 0x3c..0x7f: all ASCII characters except semicolon.
# Keep this as a one-character regex class; Complement() over arbitrary strings
# would mean language complement, as documented in TRAPS.md #1.
_NO_SEMICOLON_ASCII = Union(Range("\u0000", ":"), Range("<", "\u007f"))
_ASCII = Range("\u0000", "\u007f")


@prop(
    QUESTION_ID,
    "The exact pinned capture body [^;] admits no ASCII semicolon; the product "
    "gate separately replays complete JavaScript helper behavior",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    pattern=PATTERN,
    contract=CONTRACT,
)
def xibo_csrf_cookie_capture_isolation():
    character = String("captured_cookie_character")
    return [And(Length(character) == 1, InRe(character, _NO_SEMICOLON_ASCII))], (
        character == StringVal(";")
    )


def _mutation_spill_reproduced(witness: dict) -> bool:
    character = witness.get("captured_cookie_character", "")
    return character == ";" and mutation_reproduces(character)


@prop(
    MUTATION_ID,
    "MUTATION GUARD: widening the exact pinned capture from [^;]* to .* must "
    "admit a semicolon and reproduce capture spill into the next cookie pair",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    ground_truth=_mutation_spill_reproduced,
)
def xibo_csrf_cookie_mutated_capture_spills():
    character = String("captured_cookie_character")
    return [And(Length(character) == 1, InRe(character, _ASCII))], (
        character == StringVal(";")
    )


__all__ = ["CONTRACT", "FAMILY", "MUTATION_ID", "PATTERN", "PIN", "QUESTION_ID", "SITE"]

"""Tracecat origin-slug substitution image property and mutation guard."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import If, InRe, Length, Not, Re, Range, String, StringVal, Union

from regexproof.harness.core import prop
from regexproof.groundtruth.tracecat_replay import mutation_reproduces

PIN = "c84d52528a489821f355fc63976fbc7783ae0ad5"
FAMILY = "TC-tracecat-origin-key"
PATTERN = r"[^a-zA-Z0-9_-]"
SITE = (
    f"TracecatHQ/tracecat@{PIN}:"
    "tracecat/registry/artifact_keys.py:46:_slugify_origin"
)
_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-14-autonomous-tracecat-origin-slug"
    / "contract.json"
)
CONTRACT = json.loads(_CONTRACT_PATH.read_text(encoding="utf-8"))

SAFE_CHAR = Union(
    Range("a", "z"),
    Range("A", "Z"),
    Range("0", "9"),
    Re("_"),
    Re("-"),
)
WEAK_SAFE_CHAR = Union(SAFE_CHAR, Re("/"))


@prop(
    "TC-tracecat-origin-slug-safe-image",
    "The first _slugify_origin substitution maps each Unicode code point to "
    "the ASCII S3-component alphabet [A-Za-z0-9_-]",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="unicode",
    call_kind="substitution",
    pattern=PATTERN,
    pattern_flags="",
    contract=CONTRACT,
)
def tracecat_origin_slug_safe_image():
    """Prove the pointwise image; helper composition is checked by the gate."""
    char = String("c")
    safe = InRe(char, SAFE_CHAR)
    matched_by_source_class = Not(safe)
    substituted = If(matched_by_source_class, StringVal("_"), char)
    return [Length(char) == 1], Not(InRe(substituted, SAFE_CHAR))


def _tracecat_slash_mutation_replays(witness: dict) -> bool:
    char = witness.get("c")
    return char == "/" and mutation_reproduces(char)


@prop(
    "TC-tracecat-mutated-origin-slash-passthrough",
    "MUTATION GUARD: allowing slash in the preserved alphabet admits a path "
    "separator and must expose an unsafe origin-derived S3 key component",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="unicode",
    ground_truth=_tracecat_slash_mutation_replays,
)
def tracecat_mutated_origin_slash_passthrough():
    char = String("c")
    return [Length(char) == 1, InRe(char, WEAK_SAFE_CHAR)], char == StringVal("/")

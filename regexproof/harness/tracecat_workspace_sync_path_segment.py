"""Tracecat workspace-sync path segment image property and mutation guard."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import If, InRe, Length, Not, Range, Re, String, StringVal, Union

from regexproof.groundtruth.tracecat_workspace_sync_path_segment_replay import (
    PIN,
    SAFE_CHARS,
    SOURCE_PATTERN,
    weakened_path_segment_preserves_colon,
)
from regexproof.harness.core import prop

FAMILY = "TC-tracecat-workspace-sync-path-segment"
PROPERTY_ID = "TC-workspace-sync-path-segment-component-image"
MUTATION_ID = "TC-workspace-sync-path-segment-colon-mutation"
SITE = (
    f"TracecatHQ/tracecat@{PIN}:"
    "tracecat/workspace_sync/adapters/base.py:936:re.sub"
)

_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-16-autonomous-tracecat-workspace-sync-path-segment"
    / "contract.json"
)
CONTRACT = json.loads(_CONTRACT_PATH.read_text(encoding="utf-8"))

SAFE_PATH_CHAR = Union(
    Range("A", "Z"),
    Range("a", "z"),
    Range("0", "9"),
    Re("_"),
    Re("."),
    Re("-"),
)
WEAK_SAFE_PATH_CHAR = Union(SAFE_PATH_CHAR, Re(":"))


@prop(
    PROPERTY_ID,
    "Each output character from the pinned path_segment substitution belongs "
    "to its ASCII path-component alphabet",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="unicode",
    call_kind="substitution",
    pattern=SOURCE_PATTERN,
    pattern_flags="",
    contract=CONTRACT,
)
def workspace_sync_path_segment_component_image():
    """Prove substitution-image safety; exact helper composition is replayed."""
    char = String("segment_char")
    source_preserves = InRe(char, SAFE_PATH_CHAR)
    output_char = If(source_preserves, char, StringVal("-"))
    return [Length(char) == 1], Not(InRe(output_char, SAFE_PATH_CHAR))


@prop(
    MUTATION_ID,
    "MUTATION GUARD: allowing colon in the source class must preserve colon "
    "through path_segment and violate the component alphabet",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="unicode",
    ground_truth=lambda witness: (
        witness.get("segment_char") == ":"
        and weakened_path_segment_preserves_colon(witness["segment_char"])
    ),
)
def workspace_sync_path_segment_colon_mutation():
    char = String("segment_char")
    return [Length(char) == 1, InRe(char, WEAK_SAFE_PATH_CHAR)], char == StringVal(":")


__all__ = [
    "CONTRACT",
    "FAMILY",
    "MUTATION_ID",
    "PROPERTY_ID",
    "SAFE_CHARS",
    "SITE",
    "SOURCE_PATTERN",
]

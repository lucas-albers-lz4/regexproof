"""Tracecat path-segment substitution image property and traversal mutation."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import If, InRe, Length, Not, Re, Range, String, StringVal, Union

from regexproof.groundtruth.tracecat_artifact_path_segment_replay import (
    PIN,
    SOURCE_PATTERN,
    weakened_path_escapes_artifact_root,
)
from regexproof.harness.core import prop

FAMILY = "TC-tracecat-artifact-path-segment"
PROPERTY_ID = "TC-artifact-path-segment-safe-image"
MUTATION_ID = "TC-artifact-path-segment-slash-escape-mutation"
SITE = (
    f"TracecatHQ/tracecat@{PIN}:"
    "packages/tracecat-ee/tracecat_ee/agent/artifacts/mount_only_provider.py:31:_SAFE_PATH_SEGMENT_RE"
)

_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-16-autonomous-tracecat-artifact-path-segment"
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
WEAK_SAFE_PATH_CHAR = Union(SAFE_PATH_CHAR, Re("/"))


@prop(
    PROPERTY_ID,
    "Each output token from the pinned path-segment substitution is in its "
    "ASCII component alphabet; therefore it cannot emit slash or backslash",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="unicode",
    call_kind="substitution",
    pattern=SOURCE_PATTERN,
    pattern_flags="",
    contract=CONTRACT,
)
def artifact_path_segment_safe_image():
    """Prove the per-character image; exact run composition is replayed in the gate."""
    char = String("segment_char")
    source_preserves = InRe(char, SAFE_PATH_CHAR)
    output_char = If(source_preserves, char, StringVal("_"))
    return [Length(char) == 1], Not(InRe(output_char, SAFE_PATH_CHAR))


@prop(
    MUTATION_ID,
    "MUTATION GUARD: retaining slash in the source class must let a traversal "
    "segment escape the artifact root after Path composition",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="unicode",
    ground_truth=lambda witness: (
        witness.get("segment_char") == "/"
        and weakened_path_escapes_artifact_root(witness["segment_char"])
    ),
)
def artifact_path_segment_slash_mutation():
    char = String("segment_char")
    return [Length(char) == 1, InRe(char, WEAK_SAFE_PATH_CHAR)], char == StringVal("/")


__all__ = [
    "CONTRACT",
    "FAMILY",
    "MUTATION_ID",
    "PROPERTY_ID",
    "SITE",
    "SOURCE_PATTERN",
]

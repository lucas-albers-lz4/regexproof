"""Counterexample finder for third-party YARA descriptions in Markdown tables."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import And, InRe, Not, String, StringVal

from regexproof.compiler import compile_pattern
from regexproof.groundtruth.malcontent_description_markdown_replay import (
    PATTERN,
    WITNESS,
    ground_truth_reproduces,
)
from regexproof.harness.core import prop

PIN = "ea3e83e24676a1678a9522141da29b636c9451ab"
FAMILY = "MC-malcontent-description-markdown"
SITE = f"chainguard-dev/malcontent@{PIN}:pkg/report/report.go:118:threatHuntingKeywordRe"
COUNTEREXAMPLE_ID = "MC-malcontent-description-metadata-extra-markdown-link"
MUTATION_ID = "MC-malcontent-description-capture-mutation-guard"
_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-15-autonomous-malcontent-description-markdown-20r2"
    / "contract.json"
)
CONTRACT = json.loads(_CONTRACT_PATH.read_text(encoding="utf-8"))

_CURRENT = compile_pattern(PATTERN, dialect="re2", call_kind="search", domain="ascii")
_SAFE_BASELINE_PATTERN = (
    r"Detection patterns for the tool '([^|]*)' taken from the "
    r"ThreatHunting-Keywords github project"
)
_SAFE_BASELINE = compile_pattern(
    _SAFE_BASELINE_PATTERN, dialect="re2", call_kind="search", domain="ascii"
)
if _CURRENT.mirror is None or _SAFE_BASELINE.mirror is None:
    raise RuntimeError(
        "Malcontent description regex/mutation baseline is not encodable: "
        f"current={_CURRENT.unencodable_reason!r}, "
        f"baseline={_SAFE_BASELINE.unencodable_reason!r}"
    )


def _query():
    description = String("description_metadata")
    return description, And(
        InRe(description, _CURRENT.mirror),
        Not(InRe(description, _SAFE_BASELINE.mirror)),
    )


@prop(
    COUNTEREXAMPLE_ID,
    "The pinned threatHuntingKeywordRe search capture must not emit a raw "
    "Markdown link and table delimiter from third-party description metadata",
    expect_unsat=False,
    kind="counterexample_finder",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    pattern=PATTERN,
    pattern_flags="",
    ground_truth=ground_truth_reproduces,
    contract=CONTRACT,
)
def malcontent_description_metadata_extra_markdown_link():
    description, bad = _query()
    return [description == StringVal(WITNESS)], bad


@prop(
    MUTATION_ID,
    "MUTATION GUARD: the broad tool-name capture admits the raw table-column "
    "delimiter and Markdown-link witness excluded by a delimiter-restricting baseline",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    ground_truth=ground_truth_reproduces,
)
def malcontent_description_capture_mutation_guard():
    description, bad = _query()
    return [description == StringVal(WITNESS)], bad


__all__ = [
    "CONTRACT", "COUNTEREXAMPLE_ID", "FAMILY", "MUTATION_ID", "PIN", "SITE"
]

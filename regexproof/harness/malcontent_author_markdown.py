"""Source-regex counterexample for Malcontent author metadata Markdown links."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import And, InRe, Not, String, StringVal

from regexproof.compiler import compile_pattern
from regexproof.groundtruth.malcontent_author_markdown_replay import (
    PATTERN,
    WITNESS,
    ground_truth_reproduces,
)
from regexproof.harness.core import prop

PIN = "ea3e83e24676a1678a9522141da29b636c9451ab"
FAMILY = "MC-malcontent-author-markdown-link"
SITE = f"chainguard-dev/malcontent@{PIN}:pkg/report/report.go:117:authorWithURLRe"
COUNTEREXAMPLE_ID = "MC-malcontent-author-metadata-extra-markdown-link"
MUTATION_ID = "MC-malcontent-author-metadata-capture-mutation-guard"
_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-15-autonomous-malcontent-author-markdown-20r2"
    / "contract.json"
)
CONTRACT = json.loads(_CONTRACT_PATH.read_text(encoding="utf-8"))

_CURRENT = compile_pattern(
    PATTERN,
    dialect="re2",
    call_kind="search",
    domain="ascii",
)
_SAFE_BASELINE_PATTERN = r"^(.*?) \((http[^)\r\n]*)\)$"
_SAFE_BASELINE = compile_pattern(
    _SAFE_BASELINE_PATTERN,
    dialect="re2",
    call_kind="search",
    domain="ascii",
)
if _CURRENT.mirror is None or _SAFE_BASELINE.mirror is None:
    raise RuntimeError(
        "Malcontent author-link regex/mutation baseline is not encodable: "
        f"current={_CURRENT.unencodable_reason!r}, "
        f"baseline={_SAFE_BASELINE.unencodable_reason!r}"
    )


def _query():
    author = String("author_metadata")
    return author, And(
        InRe(author, _CURRENT.mirror),
        Not(InRe(author, _SAFE_BASELINE.mirror)),
    )


@prop(
    COUNTEREXAMPLE_ID,
    "The pinned authorWithURLRe search capture must not permit source metadata "
    "to close its Markdown link and add a second external link",
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
def malcontent_author_metadata_extra_markdown_link():
    author, bad = _query()
    return [author == StringVal(WITNESS)], bad


@prop(
    MUTATION_ID,
    "MUTATION GUARD: weakening an anchored URL capture that excludes close "
    "parentheses to the pinned http.* capture admits the Markdown-link witness",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    ground_truth=ground_truth_reproduces,
)
def malcontent_author_metadata_capture_mutation_guard():
    author, bad = _query()
    return [author == StringVal(WITNESS)], bad


__all__ = ["CONTRACT", "COUNTEREXAMPLE_ID", "FAMILY", "MUTATION_ID", "PIN", "SITE"]

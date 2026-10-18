"""Aidevops pre-dispatch cited-file path traversal counterexample."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import (
    And,
    Concat,
    InRe,
    Length,
    Plus,
    PrefixOf,
    Range,
    Re,
    String,
    StringVal,
    SuffixOf,
    Union,
)

from regexproof.groundtruth.aidevops_cited_file_replay import (
    PIN,
    SOURCE_PATTERN,
    TRAVERSAL_WITNESS,
    cited_file_traversal_reproduces,
)
from regexproof.harness.core import prop

FAMILY = "AE-aidevops-predispatch-cited-file"
PROPERTY_ID = "AE-aidevops-predispatch-cited-file-traversal-read"
MUTATION_ID = "AE-aidevops-predispatch-cited-file-traversal-mutation-guard"
SITE = (
    f"marcusquinn/aidevops@{PIN}:"
    ".agents/scripts/pre-dispatch-validator-helper.sh:1878:column-46"
)

_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-16-autonomous-aidevops-predispatch-github-text-20r2"
    / "contract-cited-file-path.json"
)
CONTRACT = json.loads(_CONTRACT_PATH.read_text(encoding="utf-8"))

# The extractor is line-oriented, so LF is not part of a captured token. Shell
# variables cannot contain NUL. The remaining ASCII characters exclude only
# the literal space and `>` delimiters in the pinned ERE.
TOKEN_CHAR = Union(
    Range("\x01", "\x09"),
    Range("\x0b", "\x1f"),
    Range("\x21", "="),
    Range("?", "\x7f"),
)
CAPTURE_RE = Concat(Re("cited_file="), Plus(TOKEN_CHAR))


@prop(
    PROPERTY_ID,
    "The issue-body cited_file capture language contains a path that escapes "
    "the cloned repository and reaches the large-file line-count sink",
    expect_unsat=False,
    kind="counterexample_finder",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    pattern=SOURCE_PATTERN,
    pattern_flags="",
    contract=CONTRACT,
    ground_truth=cited_file_traversal_reproduces,
)
def cited_file_traversal_reaches_line_count_sink():
    cited_file = String("cited_file")
    return [
        InRe(Concat(StringVal("cited_file="), cited_file), CAPTURE_RE),
        InRe(cited_file, Plus(TOKEN_CHAR)),
        Length(cited_file) == len(TRAVERSAL_WITNESS),
    ], And(
        PrefixOf(StringVal("../"), cited_file),
        SuffixOf(StringVal("oracle.txt"), cited_file),
    )


@prop(
    MUTATION_ID,
    "MUTATION GUARD: removing the intended parent-component rejection must "
    "admit the exact pinned path-traversal witness",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    pattern=SOURCE_PATTERN,
    pattern_flags="",
    ground_truth=cited_file_traversal_reproduces,
)
def cited_file_parent_component_mutation_guard():
    cited_file = String("cited_file")
    return [
        InRe(Concat(StringVal("cited_file="), cited_file), CAPTURE_RE),
        cited_file == StringVal(TRAVERSAL_WITNESS),
    ], cited_file == StringVal(TRAVERSAL_WITNESS)


__all__ = [
    "CONTRACT",
    "FAMILY",
    "MUTATION_ID",
    "PROPERTY_ID",
    "SITE",
    "SOURCE_PATTERN",
]

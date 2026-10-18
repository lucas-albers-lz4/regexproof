"""Aidevops threshold parsing counterexample at the Bash arithmetic sink."""
from __future__ import annotations

import json
from pathlib import Path

from z3 import And, Concat, InRe, Length, Plus, Range, Re, String, StringVal, Union

from regexproof.groundtruth.aidevops_threshold_replay import (
    SOURCE_PATTERN,
    WITNESS,
    threshold_failure_reproduces,
)
from regexproof.harness.core import prop

PIN = "8666b6c6c52472b5535aa295f2df593918152cb1"
FAMILY = "AE-aidevops-predispatch-threshold-decimal"
PROPERTY_ID = "AE-aidevops-predispatch-threshold-leading-zero-fail-open"
MUTATION_ID = "AE-aidevops-predispatch-threshold-mutation-guard"
SITE = (
    f"marcusquinn/aidevops@{PIN}:"
    ".agents/scripts/pre-dispatch-validator-helper.sh:1879:column-51"
)

_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-16-autonomous-aidevops-predispatch-github-text-residual-20r2"
    / "contract-threshold-decimal.json"
)
CONTRACT = json.loads(_CONTRACT_PATH.read_text(encoding="utf-8"))
DIGIT = Range("0", "9")
SOURCE_THRESHOLD_RE = Concat(Re("threshold="), Plus(DIGIT))


@prop(
    PROPERTY_ID,
    "The pinned threshold token grammar admits 08; exact-helper replay shows "
    "Bash treats it as invalid octal and lets a below-threshold file proceed",
    expect_unsat=False,
    kind="counterexample_finder",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    pattern=SOURCE_PATTERN,
    pattern_flags="",
    contract=CONTRACT,
    ground_truth=threshold_failure_reproduces,
)
def aidevops_threshold_leading_zero_fails_open():
    threshold = String("threshold")
    return [
        InRe(Concat(StringVal("threshold="), threshold), SOURCE_THRESHOLD_RE),
        Length(threshold) == len(WITNESS),
        threshold == StringVal(WITNESS),
    ], threshold == StringVal(WITNESS)


@prop(
    MUTATION_ID,
    "MUTATION GUARD: weakening a canonical decimal threshold token to the "
    "source's digits-only form admits 08 and reproduces the fail-open path",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    pattern=SOURCE_PATTERN,
    pattern_flags="",
    ground_truth=threshold_failure_reproduces,
)
def aidevops_threshold_decimal_mutation_guard():
    threshold = String("threshold")
    weakened = Concat(Re("threshold="), Plus(DIGIT))
    return [
        InRe(Concat(StringVal("threshold="), threshold), weakened),
        Length(threshold) == len(WITNESS),
        threshold == StringVal(WITNESS),
    ], threshold == StringVal(WITNESS)


__all__ = [
    "CONTRACT",
    "FAMILY",
    "MUTATION_ID",
    "PIN",
    "PROPERTY_ID",
    "SITE",
    "SOURCE_PATTERN",
]

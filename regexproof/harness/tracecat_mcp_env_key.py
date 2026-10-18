"""Tracecat MCP stdio environment-key grammar counterexample and guard."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import And, Concat, InRe, Length, Not, Range, Re, Star, String, StringVal, Union

from regexproof.groundtruth.tracecat_mcp_env_key_replay import (
    accepted_terminal_lf_reproduces,
    terminal_lf_mutation_reproduces,
)
from regexproof.harness.core import prop

PIN = "c84d52528a489821f355fc63976fbc7783ae0ad5"
FAMILY = "TC-tracecat-mcp-env-key"
PROPERTY_ID = "TC-mcp-env-key-accepts-terminal-lf"
MUTATION_ID = "TC-mcp-env-key-dollar-anchor-mutation"
PATTERN = r"^[A-Za-z_][A-Za-z0-9_]*$"
SITE = (
    f"TracecatHQ/tracecat@{PIN}:"
    "tracecat/integrations/mcp_validation.py:178:re.match"
)

_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-15-autonomous-tracecat-mcp-env-key"
    / "contract.json"
)
CONTRACT = json.loads(_CONTRACT_PATH.read_text(encoding="utf-8"))

INITIAL = Union(Range("A", "Z"), Range("a", "z"), Re("_"))
TAIL = Union(INITIAL, Range("0", "9"))
DECLARED_NAME = Concat(INITIAL, Star(TAIL))
# Without MULTILINE, CPython `$` also matches immediately before one final LF.
PYTHON_DOLLAR_MATCH = Union(DECLARED_NAME, Concat(DECLARED_NAME, Re("\n")))
ASCII_STRING = Star(Range("\x00", "\x7f"))


@prop(
    PROPERTY_ID,
    "A string accepted as an MCP stdio env key must match Tracecat's complete "
    "declared ASCII name syntax; a terminal line feed is outside that grammar",
    expect_unsat=False,
    kind="counterexample_finder",
    family=FAMILY,
    input_domain="ascii",
    call_kind="match",
    pattern=PATTERN,
    pattern_flags="",
    contract=CONTRACT,
    ground_truth=accepted_terminal_lf_reproduces,
)
def mcp_env_key_terminal_lf_counterexample():
    key = String("key")
    return [
        InRe(key, ASCII_STRING),
        Length(key) >= 1,
        Length(key) <= 64,
    ], And(InRe(key, PYTHON_DOLLAR_MATCH), Not(InRe(key, DECLARED_NAME)))


@prop(
    MUTATION_ID,
    "MUTATION GUARD: replacing the strict terminator with Python `$` admits "
    "one terminal line feed and the pinned validator must reproduce it",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
    call_kind="match",
    pattern=PATTERN,
    pattern_flags="",
    ground_truth=terminal_lf_mutation_reproduces,
)
def mcp_env_key_dollar_anchor_mutation():
    key = String("key")
    return [
        key == StringVal("TRACE_TOKEN\n"),
        Length(key) <= 64,
        InRe(key, ASCII_STRING),
        InRe(key, PYTHON_DOLLAR_MATCH),
        Not(InRe(key, DECLARED_NAME)),
    ], And(InRe(key, PYTHON_DOLLAR_MATCH), Not(InRe(key, DECLARED_NAME)))


__all__ = [
    "CONTRACT",
    "FAMILY",
    "MUTATION_ID",
    "PATTERN",
    "PIN",
    "PROPERTY_ID",
    "SITE",
]

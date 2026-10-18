"""Shape-1 Tracecat MCP server-name path-separator exclusion proof."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import InRe, Length, Or, Range, Re, String, StringVal, Union

from regexproof.groundtruth.tracecat_server_name_replay import (
    PIN,
    SOURCE_PATTERN,
    server_name_slash_mutation_reproduces,
)
from regexproof.harness.core import prop

FAMILY = "TC-tracecat-server-name"
PROPERTY_ID = "TC-mcp-server-name-separators-excluded"
MUTATION_ID = "TC-mcp-server-name-slash-allowlist-mutation"
SITE = (
    f"TracecatHQ/tracecat@{PIN}:"
    "tracecat/integrations/mcp_validation.py:267:re.match"
)

_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-16-autonomous-tracecat-server-name"
    / "contract.json"
)
CONTRACT = json.loads(_CONTRACT_PATH.read_text(encoding="utf-8"))

ALLOWED_NAME_CHAR = Union(
    Range("A", "Z"),
    Range("a", "z"),
    Range("0", "9"),
    Re("_"),
    Re("-"),
)
WEAKENED_NAME_CHAR = Union(ALLOWED_NAME_CHAR, Re("/"))
ASCII_CHAR = Range("\x00", "\x7f")


@prop(
    PROPERTY_ID,
    "The exact pinned MCP server-name validator's accepted alphabet excludes "
    "both slash and backslash characters",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="ascii",
    call_kind="match",
    pattern=SOURCE_PATTERN,
    pattern_flags="",
    contract=CONTRACT,
)
def mcp_server_name_excludes_path_separators():
    character = String("name_char")
    path_separator = Or(
        character == StringVal("/"),
        character == StringVal("\\"),
    )
    return [
        Length(character) == 1,
        InRe(character, ASCII_CHAR),
        InRe(character, ALLOWED_NAME_CHAR),
    ], path_separator


@prop(
    MUTATION_ID,
    "MUTATION GUARD: allowing slash in the exact pinned server-name regex "
    "must accept `/` through validate_mcp_command_config",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
    call_kind="match",
    pattern=SOURCE_PATTERN,
    pattern_flags="",
    ground_truth=server_name_slash_mutation_reproduces,
)
def mcp_server_name_slash_allowlist_mutation():
    character = String("name_char")
    return [
        Length(character) == 1,
        character == StringVal("/"),
        InRe(character, WEAKENED_NAME_CHAR),
    ], character == StringVal("/")


__all__ = [
    "CONTRACT",
    "FAMILY",
    "MUTATION_ID",
    "PROPERTY_ID",
    "SITE",
    "SOURCE_PATTERN",
]

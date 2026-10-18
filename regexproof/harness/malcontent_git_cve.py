"""Byte-class proof and mutation guard for malcontent's Git CVE rule."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import And, InRe, Length, String, StringVal

from regexproof.compiler import compile_pattern
from regexproof.groundtruth.malcontent_replay import mutation_reproduces
from regexproof.harness.core import prop

PIN = "ea3e83e24676a1678a9522141da29b636c9451ab"
FAMILY = "MC-malcontent-git-cve48384-crlf"
SITE = (
    f"chainguard-dev/malcontent@{PIN}:"
    "rules/impact/exploit/cve-2025-48384.yara:22:path_embedded_cr"
)
SOURCE_PATTERN = (
    r"[\n\x00][ \t]*path[ \t]*=[ \t]*\"?[^\r\n]*\r[^\n]"
)
_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-15-autonomous-malcontent-git-cr-20r2"
    / "contract.json"
)
CONTRACT = json.loads(_CONTRACT_PATH.read_text(encoding="utf-8"))


def _terminal_class_rejects_lf():
    byte = String("byte_after_carriage_return")
    compiled = compile_pattern(
        r"^[^\n]$",
        dialect="yara",
        call_kind="fullmatch",
        domain="ascii",
    )
    if compiled.mirror is None:
        raise RuntimeError(
            f"pinned terminal class is not encodable: {compiled.unencodable_reason}"
        )
    return [Length(byte) == 1], And(
        InRe(byte, compiled.mirror), byte == StringVal("\n")
    )


def _mutated_terminal_class_admits_lf():
    byte = String("byte_after_carriage_return")
    compiled = compile_pattern(
        r"^[\r\n]$",
        dialect="yara",
        call_kind="fullmatch",
        domain="ascii",
    )
    if compiled.mirror is None:
        raise RuntimeError(
            f"mutated terminal class is not encodable: {compiled.unencodable_reason}"
        )
    return [Length(byte) == 1], And(
        InRe(byte, compiled.mirror), byte == StringVal("\n")
    )


def _mutated_full_rule_flags_crlf(witness: dict) -> bool:
    return mutation_reproduces(witness.get("byte_after_carriage_return", ""))


@prop(
    "MC-malcontent-cve48384-embedded-cr-excludes-lf",
    "The terminal [^\\n] byte class in the pinned $path_embedded_cr branch "
    "cannot consume LF after its required carriage return",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="ascii",
    call_kind="fullmatch",
    pattern=r"^[^\n]$",
    pattern_flags="",
    contract=CONTRACT,
)
def malcontent_path_embedded_cr_terminal_class_excludes_lf():
    """Prove the source branch's terminal class, not the whole YARA rule."""
    return _terminal_class_rejects_lf()


@prop(
    "MC-malcontent-cve48384-mutated-embedded-cr-allows-lf",
    "MUTATION GUARD: admitting LF after the required CR must make the exact "
    "pinned full rule flag an ordinary CRLF .gitmodules file",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
    call_kind="fullmatch",
    pattern=r"^[\r\n]$",
    pattern_flags="",
    ground_truth=_mutated_full_rule_flags_crlf,
)
def malcontent_mutated_embedded_cr_allows_lf():
    """SAT means LF enters the weakened class; the callback mutates YARA-X."""
    return _mutated_terminal_class_admits_lf()


__all__ = ["CONTRACT", "FAMILY", "PIN", "SITE", "SOURCE_PATTERN"]

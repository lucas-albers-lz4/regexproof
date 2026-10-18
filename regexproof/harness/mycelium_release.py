"""Mycelium release checksum-preflight contract and mutation guard."""

from __future__ import annotations

import json
from pathlib import Path

from z3 import BoolVal, Concat, InRe, Length, Loop, Plus, Range, Re, Star, String, Union

from regexproof.groundtruth.mycelium_release_replay import (
    PATTERN,
    PIN_20R2,
    mutation_reproduces,
)
from regexproof.harness.core import prop

PIN = "4b53dc7629ca3bc88bf5467db481ad2af7130711"
FAMILY = "MY-mycelium-release-integrity"
SITE = (
    f"mycelium0/mycelium@{PIN}:"
    "scripts/verify-release.sh:60:SHA256SUMS preflight"
)
_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-15-autonomous-mycelium-script-slice"
    / "contract.json"
)
CONTRACT = json.loads(_CONTRACT_PATH.read_text(encoding="utf-8"))
SITE_20R2 = (
    f"mycelium0/mycelium@{PIN_20R2}:"
    "scripts/verify-release.sh:60:sums_n"
)
_CONTRACT_20R2_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-15-autonomous-mycelium-20r2-slice"
    / "contract.json"
)
CONTRACT_20R2 = json.loads(_CONTRACT_20R2_PATH.read_text(encoding="utf-8"))

HEX_CHAR = Union(Range("0", "9"), Range("A", "F"), Range("a", "f"))
POSIX_SPACE = Union(Re(" "), Re("\t"), Re("\v"), Re("\f"), Re("\r"))
# The grep pattern requires one non-whitespace filename character. This
# explicit ASCII class mirrors [^[:space:]] for the declared text-file domain.
NONSPACE = Union(
    Range("\x01", "\x08"),
    Range("\x0e", "\x1f"),
    Range("!", "~"),
    Re("\x7f"),
)
LINE_CHAR = Union(Range("\x01", "\t"), Range("\x0b", "\x7f"))
OPTIONAL_BINARY_MARKER = Union(Re(""), Re("*"))
PREFLIGHT_RE = Concat(
    Loop(HEX_CHAR, 64, 64),
    Plus(POSIX_SPACE),
    OPTIONAL_BINARY_MARKER,
    NONSPACE,
    Star(LINE_CHAR),
)
WEAKENED_PREFLIGHT_RE = Concat(
    Loop(HEX_CHAR, 0, 64),
    Plus(POSIX_SPACE),
    OPTIONAL_BINARY_MARKER,
    NONSPACE,
    Star(LINE_CHAR),
)


def _short_sha256_line_is_rejected(witness: dict) -> bool:
    line = witness.get("line")
    if not isinstance(line, str) or len(line) >= 64:
        return False
    return mutation_reproduces(line)


def _short_sha256_line_is_rejected_20r2(witness: dict) -> bool:
    line = witness.get("line")
    if not isinstance(line, str) or len(line) >= 64:
        return False
    return mutation_reproduces(line, pin=PIN_20R2)


@prop(
    "MY-mycelium-release-preflight-requires-64-hex",
    "A single ASCII SHA256SUMS line shorter than 64 characters cannot pass "
    "the pinned verifier's checksum-record preflight",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    pattern=PATTERN,
    pattern_flags="",
    contract=CONTRACT,
)
def release_preflight_rejects_short_checksum_line():
    line = String("line")
    return [Length(line) <= 63], InRe(line, PREFLIGHT_RE)


@prop(
    "MY-mycelium-release-preflight-mutated-empty-hash",
    "MUTATION GUARD: making the 64-hex hash optional must allow a short "
    "checksum-free response through the actual pinned verifier",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
    ground_truth=_short_sha256_line_is_rejected,
)
def mutated_release_preflight_accepts_short_line():
    line = String("line")
    return [Length(line) <= 63, InRe(line, WEAKENED_PREFLIGHT_RE)], BoolVal(True)


@prop(
    "MY-mycelium-20r2-release-preflight-requires-64-hex",
    "At the frozen 20-r2 pin, a single ASCII SHA256SUMS line shorter than 64 "
    "characters cannot pass the pinned verifier's checksum-record preflight",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    pattern=PATTERN,
    pattern_flags="",
    contract=CONTRACT_20R2,
)
def release_preflight_rejects_short_checksum_line_20r2():
    line = String("line")
    return [Length(line) <= 63], InRe(line, PREFLIGHT_RE)


@prop(
    "MY-mycelium-20r2-release-preflight-mutated-empty-hash",
    "MUTATION GUARD: at the frozen 20-r2 pin, making the 64-hex hash optional "
    "must allow a short checksum-free response through the actual verifier",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
    ground_truth=_short_sha256_line_is_rejected_20r2,
)
def mutated_release_preflight_accepts_short_line_20r2():
    line = String("line")
    return [Length(line) <= 63, InRe(line, WEAKENED_PREFLIGHT_RE)], BoolVal(True)

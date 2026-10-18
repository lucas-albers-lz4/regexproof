"""Aidevops Node secret-read extension contract and mutation guard."""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path

from z3 import AllChar, Concat, InRe, Not, Or, Re, Star, String, StringVal, Union

from regexproof.groundtruth.aidevops_secret_read_replay import (
    PIN,
    SOURCE_PATTERN,
    SOURCE_BASENAME_PATTERN,
    mutation_reproduces,
    mutation_reproduces_secret_basename,
)
from regexproof.compiler import compile_pattern as compile_regex
from regexproof.harness.core import prop

FAMILY = "AE-aidevops-secret-read-extension"
SITE = (
    f"marcusquinn/aidevops@{PIN}:"
    ".agents/plugins/opencode-aidevops/quality-hooks-secret-read.mjs:8:28"
)
_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-15-autonomous-aidevops-node-secret-boundary"
    / "contract.json"
)
CONTRACT = json.loads(_CONTRACT_PATH.read_text(encoding="utf-8"))

EXTENSIONS = ("pem", "key", "p12", "pfx", "kdbx", "age", "asc", "gpg")
ANY_CHAR = AllChar(Re("").sort())


def _ci_literal(value: str):
    pieces = []
    for character in value:
        if character.isalpha():
            pieces.append(Union(Re(character.lower()), Re(character.upper())))
        else:
            pieces.append(Re(character))
    return Concat(*pieces)


EXTENSION_LANGUAGE = Union(
    *[Concat(Re("."), _ci_literal(extension)) for extension in EXTENSIONS]
)
SOURCE_SEARCH_LANGUAGE = Concat(Star(ANY_CHAR), EXTENSION_LANGUAGE)


def _case_variants(extension: str) -> tuple[str, ...]:
    positions = [index for index, char in enumerate(extension) if char.isalpha()]
    variants = []
    for bits in product((False, True), repeat=len(positions)):
        chars = list(extension)
        for index, uppercase in zip(positions, bits, strict=True):
            chars[index] = chars[index].upper() if uppercase else chars[index].lower()
        variants.append("." + "".join(chars))
    return tuple(variants)


CASE_VARIANTS = tuple(
    variant for extension in EXTENSIONS for variant in _case_variants(extension)
)
WEAKENED_SEARCH_LANGUAGE = Union(
    *[
        Concat(Star(ANY_CHAR), Re("."), _ci_literal(extension))
        for extension in EXTENSIONS
        if extension != "pem"
    ]
)


def _mutated_pem_extension_reaches_read(witness: dict) -> bool:
    basename = witness.get("basename", "")
    return isinstance(basename, str) and mutation_reproduces(basename)


@prop(
    "AE-aidevops-secret-read-extension-coverage",
    "Every ASCII basename ending in a declared private-key extension is matched "
    "by the pinned case-insensitive secret-extension rule before a read tool runs",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="ascii",
    call_kind="search",
    contract=CONTRACT,
)
def aidevops_secret_read_extension_coverage():
    suffix = String("declared_suffix")
    return [
        Or(*[suffix == StringVal(value) for value in CASE_VARIANTS]),
    ], Not(InRe(suffix, SOURCE_SEARCH_LANGUAGE))


@prop(
    "AE-aidevops-secret-read-mutated-pem-reaches-read",
    "MUTATION GUARD: removing the .pem alternative must admit a private-key "
    "basename that the real pinned pre-read hook then fails to block",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
    ground_truth=_mutated_pem_extension_reaches_read,
)
def aidevops_mutated_secret_read_pem_reaches_read():
    basename = String("basename")
    return [basename == StringVal("proof.pem")], Not(
        InRe(basename, WEAKENED_SEARCH_LANGUAGE)
    )


__all__ = ["CONTRACT", "EXTENSIONS", "FAMILY", "PIN", "SITE", "SOURCE_PATTERN"]


BASENAME_FAMILY = "AE-aidevops-secret-read-basename"
BASENAME_SITE = (
    f"marcusquinn/aidevops@{PIN}:"
    ".agents/plugins/opencode-aidevops/quality-hooks-secret-read.mjs:7:SECRET_BASENAME_RE"
)
_BASENAME_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "properties"
    / "calibration"
    / "2026-10-15-autonomous-aidevops-node-secret-boundary"
    / "contract-basename.json"
)
BASENAME_CONTRACT = json.loads(_BASENAME_CONTRACT_PATH.read_text(encoding="utf-8"))
_SOURCE_COMPILE = compile_regex(SOURCE_BASENAME_PATTERN, "i", "ecma", "search")
if not _SOURCE_COMPILE.encodable or not _SOURCE_COMPILE.meta.get("mirror_exact", True):
    raise RuntimeError(
        "pinned Aidevops secret-basename source rule is not exactly encodable"
    )
SOURCE_BASENAME_LANGUAGE = _SOURCE_COMPILE.mirror
_WEAKENED_COMPILE = compile_regex(
    SOURCE_BASENAME_PATTERN.removesuffix("|.*secret.*)$") + ")$",
    "i",
    "ecma",
    "search",
)
if not _WEAKENED_COMPILE.encodable or not _WEAKENED_COMPILE.meta.get("mirror_exact", True):
    raise RuntimeError("weakened Aidevops basename rule is not exactly encodable")
WEAKENED_BASENAME_LANGUAGE = _WEAKENED_COMPILE.mirror


def _case_variants(value: str) -> tuple[str, ...]:
    positions = [index for index, char in enumerate(value) if char.isalpha()]
    return tuple(
        "".join(
            char.upper() if char.isalpha() and bits[position] else char.lower()
            if char.isalpha() else char
            for position, char in enumerate(value)
        )
        for bits in product((False, True), repeat=len(positions))
    )


SECRET_BASENAME_VARIANTS = _case_variants("secret")


def _mutated_secret_basename_reaches_read(witness: dict) -> bool:
    basename = witness.get("basename", "")
    return (
        isinstance(basename, str)
        and mutation_reproduces_secret_basename(basename)
    )


@prop(
    "AE-aidevops-secret-read-basename-coverage",
    "Every ASCII case variant of the declared secret basename matches the pinned "
    "pre-read basename rule",
    expect_unsat=True,
    kind="property",
    family=BASENAME_FAMILY,
    input_domain="ascii",
    call_kind="search",
    contract=BASENAME_CONTRACT,
)
def aidevops_secret_read_basename_coverage():
    basename = String("declared_secret_basename")
    return [
        Or(*[basename == StringVal(value) for value in SECRET_BASENAME_VARIANTS]),
    ], Not(InRe(basename, SOURCE_BASENAME_LANGUAGE))


@prop(
    "AE-aidevops-secret-read-mutated-basename-reaches-read",
    "MUTATION GUARD: removing the secret-substring alternative must admit the "
    "basename `secret` through the real pinned pre-read helper",
    expect_unsat=False,
    kind="mutation_guard",
    family=BASENAME_FAMILY,
    input_domain="ascii",
    ground_truth=_mutated_secret_basename_reaches_read,
)
def aidevops_mutated_secret_basename_reaches_read():
    basename = String("basename")
    return [basename == StringVal("secret")], Not(
        InRe(basename, WEAKENED_BASENAME_LANGUAGE)
    )

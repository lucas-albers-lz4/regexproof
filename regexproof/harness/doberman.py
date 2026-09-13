"""Doberman-Core Python command-boundary conversion properties.

This first wave keeps only two questions that are regular-language properties
under the pinned ``fu351/Doberman-Core`` source.  The substitution, word-boundary,
and lookaround sites remain behavioral/backend work and are deliberately not
mirrored here.
"""

from __future__ import annotations

import re

from z3 import (
    And,
    Concat,
    Contains,
    InRe,
    Length,
    Not,
    Or,
    Range,
    Re,
    Star,
    String,
    StringVal,
    Union,
)

from regexproof.harness.core import prop

FAMILY = "PY-doberman-command-exec"
PIN = "53ae43c5298a2426c6696147fdd75e2a4aef10e2"
SITE_ROOT = (
    "fu351/Doberman-Core@"
    + PIN
    + ":src/doberman/engine/rules/commands.py:266:_WINDOWS_ROOT_RE"
)
SITE_WIPE = (
    "fu351/Doberman-Core@"
    + PIN
    + ":src/doberman/engine/rules/commands.py:434:_DISK_WIPE"
)

ASCII_WORD = Union(
    Range("A", "Z"),
    Range("a", "z"),
    Range("0", "9"),
    Re("_"),
)
ASCII_WORD_PLUS = Concat(ASCII_WORD, Star(ASCII_WORD))
DRIVE = Union(Range("A", "Z"), Range("a", "z"))
ROOT_SEPARATOR = Union(Re(""), Re("/"), Re("\\"))
ROOT_WILDCARD = Union(Re(""), Re("*"))
WINDOWS_ROOT_CORE_RE = Concat(DRIVE, Re(":"), ROOT_SEPARATOR, ROOT_WILDCARD)

# Python's ``$`` also matches immediately before one final newline.  Both
# source regexes are used with ``re.match`` and therefore admit that newline
# even though it is not consumed by the visible pattern.  Keep the source
# matcher and its mirror explicit so the property tests the actual boundary
# semantics rather than a hand-written character class.
FINAL_NEWLINE = Union(Re(""), Re("\n"))
WINDOWS_ROOT_RE = Concat(WINDOWS_ROOT_CORE_RE, FINAL_NEWLINE)


def _ci(text: str):
    """Mirror ``re.IGNORECASE`` over the declared ASCII domain."""
    return Concat(
        *[Union(Re(char.lower()), Re(char.upper())) for char in text]
    )


DISK_WIPE_CORE_RE = Union(
    Concat(
        _ci("mkfs"),
        Union(Re(""), Concat(Re("."), ASCII_WORD_PLUS)),
    ),
    _ci("shred"),
    _ci("wipefs"),
    _ci("format-volume"),
    _ci("clear-disk"),
    _ci("format"),
)
DISK_WIPE_RE = Concat(DISK_WIPE_CORE_RE, FINAL_NEWLINE)

_WINDOWS_ROOT_SOURCE = re.compile(r"^[A-Za-z]:[/\\]?(\*)?$")
_DISK_WIPE_SOURCE = re.compile(
    r"^(?:mkfs(?:\.\w+)?|shred|wipefs|format-volume|clear-disk|format)$",
    re.IGNORECASE,
)


def _windows_root_ground_truth(witness):
    value = witness.get("s", "")
    return bool(_WINDOWS_ROOT_SOURCE.match(value)) and value.endswith("\n")


def _disk_wipe_ground_truth(witness):
    value = witness.get("s", "")
    return bool(_DISK_WIPE_SOURCE.match(value)) and value.endswith("\n")


def _windows_root_whitelist(s):
    values = []
    for drive in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
        for separator in ("", "/", "\\"):
            for wildcard in ("", "*"):
                values.append(s == StringVal(f"{drive}:{separator}{wildcard}"))
    return Or(*values)


@prop(
    "PY-doberman-windows-root-token",
    "exists an ASCII Windows root-target argument with a terminal newline "
    "that Python re.match accepts before the closing $",
    expect_unsat=False,
    ground_truth=_windows_root_ground_truth,
    kind="counterexample_finder",
    family=FAMILY,
    input_domain="ascii",
    call_kind="match",
    contract={
        "schema_version": "1",
        "site": SITE_ROOT,
        "guarantee": (
            "the root-target boundary does not classify an otherwise exact "
            "drive root when an unconsumed terminal newline is present"
        ),
        "input_source": "untrusted agent command argument passed to Windows delete classification",
        "trust": "untrusted-input",
        "declared_domain": (
            "ASCII argument after the product's surrounding strip() and quote "
            "removal, including one terminal LF; length 2..4; Python re.match "
            "semantics at the pinned source"
        ),
        "provenance": "human",
    },
)
def py_doberman_windows_root_token():
    s = String("s")
    return [
        InRe(s, WINDOWS_ROOT_RE),
        Length(s) >= 2,
        Length(s) <= 4,
    ], And(Contains(s, StringVal("\n")), Not(_windows_root_whitelist(s)))


@prop(
    "PY-doberman-disk-wipe-token",
    "exists an ASCII disk-wipe token with a terminal newline that Python "
    "re.match accepts before the closing $",
    expect_unsat=False,
    ground_truth=_disk_wipe_ground_truth,
    kind="counterexample_finder",
    family=FAMILY,
    input_domain="ascii",
    call_kind="match",
    contract={
        "schema_version": "1",
        "site": SITE_WIPE,
        "guarantee": (
            "the disk-wipe command boundary does not accept an unconsumed "
            "terminal newline as part of a command token"
        ),
        "input_source": "untrusted agent command token after shlex segment parsing",
        "trust": "untrusted-input",
        "declared_domain": (
            "ASCII command token including one terminal LF, Python "
            "re.IGNORECASE, full anchored match; mkfs suffix is ASCII "
            "[A-Za-z0-9_]+; length 1..64"
        ),
        "provenance": "human",
    },
)
def py_doberman_disk_wipe_token():
    s = String("s")
    return [InRe(s, DISK_WIPE_RE), Length(s) >= 1, Length(s) <= 64], Contains(
        s, StringVal("\n")
    )


@prop(
    "PY-doberman-mutated-windows-root-token",
    "MUTATION GUARD: widening the Windows-root matcher to admit ';' must flip "
    "PY-doberman-windows-root-token from UNSAT to SAT",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
)
def py_doberman_mutated_windows_root_token():
    s = String("s")
    weakened = Union(
        WINDOWS_ROOT_RE,
        Concat(WINDOWS_ROOT_CORE_RE, Re(";"), FINAL_NEWLINE),
    )
    return [InRe(s, weakened)], Contains(s, StringVal(";"))


@prop(
    "PY-doberman-mutated-disk-wipe-token",
    "MUTATION GUARD: widening the anchored disk-wipe matcher to admit ';' must "
    "flip PY-doberman-disk-wipe-token from UNSAT to SAT",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
)
def py_doberman_mutated_disk_wipe_token():
    s = String("s")
    weakened = Union(
        DISK_WIPE_RE,
        Concat(DISK_WIPE_CORE_RE, Re(";"), FINAL_NEWLINE),
    )
    return [InRe(s, weakened)], Contains(s, StringVal(";"))

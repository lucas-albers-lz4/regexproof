"""Doberman-Core Python command-boundary conversion properties.

This first wave keeps only two questions that are regular-language properties
under the pinned ``fu351/Doberman-Core`` source.  The substitution, word-boundary,
and lookaround sites remain behavioral/backend work and are deliberately not
mirrored here.
"""

from __future__ import annotations

from z3 import (
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
DISK_WIPE_CHAR = Union(
    Range("A", "Z"),
    Range("a", "z"),
    Range("0", "9"),
    Re("."),
    Re("-"),
    Re("_"),
)
DRIVE = Union(Range("A", "Z"), Range("a", "z"))
ROOT_SEPARATOR = Union(Re(""), Re("/"), Re("\\"))
ROOT_WILDCARD = Union(Re(""), Re("*"))
WINDOWS_ROOT_RE = Concat(DRIVE, Re(":"), ROOT_SEPARATOR, ROOT_WILDCARD)


def _ci(text: str):
    """Mirror ``re.IGNORECASE`` over the declared ASCII domain."""
    return Concat(
        *[Union(Re(char.lower()), Re(char.upper())) for char in text]
    )


DISK_WIPE_RE = Union(
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


def _windows_root_whitelist(s):
    values = []
    for drive in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
        for separator in ("", "/", "\\"):
            for wildcard in ("", "*"):
                values.append(s == StringVal(f"{drive}:{separator}{wildcard}"))
    return Or(*values)


@prop(
    "PY-doberman-windows-root-token",
    "Windows root-target regex admits only its exact drive-root whitelist "
    "over the declared ASCII token domain",
    expect_unsat=True,
    family=FAMILY,
    input_domain="ascii",
    call_kind="match",
    contract={
        "schema_version": "1",
        "site": SITE_ROOT,
        "guarantee": (
            "a Windows root/home deletion target classified by _WINDOWS_ROOT_RE "
            "is exactly a drive root with an optional separator and wildcard; "
            "no extra path segment or shell operator reaches root-delete BLOCK"
        ),
        "input_source": "untrusted agent command argument passed to Windows delete classification",
        "trust": "untrusted-input",
        "declared_domain": (
            "ASCII token after the product's surrounding strip(); length 2..4; "
            "Python re.match semantics at the pinned source"
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
    ], Not(_windows_root_whitelist(s))


@prop(
    "PY-doberman-disk-wipe-token",
    "case-insensitive disk-wipe regex token alphabet contains no shell "
    "separator or whitespace",
    expect_unsat=True,
    family=FAMILY,
    input_domain="ascii",
    call_kind="match",
    contract={
        "schema_version": "1",
        "site": SITE_WIPE,
        "guarantee": (
            "the disk-wipe command-token alphabet reaching _segment_verdict "
            "contains no shell separator or whitespace; exact anchoring is "
            "checked separately against Python re"
        ),
        "input_source": "untrusted agent command token after shlex segment parsing",
        "trust": "untrusted-input",
        "declared_domain": (
            "ASCII command token, Python re.IGNORECASE, full anchored match; "
            "mkfs suffix is ASCII [A-Za-z0-9_]+"
        ),
        "provenance": "human",
    },
)
def py_doberman_disk_wipe_token():
    c = String("c")
    bad = Or(
        c == StringVal(";"),
        c == StringVal("|"),
        c == StringVal("&"),
        c == StringVal(" "),
        c == StringVal("\t"),
    )
    return [InRe(c, DISK_WIPE_CHAR), Length(c) == 1], bad


@prop(
    "PY-doberman-mutated-windows-root-token",
    "MUTATION GUARD: appending ';' to the Windows-root matcher must flip "
    "PY-doberman-windows-root-token from UNSAT to SAT",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
)
def py_doberman_mutated_windows_root_token():
    s = String("s")
    weakened = Concat(WINDOWS_ROOT_RE, Re(";"))
    return [InRe(s, weakened)], Contains(s, StringVal(";"))


@prop(
    "PY-doberman-mutated-disk-wipe-token",
    "MUTATION GUARD: appending ';' to the anchored disk-wipe matcher must "
    "flip PY-doberman-disk-wipe-token from UNSAT to SAT",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
)
def py_doberman_mutated_disk_wipe_token():
    c = String("c")
    weakened = Union(DISK_WIPE_CHAR, Re(";"))
    return [InRe(c, weakened), Length(c) == 1], c == StringVal(";")

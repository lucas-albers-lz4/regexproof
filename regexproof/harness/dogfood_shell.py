"""dogfood_shell conversion-wave properties (family ``DF-dogfood-shell``).

Wave 1 (shell normalize fixpoint): fwlive ``normalize_log_prefix()``
(``sed 's/[[:space:]:]*$//'``) idempotency + no-trailing-strip-class
fixpoint at ``openwrt-feed/luci-app-fwlive/root/usr/libexec/rpcd/fwlive:97``.
This is the known-true contract class from fwlive #250 (``normalize_log_prefix``
stripped ONE trailing colon per call, so ``zz::`` drifted across backends;
fixed by stripping all trailing ``[[:space:]:]``). Z3 F1–F4 verified
*membership*, never *idempotency* — this wave closes that gap.

Product engine is ``sed`` (BusyBox on device, GNU on host) running the exact
shipped script. The Z3 mirror strips the same class with the same greediness
inside the declared domain; differential fuzz (tests + CI checker) proves
mirror ≡ real ``sed`` on both engines.
Importing this module registers into ``REGISTRY``.
"""

from __future__ import annotations

from z3 import (
    And,
    If,
    Length,
    Or,
    String,
    StringVal,
    SubString,
    SuffixOf,
)

from regexproof.harness.core import prop

FAMILY = "DF-dogfood-shell"

SITE = (
    "openwrt-feed/luci-app-fwlive/root/usr/libexec/rpcd/fwlive"
    ":97:normalize_log_prefix"
)
SED_SCRIPT = "s/[[:space:]:]*$//"

# POSIX [[:space:]] on a single line (no LF: LF would split sed into per-line
# matches, so the contract covers single-line prefixes — exactly what the
# client's ``parseRuleHint()`` capture ``^([A-Za-z0-9_.-]+)`` can produce).
# Shell strings carry no NUL (TRAPS #3); NUL is outside the declared domain.
STRIP_CHARS = (" ", "\t", "\r", "\x0c", "\x0b", ":")

# Declared length bound. strip^MAXLEN fully normalizes any input of
# len <= MAXLEN (worst case: every char strips), so the bounded mirror is
# exact — not an under-approximation — inside the declared domain.
MAXLEN = 8


def normalize_mirror(s: str) -> str:
    """Python oracle of ``sed 's/[[:space:]:]*$//'`` on single-line input.

    Shared by the differential fuzz (tests + CI checker): mirror ≡ real sed
    is proved by execution, not by inspection.
    """
    return s.rstrip(" \t\r\x0c\x0b:")


def _strip_step(s, chars=STRIP_CHARS):
    last = SubString(s, Length(s) - 1, 1)
    cond = And(Length(s) >= 1, Or(*[last == StringVal(c) for c in chars]))
    return If(cond, SubString(s, 0, Length(s) - 1), s)


def _normalize(x, rounds=MAXLEN, chars=STRIP_CHARS):
    s = x
    for _ in range(rounds):
        s = _strip_step(s, chars)
    return s


def _ends_with_strip(s):
    # z3py SuffixOf(suffix, s): the candidate suffix comes FIRST.
    return Or(*[SuffixOf(StringVal(c), s) for c in STRIP_CHARS])


_CONTRACT_BASE = {
    "schema_version": "1",
    "site": SITE,
    "input_source": (
        "log prefix from nft ruleset / iptables LOG lines "
        "(untrusted config-derived; cross-backend consistent keys are "
        "load-bearing for rulesMap lookup)"
    ),
    "trust": "untrusted-input",
    "provenance": "human",
}


@prop(
    "DF-dogfood-shell-normalize-fixpoint",
    "normalize(x) carries no trailing strip-class char (ASCII single-line, "
    "len 0..8, no NUL/LF; sed s/[[:space:]:]*$//)",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="ascii",
    call_kind="substitution",
    contract={
        **_CONTRACT_BASE,
        "guarantee": (
            "normalized prefix has no trailing space, tab, CR, FF, VT, "
            "or colon (fixpoint of the strip)"
        ),
        "declared_domain": "ASCII single-line, len 0..8, no NUL/LF",
    },
)
def normalize_fixpoint():
    x = String("x")
    n = _normalize(x)
    return [Length(x) <= MAXLEN], _ends_with_strip(n)


@prop(
    "DF-dogfood-shell-normalize-idempotent",
    "normalize(normalize(x)) == normalize(x) (ASCII single-line, "
    "len 0..8, no NUL/LF; sed s/[[:space:]:]*$//)",
    expect_unsat=True,
    kind="property",
    family=FAMILY,
    input_domain="ascii",
    call_kind="substitution",
    contract={
        **_CONTRACT_BASE,
        "guarantee": "normalization is idempotent (the fwlive #250 drift class)",
        "declared_domain": "ASCII single-line, len 0..8, no NUL/LF",
    },
)
def normalize_idempotent():
    x = String("x")
    n = _normalize(x)
    return [Length(x) <= MAXLEN], _normalize(n) != n


@prop(
    "DF-dogfood-shell-normalize-mutated-colon",
    "weakened [[:space:]]* (colon dropped — the exact 2026-08 regression) "
    "MUST flip UNSAT->SAT",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
)
def normalize_mutated_colon():
    x = String("x")
    weak = [c for c in STRIP_CHARS if c != ":"]
    n = _normalize(x, chars=weak)
    return [Length(x) <= MAXLEN], SuffixOf(StringVal(":"), n)
@prop(
    "DF-dogfood-shell-normalize-mutated-once",
    "single-strip (?-like, one round only) MUST flip idempotency UNSAT->SAT "
    "(zz:: -> zz: witness)",
    expect_unsat=False,
    kind="mutation_guard",
    family=FAMILY,
    input_domain="ascii",
)
def normalize_mutated_once():
    x = String("x")
    n = _strip_step(x)
    return [Length(x) <= MAXLEN], _strip_step(n) != n

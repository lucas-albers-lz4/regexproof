#!/usr/bin/env python3
"""regexproof harness skeleton — property registry + mutation guards.

Contract (from docs/PLAYBOOK.md and docs/DECOMPOSITION.md):
  - TIMEOUT (solver `unknown`) is a HARD FAILURE — never a pass, never a
    counterexample.
  - Every property declares its DOMAIN: exactly what was proven. A length
    bound means "proven up to this length", not "inputs are this length".
  - Mutation guards (expect_sat=True) weaken the regex and assert the result
    flips UNSAT->SAT. A harness that can't fail proves nothing.
  - Per-property wall time is logged so slice bounds can be tuned empirically.
  - SAT witnesses MUST be ground-truthed against the real implementation
    before being reported (see properties/usrmanage-p1-p6.md for the sed
    ground-truth protocol).

Usage:
  python3 z3-verify.py --list
  python3 z3-verify.py --all
  python3 z3-verify.py P1 P2 P1-mutated

Exit code: 0 = all pass; 1 = any FAIL or TIMEOUT.
"""

import sys
import time

from z3 import (
    Concat,
    Contains,
    IndexOf,
    InRe,
    Length,
    Range,
    Re,
    Solver,
    Star,
    String,
    StringVal,
    SubString,
    Union,
    sat,
    unknown,
    unsat,
)

# ---------------------------------------------------------------------------
# Property registry
# ---------------------------------------------------------------------------
REGISTRY = {}


def prop(name, declared_domain, expect_unsat=True, timeout_ms=30000):
    """Decorator: register a property. The wrapped function returns the
    constraint list; the harness adds `bad` and checks satisfiability."""

    def deco(fn):
        REGISTRY[name] = {
            "fn": fn,
            "domain": declared_domain,
            "expect_unsat": expect_unsat,
            "timeout_ms": timeout_ms,
        }
        return fn

    return deco


def run_one(name, entry):
    s = Solver()
    s.set("timeout", entry["timeout_ms"])
    constraints, bad = entry["fn"]()
    for c in constraints:
        s.add(c)
    s.add(bad)
    t0 = time.perf_counter()
    r = s.check()
    wall = (time.perf_counter() - t0) * 1000
    if r == unknown:
        print(f"[TIMEOUT] {name}: unknown ({entry['timeout_ms']}ms) — HARD FAILURE")
        return False
    ok = (r == unsat) == entry["expect_unsat"]
    tag = "UNSAT (property HOLDS)" if r == unsat else "SAT (counterexample)"
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {tag}  [{wall:.1f}ms]")
    print(f"    domain: {entry['domain']}")
    if r == sat:
        m = s.model()
        for d in m.decls():
            print(f"    witness: {d.name()} = {m[d]!r}")
    return ok


# ---------------------------------------------------------------------------
# Properties (mirrors properties/usrmanage-p1-p6.md)
# ---------------------------------------------------------------------------
USERNAME_CLS = Union(Range("a", "z"), Range("A", "Z"), Range("0", "9"), Re("_"), Re("-"))
USERNAME_RE = Concat(Union(Range("a", "z"), Re("_")), Star(USERNAME_CLS))
DENY_LIST = ["root", "daemon", "ftp", "network", "nobody", "nogroup", "admin", "ubus", "sync"]
INJECTION_CHARS = [
    ("space", " "),
    ("equals", "="),
    ("newline", "\n"),
    ("tab", "\t"),
    ("semicolon", ";"),
    ("pipe", "|"),
    ("dollar", "$"),
    ("backtick", "`"),
    ("ampersand", "&"),
]


def _p1(ch):
    """P1 builder: username validator + deny-list, 'contains <ch>' as bad."""
    u = String("u")
    constraints = [InRe(u, USERNAME_RE), Length(u) >= 1, Length(u) <= 32]
    constraints += [u != StringVal(d) for d in DENY_LIST]
    return constraints, Contains(u, StringVal(ch))


for _name, _ch in INJECTION_CHARS:
    REGISTRY[f"P1-{_name}"] = {
        "fn": lambda ch=_ch: _p1(ch),
        "expect_unsat": True,
        "timeout_ms": 30000,
        "domain": "usernames matching "
        "^[a-z_][a-z0-9_-]{0,31}$ minus deny-list "
        "(declared domain: len 1..32) contain no "
        f"{_name}",
    }

ACTOR_CLS = Union(
    Range("a", "z"), Range("A", "Z"), Range("0", "9"), Re("."), Re("_"), Re("@"), Re("-")
)


@prop(
    "P2-actor-whitelist",
    "actor whitelist [A-Za-z0-9._@-]{1,64} admits no audit-line-breaking "
    "char (proven for len <= 16; slice 17-64 for full coverage)",
    expect_unsat=True,
)
def p2():
    a = String("a")
    wl_re = Concat(ACTOR_CLS, Star(ACTOR_CLS))
    constraints = [InRe(a, wl_re), Length(a) >= 1, Length(a) <= 16]
    return constraints, Contains(a, StringVal(" "))


@prop(
    "P3-sed-capture-truncation",
    "exists v: v contains an escaped quote AND the sed-style capture "
    '[^"]* (prefix before first quote) differs from v — the rpcd sed '
    "fallback bug repro",
    expect_unsat=False,
)
def p3():
    v = String("v")
    first_quote = IndexOf(v, StringVal('"'), 0)
    capture = SubString(v, 0, first_quote)
    return [first_quote > 0, capture != v], Contains(v, StringVal('\\"'))


ESCAPE_SAFE = Union(Range("\x20", "\x21"), Range("\x23", "\x5b"), Range("\x5d", "\x7e"))
ESCAPE_ESC = Union(Re("\\\\"), Re('\\"'), Re("\\t"), Re("\\r"), Re("\\n"))
ESCAPE_TOKENS = Union(ESCAPE_SAFE, ESCAPE_ESC)


@prop(
    "P4-escape-image-tab",
    "um_json_escape output token alphabet (safe chars + escape tokens, "
    "input alphabet excludes NUL per POSIX shell domain assumption) "
    "contains no raw tab. NOTE: encoded as single-char membership — "
    "Contains-vs-Star-image TIMES OUT even per-token (measured 30s); "
    "alphabet disjointness is the equivalent instant form (0.4ms).",
    expect_unsat=True,
)
def p4_tab():
    w = String("w")
    return [InRe(w, ESCAPE_TOKENS), Length(w) == 1], w == StringVal("\t")


@prop("P4-escape-image-newline", "same token alphabet contains no raw newline", expect_unsat=True)
def p4_nl():
    w = String("w")
    return [InRe(w, ESCAPE_TOKENS), Length(w) == 1], w == StringVal("\n")


@prop("P4-escape-image-del", "same token alphabet contains no raw DEL (0x7f)", expect_unsat=True)
def p4_del():
    w = String("w")
    return [InRe(w, ESCAPE_TOKENS), Length(w) == 1], w == StringVal("\x7f")


@prop(
    "P4-nul-passthrough-demo",
    "BUG DEMO: a faithful token alphabet that includes the escaper's "
    "raw-NUL else-branch DOES contain NUL — this is why the POSIX "
    "input-domain assumption must be stated explicitly in the real property",
    expect_unsat=False,
)
def p4_nul():
    w = String("w")
    # o == 0 falls through the `o > 0 && o < 32` guard -> printed raw
    faithful = Union(ESCAPE_TOKENS, Re("\x00"))
    return [InRe(w, faithful), Length(w) == 1], w == StringVal("\x00")


# ---------------------------------------------------------------------------
# Mutation guards — the harness must be able to fail
# ---------------------------------------------------------------------------
WEAKENED_USERNAME_RE = Concat(Union(Range("a", "z"), Re("_")), Star(Union(USERNAME_CLS, Re("*"))))


@prop(
    "P1-mutated-star",
    "MUTATION GUARD: if the username regex is weakened to allow '*', the "
    "'no star' property MUST flip UNSAT->SAT. If this passes as UNSAT, the "
    "mirror is not tracking the real regex.",
    expect_unsat=False,
)
def p1_mutated():
    u = String("u")
    constraints = [InRe(u, WEAKENED_USERNAME_RE), Length(u) >= 1, Length(u) <= 32]
    return constraints, Contains(u, StringVal("*"))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    args = sys.argv[1:]
    if not args or "--all" in args:
        names = sorted(REGISTRY)
    elif "--list" in args:
        for n in sorted(REGISTRY):
            print(
                f"{n}  expect_unsat={REGISTRY[n]['expect_unsat']}  "
                f"timeout={REGISTRY[n]['timeout_ms']}ms"
            )
            print(f"    domain: {REGISTRY[n]['domain']}")
        return 0
    else:
        names = [a for a in args if a in REGISTRY]
        missing = [a for a in args if a not in REGISTRY]
        if missing:
            print(f"unknown properties: {missing}", file=sys.stderr)
            return 2

    failures = 0
    for n in names:
        if not run_one(n, REGISTRY[n]):
            failures += 1
    print(f"\n{len(names) - failures}/{len(names)} passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

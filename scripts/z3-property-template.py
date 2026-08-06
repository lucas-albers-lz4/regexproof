#!/usr/bin/env python3
"""Z3 regex-sanitation property starter — the 4 canonical shapes.

Part of regexproof. Validated with z3-solver==5.0.0 (2026-08, usrmanage
spike). Copy and adapt:
  Shape 1: alphabet-disjointness containment (instant, no length bound)
  Shape 2: whitelist membership exclusion (length-bounded sanity)
  Shape 3: counterexample finder via string ops (NOT regex — Complement gotcha)
  Shape 4: per-token escape-image check (monolithic image-regex times out)

Run: python3 scripts/z3-property-template.py
Read docs/TRAPS.md before changing anything.
"""

from z3 import *


def check(name, constraints, bad, expect_unsat=True, timeout_ms=30000):
    """UNSAT = property holds; SAT = counterexample (with model); unknown = timeout (hard fail)."""
    s = Solver()
    s.set("timeout", timeout_ms)
    for c in constraints:
        s.add(c)
    s.add(bad)
    r = s.check()
    if r == unknown:
        print(f"[TIMEOUT] {name}: unknown (solver timeout {timeout_ms}ms)")
        return None
    ok = (r == unsat) == expect_unsat
    tag = "UNSAT (property HOLDS)" if r == unsat else "SAT (counterexample)"
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {tag}")
    if r == sat:
        m = s.model()
        for d in m.decls():
            print(f"      {d.name()} = {m[d]!r}")
    return r


# ---------- Shape 1: alphabet-disjointness containment ----------
# "Accepted strings contain no injection char" = forbidden char not in alphabet.
# Instant and length-independent — do NOT length-slice containment properties.
alphabet = Union(
    Range("a", "z"), Range("A", "Z"), Range("0", "9"), Re("."), Re("_"), Re("@"), Re("-")
)
s = String("s")
for badchar, nm in [
    (" ", "space"),
    ("=", "equals"),
    ("\n", "newline"),
    (";", "semicolon"),
    ("|", "pipe"),
    ("$", "dollar"),
]:
    check(f"alphabet excludes {nm}", [InRe(s, alphabet), Length(s) == 1], s == StringVal(badchar))

# ---------- Shape 2: whitelist membership exclusion ----------
# Sanity: a whitelisted string (1..16 chars over the alphabet) cannot contain space.
wl_re = Concat(alphabet, Star(alphabet))
a = String("a")
wl_ok = [InRe(a, wl_re), Length(a) >= 1, Length(a) <= 16]
check("whitelisted string contains no space", wl_ok, Contains(a, StringVal(" ")))

# ---------- Shape 3: counterexample finder via string ops ----------
# Model a sed-style capture `[^"]*` as prefix-before-first-quote.
# Use IndexOf/SubString, NOT Complement(Re('"')) — language complement is NOT
# char-class negation (the string a" is "in the complement" of " because a" != ").
v = String("v")
first_quote = IndexOf(v, StringVal('"'), 0)
capture = SubString(v, 0, first_quote)
# expect SAT: value containing an escaped quote gets truncated by [^"]*
check(
    "escaped-quote value: sed capture differs from true value (bug repro)",
    [first_quote > 0],
    Contains(v, StringVal('\\"')),
    expect_unsat=False,
)

# ---------- Shape 4: per-token escape-image check ----------
# Prove an escaper's output language has no raw control chars.
# MEASURED (5.0.0): `Contains(w, bad)` against `InRe(w, Star(Union(safe, esc)))`
# TIMES OUT at 30s EVEN per-token. The equivalent, instant form is
# single-char membership over the TOKEN ALPHABET — for a Star-language,
# containment reduces to alphabet disjointness (same property, 0.4ms).
w = String("w")
safe = Union(Range("\x20", "\x21"), Range("\x23", "\x5b"), Range("\x5d", "\x7e"))
esc = Union(Re("\\\\"), Re('\\"'), Re("\\t"), Re("\\r"), Re("\\n"))
tokens = Union(safe, esc)  # add Re('\\uXXXX') tokens as needed
for ch, nm in [("\t", "tab"), ("\n", "newline"), ("\x7f", "DEL")]:
    check(f"escaped output has no raw {nm}", [InRe(w, tokens), Length(w) == 1], w == StringVal(ch))

# NUL demo: a FAITHFUL image (escaper's else-branch passes 0x00 raw) DOES
# emit NUL — SAT below. The real property must state the input-domain
# assumption (POSIX shell strings cannot contain NUL) and exclude NUL from
# the input alphabet, or "no raw C0 controls" is false as stated.
check(
    "nul-passthrough demo (why the domain assumption is needed)",
    [InRe(w, Union(tokens, Re("\x00"))), Length(w) == 1],
    w == StringVal("\x00"),
    expect_unsat=False,
)

print("done")

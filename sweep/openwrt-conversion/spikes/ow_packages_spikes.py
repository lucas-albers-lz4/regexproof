#!/usr/bin/env python3
"""Throwaway spikes for OW-packages contracts (not product)."""

from z3 import (
    Concat,
    Contains,
    If,
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
    unsat,
)

LABEL = Union(Range("a", "z"), Range("A", "Z"), Range("0", "9"), Re("_"), Re("-"))
EXP = Union(Range("0", "9"), Re("m"), Re("s"), Re("h"), Re("d"), Re("w"))
HEX = Union(Range("0", "9"), Range("a", "f"), Range("A", "F"))


def _check(name, constraints, bad, expect):
    s = Solver()
    s.set("timeout", 5000)
    for c in constraints:
        s.add(c)
    s.add(bad)
    r = s.check()
    ok = (r == unsat) if expect == "unsat" else (r == sat)
    print(f"{name}: {r} ok={ok}")
    if not ok:
        raise SystemExit(1)


def main() -> int:
    c = String("c")
    _check("hostname-no-semi", [InRe(c, LABEL), Length(c) == 1], c == StringVal(";"), "unsat")
    _check("hostname-no-space", [InRe(c, LABEL), Length(c) == 1], c == StringVal(" "), "unsat")
    _check("banip-expiry-no-semi", [InRe(c, EXP), Length(c) == 1], c == StringVal(";"), "unsat")
    v = String("v")
    fq = IndexOf(v, StringVal('"'), 0)
    cap = SubString(v, 0, fq)
    _check("transip-truncation", [fq > 0, cap != v], Contains(v, StringVal('"')), "sat")
    w = String("w")
    hexre = Concat(HEX, Star(HEX))
    q = IndexOf(w, StringVal("'"), 0)
    wcap = If(q < 0, w, SubString(w, 0, q))
    _check(
        "wan-mark-hex",
        [InRe(w, hexre), Length(w) >= 1, Length(w) <= 8],
        wcap != w,
        "unsat",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

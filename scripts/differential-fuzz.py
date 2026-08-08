#!/usr/bin/env python3
"""Differential fuzz: prove mirror == real implementation on random inputs.

Part of regexproof. The Z3 model is a *mirror* of the real code. Mutation
guards (z3-verify.py) prove the mirror is SENSITIVE; this script proves the
mirror AGREES with the real implementation — random inputs in, both sides
must accept/reject identically.

  mirror: a Z3 regex expression (built with the z3py API, exactly like
          z3-verify.py builds its properties) — evaluated in a namespace
          that exposes the z3py names (Concat, Union, Range, Re, Star,
          Plus, Loop, Complement). NOTE: no Opt — z3py's Opt is the
          optimizer class, not regex optional; "?" is Union(r, Re("")).
  real:   argv program that reads a string on stdin and exits 0 (accept) or
          non-zero (reject) — e.g. grep -qE '^...$', never a shell string.

IMPORTANT: the mirror is a Z3 EXPRESSION, not a pattern string. z3.Re("...")
is a literal match, not a regex — see docs/TRAPS.md. Use the same API calls
your property uses.

Phase-1 gate: real engines are invoked with shell=False argv only.

Usage (whitelist [a-z0-9._-]+ vs grep):
  python3 scripts/differential-fuzz.py --mirror-expr \
      "Concat(Union(Range('a','z'),Range('0','9'),Re('.'),Re('_'),Re('-')),Star(Union(Range('a','z'),Range('0','9'),Re('.'),Re('_'),Re('-'))))" \
      --alphabet "abc123._-" --mutations ' ;="`$|&' --runs 500 --seed 42 \
      --real-argv grep -qE '^[a-z0-9._-]+$'

  Exit 0 = all inputs agree (mirror == real).
  Exit 1 = mismatch found (mirror and real disagree on some input).
  Exit 2 = usage error. Exit 3 = wrong z3-solver version.

A mismatch is the finding: either the mirror mis-encodes the real regex, or
the real code accepts something the declared property forbids. Ground-truth
a mismatch against the real code before reporting anything.
"""

import argparse
import itertools
import random
import sys

import z3

from regexproof.fuzz.adapters import real_accepts_argv

if not z3.get_version_string().startswith("5.0"):
    print(
        f"FATAL: z3-solver {z3.get_version_string()} — this harness is "
        "validated against 5.0.x only. pip install -r requirements.txt",
        file=sys.stderr,
    )
    sys.exit(3)

# Namespace for --mirror-expr: the z3py API (same names z3-verify.py uses).
# NOTE: no Opt — z3py's Opt is the optimizer class, not regex optional.
# Regex "?" is Union(r, Re("")).
MIRROR_NS = {
    "AllChar": z3.AllChar,
    "Concat": z3.Concat,
    "Union": z3.Union,
    "Range": z3.Range,
    "Re": z3.Re,
    "Star": z3.Star,
    "Plus": z3.Plus,
    "Loop": z3.Loop,
    "Complement": z3.Complement,
}


def mirror_accepts(mirror_expr, s: str) -> bool:
    """Z3 mirror: does the mirror regex language contain the concrete string?"""
    solver = z3.Solver()
    solver.set("timeout", 10000)
    solver.add(z3.InRe(z3.StringVal(s), mirror_expr))
    r = solver.check()
    if r == z3.unknown:
        print(f"    TIMEOUT deciding membership of {s!r} — treat as mismatch", file=sys.stderr)
        return False
    return r == z3.sat


def exhaustive(alphabet: str, max_len: int):
    """Exhaustive short strings: every input of length 0..max_len over alphabet.

    Small alphabets + short lengths are cheap and give full coverage of the
    interesting boundary region (empty, single chars, first/last alphabet
    chars)."""
    for n in range(max_len + 1):
        for tup in itertools.product(alphabet, repeat=n):
            yield "".join(tup)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--mirror-expr",
        required=True,
        help="Z3 regex expression (z3py API names; NOT a pattern string)",
    )
    ap.add_argument("--alphabet", required=True, help="input chars to fuzz with")
    ap.add_argument(
        "--mutations",
        default="",
        help="extra chars to splice in (dangerous chars); defaults to the "
        "non-ASCII divergence set (CJK, Arabic-Indic digits, fullwidth, "
        "NBSP/ideographic space) when empty",
    )
    ap.add_argument(
        "--targets",
        default=[],
        nargs="*",
        help="explicit adversarial inputs to check verbatim (deterministic; "
        "for position-sensitive divergences random splicing rarely hits)",
    )
    ap.add_argument("--runs", type=int, default=200, help="random inputs (beyond exhaustive short)")
    ap.add_argument("--seed", type=int, default=42, help="RNG seed (deterministic)")
    ap.add_argument(
        "--exhaust-max-len", type=int, default=3, help="exhaustive coverage up to this length"
    )
    ap.add_argument("--max-len", type=int, default=12, help="max generated string length")
    ap.add_argument(
        "--real-cmd",
        default=None,
        help=argparse.SUPPRESS,  # rejected: shell strings are forbidden
    )
    # REMAINDER so engine flags like -qE are not eaten by argparse. Place last:
    #   ... --alphabet abc --real-argv grep -qE '^[a-z]+$'
    ap.add_argument(
        "--real-argv",
        nargs=argparse.REMAINDER,
        help="argv: program + args (must be last); reads stdin, exit 0 = accept",
    )
    args = ap.parse_args()

    if args.real_cmd is not None:
        print(
            "FATAL: --real-cmd (shell string) is forbidden. Use --real-argv PROG [ARGS...]",
            file=sys.stderr,
        )
        return 2
    real_argv = list(args.real_argv or [])
    # argparse REMAINDER keeps a leading '--' if the caller used one.
    if real_argv and real_argv[0] == "--":
        real_argv = real_argv[1:]
    if not real_argv:
        print(
            "FATAL: --real-argv PROG [ARGS...] is required (place it last)",
            file=sys.stderr,
        )
        return 2
    args.real_argv = real_argv

    # Default mutation set: the non-ASCII divergence classes. Python's
    # \w\d\s\b are Unicode-aware; an ASCII mirror diverges on these (TRAP
    # 17). If the caller passes explicit mutations, honor those instead.
    # CJK, Latin-ext, Arabic-Indic digit, fullwidth digit, ideographic
    # space (U+3000, which is \s in Python).
    if not args.mutations:
        args.mutations = "中é٣１\u3000"

    # Compile the mirror once; fail fast on invalid expression.
    try:
        mirror = eval(args.mirror_expr, {"__builtins__": {}}, MIRROR_NS)
    except Exception as e:
        print(f"FATAL: invalid --mirror-expr {args.mirror_expr!r}: {e}", file=sys.stderr)
        return 2
    if not isinstance(mirror, z3.ReRef):
        print(
            f"FATAL: --mirror-expr must evaluate to a Z3 regex (got {type(mirror).__name__})",
            file=sys.stderr,
        )
        return 2

    rng = random.Random(args.seed)
    mismatches = 0
    checked = 0

    def check(s):
        nonlocal mismatches, checked
        checked += 1
        m = mirror_accepts(mirror, s)
        r = real_accepts_argv(args.real_argv, s)
        if m != r:
            mismatches += 1
            print(f"MISMATCH {s!r}: mirror={m} real={r}")

    # 1) Exhaustive short strings over the declared alphabet: full coverage of
    #    the boundary region (empty string, single chars, shortest combos).
    for s in exhaustive(args.alphabet, args.exhaust_max_len):
        check(s)

    # 2) Random strings over the alphabet (longer, sparse coverage).
    for _ in range(args.runs):
        n = rng.randint(args.exhaust_max_len + 1, args.max_len)
        check("".join(rng.choice(args.alphabet) for _ in range(n)))

    # 3) Explicit adversarial targets (deterministic — for position-sensitive
    #    divergences random splicing rarely hits, e.g. \\b boundaries where the
    #    dangerous char must sit immediately before the token).
    for t in args.targets:
        check(t)

    # 4) Mutation splice: take a random alphabet string and insert each
    #    dangerous char at EVERY position. Real code may reject these while
    #    the mirror still accepts them — that is a REAL divergence to report.
    #    (Every position, not one random position: \\b/\\w Unicode divergences
    #    only trigger at specific offsets.)
    for _ in range(args.runs):
        base = "".join(rng.choice(args.alphabet) for _ in range(rng.randint(1, args.max_len)))
        for ch in args.mutations:
            for pos in range(len(base) + 1):
                check(base[:pos] + ch + base[pos:])

    print(f"\n{checked} inputs, {mismatches} mismatches (seed={args.seed})")
    if mismatches:
        print(
            "Mismatches mean the mirror and the real implementation disagree. "
            "Ground-truth against the real code before reporting.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

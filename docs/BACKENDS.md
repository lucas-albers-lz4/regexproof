# Backends — what to use when

## The decision table

| Backend | Regex membership | String eq | Notes |
|---|---|---|---|
| `seq` (Z3 DEFAULT) | ✅ solves | ✅ | **Use this.** P2 whitelist 927ms, P3 sed model 2ms (5.0.0) |
| `z3str3` (`smt.string_solver=z3str3`) | ❌ `unknown` instantly | ✅ | Do not use for regex — silently fails on `InRe` (**verified-finding: VF-002**) |
| Z3-Noodler (VeriFIT fork) | ✅ (automata-based) | ✅ | Hard instances; `re.from_ecma2020`; extra string ops |
| cvc5 / Z3str3RE / dZ3 | ✅ | ✅ | Academic/other solvers — see below |
| recheck / safe-regex2 / … | n/a (complexity, not membership) | n/a | ReDoS analysis — see REDOS.md |

## Stock Z3 (`z3-solver` pip package)

<!-- verified-finding: VF-002 -->

The default `seq` backend solves regex by **lazy unfolding via symbolic
derivatives** — `z3str3` returns `unknown` instantly on `InRe` instead (see
[TRAPS.md#2](TRAPS.md#2-the-seq-backend-solves-regex-z3str3-returns-unknown-instantly)).
Consequences (measured), each with its canonical trap:
- containment properties: solve instantly via alphabet reasoning
- monolithic image-language proofs: time out — decompose ([TRAPS.md#6](TRAPS.md#6-regex-unfolding-is-incomplete-with-string-constraints))
- replacements (`re.replace_re`, `str.replace_all`): unsupported — use string ops ([TRAPS.md#5](TRAPS.md#5-rereplace_re--strreplace_all-are-not-supported))
- **search-wrapped shape-5 gap queries**: routinely `unknown` — use `fullmatch`
  mirrors + length bounds ([TRAPS.md#18](TRAPS.md#18-search-wrapped-rule_diff-blows-up-z3); **verified-finding: VF-007**)

Pin `z3-solver==5.0.0` — the `Re()`/regex API changed across 4.x/5.x.

## Z3-Noodler (when stock Z3 is too slow)

[github.com/VeriFIT/z3-noodler](https://github.com/VeriFIT/z3-noodler) — a
fork of Z3 that **replaces the string theory solver** with the
equation-stabilization algorithm + the Mata automata library. When to consider:

- Word equations with regular + length constraints that stock Z3 times out on
- Extra string functions: `str.to_lower`, `str.to_upper`, `str.trim`,
  `str.delete`, `str.to_real/from_real`, `str.update`
- **`re.from_ecma2020`** — converts ECMA/JS regexes to Z3 regexes. The only
  way to show that a JS regex is correct *as written* when it uses JS-only features. It also
  shows that the authoritative source is correct rather than a hand-ported mirror.

Caveats: NOT pip-installable as a drop-in. It is a separate binary
(`cmake -DCMAKE_BUILD_TYPE=Release .. && make`, auto-fetches Mata; run
`./z3 file.smt2`). MIT license (competition use needs separate license). CI
wiring needs a build step or vendored binary.

## The rest of the SMT ecosystem (research context)

- **dZ3** (UPenn / Microsoft Research) — regex solver in Z3's sequence theory
  based on *symbolic Boolean derivatives*. It supports "extended" regular
  expressions (Boolean combinations) over an arbitrary character theory.
  MSR-TR-2020-25. These are the ideas behind Z3's own regex handling.
- **Z3str3RE** (arXiv:2010.07253) — length-aware solving for the theory of
  regex membership + linear arithmetic over string length. It is the decision
  procedure behind Z3str3's regex support.
- **cvc5** — supports string + regex theories (regular-expression
  intersection). Use cvc5 as a second opinion on cross-solver soundness
  (also: watch the Z3 issue tracker for soundness bugs — for example,
  Z3Prover/z3#10379 was an incorrect SAT on a string/regex formula).
- **AWS Zelkova / Z3 Automata** — AWS extended Z3 with their own automata-based
  regex solver to reason about IAM policy languages. Precedent that SMT regex
  reasoning is production-grade.
- **String-solver ecosystem:** S3P, Norn, HAMPI, Kaluza, Stranger. These are
  mostly symbolic-execution tooling. They are relevant background for the
  theory, not needed for the membership/counterexample patterns in this repo.

## Rule of thumb

Start with stock `z3-solver` `seq` backend + the 5 canonical shapes (incl.
shape-5 `rule_diff`). Escalate to Z3-Noodler only when: (a) the pattern is
JS/ECMA and you want to show that it is correct as written, or (b) stock Z3 times out on a
property that decomposition could not fix.

### U9 scope note (Phase 1/4, #228/#220 — NORMATIVE)

The harness does **not** route through `re.from_ecma2020` (U9 DROP, measured:
silent `\p{}` literalization, negated-membership SIGABRT, no flag
representation). All harness routes are **mirror-route only**; the S3
authority guard requires an explicitly recorded `route: "mirror"` for the
`cross-checked` tier. The backend binary is sha256-pinned (R5 policy: cache
key = asset sha256; bump = make sure that the cold download works → update `preflight.py` + CI +
`PIN.md` → luna-gated PR). The `noodler` CI job downloads the pinned asset,
runs the R8 pre-flight, and exercises the S16 noodler-backed fixture
(`P1-space`) with the real binary; stock-only CI keeps that same fixture
treated as absent (`triage_fallback`, exit unchanged, tier `seq-only`).

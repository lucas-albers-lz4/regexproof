# Blocker exit-criterion probe (design #213 §7 #2) — NETFILTER_KV_GLUE

Run 2026-08-11, pinned Noodler v1.6.1 (sha256 22b19f12…464), stock z3 5.0.0, cvc5
1.3.4 (isolated worker). Property under test: the mirror language ≡ the as-written
ECMA language (if equivalent, any property provable on the mirror holds for the
pattern as written). **Scope: solver-route feasibility.** The actual fwlive property
formulas (F2/F3, #120) are the handoff scope of Phase 5 (#221), not this probe.
**Equivalence basis: exactness BY CONSTRUCTION (S12 — the lookahead is a
constant-width positive assertion, so `X(?=K=)` ≡ `XK=` as a search language) plus
the E2M theorem below plus the 937-string regression corpus. This probe does NOT
prove the M2E direction (Noodler cannot decide it) — see the theorem section.**

## Branch outcomes

| Branch | Route | Result | Tier available |
|---|---|---|---|
| **A (primary)** | mirror through stock z3 + cvc5 cross-check | **PASS (feasibility)** — nonemptiness `sat` on both solvers (17.0ms / 19.9ms, agreeing); boundary set: stock decides 13/13, cvc5 decides 10/13 and AGREES on all 10 (the 3 control-char strings `\tIN=`, `x\nIN=`, `x\x00IN=` → cvc5 worker ABSTAIN-SIGSEGV, the documented crash class with a control-char trigger — recorded, never a disagreement) | `cross-checked` available for mirror-route formulas cvc5 can parse |
| **B** | from_ecma2020 (as-written, search-wrapped) | **PASS where it decides** — boundary membership correct (xIN= True, \tIN= False, …); abstains only on exact-boundary anchored forms (measured class) | `escalated-unconfirmed` ceiling (S3 guard) |
| **C** | neither decides | **not hit** — the mirror decides everything | — |

## Equivalence theorem (both directions, Noodler, declared ASCII domain)

- **E2M (ECMA ⊆ mirror): UNSAT** — the mirror language CONTAINS the as-written
  ECMA language within the declared domain. Every as-written glue point is caught
  by the mirror. This is the soundness-critical direction: the mirror cannot miss
  a glue position.
- **M2E (mirror ⊆ ECMA): NOT PROVABLE AT SOLVER LEVEL — Noodler ABORTS on negated
  `from_ecma2020` membership (rc=-6, SIGABRT; measured with and without the domain
  constraint).** Evidence for this direction is regression-only: the pilot's
  937-string corpus (0 divergences) plus D14 differential fuzz — exactly the
  design's D14 scoping (finite probe sets are regression evidence, never
  equivalence). The abort is an honest solver-level abstention, never a wrong
  verdict; the harness records it as an abstain state.

## Domain-boundary witness (why the theorem must be declared-domain-scoped)

The UNCONSTRAINED E2M theorem is `sat` with witness `NUL NUL "CODE=" TAB U+0080`
— the only non-ASCII char is the trailing U+0080, outside the mirror's declared
`\x00-\x7f` domain. The discrepancy is purely the domain boundary, not a \s or
lookahead issue. With the ASCII-domain constraint, E2M is `unsat`. This is the
measured justification for D14's declared-input-domain scoping.

## Noodler robustness finding (feeds the soundness section)

**Negated `re.from_ecma2020` membership aborts the pinned binary (SIGABRT, rc=-6).**
Class: solver-level abstention (honest — no wrong verdict, but a crash). Impact:
any property encoding `¬(from_ecma2020(...))` (rule_diff or complement shapes) must
avoid the negation (prove the positive direction + D14 regression evidence), and
the harness records the abort per the S13 abstain states. Combined with the S3
authority guard: the ECMA route is also unprovable in the mirror-⊆-ECMA direction,
so the mirror remains the only proof-capable route.

## cvc5 worker crash trigger (feeds D2 evidence)

The cvc5 worker ABORTs (SIGSEGV, rc -11) on formulas whose string literal contains
control characters (`\t`, `\n`, `\x00` — the boundary set's three abstaining
strings) — the batch-segfault class with a control-char trigger, captured live.
The per-query isolation (D2) contains it; the affected queries record
ABSTAIN-SIGSEGV. No wrong verdicts: cvc5 agrees with stock on every string it
decides (10/10).

## Conclusion

**Solver-route feasibility established for Branch A at `cross-checked`-tier
availability**: the mirror route matches the as-written language on the
soundness-critical direction (E2M unsat — the mirror cannot miss a glue point),
is exact by construction (S12) with 937-string regression evidence, cross-checks
cleanly (cvc5 agrees on every string it parses), and is boundary-correct (13/13
stock, matching real JS). The M2E direction is regression-evidenced only (Noodler
cannot decide it). Branch B passes where it decides with the honest ceiling;
Branch C not hit. The actual fwlive property verdicts — the reason this ticket
exists — are Phase 5 (#221) work: the route is now verified feasible to carry them.

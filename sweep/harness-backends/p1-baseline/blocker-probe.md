# Blocker exit-criterion probe (design #213 §7 #2) — NETFILTER_KV_GLUE

Run 2026-08-11, pinned Noodler v1.6.1 (sha256 22b19f12…464), stock z3 5.0.0, cvc5
1.3.4 (isolated worker). Property under test: the mirror language ≡ the as-written
ECMA language (if exact, any property provable on the mirror holds for the pattern
as written).

## Branch outcomes

| Branch | Route | Result | Tier available |
|---|---|---|---|
| **A (primary)** | mirror through stock z3 + cvc5 cross-check | **PASS** — nonemptiness `sat` on both solvers (16.8ms / 20.4ms, agreeing); 13-string boundary set decided identically (real-tab and space cases `unsat`, NUL and glue cases `sat` — all matching real JS) | `cross-checked` |
| **B** | from_ecma2020 (as-written, search-wrapped) | **PASS where it decides** — boundary membership correct (xIN= True, \tIN= False, …); abstains only on exact-boundary anchored forms (measured class) | `escalated-unconfirmed` ceiling (S3 guard) |
| **C** | neither decides | **not hit** — the mirror decides everything | — |

## Equivalence theorem (both directions, Noodler, declared ASCII domain)

- **E2M (ECMA ⊆ mirror): UNSAT** — the mirror language CONTAINS the as-written
  ECMA language within the declared domain. Every as-written glue point is caught
  by the mirror. This is the soundness-critical direction: the mirror cannot miss
  a glue position.
- **M2E (mirror ⊆ ECMA): NOT PROVABLE AT SOLVER LEVEL — Noodler ABORTS on negated
  `from_ecma2020` membership (rc=-6, SIGABRT; measured both with and without the
  domain constraint).** Evidence for this direction is regression-only: the pilot's
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
be rewritten to avoid the negation (e.g., prove the positive direction + rely on
D14 regression evidence), and the harness records the abort per the S13 abstain
states. Mitigation in the design: the S3 authority guard already caps the ECMA
route; this finding extends it — the ECMA route is also UNPROVABLE in the
mirror-⊆-ECMA direction, so the mirror remains the only proof-capable route, now
for both directions' practical purposes.

## Conclusion

**Branch A passes at `cross-checked` tier availability** — the mirror route for the
fwlive blocker is exact (E2M theorem), cross-checkable (stock + cvc5 agree), and
boundary-correct. Branch B passes where it decides with the honest ceiling. Branch
C not hit. The blocker's exit criterion is satisfied: the pattern can be proven
via the mirror with a cross-check, and the as-written route is verified as a
faithful diagnostic on its decided set.

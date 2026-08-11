# Phase 4 sweep report (P4, #220)

- corpus commit: `7a0ec5a05c4c1655959e1914b4dde09b9de423df`
- manifest files: 8 (schema v1: commit + paths + sha256)
- manifest verified: True

## Four-bucket classification (S4)

| property | bucket | noodler | cvc5 | evidence |
|---|---|---|---|---|
| P2-len64 | proven | unsat | unsat | - |
| P4-monolithic | escalated-unconfirmed | unsat | no-verdict | - |

Bucket counts: proven=1, finding=0, escalated-unconfirmed=1, still-unknown=0 (exactly one per property, S4)

## Residual-undetectable (metric 8)

- noodler-only: 0
- ecma-route: 0 (0 post-U9-DROP — no ECMA leg)
- cvc5-abstained: 1

## Divergence rate (D10)

- decided cross-check pairs: 1
- disagreements: 0
- divergence rate: 0.0

## Triage audit (S14)

- disagreements: 0, explained: 0, unexplained: none

## U9 publication

- decision: **DROP (from_ecma2020 out of scope)**
- reopen trigger hit: False
- evidence: {"divergence_rate": {"decided_pairs": 1, "disagreements": 0, "divergence_rate": 0.0}, "matrix_measured": {"P2-len64": "noodler unsat 17.4ms, cvc5 unsat 12.2ms (agree)", "P4-monolithic": "noodler unsat 19.3ms, cvc5 unknown 30s (cvc5 abstain)"}, "all_six_fwlive_patterns_mirror_expressible": true}

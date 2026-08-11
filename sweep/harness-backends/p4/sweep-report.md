# Phase 4 sweep report (P4, #220)

- corpus commit: `0e71c788ddfcd1c0c453648d4bc13077ba0491f4`
- manifest files: 10 (schema v1: commit + repo-relative paths + sha256)
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
- divergent pairs: 0 (disagreements=0, wrong-verdict events=0)
- divergence rate: 0.0
- **D10 decision: KEEP — zero divergence on the measured set; the cross-check agrees and the disagreement gate is dormant** (threshold: any divergent pair keeps the gate)

## Triage audit (S14)

- disagreements: 0, explained: 0, unexplained: none

## U9 publication

- decision: **DROP (from_ecma2020 out of scope)**
- reopen trigger hit: False
- consumed artifact: `/root/workspace/regexproof/sweep/harness-backends/p1-baseline/u9-decision.md`
- evidence: {"divergence": {"decided_pairs": 1, "divergent_pairs": 0, "disagreements": 0, "wrong_verdict_events": 0, "divergence_rate": 0.0}, "d10_decision": "KEEP \u2014 zero divergence on the measured set; the cross-check agrees and the disagreement gate is dormant", "fwlive_patterns": ["NON_FIREWALL_PREFIX", "FIREWALL_HINT", "ACTION_RE", "DENY_ACTION", "TCP_FLAG_TAIL", "NETFILTER_KV_GLUE"], "fwlive_pattern_count": 6, "pilot_mirror_divergences": 0, "measured_matrix_rows": 28}

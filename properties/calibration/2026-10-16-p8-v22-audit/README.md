# P8 audit of the v22 cohort and webhook slice

This addendum preserves v22 as a frozen retrospective checkpoint and records a fresh same-model review. It does not relabel correlated agent review as a human gold label. The exact pinned Aidevops receiver bytes were checked against SHA-256 `6d882dac90c3f9deb1a0007c9a4216d70f365a4a34ffacd145eb04cc8ae3a325`.

## Findings

- The v22 contract report remains 50 questions: 35 UNSAT, 14 ground-truthed SAT, and one timeout. The v11 overlay still classifies the 14 SAT rows as two refuted claims and 12 product candidates across ten groups; confirmed security impacts and external outcomes remain zero.
- The fresh full-census review reconfirmed six source-backed skips and one unresolved numeric-config site. It found that the old SHA and PR contracts described composed sink/dispatch behavior beyond their UNSAT queries. Their active contracts are now narrowed to the exact regex-language theorems. The historical contracts and v22 checkpoint are preserved unchanged.
- The corrected contracts passed the exact-pin regression gate: three UNSAT properties, four real-source mutation replays, 671 Bash/compiler pattern comparisons, 48 integrated helper cases, and zero mismatches. The full slug-helper inclusion attempt still times out; finite comparisons do not replace that proof.
- The audit gate rerun took 6.115017 seconds wall-clock. It attempted three existing questions, added no new question identity, and recorded no SAT candidate, reachable violation, security impact, external report, confirmation, or fix. The review duration, tokens, cost, and human active time remain unknown.
- The original P6 preflight failure is preserved, and the runner gap is now resolved with documented shape 6. A follow-on P6 wave completed all three corrected questions, source verification, mutation guards, and the exact-pin product gate; see the [shape-6 wave bundle](p6-shape6-r1/README.md). This repeated v22 questions and added no new P2 yield.
- A separate P8 candidate follow-up confirms a local Tor response-handling defect while leaving deployment/security impact unconfirmed; no report was sent. See the [Tor disposition](tor-newnym-disposition/README.md).

## Artifacts

- [Row-by-row source audit](audit.json), including each original source-order disposition and the fresh review result.
- [Corrected exact-pin gate report](aidevops-webhook-gate-report.json).
- [P6 runner scope correction](p6-scope-correction/README.md): the frozen preflight failure and its zero-work scope are preserved, with the later shape-6 resolution linked.
- [P6 shape-6 successful wave](p6-shape6-r1/README.md) and [updated cohort scorecard](scorecard-after-shape6.json).
- [Tor NEWNYM significance disposition](tor-newnym-disposition/README.md): one local false-success defect is confirmed; security impact and external outcome remain unconfirmed.
- [Historical gate report captured with v22](../2026-10-16-autonomous-aidevops-webhook-action-protocol-20r2/gate-report-v22-frozen.json).
- [Corrected SHA regex contract](../2026-10-16-autonomous-aidevops-webhook-action-protocol-20r2/contract-check-sha-regex-only.json) and [corrected PR regex contract](../2026-10-16-autonomous-aidevops-webhook-action-protocol-20r2/contract-process-pr-number-regex-only.json).
- [Repository/dialect stratification](../2026-10-16-p2-existing-evidence-20r2-v22/stratification.md) and [machine-readable source data](../2026-10-16-p2-existing-evidence-20r2-v22/stratification.json).

## Scope

This is an evidence correction and reproduction record, not a new v23 aggregate checkpoint. No files in the frozen v22 checkpoint were edited. The follow-on P6 wave joins the corrected contract digests in its local checkpoint only. A future retrospective aggregate should join them if the campaign requires a refreshed cohort checkpoint. No maintainer or third party was contacted.

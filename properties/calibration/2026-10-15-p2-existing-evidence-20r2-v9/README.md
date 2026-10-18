# 20-r2 compatible existing product evidence v9

This is a retrospective aggregate of exact-cohort product evidence joined to
the corrected P2 source inventory. It is not a prospective sample, a ranked
15-site review wave, or an estimate of future conversion yield.

## Snapshot

- Frozen cohort: `2026-09-12-calibration-20-r2`, manifest digest
  `5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d`.
- Inventory: 20,784 raw sites across 19 complete repositories and one
  repository with six unavailable submodules.
- Compatible evidence: **27** unique exact-pin questions; **16 UNSAT** and
  **11 ground-truthed SAT**. All SAT rows remain pending product triage in the
  strict checkpoint.
- Contract provenance: 20 autonomous and seven historical human contracts.
- Useful local gates: 14. Product-engine replays: 22. Differential cases:
  112,888.
- Consumer-adopted gates, confirmed security impacts, external reports,
  maintainer confirmations, and third-party fixes: zero.
- The checkpoint is 27 of the 50-question target, a shortfall of 23. Three
  attempts remain excluded because their dialects are outside the declared P2
  inventory.

The increment from v8 is two Inhale source questions, one exact-helper gate,
two product-engine replays, and six additional differential cases. The P6
runner verifies the exact Inhale source pin, both ground-truthed SAT witnesses,
the source mutation, and the local gate, then records `needs_review` pending
product-impact disposition. The concrete URLs are operator-supplied config;
the local fixture establishes output-root escape behavior, not a deployment
impact or attacker-controlled caller.

## P2 review coverage

Eight selected repository slices have complete source-review artifacts; they do
not cover the full 20-member cohort:

| Repository slice | Sites | Skips | Unresolved | Adopted |
|---|---:|---:|---:|---:|
| Malcontent Go regexes | 15 | 11 | 2 | 2 |
| Anax Go regexes | 26 | 15 | 10 | 1 |
| AutoAR Go regexes | 34 | 28 | 3 | 3 |
| llm-honeypot POSIX shell | 16 | 14 | 0 | 2 |
| Panther Python regexes | 45 | 44 | 0 | 1 |
| Inhale Python regexes | 3 | 0 | 1 | 2 |
| BinaryAlert Python regexes | 1 | 1 | 0 | 0 |
| Snyk LS Go regexes | 37 | 36 | 1 | 0 |
| **Total** | **177** | **149** | **17** | **11** |

The Inhale crawler's same-origin behavior remains unresolved: a raw prefix
check permits a hostname that shares the base URL text, but the repository
does not state an independent same-origin requirement. This behavior is not a
product question in the strict checkpoint.

The Snyk Language Server's hover `<br>` replacement is also unresolved:
the source describes sanitization, but does not establish supported-client
HTML rendering or an independent markup-sanitization guarantee. It is not a
product question in the strict checkpoint.

## Downstream candidate overlay

The separate [v9 SAT impact triage](../2026-10-15-p2-sat-impact-triage-v9/README.md)
refutes two historical Doberman claims and retains nine candidate questions
across seven issue families. The new Inhale output-path family groups the
single-file and directory save sites. The strict checkpoint still counts all
eleven SAT rows as pending product triage. Confirmed impact and external
outcomes remain zero.

## Evaluation tracks

| Track | Current evidence | What it measures |
|---|---|---|
| Useful contract-backed proofs and regression gates | 27 decided questions, 14 useful local gates, 22 product replays, 112,888 differential cases | Contract quality and exact-engine regression evidence; questions are deduplicated by exact product identity. |
| Product bug candidates | 11 replayed SAT rows; two historical claims refuted; nine candidate questions remain | Counterexamples through real-code replay and product-impact triage. Confirmed impact remains zero. |
| External outcomes | Zero reports, maintainer confirmations, or fixes | Only reports sent with authorization and independently evidenced outcomes. |

## Reproduction

```sh
.venv/bin/python scripts/build-p2-evidence-checkpoint.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-15-p2-source-inventory-v2/inventory.json \
  --sites properties/calibration/2026-10-15-p2-source-inventory-v2/sites.ndjson \
  --checkpoint-root properties/calibration \
  --conversion-root properties/generated \
  --repo-root . \
  --out-dir properties/calibration/2026-10-15-p2-existing-evidence-20r2-v9

.venv/bin/python scripts/conversion-checkpoint.py \
  properties/calibration/2026-10-15-p2-existing-evidence-20r2-v9/checkpoint.json
```

Exact identities and attempts are in [`checkpoint.json`](checkpoint.json) and
[`attempts.json`](attempts.json); summary metrics are in
[`report.json`](report.json). The Inhale proof, gate, P6 state, and source
review are linked from the [parent plan](../../../docs/AUTONOMOUS-CORPUS-PLAN.md).

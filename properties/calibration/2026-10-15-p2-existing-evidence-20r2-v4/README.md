# 20-r2 compatible existing product evidence v4

This is a **retrospective** aggregate of historical exact-cohort product
evidence matched to the corrected P2 source inventory. It is not a prospective
sample, a new review wave, or an estimate of conversion yield.

## Snapshot

- Frozen cohort: `2026-09-12-calibration-20-r2`, manifest digest
  `5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d`.
- Inventory: 20,784 raw sites across 19 complete repositories and one
  repository with six unavailable submodules.
- Compatible evidence: 20 unique exact-pin questions; 15 UNSAT and five
  SAT witnesses with persisted product replays, all five pending product
  impact triage.
- Contract provenance: 13 autonomous and seven historical human contracts.
- Useful local gates: 9. Product-engine replays: 15. Differential cases:
  46,321.
- Consumer-adopted gates, confirmed security impacts, authorized external
  reports, maintainer confirmations, and fixes: zero.
- The strict checkpoint is 20 of the 50-question target, a shortfall of 30.

The two imported Doberman-Core questions are historical human-contract rows
from the canonical conversion ledger. Their exact pins and source file/line
anchors join the frozen P2 inventory, and their persisted rows record replayed
SAT witnesses. They contribute two product-engine replays and two pending
triage candidates. Their imported attempt records deliberately do not claim
source-pin verification or a reusable local gate: neither legacy row carries
that gate evidence. The old Doberman close-out describes the witness classes,
but this aggregate does not upgrade that description into a current local
regression command.

The six exact-cohort Forge CLI canonical rows match questions already present
in a checkpoint. They are listed as corroborating evidence and do not increase
the denominator. Three attempts remain excluded from the declared-dialect
count: two AutoAR HTML-escaper attempts and one Malcontent YARA rule. Earlier
aggregate snapshots remain preserved; the builder validates their sidecar
markers before excluding them from source discovery.

This import corrects historical accounting only. The two Doberman questions
are not new review, autonomous-contract, or P7 yield and are not included in
the agent-only scorecard. The aggregate remains selected retrospective
evidence, not an independently sampled estimate of product bug prevalence.

## Reproduction

```sh
.venv/bin/python scripts/build-p2-evidence-checkpoint.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-15-p2-source-inventory-v2/inventory.json \
  --sites properties/calibration/2026-10-15-p2-source-inventory-v2/sites.ndjson \
  --checkpoint-root properties/calibration \
  --conversion-root properties/generated \
  --repo-root /home/lalbers/gitroot/regexproof \
  --out-dir properties/calibration/2026-10-15-p2-existing-evidence-20r2-v4

.venv/bin/python scripts/conversion-checkpoint.py \
  properties/calibration/2026-10-15-p2-existing-evidence-20r2-v4/checkpoint.json
```

# 20-r2 compatible existing product evidence v2

This is a **retrospective** aggregate of exact-cohort product checkpoints
matched to the corrected P2 source-site inventory. It is not a prospective
sample, a new review wave, or an estimate of conversion yield.

## Snapshot

- Frozen cohort: `2026-09-12-calibration-20-r2`, manifest digest
  `5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d`.
- P2 inventory: 20,784 raw sites across 19 complete repositories and one
  repository with six unavailable submodules.
- Compatible evidence: 17 unique exact-pin product questions; 14 UNSAT and
  three replayed SAT witnesses, all three pending product-impact triage.
- Contract provenance: 12 autonomous and five historical human contracts.
- Useful local gates: 8. Product-engine replays: 12. Differential cases:
  45,659.
- Consumer-adopted gates, external reports, maintainer confirmations, and
  fixes: zero.
- The strict checkpoint is 17 of the 50-question target, a shortfall of 33.
  This is an evidence count, not a claim of source-surface coverage.

Three attempts remain visible but excluded from the declared-dialect count:
two AutoAR HTML-escaper attempts (one failed runner attempt and its later
passing UNSAT run) and one Malcontent YARA rule. The earlier v1 aggregate is
preserved at the sibling path; the builder now recognizes its sidecar
`source-checkpoints.json` as an aggregate marker and will not recursively count
it as a source checkpoint.

## Reproduction

```sh
.venv/bin/python scripts/build-p2-evidence-checkpoint.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-15-p2-source-inventory-v2/inventory.json \
  --sites properties/calibration/2026-10-15-p2-source-inventory-v2/sites.ndjson \
  --checkpoint-root properties/calibration \
  --repo-root /home/lalbers/gitroot/regexproof \
  --out-dir properties/calibration/2026-10-15-p2-existing-evidence-20r2-v2

.venv/bin/python scripts/conversion-checkpoint.py \
  properties/calibration/2026-10-15-p2-existing-evidence-20r2-v2/checkpoint.json
```

`source-checkpoints.json` records the source digests, exact source-site joins,
excluded attempts, and contributing checkpoint paths. `roster.json`,
`attempts.json`, `checkpoint.json`, `report.json`, and `conversion.ndjson`
contain the joined question and evidence records.

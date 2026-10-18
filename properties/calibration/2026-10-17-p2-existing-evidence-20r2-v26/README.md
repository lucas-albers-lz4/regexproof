# P2 retrospective evidence checkpoint v26

This additive checkpoint joins v25 with one new exact-pin Tracecat question.
The frozen v22 and additive v23-v25 artifacts remain unchanged. This
retrospective aggregate does not select a prospective sample or estimate yield
for unreviewed sites.

## Result

- 54 eligible exact-source questions asked; the 50-question evaluation target
  is reached, but this is not a success threshold.
- 53 questions are decided: 39 UNSAT guarantees and 14 ground-truthed SAT
  questions. One earlier question remains timed out and **not proven**.
- The new table-identifier question proves that the exact table and column
  request allowlist excludes double quotes. Its mutation reproduces at the
  request-model layer; the unchanged service validator still rejects the
  mutated value before DDL. The Pydantic/service gate checks 2,227 inputs with
  zero mismatches. The final-line-feed behavior is recorded as a non-finding:
  the request model accepts it, but the service rejects it before DDL.
- Aggregate useful-gate evidence is 28 local runnable gates, 49 product-engine
  replays, and 1,758,132 differential cases. Consumer-adopted gates remain
  zero.
- The SAT track remains unchanged at 14 ground-truthed product candidates;
  confirmed security impacts, reports, maintainer confirmations, and
  third-party fixes remain zero.
- Contract provenance is 47 agent-derived and 7 human.
- The target of 100 remains 46 questions short. Reaching 50 is an evaluation
  sample-size milestone, not evidence of success or security impact.

## Lineage and reproduction

`source-checkpoints.json` binds the aggregate to the exact v23-v25 checkpoint
inputs and the new Tracecat table-identifier P6 checkpoint. Rebuild with the
exact-pin v5 inventory:

```sh
.venv/bin/python scripts/build-p2-evidence-checkpoint.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-16-p2-source-inventory-v5/inventory.json \
  --sites properties/calibration/2026-10-16-p2-source-inventory-v5/sites.ndjson \
  --checkpoint-root properties/calibration/2026-10-17-p2-checkpoint-input-v26 \
  --out-dir properties/calibration/2026-10-17-p2-existing-evidence-20r2-v26
```

Machine-readable output is in `report.json`, `checkpoint.json`,
`attempts.json`, `conversion.ndjson`, `roster.json`, and
`source-checkpoints.json`. See the [table-identifier P6 bundle](../2026-10-17-autonomous-tracecat-table-identifier/README.md)
for source and gate details.

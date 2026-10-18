# P2 retrospective evidence checkpoint v27

This additive checkpoint joins v26 with one new exact-pin Tracecat question.
The frozen v22 and additive v23-v26 artifacts remain unchanged. This
retrospective aggregate does not select a prospective sample or estimate
yield for unreviewed sites.

## Result

- 55 eligible exact-source questions asked; the 50-question evaluation target
  is reached, but this is not a success threshold.
- 54 questions are decided: 40 UNSAT guarantees and 14 ground-truthed SAT
  questions. One earlier question remains timed out and **not proven**.
- The new sandbox environment-key contract proves, without a string-length
  bound, that the pinned nsjail validator's accepted character alphabet
  excludes POSIX's `=` name/value separator. Its mutation reproduces, and the
  exact-source gate checks 4,232 inputs with zero mismatches. The source also
  accepts a terminal LF because it uses Python `.match()` with `$`; the
  contract does not claim complete POSIX-name validity.
- Aggregate useful-gate evidence is 29 local runnable gates, 50 product-engine
  replays, and 1,762,364 differential cases. Consumer-adopted gates remain
  zero.
- The SAT track remains unchanged at 14 ground-truthed product candidates;
  confirmed security impacts, reports, maintainer confirmations, and
  third-party fixes remain zero.
- Contract provenance is 48 agent-derived and 7 human.
- The target of 100 remains 45 questions short. Reaching 50 is an evaluation
  sample-size milestone, not evidence of success or security impact.

The first local encoding attempt for the new question timed out at 30 seconds
and its mutation callback did not recognize the harness's witness field. The
failure and correction are preserved in the [sandbox contract bundle](../2026-10-17-autonomous-tracecat-sandbox-env-equals/README.md).
It is not a second unique question; the final question outcome is UNSAT.

## Lineage and reproduction

`source-checkpoints.json` binds the aggregate to the exact v23-v26 checkpoint
inputs and the new Tracecat sandbox environment-key P6 checkpoint. Rebuild
with the exact-pin v5 inventory:

```sh
.venv/bin/python scripts/build-p2-evidence-checkpoint.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-16-p2-source-inventory-v5/inventory.json \
  --sites properties/calibration/2026-10-16-p2-source-inventory-v5/sites.ndjson \
  --checkpoint-root properties/calibration/2026-10-17-p2-checkpoint-input-v27 \
  --out-dir properties/calibration/2026-10-17-p2-existing-evidence-20r2-v27
```

Machine-readable output is in `report.json`, `checkpoint.json`,
`attempts.json`, `conversion.ndjson`, `roster.json`, and
`source-checkpoints.json`. See the [sandbox environment-key P6 bundle](../2026-10-17-autonomous-tracecat-sandbox-env-equals/README.md)
for exact-source and gate evidence.

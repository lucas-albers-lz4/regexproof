# P2 retrospective evidence checkpoint v23

This additive checkpoint joins the frozen v22 evidence with one new
post-v22, exact-pin Tracecat question. The v22 artifact is unchanged. The
aggregation does not select a prospective sample or estimate yield for
unreviewed sites.

## Result

- 51 eligible exact-source questions asked; the 50-question evaluation target
  is reached, but this is not a success threshold.
- 50 questions are decided: 36 UNSAT guarantees and 14 ground-truthed SAT
  questions. One earlier question remains timed out and **not proven**.
- The new Tracecat artifact path-segment question is UNSAT, has a ground-truthed
  source-weakened slash mutation, and passed an exact-source gate over 2,467
  inputs. It adds one local runnable gate, one product-engine replay, and
  2,467 question-attributed differential cases.
- Aggregate useful-gate evidence is 25 local runnable gates, 46 product-engine
  replays, and 1,750,804 differential cases. Consumer-adopted gates remain
  zero.
- The SAT outcome overlay is unchanged: 14 ground-truthed candidates; confirmed
  security impacts, reports, maintainer confirmations, and third-party fixes
  remain zero. The new UNSAT question is not a bug finding.
- Contract provenance is 44 agent-derived and 7 human.

## Lineage and reproduction

`source-checkpoints.json` binds the aggregate to two exact checkpoint inputs:
the byte-identical v22 `checkpoint.json` and the new Tracecat P6 runner's v3
checkpoint. The frozen v22 checkpoint SHA-256 remains
`ecbbf6ba284bea5454ca34cafd33470fdaa5dfc62db7034c4f0834b1cac0b249`.

Rebuild with the exact-pin v5 inventory:

```sh
.venv/bin/python scripts/build-p2-evidence-checkpoint.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-16-p2-source-inventory-v5/inventory.json \
  --sites properties/calibration/2026-10-16-p2-source-inventory-v5/sites.ndjson \
  --checkpoint-root properties/calibration/2026-10-16-p2-checkpoint-input-v23 \
  --out-dir properties/calibration/2026-10-16-p2-existing-evidence-20r2-v23
```

`report.json`, `checkpoint.json`, `attempts.json`, `conversion.ndjson`,
`roster.json`, and `source-checkpoints.json` are the machine-readable result.
The source review and exact gate are documented in the [Tracecat P6 bundle](../2026-10-16-autonomous-tracecat-artifact-path-segment/README.md).

# P2 retrospective evidence checkpoint v24

This additive checkpoint joins v23 with one new post-v23, exact-pin Tracecat
question. Frozen v22 and additive v23 artifacts are unchanged. The aggregation
does not select a prospective sample or estimate yield for unreviewed sites.

## Result

- 52 eligible exact-source questions asked; the 50-question evaluation target
  is reached, but this is not a success threshold.
- 51 questions are decided: 37 UNSAT guarantees and 14 ground-truthed SAT
  questions. One earlier question remains timed out and **not proven**.
- The new workspace-sync path-segment question is UNSAT, has a ground-truthed
  source-weakened colon mutation, and passed an exact-source gate over 2,469
  inputs. It adds one local runnable gate, one product-engine replay, and
  2,469 question-attributed differential cases.
- Aggregate useful-gate evidence is 26 local runnable gates, 47 product-engine
  replays, and 1,753,273 differential cases. Consumer-adopted gates remain
  zero.
- The SAT outcome overlay is unchanged: 14 ground-truthed candidates; confirmed
  security impacts, reports, maintainer confirmations, and third-party fixes
  remain zero. The new UNSAT question is not a bug finding.
- Contract provenance is 45 agent-derived and 7 human.

## Lineage and reproduction

`source-checkpoints.json` binds the aggregate to two exact checkpoint inputs:
the byte-identical v23 `checkpoint.json` and the new workspace-sync P6 runner's
v3 checkpoint. The v23 checkpoint SHA-256 is
`b031de9cc13deabbc0a26897fa7429bbba3298d5a4466a60f01f8e00a1201761`; its
copied input has the same digest. The frozen v22 checkpoint remains preserved
in its original directory.

Rebuild with the exact-pin v5 inventory:

```sh
.venv/bin/python scripts/build-p2-evidence-checkpoint.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-16-p2-source-inventory-v5/inventory.json \
  --sites properties/calibration/2026-10-16-p2-source-inventory-v5/sites.ndjson \
  --checkpoint-root properties/calibration/2026-10-16-p2-checkpoint-input-v24 \
  --out-dir properties/calibration/2026-10-16-p2-existing-evidence-20r2-v24
```

`report.json`, `checkpoint.json`, `attempts.json`, `conversion.ndjson`,
`roster.json`, and `source-checkpoints.json` are the machine-readable result.
The source review and exact gate are documented in the [Tracecat workspace-sync
P6 bundle](../2026-10-16-autonomous-tracecat-workspace-sync-path-segment/README.md).

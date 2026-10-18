# P2 retrospective evidence checkpoint v25

This additive checkpoint joins v24 with one new post-v24, exact-pin Tracecat
question. Frozen v22 and additive v23/v24 artifacts are unchanged. The
aggregation does not select a prospective sample or estimate yield for
unreviewed sites.

## Result

- 53 eligible exact-source questions asked; the 50-question evaluation target
  is reached, but this is not a success threshold.
- 52 questions are decided: 38 UNSAT guarantees and 14 ground-truthed SAT
  questions. One earlier question remains timed out and **not proven**.
- The new RBAC scope-pattern question is UNSAT, has a ground-truthed
  source-weakened question-mark mutation, and passed an exact-source Pydantic
  and Python gate over 2,632 inputs. It adds one local runnable gate, one
  product-engine replay, and 2,632 question-attributed differential cases.
- Aggregate useful-gate evidence is 27 local runnable gates, 48 product-engine
  replays, and 1,755,905 differential cases. Consumer-adopted gates remain
  zero.
- The SAT outcome overlay is unchanged: 14 ground-truthed candidates; confirmed
  security impacts, reports, maintainer confirmations, and third-party fixes
  remain zero. The new UNSAT question is not a bug finding.
- Contract provenance is 46 agent-derived and 7 human.

## Lineage and reproduction

`source-checkpoints.json` binds the aggregate to three exact checkpoint inputs:
the byte-identical v23 checkpoint, the Tracecat workspace-sync checkpoint from
v24, and the new RBAC-scope P6 runner's v3 checkpoint. The copied v23 input
retains SHA-256
`b031de9cc13deabbc0a26897fa7429bbba3298d5a4466a60f01f8e00a1201761`; the
copied workspace-sync input retains SHA-256
`b38c1964d2ab6af6ad9bd42d2da19137f180dcdf5948e424225511bd860897fe`. The
frozen v22 and prior additive checkpoints remain preserved in their original
directories.

Rebuild with the exact-pin v5 inventory:

```sh
.venv/bin/python scripts/build-p2-evidence-checkpoint.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-16-p2-source-inventory-v5/inventory.json \
  --sites properties/calibration/2026-10-16-p2-source-inventory-v5/sites.ndjson \
  --checkpoint-root properties/calibration/2026-10-16-p2-checkpoint-input-v25 \
  --out-dir properties/calibration/2026-10-16-p2-existing-evidence-20r2-v25
```

`report.json`, `checkpoint.json`, `attempts.json`, `conversion.ndjson`,
`roster.json`, and `source-checkpoints.json` are the machine-readable result.
The source review and exact gate are documented in the [Tracecat RBAC scope
P6 bundle](../2026-10-16-autonomous-tracecat-rbac-scope-pattern/README.md).

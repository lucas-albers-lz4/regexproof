# P2 retrospective evidence checkpoint v22

This checkpoint aggregates retrospective, exact-pin product attempts against
the frozen 20-r2 cohort and corrected v5 source inventory. It does not select
a prospective sample or establish yield for unreviewed sites.

## Result

- 50 eligible questions asked; the 50-question evaluation checkpoint is
  reached. This is an evaluation sample size, not a success threshold.
- 49 questions are decided: 35 UNSAT guarantees and 14 ground-truthed SAT
  candidates. One additional question timed out and remains **not proven**.
- The frozen disposition column still says `pending_product_triage` for all 14
  SAT rows. The later [v11 outcome overlay](../2026-10-16-p2-sat-impact-triage-v11/README.md)
  covers them separately: two refuted claims and 12 product candidates across
  ten groups. Confirmed security impacts, consumer-adopted gates, external
  reports, maintainer confirmations, and third-party fixes remain zero.
- Useful gate evidence includes 24 local runnable gates, 45 product-engine
  replays, and 1,748,337 question-attributed differential cases. These counts
  measure contract-backed proof and regression evidence; they do not imply a
  confirmed bug or external outcome.
- Contract provenance is 43 autonomous and 7 human. The 100-question target
  remains 50 questions short.

Compared with v21, this adds one exact-pin Aidevops question. Three questions
have UNSAT results; the full slug-helper inclusion question timed out at 30
seconds. Its finite Bash/product comparisons are useful regression evidence,
but do not prove the unbounded inclusion claim. The new gate contributes one
local runnable gate, four product-engine replays, and 719 question-attributed
differential cases.

## Evidence files

- `report.json`: aggregate counts, target status, provenance, and interval
  metadata.
- `checkpoint.json`: versioned checkpoint and frozen product roster.
- `attempts.json`: every joined attempt, including the timeout and pending SAT
  dispositions.
- `source-checkpoints.json`: source identity and checkpoint lineage.
- `conversion.ndjson`: the conversion rows included in the aggregate.

To validate the checkpoint report:

```bash
.venv/bin/python scripts/conversion-checkpoint.py \
  properties/calibration/2026-10-16-p2-existing-evidence-20r2-v22/checkpoint.json
```

The underlying Aidevops source review and proof/gate details are in
[`2026-10-16-autonomous-aidevops-webhook-action-protocol-20r2`](../2026-10-16-autonomous-aidevops-webhook-action-protocol-20r2/review-memo.md).

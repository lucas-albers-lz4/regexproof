# P2 retrospective checkpoint v20

**Cohort:** `2026-09-12-calibration-20-r2`
**Source inventory:** [v5](../2026-10-16-p2-source-inventory-v5/README.md)
**Checkpoint schema:** 3

The strict retrospective join still contains **46 distinct eligible,
source-matched questions**: 32 UNSAT and 14 ground-truthed SAT. The 50-question
evaluation checkpoint is four questions short; it is a measurement checkpoint,
not a success threshold.

| Measure | Result |
|---|---:|
| Contract-backed decided proofs | 46 |
| Useful local regression gates | 23 |
| Product-engine replays | 41 |
| Question-attributed differential cases | 1,747,618 |
| Ground-truthed SAT witnesses | 14 |
| Excluded attempts | 5 across 3 questions |
| Confirmed security impact / external reports / fixes | 0 / 0 / 0 |

All 14 SAT questions remain pending product triage. The five excluded attempts
are unchanged: three source sites are outside the declared P2 dialect inventory
and two Json Editor attempts have ambiguous line-only selectors. Contract
provenance is 39 autonomous and 7 human; agent provenance remains truthful.

This is a retrospective evidence join, not new prospective yield. The v5 raw
inventory adds Bash sites and repairs 26 truncated Bash source records, but none
of those rows was added to this checkpoint's eligibility or question count.
The checkpoint was validated with `scripts/conversion-checkpoint.py`.

Files: `checkpoint.json`, `attempts.json`, `conversion.ndjson`, `roster.json`,
`source-checkpoints.json`, and `report.json`.

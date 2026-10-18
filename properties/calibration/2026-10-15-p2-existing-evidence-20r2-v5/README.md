# 20-r2 compatible existing product evidence v5

This is a **retrospective** aggregate of exact-cohort product evidence joined
to the corrected P2 source inventory. It is not a prospective sample, a new
review wave, or an estimate of conversion yield.

## Snapshot

- Frozen cohort: `2026-09-12-calibration-20-r2`, manifest digest
  `5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d`.
- Inventory: 20,784 raw sites across 19 complete repositories and one
  repository with six unavailable submodules.
- Compatible evidence: 21 unique exact-pin questions; 15 UNSAT and six
  ground-truthed SAT witnesses with persisted product replays. All six SAT
  candidates are pending product impact triage.
- Contract provenance: 14 autonomous and seven historical human contracts.
- Useful local gates: 10. Product-engine replays: 16. Differential cases:
  46,321.
- Consumer-adopted gates, confirmed security impacts, authorized external
  reports, maintainer confirmations, and fixes: zero.
- The strict checkpoint is 21 of the 50-question target, a shortfall of 29.
  Three attempts remain excluded from the declared-dialect denominator.

The new Doberman-Core question is an autonomously adopted contract for the
Windows-path secret-store classifier at the exact frozen source pin. Its
formal counterexample and pinned Python/product-rule replay show that native
backslash paths to `.npmrc` and `credentials` return `PASS`. The local gate
also checks slash-separated controls, a separator-fix sensitivity control,
and refutes `.env.local` as a separate candidate because the default
`.env.*` protected-path rule covers it. The gate ran on Linux with
Windows-shaped path strings; native Windows path canonicalization was not
exercised. This candidate remains pending product triage and no report was
sent. Details and reproduction commands are in the
[Doberman calibration](../2026-10-15-autonomous-doberman-win-secret-path-20r2/README.md).

Two older Doberman-Core human-contract rows are also included. Their exact
pins and file/line anchors join the frozen P2 inventory, and both persist
replayed SAT witnesses, but neither legacy row carries evidence for a reusable
local gate. The newly imported Doberman question is a third canonical row and
does have a local gate. Six exact-cohort Forge CLI canonical rows match
questions already in the checkpoint; they are recorded as corroboration and
do not increase the denominator. Earlier aggregate snapshots are preserved,
and sidecar markers prevent them from being rediscovered as source runs.

The refreshed [question-history index](../question-history-index.json) covers
168 sources, 73 asked sites, 128 reserved sites, and seven unbound legacy
records. This is a history/dedup index, not allocation evidence. The latest
[agent-only scorecard](../2026-10-15-autonomous-scorecard-20r2-after-doberman-proof-gate.json)
has 14 timed run records and 18 proof attempts (17 decided: 13 UNSAT and four
SAT), 15 local gates, 16 mutation checks, and 252,590 differential cases.
The Doberman proof/gate replay adds one execution retry but no new product
question to this v5 denominator. Its measured proof/gate interval was 0.811
seconds; full review/adoption time, tokens, cost, and human active time remain
unknown. Scorecard SAT rows count executions/retries and do not imply four
distinct root causes.

## Reproduction

```sh
.venv/bin/python scripts/build-p2-evidence-checkpoint.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-15-p2-source-inventory-v2/inventory.json \
  --sites properties/calibration/2026-10-15-p2-source-inventory-v2/sites.ndjson \
  --checkpoint-root properties/calibration \
  --conversion-root properties/generated \
  --repo-root /home/lalbers/gitroot/regexproof \
  --out-dir properties/calibration/2026-10-15-p2-existing-evidence-20r2-v5

.venv/bin/python scripts/conversion-checkpoint.py \
  properties/calibration/2026-10-15-p2-existing-evidence-20r2-v5/checkpoint.json
```

## Evaluation tracks

| Track | Current evidence | What it measures |
|---|---|---|
| Useful proofs and gates | 21 decided contract-backed questions, 10 local gates, 16 product replays, 46,321 differential cases | Faithful properties and regression evidence; aggregate questions are deduplicated by product identity. |
| Bug discovery | Six SAT candidates, all six replayed; six pending product triage; zero confirmed security impacts | Counterexample candidates through real-code replay and product-impact classification. |
| External outcomes | Zero reports, maintainer confirmations, or fixes | Only authorized reports actually sent and independently evidenced outcomes. |

The cohort is selected and its idiom members are correlated. The checkpoint's
intervals are descriptive for these asked questions; they do not estimate
population bug prevalence. Crossing the 50-question checkpoint alone is not a
claim that the approach works. The investment decision still needs the
prespecified quality and resource criteria described in
[`docs/AUTONOMOUS-CORPUS-PLAN.md`](../../../docs/AUTONOMOUS-CORPUS-PLAN.md).

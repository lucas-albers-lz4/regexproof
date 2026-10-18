# 20-r2 compatible existing product evidence v18

This is a retrospective aggregate of exact-pin product questions in the
frozen `2026-09-12-calibration-20-r2` cohort. It is not a prospective sample
or a yield estimate.

## Snapshot

- Frozen manifest digest: `5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d`.
- Inventory v3: 20,705 raw sites across 19 complete repositories and one
  repository with six unavailable submodules.
- Compatible evidence: **45** unique source-matched product questions: **32
  UNSAT** and **13 ground-truthed SAT**. The SAT rows remain pending product
  triage.
- Contract provenance: 38 autonomous and seven historical human contracts.
- Useful local regression gates: 22. Product-engine replays: 40.
  Question-attributed differential cases: 1,747,618.
- Consumer-adopted gates, confirmed security impacts, external reports,
  maintainer confirmations, and third-party fixes: zero.
- The checkpoint remains below the 50-question evaluation checkpoint by
  **5**. Fifty is an evaluation checkpoint, not a success threshold.
- Five prior attempts across three identities remain excluded: three sites
  are outside the declared inventory dialect and two Json Editor attempts
  have ambiguous line-only selectors.

The v17-to-v18 increment is the first serial P7 Aidevops
`pre-dispatch-github-text` wave. Fifteen source sites were reviewed, one
contract was adopted, and 14 sites were skipped with source-backed reasons.
The cited-file counterexample replay reads only a local fixture outside the
mock clone; it does not demonstrate data disclosure or confirmed impact. See
the [P7 wave bundle](../2026-10-16-autonomous-aidevops-predispatch-github-text-20r2/README.md).

## Source-review coverage

Eleven completed repository slices cover 441 source sites: 315 skips, 102
unresolved, and 24 adopted contracts. Separate targeted reviews cover
Tracecat's two validator rows and two Real-Router rows (route-segment and
navigation-parameter). The P7 Aidevops wave adds 15 source-bound review
decisions and one adopted contract. These targeted reviews do not imply
full-repository coverage.

## Downstream outcomes and effort

The v10 SAT-impact overlay previously covered 12 SAT rows. V18 adds a
ground-truthed Aidevops SAT counterexample pending product triage; no
downstream impact is confirmed. Confirmed security impacts and external
outcomes remain zero.

The separate post-proof scorecard is preserved at
[`../2026-10-16-autonomous-scorecard-20r2-after-predispatch.json`](../2026-10-16-autonomous-scorecard-20r2-after-predispatch.json).
It reports run-level throughput, useful contract-backed proofs/gates, local
bug discovery, and external outcomes separately; these run counts are not the
unique-question counts above. The latest proof-only row records one replayed
reachable violation and zero confirmed impacts. Token use, cost, and human
active time remain unknown.

The [post-outcome history index](../2026-10-16-question-history-index-after-predispatch.json)
covers 338 source artifacts, 77 asked identities, 622 reserved sites, and
seven unbound records. It prevents duplicate work but is not allocation
evidence.

## Reproduction

```sh
.venv/bin/python scripts/build-p2-evidence-checkpoint.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-15-p2-source-inventory-v3/inventory.json \
  --sites properties/calibration/2026-10-15-p2-source-inventory-v3/sites.ndjson \
  --checkpoint-root properties/calibration \
  --conversion-root properties/generated \
  --repo-root . \
  --out-dir properties/calibration/2026-10-16-p2-existing-evidence-20r2-v18

.venv/bin/python scripts/conversion-checkpoint.py \
  properties/calibration/2026-10-16-p2-existing-evidence-20r2-v18/checkpoint.json

.venv/bin/python scripts/autonomous-scorecard.py \
  --cohort-id 2026-09-12-calibration-20-r2 --json
```

# 20-r2 compatible existing product evidence v17

This is a retrospective aggregate of exact-pin product questions in the
frozen `2026-09-12-calibration-20-r2` cohort. It is not a prospective sample
or a yield estimate.

## Snapshot

- Frozen manifest digest: `5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d`.
- Inventory v3: 20,705 raw sites across 19 complete repositories and one
  repository with six unavailable submodules.
- Compatible evidence: **44** unique source-matched product questions: **32
  UNSAT** and **12 ground-truthed SAT**. The SAT rows remain pending product
  triage.
- Contract provenance: 37 autonomous and seven historical human contracts.
- Useful local regression gates: 21. Product-engine replays: 39.
  Question-attributed differential cases: 1,747,618.
- Consumer-adopted gates, confirmed security impacts, external reports,
  maintainer confirmations, and third-party fixes: zero.
- The checkpoint remains below the 50-question evaluation checkpoint by **6**.
  Five attempts across three identities are excluded: three sites are outside
  the declared inventory dialect and two Json Editor attempts have ambiguous
  line-only selectors.

The v16-to-v17 increment is one Real-Router navigation-parameter control
character invariant. The targeted source review, adopted config-trust
contract, exact-source replay, and singleton P6 lifecycle evidence are in the
[review and P6 bundle](../2026-10-16-p2-real-router-navigation-source-review/README.md).
The guarantee concerns application-supplied values to an opt-in validator;
the cohort's GO decision is scale-based and does not establish remote attacker
reachability or security impact.

## Source-review coverage

Eleven completed repository slices cover 441 source sites: 315 skips, 102
unresolved, and 24 adopted contracts. Separate targeted reviews cover
Tracecat's two validator rows and two Real-Router rows (route-segment and
navigation-parameter). Together, 445 exact inventory sites have been
individually reviewed and 28 contracts adopted. The targeted reviews do not
imply full-repository coverage.

## Downstream outcomes and effort

The v10 SAT-impact overlay still applies because v17 adds only an UNSAT
question. It covers the same 12 SAT rows; the Tracecat terminal-LF candidate
remains unconfirmed pending downstream consequence evidence. Confirmed
security impacts and external outcomes remain zero.

The separate post-run scorecard is preserved at
[`../2026-10-16-autonomous-scorecard-20r2-after-navigation-control.json`](../2026-10-16-autonomous-scorecard-20r2-after-navigation-control.json).
It reports run-level throughput, useful contract-backed proofs/gates, local
bug discovery, and external outcomes separately; these run counts are not the
unique-question counts above. Resource totals, including the latest row, leave
token use, cost, and human active time unknown.

The [post-outcome history index](../2026-10-16-question-history-index-after-navigation-control.json)
covers 324 recognized artifacts, 76 asked identities, 576 reserved sites,
and seven unbound records. It prevents duplicate work but is not allocation
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
  --out-dir properties/calibration/2026-10-16-p2-existing-evidence-20r2-v17

.venv/bin/python scripts/conversion-checkpoint.py \
  properties/calibration/2026-10-16-p2-existing-evidence-20r2-v17/checkpoint.json
```

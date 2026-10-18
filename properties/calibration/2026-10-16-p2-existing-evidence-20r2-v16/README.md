# 20-r2 compatible existing product evidence v16

This is a retrospective aggregate of exact-pin product questions in the
frozen `2026-09-12-calibration-20-r2` cohort. It is not a prospective sample
or a yield estimate.

## Snapshot

- Frozen manifest digest: `5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d`.
- Inventory v3: 20,705 raw sites across 19 complete repositories and one
  repository with six unavailable submodules.
- Compatible evidence: **43** unique source-matched product questions: **31
  UNSAT** and **12 ground-truthed SAT**. The SAT rows remain pending product
  triage.
- Contract provenance: 36 autonomous and seven historical human contracts.
- Useful local regression gates: 20. Product-engine replays: 38.
  Question-attributed differential cases: 1,730,604.
- Consumer-adopted gates, confirmed security impacts, external reports,
  maintainer confirmations, and third-party fixes: zero.
- The checkpoint remains below the 50-question evaluation checkpoint by **7**.
  Five attempts across three identities are excluded: three sites are outside
  the declared inventory dialect and two Json Editor attempts have ambiguous
  line-only selectors.

The v15-to-v16 increment is one Real-Router route-segment alphabet invariant.
It is a targeted review of one row at the exact cohort pin, not a full
Real-Router source review. The source documents the ASCII alphabet; the
contract, proof, source mutation, and Node differential gate are in the
[Real-Router bundle](../2026-10-16-p2-real-router-segment/README.md). The
cohort admission decision for Real-Router was scale-based, and this result
does not claim that the repository is a security tool or that the invariant
blocks an attacker.

## Source-review coverage

Eleven completed repository slices cover 441 source sites: 315 skips, 102
unresolved, and 24 adopted contracts. Three separate targeted reviews cover
Tracecat's two validator rows and the Real-Router segment row. Together, 444
exact inventory sites have been individually reviewed and 27 contracts
adopted. The targeted reviews do not imply full-repository coverage.

## Downstream outcomes and effort

The v10 SAT-impact overlay still applies because v16 adds only an UNSAT
question. It covers the same 12 SAT rows; the Tracecat terminal-LF candidate
remains unconfirmed pending downstream consequence evidence. Confirmed
security impacts and external outcomes remain zero.

The separate post-run scorecard records 25 run rows, 39 proof attempts, 38
decided questions, 31 UNSAT guarantees, seven SAT candidates and replays,
seven reachable local violations, 25 local gates, and zero confirmed impacts.
Its aggregate is a run-measurement view and uses different counting units
from this unique-question checkpoint. Cost, token use, and human active time
are unknown. The [frozen scorecard](../2026-10-16-autonomous-scorecard-20r2-after-real-router.json)
keeps useful proofs/gates, bug discovery, and external outcomes in separate
tracks.

The [post-outcome history index](../2026-10-16-question-history-index-after-real-router.json)
covers 307 recognized sources, 75 asked identities, 574 reserved sites, and
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
  --out-dir properties/calibration/2026-10-16-p2-existing-evidence-20r2-v16

.venv/bin/python scripts/conversion-checkpoint.py \
  properties/calibration/2026-10-16-p2-existing-evidence-20r2-v16/checkpoint.json
```

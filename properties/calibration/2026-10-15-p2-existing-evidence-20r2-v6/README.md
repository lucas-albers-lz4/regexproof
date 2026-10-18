# 20-r2 compatible existing product evidence v6

This is a retrospective aggregate of exact-cohort product evidence joined to
the corrected P2 source inventory. It is not a prospective sample, a new
15-site review wave, or an estimate of conversion yield.

## Snapshot

- Frozen cohort: `2026-09-12-calibration-20-r2`, manifest digest
  `5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d`.
- Inventory: 20,784 raw sites across 19 complete repositories and one
  repository with six unavailable submodules.
- Compatible evidence: 22 unique exact-pin questions; 16 UNSAT and six
  ground-truthed SAT witnesses with persisted product replays. All six SAT
  candidates remain pending product-impact triage.
- Contract provenance: 15 autonomous and seven historical human contracts.
- Useful local gates: 11. Product-engine replays: 17. Differential cases:
  47,328.
- Consumer-adopted gates, confirmed security impacts, authorized external
  reports, maintainer confirmations, and fixes: zero.
- The strict checkpoint is 22 of the 50-question target, a shortfall of 28.
  Three attempts remain excluded from the declared-dialect denominator.

## New Xibo calibration

The added question is the exact-pinned OAuth consent CSRF-cookie capture in
`xibosignage/xibo-cms@978def55c8e68cab3a50a7ee4725039da753f0a1`. Its
contract-backed character-class property is UNSAT; a capture-widening
mutation is SAT and is ground-truthed against the real TypeScript helper in
Node. The helper agrees with an independent cookie-pair parser on 1,000
generated valid-token cookie strings plus seven negative and edge controls.
The gate checks four exact-pinned source files and runs in the
CI proof job.

This establishes a narrow extraction invariant, not a vulnerability. The P2
extractor does not encode the full expression (`per-alternative-anchor`), so
the formal claim covers the exact capture body `[^;]` over ASCII characters,
without a string-length bound; full JavaScript search behavior is checked by
the exact-source product replay and differential cases. The replay does not
launch a browser or the PHP application and does not formalize duplicate
cookie-name ordering. Security impact is not confirmed. Details, the
digest-bound contract, proof, gate report, and reproduction commands are in
the [Xibo calibration](../2026-10-15-autonomous-xibo-csrf-cookie-20r2/README.md).

## Evaluation tracks

| Track | Current evidence | What it measures |
|---|---|---|
| Useful proofs and gates | 22 decided contract-backed questions, 11 local gates, 17 product replays, 47,328 differential cases | Faithful properties and regression evidence; aggregate questions are deduplicated by exact product identity. |
| Bug discovery | Six SAT candidates, all six replayed; six pending product triage; zero confirmed security impacts | Counterexample candidates through real-code replay and product-impact classification. |
| External outcomes | Zero reports, maintainer confirmations, or fixes | Only authorized reports actually sent and independently evidenced outcomes. |

The agent-only scorecard separately records 15 timed runs and 19 proof
attempts (18 decided: 14 UNSAT and four SAT executions), 16 local gates, 17
mutation checks, and 253,597 differential cases. The Xibo run took 1.073
phase-sum seconds for the proof-and-gate stage. It adds one execution, not an
additional question beyond the strict checkpoint. Full review/adoption time,
tokens, cost, and human active time are unknown. Four SAT executions across
the run history do not imply four additional distinct root causes. See the
[agent-only scorecard](../2026-10-15-autonomous-scorecard-20r2-after-xibo-csrf.json).

The refreshed question-history index covers 176 sources, 74 asked sites, 129
reserved sites, and seven unbound legacy records. It is a deduplication and
allocation-history artifact, not allocation evidence. Earlier aggregate
snapshots remain preserved.

## Reproduction

```sh
.venv/bin/python scripts/build-p2-evidence-checkpoint.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-15-p2-source-inventory-v2/inventory.json \
  --sites properties/calibration/2026-10-15-p2-source-inventory-v2/sites.ndjson \
  --checkpoint-root properties/calibration \
  --conversion-root properties/generated \
  --repo-root /home/lalbers/gitroot/regexproof \
  --out-dir properties/calibration/2026-10-15-p2-existing-evidence-20r2-v6

.venv/bin/python scripts/conversion-checkpoint.py \
  properties/calibration/2026-10-15-p2-existing-evidence-20r2-v6/checkpoint.json
```

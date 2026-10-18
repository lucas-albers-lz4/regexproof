# 20-r2 compatible existing product evidence v3

This is a **retrospective** aggregate of exact-cohort product checkpoints
matched to the corrected P2 source inventory. It is not a prospective sample,
a new review wave, or an estimate of conversion yield.

## Snapshot

- Frozen cohort: `2026-09-12-calibration-20-r2`, manifest digest
  `5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d`.
- Inventory: 20,784 raw sites across 19 complete repositories and one
  repository with six unavailable submodules.
- Compatible evidence: 18 unique exact-pin questions; 15 UNSAT and three
  reproduced SAT witnesses, all three pending product-impact triage.
- Contract provenance: 13 autonomous and five historical human contracts.
- Useful local gates: 9. Product-engine replays: 13. Differential cases:
  46,321.
- Consumer-adopted gates, external reports, maintainer confirmations, and
  fixes: zero.
- The strict checkpoint is 18 of the 50-question target, a shortfall of 32.

The AutoAR phase-key question adds one contract-backed UNSAT property and
local path-safety regression gate. Its mutation guard shows that allowing dot
and slash through the regex reproduces a traversal from the `phase-logs`
directory. The contract does not cover `scanID` or the results root. The three
SAT questions remain pending triage; zero confirmed security impacts are
reported by the separate autonomous scorecard.

Three attempts remain visible but are excluded from this declared-dialect
count: two AutoAR HTML-escaper attempts (one failed runner attempt and its
later passing UNSAT run) and one Malcontent YARA rule. Earlier v1 and v2
aggregates are preserved. The builder recognizes each aggregate from its
sibling `source-checkpoints.json` manifest and excludes it from future source
input discovery.

## Reproduction

```sh
.venv/bin/python scripts/build-p2-evidence-checkpoint.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-15-p2-source-inventory-v2/inventory.json \
  --sites properties/calibration/2026-10-15-p2-source-inventory-v2/sites.ndjson \
  --checkpoint-root properties/calibration \
  --repo-root /home/lalbers/gitroot/regexproof \
  --out-dir properties/calibration/2026-10-15-p2-existing-evidence-20r2-v3

.venv/bin/python scripts/conversion-checkpoint.py \
  properties/calibration/2026-10-15-p2-existing-evidence-20r2-v3/checkpoint.json
```

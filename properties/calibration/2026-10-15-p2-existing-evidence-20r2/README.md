# 20-r2 compatible existing product evidence

This is a **retrospective** aggregate of the exact-cohort checkpoint artifacts
currently present under `properties/calibration/`. It joins each question to
the independent P2 source inventory by repository, pin, source file, and line.
It is not a prospective sample, a new review wave, or an estimate of
conversion yield.

## Snapshot

- Frozen cohort: `2026-09-12-calibration-20-r2`, manifest digest
  `5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d`.
- P2 source inventory: 20,779 raw sites from 19 complete repositories; one
  repository is marked incomplete because six gitlinks have no usable
  submodule mapping. These rows still carry no boundary review or trust class.
- Compatible evidence: 16 unique contract questions at exact pinned source
  sites: 13 UNSAT and 3 SAT. Provenance is 11 agent-derived and 5 historical
  human contracts.
- The SAT questions reproduce an AutoAR cross-origin loopback script fetch,
  a Malcontent author-metadata value that emits a second HTTPS Markdown link,
  and a third-party description value that emits a raw link and table
  delimiter. All three are reachable in exact product replay; downstream
  security impact remains unconfirmed and all dispositions are
  `pending_product_triage`.
- The aggregate has seven unique useful local regression gates, eleven
  product-engine replays, and 44,972 differential-case executions. Consumer
  adoption, external reports, maintainer confirmations, and fixes are all 0.
- The strict checkpoint reports 16 of the 50-question target, a shortfall of
  34. This is an observed-evidence count, not a coverage limit: most source
  rows remain unreviewed.

Three attempts remain visible in `source-checkpoints.json` and are excluded
from this declared-dialect checkpoint because their source sites are not in the
cohort member's P2 dialect inventory: AutoAR's HTML escaper (one failed runner
attempt followed by one passing UNSAT run) and Malcontent's YARA rule. They are
still exact-pin evidence in their own calibration artifacts. No failed status
was rewritten as a pass or dropped from the source record. The two Malcontent
metadata rows are independently in the declared Go-regex inventory and are
included as the fifteenth and sixteenth questions.

## Reproduction

The builder discovers `checkpoint.json` files under the calibration root,
validates those bound to the frozen 20-r2 manifest, verifies their contract
identities against the declared-dialect source inventory, and writes a
versioned roster, attempts, checkpoint, report, and input-digest manifest.

```sh
.venv/bin/python scripts/build-p2-evidence-checkpoint.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-15-p2-source-inventory/inventory.json \
  --sites properties/calibration/2026-10-15-p2-source-inventory/sites.ndjson \
  --checkpoint-root properties/calibration \
  --repo-root /home/lalbers/gitroot/regexproof \
  --out-dir properties/calibration/2026-10-15-p2-existing-evidence-20r2

.venv/bin/python scripts/conversion-checkpoint.py \
  properties/calibration/2026-10-15-p2-existing-evidence-20r2/checkpoint.json
```

Primary artifacts:

- `source-checkpoints.json` — frozen input digests, exact source-site joins,
  and excluded out-of-dialect attempts.
- `roster.json`, `attempts.json`, `checkpoint.json`, and `report.json` — the
  contract-hash roster and strict v3 funnel result.
- `conversion.ndjson` — the matched canonical proof rows.

The aggregate does not mark the remaining inventory rows as product candidates.
P2 still needs source-bound review/skip coverage for the other cohort members,
complete disposition of all reviewed candidates, and explicit treatment of
Everclaw's unresolved submodules. Malcontent now has a complete 15-site raw
review, but two sites remain unresolved and only two product questions were
asked from this member. P7 still needs prospective work; this retrospective
aggregate does not complete a 15/5 wave or reach the 50-question checkpoint.

# 20-r2 compatible existing product evidence v13

This retrospective checkpoint joins existing exact-pin product evidence to
the corrected v3 inventory. It is not a prospective sample or an estimate of
future conversion yield.

## Snapshot

- Frozen cohort: `2026-09-12-calibration-20-r2`, manifest digest
  `5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d`.
- Inventory: 20,705 raw sites across 19 complete repositories and one
  repository with six unavailable submodules. Inventory v3 removes 79
  JavaScript hashbang false positives from v2.
- Compatible evidence: **40** unique exact-pin product questions; **29
  UNSAT** and **11 ground-truthed SAT**. The SAT rows remain pending product
  triage.
- Contract provenance: 33 autonomous and seven historical human contracts.
- Useful local regression gates: 17. Product-engine replays: 35.
  Question-attributed differential cases: 1,711,421.
- Consumer-adopted gates, confirmed security impacts, external reports,
  maintainer confirmations, and third-party fixes: zero.
- The checkpoint is 40 of the 50-question target, a shortfall of 10. Five
  attempts across three questions are excluded: three source sites are outside
  the declared P2 inventory and two Json Editor attempts use an ambiguous
  line-only selector.

The separate [run-level scorecard](../2026-10-15-autonomous-scorecard-20r2-after-doberman.json)
summarizes 22 logged runs and 36 proof attempts. It keeps throughput, useful
proof/gate output, and downstream bug/external outcomes separate from the
checkpoint's 40 unique product-question denominator.

The v12-to-v13 increment adds two Doberman Codex apply_patch path-extraction
questions, both UNSAT, and one exact-source local gate. The formal contracts
cover one-character printable-ASCII destinations. The AST replay gate
compares the pinned `_apply_patch_paths` and `to_normalize_input` helper code
against 514 directive cases, including longer sample paths, indentation,
CRLF, and a mixed multi-directive envelope. A source-weakened Delete mutation
is SAT and ground-truthed. These results do not prove unbounded path
completeness or the correctness of every protected-path rule. The full
Doberman adapter could not be imported because Pydantic is absent in the
local environment; the gate uses the exact source AST subset and standard
library.

## P2 source-review coverage

Eleven selected repository slices have complete source-review artifacts; this
does not cover the full 20-member cohort.

| Repository slice | Sites | Skips | Unresolved | Adopted |
|---|---:|---:|---:|---:|
| Malcontent Go regexes | 15 | 11 | 2 | 2 |
| Anax Go regexes | 26 | 15 | 10 | 1 |
| AutoAR Go regexes | 34 | 28 | 3 | 3 |
| llm-honeypot POSIX shell | 16 | 14 | 0 | 2 |
| Panther Python regexes | 45 | 44 | 0 | 1 |
| Inhale Python regexes | 3 | 0 | 1 | 2 |
| BinaryAlert Python regexes | 1 | 1 | 0 | 0 |
| Snyk LS Go regexes | 37 | 36 | 1 | 0 |
| Json Editor ECMA regexes | 96 | 94 | 1 | 1 |
| Magic JS ECMA regexes | 64 | 53 | 1 | 10 |
| Doberman Core Python regexes | 104 | 19 | 83 | 2 |
| **Total** | **441** | **315** | **102** | **24** |

Unresolved rows remain outside product-question counts. The source review
does not infer completeness for Doberman's shell-command and destructive
operation heuristics from their security-facing call sites.

## Downstream candidate overlay

The separate [v9 SAT impact triage](../2026-10-15-p2-sat-impact-triage-v9/README.md)
remains applicable because v13 adds no SAT product question. It refutes two
historical Doberman claims and retains nine candidate questions across seven
issue families. All eleven SAT rows remain pending in the strict checkpoint.
Confirmed impact and external outcomes remain zero.

## Reproduction

```sh
.venv/bin/python scripts/build-p2-evidence-checkpoint.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-15-p2-source-inventory-v3/inventory.json \
  --sites properties/calibration/2026-10-15-p2-source-inventory-v3/sites.ndjson \
  --checkpoint-root properties/calibration \
  --conversion-root properties/generated \
  --repo-root . \
  --out-dir properties/calibration/2026-10-15-p2-existing-evidence-20r2-v13

.venv/bin/python scripts/conversion-checkpoint.py \
  properties/calibration/2026-10-15-p2-existing-evidence-20r2-v13/checkpoint.json
```

Exact identities, attempts, and source joins are in `checkpoint.json`,
`attempts.json`, and `source-checkpoints.json`; aggregate metrics are in
`report.json`. The v12 checkpoint remains a frozen historical snapshot.

# 20-r2 compatible existing product evidence v11

This is a retrospective aggregate of exact-cohort product evidence joined to
the corrected P2 source inventory. It is not a prospective sample, a ranked
15-site review wave, or an estimate of future conversion yield.

## Snapshot

- Frozen cohort: `2026-09-12-calibration-20-r2`, manifest digest
  `5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d`.
- Inventory: 20,784 raw sites across 19 complete repositories and one
  repository with six unavailable submodules.
- Compatible evidence: **28** unique exact-pin questions; **17 UNSAT** and
  **11 ground-truthed SAT**. All SAT rows remain pending product triage in the
  strict checkpoint.
- Contract provenance: 21 autonomous and seven historical human contracts.
- Useful local gates: 15. Product-engine replays: 23. Differential cases:
  1,229,873.
- Consumer-adopted gates, confirmed security impacts, external reports,
  maintainer confirmations, and third-party fixes: zero.
- The checkpoint is 28 of the 50-question target, a shortfall of 22. Three
  attempts remain excluded because their dialects are outside the declared P2
  inventory.

The v10-to-v11 increment is one source-matched Json Editor question: the
EnumEditor string replacement image is UNSAT, a source-weakened `<` mutation is
SAT and ground-truthed, and the exact pinned Node gate has zero mismatches over
1,116,985 cases. One local gate and one product-engine replay are added. The
contract is limited to application-configured schema enum string leaves and
the `display_area.innerHTML` text display path; it does not cover object keys or
other HTML contexts.

The three P6 executions are preserved under the
[Json Editor source-review bundle](../2026-10-15-p2-json-editor-source-review/README.md).
The first failed its local gate because of a command-construction quoting
error. The second passed the gate but used a line-level contract anchor that
matched three regexes in the inventory. The third used the exact source column
and is the source-matched product attempt counted here. All are retained; the
exact product question and useful gate are deduplicated once.

## P2 source review coverage

Nine selected repository slices have complete source-review artifacts; they do
not cover the full 20-member cohort:

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
| **Total** | **273** | **243** | **18** | **12** |

The unresolved sites include Inhale's same-origin prefix case, Snyk LS's hover
markup behavior, and Json Editor's Base64 preview MIME capture. Each lacks an
independent documented guarantee or source-established input trust needed to
adopt a product contract. None is counted in the product-question denominator.

## Downstream candidate overlay

The separate [v9 SAT impact triage](../2026-10-15-p2-sat-impact-triage-v9/README.md)
remains applicable because v11 adds no SAT product question. It refutes two
historical Doberman claims and retains nine candidate questions across seven
issue families. All eleven SAT rows remain pending in the strict checkpoint.
Confirmed impact and external outcomes remain zero.

## Reproduction

```sh
.venv/bin/python scripts/build-p2-evidence-checkpoint.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-15-p2-source-inventory-v2/inventory.json \
  --sites properties/calibration/2026-10-15-p2-source-inventory-v2/sites.ndjson \
  --checkpoint-root properties/calibration \
  --conversion-root properties/generated \
  --repo-root . \
  --out-dir properties/calibration/2026-10-15-p2-existing-evidence-20r2-v11

.venv/bin/python scripts/conversion-checkpoint.py \
  properties/calibration/2026-10-15-p2-existing-evidence-20r2-v11/checkpoint.json
```

Exact identities, attempts, and source joins are in `checkpoint.json`,
`attempts.json`, and `source-checkpoints.json`; summary metrics are in
`report.json`. The parent plan and source-review bundle link the proof, product
gate, mutation replay, P6 wave states, and timing records.

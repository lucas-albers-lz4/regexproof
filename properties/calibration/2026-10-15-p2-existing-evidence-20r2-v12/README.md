# 20-r2 compatible existing product evidence v12

This retrospective checkpoint joins existing product evidence to the
corrected v3 exact-pin inventory. It is not a prospective sample, a ranked
15-site review wave, or an estimate of future conversion yield.

## Snapshot

- Frozen cohort: `2026-09-12-calibration-20-r2`, manifest digest
  `5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d`.
- Inventory: 20,705 raw sites across 19 complete repositories and one
  repository with six unavailable submodules. Inventory v3 removes 79
  JavaScript hashbang false positives from v2.
- Compatible evidence: **38** unique exact-pin product questions; **27
  UNSAT** and **11 ground-truthed SAT**. The SAT rows remain pending product
  triage.
- Contract provenance: 31 autonomous and seven historical human contracts.
- Useful local regression gates: 16. Product-engine replays: 33. Distinct
  question-attributed differential cases: 1,710,907.
- Consumer-adopted gates, confirmed security impacts, external reports,
  maintainer confirmations, and third-party fixes: zero.
- The checkpoint is 38 of the 50-question target, a shortfall of 12. Three
  attempts remain excluded because their dialects are outside the declared
  P2 inventory.

The v11-to-v12 increment is ten source-matched Magic JS Base64URL output
questions. The ten per-codepoint Z3 image properties are UNSAT, and exact
Node replays report zero mismatches. The source-weakened `+` mutation is SAT
and reproduced. One reusable local gate is added; the question-attributed
replay counts sum to 481,034. Both P6 batches invoked the same full ten-question
gate, so the gate performed 962,068 comparisons across the two executions;
the checkpoint deduplicates the per-question evidence instead of counting the
repeat as new coverage. The two serial P6 phase sums total 2.0449 seconds.

The theorem is per input codepoint with no length bound. The finite Node replay
enumerates lengths zero, one, and two and seeded longer buffers for byte
encoder/DPoP paths; each PKCE chain is checked against its RFC vector and 2,048
seeded verifier digests. Five pinned TypeScript encoders and the React Native
DPoP encoder are imported directly. Three CryptoJS-dependent PKCE call sites and
the Provider DPoP call site are checked by parsing their exact pinned
replacement chains and applying them to Node-generated digests or bytes; the
CryptoJS package is unavailable in the pinned checkout, so those helper
modules are not imported. These results cover Base64URL output formatting,
not PKCE entropy, signature validity, authentication, or server acceptance.

## P2 source-review coverage

Ten selected repository slices have complete source-review artifacts; they do
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
| Magic JS ECMA regexes | 64 | 53 | 1 | 10 |
| **Total** | **337** | **296** | **19** | **22** |

The unresolved sites include Inhale's same-origin prefix case, Snyk LS's
hover markup behavior, Json Editor's Base64 preview MIME capture, and the
Magic JS wallet-kit email validator. Each lacks an independently documented
guarantee or source-established input trust needed to adopt a product
contract. None is counted in the product-question denominator.

## Downstream candidate overlay

The separate [v9 SAT impact triage](../2026-10-15-p2-sat-impact-triage-v9/README.md)
remains applicable because v12 adds no SAT product question. It refutes two
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
  --out-dir properties/calibration/2026-10-15-p2-existing-evidence-20r2-v12

.venv/bin/python scripts/conversion-checkpoint.py \
  properties/calibration/2026-10-15-p2-existing-evidence-20r2-v12/checkpoint.json
```

Exact identities, attempts, and source joins are in `checkpoint.json`,
`attempts.json`, and `source-checkpoints.json`; aggregate metrics are in
`report.json`. The earlier v11 checkpoint is preserved as a historical
snapshot built against inventory v2.

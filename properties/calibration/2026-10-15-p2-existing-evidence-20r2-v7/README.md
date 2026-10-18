# 20-r2 compatible existing product evidence v7

This is a retrospective aggregate of exact-cohort product evidence joined to
the corrected P2 source inventory. It is not a prospective sample, a ranked
15-site review wave, or an estimate of future conversion yield.

## Snapshot

- Frozen cohort: `2026-09-12-calibration-20-r2`, manifest digest
  `5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d`.
- Inventory: 20,784 raw sites across 19 complete repositories and one
  repository with six unavailable submodules.
- Compatible evidence: 24 unique exact-pin questions; 16 UNSAT and eight
  ground-truthed SAT. The strict report counts all eight SAT rows as pending
  product triage.
- Contract provenance: 17 autonomous and seven historical human contracts.
- Useful local gates: 12. Product-engine replays: 19. Differential cases:
  112,873.
- Consumer-adopted gates, confirmed security impacts, external reports,
  maintainer confirmations, and third-party fixes: zero.
- The checkpoint is 24 of the 50-question target, a shortfall of 26. Three
  attempts remain excluded because their dialects are outside the declared P2
  inventory.

The aggregate combines the prior v6 checkpoint with the LLM honeypot P6 run.
That run contributes two new contract-backed SAT questions, one local gate,
two product replays, and 65,545 sanitizer plus four Tor response cases. The
private-IP and Tor contracts are retrospective calibration and do not count as
prospective P7 yield.

## P2 review coverage

The source-review artifacts cover four selected repository slices, not the
entire inventory:

| Repository slice | Sites | Skips | Unresolved | Adopted |
|---|---:|---:|---:|---:|
| Malcontent Go regexes | 15 | 11 | 2 | 2 |
| Anax Go regexes | 26 | 15 | 10 | 1 |
| AutoAR Go regexes | 34 | 28 | 3 | 3 |
| llm-honeypot POSIX shell | 16 | 14 | 0 | 2 |
| **Total** | **91** | **68** | **15** | **8** |

The SAT impact overlay is separate from this strict checkpoint. It refutes two
historical Doberman terminal-LF security-bypass claims after source replay.
Four earlier candidates remain plausible, and the LLM honeypot slice adds two
more exact-source candidates: incomplete RFC 1918 redaction in a generated
artifact sync helper and success reporting based on an earlier Tor
AUTHENTICATE reply when SIGNAL NEWNYM fails. These are code-level candidates,
not confirmed security impact. No actual generated artifact or published
repository data was inspected, and no deployed Tor service or scan was
exercised. No external report was sent.

## Evaluation tracks

| Track | Current evidence | What it measures |
|---|---|---|
| Useful contract-backed proofs and regression gates | 24 decided questions, 12 useful local gates, 19 product replays, 112,873 differential cases | Contract quality and exact-engine regression evidence; questions are deduplicated by exact product identity. |
| Product bug candidates | Eight replayed SAT rows in the strict report; two historical claims separately refuted; six candidate questions remain | Counterexamples through real-code replay and product-impact triage. Confirmed impact remains zero. |
| External outcomes | Zero reports, maintainer confirmations, or fixes | Only reports sent with authorization and independently evidenced outcomes. |

The strict report's pending count is not overwritten by the separate curated
triage overlay. The two refuted rows therefore remain visible in the
checkpoint's source history and are represented as `false_positive` in the
curated disposition source.

## Reproduction

```sh
.venv/bin/python scripts/build-p2-evidence-checkpoint.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-15-p2-source-inventory-v2/inventory.json \
  --sites properties/calibration/2026-10-15-p2-source-inventory-v2/sites.ndjson \
  --checkpoint-root properties/calibration \
  --conversion-root properties/generated \
  --repo-root . \
  --out-dir properties/calibration/2026-10-15-p2-existing-evidence-20r2-v7

.venv/bin/python scripts/conversion-checkpoint.py \
  properties/calibration/2026-10-15-p2-existing-evidence-20r2-v7/checkpoint.json
```

The machine-readable accounting is in [`report.json`](report.json), with all
24 exact identities and attempts in [`checkpoint.json`](checkpoint.json).
The source review and the two new P6 candidate records are linked from the
[parent plan](../../../docs/AUTONOMOUS-CORPUS-PLAN.md).

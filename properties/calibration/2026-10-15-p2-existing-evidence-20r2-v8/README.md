# 20-r2 compatible existing product evidence v8

This is a retrospective aggregate of exact-cohort product evidence joined to
the corrected P2 source inventory. It is not a prospective sample, a ranked
15-site review wave, or an estimate of future conversion yield.

## Snapshot

- Frozen cohort: `2026-09-12-calibration-20-r2`, manifest digest
  `5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d`.
- Inventory: 20,784 raw sites across 19 complete repositories and one
  repository with six unavailable submodules.
- Compatible evidence: **25** unique exact-pin questions; **16 UNSAT** and
  **nine ground-truthed SAT**. All nine SAT rows remain pending product
  triage in this strict checkpoint.
- Contract provenance: 18 autonomous and seven historical human contracts.
- Useful local gates: 13. Product-engine replays: 20. Differential cases:
  112,882.
- Consumer-adopted gates, confirmed security impacts, external reports,
  maintainer confirmations, and third-party fixes: zero.
- The checkpoint is 25 of the 50-question target, a shortfall of 25. Three
  attempts remain excluded because their dialects are outside the declared
  P2 inventory.

The increment from v7 is one Panther staged-path question, one exact-helper
gate, one product-engine replay, and nine additional path cases. The Panther
P6 run records a SAT candidate with passing source verification, mutation
guard, and local gate; its wave status is `needs_review` until product-impact
disposition is settled. No Claude process or network request was used.

## P2 review coverage

The source-review artifacts cover five selected repository slices, not the
entire 20-member inventory:

| Repository slice | Sites | Skips | Unresolved | Adopted |
|---|---:|---:|---:|---:|
| Malcontent Go regexes | 15 | 11 | 2 | 2 |
| Anax Go regexes | 26 | 15 | 10 | 1 |
| AutoAR Go regexes | 34 | 28 | 3 | 3 |
| llm-honeypot POSIX shell | 16 | 14 | 0 | 2 |
| Panther Python regexes | 45 | 44 | 0 | 1 |
| **Total** | **136** | **112** | **15** | **9** |

The Anax transport follow-up supersedes its earlier skip count; the retained
raw inventory is 26 sites. The Panther contract is based on a separate slash
command's sensitive-path policy and the pre-commit helper's behavior. Whether
the slash-command policy is intended to govern that helper remains an
inference and is recorded as a candidate policy mismatch, not a confirmed
vulnerability.

## Downstream candidate overlay

The separate [v8 SAT impact triage](../2026-10-15-p2-sat-impact-triage-v8/README.md)
refutes two historical Doberman security-bypass claims and retains seven
candidate questions in six issue families. All seven need more product-impact
evidence. The strict checkpoint remains unchanged by this overlay and still
counts all nine SAT rows as pending product triage.

The previously identified limits still apply: Doberman native Windows
normalization and real secret reads were not exercised; AutoAR used harmless
loopback listeners; Malcontent Markdown consumers were not tested; the
llm-honeypot review inspected no generated publication and no live Tor
service; and Panther used only synthetic staged filenames/content. No
third-party contact was made.

## Evaluation tracks

| Track | Current evidence | What it measures |
|---|---|---|
| Useful contract-backed proofs and regression gates | 25 decided questions, 13 useful local gates, 20 product replays, 112,882 differential cases | Contract quality and exact-engine regression evidence; questions are deduplicated by exact product identity. |
| Product bug candidates | Nine replayed SAT rows; two historical claims refuted; seven candidate questions remain | Counterexamples through real-code replay and product-impact triage. Confirmed impact remains zero. |
| External outcomes | Zero reports, maintainer confirmations, or fixes | Only reports sent with authorization and independently evidenced outcomes. |

## Reproduction

```sh
.venv/bin/python scripts/build-p2-evidence-checkpoint.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-15-p2-source-inventory-v2/inventory.json \
  --sites properties/calibration/2026-10-15-p2-source-inventory-v2/sites.ndjson \
  --checkpoint-root properties/calibration \
  --conversion-root properties/generated \
  --repo-root . \
  --out-dir properties/calibration/2026-10-15-p2-existing-evidence-20r2-v8

.venv/bin/python scripts/conversion-checkpoint.py \
  properties/calibration/2026-10-15-p2-existing-evidence-20r2-v8/checkpoint.json
```

The exact identities and attempts are in [`checkpoint.json`](checkpoint.json)
and [`attempts.json`](attempts.json); summary metrics are in
[`report.json`](report.json). The source review, proof/gate, and P6 state are
linked from the [parent plan](../../../docs/AUTONOMOUS-CORPUS-PLAN.md).

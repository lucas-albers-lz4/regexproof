# Doberman Core exact-pin P2 review and Codex apply_patch calibration

This review covers all 104 Python regex sites in `fu351/Doberman-Core` at the
frozen 20-r2 pin `53ae43c5298a2426c6696147fdd75e2a4aef10e2`. The evidence
artifact records 19 evidence-backed skips, 83 unresolved sites, and two
adopted questions. The complete per-site decisions are in
[`reviews.json`](reviews.json), joined to pinned source in
[`evidence.json`](evidence.json).

## Review decision

The two adopted sites are `_APPLY_PATCH_FILE_RE` and `_APPLY_PATCH_MOVE_RE`
in `src/doberman/hosthooks/codex.py`. The repository's Codex fixture notes
document the `apply_patch` envelope and its Add, Update, Delete, and Move to
path directives. At this pin, `_apply_patch_paths` extracts the destinations;
`to_normalize_input` surfaces them as `file_write` targets for protected-path
evaluation. The tests include exact-helper extraction, indented CRLF handling,
and a multi-file `.env` block.

The formal contracts are intentionally narrower than the helper's apparent
behavior: the two Z3 theorems cover a one-character printable-ASCII path
destination, with zero to three leading spaces or tabs. The pinned helper gate
also checks longer representative paths, all three file directive verbs,
Move to, CRLF, and a mixed multi-directive envelope. Those finite replays are
regression evidence; they do not establish unbounded completeness for every
path string. The contract also does not establish filesystem canonicalization,
path-rule correctness, or enforcement outside this Codex adapter.

The adopted source-bound contracts are in [`contracts.json`](contracts.json).

The other security-facing command, secret, destructive-operation, and turn
gating heuristics remain unresolved where documentation does not define an
independent exact language or complete parser grammar. Their presence on a
pre-execution path is not evidence that they recognize every dangerous form.
Three exact Doberman sites already had product questions in the cohort and
were not counted again: Windows drive-root matching, disk-wipe detection, and
the Windows secret-store classifier. Test parsers, documentation lint, and
diagnostic version extraction were skipped with call-context evidence.

## P6 result

The two source-bound contracts are registered as product properties. Both
Z3 questions are UNSAT; the shared family mutation guard removes `Delete` from
the file regex, returns SAT for `*** Delete File: .env`, and reproduces the
miss with the exact pinned helper. The source-AST gate ran 514 differential
cases with zero mismatches: 385 attributed to Add/Update/Delete extraction
and 129 to Move-to extraction. These totals include a mixed multi-directive
case for each question's attribution. They are not 514 distinct sites or
unbounded proofs.

The gate executes the two regex assignments and the exact helper functions
from the pinned AST using Python's standard library. The checkout's complete
Doberman module could not be imported in this workspace because its Pydantic
dependency is absent, so this gate does not run the whole hook or
`ProtectedPathRule`. The repository's existing unit tests were reviewed as
source evidence but were not run as part of this gate.

The source gate is wired into the repository's `proof` CI job, and the normal
`z3-verify.py --all` step includes both product properties and the mutation
guard. The hosted CI result for this change has not been observed locally.

This wave adds two UNSAT questions, one local runnable gate, 514
question-attributed differential cases, and no SAT product candidate,
reachable violation, confirmed security impact, consumer-adopted gate,
external report, maintainer confirmation, or third-party fix. The agent run
log records the P6 phase sum as 0.9681 seconds; P2 review/contract-authoring
time and token/cost usage were not separately measured.

## Reproduction

```sh
.venv/bin/python scripts/build-p2-source-review-evidence.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-15-p2-source-inventory-v3/inventory.json \
  --sites properties/calibration/2026-10-15-p2-source-inventory-v3/sites.ndjson \
  --reviews properties/calibration/2026-10-15-p2-doberman-source-review/reviews.json \
  --checkout /tmp/regexproof-pinned-sources/Doberman-Core-53ae43c5298a2426c6696147fdd75e2a4aef10e2 \
  --repo-id fu351/Doberman-Core \
  --pin 53ae43c5298a2426c6696147fdd75e2a4aef10e2 \
  --output properties/calibration/2026-10-15-p2-doberman-source-review/evidence.json

.venv/bin/python scripts/z3-verify.py \
  DB-codex-apply-patch-file-target-path \
  DB-codex-apply-patch-move-target-path \
  DB-codex-apply-patch-weakened-file-regex-misses-delete \
  --require-ground-truth --json

.venv/bin/python scripts/doberman-codex-apply-patch-regression-gate.py \
  --source-root /tmp/regexproof-pinned-sources/Doberman-Core-53ae43c5298a2426c6696147fdd75e2a4aef10e2 \
  --roster properties/calibration/2026-10-15-p2-doberman-source-review/p6-wave/roster.json \
  --output properties/calibration/2026-10-15-p2-doberman-source-review/p6-wave/product-gate.json

.venv/bin/python scripts/run-autonomous-proof-wave.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --roster properties/calibration/2026-10-15-p2-doberman-source-review/p6-wave/roster.json \
  --state-dir properties/calibration/2026-10-15-p2-doberman-source-review/p6-wave/state \
  --wave-id doberman-codex-apply-patch \
  --corpus doberman_core_codex \
  --idiom-bucket codex-apply-patch-path-extraction \
  --checkout fu351/Doberman-Core=/tmp/regexproof-pinned-sources/Doberman-Core-53ae43c5298a2426c6696147fdd75e2a4aef10e2 \
  --gate properties/calibration/2026-10-15-p2-doberman-source-review/p6-wave/gate-config.json
```

The roster and state are frozen under [`p6-wave/`](p6-wave/). No external
maintainer, Codex service, or Doberman deployment was contacted.

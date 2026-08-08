# Changelog

All entries below cover the initial development cycle (2026-08-06 to
2026-08-08). No release tags exist yet. This changelog groups the work by
phase. Dates are merge dates.

## Foundations (2026-08-06)

- Initial release of the playbook and toolkit for Z3 regex verification.
- Added a security-only dependabot configuration and a CI gate.
- Fixed broken URLs and a stale per-token claim in the docs. Applied the
  simple-english prose pass.
- Added a curated ruff configuration, fixed lint findings, and added
  pre-commit hooks.
- Recorded pilot lessons: the Complement single-char nuance and whole-word
  gate greps.
- Made the CI link check fail on broken links. Removed `--no-fail`.
  Excluded hosts that block scripted clients.
- Added a `workflow_dispatch` trigger.

## Structural gates (2026-08-07)

- Added structural gates: `z3-solver==5.0.0` version pin, witness replay,
  mutation coverage, and the property `kind` taxonomy.
- Added `scripts/differential-fuzz.py` and the `--json` output mode.
- Documented TRAPS 13–15: `Re()` literal semantics, char-range boundaries,
  and the `Opt` alias.
- Pinned workflow permissions. Removed the trigger-test workflow.

## Dogfooding gaps P0–P2 (2026-08-08)

- Closed the case-insensitive mirror gap: `re.I` patterns need per-char case
  expansion (issue #11, gap 1).
- Closed the Unicode input-domain gap: `\w \d \s \b` are Unicode-aware in
  Python, ASCII-only in Z3 (issue #11, gap 2).
- Closed the dynamic-compiles gap: classify the site, then prove or file
  (issue #11, gap 3).

## Phase 1 — Compiler foundation (2026-08-07)

- Added the installable package with dialect compilers, the golden suite,
  and argv-only fuzz adapters.
- Fixed PCRE, CI, and extractor gate issues found by automated review.

## Phase 2 — Pilots (2026-08-07)

- Added the validator.js and gitleaks pilots: extract, compile, and
  property shapes 1–3 (issue #18).

## Phase 4 — ReDoS stage (2026-08-07)

- Added the isolated ReDoS runner, engine wrappers, and a CI job. Ran in
  parallel with Phase 3.
- Kept detector tool names on ReDoS wrapper transport failures.

## Phase 3 — Shape-5 rule_diff (2026-08-08)

- Added the shape-5 `rule_diff` pilot on the gitleaks encodable subset.
- Made `--require-ground-truth` a hard failure. Made redaction idempotent.

## Phase 5 — Batch mode (2026-08-08)

- Added batch mode: inventory, triage NDJSON, intent-vs-actual, and the
  disclosure gate.
- Fixed the batch pipeline: word-token intent and the shape-5 MD path.

## Phase 6 — CI integration (2026-08-08)

- Added CI gates: pinned toolchains, the NDJSON contract, and named merge
  blockers.

## Phase 7 — Docs (2026-08-08)

- Added the taxonomy, NDJSON contract, reporting, and disclosure docs.
- Clarified the secret-scanning wording. Required verified-finding markers.

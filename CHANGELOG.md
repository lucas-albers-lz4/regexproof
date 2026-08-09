# Changelog

All entries below cover the initial development cycle plus the 2026-08-08
dogfooding/corpus/fix waves. No release tags exist yet. This changelog groups
the work by phase; dates are merge dates.

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

## Dogfooding wave completion — CRS + validator.js (2026-08-08)

- Phase 1 CRS inventory (#42): ModSecurity `@rx` extractor (escaped-quote
  truncation regression-tested), `coreruleset` manifest + `--corpus
  coreruleset`, batch evidence fields (no hardcoded `N/A`;
  `engine_versions` on ReDoS findings).
- Completed the CRS + validator.js dogfooding wave P1–P5 (#46): 310-site CRS
  inventory and 1,597-site validator.js inventory; verified findings issue
  (facts-only) + separate toolkit-gap plan issue. CRS encodable 38.4% →
  44.5% after the lazy strip.
- Batch markdown findings carry full metadata (#48). Non-trivial PRs require
  Bugbot before merge (#47).

## Toolkit fixes — language-transparent encodability (#45, 2026-08-08)

- Lazy quantifiers are language-transparent for membership: `a*?` → `a*`
  (#49). The biggest single reject-bucket fix — CRS parse-errors 53 → 7;
  validator.js ~118 sites.
- Hex escapes `\xNN`/`\x{}` lower to codepoint literals instead of literal
  text — the mirror-fidelity repair (PR #49).
- Negated classes `[^...]` via BMP/ASCII range complement; scoped `(?i:…)`
  for PCRE/RE2; ECMA keeps scoped-`i` and `m`/`u`/`v`/`g`/`y`/`d` as
  explicit rejects (TRAPS #21–#22) (#50).
- `{1}` identity fix also on `py_re._repeat`; wave-gate regressions expanded.
- CRS encodable measured **206/318 (64.8%)** after the encode paths (was
  ~45% post-lazy/hex).

## Corpus wave — 10-corpus roster (#51–#61, 2026-08-08)

- Pre-gate (#58): mirror-fidelity differential-fuzz gate on encodable
  samples; pcre2 helper provisioning.
- Phase 1a (#59): trufflehog (215 rules), IDS rule sets suricata+snort3
  (8,171 rules), semgrep-rules (9,186 rules); new extractors (`go_regexp`,
  `ids_rules`, `semgrep_yaml`), sample corpora, cross-corpus matrix.
- Phase 1b (#60): testdata harness corpora — CPython `re` tests, busybox,
  PCRE2 testdata, RE2 testdata, rust-lang/regex (inventory-only by design).
- Phases 2–5 (#61): gitleaks re-measured to 82.4% on the fixed compiler;
  frozen-`regex_id` re-measure helper; residual-bucket a/b/c
  classification; rule_diff family semantics; TRAPS + final-report updates.

## Word-boundary wave (#62–#67, 2026-08-08)

- ASCII-domain `\b`/`\B` encoding for stock Z3 (#67) — the last genuine
  size limit for ASCII-domain engines; golden + mutation +
  differential-fuzz coverage.

## Compiler soundness fix wave (#68–#79, 2026-08-08)

Review follow-up wave; every finding mapped one-to-one to a phase,
test-first:

- P1 (#74): `{1}`/`{1,1}` quantifier crash fixed (no `Concat(body)` at
  lo==1); lazy-quantifier strip consolidated into the lowering pipeline.
- P3 (#75): pipeline integrity — `redact_witness` recursion for list-typed
  values; wall-clock ReDoS gate (count-cap removed); `sys.path` bootstrap.
- P2 (#76): false-UNSAT soundness — anchors inside alternations now
  **reject** (`per-alternative-anchor`) instead of hoisting unsoundly;
  scoped `(?i:)` case handling; `pcre_strip` `}+` corruption; `\s`
  divergence fix-or-reject per dialect.
- P4 (#77): ModSecurity `!@rx` negation — per-dialect decision table,
  reject-unsupported, never silent.
- P5 (#78): consolidation — shared `reject_markers.py`, duplicate
  `_repeat`/`_lit`/`_dot` removed, golden-suite hardening.
- MIT license badge (#79).

## Post-fix-wave re-measurement (2026-08-08)

- New `scripts/remeasure-from-inventory.py`: recompiles committed inventory
  NDJSONs through the current compiler (frozen extraction, current
  compiler) with per-record flip deltas; no silent sample fallback.
- All corpus fractions re-measured on the post-fix-wave compiler (frozen
  inventories):

| Corpus | Before | After | Flips |
|---|---|---|---|
| gitleaks | 0.8235 | 0.2262 | +0 / −132 (`per-alternative-anchor`) |
| trufflehog | 0.9349 | 0.9302 | +0 / −1 |
| ids_rules | 0.8790 | 0.8467 | +13 / −277 (mostly `per-alternative-anchor`) |
| semgrep_rules | 0.2741 (no-go) | 0.2741 (no-go) | none (composite-pattern extractor rejects preserved) |
| coreruleset | 0.7168 | 0.6908 | +0 / −9 |
| cpython_re | 0.5556 | 0.5556 | none |
| busybox / pcre2 / re2 testdata | 1.0 | 1.0 | none |
| validator.js (full inventory, dry-run) | 0.714 | 0.7639 | +91 / −31 |

  Headline: **gitleaks drops below the gate** — the false-UNSAT soundness
  fix (reject-over-hoist for per-alternative anchors) hits secret-detector
  `(?:...|$)` trailing alternations. The rejection is sound; the class is
  encodable in principle via string-op suffix equality and is the next
  toolkit-fix candidate. Semgrep stays no-go: frozen `composite-pattern`
  extractor rejects (empty placeholders) are restored on remeasure and must
  not be recompiled as encodable. The corpus-wave phase-3 decision artifacts
  are superseded by these measurements.
- `remeasure-from-inventory.py` restores extractor-frozen reasons
  (`composite-pattern`, `multi-match`) from inventory `compile_reason` so
  empty-placeholder rows cannot inflate encodable counts.

## Trailing-alt `$` P3 validate (#83, 2026-08-08)

- Remeasured all frozen inventories through the A1B compiler (#89) and
  regenerated `cross_corpus_matrix.{json,md}`.
- Headline fractions: gitleaks **0.8190** (stable), ids_rules **0.8519**
  (was 0.8467; paa 278→235), coreruleset **0.6908** (unchanged; paa=9),
  semgrep_rules **0.2842** (was 0.2741).
- AC-P3: gitleaks ≥0.70 **pass**; ids ≥0.87 and CRS ≥0.71 **miss** — residual
  `per-alternative-anchor` rows are caret-in-X / mid-pattern / non-`(?:…|$)`
  shapes outside the A1B accept class (documented in
  `properties/generated/trailing_alt_dollar_p3_delta.md`; accept class not
  widened).

## Trailing-alt `$` P4 secret corpora (#84, 2026-08-08)

- gitleaks e2e fraction **0.8190** (stable vs P3); extract `regex_id` set
  unchanged. `(***)` Anthropic shared-prefix rows classified as
  corpus-artifact (still encodable under A1B).
- detect-secrets expanded to full pin **v1.5.0** via new `python_dir`
  extractor; fraction artifact **0.3725** (19/51).
- trufflehog re-cloned at **v3.88.29** / `90190de`; `regex_id` set matches
  frozen baseline. One encodability flip (`^[xX]+|\*+$` →
  `per-alternative-anchor`) classified as compiler soundness (#76), not
  extractor drift. Drift writeup:
  `properties/generated/trailing_alt_dollar_p4_drift.md`.

## Trailing-alt `$` wave closeout (#81 / #85, 2026-08-08)

Wave plan #81 closed via P1–P5 (#86–#85):

| Phase | PR | Headline |
|---|---|---|
| P1 spike | #88 | Encoding evidence; A1B preferred over E1-only |
| P2 A1B | #89 | Compiler lowering; gitleaks **0.819** |
| P3 validate | #90 | Cross-corpus remeasure; ids/CRS AC misses documented |
| P4 corpora | #91 | detect-secrets **0.3725**; trufflehog id-stable |
| P5 docs | (this) | TRAPS §28; superseded pre-#80 decision matrices |

Authoritative fractions: `properties/generated/cross_corpus_matrix.*` and
`*_encodable_fraction.json`. Pre-wave
`phase3_decision_matrix.*` / `gitleaks_residual_abc.json` /
`gitleaks_remeasure_delta.json` are marked **superseded**.

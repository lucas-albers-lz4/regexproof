# Changelog

All entries below cover the initial development cycle plus the 2026-08-08
dogfooding/corpus/fix waves. No release tags exist yet. This changelog groups
the work by phase; dates are merge dates.

## Conversion ledger (2026-08-15)

- Added `scripts/conversion-ledger.py` and
  `properties/generated/conversion-ledger.{json,md}`: the product funnel
  (sites → properties asked → SAT → ground-truth → accepted upstream).
  Heap's-law novelty saturates compiler coverage; this ledger saturates the
  claim that we find real security problems. Curated last mile:
  `docs/conversion-upstream.jsonl`. Golden CI regenerates and drift-checks
  the artifact. `docs/why.md` records the two-machines model and the first
  freeze (1 accepted upstream, 0 third-party public).

## Accuracy flywheel (2026-08-13)

Implementation of [#424](https://github.com/lucas-albers-lz4/regexproof/issues/424)
(design [#423](https://github.com/lucas-albers-lz4/regexproof/issues/423)):

- **P2 (#426 / #436)**: C1 mirror + shape metadata on `CompileResult` (`leading_caret`,
  `trailing_dollar`, word-boundary wrap, alphabet certification). Compile records
  stream `(row, mirror, meta)` triples; unused mirrors are discarded until
  synthesis.
- **P3 (#427 / #438)**: property synthesizer behind `--synthesize` (off by default).
  Exact-mirror certification, SAT mutation guards, skip buckets, ground-truth
  replay via `regexproof.groundtruth.adapters`.
- **P4 (#428 / #439)**: batch-mode gate enforcement for synthesis (coverage floor,
  planned-status exclusion).
- **P5 (#429 / #437)**: compiler feature-yield artifact, E1 compiler diff-fuzz job,
  E2/E3 hardening, D5 provenance.
- **P6 (#430 / #440)**: materialized `gate-labels.json`, tree-probe tier,
  ledger-hash provenance, rank CLI keys.
- **P7 (#431 / #435)**: ledger `gated:*` status closes the mine loop; skip-gated
  default; search/queue sync.
- **P8 (#432 / #441)**: score-v2 fit + allocator (pure-Python deterministic model,
  pinned weights JSON, CPython 3.12 float pin).
- **P9 (#433 / #442)**: on-disk SMT-LIB mirror cache + bounded parallel compile
  (`ProcessPoolExecutor`, digest-verified entries, worker hard-kill).
- **Close-out (#443)**: probe dialect normalization, authoritative decision-pin,
  triage fingerprints namespaced by generated vs triage root.

## Smith extract/compile/fraction helpers (2026-08-14)

- **#149 / #450**: local Smith helpers (`regexproof.batch.smith_support`,
  `scripts/scaffold-smith-corpus.py`) — slug-safe paths, inflation-path
  allowlist, dialect/extractor guess, confine `-o` like author-gate. Not an
  auto-GO path. Pilot aggregate / `batch_repro.sha256` write gated so a
  single-corpus run cannot clobber all-corpus fingerprints.

## Dual-model audit wave (2026-08-12)

- **#377**: Harden required `Link check` — `lychee.toml` caps concurrency /
  retries, caches results, and keeps ACM/Microsoft bot-wall excludes. Corpus
  READMEs (`batch/corpora/**`) and `properties/generated/**` move off the
  required hot path to a path-filtered `Link check (corpora)` job so Smith
  issue-link fan-out no longer flakes merges on GitHub HTTP/2 errors.
- **#360**: `--fail-on-property-failure` CI overlay on the harness CLI and
  `z3-property-template.py`. Default exit stays the §10 recorder (FAIL is a
  recorded finding, exit 0). The required proof job now passes the flag so a
  violated property cannot ship green. PASS/FAIL is printed after ground-truth
  so `--require-ground-truth` cannot leave a PASS line on a refused replay.

## Harness backends wave (2026-08-11)

Design #213 closed at the APPROVE boundary (rev 7, U9 DROP; supersession notes
rev 7.1/7.2 on the issue). Phases 1-4 merged as #222-#234 (this PR is #235, the
CI bring-on):

- **Phase 1 (#217)**: 28-row parity matrix (25/25 verdict parity; both
  timeout classes rescued to 17/19 ms), ECMA pilot (0 divergences on 5,622
  decided comparisons), blocker probe (E2M unsat in the ASCII domain; Noodler
  SIGABRTs on negated from_ecma2020), R8 pre-flight 7/7, \p gate table
  (silent literalization measured), R5 cost table (download 0.83 s, ~144x).
- **Phase 2 (#218)**: registration gates (\p tokenizer + D7 structural
  checks via the Node/regexpp parser), D6 Noodler runner (raw-bytes SMT-LIB,
  process-group kills, S13 rc<0/139 classification, sha256 pin in the
  runner), D16 witness re-validation, the S10 operator contract (0 = recorded,
  1 = not-proven, 2 = disagreement).
- **Phase 3 (#219)**: cvc5 cross-check leg (per-query worker isolation, D12
  bounded-loop expansion cap 16), report-time verification tiers (S15),
  D15 verdict resolution (27-triple table) + the mechanical disagreement rule
  + exit 2.
- **Phase 4 (#220)**: four-bucket sweep (proven / finding /
  escalated-unconfirmed / still-unknown) with the versioned manifest, metric 8,
  D10 decision, S14-enforced triage audit, U9 publication; CI for the pinned
  Noodler asset (sha256-verified download + R8 pre-flight + S16 absent
  fixture), mutation-coverage gate, R5 finalization + CI logistics policy.

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

## Corpus Wave 2 (#94–#101, 2026-08-09)

| Phase | PR | Headline |
|---|---|---|
| P1 pre-gate | #104 | yara/pcre2 helpers; 8-surface mirror-fidelity gate |
| P2 YARA | #105 | schema v2 `domain` + YARA extractor; **0.6563 go** |
| P3 semgrep | #106 | `pattern-regex` denom; **0.4941 go** (was 0.2842 / 9186) |
| P4 testdata | #107 | budgets + `complete_run`; sample-scoped pcre2/re2/cpython/busybox |
| P5 ecma/rule_diff | #108 | test262 sample **0.8095**; Coraza↔CRS cross-engine pilot |
| P6 docs | (this) | TRAPS §29–§32; matrix rollup aligned to Wave-2 fractions |

Authoritative rollup: `properties/generated/cross_corpus_matrix.*`.
A1B residual AC close for ids_rules/CRS is tracked outside the wave (#103).
Non-goals: no re-litigation of wave #81 TRAPS §28 / superseded stubs.

## Caret-in-X lowering — A1B residual / AC-P3 (#103, 2026-08-09)

- New shape `^X(?:R|$)` in `regexproof/compiler/caret_in_x.py` (domain
  `ascii;caret_in_x`); A1B accept class **unchanged**.
- Spike GO: `properties/generated/caret_in_x_spike.*`.
- Remeasure: ids_rules **0.8717** (AC ≥0.87 **pass**; paa 235→72);
  coreruleset **0.6908** (CRS mid-pattern paa residual documented).
- TRAPS §33; delta `caret_in_x_remeasure_delta.*`.

## Corpus Wave 3 (#111–#117, 2026-08-09)

| Phase | PR | Headline |
|---|---|---|
| P1 perl helper | #119 | `helpers/perl` + SpamAssassin/perl_re spikes |
| P2 SpamAssassin | #122 | perl dialect; **0.7479 go** (442/591) |
| P3 secret pack | #123 | Nosey Parker **0.7354** + shhgit **0.9263**; `(?x)` strip |
| P4 ECMA frontier | #125 | DOMPurify **0.5625** admit-GO; isemail/email_addresses fraction-GO / admit-NO-GO |
| P5 testdata | #127 | perl_tre **0.3541** / go_regexp_tests **0.7524** / v8_mjsunit **0.5383**; OOM-hardened measure |
| P6 docs | (this) | TRAPS §34–§38; matrix + supersession aligned to Wave-3 fractions |

Authoritative rollup: `properties/generated/cross_corpus_matrix.*`.
Wave-3 measure fingerprints: `properties/generated/wave3_artifact_repro.sha256`
(CI `batch_repro.sha256` remains the three-corpus gate).
Ownership / supersession: `sweep/corpus-wave3/supersession.md`.
Non-goals: no re-litigation of Wave-2 #85 / TRAPS §29–§32 ownership.

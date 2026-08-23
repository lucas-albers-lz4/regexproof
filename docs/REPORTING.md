# Reporting artifacts — field contracts

Machine-readable and human reports from the batch / harness pipeline. Schemas
live under `regexproof/schemas/`. Writers: `regexproof/batch/report.py`,
`regexproof/batch/triage.py`, `scripts/z3-verify.py`.

## Cross-cutting semantics

| Rule | Meaning |
|---|---|
| TIMEOUT / `unknown` | Hard failure; surfaced as **not proven** (`not_proven=true` on harness JSON). Never a pass. |
| Ground truth | SAT findings must record replay status + `engine_versions` under `--require-ground-truth`. |
| Ordering | Scanner NDJSON sorted by `(regex_id, kind, …)`; harness `--all --json` sorts by property name. |
| Reproducibility | Pinned toolchains (`ci/toolchain.toml`); batch two-run byte-identical gate (`scripts/ci-batch-repro.py`). |
| Disclosure | Security-tool corpora → `private_first` — see [`SECURITY.md`](../SECURITY.md). |

### Synthesis Evidence Gates

The synthesis batch gate requires a 100% mutation-guard coverage floor over
real synthesized property rows, keyed by `(family, bad_char)`. Inventory
`planned` stubs and ordinary non-synthesized findings are excluded from both
the numerator and denominator. A run with no real synthesized rows has no
coverage claim; planned stubs cannot satisfy or inflate the floor.

The synthesis wave uses these `ground_truth_status` values:

| Value | Meaning |
|---|---|
| `reproduced` | A synthesized SAT property witness replayed successfully in the real engine. |
| `mutation-guard-sat-expected` | A mutation guard produced the required SAT result for the widened mirror. |
| `planned` | An inventory question was emitted as a planned stub and was not synthesized. |

With `--require-ground-truth`, synthesized SAT properties require
`reproduced`; mutation guards always require their exact special status and
`expected_result: "sat"`. Any mutation-guard result other than `sat`, including
`unsat`, `timeout`, or `unknown`, fails the batch gate.

## Harness NDJSON (`z3-verify.py --json`)

One JSON object per line (NDJSON). Fields include:

`schema_version`, `name`, `kind`, `family`, `call_kind`, `domain`,
`input_domain`, `expect_unsat`, `result` (`unsat`|`sat`|`timeout`), `ok`,
`witness`, `ground_truth`, `wall_ms`, `engine_versions` (`python`, `z3`),
`not_proven`.

- Partial streams remain valid if a later property fails.
- `--json-legacy` emits the same records as a single JSON array.
- `--json` and `--json-legacy` are mutually exclusive.
- Contract text in `AGENTS.md` must match the CLI module docstring.

## Scanner finding NDJSON (`properties/generated/<corpus>.ndjson`)

Schema: `regexproof/schemas/scanner_finding.schema.json`.

| Field | Notes |
|---|---|
| `schema_version` | `"1"` |
| `regex_id` | Stable id (or `inventory:…` stubs) |
| `kind` | `property` \| `counterexample_finder` \| `bug_demo` \| `mutation_guard` \| `rule_diff` \| `redos` \| `usage_mismatch` \| `intent_mismatch` \| `triage` |
| `corpus` | Short pilot name (`gitleaks`, …) |
| `result` | Finding outcome / planned status |
| `site` | `file:line:column` or inventory id |
| `pattern` | Pattern text when applicable |
| `shape` | 1–5 or null |
| `ground_truth_status` | Replay status. Present on Z3-verdict findings (`property`, `counterexample_finder`, `bug_demo`, `mutation_guard`, `rule_diff`); mutation guards require the exact `mutation-guard-sat-expected` value. Omitted on classification findings (`usage_mismatch`, `intent_mismatch`, `triage`, `redos`) — absence means "not a Z3 verdict", never a silent `N/A` |
| `ground_truth` | Optional **per-engine** evidence object for cross-engine `rule_diff` (e.g. `{pcre2: {status, version, cmd, matched, replay}, go_re2: {...}, status}`). A single `ground_truth_status` alone is not sufficient to claim dual-engine ground truth. |
| `disclosure` | `private_first` \| `public_ok` \| null. **null** means the corpus is not in `SECURITY_TOOL_CORPORA` and no approval file listed this `regex_id`. On security-tool corpora, `tag_disclosure()` defaults to `private_first` for every kind unless listed in `DISCLOSURE_EXEMPT_KINDS` (empty; fail-closed). `public_ok` is set **only** by `apply_approval()` from `--approval-path` (JSON `{"regex_ids": [...]}`) on ground-truthed (`reproduced`/`PASS`) findings. `assert_no_auto_publication()` still forbids `publish` without `approved`. |
| `witness` | Redacted when committed |
| `detail` | Kind-specific object |

## Batch markdown (`properties/generated/<corpus>_batch.md`)

Report-level YAML front matter: `schema_version`, `corpus`, `findings`.

Each finding section starts with a fenced YAML block of contracted fields
(when present on the finding record):

`regex_id`, `schema_version`, `kind`, `corpus`, `dialect`, `call_kind`,
`shape`, `result`, `family`, `domain`, `wall_ms`, `ground_truth_status`,
`engine_versions`, `disclosure`, `site`.

Then the usual prose sections:

- `## <kind>:<regex_id>[:suffix]`
- `### Pattern` / `### Context` / `### Witness` / `### Ground-truth`

Phase-3 shape-5 pilot report remains at `properties/generated/gitleaks.md`
(not overwritten by batch). Writer: `regexproof.batch.report.write_markdown`
(paths must stay `*_batch.md`).

## Triage NDJSON (`properties/triage/<corpus>.ndjson`)

Schema: `regexproof/schemas/triage_record.schema.json`. One line per
unencodable / TIMEOUT / ambiguous compile item (1:1 with those cases; empty
file is valid).

| Field | Notes |
|---|---|
| `schema_version` | `"1"` |
| `regex_id` | 32 hex |
| `reason_kind` | `unencodable` \| `timeout` \| `ambiguous` |
| `unencodable_reason` | Compiler reason or null |
| `dialect` | `py_re` \| `ecma` \| `re2` \| `pcre` |
| `call_kind` | From extractor |
| `site` | `file:line:column` |
| `pattern` | Pattern text |

Compiler `unencodable_reason` values that are **policy / explicit rejects**
(not silent approximations): `pattern-too-long` (TRAPS #21), ECMA `m-flag` /
`u-flag` / `v-flag` / `stateful` (TRAPS #22), `negated-unsupported`
(ModSecurity `!@rx` / selectors — [`docs/NEGATION.md`](NEGATION.md)). Batch
triage should route these per `scripts/crs-redos-dialect.py` `ROUTING` (and
corpus equivalents).

Human-mergable: one JSON object per line, stable key order (`sort_keys`).

## Conversion ledger

Writer: `scripts/conversion-ledger.py`. Artifacts:
`properties/generated/conversion-ledger.{json,md}`. Curated last mile:
[`docs/conversion-upstream.jsonl`](conversion-upstream.jsonl).

This is the product funnel (sites → properties asked → SAT → ground-truthed →
disclosed → accepted upstream). It is orthogonal to compiler-feature-yield
(which ranks encode-path work) and to `docs/verified-findings.jsonl` (toolkit
traps). Heap's-law novelty saturates coverage; this ledger saturates conversion.

Golden CI regenerates the artifact after batch and `git diff --exit-code`s it.
`would_open_public_upstream` must stay 0 without a human approval file
([SECURITY.md](../SECURITY.md)). TIMEOUT / `unknown` is not a pass.

Two `private_first` counters exist and must not be mixed (#486):

- `disclosed_private_first` — scanner NDJSON product+classification kinds,
  **skipping** planned inventory stubs (`is_planned`).
- `pr_dry_run_private_first` — summed from `*-pr-dry-run.json`, **including**
  planned stubs that `tag_disclosure()` marked private. The typical delta is
  31 security-tool corpora × 4 stub questions = 124.

Scanner product kinds counted as "properties asked": `property`,
`counterexample_finder`, `bug_demo`, `rule_diff` with `result` other than
`planned`. SAT-ish results: `sat` and `gap`. Ground-truth pass:
`reproduced` and `PASS`. `mutation_guard` and `usage_mismatch` /
`intent_mismatch` / `triage` are excluded from the product numerator.

Ledger JSON (`schema_version: "1"`) field groups:

| Group | Fields |
|---|---|
| funnel | `sites_extracted`, `sites_encodable`, `scanner_rows`, `planned_stubs`, `classification_rows`, `properties_asked`, `properties_asked_synthesized`, `properties_sat`, `properties_sat_synthesized`, `sat_unique_sites`, `sat_ground_truthed`, `rule_diff_report_sat`, `disclosed_private_first`, `pr_dry_run_private_first`, `accepted_upstream`, `existence_proofs`, `third_party_public`, … |
| rates | `encodable_fraction`, `pipeline_accepted_per_gt`, `pipeline_accepted_per_extracted` (aliases `accepted_per_gt` / `accepted_per_extracted` for one release). These pipeline rates include own-code usrmanage; they are **not** a wild-bug conversion rate. |
| security_tool_split | asked/SAT in vs not in `SECURITY_TOOL_CORPORA` |
| upstream | curated `docs/conversion-upstream.jsonl` status counts |
| per_wave (#554) | one row per top-level `(wave_id, idiom_bucket)`: `properties_asked` → `properties_sat` → `sat_ground_truthed` → `filed` → `accepted`, plus `shape_counts` / `shape_mix`. Join: curated rows on canonical `(site, question_id)`; `filed` = status `filed` / `private_first` / `fixed_upstream` (or `filed_at` set); `accepted` = `fixed_upstream`. GT→filed is the currently empty hop and is highlighted in the MD. |
| starvation (#554) | `backlog_weeks = demand_open / admission_per_week`; demand = open `gated:go` clusters lacking a closed wave (candidate ledger); admission = GO `*_gate_decision.json` artifacts per 7-day window ending at the latest committed GO date (artifact clock — deterministic; NOT the lagging candidate ledger). `mine_queue_pressure = queue_len / queue_cap`. `alert_backlog_increasing` when `backlog_weeks` rises ≥ 2 consecutive windows (`history` carried in this artifact). Admission is mine-cap-bounded by design — read with `mine_queue_pressure`, not as batch health. |
| queue_health (#551 C) | `properties/conversion_queue/*.json` counts by pre-contract state: emitted / claimed / contracted / skipped (+ median age days from `created_at`). Absent until Phase C ships. |
| shape_mix_by_corpus (#554) | per-corpus shape-1..5 counts over asked properties (descriptive until n ≥ 50). |

### Entity IDs and dedup (#554)

Conversion counts are **property-level**: the unit is
`(site, question_id)` (scanner `name` is the `question_id` fallback),
canonicalized as in `scripts/check-disposition-coverage.py`'s docstring.
`properties_asked_distinct` / `properties_sat_distinct` dedupe on that pair,
consistent with #480. Findings-per-site and upstream-issue-level rollups are
derived, never stored twice.

### Headline findings metric (#554, additive to encodable fraction)

Until the contracted boundary-site denominator crosses the committed
threshold (**n ≥ 50**): raw finding counts with a **Clopper-Pearson**
(exact) interval; findings per site use **Wilson**. Per-10k thereafter.
Encodable fraction stays the compiler headline (why.md three-claim
separation). Bootstrap CIs elsewhere: B=10000, 95% BCa with
percentile/exact-binomial fallback.

### Shape-3/5 ground-truth discipline

SAT shape-3/5 properties require product-engine ground-truth replay before
they count as GT (BusyBox sed/grep for OpenWrt packages, Node `RegExp` for
LuCI); expected-UNSAT shape-3 requires differential fuzz. See AGENTS.md §4
and `docs/TRAPS.md`.

## Curated dispositions (`docs/conversion-upstream.jsonl`)

Curated rows are the **source of truth for filing state** (why.md /
AGENTS.md must match or cite them — enforced by
`scripts/check-disposition-coverage.py` in CI).

- **Disposition enum** (`status`, unknown values rejected):
  `filed`, `filed_plan` ("filed upstream, awaiting response" — distinct from
  `wont_file`), `wont_file`, `false_positive`, `private_first`,
  `fixed_upstream`, `approval_missing`, `out_of_scope_redos`.
- **`approval_missing` escape (required, #556):** a row with
  `status=approval_missing` must carry `approval_escape` — either
  `approval_present` (with `approval_ref`: approval file path or issue/PR
  reference) or `wont_file` (with `reason_code`). A bare `approval_missing`
  label is rejected by the coverage checker; it is a real hop with a defined
  path, not a dead end. Record decisions via
  `scripts/record-filing-decision.py`.
- **Join keys:** `site` + `question_id`, canonicalized per the checker
  docstring; scanner `name` is the `question_id` fallback. Wave keys
  (`wave_id`, `idiom_bucket`) live at scanner-row top level in
  `*_conversion.ndjson` — never inside `contract`
  (`property_contract.schema.json` is `additionalProperties: false`).
- **`filed_at` / `resolved_at`:** required going forward;
  optional-with-reason for backfilled rows.
- **Backfill rule:** backfilled rows carry `reason_code` plus
  `disposition_date` = ISO date or the explicit enum value `unknown_date`.
- **Censoring-aware time-to-acceptance:** `unknown_date` rows are excluded
  from medians; report via Kaplan-Meier or state "median of closed rows
  only" — never mix censored + closed rows in a plain median.
- **Coverage join (#554):** every GT-confirmed SAT row in
  `*_conversion.ndjson` (`result` sat/gap, non-synthesized product kind,
  `ground_truth_status` reproduced/PASS) needs a curated row;
  `scripts/check-disposition-coverage.py` fails closed otherwise.
- **CRS 942220:** exactly one curated disposition (CU-005,
  `false_positive`). Historical-numerator rule: prior wave / rule_diff
  asked/SAT counts stay as recorded; the curated disposition governs filing
  state only.



Do not quote a frozen pipeline-accepted / SAT-GT ratio from an old ledger as
the product yield. Re-read the regenerated artifact; third-party public
accepted is the conversion claim, and it is 0.

`properties_asked` / `properties_sat` are raw scanner rows. Distinct
`(site, question_id)` counts are `properties_asked_distinct` /
`properties_sat_distinct` (#480). Synthesis is capped at `synth_max_sites`
(default 0 — untargeted synthesis is compute control; opt-in corpora set an
explicit value, first `regex_id` after sort) — recorded on the batch summary
`synthesis` object.

`crs-inventory.ndjson` is the CRS `@rx` measure, not the `coreruleset` batch
inventory. Site-count deltas between those two files are expected (#493).

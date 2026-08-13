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
| `disclosure` | `private_first` \| `public_ok` \| null |
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

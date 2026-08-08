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
| `kind` | `property` \| `rule_diff` \| `redos` \| `usage_mismatch` \| `intent_mismatch` \| `triage` |
| `corpus` | Short pilot name (`gitleaks`, …) |
| `result` | Finding outcome / planned status |
| `site` | `file:line:column` or inventory id |
| `pattern` | Pattern text when applicable |
| `shape` | 1–5 or null |
| `ground_truth_status` | Replay status. Present on Z3-verdict findings (`property`, `rule_diff`); omitted on classification findings (`usage_mismatch`, `intent_mismatch`, `triage`, `redos`) — absence means "not a Z3 verdict", never a silent `N/A` |
| `disclosure` | `private_first` \| `public_ok` \| null |
| `witness` | Redacted when committed |
| `detail` | Kind-specific object |

## Batch markdown (`properties/generated/<corpus>_batch.md`)

Front matter (YAML): `schema_version`, `corpus`, `findings`.

Per finding section headings:

- `## <kind>:<regex_id>[:suffix]`
- `### Pattern` / `### Context` / `### Witness` / `### Ground-truth`

Phase-3 shape-5 pilot report remains at `properties/generated/gitleaks.md`
(not overwritten by batch). Field-rich pilot rows include `regex_id`, dialect,
`call_kind`, shape, result, ground-truth + engine versions, `wall_ms`, domain,
`family`, `schema_version`.

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

Human-mergable: one JSON object per line, stable key order (`sort_keys`).

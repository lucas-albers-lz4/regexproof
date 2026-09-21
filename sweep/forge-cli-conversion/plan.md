# Agenticstiger/forge-cli — conversion wave 1

> Design: [`docs/CLUSTER-CONVERSION.md`](../../docs/CLUSTER-CONVERSION.md).
> This is the next conversion wave after the Doberman-Core command-execution
> slice. It deliberately selects a different corpus and idiom: Python
> secret-redaction and credential-sanitization boundaries.

**Goal:** Convert one bounded **py_re** slice from
`Agenticstiger/forge-cli`: redaction of credentials in URLs, serialized
configuration, provider error bodies, endpoint diagnostics, and rendered dbt
commands. Rank 15, write at most 5 human contracts, ground-truth against the
pinned Python implementation, and emit a `forge-cli_conversion.ndjson` ledger
join only after the contracts are adopted.

**End state:** a measured asked/SAT/ground-truth yield plus an explicit skip
list. This wave is not an audit of every regex in forge-cli, does not add the
corpus to `WAVE_CORPORA`, and does not treat agent-derived shape-1/2 rows as
product properties.

## Trust map (Gate 2 input)

forge-cli is a data/build orchestration CLI. The selected sites sit on
redaction boundaries where provider responses, engine errors, operator
configuration, or command arguments are turned into logs, persisted run
state, CLI diagnostics, or user-visible provider reports.

| Trust | Typical source | Example |
|---|---|---|
| `untrusted-input` | Provider/engine response text and remote error bodies | URL userinfo, `sasl.jaas.config`, Datamesh error-body masking |
| `config` | Operator/provider endpoint and dbt command configuration | endpoint query/userinfo, `-e KEY=VALUE` command rendering |
| `internal` | Test fixtures, banner/schema parsing, feature detection | not eligible for this wave |

The guarantee must name the actual sink. “The regex has a useful shape” is
not a contract. The first two redactor candidates are especially attractive
because the central `redact_secret_text` function is reused by state,
lineage, engine-error, auth-error, CLI-preview, MCP-output, and database-cell
paths; the ground-truth callback must exercise the real function, not just a
standalone `re.search`.

**Vocab tokens:** `secret`, `redact`, `credential`, `password`, `token`,
`api-key`, `auth`, `endpoint`, `error`, `state`, `lineage`, `dbt`, `log`.

**Product engine:** CPython `re` at the pinned forge-cli commit. This is a
Python-regex conversion wave; BusyBox is not the product engine. SAT witnesses
must be replayed through the real forge-cli helper and the actual sink path.
TIMEOUT or a non-reproducing witness is a hard failure. ReDoS claims are out
of scope for this membership wave and belong to the dedicated ReDoS tools.

**Family:** `FC-forge-cli`. Every adopted property and its mutation guard
must use the same family.

## Already measured (Gate 0 / Gate 1)

The corpus is already admitted and batched; do not re-run admission or copy
the corpus into the golden wave.

| Fact | Value |
|---|---|
| Unit | `Agenticstiger/forge-cli` @ `efcf8e4c0087def553a737dc1c4eebda5d8a90cd` |
| Measured surface | 314 Python regex sites in the top-60 `.py` allowlist |
| Encodable | 171/314 = 0.5446; complete run, 0 parse errors, budget clean |
| Existing artifacts | `forge-cli-inventory.ndjson`, `forge-cli.ndjson`, Smith decision |
| Additional surface | 11 POSIX-shell sites outside this wave’s Python scope |

The existing batch is a filter, not product evidence. No forge-cli property
has entered the conversion denominator from this plan yet.

## Non-goals and deny-list

- Do not re-ask Doberman’s terminal-newline command-token idiom.
- Do not enroll the generic `_ASSIGNMENT_RE` at
  `fluid_build/observability/secret_redactor.py:195`. Its own source comment
  documents unavoidable truncation for unknown unheld values; exact-value
  masking is the product’s stronger path. Treat it as a documented residual
  limitation, not a clean invariant.
- Do not count unencodable provider-token, PEM, lookaround, or backreference
  patterns in this wave.
- Do not mix the separate POSIX-shell surface into family `FC-forge-cli`.
- Do not file a public third-party issue without an explicit disclosure
  decision. Security-tool findings default to `private_first` only after
  ground-truth and surrounding-code review establish reachability.

## Ranked reading set (Gate 2)

The deterministic ranker used the existing inventory, the vocabulary above,
and a 15-site cap. The top set is recorded here so the reading decision is
reproducible:

| Rank | Site | Initial disposition |
|---:|---|---|
| 1 | `observability/secret_redactor.py:218` `_JAAS_CONFIG_RE` | keep; whole quoted-value redaction |
| 2 | `build_runners/base.py:54` `SENSITIVE_ENV_KEY_RE` | keep; inspect command-log sink |
| 3 | `cli/_common.py:89` x-api-key substitution | keep initially; defer after read (central-redactor overlap) |
| 4 | `llm/providers.py:287` endpoint userinfo substitution | keep; encodable `(https?://)([^@/]+)@`. Skip unencodable `:280` `[^&]+` |
| 5 | `observability/secret_redactor.py:151` `_URL_USERINFO_RE` | keep; shared central redaction sink |
| 6 | `providers/datamesh_manager/datamesh_manager.py:88` error-body pattern | keep; remote error-body sink |
| 7 | `build_runners/base.py:47` env placeholder | defer; resolution, not redaction |
| 8 | `build_runners/hooks/dlp_scan.py:35` phone detector | defer; DLP classification, separate idiom |
| 9 | `cli/_common.py:88` Bearer substitution | merge with redaction review only if its sink is distinct |
| 10 | `cli/_untrusted_content.py:50` role classifier | defer; prompt classification, not secret sink |
| 11–15 | banner/schema/parser and URL-shape sites | defer; no credential sink in this slice |

The six “keep” rows are a reading shortlist, not six adopted contracts.
After reading, rank 3 (`x-api-key`) was deferred as central-redactor overlap,
leaving five adopted sites. Do not alias PRODUCT to MATCH: that is
Concat-identity and is not a countable property.

## Proposed contracts (human adoption required)

These are the questions to adopt or reject after this proposal is reviewed.
Until adoption, they remain `agent_derived` planning material and must not
move `properties_asked`.

| Candidate | Proposed guarantee | Shape / ground truth |
|---|---|---|
| JAAS quoted value | A serialized `sasl.jaas.config` value, including escaped quotes, does not reach the shared log/state redaction sink with its secret value intact. | Shape 4 or bounded transformation; call `redact_secret_text` and assert the real output |
| URL userinfo | A credential in `scheme://user:password@host` does not reach shared logs or persisted run records; scheme/user/host remain available for diagnostics. | Shape 4; call both global and Snowflake-shared paths |
| dbt env argument | A `-e KEY=VALUE` command rendered to the CLI does not expose the value when `KEY` matches the sensitive-key policy. | Shape 3/transformation; call `_render_command_for_log` |
| Datamesh error body | A remote provider error body containing a recognized credential assignment or `ed_live_` token does not reach the raised `ProviderError` text in clear form. | Shape 4; call `_redact_error_body` with HTTP-error fixtures |
| LLM endpoint diagnostic | A configured endpoint’s recognized query credential and URL userinfo do not appear in the AI test report in clear form. | Shape 4; call `LlmConfig.redacted_endpoint` and the report path |

The `_common.py:89` x-api-key site is a fallback candidate, not an automatic
sixth contract. It enters only if its copilot-memory persistence sink is shown
to be materially distinct from the central redaction contracts and one of the
five rows above is rejected.

## Phases

### P0 — plan and source audit

- This plan records the pinned source, trust classes, rank-15 reading set, and
  explicit deny-list.
- Read the surrounding call path for each keep candidate before registration.
- Confirm whether the input is `untrusted-input` or `config`; do not infer a
  security boundary from the regex name alone.

### P1 — contract adoption and harness registration

- Adopt at most five guarantees with `provenance=human`.
- Register family `FC-forge-cli` properties plus at least one mutation guard.
- Specify PRODUCT and MATCH independently. `PRODUCT = MATCH` is Concat-identity
  and must not increment `properties_asked`.
- Use `--require-contract --require-ground-truth`; unsupported constructs stay
  skipped rather than being rewritten into a weaker question. The LLM query
  `[^&]+` at `providers.py:280` stays skipped; adopt `:287` instead.

### P2 — Python ground truth and differential checks

- Replay every SAT witness through the pinned forge-cli helper and actual sink.
- For expected-UNSAT transformation claims, differential-fuzz the mirror
  against CPython `re` and the helper, including delimiters, escaped quotes,
  URL authority characters, empty values, and terminal newlines.
- Record refuted reviewer/model claims alongside accepted findings.

### P3 — ledger join and close-out

- Emit `properties/generated/forge-cli_conversion.ndjson` only after human
  contracts and ground truth exist.
- Regenerate the conversion ledger and verify the delta is in `[1, 5]`.
- Write `forge-cli_conversion_wave.md` with asked, SAT+ground-truth, skips,
  disclosure dispositions, and the next unused idiom or a stop decision.

## Artifact contract

| Artifact | Role |
|---|---|
| `sweep/forge-cli-conversion/plan.md` | this proposal |
| `properties/generated/forge-cli-inventory.ndjson` | existing inventory |
| `properties/generated/forge-cli_smith_decision.json` | existing admission decision |
| `properties/generated/forge-cli_conversion.ndjson` | required ledger join after adoption |
| `properties/generated/forge-cli_conversion_wave.md` | required close-out |
| harness family `FC-forge-cli` | adopted contracts + mutation guard |

No public filing is implied by this plan. If a reproduced issue is found,
record its private/public disposition in `docs/conversion-upstream.jsonl` only
after the source review and disclosure decision.

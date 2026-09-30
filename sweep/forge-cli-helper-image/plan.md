# Agenticstiger/forge-cli — helper-image replay slice

This is the next conversion slice after
[`sweep/forge-cli-conversion/plan.md`](../forge-cli-conversion/plan.md) wave 1.
It stays on `Agenticstiger/forge-cli` at
`efcf8e4c0087def553a737dc1c4eebda5d8a90cd` and asks shape-4 questions about
the real sanitizer images, not another alphabet self-cover.

## P0 source audit: copilot-memory candidate rejected

Wave 1 named `_common.py:88-90` Bearer / x-api-key substitution as a possible
next idiom only if it had a distinct persistence sink. The pinned source audit
does not establish that contract:

| Path | Evidence at the pin | Decision |
|---|---|---|
| Project memory | `forge_copilot_memory.py:_clean_scalar` calls `redact_secrets` | candidate source |
| Project-memory write | `CopilotMemoryStore.save` calls `_coerce_memory_document`, which normalizes the same scalar again before `copilot-memory.json` is written | **no distinct leak property** |
| Personal memory | `forge_copilot_personal_memory.py:save_personal_memory` does not call `redact_secrets` | not this regex site |
| Team memory | `forge_team_memory.py:scaffold_team_memory` writes a template directly; no `_common.py` regex reaches it | not this regex site |

The apparent first-pass witness
`x-api-key: "abc\\" s"` becomes `x-api-key: "*** s"`, but the second
project-memory normalization removes the tail before persistence. Bearer
values are redacted on the first pass. This refutes a persistence finding; no
new `FC-forge-cli` property or `conversion-upstream.jsonl` row is adopted from
this candidate, and no public filing is implied.

## Next contracts to adopt

At most four human contracts are planned, one per distinct helper/sink:

| Site | Product question | Expected shape |
|---|---|---|
| `observability/secret_redactor.py:218` `_JAAS_CONFIG_RE` | an escaped-quote JAAS value is replaced by the redaction image without exposing the value or damaging its surrounding record | shape 4, per-token image |
| `build_runners/base.py:54` `SENSITIVE_ENV_KEY_RE` | a sensitive `KEY=VALUE` command rendered for logs contains the redacted image, never the value | shape 4, per-command token |
| `providers/datamesh_manager/datamesh_manager.py:88` `_SECRET_ERROR_PATTERNS` | a remote error body reaches `ProviderError` only after the recognized credential image is applied | shape 4, per-error fixture |
| `llm/providers.py:287` `LlmConfig.redacted_endpoint` | query credentials and URL userinfo are masked in the diagnostic endpoint image while host/scheme remain | shape 4, decomposed query/userinfo tokens |

The existing wave-1 shape-1/2 contracts remain closed. The unencodable
`providers.py:280` `[^&]+` query remains skipped unless a sound backend or an
independent product specification is supplied.

## Gates before adoption

1. Replay each helper against the pinned CPython implementation, including
   escaped quotes, delimiters, empty values, repeated assignments, and
   terminal newline cases.
2. Define each output image independently from the source matcher. Do not
   encode `PRODUCT = MATCH`, and do not use Z3 `replace_all`.
3. Use per-token decomposition where a monolithic image query times out; an
   unknown result is not proven.
4. Add a mutation guard for each helper family and differential-fuzz the
   mirror against the real helper before emitting a conversion row.
5. Ground-truth every SAT witness in code. Any reproduced third-party finding
   remains `private_first` until a disclosure decision is recorded.

No new property is counted in this planning slice. The next implementation
PR should add the first helper-image contract only after its real replay and
mutation guard are available.

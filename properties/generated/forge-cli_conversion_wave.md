# forge-cli conversion wave 1 — close-out

Pin: `Agenticstiger/forge-cli` @ `efcf8e4c0087def553a737dc1c4eebda5d8a90cd`.
Family: `FC-forge-cli`. Product engine: CPython `re` at the pinned source.
Not in `WAVE_CORPORA`. Idiom bucket: **`secret-redaction`**.

Rank: [`forge-cli_rank.json`](forge-cli_rank.json) (vocab keep-15, path filter `fluid_build/`).

## 15 read → 5 asked

| Site | Decision | Why |
|---|---|---|
| `_JAAS_CONFIG_RE` `:218` | **asked** shape 2 (escaped-quote product ⊆ MATCH) | Independent product grammar requires `\"`; MATCH is `(?:[^"\\]|\\.){,2048}`. Not `PRODUCT = MATCH`. |
| `SENSITIVE_ENV_KEY_RE` `:54` | **asked** shape 2 (policy keys ⊆ MATCH) | Documented forms including empty `[_-]?` (`apikey`, `privatekey`) vs the source regex. |
| `_common.py:89` x-api-key | skip | Central-redactor overlap; fallback only if a keep row is rejected. |
| `providers.py:287` `(https?://)([^@/]+)@` | **asked** shape 1 (no `@`) | New userinfo alphabet → `LlmConfig.redacted_endpoint`. |
| `providers.py:280` `[^&]+` query | skip | Unencodable (`unicode-not-literal`). Do not rewrite into a weaker self-cover. |
| `_URL_USERINFO_RE` `:151` | **asked** shape 1 (no space) | New password alphabet `[^/?#@\s]` → `redact_secret_text`. |
| `_SECRET_ERROR_PATTERNS` `:88` | **asked** shape 1 (no `;`) | New assignment-value alphabet `[^"'\s,;}]+` → `_redact_error_body`. |
| `base.py:47` env placeholder | skip | Resolution, not redaction. |
| `dlp_scan.py:35` phone detector | skip | DLP classification, separate idiom. |
| `_common.py:88` Bearer | skip | Central-redactor overlap. |
| `_untrusted_content.py:50` role classifier | skip | Prompt classification, not a secret sink. |
| `_ASSIGNMENT_RE` `:195` | skip | Plan deny-list: documented truncation for unknown unheld values. |
| banner/schema/parser and URL-shape sites | skip | No credential sink in this slice. |
| POSIX-shell surface | skip | Different dialect; not family `FC-forge-cli`. |
| Concat-identity URL/JAAS self-cover | skip | `InRe(s, R) ∧ ¬InRe(s, R)` is not a property. |

## Results

- 5 human-contract properties asked (3 shape 1 + 2 independent coverage inclusions).
- 5 expected-UNSAT in the declared ASCII domains.
- 0 SAT and therefore 0 SAT witnesses requiring helper replay.
- 1 mutation guard SAT (`FC-forge-cli-mutated-url-password-space`), confirming the URL-password alphabet is sensitive to a space-widening mutation.
- No pattern-class SAT. No `conversion-upstream.jsonl` row. No public forge-cli filing.

Alphabet membership is checked against CPython `re` in `tests/test_forge_cli_harness.py`. The other helper-image sinks (`redact_secret_text`, `_redact_error_body`, and `LlmConfig.redacted_endpoint`) remain outside the replay completed below.

The conversion rows are emitted in
[`forge-cli_conversion.ndjson`](forge-cli_conversion.ndjson). They record
`ground_truth_status: null` because no SAT witness was produced.

## Stop vs next slice

**Wave 1 idiom slice done.** Do not re-ask URL password charset, Datamesh assignment-value charset, LLM `:287` userinfo charset, JAAS escaped-quote product coverage, or the documented sensitive-key forms. Do not re-ask the unencodable `:280` `[^&]+` query as an ASCII self-cover.

**Next idiom (same cluster, same pin):** copilot-memory x-api-key/Bearer persistence only if it is shown to be a distinct sink from `redact_secret_text`.

**Do not:** packages/LuCI/aidevops/mycelium re-open, Smith drain, `WAVE_CORPORA`, public filing without approval, hostname / JSON `[^"]*` / IPv4-MAC charset, Concat-identity `PRODUCT = MATCH`.

## #648 helper-image follow-up — `SENSITIVE_ENV_KEY_RE`

- **Family / wave:** `FC-forge-cli` / `forge-cli_helper_image`; human contract, trust `config`, input is provider/operator dbt argv.
- **Pinned product:** `Agenticstiger/forge-cli@efcf8e4c0087def553a737dc1c4eebda5d8a90cd`; source is fetched/materialized at that revision and the actual `fluid_build.build_runners.dbt.runner._render_command_for_log` is called. The source pattern is also checked against `base.py:SENSITIVE_ENV_KEY_RE`.
- **Declared domain:** all 5,680 ASCII case assignments of the documented key forms (`password`, `passphrase`, `secret`, `token`, `credential`, `auth`, `api[_-]?key`, `private[_-]?key`, including empty separators), each rendered after both `-e` and `--env` with a sentinel. Additional hand-labeled cases cover empty and delimiter-containing values, repeated entries, mixed case, search substrings, and terminal newlines. For matched keys, expected output is independently specified as `KEY=<redacted>`.
- **Verdict:** normal shape-4 registration passes UNSAT (Z3 `5.0.0`; Python `3.14.7`). Differential classification agrees with pinned CPython `re`, and each of the 5,680 actual helper images equals the expected redacted command; the sentinel is absent. The helper-image conversion row is recorded in `forge-cli_conversion.ndjson` under this wave.
- **Mutation guard:** removing the `api[_-]?key` branch is SAT with witness `api_key` in the recorded family run; the ground-truth callback invokes the same pinned product helper with the weakened regex, confirms the original output is `api_key=<redacted>`, and confirms the weakened helper exposes `CLEAR_SENTINEL`. Status: `reproduced`; this is a sensitivity check, not a product finding.
- **Refuted / narrowed claims:** regex membership alone was not accepted as proof of sink behavior; direct helper replay now confirms the exact output for the stated domain. Delimiters, repeated env arguments, mixed case, and terminal newlines did not expose the sentinel in the tested cases. No claim is made for non-ASCII keys, unlisted keys, arbitrary command-state sequences, or values outside the replay fixtures.

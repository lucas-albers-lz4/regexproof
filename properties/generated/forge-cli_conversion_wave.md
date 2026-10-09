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

Alphabet membership is checked against CPython `re` in `tests/test_forge_cli_harness.py`. The helper-image sinks (`_render_command_for_log`, `redact_secret_text`, `_redact_error_body`, and `LlmConfig.redacted_endpoint`) are separate from the five counted language properties above. The bounded `_render_command_for_log` replay below is regression evidence only until a person adopts its contract.

The conversion rows are emitted in
[`forge-cli_conversion.ndjson`](forge-cli_conversion.ndjson). They record
`ground_truth_status: null` because no SAT witness was produced.

## Stop vs next slice

**Wave 1 idiom slice done.** Do not re-ask URL password charset, Datamesh assignment-value charset, LLM `:287` userinfo charset, JAAS escaped-quote product coverage, or the documented sensitive-key forms. Do not re-ask the unencodable `:280` `[^&]+` query as an ASCII self-cover.

**Next idiom (same cluster, same pin):** copilot-memory x-api-key/Bearer persistence only if it is shown to be a distinct sink from `redact_secret_text`.

**Do not:** packages/LuCI/aidevops/mycelium re-open, Smith drain, `WAVE_CORPORA`, public filing without approval, hostname / JSON `[^"]*` / IPv4-MAC charset, Concat-identity `PRODUCT = MATCH`.

## #648 helper-image replay — `SENSITIVE_ENV_KEY_RE`

- **Counting status:** no property registry entry or conversion row is added. The proposed finite-domain guarantee is pending human adoption; this replay currently ships as regression coverage and adds zero to the product ledger.
- **Proposed contract:** trust `config`; input is provider/operator dbt argv. For the exact enumerated argv fixtures in the declared domain, the pinned `_render_command_for_log` output redacts each documented sensitive value and contains no `CLEAR_SENTINEL`.
- **Pinned product:** `Agenticstiger/forge-cli@efcf8e4c0087def553a737dc1c4eebda5d8a90cd`; source is fetched/materialized at that revision and the actual `fluid_build.build_runners.dbt.runner._render_command_for_log` is called. The source pattern is also checked against `base.py:SENSITIVE_ENV_KEY_RE`.
- **Solver subclaim:** shape 2 proves only that every documented policy key is in the source regex language (`ENV_PRODUCT ⊆ ENV_MATCH`, length at most 32). It does not prove the renderer's output image. This duplicate solver property is omitted from the registry until adoption.
- **Declared replay domain:** all 5,680 ASCII case assignments of the documented key forms (`password`, `passphrase`, `secret`, `token`, `credential`, `auth`, `api[_-]?key`, `private[_-]?key`, including empty separators), each rendered after both `-e` and `--env` with `CLEAR_SENTINEL`. Additional hand-labeled cases cover ordinary and near-miss keys, empty and delimiter-containing values, repeated entries, search substrings, and terminal newlines. For matched keys, tests independently specify and compare the full expected output `KEY=<redacted>`.
- **Mutation guard:** removing the `api[_-]?key` branch is SAT with a key witness in the family run. A separate test replays that exact witness through the pinned helper with the weakened regex; it asserts the original output is redacted and the weakened helper exposes `CLEAR_SENTINEL`. The harness labels this expected SAT as a mutation guard, not as a ground-truthed vulnerability.
- **Evidence gate:** register a conversion property only after human adoption plus the pinned renderer tests, exact-witness mutation replay, differential checks, and full proof/test gates pass. Use `python scripts/z3-verify.py --all --require-ground-truth --require-domain --require-contract --fail-on-property-failure` and the full pytest suite.
- **Refuted / narrowed claims:** regex membership alone is insufficient evidence of sink behavior. Direct helper replay checks exact images only in the finite domain above; no claim is made for arbitrary values, non-ASCII keys, unlisted keys, or every possible command shape. No upstream filing or public disclosure is part of this wave.

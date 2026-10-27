# forge-cli conversion wave 1 — close-out

Pin: `Agenticstiger/forge-cli` @ `efcf8e4c0087def553a737dc1c4eebda5d8a90cd`.
Family: `FC-forge-cli`. Product engine: CPython `re` at the pinned source.
Not in `WAVE_CORPORA`. Idiom buckets: **`secret-redaction`** (`forge-cli_w1`)
and **`helper-image`** (`forge-cli_helper_image`, #648).

Rank: [`forge-cli_rank.json`](forge-cli_rank.json) (vocab keep-15, path filter `fluid_build/`).

## 15 read → 5 asked (4 in `forge-cli_w1`, 1 reclassified into `forge-cli_helper_image`)

| Site | Decision | Why |
|---|---|---|
| `_JAAS_CONFIG_RE` `:218` | **asked** shape 2 (escaped-quote product ⊆ MATCH) | Independent product grammar requires `\"`; MATCH is `(?:[^"\\]|\\.){,2048}`. Not `PRODUCT = MATCH`. |
| `SENSITIVE_ENV_KEY_RE` `:54` | **reclassified** into `forge-cli_helper_image` | Existing shape-2 subclaim retained; #648 adopts the bounded renderer-output guarantee without adding a duplicate solver property. |
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

- At the original wave-1 close-out, 5 human-contract properties were asked (3 shape 1 + 2 independent coverage inclusions), all 5 UNSAT in their declared ASCII domains.
- After #648, the registry still contains 5 product properties: 4 remain in `forge-cli_w1` / `secret-redaction`, and the sensitive-env property is tracked in `forge-cli_helper_image` / `helper-image`. This reuses the existing shape-2 solver query; it does not add a duplicate property.
- 0 SAT product properties. The family has 2 expected-SAT mutation guards; neither is a finding.
- No pattern-class SAT. No `conversion-upstream.jsonl` row. No public forge-cli filing.

The shape-2 solver subclaim proves only that documented policy keys are in the source regex language. The bounded `_render_command_for_log` tests independently exercise the pinned helper's exact output image. The conversion row keeps `result: unsat` and `ground_truth_status: null`; the SAT mutation witness is replayed by a helper-backed callback and remains a mutation guard, not a product finding.

The conversion rows are emitted in
[`forge-cli_conversion.ndjson`](forge-cli_conversion.ndjson).

## Stop vs next slice

**Wave 1 idiom slice done.** Do not re-ask URL password charset, Datamesh assignment-value charset, LLM `:287` userinfo charset, JAAS escaped-quote product coverage, or the documented sensitive-key forms. Do not re-ask the unencodable `:280` `[^&]+` query as an ASCII self-cover.

**Next idiom (same cluster, same pin):** copilot-memory x-api-key/Bearer persistence only if it is shown to be a distinct sink from `redact_secret_text`.

**Do not:** packages/LuCI/aidevops/mycelium re-open, Smith drain, `WAVE_CORPORA`, public filing without approval, hostname / JSON `[^"]*` / IPv4-MAC charset, Concat-identity `PRODUCT = MATCH`.

## #648 adopted helper-image contract — `SENSITIVE_ENV_KEY_RE`

- **Counting status:** human-adopted contract; the existing shape-2 registry entry is named `FC-forge-cli-sensitive-env-helper-redacts` and its conversion row is assigned to `wave_id=forge-cli_helper_image`, `idiom_bucket=helper-image`. No duplicate solver property is registered.
- **Contract:** trust class `config`; input is provider/operator dbt command argv rendered for logging. At the exact pinned source revision and within the bounded test domain, `_render_command_for_log` replaces each documented sensitive environment value with `<redacted>` and does not emit `CLEAR_SENTINEL`.
- **Pinned product:** `Agenticstiger/forge-cli@efcf8e4c0087def553a737dc1c4eebda5d8a90cd`; tests invoke the imported `fluid_build.build_runners.dbt.runner._render_command_for_log` from that checkout and verify the source path and commit. The source pattern remains checked against `base.py:SENSITIVE_ENV_KEY_RE`.
- **Solver subclaim:** shape 2 proves only that the independent documented-key language is included in the source regex language (`ENV_PRODUCT ⊆ ENV_MATCH`, key length at most 32). It does not prove the renderer's output image; the pinned helper tests provide that separate evidence.
- **Declared replay domain:** all 5,680 ASCII case assignments of the documented key forms (`password`, `passphrase`, `secret`, `token`, `credential`, `auth`, `api[_-]?key`, and `private[_-]?key`, including empty separator forms), each rendered after both `-e` and `--env` with `CLEAR_SENTINEL`. Hand-labeled cases additionally cover ordinary and near-miss keys, empty and delimiter-containing values, repeated entries, mixed-case matching, substring search behavior, and embedded/terminal newlines. For sensitive keys, tests compare the exact expected `KEY=<redacted>` output and assert the sentinel is absent.
- **Mutation guard:** removing the `api[_-]?key` branch produces the expected SAT sensitivity witness. The registered `ground_truth` callback replays that exact witness through the pinned helper with the normal and weakened regexes; it returns true only when the original output is redacted and the weakened output exposes `CLEAR_SENTINEL`. The runner invokes that callback for `mutation_guard` properties and fails the property when replay returns false, so `--require-ground-truth` enforces the replay instead of only labelling it. This remains a mutation guard, not a vulnerability finding.
- **Shape:** the slice plan expected a shape-4 per-command-token query, but the registered query is shape 2. A monolithic image regex over the renderer's output TIMEOUTs (the shape-4 caveat in `AGENTS.md`), and encoding the renderer faithfully would re-implement the product rather than describe it. The row therefore counts the shape-2 membership subclaim, and the output image is proven by the pinned helper tests instead. The ledger shape-mix reflects that split honestly.
- **Verification:** `python scripts/z3-verify.py --all --require-ground-truth --require-domain --require-contract --fail-on-property-failure` passed 75/75. The focused forge-cli tests cover the exact image, CPython `re` differential, mutation replay, and runner-enforced replay; `check_mutation_coverage()` remains enabled. The conversion row records UNSAT with no SAT ground-truth status. Rows were regenerated under CPython 3.13.5 (this host has no 3.14); other corpora rows are already mixed across interpreters.
- **Refuted / narrowed claims:** regex membership alone is insufficient evidence of sink behavior. The renderer claim is finite-domain only; no claim is made for arbitrary values, non-ASCII keys, unlisted keys, or every possible command shape. No upstream filing or public disclosure is part of this wave.

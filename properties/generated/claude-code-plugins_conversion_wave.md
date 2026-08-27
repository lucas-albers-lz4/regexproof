# claude-code-plugins conversion wave 1 — close-out

Pin: `melodic-software/claude-code-plugins` @ `f44d0df5e7bf023b88cccc37301402ba7f9dcdb1`.
Family: `AI-claude-plugins`. Product engine: BusyBox (`grep -E` at bash `=~`
search sites; `sed -E` at the skill-ref substitution; GNU not consulted).
Not in `WAVE_CORPORA`. Not mixed into `OW-packages` / `OW-luci` / `AI-aidevops`
/ `MY-mycelium`. ECMA skills/MCP were not in this family.
Asked: **3** human contracts (ledger `properties_asked` 29 → 32).
Idiom bucket: **`plugin-hook-guards`**.

Rank: [`claude-code-plugins_rank.json`](claude-code-plugins_rank.json)
(vocab keep-15, path filter `plugins/guardrails/hooks/`).

## 15 read → 3 asked

| Site | Decision | Why |
|---|---|---|
| block-hook-bypass drive `^([A-Za-z]):(/.*)?$` `:767` | skip | `[A-Za-z]` letter class sibling of asked git-clean `-e` bundle; group-1 is a single letter (tautological capture). |
| cli-flag-verify `^(--[a-zA-Z][a-zA-Z0-9-]*)` `:247` | **asked** shape 1 (no `;`) | New alphabet `[--A-Za-z0-9-]` → `<bin> --help` flag verify. |
| hook-utils env peel `^-[i0v](.+)$` `:1348` | skip | Internal GNU-env option peel (`internal`). |
| hook-utils timeout duration `:1485` | skip | Internal `timeout` wrapper skip (`internal`). |
| hook-utils `read -t` micros `:574` / `:576` / `:621` | skip | Internal stdin-timeout parse; digit class sibling of aidevops deny-list. |
| hook-utils env-assign `:950` | skip | Credential-subject bail; ident class sibling of aidevops `remote_url`. |
| skill-reference `/plugin:skill` `:290` | **asked** shape 1 (no `;`) | New alphabet `[/[a-z0-9:-]]` → marketplace skill-dir resolve. Shape-3 vs space trailer is Concat-identity (ref class cannot contain space). |
| block-dangerous-git `-e` bundle `:1055` | **asked** shape 1 (no `;`) | New alphabet `[-A-Za-z]` with required `e` → irreversible `git clean -f` block. |
| block-dangerous-git `-e` bundle `:1087` | skip | Sibling of asked `:1055` (dry-run pre-scan vs force scan). |
| block-dangerous-git short bundle `:1257` | skip | `[A-Za-z]` sibling of asked `-e` bundle. |
| block-dangerous-git lease OID hex `:338` | skip | Hex class sibling of digit-semicolon deny-list. |
| block-dangerous-git tree-wide pathspec `:549` / `:553` | skip | Internal `.`/`*`/`?` pathspec classifier, not a charset sink. |

## Results

- 3 expected-UNSAT (3 shape 1). No sound shape-3 in this bucket (skill-ref
  space trailer is Concat-identity; drive-letter group-1 is a single letter).
  Mix allows 2–3 shape 1; prefer solid alphabets over a fake capture.
- 0 SAT. Prevalence datapoint for this idiom slice.
- Mutation coverage: `AI-claude-plugins-mutated-cli-flag-semicolon`.

No pattern-class SAT. No `conversion-upstream.jsonl` row. No public
claude-code-plugins filing.

Acceptance: harness runs with `--require-contract --require-ground-truth`;
every property has `kind=` / `family=AI-claude-plugins`. Shape-1 fidelity is
BusyBox alphabet spot-checks (`ci-check-busybox-claude-code-plugins.py`).

## Stop vs next slice

**Wave 1 idiom slice done.** Do not re-ask CLI long-flag charset, `/plugin:skill`
ref charset, or git-clean `-e` short-option bundle charset. Do not re-ask
hostname / JSON `[^"]*` / digit-semicolon / brief t-ID / ssh-key / awg-dialect
/ ALPN.

**Next idiom (deferred, not registered):** ECMA under skills/MCP (`*.mjs` /
`*.js`) — later dialect decision, not a posix-shell wave 2. Scheduler
`DESIGN_TAIL` `ecma-plugins` stays unregistered (fail-closed). Remaining
posix-shell (`plugins/*/hooks/hook-utils.sh` copies, `lib/powershell/`) is not
a silent expand of `plugins/guardrails/hooks/`. Do **not** start another
cluster. Do **not** mix plugin JS into family `AI-claude-plugins`.

**Do not:** packages/LuCI/aidevops/mycelium re-open, Smith drain, `WAVE_CORPORA`,
public filing without approval, another digit-no-semicolon alphabet, JSON
`[^"]*`, hostname/IPv4/MAC/IPv6 charset, tautological Concat-identity shape-3.

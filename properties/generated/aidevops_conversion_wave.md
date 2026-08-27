# aidevops conversion wave 1 — close-out

Pin: `marcusquinn/aidevops` @ `8666b6c6c52472b5535aa295f2df593918152cb1`.
Family: `AI-aidevops`. Product engine: BusyBox `grep`/`sed` (bash `=~` replayed as ERE).
Not in `WAVE_CORPORA`. Not mixed into `OW-packages` / `OW-luci`.
Asked: **5** human contracts (ledger `properties_asked` 21 → 26).
Idiom bucket: **`shell-hook-guards`**.

Rank: [`aidevops_rank.json`](aidevops_rank.json) (vocab keep-15, path filter `.agents/hooks/`).

## 15 read → 5 asked

| Site | Decision | Why |
|---|---|---|
| brief-filename `(t[0-9]+)` `:105` | **asked** shape 3 (hyphen-free UNSAT) | Capture identity → `git log --grep` claim lookup. |
| credential `+++ b/(.*)$` `:77` | skip | `(.*)$` identity is tautological; sibling of hunk capture. |
| credential hunk `+([0-9]+)` `:90` | skip | Digit line-number sibling of asked `#[0-9]+` gh extract. |
| task-id Resolves/Closes `#NNN` `:377` | skip as first grep | Asked the extract `#[0-9]+` `:378` in the same function (gh sink). |
| brief-filename `t[0-9]+-brief.md` `:84` | **asked** shape 1 (no `;`) | New alphabet `[t0-9]` → git log --grep. |
| complexity `\.(sh|py)$` `:144` | skip | Suffix filter; helper is invoked with `--base` SHA, not the path. |
| credential `$remote_url\|$origin_url` `:103` | **asked** shape 1 (no `;`) | New ident alphabet `[a-z_]` → unsanitized emit detector. |
| credential `^[[:space:]]` `:111` | skip | Diff context line counter (`internal`). |
| credential `^\+[^+]` `:96` | skip | Added-line detector, not a charset/capture sink. |
| scope-guard Files Scope heading `:137` | **asked** shape 1 (no `;`) | New heading alphabet → scope-guard fail-closed. |
| scope-guard `grep -qE` Files Scope `:177` | skip | Sibling of asked bash `=~` heading. |
| task-id `^[0-9]+$` counter `:116`/`:129`/`:278`/`:315` | skip | Digit class sibling of asked gh issue capture. |
| task-id `#[0-9]+` `:378` | **asked** shape 3 (digit-only UNSAT) | Capture identity → `gh issue view`. |

## Results

- 5 expected-UNSAT (3 shape 1 + 2 shape 3 capture identity).
- 0 SAT. Prevalence datapoint for this idiom slice.
- Mutation coverage: `AI-aidevops-mutated-brief-tid-semicolon`.

No pattern-class SAT. No `conversion-upstream.jsonl` row. No public aidevops filing.

Acceptance: harness runs with `--require-contract --require-ground-truth`; every property has `kind=` / `family=AI-aidevops`. Expected-UNSAT shape-3 fidelity is BusyBox differential fuzz (`ci-check-busybox-aidevops.py`).

## Stop vs next slice

**Wave 1 idiom slice done.** Do not re-ask brief `t[0-9]+` charset/capture, credential `remote_url`/`origin_url` ident, Files Scope heading charset, or `#[0-9]+` issue capture.

**Next idiom (deferred, not registered):** ECMA under `.agents/plugins/opencode-aidevops/` — later dialect decision, not a posix-shell wave 2. Scheduler `DESIGN_TAIL` `ecma-plugins` stays unregistered (fail-closed). Do **not** start another cluster. Do **not** mix plugin JS into family `AI-aidevops`.

**Do not:** packages/LuCI re-open, Smith drain, `WAVE_CORPORA`, public filing without approval, another digit-no-semicolon alphabet, JSON `[^"]*`, hostname/IPv4/MAC/IPv6.

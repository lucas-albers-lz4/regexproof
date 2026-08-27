# mycelium conversion wave 1 — close-out

Pin: `mycelium0/mycelium` @ `4b53dc7629ca3bc88bf5467db481ad2af7130711`.
Family: `MY-mycelium`. Product engine: BusyBox (`grep -E` at search sites;
GNU not consulted).
Not in `WAVE_CORPORA`. Not mixed into `OW-packages` / `OW-luci` / `AI-aidevops`.
`tests/conformance` was Gate 1 drop (no boundary).
Asked: **3** human contracts (ledger `properties_asked` 26 → 29).
Idiom bucket: **`control-failclosed`**.

Rank: [`mycelium_rank.json`](mycelium_rank.json) (vocab keep-15, path filter `control/`).

## 15 read → 3 asked

| Site | Decision | Why |
|---|---|---|
| awg-issue last octet `([0-9]+)/` `:639` | skip | Concat-identity: `Concat(octet, "/", mask)` then `SubString` to `/` is tautological UNSAT when octet is digits (no slash). Delimiter-free prevalence is not a sound shape-3. |
| donor ALPN h2 line `:158` | **asked** shape 1 (no `;`) | New alphabet (ALPN protocol line) → pick_donor REALITY cover preference. |
| harden sshd `port` strip `:477` | skip | Digit class sibling of aidevops `#[0-9]+` / digit-no-semicolon deny-list. |
| harden `authorizedkeysfile` strip `:58` | skip | Prefix-strip remainder is tautological; path alphabet is not in the pattern. |
| harden sshd key prefix `:74` | **asked** shape 1 (no `;`) | New alphabet `[ssh-ed25519\|ssh-rsa\|ecdsa-\|sk-]` → key-only harden anti-lockout. |
| identity `PrivateKey:` strip `:24` | skip | Prefix-strip `(.*)$` identity; sibling of myceliumctl key parse. |
| identity `PublicKey:` strip `:25` | skip | Sibling of asked-skip PrivateKey. |
| install `Xray` version strip `:171` | skip | Internal pin skip; `[0-9.]` is IPv4-charset class. |
| install sing-box `version` strip `:42` | skip | Sibling of Xray version pin. |
| region-exclude whitespace trim `:150` | skip | Trim helper; no charset/capture sink. |
| tunnel `.[0-9]+/[0-9]+$` rewrite `:174` | skip | Substitution image sibling of last-octet Concat-identity skip. |
| AWG dialect keys `:434` | **asked** shape 1 (no `;`) | New alphabet `[Jc\|Jmin\|Jmax\|S1\|S2\|H1–H4]` → fail-closed awg-regen. |
| revoke empty-line count `:869` | skip | Internal arithmetic (`internal`). |
| revoke empty-line count `:870` | skip | Sibling of `:869`. |
| params `DNS:*.[A-Za-z0-9.-]+` `:366` | skip | Hostname charset deny-list (aidevops / packages close-out). |

## Results

- 3 expected-UNSAT (3 shape 1). No sound shape-3 in this bucket (Concat-identity / delimiter-free prevalence not filed as shape-3). Mix allows 2–3 shape 1; prefer solid alphabets over a fake capture.
- 0 SAT. Prevalence datapoint for this idiom slice.
- Mutation coverage: `MY-mycelium-mutated-ssh-key-semicolon`.

No pattern-class SAT. No `conversion-upstream.jsonl` row. No public mycelium filing.

Acceptance: harness runs with `--require-contract --require-ground-truth`; every property has `kind=` / `family=MY-mycelium`. Shape-1 fidelity is BusyBox alphabet spot-checks (`ci-check-busybox-mycelium.py`).

## Stop vs next slice

**Wave 1 idiom slice done.** Do not re-ask sshd key-type prefix charset, AWG dialect-key charset, ALPN h2 line charset, or AllowedIPs last-octet `/` capture (vacuous Concat-identity). Do not re-ask hostname / JSON `[^"]*` / digit-semicolon / brief t-ID.

**Next idiom (deferred, not registered):** posix-shell under `scripts/` (`node-bootstrap.sh`, `fungi`) — later path-slice, not a silent expand of `control/`. Scheduler `DESIGN_TAIL` `scripts-bootstrap` stays unregistered (fail-closed). Do **not** start another cluster. Do **not** mix Go `internal/diag` redact into family `MY-mycelium`.

**Do not:** packages/LuCI/aidevops re-open, Smith drain, `WAVE_CORPORA`, public filing without approval, another digit-no-semicolon alphabet, JSON `[^"]*`, hostname/IPv4/MAC/IPv6 charset, tautological key prefix-strips, Concat-identity shape-3.

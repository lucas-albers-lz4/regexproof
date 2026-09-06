# dogfood_shell conversion wave 1 — close-out

Pin: dogfooding universe (usrmanage / fwlive / happycow / hermes-agent-fork).
Extraction at current HEAD (2026-09-06): 6,648 total sites
(ecma 3,460 / posix-shell 1,670 / py_re 1,518) vs 2,856 frozen at the
P1 pins (2026-08-12) — the universe moved (3/4 repos drifted; see
`batch/corpora/dogfood_shell/README.md` for the pin-refresh rule).
Family: `DF-dogfood-shell`. Product engine: `sed` running the exact
shipped `normalize_log_prefix` script (BusyBox on device, GNU on host).
Asked: **2** human contracts (ledger `properties_asked` 32 → 34).
Idiom bucket: **`normalize-fixpoint`**.

## 2 asked (both shape 3, both UNSAT)

| Site | Decision | Why |
|---|---|---|
| fwlive:97 `normalize_log_prefix` fixpoint | **asked** shape 3 (no trailing strip-class char) | Known-true gap: Z3 F1–F4 verify membership, never idempotency; guards the fwlive #250 drift class. |
| fwlive:97 `normalize_log_prefix` idempotency | **asked** shape 3 (`N(N(x)) == N(x)`) | The exact #250 property: one-colon-per-call stripping drifted backends. |

## Results

- 2 expected-UNSAT, 0 SAT. Prevalence datapoint for this idiom slice.
- Mutation coverage: `DF-dogfood-shell-normalize-mutated-colon`
  (colon dropped — the exact 2026-08 regression, witness `:` replays
  through weakened sed) + `DF-dogfood-shell-normalize-mutated-once`
  (single-strip, witness ` :`).
- Ground truth: mirror ≡ BusyBox `sed` on 300 random + 85 exhaustive
  inputs (`ci-check-busybox-dogfood-shell.py`); shipped function
  idempotency replayed under `dash` on `zz::`.

No pattern-class SAT. No `conversion-upstream.jsonl` row (expected-UNSAT
prevalence; fwlive is first-party dogfood, not a third-party filing).

Acceptance: harness runs with `--require-contract --require-ground-truth`;
every property has `kind=` / `family=DF-dogfood-shell`. Expected-UNSAT
shape-3 fidelity is BusyBox sed differential fuzz
(`ci-check-busybox-dogfood-shell.py`).

## Stop vs next slice

**Wave 1 idiom slice done.** Do not re-ask normalize fixpoint/idempotency.

**Next idiom (deferred, not registered):** the remaining 1,669 shell
sites (usrmanage 1,274 strong) — a later slice ranks them; scheduler
`DESIGN_TAIL` stays unregistered (fail-closed). Do **not** start another
cluster. Do **not** mine the ecma/py_re fractions of the dogfood
universe under family `DF-dogfood-shell` (shell is the novelty).

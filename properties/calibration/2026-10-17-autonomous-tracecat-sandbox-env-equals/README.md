# Tracecat nsjail environment-key separator contract

**Source:** `TracecatHQ/tracecat@c84d52528a489821f355fc63976fbc7783ae0ad5`
**Tree:** `b4af14482f3483605e41307d54f2b777b63bbd84`
**Inventory row:** `914d08c870f219be6f093e8caa0ab3dc` at
`tracecat/sandbox/executor.py:71:23`
**Adoption:** agent-derived under the standing delegation in
[`AUTONOMOUS-CONTRACTS.md`](../../../docs/AUTONOMOUS-CONTRACTS.md)

## Contract and source path

The input is a Python environment-key string. In the `core.script.run_python`
path, user-authored workflow `args.env_vars` are copied into the sandbox
environment by `ExecutorBackend._execute_run_python`, passed through
`SandboxService.run_python`, and validated by `NsjailExecutor._build_env_map`
when nsjail is selected. The validator runs before the key is inserted into
the environment map. The executor then passes each key as an `--env` argument
and passes the map to `asyncio.create_subprocess_exec`. Registry-action SDK
environment keys use the same validator through `_build_action_env_map`.

The independent contract is deliberately narrow: an accepted environment
name contains no `=`. POSIX environment entries have the form `name=value`,
and the name cannot contain the equals byte ([Open Group POSIX.1-2024,
Environment Variables](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap08.html)).
The source comment says the pattern is POSIX compliant, but `.match()` with
Python `$` also accepts one terminal line feed. This contract does not claim
full POSIX name validity, value safety, sandbox isolation, or behavior in the
unsafe PID fallback. Python's `subprocess` independently rejects `=` inside
an environment key, so this gate records defense in depth, not a current
vulnerability or impact.

## Proof and gate

- `TC-sandbox-env-key-excludes-equals` uses the documented shape-1 alphabet
  proof. Every character admitted by the identifier classes or the possible
  final LF is disjoint from `=`. The proof is unbounded in key length and
  returned UNSAT in 0.2 ms in the P6 run.
- `TC-sandbox-env-key-equals-mutation` weakens the exact tail class to admit
  `=`. The Z3 witness `TRACE=TOKEN` replays against the exact pinned validator.
  It is a mutation guard, not a product SAT candidate.
- The exact-source gate verifies the pinned file digest, the input-to-nsjail
  source path, and validation before environment-map insertion. It compares
  the isolated exact validator with an independent model over 4,232
  deterministic inputs: zero mismatches. It also confirms Python's
  subprocess layer rejects an equals-sign key. The model comparison is
  differential evidence; it is not a test of the nsjail binary.
- The bounded P6 wave measured 18.2 ms source verification, 29.9 ms mutation
  replay, 0.2 ms solver time, and 1,438.1 ms local gate time: a 1.4864-second
  phase sum. The local P6 roster, state, checkpoint, and gate report are under
  [`p6-wave/`](p6-wave/).
- The standalone gate is wired into the proof CI job. Hosted CI has not yet
  been observed.

The first local encoding attempt used a whole-string `Contains` query and
timed out at its 30-second solver cap; its mutation replay also exposed a
callback witness-key mismatch. Both development failures are recorded in
[`development-attempts.json`](development-attempts.json). The solver query
was decomposed to the repo's documented shape-1 alphabet encoding, and the
mutation callback was corrected before the P6 wave. These were iterations of
the same contract, not additional product questions.

## Outcomes and artifacts

This adds one UNSAT contract-backed proof and one local regression gate. The
mutation SAT is only a sensitivity check. It adds no bug candidate, reachable
violation, confirmed security impact, upstream report, maintainer confirmation,
or fix. Source review and contract authoring were not timed; token use, cost,
and human active time are unknown.

- [`contract.json`](contract.json)
- [`product-gate.json`](product-gate.json)
- [`P6 wave artifacts`](p6-wave/)
- [`autonomous run measurement`](../../generated/autonomous_work.jsonl)
- [`cohort scorecard snapshot`](scorecard-after-tracecat-sandbox-env-key.json)
- [`P2 v27 retrospective checkpoint`](../2026-10-17-p2-existing-evidence-20r2-v27/README.md)
- [`Tracecat full source review`](../2026-10-16-p2-tracecat-full-source-review/README.md)

Reproduce the source gate and proof:

```sh
.venv/bin/python scripts/tracecat-sandbox-env-key-regression-gate.py \
  --source-root /tmp/tracecat-p2-review-20261016 \
  --output properties/calibration/2026-10-17-autonomous-tracecat-sandbox-env-equals/product-gate.json
```

Reproduce the bounded P6 wave with its frozen roster:

```sh
.venv/bin/python scripts/run-autonomous-proof-wave.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --roster properties/calibration/2026-10-17-autonomous-tracecat-sandbox-env-equals/p6-wave/roster.json \
  --state-dir properties/calibration/2026-10-17-autonomous-tracecat-sandbox-env-equals/p6-wave/state \
  --wave-id tracecat-sandbox-env-equals-20261017 \
  --corpus tracecat_sandbox_env_equals \
  --idiom-bucket sandbox-environment-key-separator \
  --checkout TracecatHQ/tracecat=/tmp/tracecat-p2-review-20261016 \
  --gate properties/calibration/2026-10-17-autonomous-tracecat-sandbox-env-equals/p6-wave/gate-config.json
```

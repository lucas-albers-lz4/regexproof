# Forge CLI autonomous-flow integration fixture

This directory records a real pinned-source integration of the autonomous
contract, roster, proof, replay, mutation, emission, and v3-checkpoint paths.
It is a **retrospective integration fixture**, not an unbiased campaign sample:
the six Forge questions already existed in the harness when this roster was
frozen. Do not use its six-question rate as prospective yield or as the 20-r2
cohort result.

The roster binds five existing human contracts and one `agent_derived` helper
image contract to the Forge CLI pin in the frozen 20-r2 cohort. The helper
contract is source-bound to `fluid_build/build_runners/base.py` and cites the
dbt caller. The local gate invokes the pinned renderer against all 5,680 ASCII
letter-case assignments, checks additional labeled argv/value cases, and runs
the family mutation guard.
[`gate.json`](gate.json) records the argv command, the six covered contract
IDs, and the helper-specific product replay and differential-case evidence.

## Recorded result

- 6 adopted identities; 6 solver attempts; 6 decided UNSAT rows.
- 1 replay through the actual pinned product helper; 5,680 differential cases
  for its helper-image property; 1 unique local runnable regression gate.
- 0 consumer-adopted gates, SAT candidates, confirmed bugs, external reports,
  maintainer confirmations, or fixes in this fixture.
- Cost, token use, elapsed agent work, and human active minutes are unknown;
  this fixture does not infer them from solver or test runtime.

The six UNSAT rows are contract-backed proofs, but only the helper-image row
is counted as replayed against the actual product implementation or covered by
the useful local gate. The other five rows reuse legacy human contracts and
remain useful proof observations in this retrospective fixture; this run does
not claim new product replay evidence for them. The bug-discovery and external
outcome tracks remain separate and empty here. An eventual externally
confirmed bug or fix should link back to its affected contract and can seed
another proof/gate revision.

## Reproduction

From the repository root, freeze the identities before executing the local
gate, emit conversion rows, and build/check the strict v3 checkpoint:

```sh
.venv/bin/python scripts/freeze-product-roster.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --contracts properties/calibration/2026-10-13-autonomous-forge-cli-integration/contracts.json \
  --out properties/calibration/2026-10-13-autonomous-forge-cli-integration/roster.json
.venv/bin/python -m pytest -q tests/test_forge_cli_harness.py
.venv/bin/python scripts/emit-conversion-ndjson.py \
  --family FC-forge-cli --corpus forge-cli --wave-id forge-cli_w1 \
  --idiom-bucket secret-redaction \
  --output properties/calibration/2026-10-13-autonomous-forge-cli-integration/conversion.ndjson
.venv/bin/python scripts/build-autonomous-checkpoint.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --roster properties/calibration/2026-10-13-autonomous-forge-cli-integration/roster.json \
  --attempts properties/calibration/2026-10-13-autonomous-forge-cli-integration/attempts.json \
  --conversion-rows properties/calibration/2026-10-13-autonomous-forge-cli-integration/conversion.ndjson \
  --out properties/calibration/2026-10-13-autonomous-forge-cli-integration/checkpoint.json
.venv/bin/python scripts/conversion-checkpoint.py \
  properties/calibration/2026-10-13-autonomous-forge-cli-integration/checkpoint.json
```

`attempts.json` records the measured gate result and should be regenerated only
after the referenced local test command passes. The checkpoint reports six
observations and a 44-question shortfall against the 50-question evaluation
checkpoint; it does not close P7 or imply a corpus coverage stop.

The resumable runner accepts at most five adopted contracts per wave, so this
six-question historical roster is intentionally not a runnable P6 input. For a
prospective wave, freeze a roster of at most five first, then create a gate
config whose coverage IDs are a subset of that roster. The runner requires the
cohort, roster, state directory, wave ID, corpus, idiom bucket, and one exact
clean source checkout per repository; `--dry-run` checks the pins and
`--status` reads the immutable resume state. Re-running this historical roster
would still not count as prospective P7 yield.

Operator command shape:

```sh
.venv/bin/python scripts/run-autonomous-proof-wave.py \
  --cohort <cohort-manifest.json> --roster <frozen-roster-of-up-to-five.json> \
  --state-dir <new-wave-state-dir> --wave-id <unique-wave-id> \
  --corpus <corpus-id> --idiom-bucket <registered-bucket> \
  --checkout <repo-id>=<clean-pinned-checkout> --gate <wave-gate.json> \
  --dry-run
```

Remove `--dry-run` to execute. To inspect or resume, use the same cohort,
roster, wave ID, corpus, idiom bucket, campaign, and gate config. Resume
requires a checkout for each rostered repository, while `--status` reads the
state without a checkout.

# Doberman Windows secret-path calibration

This is a one-question, source-pinned 20-r2 calibration for
`fu351/Doberman-Core@53ae43c5298a2426c6696147fdd75e2a4aef10e2`, at
`src/doberman/engine/rules/secrets.py:223` (`_SECRET_PATH`). It is retrospective
evidence, not a sampled conversion wave or a claim about prevalence.

## Contract and result

The adopted contract covers untrusted drive-absolute Windows paths ending in
`.npmrc` or `credentials`. The source comment classifies these as secret
stores, and the reason-code documentation requires the secret-file rule to
return `AUTH`. The path supplied to `fs_read` is preserved by normalization.
The regex requires `/` before these basenames, so a native Windows path using
backslashes is missed. The exact source file SHA-256 is
`a73b183b5ac0da101e1411384e12ffe7da9f48f59947ec76a447974e246179fa`; the
contract was autonomously adopted under the standing delegation. See
[`contract.json`](contract.json) for the declared input domain, source evidence,
and adoption digest.

The formal `bug_demo` is SAT at `k:\P\.npmrc`; its ground-truth callback runs
the Python `re` engine with the pinned source pattern. A `mutation_guard`
weakening the credentials alternative is also SAT. The local product gate
imports the pinned `normalize`, `_SECRET_PATH`, `SecretLeakageRule`, and full
`ObjectiveGuardrail`: both native-backslash Windows-shaped targets return
`PASS`, while slash-separated drive-path controls return `AUTH`. The gate also
confirms that `.env.local` is covered by the separate default `.env.*`
protected-path rule, so it is not a second candidate. A separator-fix
sensitivity control catches both Windows cases.

The gate ran on Linux with the exact pinned Python implementation and
Windows-shaped strings. `PureWindowsPath` was used to check expected Windows
normalization against the exact default protected-path globs; native Windows
canonicalization was not exercised. The product candidate therefore remains
`pending_product_triage`. No external report was sent. A broader exploratory
POSIX completeness query timed out and had a domain mismatch with this
Windows-path contract; it was discarded and is not a product property or a
checkpoint attempt.

Artifacts include the formal report, product gate report, frozen roster,
source-bound checkpoint, and canonical conversion row. The v5 P2 aggregate
counts this as one unique SAT question, one useful local gate, and one product
engine replay. It does not count the two older Doberman human-contract rows as
having reusable local gates.

A timed proof-and-gate replay is recorded in the agent-only work log. That
interval was 0.811 seconds and included only the formal proof/mutation run and
the pinned product gate; source review, contract adoption, and evidence
assembly were outside it. It counts as one execution retry in the agent
scorecard, not as another unique P2 question. Tokens, cost, and human active
time were not measured.

## Reproduction

Run from the repository root with the pinned source checkout and gate runtime
available at the paths below:

```sh
.venv/bin/python scripts/z3-verify.py \
  PY-doberman-secret-store-windows-miss \
  PY-doberman-secret-store-mutated-missing-credentials \
  --require-ground-truth --require-contract --require-domain \
  --fail-on-property-failure --json \
  > properties/calibration/2026-10-15-autonomous-doberman-win-secret-path-20r2/proof-report.ndjson

PYTHONPATH=/tmp/regexproof-doberman-deps python3 \
  scripts/doberman-secret-path-regression-gate.py \
  --source-root /tmp/regexproof-pinned-sources/Doberman-Core-53ae43c5298a2426c6696147fdd75e2a4aef10e2 \
  --output properties/calibration/2026-10-15-autonomous-doberman-win-secret-path-20r2/gate-report.json

.venv/bin/python scripts/build-doberman-secret-path-evidence.py \
  --source-root /tmp/regexproof-pinned-sources/Doberman-Core-53ae43c5298a2426c6696147fdd75e2a4aef10e2

.venv/bin/python scripts/conversion-checkpoint.py \
  properties/calibration/2026-10-15-autonomous-doberman-win-secret-path-20r2/checkpoint.json
```

Rebuild the retrospective v5 aggregate and validate its emitted checkpoint:

```sh
.venv/bin/python scripts/build-p2-evidence-checkpoint.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-15-p2-source-inventory-v2/inventory.json \
  --sites properties/calibration/2026-10-15-p2-source-inventory-v2/sites.ndjson \
  --checkpoint-root properties/calibration \
  --conversion-root properties/generated \
  --repo-root /home/lalbers/gitroot/regexproof \
  --out-dir properties/calibration/2026-10-15-p2-existing-evidence-20r2-v5

.venv/bin/python scripts/conversion-checkpoint.py \
  properties/calibration/2026-10-15-p2-existing-evidence-20r2-v5/checkpoint.json
```

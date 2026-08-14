# Doberman-Core corpus

Pinned fu351/Doberman-Core first-party policy/secrets/command detectors
(py_re) for Smith triage-trial keep
(see `sweep/accuracy-flywheel/TRIAGE-TRIAL-REVIEW.md`). Tests excluded.

## Materialize

```bash
PIN=53ae43c5298a2426c6696147fdd75e2a4aef10e2
git clone --filter=blob:none https://github.com/fu351/Doberman-Core.git /tmp/Doberman-Core
git -C /tmp/Doberman-Core fetch --depth 1 origin "$PIN"
git -C /tmp/Doberman-Core checkout "$PIN"
ln -sfn /tmp/Doberman-Core batch/corpora/Doberman-Core/rules
test "$(git -C /tmp/Doberman-Core rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/fu351-Doberman-Core_gate_decision.json` (`triage-trial`).
Security-tool: `private_first` via `SECURITY_TOOL_CORPORA`.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus Doberman-Core --assert-determinism
python -m regexproof.batch --corpus Doberman-Core
```

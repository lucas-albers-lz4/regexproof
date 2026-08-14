# devguard corpus

Pinned l3montree-dev/devguard first-party dependency-firewall package-name
regexes (Go re2) for Smith triage-trial keep
(see `sweep/accuracy-flywheel/TRIAGE-TRIAL-REVIEW.md`). Mocks/tests excluded.

## Materialize

```bash
PIN=00c7f6fc3fb20b1656827f8a8e85e603c7f4a77d
git clone --filter=blob:none https://github.com/l3montree-dev/devguard.git /tmp/devguard
git -C /tmp/devguard fetch --depth 1 origin "$PIN"
git -C /tmp/devguard checkout "$PIN"
ln -sfn /tmp/devguard batch/corpora/devguard/rules
test "$(git -C /tmp/devguard rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/l3montree-dev-devguard_gate_decision.json` (`triage-trial`).
Security-tool: `private_first` via `SECURITY_TOOL_CORPORA`.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus devguard --assert-determinism
python -m regexproof.batch --corpus devguard
```

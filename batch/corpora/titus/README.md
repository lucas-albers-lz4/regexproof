# titus corpus

Pinned praetorian-inc/titus secret-scanner validators (Go re2) for Smith
triage-trial keep (see `sweep/accuracy-flywheel/TRIAGE-TRIAL-REVIEW.md`).
Allowlist is `pkg/types/rule.go` plus first-party `pkg/validator/*.go`
(no tests, no vcrtest).

## Materialize

```bash
PIN=57b733f5ed04a59b03514f229c3052ace7473d50
git clone --filter=blob:none https://github.com/praetorian-inc/titus.git /tmp/titus
git -C /tmp/titus fetch --depth 1 origin "$PIN"
git -C /tmp/titus checkout "$PIN"
ln -sfn /tmp/titus batch/corpora/titus/rules
test "$(git -C /tmp/titus rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/praetorian-inc-titus_gate_decision.json` (`triage-trial`).
Security-tool: `private_first` via `SECURITY_TOOL_CORPORA`.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus titus --assert-determinism
python -m regexproof.batch --corpus titus
```

# inhale corpus

Pinned netspooky/inhale YARA pack for Smith triage-trial keep
(see `sweep/accuracy-flywheel/TRIAGE-TRIAL-REVIEW.md`).

## Materialize

```bash
PIN=889bbe2ab4a40a85c7ccd8399b2fd3cfddf539e8
git clone --filter=blob:none https://github.com/netspooky/inhale.git /tmp/inhale
git -C /tmp/inhale fetch --depth 1 origin "$PIN"
git -C /tmp/inhale checkout "$PIN"
ln -sfn /tmp/inhale/YaraRules batch/corpora/inhale/rules
test "$(git -C /tmp/inhale rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/inhale_gate_decision.json` (also `netspooky-inhale_gate_decision.json`; `triage-trial`).
Security-tool: `private_first` via `SECURITY_TOOL_CORPORA`.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus inhale --assert-determinism
python -m regexproof.batch --corpus inhale
```

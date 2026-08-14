# llm-honeypot-intelligence corpus

Pinned Leviticus-Triage/llm-honeypot-intelligence live YARA (`rules/yara` only;
archive snapshots excluded) for Smith triage-trial keep
(see `sweep/accuracy-flywheel/TRIAGE-TRIAL-REVIEW.md`).

## Materialize

```bash
PIN=65624396e263074bb8cb2e049f9a9ec6215ea5c1
git clone --filter=blob:none https://github.com/Leviticus-Triage/llm-honeypot-intelligence.git /tmp/llm-honeypot-intelligence
git -C /tmp/llm-honeypot-intelligence fetch --depth 1 origin "$PIN"
git -C /tmp/llm-honeypot-intelligence checkout "$PIN"
ln -sfn /tmp/llm-honeypot-intelligence/rules/yara batch/corpora/llm-honeypot-intelligence/rules
test "$(git -C /tmp/llm-honeypot-intelligence rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/Leviticus-Triage-llm-honeypot-intelligence_gate_decision.json` (`triage-trial`).
Security-tool: `private_first` via `SECURITY_TOOL_CORPORA`.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus llm-honeypot-intelligence --assert-determinism
python -m regexproof.batch --corpus llm-honeypot-intelligence
```

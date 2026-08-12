# ail-yara-rules corpus

Pinned ail-project/ail-yara-rules YARA pack for Smith triage-trial
[#242](https://github.com/lucas-albers-lz4/regexproof/issues/242)
under umbrella [#240](https://github.com/lucas-albers-lz4/regexproof/issues/240).

Delta pack vs admitted `yara_rules` / other YARA Smith packs. Materialize under
`/tmp/ail-yara-rules` (case-distinct from `/tmp/yara-rules` and
`/tmp/vaccinator-yara-rules`).

## Materialize

```bash
PIN=8e978d5e70084df6d2fae0727677ec4f60e3e639
git clone --filter=blob:none https://github.com/ail-project/ail-yara-rules.git /tmp/ail-yara-rules
git -C /tmp/ail-yara-rules fetch --depth 1 origin "$PIN"
git -C /tmp/ail-yara-rules checkout "$PIN"
ln -sfn /tmp/ail-yara-rules/rules batch/corpora/ail-yara-rules/rules
test "$(git -C /tmp/ail-yara-rules rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/ail-yara-rules_gate_decision.json` (`triage-trial`).
Security-tool: `private_first` via `SECURITY_TOOL_CORPORA`.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus ail-yara-rules --assert-determinism
python -m regexproof.batch --corpus ail-yara-rules
```

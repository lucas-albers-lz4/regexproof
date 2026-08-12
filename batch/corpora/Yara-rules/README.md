# Yara-rules corpus

Pinned bartblaze/Yara-rules YARA pack for Smith triage-trial
[#244](https://github.com/lucas-albers-lz4/regexproof/issues/244)
under umbrella [#240](https://github.com/lucas-albers-lz4/regexproof/issues/240).

Delta pack vs admitted `yara_rules` (YARA-Rules/rules); same dialect/extractor.

## Materialize

```bash
PIN=5cc871d82361de8a80d387ec8bbd01fe4258b4a9
git clone --filter=blob:none https://github.com/bartblaze/Yara-rules.git /tmp/Yara-rules
git -C /tmp/Yara-rules fetch --depth 1 origin "$PIN"
git -C /tmp/Yara-rules checkout "$PIN"
ln -sfn /tmp/Yara-rules/rules batch/corpora/Yara-rules/rules
test "$(git -C /tmp/Yara-rules rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/Yara-rules_gate_decision.json` (`triage-trial`).
Security-tool: `private_first` via `SECURITY_TOOL_CORPORA`.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus Yara-rules --assert-determinism
python -m regexproof.batch --corpus Yara-rules
```

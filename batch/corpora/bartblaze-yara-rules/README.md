# bartblaze-yara-rules corpus

Pinned bartblaze/Yara-rules YARA pack for Smith triage-trial
[#244](https://github.com/lucas-albers-lz4/regexproof/issues/244)
under umbrella [#240](https://github.com/lucas-albers-lz4/regexproof/issues/240).

Slug is owner-prefixed (`bartblaze-yara-rules`) to stay case-distinct from
VaccinatorSec `yara-rules` and admitted `yara_rules`.

## Materialize

```bash
PIN=5cc871d82361de8a80d387ec8bbd01fe4258b4a9
git clone --filter=blob:none https://github.com/bartblaze/Yara-rules.git /tmp/Yara-rules
git -C /tmp/Yara-rules fetch --depth 1 origin "$PIN"
git -C /tmp/Yara-rules checkout "$PIN"
ln -sfn /tmp/Yara-rules/rules batch/corpora/bartblaze-yara-rules/rules
test "$(git -C /tmp/Yara-rules rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/bartblaze-yara-rules_gate_decision.json` (`triage-trial`).
Security-tool: `private_first` via `SECURITY_TOOL_CORPORA`.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus bartblaze-yara-rules --assert-determinism
python -m regexproof.batch --corpus bartblaze-yara-rules
```

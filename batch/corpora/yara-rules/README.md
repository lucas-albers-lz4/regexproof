# yara-rules corpus

Pinned VaccinatorSec/yara-rules tiny YARA pack for Smith triage-trial
[#247](https://github.com/lucas-albers-lz4/regexproof/issues/247)
under umbrella [#240](https://github.com/lucas-albers-lz4/regexproof/issues/240).

Slug `yara-rules` (hyphen) is case-distinct from admitted `yara_rules` and
owner-prefixed `bartblaze-yara-rules`. Materialize under
`/tmp/vaccinator-yara-rules` so clone path stays distinct from
`/tmp/yara-rules` (YARA-Rules/rules) on case-insensitive filesystems.

## Materialize

```bash
PIN=1d7c4faed70fae431b8189c904881cc0e12436e6
git clone --filter=blob:none https://github.com/VaccinatorSec/yara-rules.git /tmp/vaccinator-yara-rules
git -C /tmp/vaccinator-yara-rules fetch --depth 1 origin "$PIN"
git -C /tmp/vaccinator-yara-rules checkout "$PIN"
ln -sfn /tmp/vaccinator-yara-rules/rules batch/corpora/yara-rules/rules
test "$(git -C /tmp/vaccinator-yara-rules rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/yara-rules_gate_decision.json` (`triage-trial`).
Security-tool: `private_first` via `SECURITY_TOOL_CORPORA`.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus yara-rules --assert-determinism
python -m regexproof.batch --corpus yara-rules
```

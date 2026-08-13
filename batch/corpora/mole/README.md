# mole corpus

Pinned mole-ids/mole yara pack for Smith GO admit
[#323](https://github.com/lucas-albers-lz4/regexproof/issues/323)
under umbrella [#317](https://github.com/lucas-albers-lz4/regexproof/issues/317).

Network IDS with **NOVEL OT-protocol rules** (modbus/Siemens-S7/OPC-UA/
MQTT/SLMP — industrial protocols, not covered by any admitted corpus).
Measured **67/68 = 0.9853 encodable** (complete, deterministic).

## Materialize

```bash
PIN=eb5356d56e914552d6b1c8dc822f19bd6f0e5774
git clone --filter=blob:none https://github.com/mole-ids/mole.git /tmp/mole
git -C /tmp/mole fetch --depth 1 origin "$PIN"
git -C /tmp/mole checkout "$PIN"
ln -sfn /tmp/mole batch/corpora/mole/rules
test "$(git -C /tmp/mole rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/mole_gate_decision.json` (`triage-trial`).
Smith: `properties/generated/mole_smith_decision.json` (`go`).
Security tool → `private_first` via `SECURITY_TOOL_CORPORA`.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus mole --assert-determinism
python -m regexproof.batch --corpus mole
```

## Notes

- The OT-protocol rule family is the corpus's novelty: industrial-ICS
  detection rules absent from the other 8 admitted yara packs. **Novelty
  CONFIRMED by rule_diff (2026-08-13)**: 235 OT rules across 13 protocol
  files; zero rule-level coverage in any admitted corpus (other packs'
  keyword hits are literal names like `CRC16_MODBUS`, not signatures);
  zero exact regex-literal overlap across the full admitted inventory set.
  Full analysis: `batch/corpora/mole-ot-rule-diff.md`.

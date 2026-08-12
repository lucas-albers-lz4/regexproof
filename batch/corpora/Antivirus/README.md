# Antivirus corpus

Pinned smartytinker/Antivirus yara pack for Smith GO admit
[#345](https://github.com/lucas-albers-lz4/regexproof/issues/345)
under umbrella [#343](https://github.com/lucas-albers-lz4/regexproof/issues/343).

Yara-based antivirus. 710 yara files measured **6,825/11,769 = 0.5799
encodable** (complete, deterministic) with 50 findings.

## Materialize

```bash
PIN=2d7fea93eca3be3df4ad7087e339d21bcd915103
git clone --filter=blob:none https://github.com/smartytinker/Antivirus.git /tmp/Antivirus
git -C /tmp/Antivirus fetch --depth 1 origin "$PIN"
git -C /tmp/Antivirus checkout "$PIN"
ln -sfn /tmp/Antivirus/rules batch/corpora/Antivirus/rules
test "$(git -C /tmp/Antivirus rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/Antivirus_gate_decision.json` (`go`).
Smith: `properties/generated/Antivirus_smith_decision.json` (`go`).
Security tool → `private_first` via `SECURITY_TOOL_CORPORA`.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus Antivirus --assert-determinism
python -m regexproof.batch --corpus Antivirus
```

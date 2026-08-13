# detekt corpus

Pinned eReader/detekt yara pack for Smith GO admit
[#340](https://github.com/lucas-albers-lz4/regexproof/issues/340)
under umbrella [#335](https://github.com/lucas-albers-lz4/regexproof/issues/335).

Spyware-detection tool. 9 yara files (njrat/gh0st/finfisher/darkcomet/rcs
RAT families). Measured **165/245 = 0.6735 encodable** (complete,
deterministic) with 10 findings.

## Materialize

```bash
PIN=14aea88a5ff4cb2840d3712dbd8a85078cd03b28
git clone --filter=blob:none https://github.com/eReader/detekt.git /tmp/detekt
git -C /tmp/detekt fetch --depth 1 origin "$PIN"
git -C /tmp/detekt checkout "$PIN"
ln -sfn /tmp/detekt batch/corpora/detekt/rules
test "$(git -C /tmp/detekt rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/detekt_gate_decision.json` (`triage-trial`).
Smith: `properties/generated/detekt_smith_decision.json` (`go`).
Security tool → `private_first` via `SECURITY_TOOL_CORPORA`.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus detekt --assert-determinism
python -m regexproof.batch --corpus detekt
```

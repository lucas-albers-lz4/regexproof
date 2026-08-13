# binaryalert corpus

Pinned airbnb/binaryalert yara pack for Smith GO admit
[#303](https://github.com/lucas-albers-lz4/regexproof/issues/303)
under umbrella [#299](https://github.com/lucas-albers-lz4/regexproof/issues/299).

Airbnb binary-alerting service. 81 yara files measured **592/911 =
0.6498 encodable** (complete, deterministic) — graduated from triage-trial.

## Materialize

```bash
PIN=a9c0f06affc35e1f8e45bb77f835b92350c68a0b
git clone --filter=blob:none https://github.com/airbnb/binaryalert.git /tmp/binaryalert
git -C /tmp/binaryalert fetch --depth 1 origin "$PIN"
git -C /tmp/binaryalert checkout "$PIN"
ln -sfn /tmp/binaryalert/rules batch/corpora/binaryalert/rules
test "$(git -C /tmp/binaryalert rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/binaryalert_gate_decision.json` (`triage-trial`).
Smith: `properties/generated/binaryalert_smith_decision.json` (`go`).
Security tool → `private_first` via `SECURITY_TOOL_CORPORA`.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus binaryalert --assert-determinism
python -m regexproof.batch --corpus binaryalert
```

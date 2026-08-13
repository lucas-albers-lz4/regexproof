# python_3_8_2 corpus

Pinned vmssoftware/python_3_8_2 first-party py_re allowlist for Smith GO
admit [#358](https://github.com/lucas-albers-lz4/regexproof/issues/358)
under umbrella [#356](https://github.com/lucas-albers-lz4/regexproof/issues/356).

Python 3.8.2 fork. Top-60 .py files measured **501/975 = 0.5138 encodable**
(complete, deterministic) with 135 findings.

## Materialize

```bash
PIN=06cdf3fc9ae103afc55cbd5657ba7c7d09120a81
git clone --filter=blob:none https://github.com/vmssoftware/python_3_8_2.git /tmp/python_3_8_2
git -C /tmp/python_3_8_2 fetch --depth 1 origin "$PIN"
git -C /tmp/python_3_8_2 checkout "$PIN"
ln -sfn /tmp/python_3_8_2 batch/corpora/python_3_8_2/rules
test "$(git -C /tmp/python_3_8_2 rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/python_3_8_2_gate_decision.json` (`go`).
Smith: `properties/generated/python_3_8_2_smith_decision.json` (`go`).
NOT a security tool → public-first disclosure.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus python_3_8_2 --assert-determinism
python -m regexproof.batch --corpus python_3_8_2
```

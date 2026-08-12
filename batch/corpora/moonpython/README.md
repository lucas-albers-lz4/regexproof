# moonpython corpus

Pinned moonbit-community/moonpython first-party py_re allowlist for Smith
GO admit [#336](https://github.com/lucas-albers-lz4/regexproof/issues/336)
under umbrella [#335](https://github.com/lucas-albers-lz4/regexproof/issues/335).

Python interpreter in MoonBit. Top-60 .py files measured **585/1,251 =
0.4676 encodable** (complete, deterministic) with 129 findings.

## Materialize

```bash
PIN=03f07eadcef3b4a4b9592d7d62703a6840e3e5d5
git clone --filter=blob:none https://github.com/moonbit-community/moonpython.git /tmp/moonpython
git -C /tmp/moonpython fetch --depth 1 origin "$PIN"
git -C /tmp/moonpython checkout "$PIN"
ln -sfn /tmp/moonpython batch/corpora/moonpython/rules
test "$(git -C /tmp/moonpython rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/moonpython_gate_decision.json` (`go`).
Smith: `properties/generated/moonpython_smith_decision.json` (`go`).
NOT a security tool → public-first disclosure.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus moonpython --assert-determinism
python -m regexproof.batch --corpus moonpython
```

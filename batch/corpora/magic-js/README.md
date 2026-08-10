# magic-js corpus

Pinned magiclabs/magic-js first-party `packages/@magic-*` ecma surfaces for
Smith triage-trial [#159](https://github.com/lucas-albers-lz4/regexproof/issues/159).

Exclude `.yarn/plugins` and rollup configs.

## Materialize

```bash
PIN=e9fb233763160316989863b4739c4656133d45b0
git clone https://github.com/magiclabs/magic-js.git /tmp/magic-js
git -C /tmp/magic-js fetch --depth 1 origin "$PIN"
git -C /tmp/magic-js checkout "$PIN"
ln -sfn /tmp/magic-js batch/corpora/magic-js/rules
test "$(git -C /tmp/magic-js rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/magic-js_gate_decision.json` (`triage-trial`).

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus magic-js --assert-determinism
python -m regexproof.batch --corpus magic-js
```

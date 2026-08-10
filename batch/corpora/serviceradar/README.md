# serviceradar corpus

Pinned carverauto/serviceradar first-party `js/cli` + elixir web-ng assets
(ecma) for Smith triage-trial
[#183](https://github.com/lucas-albers-lz4/regexproof/issues/183)
under umbrella [#179](https://github.com/lucas-albers-lz4/regexproof/issues/179).

Exclude `third_party/`, tests, and monaco SRQL editor vendor.

## Materialize

```bash
PIN=37859392af3e58b2e1825bbe75091090914277c4
git clone https://github.com/carverauto/serviceradar.git /tmp/serviceradar
git -C /tmp/serviceradar fetch --depth 1 origin "$PIN"
git -C /tmp/serviceradar checkout "$PIN"
ln -sfn /tmp/serviceradar batch/corpora/serviceradar/rules
test "$(git -C /tmp/serviceradar rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/serviceradar_gate_decision.json` (`triage-trial`).

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus serviceradar --assert-determinism
python -m regexproof.batch --corpus serviceradar
```

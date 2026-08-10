# lonkero corpus

Pinned bountyyfi/lonkero browser-assist extension scanners (ecma) for Smith
triage-trial [#180](https://github.com/lucas-albers-lz4/regexproof/issues/180)
under umbrella [#179](https://github.com/lucas-albers-lz4/regexproof/issues/179).

## Materialize

```bash
PIN=bc1e4859b321e0a6fb125f804b9d7e35975790cc
git clone https://github.com/bountyyfi/lonkero.git /tmp/lonkero
git -C /tmp/lonkero fetch --depth 1 origin "$PIN"
git -C /tmp/lonkero checkout "$PIN"
ln -sfn /tmp/lonkero batch/corpora/lonkero/rules
test "$(git -C /tmp/lonkero rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/lonkero_gate_decision.json` (`triage-trial`).
Security-tool: `private_first` via `SECURITY_TOOL_CORPORA`.

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus lonkero --assert-determinism
python -m regexproof.batch --corpus lonkero
```

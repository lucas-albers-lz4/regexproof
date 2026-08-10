# tracecat corpus

Pinned TracecatHQ/tracecat product `py_re` surfaces for Smith triage-trial
[#157](https://github.com/lucas-albers-lz4/regexproof/issues/157).

Probe reported 425 sites (ecma+py_re). This admit measures **product Python**
only (incl. `tracecat/sanitization.py`); frontend ecma and benchmark packages
are excluded.

## Materialize

```bash
PIN=c84d52528a489821f355fc63976fbc7783ae0ad5
git clone https://github.com/TracecatHQ/tracecat.git /tmp/tracecat
git -C /tmp/tracecat fetch --depth 1 origin "$PIN"
git -C /tmp/tracecat checkout "$PIN"
ln -sfn /tmp/tracecat batch/corpora/tracecat/rules
test "$(git -C /tmp/tracecat rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/tracecat_gate_decision.json` (`triage-trial`).

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus tracecat --assert-determinism
python -m regexproof.batch --corpus tracecat
```

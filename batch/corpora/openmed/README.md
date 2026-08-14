# openmed corpus

Pinned maziyarpanahi/openmed first-party clinical PII/PHI and
re-identification regexes (Python `re`) for Smith after the cap=80
flush GO (`openmed_gate_decision.json`). Tests and brand scripts
excluded.

## Materialize

```bash
PIN=353c81a6ef996b4b52eff555560efd2ac86922bf
git clone --filter=blob:none https://github.com/maziyarpanahi/openmed.git /tmp/openmed
git -C /tmp/openmed fetch --depth 1 origin "$PIN"
git -C /tmp/openmed checkout "$PIN"
ln -sfn /tmp/openmed batch/corpora/openmed/rules
test "$(git -C /tmp/openmed rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/openmed_gate_decision.json` (`go`).
Not a scanner pack — `security_tool=False` (no `private_first`).

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus openmed --assert-determinism
python -m regexproof.batch --corpus openmed
```

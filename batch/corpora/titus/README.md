# titus corpus

Pinned praetorian-inc/titus secret-scanner validators (Go re2). Smith
**NO-GO** this wave: 15/57 = 0.2632 encodable (below 0.30). Manifest kept
for the allowlist; **not** in `WAVE_CORPORA`. See
`properties/generated/titus_smith_decision.json`.

## Materialize

```bash
PIN=57b733f5ed04a59b03514f229c3052ace7473d50
git clone --filter=blob:none https://github.com/praetorian-inc/titus.git /tmp/titus
git -C /tmp/titus fetch --depth 1 origin "$PIN"
git -C /tmp/titus checkout "$PIN"
ln -sfn /tmp/titus batch/corpora/titus/rules
test "$(git -C /tmp/titus rev-parse HEAD)" = "$PIN"
```

Gate: `properties/generated/titus_gate_decision.json` (also `praetorian-inc-titus_gate_decision.json`; `triage-trial`).
Security-tool: `private_first` via `SECURITY_TOOL_CORPORA`.

## Measure

```bash
python scripts/measure-corpus-fraction.py --corpus titus --assert-determinism
```

Do not `python -m regexproof.batch --corpus titus` until a future Smith GO.

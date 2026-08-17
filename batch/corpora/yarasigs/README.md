# yarasigs corpus

Pinned `0day1day/yarasigs` at `5a07dfcde3076615e4d9394ec75ff53e74c19b45`
for Smith after admission `yarasigs_gate_decision.json` (renamed from
`0day1day-yarasigs_gate_decision.json` so the gate stem matches
`corpus=yarasigs`). YARA under `signatures/` (mostly AlienVault packs).

## Materialize

```bash
python scripts/materialize-corpus.py --gate properties/generated/yarasigs_gate_decision.json
# materialize links the clone root; re-point at signatures/
ln -sfn /tmp/0day1day-yarasigs-yarasigs/signatures batch/corpora/yarasigs/rules
test "$(git -C /tmp/0day1day-yarasigs-yarasigs rev-parse HEAD)" = "5a07dfcde3076615e4d9394ec75ff53e74c19b45"
```

Gate: `properties/generated/yarasigs_gate_decision.json` (`go`).
Scanner pack — `security_tool=True` (`private_first`).

## Measure / batch

```bash
python scripts/measure-corpus-fraction.py --corpus yarasigs --assert-determinism
python -m regexproof.batch --corpus yarasigs
python scripts/author-smith-decision.py --gate properties/generated/yarasigs_gate_decision.json \
  --fraction properties/generated/yarasigs_encodable_fraction.json \
  --decision go --reason '<N_ok>/<N> = <frac> on signatures/'
```

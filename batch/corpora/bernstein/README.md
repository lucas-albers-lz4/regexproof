# bernstein corpus

Pinned `sipyourdrink-ltd/bernstein` at `be3b073da9bb44e4c4bb35faed634380d5a9936f` for Smith after admission `properties/generated/sipyourdrink-ltd-bernstein_gate_decision.json`.

Issue: #392. The manifest and Smith artifacts use the corpus key `bernstein` from the gate record.

## Scope and result

The measured Python slice is the exact 302-file manifest allowlist: 1,002 of the 1,144 Python sites from the gate inventory. It excludes 74 probe-marked test/fixture paths (142 Python sites). ECMA (455 sites) and shell (27 sites) are outside this slice.

Measured fraction: `properties/generated/bernstein_encodable_fraction.json`. Decision: **go**. `549/1,002 (54.79%) encode in the pinned Python production-source slice; complete run, zero unclassified parse errors. Security-tool findings remain private-first; the other probe dialects are outside this measured slice.`

The corpus is a security-tool source. Batch findings default to `private_first`; no public filing was performed. No conversion property is claimed by these compiler measurements.

## Materialize

```bash
python scripts/materialize-corpus.py --gate properties/generated/sipyourdrink-ltd-bernstein_gate_decision.json
```

## Measure / batch / record decision

```bash
python scripts/measure-corpus-fraction.py --corpus bernstein --assert-determinism
python -m regexproof.batch --corpus bernstein
python scripts/author-smith-decision.py --gate properties/generated/sipyourdrink-ltd-bernstein_gate_decision.json \
  --fraction properties/generated/bernstein_encodable_fraction.json \
  --decision go --reason '549/1,002 (54.79%) encode in the pinned Python production-source slice; complete run, zero unclassified parse errors. Security-tool findings remain private-first; the other probe dialects are outside this measured slice.'
```

This corpus is not in `WAVE_CORPORA`; add it only after a separate conversion-wave decision.

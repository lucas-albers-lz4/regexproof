# lyrie-ai corpus

Pinned `OTT-Cybersecurity-LLC/lyrie-ai` at `96048f6727c01760850e5ef5e1526c8cb9061db8` for Smith after admission `properties/generated/OTT-Cybersecurity-LLC-lyrie-ai_gate_decision.json`.

Issue: #395. The manifest and Smith artifacts use the corpus key `lyrie-ai` from the gate record.

## Scope and result

The measured ECMA slice is the exact 191-file manifest allowlist: 1,589 of the 1,612 ECMA sites from the gate inventory. Four probe-marked test files (23 sites) are excluded. Python (123), shell (2), and YARA (198) sites are outside this ECMA slice.

Measured fraction: `properties/generated/lyrie-ai_encodable_fraction.json`. Decision: **go**. `913/1,589 (57.46%) encode in the pinned ECMA production-source slice; complete run, zero unclassified parse errors. Security-tool findings remain private-first; the other probe dialects are outside this measured slice.`

The corpus is a security-tool source. Batch findings default to `private_first`; no public filing was performed. No conversion property is claimed by these compiler measurements.

## Materialize

```bash
python scripts/materialize-corpus.py --gate properties/generated/OTT-Cybersecurity-LLC-lyrie-ai_gate_decision.json
```

## Measure / batch / record decision

```bash
python scripts/measure-corpus-fraction.py --corpus lyrie-ai --assert-determinism
python -m regexproof.batch --corpus lyrie-ai
python scripts/author-smith-decision.py --gate properties/generated/OTT-Cybersecurity-LLC-lyrie-ai_gate_decision.json \
  --fraction properties/generated/lyrie-ai_encodable_fraction.json \
  --decision go --reason '913/1,589 (57.46%) encode in the pinned ECMA production-source slice; complete run, zero unclassified parse errors. Security-tool findings remain private-first; the other probe dialects are outside this measured slice.'
```

This corpus is not in `WAVE_CORPORA`; add it only after a separate conversion-wave decision.

# Yara-Rules corpus

Pinned `The-DFIR-Report/Yara-Rules` at `9034e24193b38aad1fbc0912ace3683eb5728a92` for Smith after admission `properties/generated/The-DFIR-Report-Yara-Rules_gate_decision.json`.

Issue: #382. The manifest and Smith artifacts use the corpus key `Yara-Rules` from the gate record.

## Scope and result

The full pinned YARA tree: 52 files and 3,565 rule sites. The gate corpus key is `Yara-Rules`; the issue slug is recorded by the gate filename.

Measured fraction: `properties/generated/Yara-Rules_encodable_fraction.json`. Decision: **no-go**. `681/3565 (19.10%) encode in the current YARA mirror subset, below the 0.30 admission threshold; 2,884 sites require fullword-boundary support. This is compiler coverage only.`

The corpus is a security-tool source. Batch findings default to `private_first`; no public filing was performed. No conversion property is claimed by these compiler measurements.

## Materialize

```bash
python scripts/materialize-corpus.py --gate properties/generated/The-DFIR-Report-Yara-Rules_gate_decision.json
```

## Measure / batch / record decision

```bash
python scripts/measure-corpus-fraction.py --corpus Yara-Rules --assert-determinism
python -m regexproof.batch --corpus Yara-Rules
python scripts/author-smith-decision.py --gate properties/generated/The-DFIR-Report-Yara-Rules_gate_decision.json \
  --fraction properties/generated/Yara-Rules_encodable_fraction.json \
  --decision no-go --reason '681/3565 (19.10%) encode in the current YARA mirror subset, below the 0.30 admission threshold; 2,884 sites require fullword-boundary support. This is compiler coverage only.'
```

This corpus is not in `WAVE_CORPORA`; add it only after a separate conversion-wave decision.

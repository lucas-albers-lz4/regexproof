# BlueBox corpus

Pinned `svdwi/BlueBox` at `ff1563bc6e297247e30bb1509cf9c4f7385ac5af` for Smith after admission `properties/generated/svdwi-BlueBox_gate_decision.json`.

Issue: #416. The manifest and Smith artifacts use the corpus key `BlueBox` from the gate record.

## Scope and result

The measured slice is `App/yarascripts/YaraScan/rules`; other probe dialects are outside the YARA slice. The inventory contains 17,525 regex sites, of which 11,502 (65.63%) encode. This was a complete deterministic run with zero unclassified parse errors. The extractor reported one file over its standard 2,000,000-byte limit: `packers/peid.yar` (2,742,475 bytes). That generated PEiD signature file contains no YARA regex assignments, so it contributes no regex sites. The GO applies to the measured regex inventory.

The corpus is a security tool. All 71 batch findings remain `private_first`; the dry run would not open a public upstream issue. This compiler measurement does not claim a product security property.

## Materialize and reproduce

```bash
python scripts/materialize-corpus.py --gate properties/generated/svdwi-BlueBox_gate_decision.json
python scripts/measure-corpus-fraction.py --corpus BlueBox --assert-determinism
python -m regexproof.batch --corpus BlueBox
python scripts/author-smith-decision.py --gate properties/generated/svdwi-BlueBox_gate_decision.json \
  --fraction properties/generated/BlueBox_encodable_fraction.json \
  --decision go --reason '11,502/17,525 (65.63%) encode in the pinned YARA path; complete deterministic run, zero unclassified parse errors, 71 private-first batch findings. One 2.74 MB PEiD signature file exceeds the standard extractor limit; it contains no YARA regex assignments and contributes no regex sites. No product security property is claimed.'
```

This corpus is not in `WAVE_CORPORA`; a compiler-fraction go decision does not adopt a product property.

## Compiler coverage buckets

| Bucket | Sites |
|---|---:|
| `encodable` | 11,502 |
| `fullword-boundary` | 5,885 |
| `pattern-too-long` | 6 |
| `per-alternative-anchor` | 1 |
| `unsupported-escape` | 1 |
| `wide-non-literal` | 130 |

Total: 11,502/17,525 sites encodable (65.63%).
## Batch triage

The batch records 71 findings, all 71 `private_first`, and 6,023 triage rows. It also has 4 planned inventory questions; these are not solver results. The dry run is non-publishing and would not open an upstream issue.

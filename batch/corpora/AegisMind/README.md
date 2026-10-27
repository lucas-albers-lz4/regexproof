# AegisMind corpus

Pinned `Thinking-builder/AegisMind` at `cbb0b153216a4464c927bb3b84cb609fc8a41867` for Smith after admission `properties/generated/Thinking-builder-AegisMind_gate_decision.json`.

Issue: #403. The manifest and Smith artifacts use the corpus key `AegisMind` from the gate record.

## Scope and result

The measured slice is the pinned `yara_rules/` tree; ECMA probe results are outside this YARA measurement. The inventory contains 38,309 regex sites, of which 23,021 (60.09%) encode. This was a complete deterministic run with zero unclassified parse errors. The extractor reported one file over its standard 2,000,000-byte limit: `yara_rules/peid.yar` (2,742,475 bytes). It is a generated PEiD signature file with no YARA regex assignments, so it contributes no regex sites.

The corpus is a security tool. All 155 batch findings remain `private_first`; the dry run would not open a public upstream issue. The batch run records four planned inventory questions, not solved product properties. No conversion property is claimed by these compiler measurements.

## Materialize and reproduce

```bash
python scripts/materialize-corpus.py --gate properties/generated/Thinking-builder-AegisMind_gate_decision.json
python scripts/measure-corpus-fraction.py --corpus AegisMind --assert-determinism
python -m regexproof.batch --corpus AegisMind
python scripts/author-smith-decision.py --gate properties/generated/Thinking-builder-AegisMind_gate_decision.json \
  --fraction properties/generated/AegisMind_encodable_fraction.json \
  --decision go --reason '23,021/38,309 (60.09%) encode in the pinned yara_rules tree; complete deterministic run, zero unclassified parse errors, 155 private-first batch findings. One 2.74 MB generated PEiD signature file exceeds the extractor limit; it has no YARA regex assignments and contributes no regex sites. No product security property is claimed.'
```

This corpus is not in `WAVE_CORPORA`; a compiler-fraction go decision does not adopt a product property.

## Compiler coverage buckets

| Bucket | Sites |
|---|---:|
| `encodable` | 23,021 |
| `fullword-boundary` | 15,007 |
| `internal-anchor` | 3 |
| `pattern-too-long` | 22 |
| `per-alternative-anchor` | 1 |
| `repeat-count` | 2 |
| `s-flag` | 1 |
| `unsupported-escape` | 1 |
| `unsupported-modifier:FIX,FPS,Microsoft,files,with` | 2 |
| `unsupported-modifier:FPs,prone,to` | 1 |
| `unsupported-modifier:base64` | 30 |
| `unsupported-modifier:more` | 1 |
| `unsupported-modifier:xor` | 10 |
| `wide-non-literal` | 201 |
| `word-boundary` | 6 |

Total: 23,021/38,309 sites encodable (60.09%).
## Batch triage

The batch records 155 findings, all 155 `private_first`, and 15,288 triage rows. It also has 4 planned inventory questions; these are not solver results. The dry run is non-publishing and would not open an upstream issue.

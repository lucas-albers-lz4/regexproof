# SentinelX corpus

Pinned `jaytiwari05/SentinelX` at `9168547df5232067ac68eb9413f7248f89ccf8c1` for Smith after admission `properties/generated/jaytiwari05-SentinelX_gate_decision.json`.

Issue: #406. The manifest and Smith artifacts use the corpus key `SentinelX` from the gate record.

## Scope and result

The measured slice is the pinned YARA tree `rules/`; shell probe results are outside this measurement. The inventory contains 21,287 regex sites, of which 13,117 (61.62%) encode. This was a complete deterministic run with zero unclassified parse errors. The extractor reported one file over its standard 2,000,000-byte limit: `rules/yara-rules-repo/packers/peid.yar` (2,742,475 bytes). It is a generated PEiD signature file with no YARA regex assignments, so it contributes no regex sites.

The corpus is a security tool. All 86 batch findings remain `private_first`; the dry run would not open a public upstream issue. This compiler measurement does not claim a product security property.

## Materialize and reproduce

```bash
python scripts/materialize-corpus.py --gate properties/generated/jaytiwari05-SentinelX_gate_decision.json
python scripts/measure-corpus-fraction.py --corpus SentinelX --assert-determinism
python -m regexproof.batch --corpus SentinelX
python scripts/author-smith-decision.py --gate properties/generated/jaytiwari05-SentinelX_gate_decision.json \
  --fraction properties/generated/SentinelX_encodable_fraction.json \
  --decision go --reason '13,117/21,287 (61.62%) encode in the pinned YARA tree; complete deterministic run, zero unclassified parse errors, 86 private-first batch findings. One 2.74 MB generated PEiD signature file exceeds the extractor limit; it has no YARA regex assignments and contributes no regex sites. No product security property is claimed.'
```

This corpus is not in `WAVE_CORPORA`; a compiler-fraction go decision does not adopt a product property.

## Compiler coverage buckets

| Bucket | Sites |
|---|---:|
| `encodable` | 13,117 |
| `fullword-boundary` | 7,991 |
| `pattern-too-long` | 40 |
| `per-alternative-anchor` | 1 |
| `unsupported-escape` | 1 |
| `wide-non-literal` | 137 |

Total: 13,117/21,287 sites encodable (61.62%).
## Batch triage

The batch records 86 findings, all 86 `private_first`, and 8,170 triage rows. It also has 4 planned inventory questions; these are not solver results. The dry run is non-publishing and would not open an upstream issue.

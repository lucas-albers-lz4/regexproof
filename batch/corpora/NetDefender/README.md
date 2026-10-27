# NetDefender corpus

Pinned `nipunsw1999/NetDefender` at `88a81e76b19354f4e09fe47f153335da279458d4` for Smith after admission `properties/generated/nipunsw1999-NetDefender_gate_decision.json`.

Issue: #420. The manifest and Smith artifacts use the corpus key `NetDefender` from the gate record.

## Scope and result

The measured slice is the pinned YARA tree `rules/`. The repository's one Python probe site is outside this YARA measurement. The inventory contains 24,310 YARA regex sites, of which 14,136 (58.15%) encode. This was a complete deterministic run with zero unclassified parse errors.

The corpus is a security tool. All 98 batch findings remain `private_first`; the dry run would not open a public upstream issue. This compiler measurement does not claim a product security property.

## Materialize and reproduce

```bash
python scripts/materialize-corpus.py --gate properties/generated/nipunsw1999-NetDefender_gate_decision.json
python scripts/measure-corpus-fraction.py --corpus NetDefender --assert-determinism
python -m regexproof.batch --corpus NetDefender
python scripts/author-smith-decision.py --gate properties/generated/nipunsw1999-NetDefender_gate_decision.json \
  --fraction properties/generated/NetDefender_encodable_fraction.json \
  --decision go --reason '14,136/24,310 (58.15%) encode in the pinned YARA tree; complete deterministic run, zero unclassified parse errors, 98 private-first batch findings. The single Python probe site is outside the YARA scope. No product security property is claimed.'
```

This corpus is not in `WAVE_CORPORA`; a compiler-fraction go decision does not adopt a product property.

## Compiler coverage buckets

| Bucket | Sites |
|---|---:|
| `encodable` | 14,136 |
| `fullword-boundary` | 9,950 |
| `pattern-too-long` | 4 |
| `per-alternative-anchor` | 2 |
| `unsupported-escape` | 2 |
| `wide-non-literal` | 216 |

Total: 14,136/24,310 sites encodable (58.15%).
## Batch triage

The batch records 98 findings, all 98 `private_first`, and 10,174 triage rows. It also has 4 planned inventory questions; these are not solver results. The dry run is non-publishing and would not open an upstream issue.

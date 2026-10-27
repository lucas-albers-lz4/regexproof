# freki corpus

Pinned `cristianzsh/freki` at `08d593d447d27dc0794d0db68256fb1d6aecb607` for Smith after admission `properties/generated/cristianzsh-freki_gate_decision.json`.

Issue: #404. The manifest and Smith artifacts use the corpus key `freki` from the gate record.

## Scope and result

The measured slice is the YARA tree `freki/app/core/yara_rules`; the repository's Python and shell probe results are outside this measurement. The pinned YARA inventory contains 11,190 regex sites, of which 6,187 (55.29%) encode. This was a complete deterministic run with zero unclassified parse errors. One pattern uses unsupported PCRE `\\V`, now classified as `unsupported-escape`.

The corpus is a security tool. All findings remain `private_first`; the batch dry run would not open a public upstream issue. This compiler measurement does not claim a product security property.

## Materialize and reproduce

```bash
python scripts/materialize-corpus.py --gate properties/generated/cristianzsh-freki_gate_decision.json
python scripts/measure-corpus-fraction.py --corpus freki --assert-determinism
python -m regexproof.batch --corpus freki
python scripts/author-smith-decision.py --gate properties/generated/cristianzsh-freki_gate_decision.json \
  --fraction properties/generated/freki_encodable_fraction.json \
  --decision go --reason '6,187/11,190 (55.29%) encode in the pinned YARA tree; complete deterministic run, zero unclassified parse errors. Security-tool findings remain private-first.'
```

This corpus is not in `WAVE_CORPORA`; a compiler-fraction go decision does not adopt a product property.

## Compiler coverage buckets

| Bucket | Sites |
|---|---:|
| `encodable` | 6,187 |
| `fullword-boundary` | 4,892 |
| `pattern-too-long` | 2 |
| `per-alternative-anchor` | 1 |
| `unsupported-escape` | 1 |
| `wide-non-literal` | 107 |

Total: 6,187/11,190 sites encodable (55.29%).
## Batch triage

The batch records 51 findings, all 51 `private_first`, and 5,003 triage rows. It also has 4 planned inventory questions; these are not solver results. The dry run is non-publishing and would not open an upstream issue.

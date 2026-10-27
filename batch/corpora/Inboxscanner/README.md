# Inboxscanner corpus

Pinned `ag-michael/Inboxscanner` at `cafc3dcc92557192204c0479450731a3e7528388` for Smith after admission `properties/generated/ag-michael-Inboxscanner_gate_decision.json`.

Issue: #419. The manifest and Smith artifacts use the corpus key `Inboxscanner` from the gate record.

## Scope and result

The measured scope is the exact 1,860-file YARA allowlist derived from the pinned gate's `regex_sites_per_file` map, filtered by case-insensitive `.yar`/`.yara` suffix. It reproduces the gate's YARA count exactly: 51,250 sites. The 6 PCRE, 4 shell, and 12 Python sites in the gate are outside this YARA slice. The allowlist includes the uppercase `.YAR` file `rules/Open-Source-YARA-rules-master/Fireeye/MACROCHECK.YAR`.

The allowlist follows the admission walk's exclusions. In particular, it omits `rules/signature-base-master/vendor/yara/airbnb_binaryalert.yar`, a vendor file absent from the gate inventory that the broad glob extractor would otherwise count as 373 extra sites. The final per-file batch inventory matches the gate's YARA map exactly (1,860 files, 51,250 sites).

The complete first measurement encoded 30,553/51,250 sites (59.62%), with zero unclassified parse errors and no budget breach. The first pass with determinism disabled took 210.223 seconds. The subsequent `--assert-determinism` run passed in 66.763 seconds. The 17 MB inventory and both passes fit the dedicated budget: 60,000 patterns, 1,800 seconds, 6,144 MB memory, and 2,000 MB disk.

The corpus is a security tool. All 189 batch findings remain `private_first`; the dry run would not open a public upstream issue. The batch records four planned inventory questions, not solved product properties. No conversion property is claimed by this compiler measurement.

## Materialize and reproduce

```bash
python scripts/materialize-corpus.py --gate properties/generated/ag-michael-Inboxscanner_gate_decision.json
python scripts/measure-corpus-fraction.py --corpus Inboxscanner --assert-determinism
python -m regexproof.batch --corpus Inboxscanner
python scripts/author-smith-decision.py --gate properties/generated/ag-michael-Inboxscanner_gate_decision.json \
  --fraction properties/generated/Inboxscanner_encodable_fraction.json \
  --decision go --reason '30,553/51,250 (59.62%) encode in the exact 1,860-file YARA allowlist derived from the pinned gate inventory; complete deterministic run, zero unclassified parse errors. The initial no-determinism pass took 210.223s; the deterministic pass took 66.763s. Batch produced 189 private-first findings. No product security property is claimed.'
```

This corpus is not in `WAVE_CORPORA`; a compiler-fraction go decision does not adopt a product property.

## Compiler coverage buckets

| Bucket | Sites |
|---|---:|
| `encodable` | 30,553 |
| `fullword-boundary` | 20,525 |
| `internal-anchor` | 3 |
| `pattern-too-long` | 21 |
| `unsupported-escape` | 1 |
| `unsupported-modifier:a,and,be,in,mixed,quantifiers,regular,ungreedy` | 1 |
| `unsupported-modifier:more` | 1 |
| `wide-non-literal` | 137 |
| `word-boundary` | 8 |

Total: 30,553/51,250 sites encodable (59.62%).


## Batch triage


The batch records 189 findings, all 189 `private_first`, and 20,697 triage rows. It also has 4 planned inventory questions; these are not solver results. The dry run is non-publishing and would not open an upstream issue.

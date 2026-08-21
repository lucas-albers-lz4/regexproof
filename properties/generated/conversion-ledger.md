# Conversion ledger

Product funnel: sites → properties asked → SAT → ground-truthed → disclosed → accepted upstream.

Heap's-law / singleton novelty saturates **compiler coverage**. This artifact saturates **conversion**. TIMEOUT / `unknown` is not a pass. `docs/verified-findings.jsonl` VF-* rows are toolkit traps, not this numerator.

## Funnel

| stage | count |
|---|---|
| sites extracted (batch summaries) | 130,257 |
| sites encodable | 81,454 |
| scanner NDJSON rows | 8,716 |
| planned inventory stubs | 314 |
| classification rows (usage/intent/triage kinds) | 7,114 |
| mutation guards (hygiene) | 644 |
| properties asked (non-planned product kinds) | 21 |
| properties asked distinct `(site, question_id)` | 21 |
| properties UNSAT (holds in declared domain) | 14 |
| properties SAT | 6 |
| properties SAT distinct `(site, question_id)` | 6 |
| SAT unique sites | 4 |
| SAT ground-truthed (`reproduced` / `PASS`) | 6 |
| rule_diff report SAT (dedicated pilots) | 10 |
| rule_diff report SAT + ground-truth | 10 |
| disclosed `private_first` (scanner product+classification, skip planned) | 1,128 |
| disclosed `public_ok` | 0 |
| dry-run `private_first` (includes planned stubs) | 1,264 |
| dry-run would open public upstream | 0 |
| accepted upstream (curated `fixed_upstream`) | 1 |
| existence proofs (`fixed_upstream` + `private_first`) | 1 |
| filed false positives | 7 |
| third-party public accepted | 0 |

## Rates

| rate | value |
|---|---|
| encodable / extracted | 0.6253 |
| properties asked / encodable | 0.0003 |
| SAT / properties asked | 0.2857 |
| ground-truthed / SAT | 1.0000 |
| pipeline accepted (incl. own-code) / SAT GT | 0.1667 |
| pipeline accepted / extracted | 8.00e-06 |
| encodable / extracted excluding YARA inventories | 0.6105 |
| YARA share of inventory unencodable | 0.6247 |
| `fullword-boundary` share of inventory unencodable | 0.6078 |

## Security-tool split (scanner product kinds)

Asked in tools: 3. Asked elsewhere: 18. SAT in tools: 2. SAT elsewhere: 4.

## Upstream (curated)

Rows: 11. Language-membership: 10. fixed_upstream: 1. filed_plan: 1. false_positive: 7. out_of_scope_redos: 1. private_first: 0. wont_file: 1.

Source: [`docs/conversion-upstream.jsonl`](../../docs/conversion-upstream.jsonl).

## Corpora with properties asked

| corpus | security tool | asked | unsat | sat | sat GT | unique SAT sites |
|---|---|---|---|---|---|---|
| openwrt_packages | false | 14 | 11 | 3 | 3 | 3 |
| openwrt_luci | false | 4 | 3 | 1 | 1 | 1 |
| coreruleset | true | 3 | 0 | 2 | 2 | 0 |

## Denominator notes

`crs-inventory.ndjson` is the @rx-only CRS measure (346 rows) from `regexproof.batch.crs_measure`; it is **not** the batch corpus. `coreruleset-inventory.ndjson` + `coreruleset_batch_summary.json` are the batch extractor (338 extracted). Do not glob `crs-inventory` into the conversion ledger sample.

Synthesis considers at most `synth_max_sites` (default 200, sort by `regex_id`) per corpus. Corpora with properties asked are listed in the table above; their batch summaries record `synth_max_sites`.

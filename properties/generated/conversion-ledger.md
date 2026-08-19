# Conversion ledger

Product funnel: sites → properties asked → SAT → ground-truthed → disclosed → accepted upstream.

Heap's-law / singleton novelty saturates **compiler coverage**. This artifact saturates **conversion**. TIMEOUT / `unknown` is not a pass. `docs/verified-findings.jsonl` VF-* rows are toolkit traps, not this numerator.

## Funnel

| stage | count |
|---|---|
| sites extracted (batch summaries) | 125,715 |
| sites encodable | 78,816 |
| scanner NDJSON rows | 7,260 |
| planned inventory stubs | 298 |
| classification rows (usage/intent/triage kinds) | 5,674 |
| mutation guards (hygiene) | 644 |
| properties asked (non-planned product kinds) | 17 |
| properties asked distinct `(site, question_id)` | 17 |
| properties UNSAT (holds in declared domain) | 11 |
| properties SAT | 5 |
| properties SAT distinct `(site, question_id)` | 5 |
| SAT unique sites | 3 |
| SAT ground-truthed (`reproduced` / `PASS`) | 5 |
| rule_diff report SAT (dedicated pilots) | 10 |
| rule_diff report SAT + ground-truth | 10 |
| disclosed `private_first` (scanner product+classification, skip planned) | 686 |
| disclosed `public_ok` | 0 |
| dry-run `private_first` (includes planned stubs) | 814 |
| dry-run would open public upstream | 0 |
| accepted upstream (curated `fixed_upstream`) | 1 |
| existence proofs (`fixed_upstream` + `private_first`) | 1 |
| filed false positives | 7 |
| third-party public accepted | 0 |

## Rates

| rate | value |
|---|---|
| encodable / extracted | 0.6269 |
| properties asked / encodable | 0.0002 |
| SAT / properties asked | 0.2941 |
| ground-truthed / SAT | 1.0000 |
| pipeline accepted (incl. own-code) / SAT GT | 0.2000 |
| pipeline accepted / extracted | 8.00e-06 |
| encodable / extracted excluding YARA inventories | 0.6128 |
| YARA share of inventory unencodable | 0.6439 |
| `fullword-boundary` share of inventory unencodable | 0.6264 |

## Security-tool split (scanner product kinds)

Asked in tools: 3. Asked elsewhere: 14. SAT in tools: 2. SAT elsewhere: 3.

## Upstream (curated)

Rows: 11. Language-membership: 10. fixed_upstream: 1. filed_plan: 1. false_positive: 7. out_of_scope_redos: 1. private_first: 0. wont_file: 1.

Source: [`docs/conversion-upstream.jsonl`](../../docs/conversion-upstream.jsonl).

## Corpora with properties asked

| corpus | security tool | asked | unsat | sat | sat GT | unique SAT sites |
|---|---|---|---|---|---|---|
| openwrt_packages | false | 14 | 11 | 3 | 3 | 3 |
| coreruleset | true | 3 | 0 | 2 | 2 | 0 |

## Denominator notes

`crs-inventory.ndjson` is the @rx-only CRS measure (346 rows) from `regexproof.batch.crs_measure`; it is **not** the batch corpus. `coreruleset-inventory.ndjson` + `coreruleset_batch_summary.json` are the batch extractor (338 extracted). Do not glob `crs-inventory` into the conversion ledger sample.

Synthesis considers at most `synth_max_sites` (default 200, sort by `regex_id`) per corpus. Corpora with properties asked are listed in the table above; their batch summaries record `synth_max_sites`.

# Conversion ledger

Product funnel: sites → properties asked → SAT → ground-truthed → disclosed → accepted upstream.

Heap's-law / singleton novelty saturates **compiler coverage**. This artifact saturates **conversion**. TIMEOUT / `unknown` is not a pass. `docs/verified-findings.jsonl` VF-* rows are toolkit traps, not this numerator.

## Funnel

| stage | count |
|---|---|
| sites extracted (batch summaries) | 136,260 |
| sites encodable | 84,266 |
| scanner NDJSON rows | 9,741 |
| planned inventory stubs | 326 |
| classification rows (usage/intent/triage kinds) | 8,127 |
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
| encodable / extracted | 0.6184 |
| properties asked / encodable | 0.0002 |
| SAT / properties asked | 0.2857 |
| ground-truthed / SAT | 1.0000 |
| pipeline accepted (incl. own-code) / SAT GT | 0.1667 |
| pipeline accepted / extracted | 7.00e-06 |
| encodable / extracted excluding YARA inventories | 0.5979 |
| YARA share of inventory unencodable | 0.5951 |
| `fullword-boundary` share of inventory unencodable | 0.5789 |

## Security-tool split (scanner product kinds)

Asked in tools: 3. Asked elsewhere: 18. SAT in tools: 2. SAT elsewhere: 4.

## Upstream (curated)

Rows: 14. Language-membership: 13. fixed_upstream: 1. filed_plan: 1. false_positive: 7. out_of_scope_redos: 1. private_first: 0. wont_file: 4.

Source: [`docs/conversion-upstream.jsonl`](../../docs/conversion-upstream.jsonl).

## Corpora with properties asked

| corpus | security tool | asked | unsat | sat | sat GT | unique SAT sites |
|---|---|---|---|---|---|---|
| openwrt_packages | false | 14 | 11 | 3 | 3 | 3 |
| openwrt_luci | false | 4 | 3 | 1 | 1 | 1 |
| coreruleset | true | 3 | 0 | 2 | 2 | 0 |

## Per-wave conversion hops (#554)

asked → SAT → GT → filed → accepted per `(wave_id, idiom_bucket)`.
**GT→filed is the currently empty hop** — highlighted. Join: curated
`(site, question_id)`; filed = status filed/private_first/fixed_upstream
(or filed_at set); accepted = fixed_upstream.

| wave | idiom bucket | asked | SAT | GT | filed | accepted | GT→filed |
|---|---|---|---|---|---|---|---|
| openwrt_luci_w1 | form-validator-alphabets | 4 | 1 | 1 | **0** | 0 | **0.0000** |
| openwrt_packages_w1 | validator-charsets-and-captures | 5 | 1 | 1 | **0** | 0 | **0.0000** |
| openwrt_packages_w2 | image-and-ddns-json | 5 | 1 | 1 | **0** | 0 | **0.0000** |
| openwrt_packages_w3 | ddns-query-and-escape-image | 4 | 1 | 1 | **0** | 0 | **0.0000** |

## Starvation & queue pressure (#554)

- demand_open (open gated:go clusters lacking a closed wave): **64**
- admission_per_week (GO gate-decision artifacts, last 7-day window ending 2026-08-20): **2**
- backlog_weeks = demand_open / admission_per_week = **32.0**
- mine_queue_pressure = queue_len / queue_cap = 100 / 100 = **1.0000**
- alert (backlog_weeks increased >= 2 consecutive windows): **no** (consecutive increases: 0)

Admission is bounded by the ~10/day mine cap regardless of #550 batch
flush, so backlog_weeks reflects mine-cap pressure by design — read it
alongside mine_queue_pressure, not as a batch-health metric.

## Contract-queue health (#551 Phase C states)

artifacts present: False · emitted: 0 · claimed: 0 · contracted: 0 · skipped: 0 · median age: n/a days. Phase C queue artifacts not yet shipped

## Property-shape mix (#554)

Share of asked properties per shape, per wave (conversion rows).

| wave | idiom bucket | asked | shape mix (%) |
|---|---|---|---|
| openwrt_luci_w1 | form-validator-alphabets | 4 | shape 1: 0.7500, shape 3: 0.2500 |
| openwrt_packages_w1 | validator-charsets-and-captures | 5 | shape 1: 0.6000, shape 3: 0.4000 |
| openwrt_packages_w2 | image-and-ddns-json | 5 | shape 1: 0.4000, shape 3: 0.4000, shape 4: 0.2000 |
| openwrt_packages_w3 | ddns-query-and-escape-image | 4 | shape 1: 0.2500, shape 3: 0.5000, shape 4: 0.2500 |

## Denominator notes

`crs-inventory.ndjson` is the @rx-only CRS measure (346 rows) from `regexproof.batch.crs_measure`; it is **not** the batch corpus. `coreruleset-inventory.ndjson` + `coreruleset_batch_summary.json` are the batch extractor (338 extracted). Do not glob `crs-inventory` into the conversion ledger sample.

Synthesis considers at most `synth_max_sites` (default 0 — untargeted
synthesis is compute control; opt-in corpora set an explicit value, sort
by `regex_id`) per corpus. Corpora with properties asked are listed
in the table above; their batch summaries record `synth_max_sites`.

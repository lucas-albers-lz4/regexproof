# Conversion ledger

Product funnel: sites → properties asked → SAT → ground-truthed → disclosed → accepted upstream.

Heap's-law / singleton novelty saturates **compiler coverage**. This artifact saturates **conversion**. TIMEOUT / `unknown` is not a pass. `docs/verified-findings.jsonl` VF-* rows are toolkit traps, not this numerator.

## Funnel

| stage | count |
|---|---|
| sites extracted (batch summaries) | 149,212 |
| sites encodable | 96,030 |
| scanner NDJSON rows | 14,678 |
| planned inventory stubs | 338 |
| classification rows (usage/intent/triage kinds) | 13,052 |
| mutation guards (hygiene) | 644 |
| properties asked (non-planned product kinds) | 49 |
| properties asked distinct `(site, question_id)` | 49 |
| properties UNSAT (holds in declared domain) | 37 |
| properties SAT | 11 |
| properties SAT distinct `(site, question_id)` | 11 |
| SAT unique sites | 9 |
| SAT ground-truthed (`reproduced` / `PASS`) | 11 |
| rule_diff report SAT (dedicated pilots) | 10 |
| rule_diff report SAT + ground-truth | 10 |
| disclosed `private_first` (scanner product+classification, skip planned) | 1,147 |
| disclosed `public_ok` | 0 |
| dry-run `private_first` (includes planned stubs) | 1,287 |
| dry-run would open public upstream | 0 |
| accepted upstream (curated `fixed_upstream`) | 1 |
| existence proofs (`fixed_upstream` + `private_first`) | 7 |
| filed false positives | 9 |
| third-party public accepted | 0 |

## Product conversion provenance

Counts cover only product-reportable rows in `*_conversion.ndjson`; they are a separate attribution series alongside the overall scanner funnel.

| adopted provenance | conversion rows |
|---|---|
| human | 38 |
| autonomous (`agent_derived`) | 8 |
| machine pair (`version_diff` / `cross_engine`) | 0 |

## Rates

| rate | value |
|---|---|
| encodable / extracted | 0.6436 |
| properties asked / encodable | 0.0005 |
| SAT / properties asked | 0.2245 |
| ground-truthed / SAT | 1.0000 |
| pipeline accepted (incl. own-code) / SAT GT | 0.0909 |
| pipeline accepted / extracted | 7.00e-06 |
| encodable / extracted excluding YARA inventories | 0.6477 |
| YARA share of inventory unencodable | 0.5848 |
| `fullword-boundary` share of inventory unencodable | 0.5689 |

## Security-tool split (scanner product kinds)

Asked in tools: 12. Asked elsewhere: 37. SAT in tools: 5. SAT elsewhere: 6.

## Upstream (curated)

Rows: 22. Language-membership: 21. fixed_upstream: 1. filed_plan: 1. false_positive: 9. out_of_scope_redos: 1. private_first: 6. wont_file: 4.

Source: [`docs/conversion-upstream.jsonl`](../../docs/conversion-upstream.jsonl).

## Corpora with properties asked

| corpus | security tool | asked | unsat | sat | sat GT | unique SAT sites |
|---|---|---|---|---|---|---|
| openwrt_packages | false | 14 | 11 | 3 | 3 | 3 |
| aidevops | false | 10 | 8 | 2 | 2 | 2 |
| forge-cli | true | 6 | 6 | 0 | 0 | 0 |
| openwrt_luci | false | 4 | 3 | 1 | 1 | 1 |
| Doberman-Core | true | 3 | 0 | 3 | 3 | 3 |
| claude-code-plugins | false | 3 | 3 | 0 | 0 | 0 |
| coreruleset | true | 3 | 0 | 2 | 2 | 0 |
| mycelium | false | 3 | 3 | 0 | 0 | 0 |
| dogfood_shell | false | 2 | 2 | 0 | 0 | 0 |
| real-router | false | 1 | 1 | 0 | 0 | 0 |

## Per-wave conversion hops (#554)

asked → SAT → GT → filed → accepted per `(wave_id, idiom_bucket)`.
**GT→filed is the currently empty hop** — highlighted. Join: curated
`(site, question_id)`; filed = status filed/private_first/fixed_upstream
(or filed_at set); accepted = fixed_upstream.

| wave | idiom bucket | asked | SAT | GT | filed | accepted | GT→filed |
|---|---|---|---|---|---|---|---|
| aidevops-predispatch-20r2-20261016-r1 | pre-dispatch-github-text | 1 | 1 | 1 | **1** | 0 | **1.0000** |
| aidevops-webhook-action-protocol-20r2-20261016-r1 | webhook-action-protocol-validation | 3 | 0 | 0 | **0** | 0 | **n/a** |
| aidevops_predispatch_threshold_residual_20r2 | pre-dispatch-github-text | 1 | 1 | 1 | **1** | 0 | **1.0000** |
| aidevops_w1 | shell-hook-guards | 5 | 0 | 0 | **0** | 0 | **n/a** |
| claude-code-plugins_w1 | plugin-hook-guards | 3 | 0 | 0 | **0** | 0 | **n/a** |
| doberman_secret_path_20r2_r1 | windows-secret-store-path | 1 | 1 | 1 | **1** | 0 | **1.0000** |
| doberman_w1 | command-execution | 2 | 2 | 2 | **0** | 0 | **0.0000** |
| dogfood_shell_w1 | normalize-fixpoint | 2 | 0 | 0 | **0** | 0 | **n/a** |
| forge-cli_helper_image | secret-redaction | 1 | 0 | 0 | **0** | 0 | **n/a** |
| forge-cli_w1 | secret-redaction | 5 | 0 | 0 | **0** | 0 | **n/a** |
| mycelium_w1 | control-failclosed | 3 | 0 | 0 | **0** | 0 | **n/a** |
| openwrt_luci_w1 | form-validator-alphabets | 4 | 1 | 1 | **0** | 0 | **0.0000** |
| openwrt_packages_w1 | validator-charsets-and-captures | 5 | 1 | 1 | **0** | 0 | **0.0000** |
| openwrt_packages_w2 | image-and-ddns-json | 5 | 1 | 1 | **0** | 0 | **0.0000** |
| openwrt_packages_w3 | ddns-query-and-escape-image | 4 | 1 | 1 | **0** | 0 | **0.0000** |
| rr-nav-controls-p6-20261016 | navigation-param-control-calibration | 1 | 0 | 0 | **0** | 0 | **n/a** |

## Starvation & queue pressure (#554)

- demand_open (open gated:go clusters lacking a closed wave): **61**
- admission_per_week (GO gate-decision artifacts, last 7-day window ending 2026-08-26): **2**
- backlog_weeks = demand_open / admission_per_week = **30.5**
- mine_queue_pressure = queue_len / queue_cap = 100 / 100 = **1.0000**
- alert (backlog_weeks increased >= 2 consecutive windows): **no** (consecutive increases: 0)

Admission is bounded by the ~10/day mine cap regardless of #550 batch
flush, so backlog_weeks reflects mine-cap pressure by design — read it
alongside mine_queue_pressure, not as a batch-health metric.

## Contract-queue health (#551 Phase C states)

artifacts present: True · emitted: 0 · claimed: 0 · contracted: 1 · skipped: 0 · median age: 0.0 days.

## Property-shape mix (#554)

Share of asked properties per shape, per wave (conversion rows).

| wave | idiom bucket | asked | shape mix (%) |
|---|---|---|---|
| aidevops-predispatch-20r2-20261016-r1 | pre-dispatch-github-text | 1 | shape 3: 1.0000 |
| aidevops-webhook-action-protocol-20r2-20261016-r1 | webhook-action-protocol-validation | 3 | n/a |
| aidevops_predispatch_threshold_residual_20r2 | pre-dispatch-github-text | 1 | shape 3: 1.0000 |
| aidevops_w1 | shell-hook-guards | 5 | shape 1: 0.6000, shape 3: 0.4000 |
| claude-code-plugins_w1 | plugin-hook-guards | 3 | shape 1: 1.0000 |
| doberman_secret_path_20r2_r1 | windows-secret-store-path | 1 | n/a |
| doberman_w1 | command-execution | 2 | shape 2: 1.0000 |
| dogfood_shell_w1 | normalize-fixpoint | 2 | shape 3: 1.0000 |
| forge-cli_helper_image | secret-redaction | 1 | shape 4: 1.0000 |
| forge-cli_w1 | secret-redaction | 5 | shape 1: 0.6000, shape 2: 0.4000 |
| mycelium_w1 | control-failclosed | 3 | shape 1: 1.0000 |
| openwrt_luci_w1 | form-validator-alphabets | 4 | shape 1: 0.7500, shape 3: 0.2500 |
| openwrt_packages_w1 | validator-charsets-and-captures | 5 | shape 1: 0.6000, shape 3: 0.4000 |
| openwrt_packages_w2 | image-and-ddns-json | 5 | shape 1: 0.4000, shape 3: 0.4000, shape 4: 0.2000 |
| openwrt_packages_w3 | ddns-query-and-escape-image | 4 | shape 1: 0.2500, shape 3: 0.5000, shape 4: 0.2500 |
| rr-nav-controls-p6-20261016 | navigation-param-control-calibration | 1 | shape 1: 1.0000 |

## Denominator notes

`crs-inventory.ndjson` is the @rx-only CRS measure (346 rows) from `regexproof.batch.crs_measure`; it is **not** the batch corpus. `coreruleset-inventory.ndjson` + `coreruleset_batch_summary.json` are the batch extractor (338 extracted). Do not glob `crs-inventory` into the conversion ledger sample.

Synthesis considers at most `synth_max_sites` (default 0 — untargeted
synthesis is compute control; opt-in corpora set an explicit value, sort
by `regex_id`) per corpus. Corpora with properties asked are listed
in the table above; their batch summaries record `synth_max_sites`.

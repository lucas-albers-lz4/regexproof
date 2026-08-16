# Conversion ledger

Product funnel: sites → properties asked → SAT → ground-truthed → disclosed → accepted upstream.

Heap's-law / singleton novelty saturates **compiler coverage**. This artifact saturates **conversion**. TIMEOUT / `unknown` is not a pass. `docs/verified-findings.jsonl` VF-* rows are toolkit traps, not this numerator.

## Funnel

| stage | count |
|---|---|
| sites extracted (batch summaries) | 123,643 |
| sites encodable | 76,955 |
| scanner NDJSON rows | 7,117 |
| planned inventory stubs | 290 |
| classification rows (usage/intent/triage kinds) | 5,539 |
| mutation guards (hygiene) | 644 |
| properties asked (non-planned product kinds) | 644 |
| properties UNSAT (holds in declared domain) | 616 |
| properties SAT | 28 |
| SAT unique sites | 7 |
| SAT ground-truthed (`reproduced` / `PASS`) | 28 |
| rule_diff report SAT (dedicated pilots) | 17 |
| rule_diff report SAT + ground-truth | 17 |
| disclosed `private_first` (scanner product+classification, skip planned) | 686 |
| disclosed `public_ok` | 0 |
| dry-run `private_first` (includes planned stubs) | 810 |
| dry-run would open public upstream | 0 |
| accepted upstream (curated `fixed_upstream`) | 1 |
| existence proofs (`fixed_upstream` + `private_first`) | 2 |
| filed false positives | 1 |
| third-party public accepted | 0 |

## Rates

| rate | value |
|---|---|
| encodable / extracted | 0.6224 |
| properties asked / encodable | 0.0084 |
| SAT / properties asked | 0.0435 |
| ground-truthed / SAT | 1.0000 |
| accepted upstream / SAT ground-truthed | 0.0357 |
| accepted upstream / extracted | 8.00e-06 |

## Security-tool split (scanner product kinds)

Asked in tools: 0. Asked elsewhere: 644. SAT in tools: 0. SAT elsewhere: 28.

## Upstream (curated)

Rows: 5. Language-membership: 4. fixed_upstream: 1. filed_plan: 1. false_positive: 1. out_of_scope_redos: 1. private_first: 1.

Source: [`docs/conversion-upstream.jsonl`](../../docs/conversion-upstream.jsonl).

## Corpora with properties asked

| corpus | security tool | asked | unsat | sat | sat GT | unique SAT sites |
|---|---|---|---|---|---|---|
| validatorjs | false | 644 | 616 | 28 | 28 | 7 |

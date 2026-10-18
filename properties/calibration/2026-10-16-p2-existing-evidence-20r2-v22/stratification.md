# P8 frozen-cohort stratification

This report joins the 50 exact-pin questions in the v22 retrospective checkpoint to repository and dialect family. It is a selected, correlated retrospective cohort, not a prevalence estimate. Gate IDs are deduplicated globally in the overall line and within each stratum in the table.

## By repository and dialect

| Repository | Dialect | Questions | UNSAT | SAT | Timeout | Agent-derived / human | Local gates | Product replays | Differential cases |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Agenticstiger/forge-cli` | py_re | 6 | 6 | 0 | 0 | 1 / 5 | 1 | 1 | 5,680 |
| `Leviticus-Triage/llm-honeypot-intelligence` | posix-shell | 2 | 0 | 2 | 0 | 2 / 0 | 1 | 2 | 65,545 |
| `TracecatHQ/tracecat` | py_re | 2 | 1 | 1 | 0 | 2 / 0 | 2 | 2 | 2,156 |
| `chainguard-dev/malcontent` | go_re | 2 | 0 | 2 | 0 | 2 / 0 | 2 | 2 | 35,243 |
| `fu351/Doberman-Core` | py_re | 5 | 2 | 3 | 0 | 3 / 2 | 2 | 5 | 514 |
| `greydragon888/real-router` | ecma | 2 | 2 | 0 | 0 | 2 / 0 | 2 | 2 | 34,041 |
| `h0tak88r/AutoAR` | go_re | 3 | 2 | 1 | 0 | 3 / 0 | 3 | 3 | 827 |
| `json-editor/json-editor` | ecma | 1 | 1 | 0 | 0 | 1 / 0 | 1 | 1 | 1,116,985 |
| `magiclabs/magic-js` | ecma | 10 | 10 | 0 | 0 | 10 / 0 | 1 | 10 | 481,034 |
| `marcusquinn/aidevops` | posix-shell | 11 | 8 | 2 | 1 | 11 / 0 | 4 | 11 | 789 |
| `mycelium0/mycelium` | posix-shell | 1 | 1 | 0 | 0 | 1 / 0 | 1 | 1 | 3,814 |
| `netspooky/inhale` | py_re | 2 | 0 | 2 | 0 | 2 / 0 | 1 | 2 | 6 |
| `open-horizon/anax` | go_re | 1 | 1 | 0 | 0 | 1 / 0 | 1 | 1 | 687 |
| `panther-labs/panther-analysis` | py_re | 1 | 0 | 1 | 0 | 1 / 0 | 1 | 1 | 9 |
| `xibosignage/xibo-cms` | ecma | 1 | 1 | 0 | 0 | 1 / 0 | 1 | 1 | 1,007 |
| **Overall** | — | **50** | **35** | **14** | **1** | **43 / 7** | **24** | **45** | **1,748,337** |

The v22 aggregate's 43 agent-derived questions account for 30 UNSAT, 12 SAT, and one timeout; its seven human-provenance questions account for five UNSAT and two SAT. Provenance labels describe contract origin, not reviewer labor or execution time. The baseline has no matched exact-pin human denominator or comparable time/cost series, so autonomous-versus-human efficacy and speed comparisons are not permitted. The [machine-readable stratification](stratification.json) records this limitation and the joined input digests.

## P8 fresh review correction

A full same-model review of Aidevops's 11-row source-order census confirmed six skips and one unresolved numeric-config site. It also narrowed two adopted contracts: the SHA and PR UNSAT queries prove their regex languages, not the full cache-invalidator or positive-PR dispatch behavior described by the historical contracts. Corrected regex-only contracts passed the pinned local gate; the frozen v22 checkpoint remains unchanged. The full slug-helper inclusion still times out and remains not proven. See the [audit overlay](../2026-10-16-p8-v22-audit/README.md) and its [row-level JSON](../2026-10-16-p8-v22-audit/audit.json).

## Limits

- The cohort is selected and correlated; strata are small and do not estimate unreviewed-site prevalence.
- A gate used by multiple questions may be counted in multiple strata; the overall count deduplicates gate IDs.
- The v22 checkpoint preserves its own pending-product-triage snapshot. The v11 outcome overlay separately covers all 14 SAT questions.
- Costs, tokens, source-review time, human active time, and consumer-adoption measures remain unknown or separately zero; unknown is not zero.

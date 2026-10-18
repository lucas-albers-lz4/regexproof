# P2 retrospective product evidence checkpoint v19

This checkpoint joins historical and newly executed product evidence to the
frozen `2026-09-12-calibration-20-r2` source cohort and P2 source inventory v4.
It preserves the exact pins and counts only source-matched, contract-backed
product questions. It is a retrospective evaluation set, not new prospective
yield.

## Result

| Measure | v19 |
|---|---:|
| Eligible, attempted, decided unique questions | 46 |
| UNSAT guarantees | 32 |
| Ground-truthed SAT questions | 14 |
| Not proven / not attempted | 0 / 0 |
| Useful local runnable regression gates | 23 |
| Product-engine witness replays | 41 |
| Question-attributed differential cases | 1,747,618 |
| Consumer-adopted gates | 0 |
| Confirmed security impacts / external reports / maintainer confirmations / fixes | 0 / 0 / 0 / 0 |

There are four questions left to the 50-question evaluation checkpoint and 54
to 100. These are measurement checkpoints, not success thresholds. All 14 SAT
questions are pending product triage. A SAT witness reproduced in the regex
or helper is not by itself evidence of a security impact.

The question set includes 39 autonomous and seven historical human-provenance
contracts. The contract-provenance split does not change the product outcome
counts. The useful-proof/gate track, reachable bug candidates, and downstream
outcomes are reported separately.

## Source and exclusion accounting

The v4 inventory contains 20,705 raw source rows. Nineteen repository pins
were complete under the registered file selection; Everclaw remains
incomplete because six submodules could not be materialized. Inventory rows
are not assumed to be security boundaries or product questions.

The checkpoint matched 46 unique questions and retained five excluded
attempts across three question identities:

- AutoAR's HTML `esc` transform is outside the cohort's declared Go-regex
  dialect inventory.
- Malcontent's CVE YARA rule is outside the cohort's declared RE2 inventory.
- Two earlier Json Editor attempts used a line-only selector that matched
  multiple regexes; the later exact `column-24` source identity is included
  once.

These excluded rows remain visible in `source-checkpoints.json`; none was
silently dropped or counted as an eligible question. The input-set digest is
`00a4242a5e2c40787819e899418c494054168ab9719a205a58a3a61fdc330ebb` and the
product-coverage digest is
`ac8bde24401612c5456e41d1317c9cdc692e3c0ac160ab5ae570725bf0b9a4ed`.

## Reproduction and related measures

The complete machine-readable report is `report.json`; the matched questions,
roster, checkpoint, and source joins are preserved in `attempts.json`,
`roster.json`, `checkpoint.json`, and `source-checkpoints.json`.

```sh
.venv/bin/python scripts/conversion-checkpoint.py \
  properties/calibration/2026-10-16-p2-existing-evidence-20r2-v19/checkpoint.json
```

The run-level scorecard at
[`after-predispatch-residual`](../2026-10-16-autonomous-scorecard-20r2-after-predispatch-residual.json)
records 28 runs, 42 proof attempts, 41 decided attempts, 32 UNSAT guarantees,
nine SAT candidates/replays/reachable local violations, 28 local gate
executions, 30 mutation checks, and 3,486,352 differential cases. It counts
timed runs and retries, so its denominators differ from the deduplicated P2
checkpoint. Confirmed impacts, consumer adoption, external reports,
confirmations, and third-party fixes are all zero. Elapsed time is 2,167.814
seconds across `wall_clock` and `phase_sum` bases; tokens, cost, and human
active time remain unmeasured.

The source inventory and its limitations are documented in
[`inventory v4`](../2026-10-16-p2-source-inventory-v4/README.md). The latest
Aidevops source review is the [first 15-site wave](../2026-10-16-autonomous-aidevops-predispatch-github-text-20r2/README.md)
plus its [14-site residual census](../2026-10-16-autonomous-aidevops-predispatch-github-text-residual-20r2/README.md).

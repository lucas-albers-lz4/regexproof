# 20-r2 compatible existing product evidence v15

This retrospective checkpoint joins existing exact-pin product evidence to
the corrected v3 inventory. It is not a prospective sample or an estimate of
future conversion yield.

## Snapshot

- Frozen cohort: `2026-09-12-calibration-20-r2`, manifest digest
  `5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d`.
- Inventory: 20,705 raw sites across 19 complete repositories and one
  repository with six unavailable submodules. Inventory v3 removes 79
  JavaScript hashbang false positives from v2.
- Compatible evidence: **42** unique exact-pin product questions; **30
  UNSAT** and **12 ground-truthed SAT**. The SAT rows remain pending product
  triage.
- Contract provenance: 35 autonomous and seven historical human contracts.
- Useful local regression gates: 19. Product-engine replays: 37.
  Question-attributed differential cases: 1,713,577.
- Consumer-adopted gates, confirmed security impacts, external reports,
  maintainer confirmations, and third-party fixes: zero.
- The checkpoint is 42 of the 50-question target, a shortfall of 8. Five
  attempts across three questions are excluded: three source sites are outside
  the declared P2 inventory and two Json Editor attempts use an ambiguous
  line-only selector.

The separate [run-level scorecard](../2026-10-16-autonomous-scorecard-20r2-after-server-name.json)
summarizes 24 logged runs and 38 proof attempts. It keeps throughput, useful
proof/gate output, and downstream bug/external outcomes separate from the
checkpoint's 42 unique product-question denominator.

The v12-to-v13 increment adds two Doberman Codex apply_patch path-extraction
questions, both UNSAT, and one exact-source local gate. The formal contracts
cover one-character printable-ASCII destinations. The AST replay gate
compares the pinned `_apply_patch_paths` and `to_normalize_input` helper code
against 514 directive cases, including longer sample paths, indentation,
CRLF, and a mixed multi-directive envelope. A source-weakened Delete mutation
is SAT and ground-truthed. These results do not prove unbounded path
completeness or the correctness of every protected-path rule. The full
Doberman adapter could not be imported because Pydantic is absent in the
local environment; the gate uses the exact source AST subset and standard
library.

The v13-to-v14 increment adds one Tracecat MCP stdio environment-key question
at the frozen `TracecatHQ/tracecat@c84d52528a489821f355fc63976fbc7783ae0ad5`
pin. The validator uses `^...$`; CPython accepts a key ending in one final
line feed, outside the exact ASCII grammar declared by Tracecat's comment and
error message. The exact `validate_mcp_command_config` path accepts the
witness, and a local POSIX child process receives that environment key. A
strict `\Z` mutation rejects it and restoring `$` makes it pass again. The
standalone exact-source gate compares 1,442 deterministic cases with an
independent model and reports zero mismatches. This is a reproduced
configuration-validation gap; it does not establish command injection,
privilege escalation, or security impact in an MCP server. The P6 wave remains
`needs_review` pending product triage.

The v14-to-v15 increment adds a Tracecat server-name separator invariant at
the same frozen repository pin, from a distinct inventory row in
`mcp_validation.py`. Z3 proved, without a length bound, that the accepted
character class excludes `/` and `\`. Its source-weakened slash mutation is
SAT and ground-truthed through `validate_mcp_command_config`. The pinned-source
CPython gate checked 714 deterministic names with zero model mismatches. This
is a positive invariant only; it does not claim path traversal or security
impact. Its P6 wave completed with one UNSAT question and a 0.6676-second
phase sum.

## P2 source-review coverage

Eleven selected repository slices have complete source-review artifacts; this
does not cover the full 20-member cohort.

| Repository slice | Sites | Skips | Unresolved | Adopted |
|---|---:|---:|---:|---:|
| Malcontent Go regexes | 15 | 11 | 2 | 2 |
| Anax Go regexes | 26 | 15 | 10 | 1 |
| AutoAR Go regexes | 34 | 28 | 3 | 3 |
| llm-honeypot POSIX shell | 16 | 14 | 0 | 2 |
| Panther Python regexes | 45 | 44 | 0 | 1 |
| Inhale Python regexes | 3 | 0 | 1 | 2 |
| BinaryAlert Python regexes | 1 | 1 | 0 | 0 |
| Snyk LS Go regexes | 37 | 36 | 1 | 0 |
| Json Editor ECMA regexes | 96 | 94 | 1 | 1 |
| Magic JS ECMA regexes | 64 | 53 | 1 | 10 |
| Doberman Core Python regexes | 104 | 19 | 83 | 2 |
| **Total** | **441** | **315** | **102** | **24** |

Separately, targeted reviews covered two Tracecat inventory sites and adopted
two contracts. They are not a complete Tracecat slice review. Across those
artifacts, 443 exact inventory sites have been individually reviewed and 26
contracts adopted; the 441-site table above continues to describe only the
eleven complete slices.

Unresolved rows remain outside product-question counts. The source review
does not infer completeness for Doberman's shell-command and destructive
operation heuristics from their security-facing call sites.

## Downstream candidate overlay

The separate [v10 SAT impact triage](../2026-10-16-p2-sat-impact-triage-v10/README.md)
covers all twelve SAT questions in v15: it refutes two historical Doberman
claims and retains ten candidates across eight issue families. It is bound to
v14, which has the same SAT question set; v15 adds only an UNSAT property.
The Tracecat environment-key candidate remains unconfirmed pending downstream
consequence evidence. All twelve SAT rows remain pending in the strict
checkpoint. Confirmed impact and external outcomes remain zero.

## Reproduction

```sh
.venv/bin/python scripts/build-p2-evidence-checkpoint.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-15-p2-source-inventory-v3/inventory.json \
  --sites properties/calibration/2026-10-15-p2-source-inventory-v3/sites.ndjson \
  --checkpoint-root properties/calibration \
  --conversion-root properties/generated \
  --repo-root . \
  --out-dir properties/calibration/2026-10-16-p2-existing-evidence-20r2-v15

.venv/bin/python scripts/conversion-checkpoint.py \
  properties/calibration/2026-10-16-p2-existing-evidence-20r2-v15/checkpoint.json
```

Exact identities, attempts, and source joins are in `checkpoint.json`,
`attempts.json`, and `source-checkpoints.json`; aggregate metrics are in
`report.json`. The v14 checkpoint remains a frozen historical snapshot.

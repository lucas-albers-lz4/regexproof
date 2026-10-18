# Real-Router navigation parameter control-character P6 calibration

This bundle records one source-reviewed site through candidate intake,
contract adoption, queue transitions, proof, exact-source replay, and wave
close-out. It is a singleton integration calibration, not the P7 target of
15 reviewed sites and up to five adopted contracts.

## Source and contract

- Cohort: `2026-09-12-calibration-20-r2`; frozen Real-Router pin:
  `55aa7ef43a9c129beba90823cd8a4db10bb01211`.
- Site: `packages/validation-plugin/src/validators/navigation.ts:69:25`,
  regex `[\\u0000-\\u001F\\u007F]`.
- Contract: string values in own enumerable navigation parameters supplied by
  application callers to the opt-in `validateNavigateParams` callback are
  rejected if they contain C0 controls or DEL. Trust is `config`; no remote
  attacker input is established.
- Adoption used the standing `autonomous-contracts-v1` delegation. The source
  review is bound to pinned implementation, plugin wiring, functional test,
  changelog, inventory identity, and source hashes in `review-evidence.json`.
- The admission GO decision is based on repository scale. Its
  `security-boundary` condition is false.

## Result

- One unique product question: `RR-navigation-param-control-characters-rejected`.
- Formal shape-1 alphabet property: UNSAT (the regex matches every ASCII C0
  and DEL character in the declared domain).
- Source mutation: omit DEL from the pinned expression. The original helper
  throws `TypeError`; the weakened helper accepts DEL. The mutation guard is
  SAT and replayed against the exact pinned helper.
- Node v26.11.1 local product gate: 17,014 differential input values,
  zero mismatches.
- The frozen close-out records four runner invocations (three failed resumes
  preserved), one unique product solver-question execution, no solver retry,
  and a 1.1065-second final-resume phase sum. The early failures were a
  mistaken mutation formula, a callback witness-key mismatch, and a gate
  interpreter that lacked `jsonschema`; the final dependency-light gate argv
  passed without repeating the UNSAT question.
- Queue state is `contracted`; corpus wave `rr-nav-controls-p6-20261016`
  closed successfully at generation 1 with a valid event log.
- Bug and downstream outcomes: zero SAT product candidates, zero confirmed
  impacts, zero consumer-adopted gates, zero reports, confirmations, or fixes.

This result demonstrates one composed serial lifecycle and one useful local
contract-backed proof/regression gate. It does not demonstrate ranking
quality, stratified allocation, a representative yield, a security finding,
or P7 completion. The P7 15/5 wave and the generic P6 orchestration work remain
open.

## Reproduction

The runner state, frozen roster, queue transition replay, proof/gate outputs,
and close-out are under `p6-wave/`. The canonical conversion row is
`properties/generated/real-router_conversion.ndjson`; the refreshed aggregate
is `properties/generated/conversion-ledger.{json,md}`. The run-level metrics
are in `properties/generated/autonomous_work.jsonl` and the frozen scorecard
linked from the v17 checkpoint README.

With the exact clean source checkout available at the frozen pin:

```sh
.venv/bin/python scripts/z3-verify.py \
  RR-navigation-param-control-characters-rejected \
  RR-navigation-param-del-omission-mutation \
  --require-ground-truth --json

.venv/bin/python scripts/real-router-navigation-control-regression-gate.py \
  --source-root /tmp/regexproof-pinned-sources/real-router-55aa7ef43a9c129beba90823cd8a4db10bb01211 \
  --output properties/calibration/2026-10-16-p2-real-router-navigation-source-review/p6-wave/product-gate-reproduction.json
```

The gate verifies the pin, cleanliness, source-file digests, adopted contract,
review evidence, frozen roster, and pre-outcome history. Its replay copies the
pinned TypeScript helper and guard bodies into temporary modules; it only
rewrites one extensionless import and the sole parameter-property constructor
to equivalent JavaScript so Node's native TypeScript stripper can execute
them. See `p6-wave/product-gate.json` for these adaptations and source hashes.

## Duplicate-prevention follow-up

The next scheduler snapshot initially offered this completed bucket again:
its ledger row used canonical `corpora: ["real-router"]` while the P6
`wave_id` had a wave-specific name. The scheduler now marks the canonical
corpus/bucket consumed before consulting legacy wave-id attribution; the
focused regression check passes and the regenerated schedule has no available
Real-Router bucket. The related history-index fix matches legacy token-name
selectors to current source inventory columns by repository, pin, path, line,
and exact regex signature. Where a historical row has no pattern signature, a
same-line alias is conservatively treated as already reviewed. The refreshed
dated history index and canonical `question-history-index.json` are byte
identical (324 sources, 76 asked identities, 576 reserved sites, seven
unbound records). The six focused scheduler/history checks passed. These are
duplicate-prevention repairs only; they are not a 15-site P7 intake.

# 12-hour work plan: replay forge-cli sensitive environment redaction

**Scope:** one sink, one pinned source, one contract proposal. Stop after 12
hours; do not widen into another forge-cli sink or a new corpus cohort.

**Parent:** the helper-image slice in [plan.md](plan.md), wave 1 in
[`sweep/forge-cli-conversion/plan.md`](../forge-cli-conversion/plan.md), and
the human-contract workflow in [`docs/CONTRACTS.md`](../../docs/CONTRACTS.md).
Wave 1 explicitly left the real renderer image unverified.

## Question and declared domain

At forge-cli commit `efcf8e4c0087def553a737dc1c4eebda5d8a90cd`, does
`fluid_build.build_runners.dbt.runner._render_command_for_log` replace
documented sensitive `KEY=VALUE` arguments with `KEY=<redacted>`?

The finite replay domain is:

- each of the 5,680 ASCII letter-case assignments of the documented key
  spellings: `password`, `passphrase`, `secret`, `token`, `credential`,
  `auth`, `api[_-]?key`, and `private[_-]?key` (including empty separators);
- each key after both `-e` and `--env`, with `CLEAR_SENTINEL` as the value;
- the separately enumerated ordinary, near-miss, empty-value, delimiter,
  repeated-entry, mixed-case, substring, and terminal-newline fixtures in
  `tests/test_forge_cli_harness.py`.

The guarantee is limited to these exact command fixtures. Do not generalize to
arbitrary values, non-ASCII keys, unlisted keys, or every possible argv shape.
Expected command strings are specified directly in the tests, independently
of the regex mirror.

## Work sequence and timebox

1. **0–1 hour — establish the boundary and adoption.** Read the pinned call
   path and `docs/TRAPS.md`; inspect only the selected changes from the dirty
   worktree. Present the exact guarantee above for human adoption. If adoption
   is unavailable, keep the solver property out of the registry and conversion
   artifacts, and ship the pinned replay only as regression coverage.
2. **1–3 hours — reuse the regex subclaim.** The existing wave-1 shape-2
   property already checks documented policy-key inclusion in the source
   pattern. Confirm that its source mirror agrees with the pinned pattern; do
   not add a duplicate registered property. This inclusion is not a proof of
   the renderer's output image. `unknown` is not proven and fails the gate.
3. **3–5 hours — replay the real helper.** Fetch or materialize the exact
   source pin, verify the loaded module path and clean checkout, and compare
   exact output strings for the full finite domain. Do not substitute a local
   implementation for the product helper.
4. **5–7 hours — exercise sensitivity and parity.** Keep an API-key mutation
   guard that returns its expected SAT sensitivity witness. A separate
   ground-truth test must replay that witness through the pinned helper under
   the weakened regex and show `CLEAR_SENTINEL` is exposed. Differentially
   compare the mirror with CPython `re` and the helper on all listed cases.
5. **7–8 hours — review concurrency and evidence handling.** Make checkout
   caching safe for parallel test processes and serialize temporary regex
   mutations. Ensure the close-out distinguishes the existing solver claim
   from the real-helper regression evidence.
6. **8–9 hours — gate artifact generation.** Without adoption, regenerate the
   existing conversion artifacts without adding a helper-image row. If adopted,
   add and emit a narrowly scoped contract only after the real replay tests,
   mutation replay, and differential checks pass. Inspect row counts, shape,
   domain, provenance, and engine versions.
7. **9–10 hours — adversarial review.** Ask a read-only reviewer to challenge
   source pinning, mirror semantics, value-domain wording, output claims,
   mutation behavior, and ledger eligibility. Address concrete issues only.
8. **10–12 hours — verify and close.** Run the targeted tests, full pytest,
   Ruff, `git diff --check`, and
   `python scripts/z3-verify.py --all --require-ground-truth
   --require-domain --require-contract --fail-on-property-failure`. Review
   the exact branch diff and CI result. Record the domain, separate solver
   and product-test evidence, engine versions, limits, and refuted claims.

## Acceptance gates

- The proposed contract records site, trust, input, finite declared domain,
  pin, and provenance. Only `human` provenance counts; without adoption, do
  not register the property or publish a conversion row.
- The solver query proves key-pattern inclusion only and is labeled shape 2.
- Tests call the real renderer at the exact pin and compare full expected
  command strings; sentinel absence is asserted for each sensitive fixture.
- The exact SAT witness for the API-key mutation is replayed through the real
  helper with the weakened policy, and the cleartext leak is asserted.
- Mirror classification agrees with CPython `re` for the declared domain.
- The full proof command treats timeout/unknown and missing contract/domain/
  mutation coverage as hard failures.
- The conversion ledger includes a product row only after every preceding
  gate passes and a person adopts the guarantee. Without that adoption, replay
  tests remain ordinary regression coverage and add zero conversion rows. No
  upstream filing or public disclosure is part of this work.

## Out of scope

JAAS, Datamesh, URL, LLM endpoint, copilot-memory sinks, changes to forge-cli,
new solver backends, general helper-image infrastructure, and the proposed
30-repository cohort refresh. Candidate data for that cohort must first be
refreshed and re-probed, as recorded in `docs/THROUGHPUT-PLAN.md`.

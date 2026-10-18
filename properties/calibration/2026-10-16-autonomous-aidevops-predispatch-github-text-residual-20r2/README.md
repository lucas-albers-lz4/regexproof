# Aidevops pre-dispatch GitHub-text residual census

This is the deterministic complement of the first frozen P7 allocation. It
closes review of the bucket's 29 candidate identities; it is not a second
sample or a replacement for the first 15-site allocation.

## Frozen scope and decisions

- Repository and pin: `marcusquinn/aidevops` at
  `8666b6c6c52472b5535aa295f2df593918152cb1`.
- Source: `.agents/scripts/pre-dispatch-validator-helper.sh`, SHA-256
  `b68445d5eaf510e820831422c6e064ac58bbdc4496483ad562df30786e3723b5`.
- Selection: all 14 candidate identities left by the first 15-site
  allocation. `residual-selection.json` records the complement; no site was
  added by backfill or selected after observing a proof result.
- Source-bound dispositions: one adopted contract and 13 evidence-backed
  skips, bound by `review-evidence.json` to the frozen population, source
  windows, and run context.

The adopted question concerns `threshold=[0-9]+` at helper line 1879,
column 51. GitHub issue-body text is untrusted. The large-file producer emits
`LARGE_FILE_LINE_THRESHOLD` as decimal text; the helper parses it from a
`threshold=` marker and compares it with `wc -l` using Bash arithmetic.
The witness `threshold=08` is accepted by the marker expression. With a
five-line fixture, the exact pinned helper reports Bash's invalid-octal
arithmetic error and returns 0 through the "premise holds" path. The same
fixture with `threshold=8` returns 10 because five lines are below the
threshold. The replay uses local `gh` and `git` stubs and an in-clone fixture;
it establishes a reachable local workflow-gate behavior, not a deployed
security impact or third-party disclosure. The finding remains
`pending_product_triage`.

The proof bundle is `contract-threshold-decimal.json`,
`proof-results-threshold.ndjson`, and `replay-threshold.json`. The contract's
adoption record uses the standing `autonomous-contracts-v1` delegation and
retains agent provenance. Z3 5.0.0 returned SAT for the counterexample finder
and for the mutation guard; the ground-truth callbacks ran the real pinned
helper on the witness and control. The measured proof plus callback phase sum
was 8.5511 seconds. Review, adoption, and queue time are outside that
measurement; token use, cost, and human active time remain unknown.

The 13 skips preserve source-based reasons in `reviews.ndjson`. They include
numeric or hash captures whose values are subsequently constrained or used
as data, fixed issue-section searches, path text used only for GitHub
correlation, and prefix stripping without an independent boundary. A raw
regex inventory row was not treated as a product property by itself.

## Queue close-out and measures

`queue-transition-replay.json` binds the isolated generation 1-to-2
close-out to the same GO decision SHA-256
`02875563f71ec7459f3a97967a663da09d281478507cba82cfd49c75ce3fcb4c` and
ledger SHA-256
`99f1f49098d8748544edf88e081d6a4cf0b5e95383827b916e0aee559d764677` as the
original allocation. It records 15 transitions: one contract and 13
out-of-scope skips. The run used its own queue state and event log; shared
campaign state was unchanged.

Across the first sample and its complete complement, the bucket has 29
source-reviewed identities, two adopted contracts, and 27 skips. The strict
P2 retrospective checkpoint now has 46 eligible exact-pin questions (32
UNSAT and 14 ground-truthed SAT), with four still needed to reach the
50-question evaluation checkpoint. This threshold is a measurement checkpoint,
not a success criterion. The 14 SAT questions remain pending product triage.
Useful contract-backed proofs and regression gates, reachable local
violations, and external outcomes remain separately counted; no confirmed
security impact, consumer-adopted gate, report, maintainer confirmation, or
fix resulted from this residual census.

The current P2 detail is in the [v20 checkpoint](../2026-10-16-p2-existing-evidence-20r2-v20/README.md); the original residual-wave run was recorded against the earlier v19 snapshot.
The run-level scorecard remains separate because it counts timed run records
and executed attempts rather than deduplicated retrospective questions:
[`post-residual scorecard`](../2026-10-16-autonomous-scorecard-20r2-after-predispatch-residual.json).

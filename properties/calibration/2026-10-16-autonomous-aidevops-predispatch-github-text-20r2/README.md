# Aidevops pre-dispatch GitHub-text P7 wave

This is the first completed serial 15-reviewed/up-to-5-adopted wave in the
frozen `2026-09-12-calibration-20-r2` cohort. It is a source-review and proof
calibration for the `pre-dispatch-github-text` bucket, not evidence of general
corpus yield.

## Frozen inputs and allocation

- Repository: `marcusquinn/aidevops`
- Commit: `8666b6c6c52472b5535aa295f2df593918152cb1`
- Reviewed helper: `.agents/scripts/pre-dispatch-validator-helper.sh`
- Helper SHA-256: `b68445d5eaf510e820831422c6e064ac58bbdc4496483ad562df30786e3723b5`
- Candidate population: 29 source identities, frozen in
  `candidate-population.json` before source decisions.
- Allocation: 15 selected (10 novel-idiom and five unbiased), recorded in
  `allocation.json`; selection seed and selected rank order are preserved.
- Review result: one adopted contract and 14 evidence-backed skips.

The 14 unselected identities remain outside this frozen sample. Any later
review of them is follow-on work and must not be added to this wave's 15-site
denominator.

`review-evidence.json` binds the decisions to exact-pin source windows, file
hashes, the frozen shortlist, and run-context digest. The corrected
[`queue-transition-replay-r2.json`](queue-transition-replay-r2.json) records
all 16 isolated transitions: one contract, two duplicate skips, and 12
out-of-scope skips. It binds to the exact GO decision SHA-256
`02875563f71ec7459f3a97967a663da09d281478507cba82cfd49c75ce3fcb4c` used by
the frozen allocation and the conversion-ledger SHA-256
`99f1f49098d8748544edf88e081d6a4cf0b5e95383827b916e0aee559d764677`. It
closed generation 0 to 1 without changing the shared campaign queue or event
log. The initial replay is preserved as
[`queue-transition-replay-initial-gate-mismatch.json`](queue-transition-replay-initial-gate-mismatch.json):
it used a different, same-pin GO decision file and therefore did not bind to
the frozen allocation's exact GO snapshot.

## Adopted contract and proof result

The adopted site is
`.agents/scripts/pre-dispatch-validator-helper.sh:1878:column-46`,
`grep -oE 'cited_file=[^ >]+'`. Public issue body text is untrusted input. The
large-file producer emits a repository-relative `lf_path`; the helper says it
re-measures that path against fresh `HEAD`, then joins the captured value below
`${SCRATCH_DIR}/repo/` and runs `wc -l`.

The contract asks that this path resolve to a regular file inside the fresh
clone. The exact pinned helper accepted the witness `../oracle.txt`, resolved
it to a temporary fixture at the parent of the mock clone, and measured its 37
lines. The replay used local `gh` and `git` stubs. It establishes local path
reachability only: it did not invoke a remote helper, prove public disclosure,
access user data, or establish a confirmed security impact. The candidate
remains `pending_product_triage`.

The proof registry contains a contract-backed SAT counterexample finder and a
mutation guard. Both returned the same witness; the product property was
ground-truthed through the exact pinned helper. Solver version was Z3 5.0.0.
The local gate is useful for guarding the stated clone-containment property;
the repository has not adopted it as a consumer gate.

Reproduce the registered proof and mutation guard with:

```sh
.venv/bin/python scripts/z3-verify.py --json \
  --require-ground-truth --require-domain --require-contract \
  --fail-on-property-failure \
  AE-aidevops-predispatch-cited-file-traversal-read \
  AE-aidevops-predispatch-cited-file-traversal-mutation-guard
```

The exact stdout is preserved in `proof-results.ndjson`; the source replay
record is `replay-cited-file.json`. The recorded 7.1128-second `phase_sum`
covers the property, ground-truth callback, and mutation guard. It excludes
candidate intake, source review, contract drafting/adoption, and queue work.
Token use, cost, and human active time are unmeasured.

## Product and campaign accounting

- One eligible exact-pin product question was added to the strict P2
  checkpoint. After the first wave, the checkpoint was 45/50; the complete
  14-site complement later added one more question, bringing the current
  checkpoint to 46/50. See the
  [residual census](../2026-10-16-autonomous-aidevops-predispatch-github-text-residual-20r2/README.md)
  and [v19 checkpoint](../2026-10-16-p2-existing-evidence-20r2-v19/README.md).
- Useful local regression gates: +1.
- SAT witnesses replayed: +1; locally reachable violations: +1.
- Confirmed security impacts: +0.
- Consumer-adopted gates, reports sent, maintainer confirmations, and fixes:
  +0.
- Downstream disposition: pending product triage.

The run row is in `properties/generated/autonomous_work.jsonl`; the exact
conversion product row is in `aidevops_conversion.ndjson` and the canonical
`properties/generated/aidevops_conversion.ndjson`. The source review, contract,
replay, proof, roster, checkpoint, and isolated queue transition artifacts in
this directory are the reproducibility bundle.

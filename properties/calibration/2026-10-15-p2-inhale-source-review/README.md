# Inhale exact-pin P2 source review

This is a complete raw-regex review for one frozen cohort member. It does not
cover the remaining cohort or close P2.

## Scope and result

- Repository: `netspooky/inhale`
- Pin: `889bbe2ab4a40a85c7ccd8399b2fd3cfddf539e8`
- Extracted Python regex sites reviewed: **3**
- Evidence-backed skips: **0**
- Unresolved: **1**
- Adopted contracts / product questions: **2**

The evidence builder confirms the complete three-site review against the exact
source inventory and checkout. The URL matcher at line 7 participates in
recursive link resolution and the crawler's prefix filter, so it is not a
cosmetic site. A local helper replay demonstrates that a link to
`https://trusted.example.attacker.test/malware.bin` passes the filter when the
root is `https://trusted.example` without a trailing slash. This remains
unresolved and is excluded from product counts because the repository does not
independently state a same-origin requirement. The trailing-slash root blocks
that synthetic cross-origin link; the behavior depends on the caller's URL
form. See [`scope-exploration.json`](scope-exploration.json).

## Adopted output-directory contracts

The README promises that `-o OUTDIR` stores scraped files in that specific
directory. The CLI sends `-u` and entries read from `-l` to `getSingleFile`, and
`-r` to `parseDir`. Both helpers strip only `https?://`, concatenate the
remaining URL text to the configured output path, then create and write the
resulting filesystem destination.
Before those calls, `inhale.py` constructs `fpath` as `./` plus `args.outdir`
plus `/`. The exact-helper replay uses that same relative form while its
working directory is a disposable fixture, then resolves the resulting file
against the fixture's `-o` root.

The frozen inventory classifies these compile sites with `call_kind=search`,
but the pinned helper invokes `Pattern.sub` at both call sites. The proof
registry records the actual substitution semantics; the raw inventory remains
unchanged and its extraction label is visible in the source-review evidence.

Two source-bound contracts record the distinct save paths:

- [`file-contract.json`](file-contract.json):
  `https://downloads.example/../../escape.bin` escapes the `-o` directory in
  `getSingleFile`.
- [`directory-contract.json`](directory-contract.json):
  `https://downloads.example/../../directory.bin` escapes the `-o` directory
  in `parseDir`.

Both are classified as `config`: these examples are supplied through the
operator's CLI URL or URL-list input. The synthetic response bytes are written
only inside disposable temporary fixtures. The source review does not establish
that an untrusted party controls these CLI inputs or that a real deployment
was affected.

## Proof and gate

[`proof-report.ndjson`](proof-report.ndjson) records two exact-witness SAT
counterexample-finders with replay against the pinned Python helper, plus the
family mutation guard. The mutation widens the scheme-strip regex to
`https?://[^/]+/`; for `https://downloads.example/../escape.bin`, the baseline
resolves inside `-o` and the mutated helper resolves outside it.

The local gate in [`product-replay.json`](product-replay.json) compares three
URLs for each save path (normal, one parent segment, two parent segments) with
the exact helper. All six predicted paths match the helper. The regression
candidate reproduces in both functions, the mutation passes, and all writes
stay inside a temporary directory. No network request is made. The P6 runner
rechecked the source pin, both SAT witnesses, mutation guard, and gate; its
expected state is `needs_review` because both SAT candidates need product
impact disposition. See [`p6-wave-r1/`](p6-wave-r1/).

## Claims checked and limits

- `-o` is documented as a specific output directory; the path escape is
  reproduced for concrete `-u`, `-l`, and `-r` URL forms.
- A single `..` segment remains within the output directory because the
  stripped hostname component absorbs it; two segments escape that directory.
- The file and directory paths are separate reviewed source sites but share
  one downstream candidate family.
- The recursive cross-origin prefix case is recorded as unresolved. Its
  apparent scope intent is not enough to adopt a same-origin contract without
  independent product evidence.
- No external report, maintainer confirmation, security impact, consumer gate
  adoption, or fix is recorded.

## Reproduction

```sh
.venv/bin/python scripts/z3-verify.py \
  IH-inhale-file-url-output-root-confinement \
  IH-inhale-directory-url-output-root-confinement \
  IH-inhale-weakened-url-strip-traversal-mutation \
  --require-ground-truth --require-domain --require-contract --json \
  --fail-on-property-failure

.venv/bin/python scripts/inhale-output-path-regression-gate.py \
  --source-root /tmp/regexproof-pinned-sources/inhale-889bbe2ab4a40a85c7ccd8399b2fd3cfddf539e8 \
  --output properties/calibration/2026-10-15-p2-inhale-source-review/product-replay.json
```

The immutable roster, contracts, review evidence, product replays, and P6
attempts are retained with this review bundle.

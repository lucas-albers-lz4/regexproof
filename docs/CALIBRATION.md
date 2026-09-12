# PR5 calibration execution

PR5 runs the first ten repositories from a frozen PR2 manifest. It is an
execution artifact, not a new selector: membership, URL, commit pin, family,
and repository order come only from the manifest.

The operator prepares local checkouts at the exact pins, then runs:

```text
python scripts/calibration.py properties/calibration/2026-09-10-10/manifest.json \
  --repo owner/a=/srv/calibration/owner-a \
  --repo owner/b=/srv/calibration/owner-b \
  --output-dir properties/calibration/2026-09-10-10
```

The command never clones, fetches, or updates a checkout. It verifies
`git rev-parse HEAD` against every manifest pin and scans the pinned tree with
the registered `extract_repo()` and `_ident_of()` implementation from
`scripts/dogfood-singleton-analysis.py`. Canonical IDs are the exact tuple
`(canon(pattern), flags, dialect)`, with shell syntax retained as the fourth
element. `novel_sites` counts site instances whose canonical ID is absent from
the preceding eligible prefix for that family.

Manifest dialect families are checked against the dialects emitted by the
registered extractor before an observation is counted. An assignment with no
compatible extractor, including the current `go_re` family until the dogfood
runner emits `re2` records, is recorded as `unsupported_dialect`; records from
another language are never relabeled as evidence for the manifest family.

The command emits these committed artifacts:

| Artifact | Meaning |
|---|---|
| `canonical-observations.json` | Ordered observations, canonical IDs, counts, and the embedded manifest |
| `saturation-report.json` | PR1 report, emitted only when every repository completed |
| `skip-failure-log.json` | Exact missing-pin, missing-checkout, empty-inventory, oversized-file, unsupported-dialect, or extractor failures |
| `closeout.json` / `closeout.md` | Continue, retarget, or stop decision and per-family outcomes |

The producer records an incomplete cohort as incomplete. It never turns a
missing repository into a zero-novelty row, and PR1's saturation envelope
cannot be projected until all ten observations are present. A family with
fewer than two completed eligible repositories is `insufficient_data`, never
`saturated`.

The PR4 conversion checkpoint may be supplied with `--conversion-report`. Its
product funnel remains a separate arm: no conversion rows are invented by the
compiler observation step, and zero filing is not evidence that compiler
idioms are exhausted.

The first ten-repository close-out can recommend continuing to 20, but it
cannot claim that 20 or 30 have been evaluated. The committed manifest digest,
observation artifact, failure log, and close-out are the evidence for the
issue decision.

# P2 exact-pin source inventory v2

This is the refreshed raw regex-site inventory for the frozen
`2026-09-12-calibration-20-r2` cohort. It supersedes the v1 artifact after a
Go extractor omission was found during Anax source review.

## Contents and limits

- 20,784 extracted sites across 20 pinned repositories.
- 19 repositories are complete under the registered file selection.
- Everclaw contains 464 root-repository sites; six submodule gitlinks remain
  unavailable because its `.gitmodules` file does not map them correctly.
- The `sites.ndjson` SHA-256 is
  `381c0ca4d80c8f050b5446f378f6d95bd9b54ec83c02a48e5072a10beaabc73c`.
- The five additions over v1 are one production literal `regexp.MatchString`
  site in AutoAR, two production literal `regexp.MatchString` sites in Anax,
  and two test-only direct-call sites in Snyk LS.

The Go extractor now recognizes static literal arguments to `regexp.Match`,
`MatchString`, and `MatchReader`, as well as the previously supported
`Compile` and `MustCompile` APIs. Calls whose pattern is computed at runtime
remain outside this literal-pattern inventory and require the classification
workflow in `docs/DYNAMIC.md`.

These are raw source sites, not boundary-reviewed candidates. Each row remains
unreviewed in this inventory; the source-review artifacts separately record
the 26-site Anax review and its decisions.

## Reproduction

The pinned checkouts are under `/tmp/regexproof-pinned-sources` in the working
environment. The freezer writes the per-repository manifest and available
rows before returning a nonzero status for the known Everclaw submodule gap.

```sh
.venv/bin/python scripts/freeze-p2-source-inventory.py \
  --manifest properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --checkout-root /tmp/regexproof-pinned-sources \
  --out-dir properties/calibration/2026-10-15-p2-source-inventory-v2
```

The manifest digest remains the frozen 20-r2 digest. The extractor fingerprint
and individual source-file hashes are in `inventory.json` and `sites.ndjson`.

# P2 exact-pin source inventory v5

**Cohort:** `2026-09-12-calibration-20-r2`
**Frozen manifest SHA-256:** `5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d`
**Inventory SHA-256:** `e2d6b921bc7f2910eab6ce6f6f63aa1e1832881a81823cd84ac70053e9e0af3a`

The exact-pin extraction contains **21,956 raw regex-site rows** across 20
repositories. Nineteen repositories are complete under the registered file
selection. Everclaw remains incomplete because six submodules could not be
materialized; its 423 root sites are still listed with that limitation. The
inventory covers registered Python AST, Babel ECMA, Go regexp, and POSIX shell
extractors, including hidden paths. These are source sightings only: they are
not reviewed boundaries, adopted contracts, or product questions.

The exact-pin follow-up found that the pinned root tree has no `.gitmodules`
file. It contains six gitlinks with commit IDs but no complete path-to-URL
mapping, so their contents cannot be attributed and fetched reproducibly from
this checkout alone. This corrects the earlier plan note that called the file
malformed. See the [submodule audit](../2026-10-16-p2-everclaw-submodule-audit/README.md)
for the pinned tree evidence and the limits of an in-tree install URL.

## Extractor correction

V4 contained 20,705 rows; v5 contains 21,956, a net increase of 1,251. Review
of the exact pinned Aidevops webhook receiver
found that the shell extractor omitted Bash `[[ ... =~ ... ]]` comparisons when
they shared a condition with `&&` or `||`, or continued over a backslash-newline.
The extractor now records each unquoted regex operand in such conditions.

The same review found 26 prior Bash rows truncated at `]]` inside POSIX
character classes such as `[[:space:]]`. V5 removes the 26 malformed records
and adds 1,277 corrected or newly found records, for the net increase above.
The extractor now recognizes the closing `]]` as a shell token and keeps the
full test context. The corrected source records
include the webhook receiver's numeric comparisons at lines 147, 149, 189,
257, and 302.

The `[[` scanner remains a labeled source extractor, not a complete Bash
parser. Every product claim still requires a source-backed contract, exact
engine replay, and the applicable mutation and regression gates.

## Files

- `inventory.json`: manifest, extractor fingerprints, repository pins,
  completeness, and extraction limits.
- `sites.ndjson`: deterministic exact-pin source records.

The inventory freeze returned a nonzero status because Everclaw's six
submodules are unavailable in the pinned checkout. It completed the other 19
repositories and records Everclaw as incomplete rather than treating it as a
complete inventory.

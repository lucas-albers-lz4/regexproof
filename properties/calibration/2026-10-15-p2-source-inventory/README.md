# 20-r2 exact-pin source-site inventory

This is the raw regex-site inventory for the frozen cohort at
[`2026-09-12-calibration-20-r2/manifest.json`](../2026-09-12-calibration-20-r2/manifest.json).
The cohort manifest digest is
`5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d`.

`inventory.json` binds the run to the raw manifest hash, registered extractor
source hashes, Python runtime, repository pins, and Git tree OIDs. `sites.ndjson`
contains one record per extracted site with the source file's worktree SHA-256,
Git blob OID and mode, regex ID, and source window. Reproduce from clean exact-pin
checkouts with:

```sh
python scripts/freeze-p2-source-inventory.py \
  --manifest properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --checkout-root /tmp/regexproof-pinned-sources \
  --out-dir properties/calibration/2026-10-15-p2-source-inventory
```

The checkout-root convention is `<repo basename>-<frozen pin>`. The command
checks the checkout HEAD, origin URL, clean status, and source paths before it
accepts records. It uses the cohort member's declared dialect family and
`dogfood.extract_repo(include_hidden=True)`, so hidden product paths such as
`.agents/` are scanned. The registered fixed skips remain: `.git`,
`node_modules`, `dist`, `build`, `.venv`, `venv`, `__pycache__`, `.tox`,
`coverage`, `htmlcov`, and `.next`. Files over 2 MB, unsupported or empty
inventories, and gitlinks remain visible as incomplete repository statuses.
The command writes its artifact atomically and exits nonzero when a cohort
member is incomplete.

The first pass had 10,231 sites because it used the default hidden-path filter;
that pass missed Aidevops's `.agents/` tree and is superseded. Its hashes and
the correction evidence are recorded in
[`superseded-pass.json`](superseded-pass.json). The current pass includes
11,330 Aidevops shell sites, matching the exact-pin corpus scan.

## Snapshot

- Cohort members: 20
- Repositories complete under the registered file selection: 19
- Incomplete repositories: 1
- Extracted source sites: 20,779
- Boundary-reviewed sites: 0
- Adopted contracts: 0
- Attempted questions: 0
- Solver outcomes: 0
- `sites.ndjson` SHA-256: `a1996ab9b4a90314aa69b8476c913199bb0de6b4299ccd696035976b121799ff`
- `inventory.json` SHA-256: `9d9c36714b8084cf37084fe60279524802a4e21689201b5e4628eea50359a717`

Everclaw has 464 sites from its root repository and six excluded gitlinks. Its
`.gitmodules` file has no mapping for `archive/misc/everclaw`; therefore the
artifact marks Everclaw `incomplete_submodules` and does not claim coverage of
those submodule contents.

These are source regex sites under the registered dialect and file selection,
not security-boundary candidates or a claim about every tracked file. The historical
26,702-row scanner inventories are separate artifacts and were not retroactively
authenticated by this run. No row here implies a trust class, contract, proof
question, or solver result.

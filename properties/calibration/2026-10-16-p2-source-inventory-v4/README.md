# P2 exact-pin source inventory v4

This refresh preserves the POSIX-shell syntax selector emitted by the
registered shell extractor. The prior inventory serialized `pattern`,
`dialect`, and `call_kind` but dropped `shell_flags`; a downstream compiler
therefore defaulted ERE sites such as `grep -E` to BRE. That could model a
different product language while still joining the same source row.

## Contents and limits

- 20,705 extracted sites across the frozen 20-repository cohort.
- 19 repositories are complete under the registered file selection. Everclaw
  remains incomplete because six submodules are unavailable.
- 13,582 POSIX-shell rows now carry their extractor-recorded `shell_flags`.
- Cohort: `2026-09-12-calibration-20-r2`; manifest digest
  `5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d`.
- Inventory-builder fingerprint:
  `f30ed74837cabe95ae4ca2efebe1f88253d424de2b0cd74c6c2b328797b4d6c8`.
- The `sites.ndjson` SHA-256 is
  `491b55d501e0f6a7a62bfea151e513121356332b02f5d3848e34619532ce95dd`.

The Aidevops `pre-dispatch-validator-helper.sh:1881:47` record retains
`{"syntax":"ere","grep_mode":"extended"}` for the exact `grep -oE`
call. Its pattern `detector=[a-z0-9_-]+` compiles as an exact POSIX ERE mirror
when passed through `compile_records` with that metadata.

The inventory remains raw source extraction. It does not mark security
boundaries, adopt contracts, or establish conversion yield. The old v3
artifact remains preserved for earlier checkpoints.

## Reproduction

```sh
.venv/bin/python scripts/freeze-p2-source-inventory.py \
  --manifest properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --checkout-root /tmp/regexproof-pinned-sources \
  --out-dir properties/calibration/2026-10-16-p2-source-inventory-v4
```

The freezer writes available rows before returning nonzero for the known
Everclaw submodule gap. Per-repository hashes and completeness are in
`inventory.json` and `sites.ndjson`.

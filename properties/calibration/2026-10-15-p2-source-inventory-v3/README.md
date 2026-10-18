# P2 exact-pin source inventory v3

This refresh corrects a scanner false positive found during the Magic JS
source review. The v2 scanner parsed the slash in JavaScript hashbang lines
such as `#!/usr/bin/env node` as a regex literal and emitted the pattern
`usr`. The token-aware ECMA scanner now skips a leading BOM/hashbang before
collecting regex literals and dynamic `RegExp` calls.

## Contents and limits

- 20,705 extracted sites across the frozen 20-repository cohort, down from
  20,784 in v2. The 79 removed rows were hashbang directives in Magic JS,
  Gigachad GRC, Everclaw, and Real Router.
- 19 repositories are complete under the registered file selection. Everclaw
  still has six unavailable submodules and remains incomplete.
- Cohort: `2026-09-12-calibration-20-r2`, manifest digest
  `5745d8307a4eeb8483602b2a787b411bac521c6c242755a5f9bb2371c417056d`.
- Extractor fingerprint:
  `7cc4f23f690738bcdb22b5c395e08e876233accdee85df8e8702dfab8e0f8ce3`.
- The `sites.ndjson` SHA-256 is
  `a4e1dfbbd84e2258089d1fd52694ff1e28f6c48cef1caa13fed306e82b1b212f`.
- Magic JS now has 64 inventory rows; the removed eleven entries were its
  TypeScript tool-script hashbangs, not regex literals.

These remain raw extracted sites, not security-boundary candidates. The
inventory records 19 complete repositories; it does not make claims about
excluded dynamic regexes or the unavailable Everclaw submodule contents.

## Reproduction

```sh
.venv/bin/python scripts/freeze-p2-source-inventory.py \
  --manifest properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --checkout-root /tmp/regexproof-pinned-sources \
  --out-dir properties/calibration/2026-10-15-p2-source-inventory-v3
```

The freezer writes available rows before returning nonzero for the known
Everclaw submodule gap. Per-repository file hashes and completeness details
are in `inventory.json` and `sites.ndjson`.

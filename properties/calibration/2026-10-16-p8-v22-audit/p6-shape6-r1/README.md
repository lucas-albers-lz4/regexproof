# P6 Aidevops webhook wave using shape 6

**Wave:** `aidevops-webhook-action-protocol-shape6-r1`
**Cohort:** `2026-09-12-calibration-20-r2`
**Source pin:** `marcusquinn/aidevops@8666b6c6c52472b5535aa295f2df593918152cb1`

## Result

The bounded P6 runner completed the three corrected source-bound contracts
after shape 6 was added to the canonical emitter. The exact checkout and all
three source selectors were verified. The runner's numeric Bash selector check
now binds the extractor's zero-based column to the literal `[[ ... =~
pattern` on that line; it no longer treats a numeric column as a symbol name.

- Three unique proof questions ran and returned UNSAT; solver time was 871.9
  ms in aggregate. These repeat v22 questions and add no new corpus yield.
- All three registered, source-weakened mutation guards ran in the wave and
  reproduced against Bash. The integrated gate also replayed its fourth,
  repository-slug mutation guard.
- The exact-pin gate passed with zero mismatches: 671 Bash/compiler pattern
  comparisons plus 48 integrated helper cases (719 total). The P6 roster
  attributes 395 cases to its three questions; the full gate report includes
  the broader slug checks as well.
- The gate confirms no consumer adoption, security impact, external report,
  maintainer confirmation, or third-party fix.

The first preflight failure remains preserved in the
[scope-correction bundle](../p6-scope-correction/README.md). A dry-run after
shape registration exposed the numeric-column verifier issue; after correcting
that check, dry-run verified the exact source pin and gate coverage before the
wave executed.

## Artifacts

- [Roster](roster.json), [gate configuration](gate-config.json), and
  [measured work items](work-items.json)
- [P6 state](state/state.json), [checkpoint](state/checkpoint.json), and
  [conversion rows](state/conversion.ndjson)
- [Exact-source product gate report](product-gate.json)
- [Cohort run scorecard after this wave](../scorecard-after-shape6.json)

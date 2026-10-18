# Tracecat workspace-sync path-segment contract

**Source:** `TracecatHQ/tracecat@c84d52528a489821f355fc63976fbc7783ae0ad5`
**Tree:** `b4af14482f3483605e41307d54f2b777b63bbd84`
**Source file SHA-256:** `fee3084582517c417c3b8dab6f372b71e423f3c1b413cdec8dbb58663a99cce6`

## Contract

For new unmapped workspace resources, `_SourceIdAssigner` calls
`unique_source_id` or `unique_environment_source_id`. Those helpers call the
pinned `path_segment` normalizer with the fixed production fallbacks
`resource` and `default`. The returned name component is then used to build a
repository-relative workspace-sync source path. Environment-scoped resources
intentionally join two independently normalized components with one slash.

The contract covers only those newly minted component values. Reused source
IDs bypass `path_segment`; export-root enforcement, symlinks, collisions,
Git-provider path behavior, and attacker reachability are outside the scope.
Names come from persisted workspace configuration; no current vulnerability
or security impact is claimed.

## Proof and exact-source gate

The shape-4 per-token image property is UNSAT over the Unicode domain. The
regex replacement maps each non-alphabet run to `-`; the surrounding pinned
helper strips punctuation, caps the value at 96 characters, and returns one
of the fixed safe fallbacks if trimming empties it. The family mutation guard
weakens the regex class to retain `:`, obtains the SAT witness `:`, and
reproduces that output through the exact mutated source.

The bounded P6 runner completed one UNSAT question, one mutation check, and
one exact-source product gate. The gate compared the pinned helper with an
independent run-wise model over 2,469 values, including separators, NUL,
Unicode, line breaks, dot components, and length boundaries. It found zero
mismatches; 2,057 inputs contained `/` or `\`. Path composition of every
tested source result remained beneath the temporary export root.

| Track | Recorded outcome |
|---|---|
| Useful contract-backed proof/gate | 1 UNSAT guarantee; 1 local runnable gate; 1 mutation check; 2,469 differential cases; zero mismatches |
| Bug and impact | No SAT product candidate; no reachable violation, confirmed impact, or fix claimed |
| External outcome | No report or maintainer confirmation; no consumer-adopted gate |
| Throughput | 20.1029 seconds measured P6 phase sum; source-review/contract-authoring duration unknown |
| Resources | Tokens, cost, and human active time unknown |

This is post-v23 retrospective evidence and is included as question 52 in the
additive [v24 checkpoint](../2026-10-16-p2-existing-evidence-20r2-v24/README.md).
The frozen v22 and v23 checkpoints remain unchanged. The separate cohort
scorecard is
[`scorecard-after-tracecat-workspace-sync-path-segment.json`](p6-wave/scorecard-after-tracecat-workspace-sync-path-segment.json).

## Reproduction

The immutable P6 roster, gate config, runner state, checkpoint, and gate report
are under [`p6-wave/`](p6-wave/). The runner command was:

```sh
.venv/bin/python scripts/run-autonomous-proof-wave.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --roster properties/calibration/2026-10-16-autonomous-tracecat-workspace-sync-path-segment/p6-wave/roster.json \
  --state-dir properties/calibration/2026-10-16-autonomous-tracecat-workspace-sync-path-segment/p6-wave/state \
  --wave-id tracecat-workspace-path-segment-20261016 \
  --corpus tracecat_workspace_sync_path_segment \
  --idiom-bucket workspace-sync-path-segment \
  --checkout TracecatHQ/tracecat=/tmp/tracecat-p2-review-20261016 \
  --gate properties/calibration/2026-10-16-autonomous-tracecat-workspace-sync-path-segment/p6-wave/gate-config.json
```

The exact checkout was clean at the pinned commit. The wave used the campaign's
serial, no-solver-retry policy and emitted a v3 checkpoint. The cohort run log
records the measured phase sum and leaves unavailable token, cost, and human
time fields null.

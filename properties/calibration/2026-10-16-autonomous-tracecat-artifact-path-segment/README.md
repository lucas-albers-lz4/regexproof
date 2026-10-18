# Tracecat mount-only artifact path-segment contract

**Source:** `TracecatHQ/tracecat@c84d52528a489821f355fc63976fbc7783ae0ad5`
**Tree:** `b4af14482f3483605e41307d54f2b777b63bbd84`
**Source file SHA-256:** `b9ef06e9fa2582b4c376ab8eb526eef1dc9adeb1c7d2d92e1c8da92ac14a3b11`

## Contract

`MountOnlyArtifactWorkingSetProvider` sanitizes `Artifact.type` and
`Artifact.id` before constructing the artifact directory, and sanitizes a
hydrated filename before writing beneath the per-turn host artifact root. The
contract asks whether each output from `_safe_path_segment` is a nonempty,
single relative component in the ASCII alphabet `A-Za-z0-9_.-`, and therefore
cannot introduce `/`, `\`, `.` or `..` as a path component.

The inputs are persisted workspace artifact/configuration data. Built-in
enterprise hydrators use the fixed filenames `case.json`, `table.json`, and
`agent.json`. This is a preventive helper guarantee; it does not establish
attacker reachability or a current security impact. Symlink ancestry,
`host_root` provenance, races, and name collisions are outside the contract.

## Proof and exact-source gate

The shape-4 per-token image property is UNSAT over Python strings with the
Unicode domain declared. The family mutation guard admits `/`, produces the
SAT witness `/`, and replays the weakened source to show that
`../../outside` can escape the artifact root after path composition. That
mutation demonstrates sensitivity; it is not a finding against the pinned
source.

The bounded P6 runner completed one UNSAT question, one mutation check, and
one exact-source product gate. The gate compared the pinned helper with an
independent run-wise transformation over 2,467 inputs, including Unicode,
NUL, line breaks, long strings, and separator-containing paths. It found zero
mismatches; 2,057 inputs contained `/` or `\`. The gate also rechecked that
the weakened slash rule escapes the root.

| Track | Recorded outcome |
|---|---|
| Useful contract-backed proof/gate | 1 UNSAT guarantee; 1 local runnable gate; 1 mutation check; 2,467 differential cases; zero mismatches |
| Bug and impact | No SAT product candidate; no reachable violation, confirmed impact, or fix claimed |
| External outcome | No report or maintainer confirmation; no consumer-adopted gate |
| Throughput | 9.3449 seconds measured P6 phase sum; source-review/contract-authoring duration unknown |
| Resources | Tokens, cost, and human active time unknown |

The run is post-v22 retrospective evidence and is included as question 51 in
the additive [v23 checkpoint](../2026-10-16-p2-existing-evidence-20r2-v23/README.md).
The frozen v22 checkpoint remains unchanged. The separate cohort scorecard is
[`scorecard-after-tracecat-artifact-path-segment.json`](p6-wave/scorecard-after-tracecat-artifact-path-segment.json).

## Reproduction

The immutable P6 roster, gate config, runner state, checkpoint, and gate report
are under [`p6-wave/`](p6-wave/). The runner command was:

```sh
.venv/bin/python scripts/run-autonomous-proof-wave.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --roster properties/calibration/2026-10-16-autonomous-tracecat-artifact-path-segment/p6-wave/roster.json \
  --state-dir properties/calibration/2026-10-16-autonomous-tracecat-artifact-path-segment/p6-wave/state \
  --wave-id tracecat-artifact-segment-20261016 \
  --corpus tracecat_artifact_path_segment \
  --idiom-bucket artifact-path-segment \
  --checkout TracecatHQ/tracecat=/tmp/tracecat-p2-review-20261016 \
  --gate properties/calibration/2026-10-16-autonomous-tracecat-artifact-path-segment/p6-wave/gate-config.json
```

The exact checkout was clean at the pinned commit. The wave ran with the
campaign's serial, no-solver-retry policy and emitted a v3 checkpoint. The
cohort run ledger records the phase sum and leaves unavailable token, cost,
and human-time fields null.

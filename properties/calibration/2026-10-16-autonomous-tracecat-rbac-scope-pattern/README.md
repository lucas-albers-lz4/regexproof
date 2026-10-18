# Tracecat RBAC scope-pattern contract

**Source:** `TracecatHQ/tracecat@c84d52528a489821f355fc63976fbc7783ae0ad5`
**Tree:** `b4af14482f3483605e41307d54f2b777b63bbd84`
**Inventory identity:** `0beaf519936fc85fed0927ff3f35c617`
**Source file SHA-256:** `a63e61a139aeb35665b43f2a000095b42e8c6050778144f7c9f28af5c58ed32b`

## Contract

The EE `POST /rbac/scopes` route takes `ScopeCreate.name`, requires
`org:rbac:create`, and calls `RBACService.create_scope`. The request model
constrains the name to 1–255 characters and the allowlist
`^[a-z0-9:_.*-]+$`; the service repeats the same character check before
splitting at the final colon and persisting the custom scope. Assigned scope
names later flow through `scope_matches`; wildcard grants containing `*` use
Python `fnmatch`.

The contract covers newly submitted names through that pinned API path. It
excludes pre-existing database scopes, direct internal calls that bypass the
request model, role assignment policy, and broader authorization correctness.
The input is organization RBAC configuration submitted by an authorized
administrator. No remote attacker or current security impact is claimed.

## Proof and exact-source gate

The shape-1 alphabet property is UNSAT for `?`, `[` and `]` in the accepted
scope alphabet. The family mutation adds `?` to both the exact request-schema
and service patterns. It is SAT for
`action:tools?okta.*:execute`; ground truth replays the weakened Pydantic model,
the weakened service validator, the final-colon parse, and the pinned
`scope_matches` implementation matching
`action:toolsXokta.list_users:execute`.

The P6 wave completed one UNSAT question, one grounded mutation check, and an
exact-source replay over 2,632 deterministic inputs with zero mismatches. It
used Pydantic 2.12.5, matching the Tracecat lockfile. The source gate extracts
and executes the pinned `ScopeCreate` class and the exact validator/matcher
functions from the clean pinned checkout.

The source review also found a helper-level semantic difference: Python's
`$`-anchored `validate_scope_string` accepts a final line feed, while the
Pydantic request schema rejects it. The exact route rejects that value before
the helper, and the gate records the distinction. This is not a current HTTP
acceptance, bug-impact, or security finding.

| Track | Recorded outcome |
|---|---|
| Useful contract-backed proof/gate | 1 UNSAT guarantee; 1 local runnable gate; 1 mutation check; 2,632 differential cases; zero mismatches |
| Bug and impact | No current over-accept through the pinned route; no SAT product candidate, reachable violation, impact, or fix claimed |
| External outcome | No report or maintainer confirmation; no consumer-adopted gate |
| Throughput | 1.8441 seconds measured P6 phase sum; source-review and contract-authoring time unknown |
| Resources | Tokens, cost, and human active time unknown |

This is post-v24 retrospective evidence and is included as question 53 in the
additive [v25 checkpoint](../2026-10-16-p2-existing-evidence-20r2-v25/README.md).
The frozen v22 and prior additive v23/v24 checkpoints remain unchanged. The
cohort scorecard snapshot is
[`scorecard-after-tracecat-rbac-scope-pattern.json`](p6-wave/scorecard-after-tracecat-rbac-scope-pattern.json).

## Reproduction

The immutable P6 roster, gate config, runner state, checkpoint, and gate report
are under [`p6-wave/`](p6-wave/). The runner command was:

```sh
.venv/bin/python scripts/run-autonomous-proof-wave.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --roster properties/calibration/2026-10-16-autonomous-tracecat-rbac-scope-pattern/p6-wave/roster.json \
  --state-dir properties/calibration/2026-10-16-autonomous-tracecat-rbac-scope-pattern/p6-wave/state \
  --wave-id tracecat-rbac-scope-pattern-20261016 \
  --corpus tracecat_rbac_scope_pattern \
  --idiom-bucket rbac-scope-wildcard-allowlist \
  --checkout TracecatHQ/tracecat=/tmp/tracecat-p2-review-20261016 \
  --gate properties/calibration/2026-10-16-autonomous-tracecat-rbac-scope-pattern/p6-wave/gate-config.json
```

The proof CI job now installs Pydantic 2.12.5 for this source-engine replay and
runs the gate at the pinned Tracecat commit. Hosted CI has not yet been
observed. The autonomous work log records the measured phase sum and leaves
tokens, cost, and human time unknown.

# Tracecat origin-slug contract calibration

**Source:** `TracecatHQ/tracecat@c84d52528a489821f355fc63976fbc7783ae0ad5`,
which is already a member of the frozen `2026-09-12-calibration-20-r2`
cohort. **Status:** contract adopted under `autonomous-contracts-v1`; the
proof and product regression gate passed on 2026-10-15. It remains a focused
calibration, not a registered conversion wave or campaign observation.

Tracecat's current `properties/generated/tracecat_gate_decision.json` is
`triage-trial`, while the new-bucket registration command requires a current
`go` decision. This slice is therefore a harness/CI calibration and is not
registered or counted as a conversion wave. Promote it only through the
documented admission decision and P4 registration path.

## Contract and source path

The adopted site is the first substitution in
`tracecat/registry/artifact_keys.py::_slugify_origin`:
`[^a-zA-Z0-9_-]` becomes `_`. Repository origins enter through
`RegistryRepositoryCreate.origin` (1–255 characters, normally `git+ssh://` or
one of two built-in values) and `RegistryRepositoryUpdate.origin` (1–255
characters). Registry sync passes the origin to
`get_artifact_s3_key`; the sync runner uses that key for the S3 upload.

The guarantee is local and concrete: every origin-derived character in this
S3 key component is ASCII alphanumeric, `_`, or `-`. The theorem is a
length-independent per-character image proof. The helper then collapses and
strips underscores and caps the final component at 100 characters. The gate
checks those composed behaviors and verifies the origin does not add `/`
components to the expected key layout.

This is a useful regression contract, not a claim that the current product has
a bug. The mutation guard allows `/` through the preserved alphabet and
replays the weakened pinned helper to show the resulting key structure would
break. The gate also differentially checks the exact source regex and compares
the composed helper against an independent character-wise reference over
bounded exhaustive and seeded cases.

## Reproduction

Run the gate against a clean checkout at the adopted pin:

```sh
TRACECAT_REPLAY_SOURCE=/path/to/tracecat-at-c84d52528a489821f355fc63976fbc7783ae0ad5 \
  .venv/bin/python scripts/tracecat-origin-slug-regression-gate.py
```

The `proof` job in `.github/workflows/ci.yml` runs the same gate on pushes and
pull requests.

The gate requires the pinned source digest, Z3 5.0.0, contract/domain
eligibility, a real mutation replay, source-pattern differential fuzz, and
full-helper/key-layout differential cases.

## Recorded gate result (2026-10-15)

Command:

```sh
TRACECAT_REPLAY_SOURCE=/tmp/regexproof-pinned-sources/tracecat-c84d52528a489821f355fc63976fbc7783ae0ad5 \
  .venv/bin/python scripts/tracecat-origin-slug-regression-gate.py
```

Exit status was 0. Z3 reported the adopted image property UNSAT and the slash
mutation SAT with witness `/`; the ground-truth callback reproduced the unsafe
S3-key path split in the pinned helper. Source-pattern differential fuzz checked
22 inputs with 0 mismatches (seed 42). The composed helper/key-layout reference
checked 2,472 origins with 0 mismatches. Runtime versions were Python 3.14.8,
Z3 5.0.0, and Node 26.11.1. The checkout was clean at the adopted pin and its
source digest matched the contract.

The gate execution was recorded as
`tracecat-origin-gate-20261015-r1` in
[`properties/generated/autonomous_work.jsonl`](../../generated/autonomous_work.jsonl):
2.915 elapsed seconds; token usage and dollar cost unavailable; human active
time unavailable; no human intervention. The scorecard reports 1 attempted,
decided UNSAT guarantee, 1 local gate, 1 mutation check, and 2,494 differential
cases. It reports 0 SAT candidates, reachable violations, security-impact
confirmations, reports sent, maintainer confirmations, or fixes. This is one
focused gate run, not a full conversion-wave throughput rate.

The first run exposed that the shared registration gate applied full-string
anchor requirements to a `re.sub` character class. Registration now uses the
declared `call_kind`: substitution patterns still pass parser and unsupported
escape checks, while validator-only anchor checks do not apply. The focused
registration suite passed 15 tests after this change.

This result supports a useful local regression gate, not a current product bug.
Tracecat remains `triage-trial`; it is not admitted to a conversion bucket and
does not count as a P4 wave or P7 campaign yield.

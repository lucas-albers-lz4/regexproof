# Real-Router route-segment alphabet contract

## Review scope

This is a targeted P2 review of one ECMA inventory row at the frozen Real-Router
pin `55aa7ef43a9c129beba90823cd8a4db10bb01211`. It is not a review of all
2,840 inventory rows at that pin.

The pinned `constants.ts` comment defines `\\w` as ASCII letters, digits, and
underscore; the pattern adds dot and hyphen. `segmentTesters.ts` applies the
shared validation to `startsWithSegment`, `endsWithSegment`, and
`includesSegment`, and `INVARIANTS.md` independently declares the same
character partition and 10,000-character limit. The input is library/API route
configuration. The Real-Router admission decision was based on corpus scale;
this evidence does not call the repository a security tool and makes no claim
of remote attacker reachability or security impact.

The adopted contract is [`contract.json`](contract.json); the source review is
[`review.json`](review.json). The P2 join adds one exact-pin question and one
targeted reviewed site, not a prospective sample.

## Proof and exact-source gate

The formal shape-1 query is UNSAT: every one-character ASCII match of the
pinned `^[\\w.-]+$` expression is in `[A-Za-z0-9_.-]`. This alphabet-level
proof is length-independent. A source-mutated pattern that also allows `/`
produces SAT, and the witness replays through all three exact helper
functions: the original source throws `TypeError`, while the weakened source
accepts it.

The local Node.js 26.11.1 gate executes the pinned TypeScript helper body with
native type stripping; the only adaptation is changing its relative constants
import to the temporary `.mts` filename. It compared 17,027 inputs against an
independent model for each helper (51,081 helper comparisons total) with zero
mismatches. Cases include every ASCII code point, every two-character ASCII
string, 512 seeded mixed strings, Unicode and control examples, and lengths
10,000 and 10,001. The CI job repeats this exact-pin gate on Node 22. Its
hosted result has not yet been observed.

The P6 proof-wave runner recorded one decided UNSAT question, one passing
mutation check, one local gate, and a 1.6433-second phase sum. Source review
and contract authoring were not timed; token use, cost, and human active time
are unknown. No product SAT candidate, reachable violation, security impact,
consumer adoption, external report, maintainer confirmation, or fix was
established.

Reproduce the proof and pinned-source gate from the repository root:

```sh
.venv/bin/python scripts/z3-verify.py \
  RR-route-segment-allowed-alphabet \
  RR-route-segment-slash-allowlist-mutation \
  --require-ground-truth --json

.venv/bin/python scripts/real-router-segment-regression-gate.py \
  --source-root /tmp/regexproof-pinned-sources/real-router-55aa7ef43a9c129beba90823cd8a4db10bb01211 \
  --output properties/calibration/2026-10-16-p2-real-router-segment/p6-wave/product-gate.json
```

The frozen roster, gate configuration/report, runner state, and checkpoint
are under [`p6-wave/`](p6-wave/). The retrospective P2 aggregate is
[`20-r2 v16`](../2026-10-16-p2-existing-evidence-20r2-v16/README.md).

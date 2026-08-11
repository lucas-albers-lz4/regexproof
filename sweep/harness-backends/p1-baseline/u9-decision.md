# U9 decision — evaluated per the pre-committed criterion (design #213 rev 5, reopened-able per rev 6)

## The pre-committed flip criterion (rev 5)
**DROP the ECMA branch if: (a) ALL fwlive classifier patterns have proof-capable
mirror/standard routes, AND (b) NO consumer needs ECMA-as-written output.** Any
new fwlive pattern lacking a standard-encoding mirror AUTO-REOPENS this decision
(rev 6 reopen trigger).

## Evidence per condition (all measured 2026-08-11, pinned v1.6.1)

### Condition (a): all six patterns have proof-capable mirror routes — **MET**
Per-pattern evidence (all measured 2026-08-11, pinned v1.6.1):

| Pattern | Exactness basis | Level |
|---|---|---|
| NETFILTER_KV_GLUE | S12 by-construction (constant-width positive lookahead elimination) + **E2M theorem UNSAT** within the declared ASCII domain (blocker probe #224) + 937-string corpus | theorem + regression |
| NON_FIREWALL_PREFIX, FIREWALL_HINT, ACTION_RE, DENY_ACTION, TCP_FLAG_TAIL | boundary-exact encodings (pilot #223) + **0 divergences on the 937-string corpus each** (real JS vs mirror) | regression parity (no solver-level theorem — the corpus is the evidence) |

The 5,622-comparison pilot corpus establishes regression parity on every decided
string; the E2M theorem covers the lookahead pattern specifically. M2E is
regression-only for all six (Noodler SIGABRTs on negated `from_ecma2020`).
Boundary set 13/13 matching real JS; cvc5 agrees on every mirror formula it
parses (blocker probe #224).

### Condition (b): no consumer needs ECMA-as-written output — **MET (with the
trigger as the safety net)**
- The fwlive #120 scan classifies with the six patterns — all six are
  mirror-expressible (per-pattern evidence above); no CURRENT consumer requires
  the solver to parse the pattern AS WRITTEN. This includes the design's P7
  fwlive handoff (its intended consumer): all six handoff patterns are
  mirror-expressible, so the handoff proceeds on mirrors.
- The as-written route's residual values (diagnostic fidelity for unmirrorable
  future patterns) are exactly what the reopen trigger guards: any new pattern
  without a mirror reopens U9 before the route is needed.

### Supporting findings that strengthen the DROP (all measured)
- `from_ecma2020` **silently literalizes `\p{}`** (identity escape, never an
  error — the \p gate table, #226 merged) and **aborts on negated membership**
  (rc=-6) — the route has two hazards the mirror lacks.
- The ECMA route abstains on exact-boundary anchored forms (163/5,622, all
  `unknown/rc=0` — honest, but the mirror decides every one of them).
- No flag representation in `from_ecma2020` (i/u/g flags exist only in the
  as-written source; the route cannot honor them).

## Decision: **DROP the from_ecma2020 branch from the harness scope**

The harness will NOT ship a `from_ecma2020` runner. Noodler escalation is scoped
to the standard-encoding mirror route (proof-capable, cross-checkable). The
as-written diagnostic stays available as a REPO-LEVEL probe tool (the pilot
scripts remain in sweep/harness-backends as the equivalence evidence), but it is
not part of the harness result path.

**Phase-2 scope change (concrete):** no `dialect="ecma"` registry field, no
`from_ecma2020` invocation in the runner, no ECMA-leg tier ceiling logic. The
`route:"mirror"`-required assertion (S3) simplifies to "every harness result is
mirror-route" — the cross-checked ceiling applies without an exception class.
The U9 flip criterion's counterpart (R9 KEEP-branch value — as-written
diagnostics) is superseded: the mirror's exactness evidence (this P1 package)
makes the as-written route redundant for the current consumer set.

## Reopen trigger (stays active, rev 6)
ANY new fwlive classifier pattern that cannot be expressed as a standard-encoding
mirror AUTO-REOPENS U9 — the decision is re-evaluated with the new pattern as the
consumer case, before any harness work proceeds. Also re-evaluated if the fwlive
scan explicitly requests as-written audit output (a consumer-need change).

## Consequence summary for the wave
- **#218 Phase 2 scope shrinks**: no `dialect="ecma"` registry field, no
  `from_ecma2020` invocation in the runner, no ECMA-leg tier ceiling logic; the
  S3 authority assertion simplifies to "every harness result is mirror-route".
  The #213 canonical body's ECMA registry fields and S3 ECMA-authority wording
  are marked **superseded for the current scope** by this decision (a #213
  amendment note accompanies this PR's merge); #218's body drops its ECMA items.
- **#219 cross-check simplifies**: mirror formulas only (no ECMA-leg ceiling
  class).
- **D14 / P5 differential fuzz is UNAFFECTED**: the fuzz compares real JS vs the
  translated mirror — a mirror-only world keeps that comparison intact (it is
  the mirror's regression evidence, now the sole exactness evidence for five of
  six patterns).
- **P7 fwlive handoff (#221)**: proceeds on mirrors for all six patterns — the
  handoff artifact is the mirror encoding table + the per-pattern equivalence
  evidence package (pilot + blocker probe + \p gate), not an as-written runner.
- The equivalence evidence package is the permanent justification, committed
  under p1-baseline/.

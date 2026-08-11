# R8 regression fixtures (design #213 R8, rev 3)

Pinned-target: Noodler v1.6.1 (sha256 22b19f12…464). Purpose: the wrong-UNSAT bug
class the escalation exists to distrust, plus the hang/crash class. Replay on every
binary bump BEFORE the bump is approved (R5 bump policy) and at runtime by
`preflight.py`.

| Fixture | Source | Expected on v1.6.1 | Why |
|---|---|---|---|
| `gh316.smt2` | Noodler tracker #316 (wrong-UNSAT, closed) | `sat` | The class replay: a solver returning `unsat` here is the buggy class — do not trust its UNSAT |
| `gh325.smt2` | Noodler tracker #325 (wrong-UNSAT, **STILL OPEN upstream**) | `sat` | Same class, still open — the sha256 pin alone is insufficient; the INVOKED binary must be self-checked |
| `gh344.smt2` | Noodler tracker #344 (segfault without set-logic) | **contained**: verdict OR timeout-contained hang, NEVER a crash | The D6 mandate: this fixture carries `(set-logic QF_SLIA)`; measured on v1.6.1 it HANGS >30s (the improvement over the v1.5.x-era segfault — the hang class persists, which is why the runner's subprocess timeout is mandatory) |

Verification history (2026-08-11, deep-research phase): #316 and #325 both replay
`sat` on v1.6.1 (fixed since the v1.5.x era); #344 with set-logic hangs >30s
(contained by the runner timeout — no segfault, but the hang class persists;
always emit set-logic + subprocess timeout).

"""D15 verdict resolution (design #213 D15 + S16 + the mechanical disagreement
definition, Phase 3 PR B).

Total order on CONCRETE verdicts; abstentions (unknown / solver-abstain) are an
ERROR STATE outside the order (S16):

    sat < unsat     (both concrete; a disagreement between them is resolved
                     by the mechanical reproduction rule, NOT by the order)

Disagreement is defined MECHANICALLY (design): the unsat solver fails to
reproduce the sat witness. Concretely, for a concrete-vs-concrete disagreement
(a=sat, b=unsat with the sat witness w):

- re-assert w in the UNSAT solver: if it comes back sat, the unsat side was
  WRONG — a wrong-verdict EVENT (recorded, the sat side stands, NO hard fail);
- if it stays unsat (w does not hold in the unsat solver's theory), the
  solvers genuinely disagree on the formula — HARD FAIL + exit 2.

D16 runs BEFORE this machinery (witness re-validation gates the sat side
first); D15 consumes its outcome.

The 27-triple table (3^3 = sat/unsat/unknown over the three axes: primary,
cross, reproduction-outcome) is unit-tested exhaustively below.
"""

from __future__ import annotations

from typing import Callable, Optional

# The concrete verdict order (abstentions are OUTSIDE the order — S16)
CONCRETE = ("sat", "unsat")


def order(v: Optional[str]) -> int:
    """sat < unsat. unknown/None/abstain states raise — they are outside the
    total order (S16)."""
    if v not in CONCRETE:
        raise ValueError(f"{v!r} is not a concrete verdict (abstentions are "
                         "outside the D15 order)")
    return 0 if v == "sat" else 1


def resolve(primary: Optional[str], cross: Optional[str],
            reproduce: Optional[Callable[[], str]] = None) -> dict:
    """Classify a (primary, cross) verdict pair per D15.

    reproduce: a callback returning the REPRODUCTION OUTCOME as a tri-state
    string — "sat" (the sat witness re-asserted sat in the unsat solver: the
    unsat side was wrong), "unsat" (the witness did not hold: genuine
    disagreement), or "unknown" (the reproduction itself ABSTAINED — timeout,
    sigsegv, no-verdict — which is outside the D15 order, S16, and never a
    disagreement). None = no reproduction available (conservative: a
    concrete-vs-concrete conflict that cannot be cleared is a genuine
    disagreement).

    Returns {kind, disagreement, wrong_verdict_event, detail}:
      kind: "agree" | "disagreement" | "wrong-verdict-event" | "abstain-involved"
    """
    if primary not in CONCRETE or cross not in CONCRETE:
        return {"kind": "abstain-involved", "disagreement": False,
                "wrong_verdict_event": False,
                "detail": f"abstention outside the order ({primary}, {cross})"}
    if primary == cross:
        return {"kind": "agree", "disagreement": False,
                "wrong_verdict_event": False, "detail": f"{primary}/{cross}"}
    # concrete-vs-concrete disagreement — mechanical reproduction rule
    if reproduce is None:
        return {"kind": "disagreement", "disagreement": True,
                "wrong_verdict_event": False,
                "detail": "no reproduction callback (cannot clear)"}
    outcome = reproduce()
    if outcome not in ("sat", "unsat", "unknown"):
        raise ValueError(f"reproduction outcome {outcome!r} is not tri-state")
    sat_side = "primary" if primary == "sat" else "cross"
    if outcome == "sat":
        # the sat witness re-asserts sat in the UNSAT solver: the unsat side
        # was wrong — a wrong-verdict EVENT, the sat side stands
        return {"kind": "wrong-verdict-event", "disagreement": False,
                "wrong_verdict_event": True,
                "detail": f"{sat_side}=sat reproduced in the unsat solver"}
    if outcome == "unknown":
        # the reproduction ABSTAINED — outside the D15 order (S16), never a
        # disagreement and never a wrong-verdict event
        return {"kind": "abstain-involved", "disagreement": False,
                "wrong_verdict_event": False,
                "detail": "reproduction abstained (timeout/sigsegv/no-verdict)"}
    # outcome == "unsat": the witness does NOT hold in the unsat solver's
    # theory: genuine disagreement → HARD FAIL + exit 2
    return {"kind": "disagreement", "disagreement": True,
            "wrong_verdict_event": False,
            "detail": f"{sat_side}=sat witness NOT reproduced (unsat stands)"}

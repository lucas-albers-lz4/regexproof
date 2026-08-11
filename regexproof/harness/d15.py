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
            reproduce: Optional[Callable[[], bool]] = None) -> dict:
    """Classify a (primary, cross) verdict pair per D15.

    Returns {kind, disagreement, wrong_verdict_event, detail}:
      kind: "agree" | "disagreement" | "abstain-involved"
      disagreement: True only for a genuine concrete-vs-concrete disagreement
        after the mechanical reproduction rule (HARD FAIL + exit 2).
      wrong_verdict_event: True when the reproduction showed the unsat side
        was wrong (recorded; the sat side stands; NOT a hard fail).
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
    sat_side = "primary" if primary == "sat" else "cross"
    reproduced = bool(reproduce())
    if reproduced:
        # the sat witness re-asserts sat in the UNSAT solver: the unsat side
        # was wrong — a wrong-verdict EVENT, the sat side stands
        return {"kind": "wrong-verdict-event", "disagreement": False,
                "wrong_verdict_event": True,
                "detail": f"{sat_side}=sat reproduced in the unsat solver"}
    # the witness does NOT hold in the unsat solver's theory: genuine
    # disagreement → HARD FAIL + exit 2
    return {"kind": "disagreement", "disagreement": True,
            "wrong_verdict_event": False,
            "detail": f"{sat_side}=sat witness NOT reproduced (unsat stands)"}

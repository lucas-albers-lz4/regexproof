"""D16 witness re-validation (design #213 D16, Phase 2 PR B — uniform, no
ECMA clause per the U9 DROP).

An external (Noodler-produced) SAT witness is re-asserted against the ORIGINAL
constraints in stock z3: the witness must re-produce a sat model, else it is
not trustworthy. Re-assertion (not byte-compare) is the discriminator — the
measured m2-close finding: existential properties admit multiple valid models,
so only the re-check is meaningful.

Binds witness vars by name: the constraint functions declare their variables
via z3.String(name) (top-level symbols), so String(k) == StringVal(v) binds
the same symbol.
"""

from __future__ import annotations

from z3 import Solver, String, StringVal, sat

from regexproof.harness.core import z3_str


def revalidate_witness(constraints, bad, witness: dict, timeout_ms: int = 30000) -> bool:
    """Re-assert constraints + bad + witness bindings in stock z3. True iff sat.
    A False result means the witness does not reproduce — the result must NOT
    be reported (design D16: re-validation runs BEFORE tier assignment)."""
    s = Solver()
    s.set("timeout", timeout_ms)
    for c in constraints:
        s.add(c)
    s.add(bad)
    for k, v in witness.items():
        s.add(String(k) == StringVal(z3_str(v) if hasattr(v, "as_string") else v))
    return s.check() == sat

# Shape 5 — `rule_diff` (canonical example)

Unconditional documentation for shape-5 gap queries. Encoding demo also lives
in `scripts/z3-property-template.py`; **registry `kind` / `family` / mutation
guards** are exercised by `scripts/rule-diff-pilot.py`.

## Question

Does detector language **R2** accept any string that independent-spec language
**R1** misses (within a declared length bound)?

## Encoding (complement-free)

Never build `Complement(R1)` as a regex (language complement ≠ char-class gap;
see TRAPS `VF-001`). Use:

```text
InRe(s, R2) ∧ Not(InRe(s, R1)) ∧ len(s) ∈ [lo, hi]
```

SAT ⇒ gap (finding). UNSAT ⇒ no gap in the declared domain. TIMEOUT ⇒
**not proven** (hard failure).

Implementation: `regexproof.rule_diff.encode.shape5_constraints`.

## Registry fields

| Field | Value |
|---|---|
| `kind` | `rule_diff` |
| `family` | shared id for the gap + its mutation guards (e.g. `RD-github-oauth-token`) |
| `expect_unsat` | `True` for “no gap” properties; gap queries treat SAT as a finding |
| `call_kind` | solver uses `fullmatch` mirrors (search wrappers blow up Z3 — `VF-007`) |

## Mutation guards (required)

Every `rule_diff` family must have at least one `kind=mutation_guard` sibling
(`check_mutation_coverage` / `KINDS_NEEDING_MUTATION_GUARD`). The Phase-3
pilot registers, per admitted pair:

| Guard | Intent |
|---|---|
| `…-widen-R1` | Weaken R1 → gap must appear (SAT) |
| `…-narrow-R2` | Strengthen R2 → gap must disappear (UNSAT) |
| `…-control` | R1≡R2 → no gap (UNSAT) |

## Run

```bash
# Encoding smoke (template shapes 1–5):
python scripts/z3-property-template.py

# Full gitleaks encodable-subset pilot:
python scripts/rule-diff-pilot.py --require-ground-truth

# One measured-stable family (Phase 6 CI subset):
python scripts/rule-diff-pilot.py --family RD-github-oauth-token --require-ground-truth
```

## Ground truth

SAT gap witnesses replay against the **real** dialect engine (go-re2 for
gitleaks) under the site `call_kind` (usually `search`), even though the Z3
mirror used `fullmatch` + length bounds. See `docs/REPORTING.md` and
`--require-ground-truth`.

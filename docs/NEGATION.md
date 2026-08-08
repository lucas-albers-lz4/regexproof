# ModSecurity negation policy (fix-wave #72)

ModSecurity extracts `negated=True` for `!@rx` operators and variable-selector
regexes (`selector=True`). Stock Z3 `Complement()` is **language** complement
(TRAPS #1), not a safe encoding of rule negation — so this wave **rejects**
negated records before compile/triage with reason `negated-unsupported`.

Machine source of truth: [`regexproof/batch/negation_policy.py`](../regexproof/batch/negation_policy.py).

## Per-dialect decision table

| Dialect | Policy | Reason string |
|---|---|---|
| `py_re` | reject-unsupported | `negated-unsupported` |
| `ecma` | reject-unsupported | `negated-unsupported` |
| `re2` | reject-unsupported | `negated-unsupported` |
| `pcre` | reject-unsupported | `negated-unsupported` |

True complement encoding (if ever sound per dialect) is a follow-up — never
silent drop of the `negated` bit.

## CRS surface (coreruleset v4.28.0)

| Class | Count |
|---|---|
| `!@rx` (negated operator) | 21 |
| Variable selectors (`selector=True`, all negated) | 28 |
| Total negated regex-bearing records | 49 |
| Total `@rx` sites (positive + negated) | 318 |

After the gate, all 49 carry `compile_reason=negated-unsupported` and triage
`reason_kind=unencodable` with `negated=true` on the triage row.

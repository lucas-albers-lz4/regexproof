# P3 validate — trailing-alt `$` A1B remeasure (#83)

Post-P2 (#89) remeasure of every frozen `*-inventory.ndjson` through
`scripts/remeasure-from-inventory.py`, then
`scripts/build-cross-corpus-matrix.py`.

Compiler fingerprint: see each `*_encodable_fraction.json`
(`compiler_fingerprint`).

## Fraction delta (prior artifact → P3)

Prior = post–fix-wave / pre-A1B committed artifact (PR #80 era), except
gitleaks which already reflected A1B in #89.

| Corpus | Before | After | Δ | `per-alternative-anchor` |
|---|---:|---:|---:|---:|
| gitleaks | 0.8190 | 0.8190 | 0 | 1 → 1 |
| ids_rules | 0.8467 | **0.8519** | +0.0052 | 278 → **235** |
| coreruleset | 0.6908 | 0.6908 | 0 | 9 → 9 |
| trufflehog | 0.9302 | 0.9302 | 0 | 1 → 1 |
| semgrep_rules | 0.2741 | **0.2842** | +0.0101 | (see reasons; +93 now-encodable) |
| cpython_re | 0.5556 | 0.5556 | 0 | — |
| busybox / pcre2 / re2 testdata | 1.0 | 1.0 | 0 | — |

## AC-P3

| Gate | Target | Measured | Result |
|---|---|---|---|
| gitleaks | ≥ 0.70 | 0.8190 | **pass** |
| ids_rules | ≥ 0.87 | 0.8519 | **miss** (doc gap) |
| coreruleset | ≥ 0.71 | 0.6908 | **miss** (doc gap) |

Accept class **not** widened in this phase.

## Residual `per-alternative-anchor` buckets (A1B accept-class boundary)

Classified by `split_trailing_dollar` on frozen-inventory recompile rejects.

### ids_rules (paa = 235)

| Bucket | Count | Notes |
|---|---:|---|
| `caret_in_x_out_of_a1b` | 164 | Pattern-final `(?:…|$)` but `^` in X — rejected by design (same as `^0+(?:&|$)` P2 control) |
| `paa_without_\|$_surface` | 70 | Mid-pattern anchors, e.g. `(?:^|&|Content-Disposition…)` — not trailing `|$)` |
| `capturing_or_bare_alt_dollar` | 1 | `(&|$)` — not non-capturing `(?:…|$)` |

Even encoding all 235 paa rows would reach ~0.8807; encoding only the
non-caret residuals (+71) yields ~0.8606 — still below 0.87. Closing AC-P3
for ids needs a follow-up toolkit shape (caret-branch / mid-pattern), not
silent expansion of A1B.

Examples (caret-in-X): `^0+(?:&|$)`, `^[a-f0-9]{64}(?:&|$)`, `^(?:\x3b|$)`.

### coreruleset (paa = 9)

| Bucket | Count | Notes |
|---|---:|---|
| `paa_without_\|$_surface` | 8 | Mid-pattern `^`/`$` alts; not pattern-final `(?:…|$)` |
| `mid_or_suffix_after_group` | 1 | `|$)` inside a larger alternation: `<?(?:php…|$)|\[[/\…]?php\]…` |

Need 246/346 (≥0.71); have 239. The 9 paa rows are outside A1B; gap is a
follow-up, not an A1B bug.

### gitleaks (paa = 1)

Residual is caret-branch / boundary shape
`(?:^|[…])(…)(?:$|[…])` — not pattern-final `(?:…|$)`. Out of scope for A1B
(locked in #89).

## Leftover classification

| Class | Meaning |
|---|---|
| (a) fixed | ids +43 paa recovered vs pre-A1B artifact; semgrep +93 encodable |
| (b) engine / out-of-scope | caret-in-X, mid-pattern `$`/`^`, capturing `(|$)`, gitleaks residual |
| (c) pending policy | none in this phase — follow-ups for caret-branch / mid-pattern shapes |

## Gates run

- Full `pytest` (CI) + local trailing-alt suite / mutation guards
- Differential membership fuzz on encoded toys (`tests/test_trailing_alt_dollar.py`,
  ≥15s membership timeout)
- No false-UNSAT expansion: reject controls (`^0+(?:&|$)`, mid-pattern `$`)
  remain rejected

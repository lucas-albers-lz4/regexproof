# Caret-in-X remeasure delta (#103)

## AC-P3

| Corpus | Prior | Now | Target | Result |
|---|---:|---:|---:|---|
| ids_rules | 0.8519 | **0.8717** (7123/8171) | ≥0.87 | **pass** |
| coreruleset | 0.6908 | **0.6908** (239/346) | ≥0.71 | **miss (residual)** |

ids `per-alternative-anchor`: 235 → 72.
CRS `per-alternative-anchor`: 9 → 9 (unchanged).

## CRS residual (honest)

The 9 CRS paa rows are mid-pattern / leading `(?:^|…)` / `$`-first shapes —
**not** caret-in-X. Left as permanent class-(b) out-of-scope for this issue;
AC-P3 for CRS remains aspirational pending a mid-pattern toolkit shape.

## A1B

Accept class unchanged. Caret-in-X is a separate dispatcher path
(`ascii;caret_in_x`).

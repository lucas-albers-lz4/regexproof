# Phase 2 (#54) toolkit-fix acceptance closeout

Vehicle: #45 (lazy strip, hex, negated-class, scoped `(?i:)`, ECMA rejects, TRAPS #21 pattern-too-long).

| Fix | Golden | Mutation guard | Diff-fuzz / note |
|---|---|---|---|
| Lazy quantifier strip | `tests/test_pcre_strip.py`, wave gates | `P1-mutated-star` family | language-transparent; fuzz via mirror-fidelity gate |
| Hex `\xNN` / `\x{}` soundness | `test_hex_escape_soundness_codepoint_not_literal_text` | TRAPS #23 | codepoint accept / literal reject |
| Negated class | golden suite | covered in template shapes | — |
| Scoped `(?i:...)` | golden + `test_ecma_rejects_scoped_i` | — | `(?-i:)` stays honest reject |
| Pattern-too-long | TRAPS #21 decision recorded | n/a | no raise without measured need |

## Phase-1-driven backlog (from buckets)

| Reason | Surface (Phase 1) | Action |
|---|---|---|
| `word-boundary` | gitleaks 65, trufflehog 159, CRS 34 | engine limit — residual (b) |
| `pattern-too-long` | CRS 73, IDS 186 | policy (c) — TRAPS #21 |
| `composite-pattern` | semgrep 3247 | extractor honesty; not a compiler lift |
| `internal-anchor` | semgrep 3113 | engine / rewrite backlog |
| `unclosed-class` | IDS 219 | classified (not parse-error) |
| `(?-i:...)` | low | stay reject unless surface rises |

## Re-measure

`scripts/remeasure-frozen-ids.py` freezes `regex_id`s and emits
`*_remeasure_delta.json` for Phase 3.

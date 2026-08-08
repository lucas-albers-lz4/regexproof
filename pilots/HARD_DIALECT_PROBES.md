# Hard-dialect probes from Phase 2 → Phase 1 golden suite

Routed probes exercised by the gitleaks / validator.js pilots
([issue #18](https://github.com/lucas-albers-lz4/regexproof/issues/18)).

| Probe | Dialect | Source | Golden coverage |
|---|---|---|---|
| Leading `(?i)` lifted to `flags=i` | re2 | gitleaks rules | `normalize_inline_flags` + re2 fold cases |
| `\b` word boundary → `unencodable: word-boundary` | re2 | majority of gitleaks | reject-list golden |
| RE2 vs Python İ/ı fold divergence | re2 | fold tables | `re2-fold-i` trap |
| JS `\s` includes NBSP / U+2028 | ecma | isFQDN / email | `js-space` / `dot-terminator` traps |
| Unicode alphabet on isAscii boundary | ecma | isAscii.js | `VJS-ascii-no-high` pilot property |

These are checkable via `pytest tests/test_golden.py` and `scripts/pilot-properties.py`.

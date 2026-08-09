# Cross-corpus encodable matrix

Rollup of committed `*_encodable_fraction.json` (Corpus Wave 2 closeout).
Sample-scoped rows have `complete_run=false` — not full-corpus proofs.

| Corpus | Decision | Fraction | Encodable | Size | scope | parse-error |
|---|---|---|---|---|---|---|
| gitleaks | go | 0.819 | 181 | 221 | full_corpus | 0 |
| validatorjs | go | 0.7689 | 163 | 212 | None | 0 |
| coreruleset | go | 0.6908 | 239 | 346 | full_corpus | 0 |
| trufflehog | go | 0.9302 | 200 | 215 | full_corpus | 0 |
| detect-secrets | go | 0.3725 | 19 | 51 | full_corpus | 0 |
| ids_rules | go | 0.8519 | 6961 | 8171 | full_corpus | 0 |
| semgrep_rules | go | 0.4941 | 707 | 1431 | full_corpus | 0 |
| yara_rules | go | 0.6563 | 11534 | 17574 | full_corpus | 1 |
| pcre2_testdata | go | 1.0 | 2 | 2 | sample | 0 |
| re2_testdata | go | 1.0 | 4 | 4 | sample | 0 |
| cpython_re | go | 0.5556 | 15 | 27 | sample | 0 |
| busybox | go | 1.0 | 2 | 2 | sample | 0 |
| test262 | go | 0.8095 | 34 | 42 | sample | 0 |
| rust_regex | inventory_only | None | 1 | 1 | inventory_only | 0 |

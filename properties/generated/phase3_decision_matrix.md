# Phase 3 decision matrix

| Corpus | Decision | Fraction | Phase-3 note |
|---|---|---|---|
| gitleaks | go | 0.6018 | confirm go |
| validatorjs | go | 0.684 | confirm go |
| coreruleset | go | 0.6478 | confirm go |
| trufflehog | no-go | 0.2326 | remain no-go; primary residual is engine-limit (word-boundary / composite-pattern / internal-anchor) — not a silent skip |
| ids_rules | go | 0.879 | confirm go |
| semgrep_rules | no-go | 0.2741 | remain no-go; primary residual is engine-limit (word-boundary / composite-pattern / internal-anchor) — not a silent skip |
| pcre2_testdata | go | 1.0 | confirm go |
| re2_testdata | go | 1.0 | confirm go |
| cpython_re | go | 0.5556 | confirm go |
| busybox | go | 1.0 | confirm go |
| rust_regex | inventory_only | None | no fraction gate |

# Phase 3 decision matrix — SUPERSEDED

> **Superseded** by post–fix-wave remeasure (PR #80), A1B trailing-alt
> lowering (PR #89), and P3 validate (PR #90). Do not use these fractions
> for go/no-go gates.
>
> Current truth: [`cross_corpus_matrix.md`](cross_corpus_matrix.md) and
> each `*_encodable_fraction.json` (plus
> [`trailing_alt_dollar_p3_delta.md`](trailing_alt_dollar_p3_delta.md)).

| Corpus | Decision (stale) | Fraction (stale) | Phase-3 note |
|---|---|---|---|
| gitleaks | go | 0.8235 | **now 0.8190** after reject-over-hoist + A1B |
| validatorjs | go | 0.684 | see current fraction artifact |
| coreruleset | go | 0.7168 | **now 0.6908** |
| trufflehog | go | 0.9349 | **now 0.9302** |
| ids_rules | go | 0.879 | **now 0.8519** |
| semgrep_rules | no-go | 0.2741 | **now 0.2842** (still no-go) |
| pcre2_testdata | go | 1.0 | unchanged |
| re2_testdata | go | 1.0 | unchanged |
| cpython_re | go | 0.5556 | unchanged |
| busybox | go | 1.0 | unchanged |
| rust_regex | inventory_only | None | no fraction gate |
| detect-secrets | — | — | **added P4: 0.3725** (v1.5.0) |

# Compiler feature-yield artifact (D5)

<!-- provenance: 94 triage files, inputs d7769ea6c574, 871 gate decisions -->

Sites unlocked per missing compiler feature, aggregated across
`properties/triage/*.ndjson` and weighted by corpus admission status
(GO=3, triage-trial=2, no-go=1). Sorted by weighted unlock value.

- Input files: 94
- Triage inputs hash: `d7769ea6c574ea1a`
- Gate decisions: 871
- Total unencodable rows: 60271
- Total weighted sites: 177744.0

| # | unencodable_reason | sites | weighted | per-corpus (decision:weighted) | top dialects |
|---|---|---|---|---|---|
| 1 | `fullword-boundary` | 37791 | 112800.0 | go:111654.0, triage-trial:1146.0 | yara:37791 |
| 2 | `stateful` | 6134 | 17540.0 | go:15951.0, no-go:45.0, triage-trial:1544.0 | ecma:6134 |
| 3 | `composite-pattern` | 4519 | 12913.0 | go:12474.0, no-go:283.0, triage-trial:156.0 | py_re:4181, ecma:338 |
| 4 | `u-flag` | 1845 | 5528.0 | go:5514.0, triage-trial:14.0 | ecma:1845 |
| 5 | `word-boundary` | 1838 | 5309.0 | go:4965.0, no-go:22.0, triage-trial:322.0 | py_re:1695, ecma:115, pcre:21, re2:6 |
| 6 | `internal-anchor` | 1185 | 3516.0 | go:3438.0, triage-trial:78.0 | posix-shell:1174, ecma:10, pcre:1 |
| 7 | `lookaround` | 844 | 2409.0 | go:2313.0, no-go:50.0, triage-trial:46.0 | py_re:701, ecma:143 |
| 8 | `wide-non-literal` | 723 | 2075.0 | go:1887.0, triage-trial:188.0 | yara:723 |
| 9 | `per-alternative-anchor` | 706 | 2064.0 | go:1968.0, no-go:4.0, triage-trial:92.0 | ecma:314, posix-shell:271, py_re:116, re2:3 |
| 10 | `m-flag` | 659 | 1905.0 | go:1836.0, no-go:25.0, triage-trial:44.0 | py_re:498, ecma:161 |
| 11 | `negated-shorthand` | 497 | 1419.0 | go:1323.0, no-go:16.0, triage-trial:80.0 | py_re:281, ecma:213, re2:2, yara:1 |
| 12 | `unsupported:POSSESSIVE_REPEAT` | 466 | 1398.0 | go:1398.0 | py_re:466 |
| 13 | `unicode-not-literal` | 486 | 1353.0 | go:1197.0, no-go:18.0, triage-trial:138.0 | py_re:486 |
| 14 | `multi-match` | 458 | 1298.0 | go:1242.0, no-go:32.0, triage-trial:24.0 | py_re:458 |
| 15 | `backref` | 407 | 1168.0 | go:1137.0, no-go:25.0, triage-trial:6.0 | py_re:353, ecma:51, posix-shell:2, yara:1 |
| 16 | `pattern-too-long` | 324 | 942.0 | go:909.0, no-go:9.0, triage-trial:24.0 | py_re:194, pcre:72, yara:29, ecma:21 |
| 17 | `unsupported:ATOMIC_GROUP` | 276 | 828.0 | go:828.0 | py_re:276 |
| 18 | `gnu-extension` | 236 | 707.0 | go:705.0, triage-trial:2.0 | posix-shell:236 |
| 19 | `unsupported-modifier:base64` | 193 | 576.0 | go:570.0, triage-trial:6.0 | yara:193 |
| 20 | `parse-error` | 182 | 545.0 | go:543.0, triage-trial:2.0 | posix-shell:71, pcre:53, ecma:51, yara:7 |
| 21 | `inline-flag` | 125 | 337.0 | go:273.0, no-go:4.0, triage-trial:60.0 | re2:59, py_re:56, pcre:6, ecma:4 |
| 22 | `v-flag` | 93 | 276.0 | go:270.0, triage-trial:6.0 | ecma:93 |
| 23 | `parse-error:PatternError` | 60 | 176.0 | go:174.0, no-go:2.0 | py_re:60 |
| 24 | `negated-class` | 45 | 135.0 | go:135.0 | pcre:32, py_re:13 |
| 25 | `unsupported-syntax` | 43 | 125.0 | go:117.0, triage-trial:8.0 | ecma:32, posix-shell:11 |
| 26 | `empty-class` | 29 | 87.0 | go:87.0 | posix-shell:20, ecma:6, yara:3 |
| 27 | `unclosed-group` | 29 | 87.0 | go:87.0 | ecma:23, posix-shell:6 |
| 28 | `bad-range` | 27 | 77.0 | go:69.0, triage-trial:8.0 | ecma:21, pcre:6 |
| 29 | `repeat-count` | 15 | 45.0 | go:45.0 | yara:15 |
| 30 | `unclosed-class` | 12 | 36.0 | go:36.0 | posix-shell:12 |
| 31 | `gnu-word-boundary` | 9 | 27.0 | go:27.0 | posix-shell:9 |
| 32 | `unsupported:FAILURE` | 7 | 21.0 | go:21.0 | py_re:7 |
| 33 | `unsupported-modifier:xor` | 6 | 18.0 | go:18.0 | yara:6 |
| 34 | `unsupported-modifier:base64,base64wide` | 2 | 4.0 | triage-trial:4.0 | yara:2 |

## Corpus admission weighting

| decision | weight | rows | weighted sites |
|---|---|---|---|
| go | 3 | 57737 | 173211.0 |
| no-go | 1 | 535 | 535.0 |
| triage-trial | 2 | 1999 | 3998.0 |

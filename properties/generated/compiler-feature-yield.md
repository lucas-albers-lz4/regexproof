# Compiler feature-yield artifact (D5)

<!-- provenance: 82 triage files, inputs 13d82c0f35f1, 837 gate decisions -->

Sites unlocked per missing compiler feature, aggregated across
`properties/triage/*.ndjson` and weighted by corpus admission status
(GO=3, triage-trial=2, no-go=1). Sorted by weighted unlock value.

- Input files: 82
- Triage inputs hash: `13d82c0f35f11f1e`
- Gate decisions: 837
- Total unencodable rows: 48772
- Total weighted sites: 143387.0

| # | unencodable_reason | sites | weighted | per-corpus (decision:weighted) | top dialects |
|---|---|---|---|---|---|
| 1 | `fullword-boundary` | 31864 | 95019.0 | go:93873.0, triage-trial:1146.0 | yara:31864 |
| 2 | `composite-pattern` | 4293 | 12279.0 | go:11862.0, no-go:261.0, triage-trial:156.0 | py_re:4087, ecma:206 |
| 3 | `stateful` | 3295 | 9113.0 | go:7569.0, triage-trial:1544.0 | ecma:3295 |
| 4 | `word-boundary` | 1628 | 4679.0 | go:4335.0, no-go:22.0, triage-trial:322.0 | py_re:1518, ecma:82, pcre:21, re2:6 |
| 5 | `u-flag` | 1096 | 3281.0 | go:3267.0, triage-trial:14.0 | ecma:1096 |
| 6 | `lookaround` | 774 | 2201.0 | go:2106.0, no-go:49.0, triage-trial:46.0 | py_re:681, ecma:93 |
| 7 | `wide-non-literal` | 694 | 1988.0 | go:1800.0, triage-trial:188.0 | yara:694 |
| 8 | `m-flag` | 569 | 1635.0 | go:1566.0, no-go:25.0, triage-trial:44.0 | py_re:451, ecma:118 |
| 9 | `internal-anchor` | 490 | 1431.0 | go:1353.0, triage-trial:78.0 | posix-shell:480, ecma:9, pcre:1 |
| 10 | `unsupported:POSSESSIVE_REPEAT` | 466 | 1398.0 | go:1398.0 | py_re:466 |
| 11 | `negated-shorthand` | 449 | 1275.0 | go:1179.0, no-go:16.0, triage-trial:80.0 | py_re:264, ecma:182, re2:2, yara:1 |
| 12 | `multi-match` | 450 | 1274.0 | go:1218.0, no-go:32.0, triage-trial:24.0 | py_re:450 |
| 13 | `per-alternative-anchor` | 438 | 1262.0 | go:1167.0, no-go:3.0, triage-trial:92.0 | ecma:234, posix-shell:100, py_re:99, re2:3 |
| 14 | `unicode-not-literal` | 420 | 1155.0 | go:999.0, no-go:18.0, triage-trial:138.0 | py_re:420 |
| 15 | `backref` | 399 | 1144.0 | go:1113.0, no-go:25.0, triage-trial:6.0 | py_re:353, ecma:45, posix-shell:1 |
| 16 | `pattern-too-long` | 313 | 911.0 | go:879.0, no-go:8.0, triage-trial:24.0 | py_re:192, pcre:72, yara:26, ecma:19 |
| 17 | `unsupported:ATOMIC_GROUP` | 276 | 828.0 | go:828.0 | py_re:276 |
| 18 | `unsupported-modifier:base64` | 193 | 576.0 | go:570.0, triage-trial:6.0 | yara:193 |
| 19 | `parse-error` | 119 | 356.0 | go:354.0, triage-trial:2.0 | pcre:53, ecma:51, posix-shell:8, yara:7 |
| 20 | `inline-flag` | 125 | 337.0 | go:273.0, no-go:4.0, triage-trial:60.0 | re2:59, py_re:56, pcre:6, ecma:4 |
| 21 | `v-flag` | 93 | 276.0 | go:270.0, triage-trial:6.0 | ecma:93 |
| 22 | `gnu-extension` | 74 | 221.0 | go:219.0, triage-trial:2.0 | posix-shell:74 |
| 23 | `parse-error:PatternError` | 60 | 176.0 | go:174.0, no-go:2.0 | py_re:60 |
| 24 | `unsupported-syntax` | 43 | 125.0 | go:117.0, triage-trial:8.0 | ecma:32, posix-shell:11 |
| 25 | `negated-class` | 40 | 120.0 | go:120.0 | pcre:32, py_re:8 |
| 26 | `unclosed-group` | 28 | 84.0 | go:84.0 | ecma:22, posix-shell:6 |
| 27 | `bad-range` | 27 | 77.0 | go:69.0, triage-trial:8.0 | ecma:21, pcre:6 |
| 28 | `repeat-count` | 15 | 45.0 | go:45.0 | yara:15 |
| 29 | `empty-class` | 13 | 39.0 | go:39.0 | ecma:5, posix-shell:5, yara:3 |
| 30 | `unclosed-class` | 12 | 36.0 | go:36.0 | posix-shell:12 |
| 31 | `unsupported:FAILURE` | 7 | 21.0 | go:21.0 | py_re:7 |
| 32 | `unsupported-modifier:xor` | 6 | 18.0 | go:18.0 | yara:6 |
| 33 | `unsupported-modifier:base64,base64wide` | 2 | 4.0 | triage-trial:4.0 | yara:2 |
| 34 | `gnu-word-boundary` | 1 | 3.0 | go:3.0 | posix-shell:1 |

## Corpus admission weighting

| decision | weight | rows | weighted sites |
|---|---|---|---|
| go | 3 | 46308 | 138924.0 |
| no-go | 1 | 465 | 465.0 |
| triage-trial | 2 | 1999 | 3998.0 |

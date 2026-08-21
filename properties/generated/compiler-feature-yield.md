# Compiler feature-yield artifact (D5)

<!-- provenance: 82 triage files, inputs 47c5eafcb90c, 837 gate decisions -->

Sites unlocked per missing compiler feature, aggregated across
`properties/triage/*.ndjson` and weighted by corpus admission status
(GO=3, triage-trial=2, no-go=1). Sorted by weighted unlock value.

- Input files: 82
- Triage inputs hash: `47c5eafcb90ce6cc`
- Gate decisions: 837
- Total unencodable rows: 48803
- Total weighted sites: 143480.0

| # | unencodable_reason | sites | weighted | per-corpus (decision:weighted) | top dialects |
|---|---|---|---|---|---|
| 1 | `fullword-boundary` | 31864 | 95019.0 | go:93873.0, triage-trial:1146.0 | yara:31864 |
| 2 | `composite-pattern` | 4298 | 12294.0 | go:11877.0, no-go:261.0, triage-trial:156.0 | py_re:4087, ecma:211 |
| 3 | `stateful` | 3307 | 9149.0 | go:7605.0, triage-trial:1544.0 | ecma:3307 |
| 4 | `word-boundary` | 1628 | 4679.0 | go:4335.0, no-go:22.0, triage-trial:322.0 | py_re:1518, ecma:82, pcre:21, re2:6 |
| 5 | `u-flag` | 1098 | 3287.0 | go:3273.0, triage-trial:14.0 | ecma:1098 |
| 6 | `lookaround` | 776 | 2207.0 | go:2112.0, no-go:49.0, triage-trial:46.0 | py_re:681, ecma:95 |
| 7 | `wide-non-literal` | 694 | 1988.0 | go:1800.0, triage-trial:188.0 | yara:694 |
| 8 | `m-flag` | 569 | 1635.0 | go:1566.0, no-go:25.0, triage-trial:44.0 | py_re:451, ecma:118 |
| 9 | `internal-anchor` | 492 | 1437.0 | go:1359.0, triage-trial:78.0 | posix-shell:480, ecma:11, pcre:1 |
| 10 | `unsupported:POSSESSIVE_REPEAT` | 466 | 1398.0 | go:1398.0 | py_re:466 |
| 11 | `negated-shorthand` | 450 | 1278.0 | go:1182.0, no-go:16.0, triage-trial:80.0 | py_re:264, ecma:183, re2:2, yara:1 |
| 12 | `multi-match` | 450 | 1274.0 | go:1218.0, no-go:32.0, triage-trial:24.0 | py_re:450 |
| 13 | `per-alternative-anchor` | 439 | 1265.0 | go:1170.0, no-go:3.0, triage-trial:92.0 | ecma:235, posix-shell:100, py_re:99, re2:3 |
| 14 | `unicode-not-literal` | 420 | 1155.0 | go:999.0, no-go:18.0, triage-trial:138.0 | py_re:420 |
| 15 | `backref` | 399 | 1144.0 | go:1113.0, no-go:25.0, triage-trial:6.0 | py_re:353, ecma:45, posix-shell:1 |
| 16 | `pattern-too-long` | 313 | 911.0 | go:879.0, no-go:8.0, triage-trial:24.0 | py_re:192, pcre:72, yara:26, ecma:19 |
| 17 | `unsupported:ATOMIC_GROUP` | 276 | 828.0 | go:828.0 | py_re:276 |
| 18 | `unsupported-modifier:base64` | 193 | 576.0 | go:570.0, triage-trial:6.0 | yara:193 |
| 19 | `parse-error` | 119 | 356.0 | go:354.0, triage-trial:2.0 | pcre:53, ecma:51, posix-shell:8, yara:7 |
| 20 | `inline-flag` | 125 | 337.0 | go:273.0, no-go:4.0, triage-trial:60.0 | re2:59, py_re:56, pcre:6, ecma:4 |
| 21 | `v-flag` | 96 | 285.0 | go:279.0, triage-trial:6.0 | ecma:96 |
| 22 | `gnu-extension` | 74 | 221.0 | go:219.0, triage-trial:2.0 | posix-shell:74 |
| 23 | `parse-error:PatternError` | 60 | 176.0 | go:174.0, no-go:2.0 | py_re:60 |
| 24 | `unsupported-syntax` | 44 | 128.0 | go:120.0, triage-trial:8.0 | ecma:33, posix-shell:11 |
| 25 | `negated-class` | 40 | 120.0 | go:120.0 | pcre:32, py_re:8 |
| 26 | `unclosed-group` | 30 | 90.0 | go:90.0 | ecma:24, posix-shell:6 |
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
| go | 3 | 46339 | 139017.0 |
| no-go | 1 | 465 | 465.0 |
| triage-trial | 2 | 1999 | 3998.0 |

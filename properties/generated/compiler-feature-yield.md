# Compiler feature-yield artifact (D5)

<!-- provenance: 84 triage files, inputs ec70b8f95d1b, 837 gate decisions -->

Sites unlocked per missing compiler feature, aggregated across
`properties/triage/*.ndjson` and weighted by corpus admission status
(GO=3, triage-trial=2, no-go=1). Sorted by weighted unlock value.

- Input files: 84
- Triage inputs hash: `ec70b8f95d1be0f0`
- Gate decisions: 837
- Total unencodable rows: 51512
- Total weighted sites: 151607.0

| # | unencodable_reason | sites | weighted | per-corpus (decision:weighted) | top dialects |
|---|---|---|---|---|---|
| 1 | `fullword-boundary` | 31864 | 95019.0 | go:93873.0, triage-trial:1146.0 | yara:31864 |
| 2 | `stateful` | 4998 | 14222.0 | go:12678.0, triage-trial:1544.0 | ecma:4998 |
| 3 | `composite-pattern` | 4347 | 12441.0 | go:12024.0, no-go:261.0, triage-trial:156.0 | py_re:4087, ecma:260 |
| 4 | `u-flag` | 1930 | 5783.0 | go:5769.0, triage-trial:14.0 | ecma:1930 |
| 5 | `word-boundary` | 1645 | 4730.0 | go:4386.0, no-go:22.0, triage-trial:322.0 | py_re:1518, ecma:99, pcre:21, re2:6 |
| 6 | `lookaround` | 816 | 2327.0 | go:2232.0, no-go:49.0, triage-trial:46.0 | py_re:681, ecma:135 |
| 7 | `wide-non-literal` | 694 | 1988.0 | go:1800.0, triage-trial:188.0 | yara:694 |
| 8 | `m-flag` | 606 | 1746.0 | go:1677.0, no-go:25.0, triage-trial:44.0 | py_re:451, ecma:155 |
| 9 | `internal-anchor` | 490 | 1431.0 | go:1353.0, triage-trial:78.0 | posix-shell:480, ecma:9, pcre:1 |
| 10 | `unsupported:POSSESSIVE_REPEAT` | 466 | 1398.0 | go:1398.0 | py_re:466 |
| 11 | `per-alternative-anchor` | 463 | 1337.0 | go:1242.0, no-go:3.0, triage-trial:92.0 | ecma:259, posix-shell:100, py_re:99, re2:3 |
| 12 | `negated-shorthand` | 469 | 1335.0 | go:1239.0, no-go:16.0, triage-trial:80.0 | py_re:264, ecma:202, re2:2, yara:1 |
| 13 | `multi-match` | 450 | 1274.0 | go:1218.0, no-go:32.0, triage-trial:24.0 | py_re:450 |
| 14 | `backref` | 405 | 1162.0 | go:1131.0, no-go:25.0, triage-trial:6.0 | py_re:353, ecma:51, posix-shell:1 |
| 15 | `unicode-not-literal` | 420 | 1155.0 | go:999.0, no-go:18.0, triage-trial:138.0 | py_re:420 |
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
| 26 | `unclosed-group` | 29 | 87.0 | go:87.0 | ecma:23, posix-shell:6 |
| 27 | `bad-range` | 27 | 77.0 | go:69.0, triage-trial:8.0 | ecma:21, pcre:6 |
| 28 | `repeat-count` | 15 | 45.0 | go:45.0 | yara:15 |
| 29 | `empty-class` | 14 | 42.0 | go:42.0 | ecma:6, posix-shell:5, yara:3 |
| 30 | `unclosed-class` | 12 | 36.0 | go:36.0 | posix-shell:12 |
| 31 | `unsupported:FAILURE` | 7 | 21.0 | go:21.0 | py_re:7 |
| 32 | `unsupported-modifier:xor` | 6 | 18.0 | go:18.0 | yara:6 |
| 33 | `unsupported-modifier:base64,base64wide` | 2 | 4.0 | triage-trial:4.0 | yara:2 |
| 34 | `gnu-word-boundary` | 1 | 3.0 | go:3.0 | posix-shell:1 |

## Corpus admission weighting

| decision | weight | rows | weighted sites |
|---|---|---|---|
| go | 3 | 49048 | 147144.0 |
| no-go | 1 | 465 | 465.0 |
| triage-trial | 2 | 1999 | 3998.0 |

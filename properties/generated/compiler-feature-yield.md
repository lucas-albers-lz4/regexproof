# Compiler feature-yield artifact (D5)

<!-- provenance: 86 triage files, inputs 466a693984fe, 837 gate decisions -->

Sites unlocked per missing compiler feature, aggregated across
`properties/triage/*.ndjson` and weighted by corpus admission status
(GO=3, triage-trial=2, no-go=1). Sorted by weighted unlock value.

- Input files: 86
- Triage inputs hash: `466a693984fe79c2`
- Gate decisions: 837
- Total unencodable rows: 53112
- Total weighted sites: 156407.0

| # | unencodable_reason | sites | weighted | per-corpus (decision:weighted) | top dialects |
|---|---|---|---|---|---|
| 1 | `fullword-boundary` | 31864 | 95019.0 | go:93873.0, triage-trial:1146.0 | yara:31864 |
| 2 | `stateful` | 5495 | 15713.0 | go:14169.0, triage-trial:1544.0 | ecma:5495 |
| 3 | `composite-pattern` | 4376 | 12528.0 | go:12111.0, no-go:261.0, triage-trial:156.0 | py_re:4087, ecma:289 |
| 4 | `u-flag` | 1845 | 5528.0 | go:5514.0, triage-trial:14.0 | ecma:1845 |
| 5 | `word-boundary` | 1656 | 4763.0 | go:4419.0, no-go:22.0, triage-trial:322.0 | py_re:1518, ecma:110, pcre:21, re2:6 |
| 6 | `internal-anchor` | 1184 | 3513.0 | go:3435.0, triage-trial:78.0 | posix-shell:1174, ecma:9, pcre:1 |
| 7 | `lookaround` | 823 | 2348.0 | go:2253.0, no-go:49.0, triage-trial:46.0 | py_re:681, ecma:142 |
| 8 | `wide-non-literal` | 694 | 1988.0 | go:1800.0, triage-trial:188.0 | yara:694 |
| 9 | `per-alternative-anchor` | 648 | 1892.0 | go:1797.0, no-go:3.0, triage-trial:92.0 | ecma:273, posix-shell:271, py_re:99, re2:3 |
| 10 | `m-flag` | 607 | 1749.0 | go:1680.0, no-go:25.0, triage-trial:44.0 | py_re:451, ecma:156 |
| 11 | `unsupported:POSSESSIVE_REPEAT` | 466 | 1398.0 | go:1398.0 | py_re:466 |
| 12 | `negated-shorthand` | 476 | 1356.0 | go:1260.0, no-go:16.0, triage-trial:80.0 | py_re:264, ecma:209, re2:2, yara:1 |
| 13 | `multi-match` | 450 | 1274.0 | go:1218.0, no-go:32.0, triage-trial:24.0 | py_re:450 |
| 14 | `backref` | 406 | 1165.0 | go:1134.0, no-go:25.0, triage-trial:6.0 | py_re:353, ecma:51, posix-shell:2 |
| 15 | `unicode-not-literal` | 420 | 1155.0 | go:999.0, no-go:18.0, triage-trial:138.0 | py_re:420 |
| 16 | `pattern-too-long` | 318 | 926.0 | go:894.0, no-go:8.0, triage-trial:24.0 | py_re:192, pcre:72, yara:26, ecma:20 |
| 17 | `unsupported:ATOMIC_GROUP` | 276 | 828.0 | go:828.0 | py_re:276 |
| 18 | `gnu-extension` | 236 | 707.0 | go:705.0, triage-trial:2.0 | posix-shell:236 |
| 19 | `unsupported-modifier:base64` | 193 | 576.0 | go:570.0, triage-trial:6.0 | yara:193 |
| 20 | `parse-error` | 182 | 545.0 | go:543.0, triage-trial:2.0 | posix-shell:71, pcre:53, ecma:51, yara:7 |
| 21 | `inline-flag` | 125 | 337.0 | go:273.0, no-go:4.0, triage-trial:60.0 | re2:59, py_re:56, pcre:6, ecma:4 |
| 22 | `v-flag` | 93 | 276.0 | go:270.0, triage-trial:6.0 | ecma:93 |
| 23 | `parse-error:PatternError` | 60 | 176.0 | go:174.0, no-go:2.0 | py_re:60 |
| 24 | `unsupported-syntax` | 43 | 125.0 | go:117.0, triage-trial:8.0 | ecma:32, posix-shell:11 |
| 25 | `negated-class` | 40 | 120.0 | go:120.0 | pcre:32, py_re:8 |
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
| go | 3 | 50648 | 151944.0 |
| no-go | 1 | 465 | 465.0 |
| triage-trial | 2 | 1999 | 3998.0 |

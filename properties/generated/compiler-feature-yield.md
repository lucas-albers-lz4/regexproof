# Compiler feature-yield artifact (D5)

<!-- provenance: 80 triage files, inputs 4a90af62427b, 837 gate decisions -->

Sites unlocked per missing compiler feature, aggregated across
`properties/triage/*.ndjson` and weighted by corpus admission status
(GO=3, triage-trial=2, no-go=1). Sorted by weighted unlock value.

- Input files: 80
- Triage inputs hash: `4a90af62427bad0f`
- Gate decisions: 837
- Total unencodable rows: 47120
- Total weighted sites: 138431.0

| # | unencodable_reason | sites | weighted | per-corpus (decision:weighted) | top dialects |
|---|---|---|---|---|---|
| 1 | `fullword-boundary` | 31864 | 95019.0 | go:93873.0, triage-trial:1146.0 | yara:31864 |
| 2 | `composite-pattern` | 3999 | 11397.0 | go:10980.0, no-go:261.0, triage-trial:156.0 | py_re:3852, ecma:147 |
| 3 | `stateful` | 2939 | 8045.0 | go:6501.0, triage-trial:1544.0 | ecma:2939 |
| 4 | `word-boundary` | 1147 | 3236.0 | go:2892.0, no-go:22.0, triage-trial:322.0 | py_re:1041, ecma:78, pcre:21, re2:6 |
| 5 | `u-flag` | 963 | 2882.0 | go:2868.0, triage-trial:14.0 | ecma:963 |
| 6 | `lookaround` | 743 | 2108.0 | go:2013.0, no-go:49.0, triage-trial:46.0 | py_re:665, ecma:78 |
| 7 | `wide-non-literal` | 694 | 1988.0 | go:1800.0, triage-trial:188.0 | yara:694 |
| 8 | `internal-anchor` | 489 | 1428.0 | go:1350.0, triage-trial:78.0 | posix-shell:480, ecma:8, pcre:1 |
| 9 | `unsupported:POSSESSIVE_REPEAT` | 466 | 1398.0 | go:1398.0 | py_re:466 |
| 10 | `m-flag` | 444 | 1260.0 | go:1191.0, no-go:25.0, triage-trial:44.0 | py_re:371, ecma:73 |
| 11 | `multi-match` | 435 | 1229.0 | go:1173.0, no-go:32.0, triage-trial:24.0 | py_re:435 |
| 12 | `negated-shorthand` | 424 | 1200.0 | go:1104.0, no-go:16.0, triage-trial:80.0 | py_re:246, ecma:175, re2:2, yara:1 |
| 13 | `backref` | 382 | 1093.0 | go:1062.0, no-go:25.0, triage-trial:6.0 | py_re:348, ecma:33, posix-shell:1 |
| 14 | `per-alternative-anchor` | 377 | 1079.0 | go:984.0, no-go:3.0, triage-trial:92.0 | ecma:201, posix-shell:100, py_re:71, re2:3 |
| 15 | `unicode-not-literal` | 332 | 891.0 | go:735.0, no-go:18.0, triage-trial:138.0 | py_re:332 |
| 16 | `pattern-too-long` | 289 | 839.0 | go:807.0, no-go:8.0, triage-trial:24.0 | py_re:169, pcre:72, yara:26, ecma:18 |
| 17 | `unsupported:ATOMIC_GROUP` | 276 | 828.0 | go:828.0 | py_re:276 |
| 18 | `unsupported-modifier:base64` | 193 | 576.0 | go:570.0, triage-trial:6.0 | yara:193 |
| 19 | `parse-error` | 119 | 356.0 | go:354.0, triage-trial:2.0 | pcre:53, ecma:51, posix-shell:8, yara:7 |
| 20 | `inline-flag` | 125 | 337.0 | go:273.0, no-go:4.0, triage-trial:60.0 | re2:59, py_re:56, pcre:6, ecma:4 |
| 21 | `v-flag` | 93 | 276.0 | go:270.0, triage-trial:6.0 | ecma:93 |
| 22 | `gnu-extension` | 74 | 221.0 | go:219.0, triage-trial:2.0 | posix-shell:74 |
| 23 | `parse-error:PatternError` | 60 | 176.0 | go:174.0, no-go:2.0 | py_re:60 |
| 24 | `unsupported-syntax` | 43 | 125.0 | go:117.0, triage-trial:8.0 | ecma:32, posix-shell:11 |
| 25 | `negated-class` | 40 | 120.0 | go:120.0 | pcre:32, py_re:8 |
| 26 | `unclosed-group` | 27 | 81.0 | go:81.0 | ecma:21, posix-shell:6 |
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
| go | 3 | 44656 | 133968.0 |
| no-go | 1 | 465 | 465.0 |
| triage-trial | 2 | 1999 | 3998.0 |

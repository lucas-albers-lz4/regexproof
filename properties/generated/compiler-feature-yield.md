# Compiler feature-yield artifact (D5)

<!-- provenance: 100 triage files, inputs 1650ee6a7010, 871 gate decisions -->

Sites unlocked per missing compiler feature, aggregated across
`properties/triage/*.ndjson` and weighted by corpus admission status
(GO=3, triage-trial=2, no-go=1). Sorted by weighted unlock value.

- Input files: 100
- Triage inputs hash: `1650ee6a7010efd6`
- Gate decisions: 871
- Total unencodable rows: 125626
- Total weighted sites: 373809.0

| # | unencodable_reason | sites | weighted | per-corpus (decision:weighted) | top dialects |
|---|---|---|---|---|---|
| 1 | `fullword-boundary` | 102041 | 305550.0 | go:304404.0, triage-trial:1146.0 | yara:102041 |
| 2 | `stateful` | 6134 | 17540.0 | go:15951.0, no-go:45.0, triage-trial:1544.0 | ecma:6134 |
| 3 | `composite-pattern` | 4519 | 12913.0 | go:12474.0, no-go:283.0, triage-trial:156.0 | py_re:4181, ecma:338 |
| 4 | `u-flag` | 1845 | 5528.0 | go:5514.0, triage-trial:14.0 | ecma:1845 |
| 5 | `word-boundary` | 1852 | 5351.0 | go:5007.0, no-go:22.0, triage-trial:322.0 | py_re:1695, ecma:115, pcre:21, yara:15 |
| 6 | `wide-non-literal` | 1651 | 4859.0 | go:4671.0, triage-trial:188.0 | yara:1651 |
| 7 | `internal-anchor` | 1191 | 3534.0 | go:3456.0, triage-trial:78.0 | posix-shell:1174, ecma:10, yara:6, pcre:1 |
| 8 | `lookaround` | 844 | 2409.0 | go:2313.0, no-go:50.0, triage-trial:46.0 | py_re:701, ecma:143 |
| 9 | `per-alternative-anchor` | 712 | 2082.0 | go:1986.0, no-go:4.0, triage-trial:92.0 | ecma:314, posix-shell:271, py_re:116, yara:8 |
| 10 | `m-flag` | 659 | 1905.0 | go:1836.0, no-go:25.0, triage-trial:44.0 | py_re:498, ecma:161 |
| 11 | `negated-shorthand` | 497 | 1419.0 | go:1323.0, no-go:16.0, triage-trial:80.0 | py_re:281, ecma:213, re2:2, yara:1 |
| 12 | `unsupported:POSSESSIVE_REPEAT` | 466 | 1398.0 | go:1398.0 | py_re:466 |
| 13 | `unicode-not-literal` | 486 | 1353.0 | go:1197.0, no-go:18.0, triage-trial:138.0 | py_re:486 |
| 14 | `multi-match` | 458 | 1298.0 | go:1242.0, no-go:32.0, triage-trial:24.0 | py_re:458 |
| 15 | `pattern-too-long` | 419 | 1227.0 | go:1194.0, no-go:9.0, triage-trial:24.0 | py_re:194, yara:124, pcre:72, ecma:21 |
| 16 | `backref` | 407 | 1168.0 | go:1137.0, no-go:25.0, triage-trial:6.0 | py_re:353, ecma:51, posix-shell:2, yara:1 |
| 17 | `unsupported:ATOMIC_GROUP` | 276 | 828.0 | go:828.0 | py_re:276 |
| 18 | `gnu-extension` | 236 | 707.0 | go:705.0, triage-trial:2.0 | posix-shell:236 |
| 19 | `unsupported-modifier:base64` | 223 | 666.0 | go:660.0, triage-trial:6.0 | yara:223 |
| 20 | `parse-error` | 182 | 545.0 | go:543.0, triage-trial:2.0 | posix-shell:71, pcre:53, ecma:51, yara:7 |
| 21 | `inline-flag` | 125 | 337.0 | go:273.0, no-go:4.0, triage-trial:60.0 | re2:59, py_re:56, pcre:6, ecma:4 |
| 22 | `v-flag` | 93 | 276.0 | go:270.0, triage-trial:6.0 | ecma:93 |
| 23 | `parse-error:PatternError` | 60 | 176.0 | go:174.0, no-go:2.0 | py_re:60 |
| 24 | `negated-class` | 45 | 135.0 | go:135.0 | pcre:32, py_re:13 |
| 25 | `unsupported-syntax` | 43 | 125.0 | go:117.0, triage-trial:8.0 | ecma:32, posix-shell:11 |
| 26 | `empty-class` | 29 | 87.0 | go:87.0 | posix-shell:20, ecma:6, yara:3 |
| 27 | `unclosed-group` | 29 | 87.0 | go:87.0 | ecma:23, posix-shell:6 |
| 28 | `bad-range` | 27 | 77.0 | go:69.0, triage-trial:8.0 | ecma:21, pcre:6 |
| 29 | `repeat-count` | 17 | 51.0 | go:51.0 | yara:17 |
| 30 | `unsupported-modifier:xor` | 16 | 48.0 | go:48.0 | yara:16 |
| 31 | `unclosed-class` | 12 | 36.0 | go:36.0 | posix-shell:12 |
| 32 | `gnu-word-boundary` | 9 | 27.0 | go:27.0 | posix-shell:9 |
| 33 | `unsupported-escape` | 7 | 21.0 | go:21.0 | yara:7 |
| 34 | `unsupported:FAILURE` | 7 | 21.0 | go:21.0 | py_re:7 |
| 35 | `unsupported-modifier:FIX,FPS,Microsoft,files,with` | 2 | 6.0 | go:6.0 | yara:2 |
| 36 | `unsupported-modifier:more` | 2 | 6.0 | go:6.0 | yara:2 |
| 37 | `unsupported-modifier:base64,base64wide` | 2 | 4.0 | triage-trial:4.0 | yara:2 |
| 38 | `s-flag` | 1 | 3.0 | go:3.0 | yara:1 |
| 39 | `unsupported-modifier:FPs,prone,to` | 1 | 3.0 | go:3.0 | yara:1 |
| 40 | `unsupported-modifier:a,and,be,in,mixed,quantifiers,regular,ungreedy` | 1 | 3.0 | go:3.0 | yara:1 |

## Corpus admission weighting

| decision | weight | rows | weighted sites |
|---|---|---|---|
| go | 3 | 123092 | 369276.0 |
| no-go | 1 | 535 | 535.0 |
| triage-trial | 2 | 1999 | 3998.0 |

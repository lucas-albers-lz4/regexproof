# Compiler feature-yield artifact (D5)

<!-- provenance: 71 triage files, inputs 7668b83f3974, 818 gate decisions -->

Sites unlocked per missing compiler feature, aggregated across
`properties/triage/*.ndjson` and weighted by corpus admission status
(GO=3, triage-trial=2, no-go=1). Sorted by weighted unlock value.

- Input files: 71
- Triage inputs hash: `7668b83f39740f0b`
- Gate decisions: 818
- Total unencodable rows: 46476
- Total weighted sites: 136614.0

| # | unencodable_reason | sites | weighted | per-corpus (decision:weighted) | top dialects |
|---|---|---|---|---|---|
| 1 | `fullword-boundary` | 31798 | 94887.0 | go:93873.0, triage-trial:1014.0 | yara:31798 |
| 2 | `composite-pattern` | 3956 | 11283.0 | go:10896.0, no-go:261.0, triage-trial:126.0 | py_re:3824, ecma:132 |
| 3 | `stateful` | 2770 | 7538.0 | go:5994.0, triage-trial:1544.0 | ecma:2770 |
| 4 | `word-boundary` | 1120 | 3175.0 | go:2871.0, no-go:22.0, triage-trial:282.0 | py_re:1016, ecma:76, pcre:21, re2:6 |
| 5 | `u-flag` | 962 | 2879.0 | go:2865.0, triage-trial:14.0 | ecma:962 |
| 6 | `lookaround` | 741 | 2102.0 | go:2007.0, no-go:49.0, triage-trial:46.0 | py_re:663, ecma:78 |
| 7 | `wide-non-literal` | 694 | 1988.0 | go:1800.0, triage-trial:188.0 | yara:694 |
| 8 | `unsupported:POSSESSIVE_REPEAT` | 466 | 1398.0 | go:1398.0 | py_re:466 |
| 9 | `m-flag` | 440 | 1250.0 | go:1185.0, no-go:25.0, triage-trial:40.0 | py_re:369, ecma:71 |
| 10 | `multi-match` | 434 | 1227.0 | go:1173.0, no-go:32.0, triage-trial:22.0 | py_re:434 |
| 11 | `negated-shorthand` | 420 | 1189.0 | go:1095.0, no-go:16.0, triage-trial:78.0 | py_re:242, ecma:175, re2:2, yara:1 |
| 12 | `backref` | 376 | 1075.0 | go:1044.0, no-go:25.0, triage-trial:6.0 | py_re:344, ecma:31, posix-shell:1 |
| 13 | `per-alternative-anchor` | 352 | 1005.0 | go:912.0, no-go:3.0, triage-trial:90.0 | ecma:187, posix-shell:91, py_re:69, re2:3 |
| 14 | `internal-anchor` | 320 | 921.0 | go:843.0, triage-trial:78.0 | posix-shell:312, ecma:7, pcre:1 |
| 15 | `unicode-not-literal` | 327 | 881.0 | go:735.0, no-go:18.0, triage-trial:128.0 | py_re:327 |
| 16 | `unsupported:ATOMIC_GROUP` | 276 | 828.0 | go:828.0 | py_re:276 |
| 17 | `pattern-too-long` | 276 | 804.0 | go:780.0, no-go:8.0, triage-trial:16.0 | py_re:165, pcre:72, yara:26, ecma:9 |
| 18 | `unsupported-modifier:base64` | 193 | 576.0 | go:570.0, triage-trial:6.0 | yara:193 |
| 19 | `inline-flag` | 125 | 337.0 | go:273.0, no-go:4.0, triage-trial:60.0 | re2:59, py_re:56, pcre:6, ecma:4 |
| 20 | `v-flag` | 93 | 276.0 | go:270.0, triage-trial:6.0 | ecma:93 |
| 21 | `parse-error` | 70 | 209.0 | go:207.0, triage-trial:2.0 | pcre:53, ecma:10, yara:7 |
| 22 | `parse-error:PatternError` | 60 | 176.0 | go:174.0, no-go:2.0 | py_re:60 |
| 23 | `gnu-extension` | 49 | 146.0 | go:144.0, triage-trial:2.0 | posix-shell:49 |
| 24 | `negated-class` | 40 | 120.0 | go:120.0 | pcre:32, py_re:8 |
| 25 | `bad-range` | 26 | 74.0 | go:66.0, triage-trial:8.0 | ecma:20, pcre:6 |
| 26 | `unsupported-syntax` | 23 | 65.0 | go:57.0, triage-trial:8.0 | ecma:12, posix-shell:11 |
| 27 | `repeat-count` | 15 | 45.0 | go:45.0 | yara:15 |
| 28 | `unclosed-group` | 14 | 42.0 | go:42.0 | ecma:8, posix-shell:6 |
| 29 | `empty-class` | 12 | 36.0 | go:36.0 | ecma:5, posix-shell:4, yara:3 |
| 30 | `unclosed-class` | 12 | 36.0 | go:36.0 | posix-shell:12 |
| 31 | `unsupported:FAILURE` | 7 | 21.0 | go:21.0 | py_re:7 |
| 32 | `unsupported-modifier:xor` | 6 | 18.0 | go:18.0 | yara:6 |
| 33 | `unsupported-modifier:base64,base64wide` | 2 | 4.0 | triage-trial:4.0 | yara:2 |
| 34 | `gnu-word-boundary` | 1 | 3.0 | go:3.0 | posix-shell:1 |

## Corpus admission weighting

| decision | weight | rows | weighted sites |
|---|---|---|---|
| go | 3 | 44127 | 132381.0 |
| no-go | 1 | 465 | 465.0 |
| triage-trial | 2 | 1884 | 3768.0 |

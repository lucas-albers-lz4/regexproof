# Compiler feature-yield artifact (D5)

<!-- provenance: 76 triage files, inputs ab87c527e59b, 825 gate decisions -->

Sites unlocked per missing compiler feature, aggregated across
`properties/triage/*.ndjson` and weighted by corpus admission status
(GO=3, triage-trial=2, no-go=1). Sorted by weighted unlock value.

- Input files: 76
- Triage inputs hash: `ab87c527e59b0b69`
- Gate decisions: 825
- Total unencodable rows: 46688
- Total weighted sites: 137155.0

| # | unencodable_reason | sites | weighted | per-corpus (decision:weighted) | top dialects |
|---|---|---|---|---|---|
| 1 | `fullword-boundary` | 31864 | 95019.0 | go:93873.0, triage-trial:1146.0 | yara:31864 |
| 2 | `composite-pattern` | 3975 | 11337.0 | go:10944.0, no-go:261.0, triage-trial:132.0 | py_re:3840, ecma:135 |
| 3 | `stateful` | 2770 | 7538.0 | go:5994.0, triage-trial:1544.0 | ecma:2770 |
| 4 | `word-boundary` | 1145 | 3230.0 | go:2886.0, no-go:22.0, triage-trial:322.0 | py_re:1041, ecma:76, pcre:21, re2:6 |
| 5 | `u-flag` | 963 | 2882.0 | go:2868.0, triage-trial:14.0 | ecma:963 |
| 6 | `lookaround` | 743 | 2108.0 | go:2013.0, no-go:49.0, triage-trial:46.0 | py_re:665, ecma:78 |
| 7 | `wide-non-literal` | 694 | 1988.0 | go:1800.0, triage-trial:188.0 | yara:694 |
| 8 | `unsupported:POSSESSIVE_REPEAT` | 466 | 1398.0 | go:1398.0 | py_re:466 |
| 9 | `m-flag` | 442 | 1256.0 | go:1191.0, no-go:25.0, triage-trial:40.0 | py_re:369, ecma:73 |
| 10 | `multi-match` | 435 | 1229.0 | go:1173.0, no-go:32.0, triage-trial:24.0 | py_re:435 |
| 11 | `negated-shorthand` | 423 | 1198.0 | go:1104.0, no-go:16.0, triage-trial:78.0 | py_re:245, ecma:175, re2:2, yara:1 |
| 12 | `backref` | 380 | 1087.0 | go:1056.0, no-go:25.0, triage-trial:6.0 | py_re:348, ecma:31, posix-shell:1 |
| 13 | `per-alternative-anchor` | 353 | 1008.0 | go:915.0, no-go:3.0, triage-trial:90.0 | ecma:187, posix-shell:91, py_re:70, re2:3 |
| 14 | `internal-anchor` | 320 | 921.0 | go:843.0, triage-trial:78.0 | posix-shell:312, ecma:7, pcre:1 |
| 15 | `unicode-not-literal` | 328 | 883.0 | go:735.0, no-go:18.0, triage-trial:130.0 | py_re:328 |
| 16 | `pattern-too-long` | 289 | 839.0 | go:807.0, no-go:8.0, triage-trial:24.0 | py_re:169, pcre:72, yara:26, ecma:18 |
| 17 | `unsupported:ATOMIC_GROUP` | 276 | 828.0 | go:828.0 | py_re:276 |
| 18 | `unsupported-modifier:base64` | 193 | 576.0 | go:570.0, triage-trial:6.0 | yara:193 |
| 19 | `inline-flag` | 125 | 337.0 | go:273.0, no-go:4.0, triage-trial:60.0 | re2:59, py_re:56, pcre:6, ecma:4 |
| 20 | `parse-error` | 110 | 329.0 | go:327.0, triage-trial:2.0 | pcre:53, ecma:50, yara:7 |
| 21 | `v-flag` | 93 | 276.0 | go:270.0, triage-trial:6.0 | ecma:93 |
| 22 | `parse-error:PatternError` | 60 | 176.0 | go:174.0, no-go:2.0 | py_re:60 |
| 23 | `gnu-extension` | 49 | 146.0 | go:144.0, triage-trial:2.0 | posix-shell:49 |
| 24 | `unsupported-syntax` | 43 | 125.0 | go:117.0, triage-trial:8.0 | ecma:32, posix-shell:11 |
| 25 | `negated-class` | 40 | 120.0 | go:120.0 | pcre:32, py_re:8 |
| 26 | `unclosed-group` | 27 | 81.0 | go:81.0 | ecma:21, posix-shell:6 |
| 27 | `bad-range` | 27 | 77.0 | go:69.0, triage-trial:8.0 | ecma:21, pcre:6 |
| 28 | `repeat-count` | 15 | 45.0 | go:45.0 | yara:15 |
| 29 | `empty-class` | 12 | 36.0 | go:36.0 | ecma:5, posix-shell:4, yara:3 |
| 30 | `unclosed-class` | 12 | 36.0 | go:36.0 | posix-shell:12 |
| 31 | `unsupported:FAILURE` | 7 | 21.0 | go:21.0 | py_re:7 |
| 32 | `unsupported-modifier:xor` | 6 | 18.0 | go:18.0 | yara:6 |
| 33 | `unsupported-modifier:base64,base64wide` | 2 | 4.0 | triage-trial:4.0 | yara:2 |
| 34 | `gnu-word-boundary` | 1 | 3.0 | go:3.0 | posix-shell:1 |

## Corpus admission weighting

| decision | weight | rows | weighted sites |
|---|---|---|---|
| go | 3 | 44244 | 132732.0 |
| no-go | 1 | 465 | 465.0 |
| triage-trial | 2 | 1979 | 3958.0 |

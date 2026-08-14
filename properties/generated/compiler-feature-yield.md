# Compiler feature-yield artifact (D5)

<!-- provenance: 71 triage files, inputs 5f1c04e7976a, 825 gate decisions -->

Sites unlocked per missing compiler feature, aggregated across
`properties/triage/*.ndjson` and weighted by corpus admission status
(GO=3, triage-trial=2, no-go=1). Sorted by weighted unlock value.

- Input files: 71
- Triage inputs hash: `5f1c04e7976a7337`
- Gate decisions: 825
- Total unencodable rows: 46565
- Total weighted sites: 136881.0

| # | unencodable_reason | sites | weighted | per-corpus (decision:weighted) | top dialects |
|---|---|---|---|---|---|
| 1 | `fullword-boundary` | 31798 | 94887.0 | go:93873.0, triage-trial:1014.0 | yara:31798 |
| 2 | `composite-pattern` | 3959 | 11292.0 | go:10905.0, no-go:261.0, triage-trial:126.0 | py_re:3824, ecma:135 |
| 3 | `stateful` | 2770 | 7538.0 | go:5994.0, triage-trial:1544.0 | ecma:2770 |
| 4 | `word-boundary` | 1120 | 3175.0 | go:2871.0, no-go:22.0, triage-trial:282.0 | py_re:1016, ecma:76, pcre:21, re2:6 |
| 5 | `u-flag` | 963 | 2882.0 | go:2868.0, triage-trial:14.0 | ecma:963 |
| 6 | `lookaround` | 741 | 2102.0 | go:2007.0, no-go:49.0, triage-trial:46.0 | py_re:663, ecma:78 |
| 7 | `wide-non-literal` | 694 | 1988.0 | go:1800.0, triage-trial:188.0 | yara:694 |
| 8 | `unsupported:POSSESSIVE_REPEAT` | 466 | 1398.0 | go:1398.0 | py_re:466 |
| 9 | `m-flag` | 442 | 1256.0 | go:1191.0, no-go:25.0, triage-trial:40.0 | py_re:369, ecma:73 |
| 10 | `multi-match` | 434 | 1227.0 | go:1173.0, no-go:32.0, triage-trial:22.0 | py_re:434 |
| 11 | `negated-shorthand` | 420 | 1189.0 | go:1095.0, no-go:16.0, triage-trial:78.0 | py_re:242, ecma:175, re2:2, yara:1 |
| 12 | `backref` | 376 | 1075.0 | go:1044.0, no-go:25.0, triage-trial:6.0 | py_re:344, ecma:31, posix-shell:1 |
| 13 | `per-alternative-anchor` | 352 | 1005.0 | go:912.0, no-go:3.0, triage-trial:90.0 | ecma:187, posix-shell:91, py_re:69, re2:3 |
| 14 | `internal-anchor` | 320 | 921.0 | go:843.0, triage-trial:78.0 | posix-shell:312, ecma:7, pcre:1 |
| 15 | `unicode-not-literal` | 327 | 881.0 | go:735.0, no-go:18.0, triage-trial:128.0 | py_re:327 |
| 16 | `pattern-too-long` | 285 | 831.0 | go:807.0, no-go:8.0, triage-trial:16.0 | py_re:165, pcre:72, yara:26, ecma:18 |
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
| go | 3 | 44216 | 132648.0 |
| no-go | 1 | 465 | 465.0 |
| triage-trial | 2 | 1884 | 3768.0 |

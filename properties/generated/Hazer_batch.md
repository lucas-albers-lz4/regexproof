---
schema_version: "1"
corpus: Hazer
findings: 132
---

# Hazer batch findings

## intent_mismatch:0151539a07d0ca21404871d2d07941d4:email

```yaml
regex_id: 0151539a07d0ca21404871d2d07941d4
schema_version: "1"
kind: intent_mismatch
corpus: Hazer
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/email/feedparser.py:37:11"
```

### Pattern

`^(From |[\041-\071\073-\176]*:|[\t ])`

### Context

```json
{"admitted_char": "' '", "keyword": "email", "reason": "name/comment claims validation but pattern admits excluded char"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0151539a07d0ca21404871d2d07941d4:search

```yaml
regex_id: 0151539a07d0ca21404871d2d07941d4
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/email/feedparser.py:37:11"
```

### Pattern

`^(From |[\041-\071\073-\176]*:|[\t ])`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0172bd81786b27138322ddedacc6455b:match

```yaml
regex_id: 0172bd81786b27138322ddedacc6455b
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:766:24"
```

### Pattern

`^x{3,4}?$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:017bccb234d4caa870a1b781f4c3d478:match

```yaml
regex_id: 017bccb234d4caa870a1b781f4c3d478
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:768:26"
```

### Pattern

`^x{}$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:06ea9be57d3d03e2ce231cd1e2e4ad51:match

```yaml
regex_id: 06ea9be57d3d03e2ce231cd1e2e4ad51
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:742:26"
```

### Pattern

`^(\w){1,2}?$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:09275c94a2a4a6c41099fffd3fe26d44:search

```yaml
regex_id: 09275c94a2a4a6c41099fffd3fe26d44
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/urllib/request.py:268:15"
```

### Pattern

`:\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0a8ae96decee93f682c28b028a3ffb69:search

```yaml
regex_id: 0a8ae96decee93f682c28b028a3ffb69
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/doctest.py:767:27"
```

### Pattern

`#\s*doctest:\s*([^\n\'"]*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0ae2a2f9641f45e9c8dd813b800b7582:match

```yaml
regex_id: 0ae2a2f9641f45e9c8dd813b800b7582
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:2540:24"
```

### Pattern

`^x{3}+$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0af8de339e42f6c3b1e76fb8156bde28:match

```yaml
regex_id: 0af8de339e42f6c3b1e76fb8156bde28
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:643:25"
```

### Pattern

`^(?:(a)|c)((?(1)b|d))$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0cceec5c0aca40d2a976ccbdb56e88d8:search

```yaml
regex_id: 0cceec5c0aca40d2a976ccbdb56e88d8
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Tools/c-analyzer/c_parser/preprocessor/gcc.py:37:23"
```

### Pattern

`^\s*#\s*(\w+)\b.*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0cfc1e39c50ccc4ba34c41a2ac037d77:search

```yaml
regex_id: 0cfc1e39c50ccc4ba34c41a2ac037d77
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:632:12"
```

### Pattern

`.*?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0d4b05bdc33b4df1e020aa326fc88e79:search

```yaml
regex_id: 0d4b05bdc33b4df1e020aa326fc88e79
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/http/cookiejar.py:1260:15"
```

### Pattern

`^\#LWP-Cookies-(\d+\.\d+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0dd0616e80a59d002dc163d0f6d0c81b:match

```yaml
regex_id: 0dd0616e80a59d002dc163d0f6d0c81b
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:755:26"
```

### Pattern

`^x{1,2}$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0de8512fdee7171797c39f46989b01d3:search

```yaml
regex_id: 0de8512fdee7171797c39f46989b01d3
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/logging/config.py:377:18"
```

### Pattern

`^\.\s*(\w+)\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:115493127f1d30d60859bd53794542fc:match

```yaml
regex_id: 115493127f1d30d60859bd53794542fc
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:718:25"
```

### Pattern

`^(?:(a)|c)(\1)?$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:12f051b70d1b30d7dcc3fe1798774020:match

```yaml
regex_id: 12f051b70d1b30d7dcc3fe1798774020
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:756:26"
```

### Pattern

`^x{1,2}?$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:19322b32487e02bf9a9ea2a5e3783bce:search

```yaml
regex_id: 19322b32487e02bf9a9ea2a5e3783bce
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/logging/config.py:378:20"
```

### Pattern

`^\[([^\[\]]*)\]\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1aa0360a9671318353927ef0860c00ad:match

```yaml
regex_id: 1aa0360a9671318353927ef0860c00ad
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:762:24"
```

### Pattern

`^x{3,4}?$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1b306ea6b316dbf1eb510cbbabe2b22c:match

```yaml
regex_id: 1b306ea6b316dbf1eb510cbbabe2b22c
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:765:24"
```

### Pattern

`^x{1,4}?$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1c5add1a229030ebd06b7b1817fba59d:search

```yaml
regex_id: 1c5add1a229030ebd06b7b1817fba59d
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/http/cookiejar.py:344:25"
```

### Pattern

`^\s*([^=\s;,]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:20ca3eb72abfbeda651ced7cb81adcd8:search

```yaml
regex_id: 20ca3eb72abfbeda651ced7cb81adcd8
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:1849:18"
```

### Pattern

`$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:22e9f3324ac6068b10fc158c7b3a69d4:search

```yaml
regex_id: 22e9f3324ac6068b10fc158c7b3a69d4
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/http/cookiejar.py:206:17"
```

### Pattern

`^[SMTWF][a-z][a-z], (\d\d) ([JFMASOND][a-z][a-z]) (\d\d\d\d) (\d\d):(\d\d):(\d\d) GMT$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:262315789b68f80791ec38b1513717db:match

```yaml
regex_id: 262315789b68f80791ec38b1513717db
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/idlelib/format.py:181:11"
```

### Pattern

`^\s*$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:27e92945185c54d14780608bbfc1777f:match

```yaml
regex_id: 27e92945185c54d14780608bbfc1777f
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:754:26"
```

### Pattern

`^x{1}?$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:289f36ee4826b780505548d3791f9bd2:search

```yaml
regex_id: 289f36ee4826b780505548d3791f9bd2
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/idlelib/pyshell.py:1340:35"
```

### Pattern

`^([ \t]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2a048dc103e096694b0e2eed3e3bba4f:search

```yaml
regex_id: 2a048dc103e096694b0e2eed3e3bba4f
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/http/cookiejar.py:211:21"
```

### Pattern

`^
    (\d\d?)            # day
       (?:\s+|[-\/])
    (\w+)              # month
        (?:\s+|[-\/])
    (\d+)              # year
    (?:
          (?:\s+|:)    # separator before clock
       (\d\d?):(\d\d)  # hour:min
       (?::(\d\d))?    # optional seconds
    )?                 # optional clock
       \s*
    (?:
       ([-+]?\d{2,4}|(?![APap][Mm]\b)[A-Za-z]+) # timezone
       \s*
    )?
    (?:
       \(\w+\)         # ASCII representation of timezone in parens.
       \s*
    )?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2c690186e0cdf5dc66eeae922c8f6d13:search

```yaml
regex_id: 2c690186e0cdf5dc66eeae922c8f6d13
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Android/android.py:146:20"
```

### Pattern

`^(declare -x |export )?(\w+)=['"]?(.*?)['"]?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2fbf01bcb307e4f5c158448fe5f3c02c:search

```yaml
regex_id: 2fbf01bcb307e4f5c158448fe5f3c02c
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_smtplib.py:544:17"
```

### Pattern

`^sender: foo@bar.com$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:30b2940fee5f3ae491371967ab80b419:match

```yaml
regex_id: 30b2940fee5f3ae491371967ab80b419
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:2535:25"
```

### Pattern

`^(\w){1,4}+$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:30e5c2368336955ef7ce659d9298a52d:search

```yaml
regex_id: 30e5c2368336955ef7ce659d9298a52d
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Tools/c-analyzer/c_parser/preprocessor/gcc.py:36:17"
```

### Pattern

`^# (\d+) "([^"]+)"((?: [1234])*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:3343636ad07dc602bf653dbf2c3f3575:email

```yaml
regex_id: 3343636ad07dc602bf653dbf2c3f3575
schema_version: "1"
kind: intent_mismatch
corpus: Hazer
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/email/header.py:35:7"
```

### Pattern

`
  =\?                   # literal =?
  (?P<charset>[^?]*?)   # non-greedy up to the next ? is the charset
  \?                    # literal ?
  (?P<encoding>[qQbB])  # either a "q" or a "b", case insensitive
  \?                    # literal ?
  (?P<encoded>.*?)      # non-greedy up to the next ?= is the encoded string
  \?=                   # literal ?=
  `

### Context

```json
{"admitted_char": "'\\n'", "keyword": "email", "reason": "name/comment claims validation but pattern admits excluded char"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:373f970bf460b27267e2f95f45469077:match

```yaml
regex_id: 373f970bf460b27267e2f95f45469077
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:763:24"
```

### Pattern

`^x{3}?$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3b2767636ba3947f289a71c614649dae:match

```yaml
regex_id: 3b2767636ba3947f289a71c614649dae
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:2541:24"
```

### Pattern

`^x{1,3}+$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3b73a21318de242fbcdad1e4ea0b1167:search

```yaml
regex_id: 3b73a21318de242fbcdad1e4ea0b1167
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/logging/config.py:379:20"
```

### Pattern

`^\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3bc1db3c8a7ff3ec8179e18cc6728153:match

```yaml
regex_id: 3bc1db3c8a7ff3ec8179e18cc6728153
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:2531:26"
```

### Pattern

`^(\w){1,2}+$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3fd642751f002d4de3b0ffbe463fc8f2:match

```yaml
regex_id: 3fd642751f002d4de3b0ffbe463fc8f2
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:745:25"
```

### Pattern

`^(\w){1,3}$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:42b9a96de863ce2dde73af1e2c56230d:search

```yaml
regex_id: 42b9a96de863ce2dde73af1e2c56230d
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/http/cookiejar.py:135:14"
```

### Pattern

`^([-+])?(\d\d?):?(\d\d)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:42f07fa3bc822ed3bbf89854fe683902:search

```yaml
regex_id: 42f07fa3bc822ed3bbf89854fe683902
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/http/cookiejar.py:346:25"
```

### Pattern

`^\s*=\s*([^\s;,]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:45f9d1bfdbc55adfa437300b0906c695:match

```yaml
regex_id: 45f9d1bfdbc55adfa437300b0906c695
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:642:26"
```

### Pattern

`^(\()?([^()]+)(?(1)\))$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:489a630307a202a7147c26a73a70f155:match

```yaml
regex_id: 489a630307a202a7147c26a73a70f155
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:712:25"
```

### Pattern

`^(\|)?([^()]+)\1?$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4968c86f3db96cb301b8f6628794218a:match

```yaml
regex_id: 4968c86f3db96cb301b8f6628794218a
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:750:25"
```

### Pattern

`^(\w){1,4}?$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4a934b3b0fd8a7cc4270e7b4ee1094ba:search

```yaml
regex_id: 4a934b3b0fd8a7cc4270e7b4ee1094ba
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/http/cookiejar.py:288:14"
```

### Pattern

`^
    (\d{4})              # year
       [-\/]?
    (\d\d?)              # numerical month
       [-\/]?
    (\d\d?)              # day
   (?:
         (?:\s+|[-:Tt])  # separator before clock
      (\d\d?):?(\d\d)    # hour:min
      (?::?(\d\d(?:\.\d*)?))?  # optional seconds (and fractional)
   )?                    # optional clock
      \s*
   (?:
      ([-+]?\d\d?:?(:?\d\d)?
       |Z|z)             # timezone  (Z is "zero meridian", i.e. GMT)
      \s*
   )?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:502b21a6638f8bd18b4d029af4bfc70b:match

```yaml
regex_id: 502b21a6638f8bd18b4d029af4bfc70b
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:641:26"
```

### Pattern

`^(\()?([^()]+)(?(1)\))$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:54dafa59c2aefe22825d92d108ba0898:search

```yaml
regex_id: 54dafa59c2aefe22825d92d108ba0898
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/_pydecimal.py:6117:13"
```

### Pattern

`0*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:56bc3470e6b5eeec8bea2fafc0c8d264:search

```yaml
regex_id: 56bc3470e6b5eeec8bea2fafc0c8d264
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_smtplib.py:574:17"
```

### Pattern

`^sender: foo@bar.com$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:56d3448ca646f11a019769453e13dec6:match

```yaml
regex_id: 56d3448ca646f11a019769453e13dec6
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:758:24"
```

### Pattern

`^x{3}$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:56fc8d17512e909747427666a19916ae:search

```yaml
regex_id: 56fc8d17512e909747427666a19916ae
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/doctest.py:798:17"
```

### Pattern

`^([ ]*)(?=\S)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5c6ff9f3c922307c322f1ca0e47d514c:match

```yaml
regex_id: 5c6ff9f3c922307c322f1ca0e47d514c
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:739:26"
```

### Pattern

`^(\w){1}$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5e7316c61c55cae276591f16d1914365:search

```yaml
regex_id: 5e7316c61c55cae276591f16d1914365
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:1443:28"
```

### Pattern

`^pattern$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5fac32f87e14138986e2fa6625e247da:search

```yaml
regex_id: 5fac32f87e14138986e2fa6625e247da
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:807:26"
```

### Pattern

`^\Aabc\z$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5feed09f6db5d143bce81a1704b50fff:match

```yaml
regex_id: 5feed09f6db5d143bce81a1704b50fff
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:715:26"
```

### Pattern

`^(\|)?([^()]+)\1$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:63f089d00cff5088d4b97b55ba12d5ad:search

```yaml
regex_id: 63f089d00cff5088d4b97b55ba12d5ad
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_unittest/test_case.py:1540:46"
```

### Pattern

`expect$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6713f3e1298c9cc569975a1b7117fe89:match

```yaml
regex_id: 6713f3e1298c9cc569975a1b7117fe89
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:2538:26"
```

### Pattern

`^x{1,2}+$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6904d76badc041faf091056c1a3250e3:match

```yaml
regex_id: 6904d76badc041faf091056c1a3250e3
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:769:24"
```

### Pattern

`^x{}$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:69e9e49fe5dfcd094485b0b8df7680c5:match

```yaml
regex_id: 69e9e49fe5dfcd094485b0b8df7680c5
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:2534:25"
```

### Pattern

`^(\w){1,3}+$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6b6fb485a85a0a783f66b0a312a6117d:match

```yaml
regex_id: 6b6fb485a85a0a783f66b0a312a6117d
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:637:25"
```

### Pattern

`^(\()?([^()]+)(?(1)\))$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6d4058b641b759e0f78a30fb45d8542a:match

```yaml
regex_id: 6d4058b641b759e0f78a30fb45d8542a
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:2545:24"
```

### Pattern

`^x{}+$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:70afbfb4c8510b0255c644b92c01466c:search

```yaml
regex_id: 70afbfb4c8510b0255c644b92c01466c
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/doctest.py:1525:30"
```

### Pattern

`<doctest (?P<name>.+)\[(?P<examplenum>\d+)\]>$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:70d1ac828b3f274a80ed852cd559150c:match

```yaml
regex_id: 70d1ac828b3f274a80ed852cd559150c
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:716:25"
```

### Pattern

`^(?:(a)|c)(\1)$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:71456da98e751959f598306f0c6e74f1:search

```yaml
regex_id: 71456da98e751959f598306f0c6e74f1
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:1844:18"
```

### Pattern

`$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7150041708f35c80ab352edff11a32a3:match

```yaml
regex_id: 7150041708f35c80ab352edff11a32a3
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:748:25"
```

### Pattern

`^(\w){3}?$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7188133cab7229d259f16dd2ce133d18:match

```yaml
regex_id: 7188133cab7229d259f16dd2ce133d18
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:751:25"
```

### Pattern

`^(\w){3,4}?$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:74ae74ca249268e5655ad54fd3586069:match

```yaml
regex_id: 74ae74ca249268e5655ad54fd3586069
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:645:25"
```

### Pattern

`^(?:(a)|c)((?(1)b|d))$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:75a756e15200e42a75fc9433fbfb4e9d:match

```yaml
regex_id: 75a756e15200e42a75fc9433fbfb4e9d
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:639:25"
```

### Pattern

`^(\()?([^()]+)(?(1)\))$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:77a8ffe3ebadf153f81a94719cfb5360:match

```yaml
regex_id: 77a8ffe3ebadf153f81a94719cfb5360
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:746:25"
```

### Pattern

`^(\w){1,4}$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7914a435bc1cc2e6b862076b2f23b937:match

```yaml
regex_id: 7914a435bc1cc2e6b862076b2f23b937
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:2533:25"
```

### Pattern

`^(\w){3}+$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:7930f6be65ba213a8e5e5c6ed3d6de8f:email

```yaml
regex_id: 7930f6be65ba213a8e5e5c6ed3d6de8f
schema_version: "1"
kind: intent_mismatch
corpus: Hazer
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/email/feedparser.py:40:16"
```

### Pattern

`(?P<end>--)?(?P<ws>[ \t]*)(?P<linesep>\r\n|\r|\n)?$`

### Context

```json
{"admitted_char": "' '", "keyword": "email", "reason": "name/comment claims validation but pattern admits excluded char"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7930f6be65ba213a8e5e5c6ed3d6de8f:search

```yaml
regex_id: 7930f6be65ba213a8e5e5c6ed3d6de8f
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/email/feedparser.py:40:16"
```

### Pattern

`(?P<end>--)?(?P<ws>[ \t]*)(?P<linesep>\r\n|\r|\n)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7af93425649b3ca69c846ebd47aeaae2:search

```yaml
regex_id: 7af93425649b3ca69c846ebd47aeaae2
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/idlelib/pyshell.py:1339:35"
```

### Pattern

`^([ \t]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:803bfd5b8a6e4b11a15107eeb7fdcb8a:match

```yaml
regex_id: 803bfd5b8a6e4b11a15107eeb7fdcb8a
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:747:25"
```

### Pattern

`^(\w){3,4}?$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:831f6276175b58deec95c73c8541ba6e:search

```yaml
regex_id: 831f6276175b58deec95c73c8541ba6e
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_smtplib.py:635:17"
```

### Pattern

`^sender: the_rescuers@Rescue-Aid-Society.com$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:851720613cdaee2b432478f79337be67:match

```yaml
regex_id: 851720613cdaee2b432478f79337be67
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:1769:30"
```

### Pattern

`^\d$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:854a7fa084088fcff305ff89aa159a4c:search

```yaml
regex_id: 854a7fa084088fcff305ff89aa159a4c
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/logging/config.py:374:22"
```

### Pattern

`^(?P<prefix>[a-z]+)://(?P<suffix>.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:85bd8397cb318988687e5b77445ade72:search

```yaml
regex_id: 85bd8397cb318988687e5b77445ade72
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:805:25"
```

### Pattern

`^abc$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:86bb003ba843c39976fdd528b78d18d9:search

```yaml
regex_id: 86bb003ba843c39976fdd528b78d18d9
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_smtplib.py:603:17"
```

### Pattern

`^sender: joe@example.com$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:8b0b7932b191293d0dadecf34c26b7ee:email

```yaml
regex_id: 8b0b7932b191293d0dadecf34c26b7ee
schema_version: "1"
kind: intent_mismatch
corpus: Hazer
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_email/test_email.py:5807:17"
```

### Pattern

`^--([^\n]+)\n(.*?)\n--\1$`

### Context

```json
{"admitted_char": "'\\n'", "keyword": "email", "reason": "name/comment claims validation but pattern admits excluded char"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8b0b7932b191293d0dadecf34c26b7ee:search

```yaml
regex_id: 8b0b7932b191293d0dadecf34c26b7ee
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_email/test_email.py:5807:17"
```

### Pattern

`^--([^\n]+)\n(.*?)\n--\1$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8b6dfa4b0b0c6b7a88612a24a4b44b6e:search

```yaml
regex_id: 8b6dfa4b0b0c6b7a88612a24a4b44b6e
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/email/utils.py:392:23"
```

### Pattern

`^(?P<name>\w+)\*((?P<num>[0-9]+)\*?)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:8b75ac00a775947e364fca337cb16e09:email

```yaml
regex_id: 8b75ac00a775947e364fca337cb16e09
schema_version: "1"
kind: intent_mismatch
corpus: Hazer
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/email/generator.py:23:7"
```

### Pattern

`^From `

### Context

```json
{"admitted_char": "' '", "keyword": "email", "reason": "name/comment claims validation but pattern admits excluded char"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8b75ac00a775947e364fca337cb16e09:search

```yaml
regex_id: 8b75ac00a775947e364fca337cb16e09
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/email/generator.py:23:7"
```

### Pattern

`^From `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8e90ab4d55984e4a6f457c9129210733:match

```yaml
regex_id: 8e90ab4d55984e4a6f457c9129210733
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:749:25"
```

### Pattern

`^(\w){1,3}?$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:901ddf85c09af948d9b5de8e2a358cbb:match

```yaml
regex_id: 901ddf85c09af948d9b5de8e2a358cbb
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:740:26"
```

### Pattern

`^(\w){1}?$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:90b4f913a7aba547f780f138b54711cd:email

```yaml
regex_id: 90b4f913a7aba547f780f138b54711cd
schema_version: "1"
kind: intent_mismatch
corpus: Hazer
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/email/_header_value_parser.py:116:18"
```

### Pattern

`
   =\?            # literal =?
   [^?]*          # charset
   \?             # literal ?
   [qQbB]         # literal 'q' or 'b', case insensitive
   \?             # literal ?
  .*?             # encoded word
  \?=             # literal ?=
`

### Context

```json
{"admitted_char": "'\\n'", "keyword": "email", "reason": "name/comment claims validation but pattern admits excluded char"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:92a110bb1dbb744db90de98d9b841a7d:search

```yaml
regex_id: 92a110bb1dbb744db90de98d9b841a7d
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/logging/__init__.py:480:17"
```

### Pattern

`^(\d+|\w+)(\.\w+|\[[^]]+\])*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9326dc2afcc7723539c25d2cf8245f85:search

```yaml
regex_id: 9326dc2afcc7723539c25d2cf8245f85
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:809:26"
```

### Pattern

`^\Aabc\Z$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:93a2bdfa5eab4c9bb5c57c719e423935:match

```yaml
regex_id: 93a2bdfa5eab4c9bb5c57c719e423935
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:649:25"
```

### Pattern

`^(?:(a)|c)((?(1)|d))$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:93a7ab34db50889f5ed40a23b0a729a4:search

```yaml
regex_id: 93a7ab34db50889f5ed40a23b0a729a4
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/http/cookiejar.py:345:25"
```

### Pattern

`^\s*=\s*\"([^\"\\]*(?:\\.[^\"\\]*)*)\"`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9cbb9dd197703ccc7897199d8ac8a709:match

```yaml
regex_id: 9cbb9dd197703ccc7897199d8ac8a709
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:1760:29"
```

### Pattern

`^\d$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9e910893abf284d4a57ee723340ce5c1:search

```yaml
regex_id: 9e910893abf284d4a57ee723340ce5c1
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_smtplib.py:609:16"
```

### Pattern

`^recips: .*'foo@example.net'.*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a2e5f5745c3cdb48888e716a31026134:search

```yaml
regex_id: a2e5f5745c3cdb48888e716a31026134
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_smtplib.py:148:19"
```

### Pattern

`^connect:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a3b706546b3a092df532d8ba8356f992:match

```yaml
regex_id: a3b706546b3a092df532d8ba8356f992
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:647:25"
```

### Pattern

`^(?:(a)|c)((?(1)|d))$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a646697da4b933ea3296a80173ce3d66:search

```yaml
regex_id: a646697da4b933ea3296a80173ce3d66
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_smtplib.py:491:17"
```

### Pattern

`^sender: <>$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a7efea761e3f6801ae38add5bb5746ab:match

```yaml
regex_id: a7efea761e3f6801ae38add5bb5746ab
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:764:24"
```

### Pattern

`^x{1,3}?$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:aaba817122674ffddf3778864b6167ea:match

```yaml
regex_id: aaba817122674ffddf3778864b6167ea
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:744:25"
```

### Pattern

`^(\w){3}$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ae3f34e67ea26bc2a900bee7c569fd49:match

```yaml
regex_id: ae3f34e67ea26bc2a900bee7c569fd49
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:761:24"
```

### Pattern

`^x{1,4}$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:af5c43f686ffc6db9c33bd05e588e492:search

```yaml
regex_id: af5c43f686ffc6db9c33bd05e588e492
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_pyrepl/test_pyrepl.py:1672:24"
```

### Pattern

`^'.*calx.py'$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b3183e5501427ef3cc6722c4db3faae5:search

```yaml
regex_id: b3183e5501427ef3cc6722c4db3faae5
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/http/cookiejar.py:620:14"
```

### Pattern

`:\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b3b5b45a80d4adbab2ec3ba65724164a:match

```yaml
regex_id: b3b5b45a80d4adbab2ec3ba65724164a
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:753:26"
```

### Pattern

`^x{1}$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b678d95b1511846435e605ed3b28830f:match

```yaml
regex_id: b678d95b1511846435e605ed3b28830f
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:2537:26"
```

### Pattern

`^x{1}+$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b7f19daaa06008f0f527fe2bcb18f6ce:search

```yaml
regex_id: b7f19daaa06008f0f527fe2bcb18f6ce
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/doctest.py:649:27"
```

### Pattern

`^[ ]*(#.*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b82f88abff58145ac027822a622701fe:search

```yaml
regex_id: b82f88abff58145ac027822a622701fe
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/http/cookiejar.py:209:13"
```

### Pattern

`^(?:Sun|Mon|Tue|Wed|Thu|Fri|Sat)[a-z]*,?\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b886b9735bb0648cfda8d9f67ad9580c:search

```yaml
regex_id: b886b9735bb0648cfda8d9f67ad9580c
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_unittest/test_case.py:1602:16"
```

### Pattern

`^Expected$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bc1d3a8926b59a8e3839c5030c94f753:search

```yaml
regex_id: bc1d3a8926b59a8e3839c5030c94f753
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/http/cookiejar.py:1258:14"
```

### Pattern

`^\.+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bc3b50f2b338e9db110ff6ba52c7333f:search

```yaml
regex_id: bc3b50f2b338e9db110ff6ba52c7333f
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_regrtest.py:1419:16"
```

### Pattern

`^(test[^ ]+).*ok$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c00dc246aaf49e7571e0d7c3b0f434e9:search

```yaml
regex_id: c00dc246aaf49e7571e0d7c3b0f434e9
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/http/cookiejar.py:535:10"
```

### Pattern

`\.\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c311555c0d85ee15cbe79734e0fc423e:match

```yaml
regex_id: c311555c0d85ee15cbe79734e0fc423e
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:2544:26"
```

### Pattern

`^x{}+$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c42feae31da27f41c4ca8c67e0a5ec18:search

```yaml
regex_id: c42feae31da27f41c4ca8c67e0a5ec18
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_smtplib.py:672:17"
```

### Pattern

`^sender: holy@grail.net$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c6c0fa3caa2466ea026df6f11b266cb0:match

```yaml
regex_id: c6c0fa3caa2466ea026df6f11b266cb0
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:714:26"
```

### Pattern

`^(\|)?([^()]+)\1$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c7aa057c4ce6c64c6bfbdb95973eeea9:match

```yaml
regex_id: c7aa057c4ce6c64c6bfbdb95973eeea9
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:2542:24"
```

### Pattern

`^x{1,4}+$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cebff5347678eb881a30afcd67d381d6:search

```yaml
regex_id: cebff5347678eb881a30afcd67d381d6
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:2040:12"
```

### Pattern

`$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d0495b9b9f371b712cb10eb4b57403e0:search

```yaml
regex_id: d0495b9b9f371b712cb10eb4b57403e0
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_pyrepl/test_pyrepl.py:1682:24"
```

### Pattern

`^'.*calx.py'$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d281e06f3729b160eb0223e36c83fafc:search

```yaml
regex_id: d281e06f3729b160eb0223e36c83fafc
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/email/header.py:48:7"
```

### Pattern

`[\041-\176]+:$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d2e0496766c0b50b018ce94a703e95b8:search

```yaml
regex_id: d2e0496766c0b50b018ce94a703e95b8
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_smtplib.py:158:19"
```

### Pattern

`^\d{2}:\d{2}:\d{2}\.\d{6} connect: `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d61f33f95c0d2096e6df5f87c28bc727:search

```yaml
regex_id: d61f33f95c0d2096e6df5f87c28bc727
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:808:25"
```

### Pattern

`^\Aabc\Z$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d6ebcb4a90e634e5821a6e024769fe50:search

```yaml
regex_id: d6ebcb4a90e634e5821a6e024769fe50
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/platform.py:1347:22"
```

### Pattern

`^(?P<name>[a-zA-Z0-9_]+)=(?P<quote>["']?)(?P<value>.*)(?P=quote)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d8a13244f3e212348b39688a7bb07429:search

```yaml
regex_id: d8a13244f3e212348b39688a7bb07429
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/logging/config.py:376:19"
```

### Pattern

`^\s*(\w+)\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:df22dbf3a6f16904d7992267effe0046:search

```yaml
regex_id: df22dbf3a6f16904d7992267effe0046
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/logging/config.py:294:13"
```

### Pattern

`^[a-z_][a-z0-9_]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e02e1bc82ecdf0fcf7de5c40efd3d249:search

```yaml
regex_id: e02e1bc82ecdf0fcf7de5c40efd3d249
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:806:25"
```

### Pattern

`^\Aabc\z$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e0d892139c5505c37811eb9105d2f6cb:search

```yaml
regex_id: e0d892139c5505c37811eb9105d2f6cb
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Doc/tools/extensions/misc_news.py:33:38"
```

### Pattern

`^what's new in (.*?)\??$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e4006b71798bac490aac13084fab83d0:match

```yaml
regex_id: e4006b71798bac490aac13084fab83d0
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:710:25"
```

### Pattern

`^(\|)?([^()]+)\1$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e4e08959163ab90e2d2ae1032142360a:match

```yaml
regex_id: e4e08959163ab90e2d2ae1032142360a
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:2530:26"
```

### Pattern

`^(\w){1}+$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e65c8c53e915d21c45039341f3adbf62:match

```yaml
regex_id: e65c8c53e915d21c45039341f3adbf62
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:760:24"
```

### Pattern

`^x{3,3}$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:eaf2d313b234316a4a4160b891b9ed29:search

```yaml
regex_id: eaf2d313b234316a4a4160b891b9ed29
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/_pydecimal.py:6118:14"
```

### Pattern

`50*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ec1d9d1edb9df28c4817e435a2ac63ad:match

```yaml
regex_id: ec1d9d1edb9df28c4817e435a2ac63ad
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:741:26"
```

### Pattern

`^(\w){1,2}$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f380c286c89dc2237fe2f69effc22a89:match

```yaml
regex_id: f380c286c89dc2237fe2f69effc22a89
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/test/test_re.py:759:24"
```

### Pattern

`^x{1,3}$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f965f610d8e377a9ba9ebc40a71454c6:search

```yaml
regex_id: f965f610d8e377a9ba9ebc40a71454c6
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/configparser.py:1367:16"
```

### Pattern

`^get(?P<name>.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fcec2ac13826e0ef16d984ca38a3c413:search

```yaml
regex_id: fcec2ac13826e0ef16d984ca38a3c413
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/pydoc.py:192:14"
```

### Pattern

` at 0x[0-9a-f]{6,16}(>+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ff14af03bedddfaee12c995c8a0c0a74:search

```yaml
regex_id: ff14af03bedddfaee12c995c8a0c0a74
schema_version: "1"
kind: usage_mismatch
corpus: Hazer
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/Hazer/rules/Lib/logging/__init__.py:479:15"
```

### Pattern

`^(.?[<>=^])?[+ -]?#?0?(\d+|{\w+})?[,_]?(\.(\d+|{\w+}))?[bcdefgnosx%]?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## property:inventory:rc-shape1-injection-alphabet:rc-shape1-injection-alphabet

```yaml
regex_id: "inventory:rc-shape1-injection-alphabet"
schema_version: "1"
kind: property
corpus: Hazer
shape: 1
result: planned
disclosure: null
site: "inventory:rc-shape1-injection-alphabet"
```

### Pattern

``

### Context

```json
{"question_id": "rc-shape1-injection-alphabet", "threat": "Rule language admits control/injection characters unexpected for a secret token"}
```

### Witness

```json
null
```

### Ground-truth

None

## property:inventory:rc-shape2-missing-keyword:rc-shape2-missing-keyword

```yaml
regex_id: "inventory:rc-shape2-missing-keyword"
schema_version: "1"
kind: property
corpus: Hazer
shape: 2
result: planned
disclosure: null
site: "inventory:rc-shape2-missing-keyword"
```

### Pattern

``

### Context

```json
{"question_id": "rc-shape2-missing-keyword", "threat": "Regex accepts a string lacking its required keyword/prefix"}
```

### Witness

```json
null
```

### Ground-truth

None

## property:inventory:rc-shape3-capture-truncation:rc-shape3-capture-truncation

```yaml
regex_id: "inventory:rc-shape3-capture-truncation"
schema_version: "1"
kind: property
corpus: Hazer
shape: 3
result: planned
disclosure: null
site: "inventory:rc-shape3-capture-truncation"
```

### Pattern

``

### Context

```json
{"question_id": "rc-shape3-capture-truncation", "threat": "Fallback capture truncates or mismatches true token value"}
```

### Witness

```json
null
```

### Ground-truth

None

## property:inventory:rc-shape4-escape-image:rc-shape4-escape-image

```yaml
regex_id: "inventory:rc-shape4-escape-image"
schema_version: "1"
kind: property
corpus: Hazer
shape: 4
result: planned
disclosure: null
site: "inventory:rc-shape4-escape-image"
```

### Pattern

``

### Context

```json
{"question_id": "rc-shape4-escape-image", "threat": "If rule output is escaped into logs/shell, raw controls must not appear"}
```

### Witness

```json
null
```

### Ground-truth

None

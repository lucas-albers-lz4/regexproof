---
schema_version: "1"
corpus: python_3_8_2
findings: 135
---

# python_3_8_2 batch findings

## usage_mismatch:01e78ec76744a86ceb1a2dd294fa0a07:search

```yaml
regex_id: 01e78ec76744a86ceb1a2dd294fa0a07
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/idlelib/pyshell.py:1225:35"
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

## usage_mismatch:04bf4686f5ba760898826463ef3083fe:search

```yaml
regex_id: 04bf4686f5ba760898826463ef3083fe
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/urllib/request.py:306:15"
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

## usage_mismatch:058f6508e4c5862faea0b3a7e972d8ee:match

```yaml
regex_id: 058f6508e4c5862faea0b3a7e972d8ee
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:599:25"
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

## intent_mismatch:06f472f967ae3bf2dd16d63e7614f4f0:email

```yaml
regex_id: 06f472f967ae3bf2dd16d63e7614f4f0
schema_version: "1"
kind: intent_mismatch
corpus: python_3_8_2
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/email/header.py:35:7"
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

## usage_mismatch:0766000d573ee7b517b28d331f3d7702:search

```yaml
regex_id: 0766000d573ee7b517b28d331f3d7702
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/http/cookiejar.py:202:13"
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

## usage_mismatch:0ff929519e917bed8692d158aa9f1e58:search

```yaml
regex_id: 0ff929519e917bed8692d158aa9f1e58
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/http/cookiejar.py:281:14"
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

## usage_mismatch:10b8026ee0fa49cd2ddaa51eccaa867d:match

```yaml
regex_id: 10b8026ee0fa49cd2ddaa51eccaa867d
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:520:26"
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

## usage_mismatch:1ae88273b49783400d37b0da27d6f641:search

```yaml
regex_id: 1ae88273b49783400d37b0da27d6f641
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Tools/scripts/h2py.py:26:11"
```

### Pattern

`^[\t ]*#[\t ]*define[\t ]+([a-zA-Z0-9_]+)[\t ]+`

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

## usage_mismatch:1c4d98993f780902570746a64f452d2d:search

```yaml
regex_id: 1c4d98993f780902570746a64f452d2d
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/logging/config.py:360:18"
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

## usage_mismatch:1cc61fcbf36f1c9a64538e1205fa6992:match

```yaml
regex_id: 1cc61fcbf36f1c9a64538e1205fa6992
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:560:25"
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

## usage_mismatch:1dc06d5ec06bfd43b2d422e59c10ce2e:search

```yaml
regex_id: 1dc06d5ec06bfd43b2d422e59c10ce2e
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/doctest.py:1407:30"
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

## usage_mismatch:1e0d89c45de73ac4a5e0996a211405f8:search

```yaml
regex_id: 1e0d89c45de73ac4a5e0996a211405f8
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/http/cookiejar.py:612:14"
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

## usage_mismatch:23b054fb8bba49bb545dc716514c7ecc:search

```yaml
regex_id: 23b054fb8bba49bb545dc716514c7ecc
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/http/cookiejar.py:337:25"
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

## intent_mismatch:27412b1e8efcc7a44f69edc967075c44:email

```yaml
regex_id: 27412b1e8efcc7a44f69edc967075c44
schema_version: "1"
kind: intent_mismatch
corpus: python_3_8_2
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/email/generator.py:22:7"
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

## usage_mismatch:27412b1e8efcc7a44f69edc967075c44:search

```yaml
regex_id: 27412b1e8efcc7a44f69edc967075c44
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/email/generator.py:22:7"
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

## usage_mismatch:2c779e6035150cbdde10be3f9f81984e:search

```yaml
regex_id: 2c779e6035150cbdde10be3f9f81984e
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Tools/scripts/mailerdaemon.py:92:4"
```

### Pattern

`^<<< 5\d{2} (?P<reason>.*)`

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

## usage_mismatch:2cb83b9531726b45464294dffebdf5d2:match

```yaml
regex_id: 2cb83b9531726b45464294dffebdf5d2
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:528:25"
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

## usage_mismatch:2d297b92d769ac5a5aade0a971909433:search

```yaml
regex_id: 2d297b92d769ac5a5aade0a971909433
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/textwrap.py:411:22"
```

### Pattern

`^[ 	]+$`

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

## usage_mismatch:2e44dba4ca51d37fc628e4a0e13628b2:search

```yaml
regex_id: 2e44dba4ca51d37fc628e4a0e13628b2
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:1690:12"
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

## usage_mismatch:2e94454bfc4a8440749eee32aee21a87:match

```yaml
regex_id: 2e94454bfc4a8440749eee32aee21a87
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Tools/demo/ss1.py:436:12"
```

### Pattern

`^([A-Z]+)([1-9][0-9]*)(?::([A-Z]+)([1-9][0-9]*))?$`

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

## usage_mismatch:36b0592e526983100c8cc9899b684486:search

```yaml
regex_id: 36b0592e526983100c8cc9899b684486
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/nntplib.py:789:14"
```

### Pattern

`^([0-9]+) ?(.*)
?`

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

## usage_mismatch:386f57fc78c71d1496543660e9ed0eb5:search

```yaml
regex_id: 386f57fc78c71d1496543660e9ed0eb5
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:1082:28"
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

## usage_mismatch:3b97cb7dab18f28108b1b7da8f4febff:search

```yaml
regex_id: 3b97cb7dab18f28108b1b7da8f4febff
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/logging/__init__.py:447:17"
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

## usage_mismatch:3e4c5598e52a5af56a427e7b0b2adba0:search

```yaml
regex_id: 3e4c5598e52a5af56a427e7b0b2adba0
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/idlelib/iomenu.py:63:12"
```

### Pattern

`^[ \t\f]*#.*?coding[:=][ \t]*([-\w.]+)`

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

## usage_mismatch:46c225850b44610fdf1e6054d5e88fcf:search

```yaml
regex_id: 46c225850b44610fdf1e6054d5e88fcf
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_smtplib.py:138:19"
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

## usage_mismatch:49bfe84b0fb91fdb7b6ef84401480cec:match

```yaml
regex_id: 49bfe84b0fb91fdb7b6ef84401480cec
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:601:25"
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

## usage_mismatch:4b6d15f800dd90d9d7d7a4a58116d982:search

```yaml
regex_id: 4b6d15f800dd90d9d7d7a4a58116d982
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:657:26"
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

## usage_mismatch:4bd62a7271c789fd443c599cd48f942b:search

```yaml
regex_id: 4bd62a7271c789fd443c599cd48f942b
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_smtplib.py:387:17"
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

## usage_mismatch:4dc81b3d3cdeae1eb2fb5bfbf0740ce2:match

```yaml
regex_id: 4dc81b3d3cdeae1eb2fb5bfbf0740ce2
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:613:24"
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

## usage_mismatch:4f3750acb82d731b2f58af1b25955e6f:match

```yaml
regex_id: 4f3750acb82d731b2f58af1b25955e6f
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:522:25"
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

## usage_mismatch:51c9a954bf9761311407aacce5bafc1e:search

```yaml
regex_id: 51c9a954bf9761311407aacce5bafc1e
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Tools/scripts/texi2html.py:73:9"
```

### Pattern

`^@([a-z]+)([ 	]|$)`

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

## usage_mismatch:540049d0ff6963feb2b8149929e65b3c:match

```yaml
regex_id: 540049d0ff6963feb2b8149929e65b3c
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:612:24"
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

## usage_mismatch:560e07e1359542a7088cc7843c356bb9:search

```yaml
regex_id: 560e07e1359542a7088cc7843c356bb9
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:511:12"
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

## usage_mismatch:57a7508b68042583798b5ce967402ca3:search

```yaml
regex_id: 57a7508b68042583798b5ce967402ca3
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/logging/config.py:277:13"
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

## usage_mismatch:5a1af8c11d6d531f092cd2bdb32421a7:match

```yaml
regex_id: 5a1af8c11d6d531f092cd2bdb32421a7
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/msilib/__init__.py:181:11"
```

### Pattern

`^[A-Za-z_][A-Za-z0-9_.]*$`

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

## usage_mismatch:5ca42703c63bc824d1c547ab3ca2276e:match

```yaml
regex_id: 5ca42703c63bc824d1c547ab3ca2276e
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:598:25"
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

## usage_mismatch:5d5151327d25b1d1a5e14419bcb9ac35:match

```yaml
regex_id: 5d5151327d25b1d1a5e14419bcb9ac35
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/idlelib/format.py:181:11"
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

## usage_mismatch:5e74b36ac85843733b3cb0c3cf7d1354:search

```yaml
regex_id: 5e74b36ac85843733b3cb0c3cf7d1354
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/idlelib/pyshell.py:1226:35"
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

## usage_mismatch:60f6e0324876150d2499d82db2d2aa4e:match

```yaml
regex_id: 60f6e0324876150d2499d82db2d2aa4e
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:589:26"
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

## usage_mismatch:6353d022d02719196c4a36ef34dee8db:match

```yaml
regex_id: 6353d022d02719196c4a36ef34dee8db
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:565:26"
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

## usage_mismatch:64029c3ebc841d45fe87234c789e854c:search

```yaml
regex_id: 64029c3ebc841d45fe87234c789e854c
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/logging/config.py:361:20"
```

### Pattern

`^\[\s*(\w+)\s*\]\s*`

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

## usage_mismatch:6413374064cc286ccec5988d14da7b1f:search

```yaml
regex_id: 6413374064cc286ccec5988d14da7b1f
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/_pydecimal.py:6132:13"
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

## usage_mismatch:64f3fa9b6e06cf8fad57eaf07e9aea4f:search

```yaml
regex_id: 64f3fa9b6e06cf8fad57eaf07e9aea4f
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_smtplib.py:438:17"
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

## usage_mismatch:6853c2f9eb7122702e0fa37d396cfc81:match

```yaml
regex_id: 6853c2f9eb7122702e0fa37d396cfc81
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/lib2to3/pgen2/conv.py:71:17"
```

### Pattern

`^#define\s+(\w+)\s+(\d+)$`

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

## usage_mismatch:6d6b018a7c5fb46bcb68592fdeec9d78:search

```yaml
regex_id: 6d6b018a7c5fb46bcb68592fdeec9d78
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/distutils/versionpredicate.py:156:24"
```

### Pattern

`([a-zA-Z_]\w*(?:\.[a-zA-Z_]\w*)*)(?:\s*\(\s*([^)\s]+)\s*\))?$`

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

## usage_mismatch:6ef382505aae3e5fb5fd17237e5a2fb3:match

```yaml
regex_id: 6ef382505aae3e5fb5fd17237e5a2fb3
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:608:24"
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

## usage_mismatch:6f00a64a233747e14877382f2a7ab840:match

```yaml
regex_id: 6f00a64a233747e14877382f2a7ab840
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:614:24"
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

## usage_mismatch:6ff6b004aa5f2f1eb3b704d49cafdfac:search

```yaml
regex_id: 6ff6b004aa5f2f1eb3b704d49cafdfac
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/http/cookiejar.py:1256:15"
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

## usage_mismatch:740a364fa7756cb1e313588397f3f733:search

```yaml
regex_id: 740a364fa7756cb1e313588397f3f733
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:1507:18"
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

## usage_mismatch:745ece92c854fd6f823ab66627c30e7c:match

```yaml
regex_id: 745ece92c854fd6f823ab66627c30e7c
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:616:24"
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

## usage_mismatch:74ae1eb125f10ae6e855bd53108b5ab7:search

```yaml
regex_id: 74ae1eb125f10ae6e855bd53108b5ab7
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/logging/config.py:359:19"
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

## usage_mismatch:76f01548d481684f52258e0536598612:match

```yaml
regex_id: 76f01548d481684f52258e0536598612
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:526:25"
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

## usage_mismatch:77f2beaf652242babe198e798a45d3f3:search

```yaml
regex_id: 77f2beaf652242babe198e798a45d3f3
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Tools/scripts/h2py.py:28:10"
```

### Pattern

`^[\t ]*#[\t ]*define[\t ]+([a-zA-Z0-9_]+)\(([_a-zA-Z][_a-zA-Z0-9]*)\)[\t ]+`

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

## usage_mismatch:77fa2a2f1c2c4a66d75e8017f47ab404:match

```yaml
regex_id: 77fa2a2f1c2c4a66d75e8017f47ab404
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:564:26"
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

## intent_mismatch:7836b195cbd27fe8ee39b2c3b6756252:email

```yaml
regex_id: 7836b195cbd27fe8ee39b2c3b6756252
schema_version: "1"
kind: intent_mismatch
corpus: python_3_8_2
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/email/_header_value_parser.py:100:18"
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

## usage_mismatch:791d36a08d57c2eeb9e26fe0b9120e00:search

```yaml
regex_id: 791d36a08d57c2eeb9e26fe0b9120e00
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/http/cookiejar.py:1254:14"
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

## usage_mismatch:79861dd20b3cca9ffbef94d193b7b85d:search

```yaml
regex_id: 79861dd20b3cca9ffbef94d193b7b85d
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_smtplib.py:526:17"
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

## intent_mismatch:7caf5f10e78e1fa6312679cbad83f3e5:email

```yaml
regex_id: 7caf5f10e78e1fa6312679cbad83f3e5
schema_version: "1"
kind: intent_mismatch
corpus: python_3_8_2
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/email/feedparser.py:37:11"
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

## usage_mismatch:7caf5f10e78e1fa6312679cbad83f3e5:search

```yaml
regex_id: 7caf5f10e78e1fa6312679cbad83f3e5
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/email/feedparser.py:37:11"
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

## usage_mismatch:7fd38e4334f1df6bbd595ab404841d40:match

```yaml
regex_id: 7fd38e4334f1df6bbd595ab404841d40
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:592:26"
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

## usage_mismatch:8274da875ef5c43a678f0d7c84cfa624:search

```yaml
regex_id: 8274da875ef5c43a678f0d7c84cfa624
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Tools/scripts/mailerdaemon.py:168:10"
```

### Pattern

`^[0-9]*$`

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

## usage_mismatch:858f18798314c5d882ef26de6383fdde:search

```yaml
regex_id: 858f18798314c5d882ef26de6383fdde
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/email/utils.py:254:23"
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

## usage_mismatch:8597d9f296efa0f14c02b1b86f66d81a:search

```yaml
regex_id: 8597d9f296efa0f14c02b1b86f66d81a
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/logging/__init__.py:446:15"
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

## usage_mismatch:85f43fbbebd1e496fadc8f7a433cdf71:search

```yaml
regex_id: 85f43fbbebd1e496fadc8f7a433cdf71
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/http/cookiejar.py:199:17"
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

## usage_mismatch:88a569ea43feeef18e3d9503a5b80929:match

```yaml
regex_id: 88a569ea43feeef18e3d9503a5b80929
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:562:25"
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

## usage_mismatch:8960e65f76c30f147181953ccd81257f:match

```yaml
regex_id: 8960e65f76c30f147181953ccd81257f
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:603:26"
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

## usage_mismatch:89d6f88ce03811fc00f155ab43faac28:search

```yaml
regex_id: 89d6f88ce03811fc00f155ab43faac28
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_smtplib.py:467:17"
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

## usage_mismatch:8cca8a227cddc0857153a3e43037d28e:search

```yaml
regex_id: 8cca8a227cddc0857153a3e43037d28e
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/nntplib.py:614:19"
```

### Pattern

`^(?P<group>[^ 	]+)[ 	]+(.*)$`

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

## usage_mismatch:8e68a1729b0ff6fca1358c08b8e91568:search

```yaml
regex_id: 8e68a1729b0ff6fca1358c08b8e91568
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_regrtest.py:960:16"
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

## usage_mismatch:907b7467d2f4e473756e874d960b5c2a:match

```yaml
regex_id: 907b7467d2f4e473756e874d960b5c2a
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:606:26"
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

## usage_mismatch:92fddce7ad8d00a391cc103880ef6b85:search

```yaml
regex_id: 92fddce7ad8d00a391cc103880ef6b85
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Tools/scripts/texi2html.py:81:9"
```

### Pattern

`^\* ([^:]*):(:|[ \t]*([^\t,\n.]+)([^ \t\n]*))[ \t\n]*`

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

## usage_mismatch:945ffb3846c2a8da5be0719bb9d040ee:search

```yaml
regex_id: 945ffb3846c2a8da5be0719bb9d040ee
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:655:25"
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

## usage_mismatch:9693a5942b59ed51a9b5d16540c660dd:match

```yaml
regex_id: 9693a5942b59ed51a9b5d16540c660dd
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:524:25"
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

## usage_mismatch:97550d6d76ef94ff638453f51252c5dc:match

```yaml
regex_id: 97550d6d76ef94ff638453f51252c5dc
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:611:24"
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

## usage_mismatch:987b278d23d45c3b15ea36e90c27d86c:search

```yaml
regex_id: 987b278d23d45c3b15ea36e90c27d86c
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/http/cookiejar.py:338:25"
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

## usage_mismatch:9f57bb8c3cfd13dd72c732ea53893494:search

```yaml
regex_id: 9f57bb8c3cfd13dd72c732ea53893494
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/configparser.py:1315:16"
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

## usage_mismatch:a113792e1fe71d452f0f37d85dc05767:search

```yaml
regex_id: a113792e1fe71d452f0f37d85dc05767
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/distutils/versionpredicate.py:12:11"
```

### Pattern

`^\s*\((.*)\)\s*$`

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

## usage_mismatch:a22361a7f0d6cc66c4a198332110499c:match

```yaml
regex_id: a22361a7f0d6cc66c4a198332110499c
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:516:25"
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

## usage_mismatch:a2521ecb81fa052b6ec276ef0a22bc41:search

```yaml
regex_id: a2521ecb81fa052b6ec276ef0a22bc41
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/logging/config.py:362:20"
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

## usage_mismatch:a4ea492e03731ba04e9a1eadd4dfd085:search

```yaml
regex_id: a4ea492e03731ba04e9a1eadd4dfd085
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/_pydecimal.py:6133:14"
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

## usage_mismatch:a67c15a59ff80cb18cb25a68693055d5:search

```yaml
regex_id: a67c15a59ff80cb18cb25a68693055d5
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/http/cookiejar.py:444:23"
```

### Pattern

`^\w+$`

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

## usage_mismatch:a7f2d2abc2037d0505aab05d29ffed74:search

```yaml
regex_id: a7f2d2abc2037d0505aab05d29ffed74
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/doctest.py:767:17"
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

## usage_mismatch:a82dec1ad3af76b522dd375922ab115c:match

```yaml
regex_id: a82dec1ad3af76b522dd375922ab115c
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Tools/demo/ss1.py:417:16"
```

### Pattern

`^([A-Z]+)([1-9][0-9]*)$`

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

## usage_mismatch:a9852ba2df032b9da6738d820d06157c:search

```yaml
regex_id: a9852ba2df032b9da6738d820d06157c
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:656:25"
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

## usage_mismatch:aa830fa1000e80f8e5869d9d4faf741a:match

```yaml
regex_id: aa830fa1000e80f8e5869d9d4faf741a
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:1379:29"
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

## usage_mismatch:ac2731bd7743de113104b698f58c2646:search

```yaml
regex_id: ac2731bd7743de113104b698f58c2646
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_smtplib.py:562:17"
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

## usage_mismatch:ac7812d48bba2a51f56e0054c2b953ad:match

```yaml
regex_id: ac7812d48bba2a51f56e0054c2b953ad
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:518:25"
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

## usage_mismatch:ad6cfdfa88eec0c6b7a656c4254265f9:match

```yaml
regex_id: ad6cfdfa88eec0c6b7a656c4254265f9
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:596:25"
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

## usage_mismatch:ae9785fcf017c41c1730431a0d2f84d9:match

```yaml
regex_id: ae9785fcf017c41c1730431a0d2f84d9
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:610:24"
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

## usage_mismatch:afaca15f35b986917540670dbe6c64f1:match

```yaml
regex_id: afaca15f35b986917540670dbe6c64f1
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:597:25"
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

## usage_mismatch:b30ff5e86d01d2c36051c4a76f8e06d6:search

```yaml
regex_id: b30ff5e86d01d2c36051c4a76f8e06d6
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Tools/scripts/mailerdaemon.py:94:4"
```

### Pattern

`^Diagnostic-Code: (?P<reason>.*)`

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

## usage_mismatch:b58d27617f5646c620d7dc88ee56575c:match

```yaml
regex_id: b58d27617f5646c620d7dc88ee56575c
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:521:26"
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

## usage_mismatch:b84c04244fe44cdde2d323d5748d021b:search

```yaml
regex_id: b84c04244fe44cdde2d323d5748d021b
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Doc/tools/extensions/pyspecific.py:356:14"
```

### Pattern

`(?im)^what's new in (.*?)\??$`

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

## usage_mismatch:bbb6aacaeaa462a35576587dbf6322ec:search

```yaml
regex_id: bbb6aacaeaa462a35576587dbf6322ec
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/doctest.py:618:27"
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

## usage_mismatch:bd60f3e13868d6eac460415002049c25:search

```yaml
regex_id: bd60f3e13868d6eac460415002049c25
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_smtplib.py:501:16"
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

## usage_mismatch:bf55df3eadb560aef57d5ebe886b0b63:search

```yaml
regex_id: bf55df3eadb560aef57d5ebe886b0b63
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/logging/config.py:357:22"
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

## usage_mismatch:c32f9088df166859f30cf92c7ad31c41:search

```yaml
regex_id: c32f9088df166859f30cf92c7ad31c41
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Tools/scripts/texi2html.py:1597:19"
```

### Pattern

`^(@[a-z]+)?{`

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

## usage_mismatch:c335bd8be5a9fc1f065ba3e701f68ee1:search

```yaml
regex_id: c335bd8be5a9fc1f065ba3e701f68ee1
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/http/cookiejar.py:339:25"
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

## usage_mismatch:c3d45f9454a64e8c4139a48067574277:match

```yaml
regex_id: c3d45f9454a64e8c4139a48067574277
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:594:25"
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

## usage_mismatch:c62b87d906b78970d10ef7ca6954b7f0:search

```yaml
regex_id: c62b87d906b78970d10ef7ca6954b7f0
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_smtplib.py:148:19"
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

## usage_mismatch:c6912b366b04c7e84a4e546f3a698a41:search

```yaml
regex_id: c6912b366b04c7e84a4e546f3a698a41
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/doctest.py:736:27"
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

## usage_mismatch:c86b69dccbafb89f74e3c706eb1b86cc:match

```yaml
regex_id: c86b69dccbafb89f74e3c706eb1b86cc
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:605:26"
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

## usage_mismatch:cb4503c6b90db5754d0de73aa7a44ca1:search

```yaml
regex_id: cb4503c6b90db5754d0de73aa7a44ca1
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/http/cookiejar.py:204:21"
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

## usage_mismatch:cc168fd7e7fc1ad52479faa5663e7440:search

```yaml
regex_id: cc168fd7e7fc1ad52479faa5663e7440
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Tools/scripts/texi2html.py:74:9"
```

### Pattern

`^[ 	]*$`

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

## usage_mismatch:d100906b0c68a2e997e927baba06e020:match

```yaml
regex_id: d100906b0c68a2e997e927baba06e020
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:604:26"
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

## usage_mismatch:d1a46d5faf7948a9d10af955d447247d:match

```yaml
regex_id: d1a46d5faf7948a9d10af955d447247d
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:591:26"
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

## usage_mismatch:d5171ea9ad9b32cc2e654e2c10e55e6f:search

```yaml
regex_id: d5171ea9ad9b32cc2e654e2c10e55e6f
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:1502:18"
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

## usage_mismatch:dbe7cc2c6255fd05782b053fba2de563:search

```yaml
regex_id: dbe7cc2c6255fd05782b053fba2de563
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/distutils/versionpredicate.py:13:21"
```

### Pattern

`^\s*(<=|>=|<|>|!=|==)\s*([^\s,]+)\s*$`

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

## usage_mismatch:ddb2cc2723ef3656ec800d89ca17735b:search

```yaml
regex_id: ddb2cc2723ef3656ec800d89ca17735b
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/idlelib/iomenu.py:64:11"
```

### Pattern

`^[ \t\f]*(?:[#\r\n]|$)`

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

## usage_mismatch:dea0759083b5dda17d0c79bd86481241:match

```yaml
regex_id: dea0759083b5dda17d0c79bd86481241
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:595:25"
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

## usage_mismatch:e33e5e390c191e399428e9fd7621ace8:match

```yaml
regex_id: e33e5e390c191e399428e9fd7621ace8
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:609:24"
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

## usage_mismatch:e478d52911a2d263e879954846340cdc:match

```yaml
regex_id: e478d52911a2d263e879954846340cdc
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:590:26"
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

## usage_mismatch:e6c0ef6f4d546cabb61f5b242c81dfe8:search

```yaml
regex_id: e6c0ef6f4d546cabb61f5b242c81dfe8
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/email/header.py:48:7"
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

## usage_mismatch:e710b2ac1a55b0c2d4f2bcce8c5ac823:search

```yaml
regex_id: e710b2ac1a55b0c2d4f2bcce8c5ac823
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/pydoc.py:135:14"
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

## usage_mismatch:e98ad2a51a5a39f857486d3bee507325:match

```yaml
regex_id: e98ad2a51a5a39f857486d3bee507325
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:600:25"
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

## usage_mismatch:eaffc966ba1c7d7ce459cb020b1eaf05:match

```yaml
regex_id: eaffc966ba1c7d7ce459cb020b1eaf05
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:619:24"
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

## usage_mismatch:eb02108a191a0774aa4a9cf5e637f362:match

```yaml
regex_id: eb02108a191a0774aa4a9cf5e637f362
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:615:24"
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

## usage_mismatch:ebd20edff6904856d23f602ce1786a48:search

```yaml
regex_id: ebd20edff6904856d23f602ce1786a48
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/http/cookiejar.py:128:14"
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

## usage_mismatch:ecdba330ce5b3243a1178b3ca63a0f8e:search

```yaml
regex_id: ecdba330ce5b3243a1178b3ca63a0f8e
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/lib2to3/pgen2/tokenize.py:227:12"
```

### Pattern

`^[ \t\f]*#.*?coding[:=][ \t]*([-\w.]+)`

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

## usage_mismatch:eceb06bc30dea00790c910a186e63b70:match

```yaml
regex_id: eceb06bc30dea00790c910a186e63b70
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:1388:30"
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

## usage_mismatch:ef63d975eed8b87ff969b1c2718381ca:search

```yaml
regex_id: ef63d975eed8b87ff969b1c2718381ca
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_gdb.py:36:12"
```

### Pattern

`^GNU gdb.*?\b(\d+)\.(\d+)`

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

## usage_mismatch:f14a8cc0b777317bceb0d384200be6cc:match

```yaml
regex_id: f14a8cc0b777317bceb0d384200be6cc
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:568:25"
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

## usage_mismatch:f2d2b3538fc5c87a6f6769954c25d2c5:match

```yaml
regex_id: f2d2b3538fc5c87a6f6769954c25d2c5
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:566:25"
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

## usage_mismatch:f9a92193f6fc76125d53734350269cd6:search

```yaml
regex_id: f9a92193f6fc76125d53734350269cd6
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/http/cookiejar.py:527:10"
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

## usage_mismatch:f9c95f80ce4b6f3e5bd85778007d9ed3:search

```yaml
regex_id: f9c95f80ce4b6f3e5bd85778007d9ed3
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_smtplib.py:495:17"
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

## usage_mismatch:fa21e3bccd07124153d6f66e08c18fd7:search

```yaml
regex_id: fa21e3bccd07124153d6f66e08c18fd7
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Tools/scripts/h2py.py:32:12"
```

### Pattern

`^[\t ]*#[\t ]*include[\t ]+<([^>\n]+)>`

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

## usage_mismatch:fada6108b7c3c9b55d1d72d0797fea25:match

```yaml
regex_id: fada6108b7c3c9b55d1d72d0797fea25
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_re.py:618:26"
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

## intent_mismatch:fb16d2389481e25c80e493a51de5777c:email

```yaml
regex_id: fb16d2389481e25c80e493a51de5777c
schema_version: "1"
kind: intent_mismatch
corpus: python_3_8_2
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_email/test_email.py:5421:17"
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

## usage_mismatch:fb16d2389481e25c80e493a51de5777c:search

```yaml
regex_id: fb16d2389481e25c80e493a51de5777c
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/test/test_email/test_email.py:5421:17"
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

## usage_mismatch:fd0566eb17534d70b9b30a5dbfbe66b7:search

```yaml
regex_id: fd0566eb17534d70b9b30a5dbfbe66b7
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Tools/scripts/mailerdaemon.py:96:20"
```

### Pattern

`^From:`

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

## usage_mismatch:fd92da7bc302e732c10afaf8c1d95ada:search

```yaml
regex_id: fd92da7bc302e732c10afaf8c1d95ada
schema_version: "1"
kind: usage_mismatch
corpus: python_3_8_2
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/python_3_8_2/rules/Lib/nntplib.py:846:19"
```

### Pattern

`^([^ 	]+)[ 	]+(.*)$`

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
corpus: python_3_8_2
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
corpus: python_3_8_2
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
corpus: python_3_8_2
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
corpus: python_3_8_2
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

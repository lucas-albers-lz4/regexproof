---
schema_version: "1"
corpus: cpython
findings: 138
---

# cpython batch findings

## usage_mismatch:0084f2116d74be200c2e6ed190288db4:match

```yaml
regex_id: 0084f2116d74be200c2e6ed190288db4
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:562:25"
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

## usage_mismatch:00e782f96a304e8c6450b6efbd78a4be:match

```yaml
regex_id: 00e782f96a304e8c6450b6efbd78a4be
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:1352:30"
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

## usage_mismatch:01d81eeb4b98fb6d4f879ba8b61e90d6:match

```yaml
regex_id: 01d81eeb4b98fb6d4f879ba8b61e90d6
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:594:25"
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

## usage_mismatch:02840eae7c770207849250f0227a8fb8:search

```yaml
regex_id: 02840eae7c770207849250f0227a8fb8
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_smtplib.py:417:17"
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

## usage_mismatch:02cb5090ec1757e65b6d5fac0dc8ed00:search

```yaml
regex_id: 02cb5090ec1757e65b6d5fac0dc8ed00
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/http/cookiejar.py:203:21"
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
    ([-+]?\d{2,4}|(?![APap][Mm]\b)[A-Za-z]+)? # timezone
       \s*
    (?:\(\w+\))?       # ASCII representation of timezone in parens.
       \s*$`

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

## usage_mismatch:065c36e8cc558be35adf2dc803b2f053:search

```yaml
regex_id: 065c36e8cc558be35adf2dc803b2f053
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/logging/config.py:358:19"
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

## usage_mismatch:0799f5889bea8c3e00f0a0fbdc3bbd25:search

```yaml
regex_id: 0799f5889bea8c3e00f0a0fbdc3bbd25
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Tools/scripts/texi2html.py:73:9"
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

## usage_mismatch:081f2c2c4b3394fd7ce43eb81e67c295:search

```yaml
regex_id: 081f2c2c4b3394fd7ce43eb81e67c295
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:655:25"
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

## usage_mismatch:0a84c875261f973a22d7692190080a03:search

```yaml
regex_id: 0a84c875261f973a22d7692190080a03
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/importlib/metadata.py:48:14"
```

### Pattern

`(?P<module>[\w.]+)\s*(:\s*(?P<attr>[\w.]+))?\s*(?P<extras>\[.*\])?\s*$`

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

## usage_mismatch:0dee07d71cbab17868ea4a204aba69ee:search

```yaml
regex_id: 0dee07d71cbab17868ea4a204aba69ee
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_smtplib.py:145:19"
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

## usage_mismatch:0efb05223ddafabd8b40eec37ec72433:search

```yaml
regex_id: 0efb05223ddafabd8b40eec37ec72433
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:657:26"
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

## usage_mismatch:1168cf37b20b13ea236d78c824576904:match

```yaml
regex_id: 1168cf37b20b13ea236d78c824576904
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/idlelib/format.py:181:11"
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

## usage_mismatch:116d30d8f0bbb65e05adb484b0c77783:search

```yaml
regex_id: 116d30d8f0bbb65e05adb484b0c77783
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/http/cookiejar.py:201:13"
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

## usage_mismatch:129af2830a7909bcc1657244f1438a4c:search

```yaml
regex_id: 129af2830a7909bcc1657244f1438a4c
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:1466:18"
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

## usage_mismatch:13dbd1382da88b3111fca8d86d098ed0:search

```yaml
regex_id: 13dbd1382da88b3111fca8d86d098ed0
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:1046:28"
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

## usage_mismatch:1517f3e5ffa13d66cac2131a2c30fecf:search

```yaml
regex_id: 1517f3e5ffa13d66cac2131a2c30fecf
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_gdb.py:36:12"
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

## usage_mismatch:152e8869a855103ff709829071e30c5e:match

```yaml
regex_id: 152e8869a855103ff709829071e30c5e
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:611:24"
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

## usage_mismatch:178e8153bce708630155cd1563fb71a6:search

```yaml
regex_id: 178e8153bce708630155cd1563fb71a6
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Tools/scripts/mailerdaemon.py:96:20"
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

## usage_mismatch:18d22feee2e2356edeebb0cc89759af2:match

```yaml
regex_id: 18d22feee2e2356edeebb0cc89759af2
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:566:25"
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

## usage_mismatch:1a592f1ebfa0233a1c5f88f1836cda92:search

```yaml
regex_id: 1a592f1ebfa0233a1c5f88f1836cda92
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/urllib/parse.py:977:20"
```

### Pattern

`(.*):([0-9]*)$`

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

## usage_mismatch:1a876afbb192aed4ae2b86b2930a2277:match

```yaml
regex_id: 1a876afbb192aed4ae2b86b2930a2277
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:619:24"
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

## usage_mismatch:1c18c7734e2245509d3a7032e7cb6cdb:search

```yaml
regex_id: 1c18c7734e2245509d3a7032e7cb6cdb
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/logging/config.py:360:20"
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

## usage_mismatch:1c629e30ae8806c99e85404dfabd3ef6:search

```yaml
regex_id: 1c629e30ae8806c99e85404dfabd3ef6
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/nntplib.py:844:19"
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

## usage_mismatch:1cb2ae515e9c553d7985b0f337dcdb1d:search

```yaml
regex_id: 1cb2ae515e9c553d7985b0f337dcdb1d
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_smtplib.py:368:17"
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

## usage_mismatch:1cd2df4da0b667140bf30de624c561f0:search

```yaml
regex_id: 1cd2df4da0b667140bf30de624c561f0
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/email/utils.py:254:23"
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

## usage_mismatch:1dc363a6db747af5c832711379f070d4:match

```yaml
regex_id: 1dc363a6db747af5c832711379f070d4
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:564:26"
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

## usage_mismatch:20a98419662d2bfa2bbd0a7ba8cb053a:match

```yaml
regex_id: 20a98419662d2bfa2bbd0a7ba8cb053a
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:592:26"
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

## usage_mismatch:23d7bc6148d4a6cac4ea6e677ff79664:match

```yaml
regex_id: 23d7bc6148d4a6cac4ea6e677ff79664
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:614:24"
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

## usage_mismatch:2ef8e92f418094d9b993a1204bc4963e:match

```yaml
regex_id: 2ef8e92f418094d9b993a1204bc4963e
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:522:25"
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

## intent_mismatch:2f0e99cee8750ed4a46f66e005a000a8:email

```yaml
regex_id: 2f0e99cee8750ed4a46f66e005a000a8
schema_version: "1"
kind: intent_mismatch
corpus: cpython
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/email/header.py:35:7"
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
{"admitted_char": "' '", "keyword": "email", "reason": "name/comment claims validation but pattern admits excluded char"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:31d3868c01cdc093bf29d1143716503f:match

```yaml
regex_id: 31d3868c01cdc093bf29d1143716503f
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:601:25"
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

## usage_mismatch:32477791641c06f6f835b71475e22e7b:search

```yaml
regex_id: 32477791641c06f6f835b71475e22e7b
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:656:25"
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

## usage_mismatch:379fcc4d1402b3fa61423e5c38a34449:match

```yaml
regex_id: 379fcc4d1402b3fa61423e5c38a34449
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:615:24"
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

## usage_mismatch:37b3d9cdaafb2d6897f4cc8339b2495a:search

```yaml
regex_id: 37b3d9cdaafb2d6897f4cc8339b2495a
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/doctest.py:736:27"
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

## usage_mismatch:38fbea1f8be28ffc921d781939891dce:search

```yaml
regex_id: 38fbea1f8be28ffc921d781939891dce
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/http/cookiejar.py:332:25"
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

## usage_mismatch:3a296863377bf0967ad165802351b4ec:match

```yaml
regex_id: 3a296863377bf0967ad165802351b4ec
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:613:24"
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

## usage_mismatch:3a56f0cd80ab99d675f2f32b7c1f7420:search

```yaml
regex_id: 3a56f0cd80ab99d675f2f32b7c1f7420
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:1655:12"
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

## usage_mismatch:3bab6c19ade4f2ed8ec990b36ef953f3:search

```yaml
regex_id: 3bab6c19ade4f2ed8ec990b36ef953f3
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/idlelib/iomenu.py:69:11"
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

## usage_mismatch:3bd23bad8885317cf50d867a01f74b1a:search

```yaml
regex_id: 3bd23bad8885317cf50d867a01f74b1a
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/idlelib/pyshell.py:1223:35"
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

## usage_mismatch:3d737fa9d85affc9eeee525a6e1c1bec:search

```yaml
regex_id: 3d737fa9d85affc9eeee525a6e1c1bec
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_smtplib.py:502:17"
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

## usage_mismatch:3e19386333d6bf710aca28280c887d4d:match

```yaml
regex_id: 3e19386333d6bf710aca28280c887d4d
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:600:25"
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

## usage_mismatch:44137433990a3d240d77f678de7b1468:match

```yaml
regex_id: 44137433990a3d240d77f678de7b1468
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:589:26"
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

## usage_mismatch:454ed1be47d8c10b54e5bd0fd2745394:search

```yaml
regex_id: 454ed1be47d8c10b54e5bd0fd2745394
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Tools/scripts/h2py.py:28:10"
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

## usage_mismatch:4a20750c6e722b6269565d89481f1d18:search

```yaml
regex_id: 4a20750c6e722b6269565d89481f1d18
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Tools/scripts/mailerdaemon.py:94:4"
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

## usage_mismatch:4b13f1c1247fc127e2d59faa01459b1d:match

```yaml
regex_id: 4b13f1c1247fc127e2d59faa01459b1d
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:608:24"
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

## usage_mismatch:4b3e40690f7b20bd0fe7d5dee070e6f6:search

```yaml
regex_id: 4b3e40690f7b20bd0fe7d5dee070e6f6
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/nntplib.py:787:14"
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

## usage_mismatch:4e34541342906967efd4e9d293493fee:search

```yaml
regex_id: 4e34541342906967efd4e9d293493fee
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/http/cookiejar.py:1234:15"
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

## usage_mismatch:532f32c2fba5dd87435d5138eec457b7:match

```yaml
regex_id: 532f32c2fba5dd87435d5138eec457b7
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:598:25"
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

## usage_mismatch:5a49a964faf209bf291d4366cbcdada9:search

```yaml
regex_id: 5a49a964faf209bf291d4366cbcdada9
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Tools/scripts/mailerdaemon.py:92:4"
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

## usage_mismatch:5b0cdca423be21823805a122296f2e04:search

```yaml
regex_id: 5b0cdca423be21823805a122296f2e04
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:1471:18"
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

## usage_mismatch:5c6f4e2e0b80fd592f0b0e498cb11d16:search

```yaml
regex_id: 5c6f4e2e0b80fd592f0b0e498cb11d16
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/distutils/versionpredicate.py:156:24"
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

## usage_mismatch:5ebfc26ad57a8b6033550ddad06454e1:search

```yaml
regex_id: 5ebfc26ad57a8b6033550ddad06454e1
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Doc/tools/extensions/pyspecific.py:261:14"
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

## usage_mismatch:61cc24ed802fac49eddae1e2f0fd6265:search

```yaml
regex_id: 61cc24ed802fac49eddae1e2f0fd6265
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Tools/scripts/h2py.py:32:12"
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

## usage_mismatch:62141e81ee7e76c7ec11baf08d841de3:search

```yaml
regex_id: 62141e81ee7e76c7ec11baf08d841de3
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/http/cookiejar.py:520:10"
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

## usage_mismatch:6287234fbdeded81b6df95defdc336a4:search

```yaml
regex_id: 6287234fbdeded81b6df95defdc336a4
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/http/cookiejar.py:331:25"
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

## usage_mismatch:65a1ed6bc7a1172ac62731aacbef965c:search

```yaml
regex_id: 65a1ed6bc7a1172ac62731aacbef965c
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Tools/scripts/mailerdaemon.py:168:10"
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

## usage_mismatch:6682eca18d5921960c08543d2662c0c7:match

```yaml
regex_id: 6682eca18d5921960c08543d2662c0c7
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:605:26"
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

## usage_mismatch:693999cc639fdd84dd64ef393c987ff9:search

```yaml
regex_id: 693999cc639fdd84dd64ef393c987ff9
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/http/cookiejar.py:330:25"
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

## usage_mismatch:6b3f2d3d23f96637d3f81525623bd1f2:search

```yaml
regex_id: 6b3f2d3d23f96637d3f81525623bd1f2
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Tools/scripts/texi2html.py:1598:19"
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

## usage_mismatch:6b888295f43e02e8dda2708cce2286ba:search

```yaml
regex_id: 6b888295f43e02e8dda2708cce2286ba
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/distutils/versionpredicate.py:13:21"
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

## usage_mismatch:6e258bb3242c1a660d8a66a816f94310:match

```yaml
regex_id: 6e258bb3242c1a660d8a66a816f94310
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Tools/demo/ss1.py:417:16"
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

## usage_mismatch:6f7b35ada2253935070aaa6260112bc1:match

```yaml
regex_id: 6f7b35ada2253935070aaa6260112bc1
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:596:25"
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

## usage_mismatch:714f876cd9f7534387f37c4648ea499a:match

```yaml
regex_id: 714f876cd9f7534387f37c4648ea499a
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Tools/demo/ss1.py:436:12"
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

## intent_mismatch:772521efb1cb6c1486682a0d386e5eff:email

```yaml
regex_id: 772521efb1cb6c1486682a0d386e5eff
schema_version: "1"
kind: intent_mismatch
corpus: cpython
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/email/feedparser.py:37:11"
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

## usage_mismatch:772521efb1cb6c1486682a0d386e5eff:search

```yaml
regex_id: 772521efb1cb6c1486682a0d386e5eff
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/email/feedparser.py:37:11"
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

## usage_mismatch:7b04d9cd5dd8c07a65e7c7d835681f5a:match

```yaml
regex_id: 7b04d9cd5dd8c07a65e7c7d835681f5a
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/idlelib/paragraph.py:174:11"
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

## usage_mismatch:8611b33cb26beaf0deaa6203dcdd9d92:search

```yaml
regex_id: 8611b33cb26beaf0deaa6203dcdd9d92
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/nntplib.py:612:19"
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

## intent_mismatch:87c693424674a0106c367e75779b5c14:email

```yaml
regex_id: 87c693424674a0106c367e75779b5c14
schema_version: "1"
kind: intent_mismatch
corpus: cpython
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_email/test_email.py:5374:17"
```

### Pattern

`^--([^\n]+)\n(.*?)\n--\1$`

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

## usage_mismatch:87c693424674a0106c367e75779b5c14:search

```yaml
regex_id: 87c693424674a0106c367e75779b5c14
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_email/test_email.py:5374:17"
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

## usage_mismatch:87cc47f869002a678707ecd3e72c4116:match

```yaml
regex_id: 87cc47f869002a678707ecd3e72c4116
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:526:25"
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

## usage_mismatch:87ffdd95e2089caafe3202ae20d3fa22:search

```yaml
regex_id: 87ffdd95e2089caafe3202ae20d3fa22
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_smtplib.py:537:17"
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

## usage_mismatch:891664c2615cab51317d76185fa824f1:search

```yaml
regex_id: 891664c2615cab51317d76185fa824f1
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/logging/config.py:356:22"
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

## usage_mismatch:89eb92139276a99e912c8d59d12e4c64:match

```yaml
regex_id: 89eb92139276a99e912c8d59d12e4c64
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:595:25"
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

## usage_mismatch:8ad6f4a7a96be52948a2ecfe90850722:match

```yaml
regex_id: 8ad6f4a7a96be52948a2ecfe90850722
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:606:26"
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

## usage_mismatch:8c7903f3fe6841f7f14cd82423f7bfbb:search

```yaml
regex_id: 8c7903f3fe6841f7f14cd82423f7bfbb
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/logging/config.py:361:20"
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

## usage_mismatch:8eb1f48094d38660c04497473ec7c0ae:search

```yaml
regex_id: 8eb1f48094d38660c04497473ec7c0ae
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/lib2to3/pgen2/tokenize.py:227:12"
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

## usage_mismatch:8f391af712e8669d654ceb4b4fac3562:match

```yaml
regex_id: 8f391af712e8669d654ceb4b4fac3562
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:528:25"
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

## usage_mismatch:91b2a42ce9360b77d01ef873f3373c5a:match

```yaml
regex_id: 91b2a42ce9360b77d01ef873f3373c5a
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/msilib/__init__.py:181:11"
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

## usage_mismatch:928e14738ac13a449ea9acc63b864a61:match

```yaml
regex_id: 928e14738ac13a449ea9acc63b864a61
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:618:26"
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

## usage_mismatch:99e19b871d1262b4ef4b04817450e4b1:search

```yaml
regex_id: 99e19b871d1262b4ef4b04817450e4b1
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/unittest/test/test_case.py:1359:16"
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

## usage_mismatch:99f803af55a49f4f1faf5d6fa5f079e2:search

```yaml
regex_id: 99f803af55a49f4f1faf5d6fa5f079e2
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Tools/scripts/texi2html.py:81:9"
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

## usage_mismatch:9b43d24205f8f64ce2334cd9034d0512:search

```yaml
regex_id: 9b43d24205f8f64ce2334cd9034d0512
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/http/cookiejar.py:198:17"
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

## usage_mismatch:9d962b7c3fe371bc308487c22a4ab75b:search

```yaml
regex_id: 9d962b7c3fe371bc308487c22a4ab75b
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/http/cookiejar.py:437:23"
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

## usage_mismatch:a10e13c81468752256bd28fb4e9e586c:search

```yaml
regex_id: a10e13c81468752256bd28fb4e9e586c
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Tools/scripts/h2py.py:26:11"
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

## usage_mismatch:a352c95b21f9609284b15d860be65a49:search

```yaml
regex_id: a352c95b21f9609284b15d860be65a49
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/textwrap.py:411:22"
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

## usage_mismatch:a98324a8e381078776d3a6cfc67a4f8d:match

```yaml
regex_id: a98324a8e381078776d3a6cfc67a4f8d
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:565:26"
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

## usage_mismatch:aa4a1a18972d840b78ab966050f1a053:match

```yaml
regex_id: aa4a1a18972d840b78ab966050f1a053
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/lib2to3/pgen2/conv.py:71:17"
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

## usage_mismatch:b053ae94a80624c14449f21bf9d295b6:search

```yaml
regex_id: b053ae94a80624c14449f21bf9d295b6
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_regrtest.py:905:16"
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

## usage_mismatch:b056fab0e637c71fa879d96bce61de88:search

```yaml
regex_id: b056fab0e637c71fa879d96bce61de88
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/doctest.py:618:27"
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

## usage_mismatch:b313cc84287a209df6d7415e95019a0b:match

```yaml
regex_id: b313cc84287a209df6d7415e95019a0b
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:604:26"
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

## usage_mismatch:b326c9fd21d48f59c9ebf17ed5909fe3:match

```yaml
regex_id: b326c9fd21d48f59c9ebf17ed5909fe3
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:1343:29"
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

## usage_mismatch:b777dda2f1fb7a04adbf2cb279be4752:match

```yaml
regex_id: b777dda2f1fb7a04adbf2cb279be4752
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:610:24"
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

## usage_mismatch:ba48e630325d7c6ddc2024b516839db6:match

```yaml
regex_id: ba48e630325d7c6ddc2024b516839db6
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:616:24"
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

## usage_mismatch:ba6be78ee6ae4a807f209aef40bf0935:search

```yaml
regex_id: ba6be78ee6ae4a807f209aef40bf0935
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/email/header.py:48:7"
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

## usage_mismatch:ba7d655599c748c108b8b90b19a276bc:search

```yaml
regex_id: ba7d655599c748c108b8b90b19a276bc
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/urllib/request.py:306:15"
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

## usage_mismatch:bc01550b40e9ebd95515bc54057f1216:search

```yaml
regex_id: bc01550b40e9ebd95515bc54057f1216
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/idlelib/pyshell.py:1222:35"
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

## intent_mismatch:bfc6b1fc57011db1bce1523eae1b3b37:email

```yaml
regex_id: bfc6b1fc57011db1bce1523eae1b3b37
schema_version: "1"
kind: intent_mismatch
corpus: cpython
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/email/generator.py:22:7"
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

## usage_mismatch:bfc6b1fc57011db1bce1523eae1b3b37:search

```yaml
regex_id: bfc6b1fc57011db1bce1523eae1b3b37
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/email/generator.py:22:7"
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

## usage_mismatch:c1c5fa45d9f8eda8b2541f6c59e63cca:search

```yaml
regex_id: c1c5fa45d9f8eda8b2541f6c59e63cca
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/http/cookiejar.py:276:14"
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
   ([-+]?\d\d?:?(:?\d\d)?
    |Z|z)?               # timezone  (Z is "zero meridian", i.e. GMT)
      \s*$`

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

## usage_mismatch:c2e43b06df813ab08f30c0977ba50d90:search

```yaml
regex_id: c2e43b06df813ab08f30c0977ba50d90
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/pydoc.py:134:14"
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

## usage_mismatch:c628f06b8b6a69a9d3b7a70630c27888:search

```yaml
regex_id: c628f06b8b6a69a9d3b7a70630c27888
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/doctest.py:767:17"
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

## usage_mismatch:cc0cf73cf632f5613a0ffb08ffa4573c:search

```yaml
regex_id: cc0cf73cf632f5613a0ffb08ffa4573c
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/doctest.py:1406:30"
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

## usage_mismatch:cd9c2a68b00ec3fd68505cb8eb582d2e:search

```yaml
regex_id: cd9c2a68b00ec3fd68505cb8eb582d2e
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/http/cookiejar.py:127:14"
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

## usage_mismatch:cfe924d83040318626abff486dfbf5bc:search

```yaml
regex_id: cfe924d83040318626abff486dfbf5bc
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/logging/config.py:276:13"
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

## usage_mismatch:cff7314010cc637ff81b3130d094fb8f:match

```yaml
regex_id: cff7314010cc637ff81b3130d094fb8f
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:597:25"
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

## usage_mismatch:d0461157043886565881e5a7990c6fbc:match

```yaml
regex_id: d0461157043886565881e5a7990c6fbc
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:612:24"
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

## usage_mismatch:d11e1ad224c05b3589de35ed2c4d8610:search

```yaml
regex_id: d11e1ad224c05b3589de35ed2c4d8610
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_smtplib.py:135:19"
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

## usage_mismatch:d1656133d591e73aee77c39581a60054:match

```yaml
regex_id: d1656133d591e73aee77c39581a60054
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:599:25"
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

## usage_mismatch:d56fd5f3d9ae29e6f38898abecd684c8:search

```yaml
regex_id: d56fd5f3d9ae29e6f38898abecd684c8
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_smtplib.py:472:17"
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

## usage_mismatch:d74105fb82635ebc169dec5437ca3dec:search

```yaml
regex_id: d74105fb82635ebc169dec5437ca3dec
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/tokenize.py:37:12"
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

## usage_mismatch:da1d5c315d8842642cf9a25045f5bdf7:search

```yaml
regex_id: da1d5c315d8842642cf9a25045f5bdf7
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/_pydecimal.py:6134:13"
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

## usage_mismatch:daa4f2bedf4c44bc4ba82a72d96bb0fb:search

```yaml
regex_id: daa4f2bedf4c44bc4ba82a72d96bb0fb
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_smtplib.py:445:17"
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

## usage_mismatch:db54956a0d95bd081f09dc71fd94bd45:match

```yaml
regex_id: db54956a0d95bd081f09dc71fd94bd45
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:524:25"
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

## usage_mismatch:e0071923a65afcfc4217f012324935c8:match

```yaml
regex_id: e0071923a65afcfc4217f012324935c8
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:518:25"
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

## usage_mismatch:e0c39f7b0fa46c40421c3bd2fb6bdded:search

```yaml
regex_id: e0c39f7b0fa46c40421c3bd2fb6bdded
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/http/cookiejar.py:605:14"
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

## usage_mismatch:e1c8692a00e296b5cd1d831b0183ea04:match

```yaml
regex_id: e1c8692a00e296b5cd1d831b0183ea04
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:521:26"
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

## usage_mismatch:e4292d812c29deaabafc31df1faa0535:match

```yaml
regex_id: e4292d812c29deaabafc31df1faa0535
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:603:26"
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

## usage_mismatch:e58e9f6f20009794f1e3bfe9f31732c8:match

```yaml
regex_id: e58e9f6f20009794f1e3bfe9f31732c8
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:609:24"
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

## usage_mismatch:e5db3f91d57e0757be16f678a4730eb8:match

```yaml
regex_id: e5db3f91d57e0757be16f678a4730eb8
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:516:25"
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

## usage_mismatch:e8ab8c675e7a50fc4c010262bb2d498c:match

```yaml
regex_id: e8ab8c675e7a50fc4c010262bb2d498c
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:590:26"
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

## usage_mismatch:e96d0c9af9d2c3479b4cd9bba4add0a7:search

```yaml
regex_id: e96d0c9af9d2c3479b4cd9bba4add0a7
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/configparser.py:1312:16"
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

## usage_mismatch:ea108b99612a432b9dba16393b44cc84:match

```yaml
regex_id: ea108b99612a432b9dba16393b44cc84
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:591:26"
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

## usage_mismatch:eb204ddf53b4271589ba4680637cf879:match

```yaml
regex_id: eb204ddf53b4271589ba4680637cf879
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:560:25"
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

## usage_mismatch:ebb9d2a4c7e34e9ac0a471dd4e8dc417:match

```yaml
regex_id: ebb9d2a4c7e34e9ac0a471dd4e8dc417
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:568:25"
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

## usage_mismatch:ec1fbad6e22f508601c040384572bf4a:search

```yaml
regex_id: ec1fbad6e22f508601c040384572bf4a
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/unittest/test/test_case.py:1310:46"
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

## usage_mismatch:ee859c9323ed23ceb1b1fa4da9389b1f:search

```yaml
regex_id: ee859c9323ed23ceb1b1fa4da9389b1f
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_smtplib.py:478:16"
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

## usage_mismatch:f0d336a1795d8fc043f3746e304c3f79:search

```yaml
regex_id: f0d336a1795d8fc043f3746e304c3f79
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/distutils/versionpredicate.py:12:11"
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

## usage_mismatch:f3771af26ddfc060a67653a7593a9c9d:search

```yaml
regex_id: f3771af26ddfc060a67653a7593a9c9d
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Tools/scripts/texi2html.py:74:9"
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

## usage_mismatch:f5e4949ffdc4446731c1c4940b2971db:search

```yaml
regex_id: f5e4949ffdc4446731c1c4940b2971db
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/_pydecimal.py:6135:14"
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

## usage_mismatch:f81d82cd84d357d8d3421fafa2b2178d:search

```yaml
regex_id: f81d82cd84d357d8d3421fafa2b2178d
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/idlelib/iomenu.py:68:12"
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

## usage_mismatch:f97b4daade7f7b1f1d143b8e374b67bf:search

```yaml
regex_id: f97b4daade7f7b1f1d143b8e374b67bf
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/http/cookiejar.py:1232:14"
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

## usage_mismatch:fac261b42765d2104f63411d100200ea:search

```yaml
regex_id: fac261b42765d2104f63411d100200ea
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/logging/config.py:359:18"
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

## usage_mismatch:fb3d5b5925cedfa07cee26ff09065b3d:search

```yaml
regex_id: fb3d5b5925cedfa07cee26ff09065b3d
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:511:12"
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

## usage_mismatch:fdc4ee99b1a465a95a392689b351a26e:match

```yaml
regex_id: fdc4ee99b1a465a95a392689b351a26e
schema_version: "1"
kind: usage_mismatch
corpus: cpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython/rules/Lib/test/test_re.py:520:26"
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

## property:inventory:rc-shape1-injection-alphabet:rc-shape1-injection-alphabet

```yaml
regex_id: "inventory:rc-shape1-injection-alphabet"
schema_version: "1"
kind: property
corpus: cpython
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
corpus: cpython
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
corpus: cpython
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
corpus: cpython
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

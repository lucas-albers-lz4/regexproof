---
schema_version: "1"
corpus: cpython-13
findings: 131
---

# cpython-13 batch findings

## usage_mismatch:0172faf79864c3dca6db8d4c533d34fb:search

```yaml
regex_id: 0172faf79864c3dca6db8d4c533d34fb
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/doctest.py:771:27"
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

## usage_mismatch:041b09ec5012fdb3000ef3758877ef67:search

```yaml
regex_id: 041b09ec5012fdb3000ef3758877ef67
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/http/cookiejar.py:535:10"
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

## usage_mismatch:083aa08b0799249a543e1603fc839b70:match

```yaml
regex_id: 083aa08b0799249a543e1603fc839b70
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:769:24"
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

## usage_mismatch:095f7b4b0d72caa602f5bdc540dd542e:match

```yaml
regex_id: 095f7b4b0d72caa602f5bdc540dd542e
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:1750:30"
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

## usage_mismatch:0a540ba0cee22cf812b5ac4ecae251d7:search

```yaml
regex_id: 0a540ba0cee22cf812b5ac4ecae251d7
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/logging/config.py:294:13"
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

## usage_mismatch:0e00e5bc362f4c2eec4a32dd9e43877e:match

```yaml
regex_id: 0e00e5bc362f4c2eec4a32dd9e43877e
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:741:26"
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

## usage_mismatch:0eaa4491beb6e67c967ae507c9016add:search

```yaml
regex_id: 0eaa4491beb6e67c967ae507c9016add
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:2021:12"
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

## usage_mismatch:10cacc852c21afcb818e9b19be4dc966:search

```yaml
regex_id: 10cacc852c21afcb818e9b19be4dc966
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:805:25"
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

## usage_mismatch:111fca3641dc8db757bfa5ac8d2f2508:search

```yaml
regex_id: 111fca3641dc8db757bfa5ac8d2f2508
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Doc/tools/extensions/misc_news.py:33:38"
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

## usage_mismatch:119eadcdacb541b32ea7b04732478c9b:search

```yaml
regex_id: 119eadcdacb541b32ea7b04732478c9b
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/logging/config.py:378:20"
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

## usage_mismatch:14f826999535787e2fd3da720e384a52:search

```yaml
regex_id: 14f826999535787e2fd3da720e384a52
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/http/cookiejar.py:1260:15"
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

## usage_mismatch:179701ccf9fb066eae039b690327bcda:match

```yaml
regex_id: 179701ccf9fb066eae039b690327bcda
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:2532:24"
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

## usage_mismatch:187d419c7e560a3483df6d64ebb07f8b:search

```yaml
regex_id: 187d419c7e560a3483df6d64ebb07f8b
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/http/cookiejar.py:288:14"
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

## usage_mismatch:19f57036089c64d5918a9abeab1cba5a:match

```yaml
regex_id: 19f57036089c64d5918a9abeab1cba5a
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:750:25"
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

## intent_mismatch:1b1090e2bf2e22c9b885850ff5ae48fa:email

```yaml
regex_id: 1b1090e2bf2e22c9b885850ff5ae48fa
schema_version: "1"
kind: intent_mismatch
corpus: cpython-13
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/email/feedparser.py:37:11"
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

## usage_mismatch:1b1090e2bf2e22c9b885850ff5ae48fa:search

```yaml
regex_id: 1b1090e2bf2e22c9b885850ff5ae48fa
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/email/feedparser.py:37:11"
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

## usage_mismatch:1e0a98a9e70df6e8cac10a6f506cddb2:match

```yaml
regex_id: 1e0a98a9e70df6e8cac10a6f506cddb2
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:637:25"
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

## usage_mismatch:200b9745b394a84f06f616d063f9a250:search

```yaml
regex_id: 200b9745b394a84f06f616d063f9a250
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/_pydecimal.py:6076:13"
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

## usage_mismatch:2089ca83279637037b2e726445530e5e:match

```yaml
regex_id: 2089ca83279637037b2e726445530e5e
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:764:24"
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

## usage_mismatch:2543c4a440d52529c51a49583785b115:match

```yaml
regex_id: 2543c4a440d52529c51a49583785b115
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:714:26"
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

## usage_mismatch:2dd741ab21807698804d3c0c7666891c:match

```yaml
regex_id: 2dd741ab21807698804d3c0c7666891c
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:2524:26"
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

## usage_mismatch:2e544597527ce5fb56ee0cabe7547ca8:search

```yaml
regex_id: 2e544597527ce5fb56ee0cabe7547ca8
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/configparser.py:1339:16"
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

## usage_mismatch:2eeef5758c32e7ad5a73699a38e66ffa:search

```yaml
regex_id: 2eeef5758c32e7ad5a73699a38e66ffa
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/logging/__init__.py:482:15"
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

## usage_mismatch:33bd12304c6bf0d072229c976c28299f:search

```yaml
regex_id: 33bd12304c6bf0d072229c976c28299f
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Android/android.py:160:20"
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

## usage_mismatch:36e3ce27a66bb0ed0de6c87f3aea2f33:search

```yaml
regex_id: 36e3ce27a66bb0ed0de6c87f3aea2f33
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:1442:28"
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

## usage_mismatch:38d0a8c4077790db34e44b695348bebd:search

```yaml
regex_id: 38d0a8c4077790db34e44b695348bebd
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/platform.py:1408:22"
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

## usage_mismatch:3957e0ef6690781298d1543b3407e353:match

```yaml
regex_id: 3957e0ef6690781298d1543b3407e353
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:748:25"
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

## usage_mismatch:3ad0fb930bf1158ca190303922967b99:search

```yaml
regex_id: 3ad0fb930bf1158ca190303922967b99
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/http/cookiejar.py:620:14"
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

## usage_mismatch:3b992ab4fbfd83b46e748d960917b863:match

```yaml
regex_id: 3b992ab4fbfd83b46e748d960917b863
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:759:24"
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

## usage_mismatch:3bf7e398bd17bab08566268e40f5cf54:search

```yaml
regex_id: 3bf7e398bd17bab08566268e40f5cf54
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/logging/config.py:377:18"
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

## usage_mismatch:3fd15f033983db12e01c5f6a60362298:search

```yaml
regex_id: 3fd15f033983db12e01c5f6a60362298
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/http/cookiejar.py:211:21"
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

## usage_mismatch:40c53a02144cb9363962468c33d7b93d:search

```yaml
regex_id: 40c53a02144cb9363962468c33d7b93d
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_pyrepl/test_pyrepl.py:1188:24"
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

## usage_mismatch:40e6035d191c91e6723cc9d16cdce6a4:match

```yaml
regex_id: 40e6035d191c91e6723cc9d16cdce6a4
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:760:24"
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

## usage_mismatch:4461675b7edd16af2a97f2f062702b30:match

```yaml
regex_id: 4461675b7edd16af2a97f2f062702b30
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:2517:26"
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

## usage_mismatch:509408678fa8fbb4f1114eb0540766ac:match

```yaml
regex_id: 509408678fa8fbb4f1114eb0540766ac
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:641:26"
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

## usage_mismatch:5219cc8da7b27be1670d2195478a2df5:search

```yaml
regex_id: 5219cc8da7b27be1670d2195478a2df5
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/http/cookiejar.py:345:25"
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

## usage_mismatch:52c509f09d96e5f042b5c3007acd21be:search

```yaml
regex_id: 52c509f09d96e5f042b5c3007acd21be
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_smtplib.py:635:17"
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

## usage_mismatch:54c7d169e73d3a7279421aa67f38bb08:match

```yaml
regex_id: 54c7d169e73d3a7279421aa67f38bb08
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:766:24"
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

## usage_mismatch:55bb7c47d1243ae210f2d21d86771d14:search

```yaml
regex_id: 55bb7c47d1243ae210f2d21d86771d14
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_smtplib.py:672:17"
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

## usage_mismatch:58f89bfede5b1b2c1e953151411bd04d:search

```yaml
regex_id: 58f89bfede5b1b2c1e953151411bd04d
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/_pydecimal.py:6077:14"
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

## usage_mismatch:5bdc50320734a0b9cbb87ee759eb0888:search

```yaml
regex_id: 5bdc50320734a0b9cbb87ee759eb0888
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/doctest.py:653:27"
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

## usage_mismatch:5cc3172ab090cf11e88c60c75ca72982:match

```yaml
regex_id: 5cc3172ab090cf11e88c60c75ca72982
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:765:24"
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

## usage_mismatch:5e239da01c71c3f0cc50da573dc17639:search

```yaml
regex_id: 5e239da01c71c3f0cc50da573dc17639
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:1825:18"
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

## usage_mismatch:5ed1ee2231e68c5cf4607b1f6ace1cb0:search

```yaml
regex_id: 5ed1ee2231e68c5cf4607b1f6ace1cb0
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Tools/c-analyzer/c_parser/preprocessor/gcc.py:36:17"
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

## usage_mismatch:5f23e353adfca95313b0b6496c10852e:search

```yaml
regex_id: 5f23e353adfca95313b0b6496c10852e
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/http/cookiejar.py:209:13"
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

## usage_mismatch:64103059c2b9e5f4788a2c470c66559d:search

```yaml
regex_id: 64103059c2b9e5f4788a2c470c66559d
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/doctest.py:802:17"
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

## usage_mismatch:65197960f51803293720209a044cd196:search

```yaml
regex_id: 65197960f51803293720209a044cd196
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/idlelib/pyshell.py:1341:35"
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

## usage_mismatch:65c74dfd555a25c69bb0aa2114a0dab9:search

```yaml
regex_id: 65c74dfd555a25c69bb0aa2114a0dab9
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_smtplib.py:609:16"
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

## usage_mismatch:695ae01f0b6898c70fc747f97031351c:match

```yaml
regex_id: 695ae01f0b6898c70fc747f97031351c
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:716:25"
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

## usage_mismatch:6a86a93096f3ca79281a1acf2add2d13:match

```yaml
regex_id: 6a86a93096f3ca79281a1acf2add2d13
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:763:24"
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

## usage_mismatch:6ac5be2ab7fbdfa42472a648727ee426:search

```yaml
regex_id: 6ac5be2ab7fbdfa42472a648727ee426
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/idlelib/pyshell.py:1340:35"
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

## usage_mismatch:6b22949c28331b16d3c7dc502e945901:search

```yaml
regex_id: 6b22949c28331b16d3c7dc502e945901
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/textwrap.py:416:22"
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

## usage_mismatch:6bf0e45fef532dd8864ef61a0f62d699:match

```yaml
regex_id: 6bf0e45fef532dd8864ef61a0f62d699
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:645:25"
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

## usage_mismatch:6c585f3b871ac3a8c1929c1a3152a80f:match

```yaml
regex_id: 6c585f3b871ac3a8c1929c1a3152a80f
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:745:25"
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

## usage_mismatch:6cac74acd667be2c4d1f09a977424aad:match

```yaml
regex_id: 6cac74acd667be2c4d1f09a977424aad
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:758:24"
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

## usage_mismatch:6d621fae959722d2d632280ea4978073:search

```yaml
regex_id: 6d621fae959722d2d632280ea4978073
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_regrtest.py:1416:16"
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

## usage_mismatch:6e19c727a359596bfdd18adf37cdf92c:search

```yaml
regex_id: 6e19c727a359596bfdd18adf37cdf92c
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:632:12"
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

## usage_mismatch:6ed90e0cb33b55dc09e40bc86acad66d:match

```yaml
regex_id: 6ed90e0cb33b55dc09e40bc86acad66d
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:2525:26"
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

## usage_mismatch:7015fad118ff178ab81d28f58f71fd34:match

```yaml
regex_id: 7015fad118ff178ab81d28f58f71fd34
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:754:26"
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

## usage_mismatch:72e27b8622f8e730d493b61c81694537:match

```yaml
regex_id: 72e27b8622f8e730d493b61c81694537
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:1741:29"
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

## usage_mismatch:7946450becc9592b6e36e2125e921d33:match

```yaml
regex_id: 7946450becc9592b6e36e2125e921d33
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:649:25"
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

## usage_mismatch:79fce9ae1cb02494b18f01c4a20fca22:match

```yaml
regex_id: 79fce9ae1cb02494b18f01c4a20fca22
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:739:26"
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

## usage_mismatch:7a32e252dd4cf87c4b5e19377b6d3946:match

```yaml
regex_id: 7a32e252dd4cf87c4b5e19377b6d3946
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:761:24"
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

## intent_mismatch:7a8e373f3ab0c3e943cb61c066735a1b:email

```yaml
regex_id: 7a8e373f3ab0c3e943cb61c066735a1b
schema_version: "1"
kind: intent_mismatch
corpus: cpython-13
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/email/_header_value_parser.py:116:18"
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
{"admitted_char": "' '", "keyword": "email", "reason": "name/comment claims validation but pattern admits excluded char"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7ca3a29c7893bb26e9df36368e64d2e0:search

```yaml
regex_id: 7ca3a29c7893bb26e9df36368e64d2e0
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_unittest/test_case.py:1455:16"
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

## usage_mismatch:7d9b5a7574dc44c0837915cf9349eaed:match

```yaml
regex_id: 7d9b5a7574dc44c0837915cf9349eaed
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:756:26"
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

## usage_mismatch:7f539b78ec12ed5e2be8dfe2a2088e95:search

```yaml
regex_id: 7f539b78ec12ed5e2be8dfe2a2088e95
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_smtplib.py:148:19"
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

## usage_mismatch:800e21f3c0f03088d82588ff11c42ed8:match

```yaml
regex_id: 800e21f3c0f03088d82588ff11c42ed8
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:2529:24"
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

## usage_mismatch:80b4eabe9a97c53d4946abf05ff888fe:search

```yaml
regex_id: 80b4eabe9a97c53d4946abf05ff888fe
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/email/utils.py:392:23"
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

## usage_mismatch:833f9355cf612f614485d65777172bba:search

```yaml
regex_id: 833f9355cf612f614485d65777172bba
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/logging/config.py:379:20"
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

## usage_mismatch:8685814d62125bfdf0e5716ad2f67036:match

```yaml
regex_id: 8685814d62125bfdf0e5716ad2f67036
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:751:25"
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

## intent_mismatch:88ad47dde9d5d34a9954f2c44f0344dd:email

```yaml
regex_id: 88ad47dde9d5d34a9954f2c44f0344dd
schema_version: "1"
kind: intent_mismatch
corpus: cpython-13
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/email/feedparser.py:40:16"
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

## usage_mismatch:88ad47dde9d5d34a9954f2c44f0344dd:search

```yaml
regex_id: 88ad47dde9d5d34a9954f2c44f0344dd
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/email/feedparser.py:40:16"
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

## usage_mismatch:89f56105cd214f2ca14e9465561b5128:search

```yaml
regex_id: 89f56105cd214f2ca14e9465561b5128
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/http/cookiejar.py:346:25"
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

## usage_mismatch:8dcda9f12be94c7eb80ecaccdfe37801:match

```yaml
regex_id: 8dcda9f12be94c7eb80ecaccdfe37801
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:746:25"
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

## usage_mismatch:8de16548a41160cac109e73d8b72aff9:match

```yaml
regex_id: 8de16548a41160cac109e73d8b72aff9
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:642:26"
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

## usage_mismatch:8ec52b05946031e5f4bb55be16f6ec44:match

```yaml
regex_id: 8ec52b05946031e5f4bb55be16f6ec44
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:2527:24"
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

## usage_mismatch:94b1729c3cd7812c57d99929a2a51569:match

```yaml
regex_id: 94b1729c3cd7812c57d99929a2a51569
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:643:25"
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

## usage_mismatch:990cbb3a7da5e8403857d75a9212eec2:search

```yaml
regex_id: 990cbb3a7da5e8403857d75a9212eec2
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_smtplib.py:491:17"
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

## usage_mismatch:9a2e1730f9b4af8924e6595537c2bd1c:search

```yaml
regex_id: 9a2e1730f9b4af8924e6595537c2bd1c
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Tools/c-analyzer/c_parser/preprocessor/gcc.py:37:23"
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

## usage_mismatch:a0042373531ee0fbdbfbc9e704965eaf:search

```yaml
regex_id: a0042373531ee0fbdbfbc9e704965eaf
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/doctest.py:1496:30"
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

## usage_mismatch:a00f773200c92f304c66112746430220:match

```yaml
regex_id: a00f773200c92f304c66112746430220
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:740:26"
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

## usage_mismatch:a0d979d0bbdcc1833f452a5b88bd0916:match

```yaml
regex_id: a0d979d0bbdcc1833f452a5b88bd0916
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:753:26"
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

## usage_mismatch:a1956c96a4c54cf024e3701ea5219938:match

```yaml
regex_id: a1956c96a4c54cf024e3701ea5219938
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:710:25"
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

## usage_mismatch:a1b98c511fb67775a9743edbd925f5b4:search

```yaml
regex_id: a1b98c511fb67775a9743edbd925f5b4
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:806:25"
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

## usage_mismatch:a3be9d974da2b468b4de72deadac95b9:match

```yaml
regex_id: a3be9d974da2b468b4de72deadac95b9
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:2531:26"
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

## usage_mismatch:a5d9e4f261d03b5a4bbccdb4952ffef6:match

```yaml
regex_id: a5d9e4f261d03b5a4bbccdb4952ffef6
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:755:26"
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

## usage_mismatch:a694697be386b679575e85165e26b152:match

```yaml
regex_id: a694697be386b679575e85165e26b152
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:2522:25"
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

## usage_mismatch:a7efeb9b5981cc83b85fce3952d1cc0d:search

```yaml
regex_id: a7efeb9b5981cc83b85fce3952d1cc0d
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/logging/__init__.py:483:17"
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

## usage_mismatch:a892c25f3aaccb9ee5feae35870f7d53:match

```yaml
regex_id: a892c25f3aaccb9ee5feae35870f7d53
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:2518:26"
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

## intent_mismatch:a94a4f929cf642d0ef9e25c79f4fdf9e:email

```yaml
regex_id: a94a4f929cf642d0ef9e25c79f4fdf9e
schema_version: "1"
kind: intent_mismatch
corpus: cpython-13
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_email/test_email.py:5780:17"
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

## usage_mismatch:a94a4f929cf642d0ef9e25c79f4fdf9e:search

```yaml
regex_id: a94a4f929cf642d0ef9e25c79f4fdf9e
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_email/test_email.py:5780:17"
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

## usage_mismatch:a9929e6ed18c92975a0322489623f872:search

```yaml
regex_id: a9929e6ed18c92975a0322489623f872
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/urllib/request.py:270:15"
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

## usage_mismatch:abe3f1e9388f2564ab5f9620c0b72de1:match

```yaml
regex_id: abe3f1e9388f2564ab5f9620c0b72de1
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:2528:24"
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

## usage_mismatch:aecbff56b2d91aec5294b31a64ff9417:search

```yaml
regex_id: aecbff56b2d91aec5294b31a64ff9417
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/http/cookiejar.py:1258:14"
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

## usage_mismatch:af9f1517f8c787c37b7acab932843212:match

```yaml
regex_id: af9f1517f8c787c37b7acab932843212
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/idlelib/format.py:181:11"
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

## usage_mismatch:aff2509a469f8ee1def997954180c207:match

```yaml
regex_id: aff2509a469f8ee1def997954180c207
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:2521:25"
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

## usage_mismatch:b0613441d92cfea672a69bfc9dfadda9:search

```yaml
regex_id: b0613441d92cfea672a69bfc9dfadda9
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:807:26"
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

## usage_mismatch:b1affed40ea4c6c11d577a7e6be4e3a4:search

```yaml
regex_id: b1affed40ea4c6c11d577a7e6be4e3a4
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/http/cookiejar.py:135:14"
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

## usage_mismatch:b1e63effd94741c3be7fe23b7e83bda0:search

```yaml
regex_id: b1e63effd94741c3be7fe23b7e83bda0
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/logging/config.py:374:22"
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

## usage_mismatch:b25c3f2ecc80c764d1666745d79c910d:search

```yaml
regex_id: b25c3f2ecc80c764d1666745d79c910d
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/http/cookiejar.py:344:25"
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

## usage_mismatch:b6d867653da9baeb9235f4832a6fabea:search

```yaml
regex_id: b6d867653da9baeb9235f4832a6fabea
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/email/header.py:48:7"
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

## usage_mismatch:b77aa549cbb8ba6cfe2ca35f3a928bdf:match

```yaml
regex_id: b77aa549cbb8ba6cfe2ca35f3a928bdf
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:639:25"
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

## usage_mismatch:b8d20f2cf4e4d27185dada881da5854e:match

```yaml
regex_id: b8d20f2cf4e4d27185dada881da5854e
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:749:25"
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

## usage_mismatch:b8ff4124bfa20f100089a6c49ab47502:match

```yaml
regex_id: b8ff4124bfa20f100089a6c49ab47502
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:715:26"
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

## usage_mismatch:ba6e0a20ddcfdf77b73dac0d85be0a3f:search

```yaml
regex_id: ba6e0a20ddcfdf77b73dac0d85be0a3f
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/tokenize.py:39:12"
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

## intent_mismatch:bb35edb9daeae18c8c69bb4690ad3de0:email

```yaml
regex_id: bb35edb9daeae18c8c69bb4690ad3de0
schema_version: "1"
kind: intent_mismatch
corpus: cpython-13
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/email/header.py:35:7"
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

## usage_mismatch:bdd844b599216449fe639c5a042fdce2:search

```yaml
regex_id: bdd844b599216449fe639c5a042fdce2
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/http/cookiejar.py:206:17"
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

## usage_mismatch:bf0f0028711154c785546beaf74c4ce2:search

```yaml
regex_id: bf0f0028711154c785546beaf74c4ce2
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:1830:18"
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

## intent_mismatch:bf2ee6b4e38179c17add00ac410b84df:email

```yaml
regex_id: bf2ee6b4e38179c17add00ac410b84df
schema_version: "1"
kind: intent_mismatch
corpus: cpython-13
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/email/generator.py:23:7"
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

## usage_mismatch:bf2ee6b4e38179c17add00ac410b84df:search

```yaml
regex_id: bf2ee6b4e38179c17add00ac410b84df
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/email/generator.py:23:7"
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

## usage_mismatch:c5a7da60ab1cae27444a1fc8ea059f1c:match

```yaml
regex_id: c5a7da60ab1cae27444a1fc8ea059f1c
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:768:26"
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

## usage_mismatch:c69801fe7945f0f2119cf54d0224ec8a:search

```yaml
regex_id: c69801fe7945f0f2119cf54d0224ec8a
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_smtplib.py:158:19"
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

## usage_mismatch:d161eeb7e22ee7a86c276ed9cdf01d8c:match

```yaml
regex_id: d161eeb7e22ee7a86c276ed9cdf01d8c
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:747:25"
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

## usage_mismatch:d3c8f5dd3aeb3c31bb20a9056b1634d8:search

```yaml
regex_id: d3c8f5dd3aeb3c31bb20a9056b1634d8
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_smtplib.py:603:17"
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

## usage_mismatch:d3e54ac1837fad5f708e4068c265f59c:search

```yaml
regex_id: d3e54ac1837fad5f708e4068c265f59c
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/logging/config.py:376:19"
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

## usage_mismatch:d82dc3f96128f1a3b218452829b4b855:match

```yaml
regex_id: d82dc3f96128f1a3b218452829b4b855
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:762:24"
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

## usage_mismatch:dc9a43083a0cc1c0804b4132eb76f340:search

```yaml
regex_id: dc9a43083a0cc1c0804b4132eb76f340
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_smtplib.py:544:17"
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

## usage_mismatch:dd4589d1ae5e87b2be8f9297ea0ac373:match

```yaml
regex_id: dd4589d1ae5e87b2be8f9297ea0ac373
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:742:26"
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

## usage_mismatch:df7c14265c4cc68e68eb828a13d402d1:match

```yaml
regex_id: df7c14265c4cc68e68eb828a13d402d1
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:647:25"
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

## usage_mismatch:e29a4ea95b589a6215bad20c233837c2:search

```yaml
regex_id: e29a4ea95b589a6215bad20c233837c2
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_unittest/test_case.py:1393:46"
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

## usage_mismatch:e79b16a0c5115f2b5f38ebf110f7641f:search

```yaml
regex_id: e79b16a0c5115f2b5f38ebf110f7641f
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/pydoc.py:274:14"
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

## usage_mismatch:e933bf8ac9bd56f340ba947df211d789:match

```yaml
regex_id: e933bf8ac9bd56f340ba947df211d789
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:718:25"
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

## usage_mismatch:ea1b6c9160a921563f78a9f0bb4ce1a1:match

```yaml
regex_id: ea1b6c9160a921563f78a9f0bb4ce1a1
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:2520:25"
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

## usage_mismatch:eca8173122145719a38251a0c490d3e5:match

```yaml
regex_id: eca8173122145719a38251a0c490d3e5
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:744:25"
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

## usage_mismatch:f09c777dcf0bd8f21318680aca41e159:search

```yaml
regex_id: f09c777dcf0bd8f21318680aca41e159
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_smtplib.py:574:17"
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

## usage_mismatch:fea347cdab22064100c19b9e30c11fe9:match

```yaml
regex_id: fea347cdab22064100c19b9e30c11fe9
schema_version: "1"
kind: usage_mismatch
corpus: cpython-13
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cpython-13/rules/Lib/test/test_re.py:712:25"
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

## property:inventory:rc-shape1-injection-alphabet:rc-shape1-injection-alphabet

```yaml
regex_id: "inventory:rc-shape1-injection-alphabet"
schema_version: "1"
kind: property
corpus: cpython-13
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
corpus: cpython-13
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
corpus: cpython-13
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
corpus: cpython-13
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

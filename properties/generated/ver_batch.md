---
schema_version: "1"
corpus: ver
findings: 132
---

# ver batch findings

## usage_mismatch:0374099d11b03c174bd31b2ab0c61ca9:search

```yaml
regex_id: 0374099d11b03c174bd31b2ab0c61ca9
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/logging/config.py:376:19"
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

## usage_mismatch:05302e63a4a46bfc127eb7c22f64030f:match

```yaml
regex_id: 05302e63a4a46bfc127eb7c22f64030f
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:718:25"
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

## usage_mismatch:061cbbe03e8d36736d39f2b139bd9286:match

```yaml
regex_id: 061cbbe03e8d36736d39f2b139bd9286
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:742:26"
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

## usage_mismatch:06eb3b541cba66f3d59412d4c2792149:match

```yaml
regex_id: 06eb3b541cba66f3d59412d4c2792149
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:2524:24"
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

## usage_mismatch:07a0b12a3da1ea25b91fe67f92d24c94:search

```yaml
regex_id: 07a0b12a3da1ea25b91fe67f92d24c94
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/logging/config.py:377:18"
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

## usage_mismatch:07e3ee210d33d80c6b702d868a6076f5:search

```yaml
regex_id: 07e3ee210d33d80c6b702d868a6076f5
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_smtplib.py:148:19"
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

## usage_mismatch:0838cc251ff2a79ec8a4f919dbbb4ed8:search

```yaml
regex_id: 0838cc251ff2a79ec8a4f919dbbb4ed8
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:1831:18"
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

## usage_mismatch:0e3e9a83fd992c276a51e99e1f9b30ca:search

```yaml
regex_id: 0e3e9a83fd992c276a51e99e1f9b30ca
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/configparser.py:1374:16"
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

## usage_mismatch:13762b24dce25574c3119e10362340e8:match

```yaml
regex_id: 13762b24dce25574c3119e10362340e8
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:2523:24"
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

## usage_mismatch:1448025d5eb4cb31dd172b655e726fb3:match

```yaml
regex_id: 1448025d5eb4cb31dd172b655e726fb3
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:746:25"
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

## usage_mismatch:154f3393d9a3b5dbecf912e6f1292527:search

```yaml
regex_id: 154f3393d9a3b5dbecf912e6f1292527
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:632:12"
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

## usage_mismatch:15e6312490fbefceab3c5b0aa6e4c816:search

```yaml
regex_id: 15e6312490fbefceab3c5b0aa6e4c816
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/http/cookiejar.py:211:21"
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

## usage_mismatch:1830c20ab33f0e11bd55cc1f1ae268d9:match

```yaml
regex_id: 1830c20ab33f0e11bd55cc1f1ae268d9
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:760:24"
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

## usage_mismatch:194a80b705ea6e1473a1eca7829f04e3:search

```yaml
regex_id: 194a80b705ea6e1473a1eca7829f04e3
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/doctest.py:1498:30"
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

## usage_mismatch:1aadde8f51e1bb49b7324f2d8382bc0b:search

```yaml
regex_id: 1aadde8f51e1bb49b7324f2d8382bc0b
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_regrtest.py:1419:16"
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

## usage_mismatch:1c0f4f219674623bf0b2ff6b2625f365:search

```yaml
regex_id: 1c0f4f219674623bf0b2ff6b2625f365
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/platform.py:1425:22"
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

## usage_mismatch:1d5cb819e14a4339d6536528d5f3c07d:search

```yaml
regex_id: 1d5cb819e14a4339d6536528d5f3c07d
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_smtplib.py:574:17"
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

## usage_mismatch:1ece282cefb637b62f69bb4ef1250519:match

```yaml
regex_id: 1ece282cefb637b62f69bb4ef1250519
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:2527:24"
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

## usage_mismatch:1fdc663a813d89689718a562ae519697:match

```yaml
regex_id: 1fdc663a813d89689718a562ae519697
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:2515:25"
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

## usage_mismatch:2034e88272f7a34495aa2080e39cb9cd:search

```yaml
regex_id: 2034e88272f7a34495aa2080e39cb9cd
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/doctest.py:773:27"
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

## intent_mismatch:21515c06a3b2441809020d45d52d807e:email

```yaml
regex_id: 21515c06a3b2441809020d45d52d807e
schema_version: "1"
kind: intent_mismatch
corpus: ver
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/email/header.py:35:7"
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

## usage_mismatch:217aff215b9951d8b781eed6c7823a2b:match

```yaml
regex_id: 217aff215b9951d8b781eed6c7823a2b
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:2517:25"
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

## usage_mismatch:25cf6e7d125c19578c56b9cc46cf1007:match

```yaml
regex_id: 25cf6e7d125c19578c56b9cc46cf1007
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:755:26"
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

## usage_mismatch:27ac7c95e8dbf4f82087b66f92186adf:match

```yaml
regex_id: 27ac7c95e8dbf4f82087b66f92186adf
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:2516:25"
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

## intent_mismatch:2a007bd823262e91528f259e38076f5e:email

```yaml
regex_id: 2a007bd823262e91528f259e38076f5e
schema_version: "1"
kind: intent_mismatch
corpus: ver
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/email/generator.py:23:7"
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

## usage_mismatch:2a007bd823262e91528f259e38076f5e:search

```yaml
regex_id: 2a007bd823262e91528f259e38076f5e
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/email/generator.py:23:7"
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

## usage_mismatch:2a2126a625f52f078d13af44212af1c5:search

```yaml
regex_id: 2a2126a625f52f078d13af44212af1c5
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_smtplib.py:609:16"
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

## usage_mismatch:2dbed35c1c5e549f4a5f71be895d7b18:match

```yaml
regex_id: 2dbed35c1c5e549f4a5f71be895d7b18
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/idlelib/format.py:181:11"
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

## usage_mismatch:2e0bc6876288bc21334d70163831657e:search

```yaml
regex_id: 2e0bc6876288bc21334d70163831657e
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_unittest/test_case.py:1602:16"
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

## usage_mismatch:372a631cf395844990dab0f1c3e31ec6:match

```yaml
regex_id: 372a631cf395844990dab0f1c3e31ec6
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:750:25"
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

## intent_mismatch:37f44019785c8a6602a558e554297df0:email

```yaml
regex_id: 37f44019785c8a6602a558e554297df0
schema_version: "1"
kind: intent_mismatch
corpus: ver
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_email/test_email.py:5814:17"
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

## usage_mismatch:37f44019785c8a6602a558e554297df0:search

```yaml
regex_id: 37f44019785c8a6602a558e554297df0
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_email/test_email.py:5814:17"
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

## usage_mismatch:3d65b6dacb986f17df881a0b8158308a:search

```yaml
regex_id: 3d65b6dacb986f17df881a0b8158308a
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/logging/config.py:378:20"
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

## usage_mismatch:3e4abfd2b857058262782e26cce3a328:search

```yaml
regex_id: 3e4abfd2b857058262782e26cce3a328
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/idlelib/pyshell.py:1341:35"
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

## usage_mismatch:3eb22f5c2347ea43338957b706864ffa:match

```yaml
regex_id: 3eb22f5c2347ea43338957b706864ffa
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:2512:26"
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

## usage_mismatch:42b960fb373ea979a18f7374808cc0eb:search

```yaml
regex_id: 42b960fb373ea979a18f7374808cc0eb
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_smtplib.py:158:19"
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

## usage_mismatch:43299f2caefc02d0c8785dd1799631cb:match

```yaml
regex_id: 43299f2caefc02d0c8785dd1799631cb
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:637:25"
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

## usage_mismatch:45a8d7ac0b5a21f2e18c5e9d8f1393fa:search

```yaml
regex_id: 45a8d7ac0b5a21f2e18c5e9d8f1393fa
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Tools/c-analyzer/c_parser/preprocessor/gcc.py:36:17"
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

## usage_mismatch:464759a7b51d0416951d8a4ba7806f43:search

```yaml
regex_id: 464759a7b51d0416951d8a4ba7806f43
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/http/cookiejar.py:620:14"
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

## usage_mismatch:47bcdf07ca184a327eaf8a2d9e04a96a:match

```yaml
regex_id: 47bcdf07ca184a327eaf8a2d9e04a96a
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:753:26"
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

## usage_mismatch:4912fa9fbc910d67a680beb837eed553:match

```yaml
regex_id: 4912fa9fbc910d67a680beb837eed553
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:759:24"
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

## usage_mismatch:4d584a127f4ccd13e39b15714e8a9d5f:match

```yaml
regex_id: 4d584a127f4ccd13e39b15714e8a9d5f
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:756:26"
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

## usage_mismatch:4ec539bba1ed9aec907097e9c80627fa:search

```yaml
regex_id: 4ec539bba1ed9aec907097e9c80627fa
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/http/cookiejar.py:345:25"
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

## usage_mismatch:53c0fc57e28dcf0daf4333d089719d82:search

```yaml
regex_id: 53c0fc57e28dcf0daf4333d089719d82
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:809:26"
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

## usage_mismatch:565caf003c88971d4199a5f1bfccb4f5:match

```yaml
regex_id: 565caf003c88971d4199a5f1bfccb4f5
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:765:24"
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

## usage_mismatch:5ea08fcab2335313571b57852b145df3:match

```yaml
regex_id: 5ea08fcab2335313571b57852b145df3
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:642:26"
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

## usage_mismatch:5fe9abd09f9f06c78f86b65a350bb3d8:match

```yaml
regex_id: 5fe9abd09f9f06c78f86b65a350bb3d8
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:744:25"
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

## usage_mismatch:64bde9c7ecc7dc9528ba2d00ba0056f8:match

```yaml
regex_id: 64bde9c7ecc7dc9528ba2d00ba0056f8
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:712:25"
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

## usage_mismatch:650ac30623aa935d1f0f784c51992743:search

```yaml
regex_id: 650ac30623aa935d1f0f784c51992743
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/logging/__init__.py:482:15"
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

## usage_mismatch:669df196e3e44ea9fc0fa66a6a125ec4:search

```yaml
regex_id: 669df196e3e44ea9fc0fa66a6a125ec4
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/http/cookiejar.py:535:10"
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

## usage_mismatch:673e35776bff46b93ea71382e7e447ef:search

```yaml
regex_id: 673e35776bff46b93ea71382e7e447ef
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/idlelib/pyshell.py:1340:35"
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

## usage_mismatch:684ddd13eb2885555bdda61d8eee6d41:match

```yaml
regex_id: 684ddd13eb2885555bdda61d8eee6d41
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:639:25"
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

## usage_mismatch:6a1cb584e755ff724c0ca5a880d18160:search

```yaml
regex_id: 6a1cb584e755ff724c0ca5a880d18160
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_smtplib.py:672:17"
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

## usage_mismatch:6c302dbf1493cd67f2295ab8905050ed:search

```yaml
regex_id: 6c302dbf1493cd67f2295ab8905050ed
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/pydoc.py:278:14"
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

## usage_mismatch:6dab18cf12209ead91c9a923fb214e6a:search

```yaml
regex_id: 6dab18cf12209ead91c9a923fb214e6a
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/logging/config.py:294:13"
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

## usage_mismatch:6f94d519806b22054dd9d039985feed8:search

```yaml
regex_id: 6f94d519806b22054dd9d039985feed8
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/http/cookiejar.py:209:13"
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

## usage_mismatch:70156562a0eb5e2ce30d390d08534004:match

```yaml
regex_id: 70156562a0eb5e2ce30d390d08534004
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:2513:26"
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

## usage_mismatch:7232d481a667ec86ec0368935ca486e8:match

```yaml
regex_id: 7232d481a667ec86ec0368935ca486e8
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:748:25"
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

## usage_mismatch:77c688ce24b9b0ab5fbbf15115005c56:search

```yaml
regex_id: 77c688ce24b9b0ab5fbbf15115005c56
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/http/cookiejar.py:288:14"
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

## usage_mismatch:7834d3754f39bf4ccb0cc340d41ec469:match

```yaml
regex_id: 7834d3754f39bf4ccb0cc340d41ec469
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:751:25"
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

## usage_mismatch:79b8b94a5fe6f8cbcada4219f8a41392:match

```yaml
regex_id: 79b8b94a5fe6f8cbcada4219f8a41392
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:745:25"
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

## usage_mismatch:7bc62c9edb839187c6039c2906ccbe4a:match

```yaml
regex_id: 7bc62c9edb839187c6039c2906ccbe4a
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:643:25"
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

## usage_mismatch:7e3d5be48ab01c672b0106f9d4887862:search

```yaml
regex_id: 7e3d5be48ab01c672b0106f9d4887862
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/http/cookiejar.py:1260:15"
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

## usage_mismatch:80e06e598ac702f81687dd4a6beaf706:search

```yaml
regex_id: 80e06e598ac702f81687dd4a6beaf706
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_smtplib.py:603:17"
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

## usage_mismatch:813492d808c5be66831b7a14310510ff:search

```yaml
regex_id: 813492d808c5be66831b7a14310510ff
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/http/cookiejar.py:346:25"
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

## usage_mismatch:81b033923462d840a477ed963d24f6cf:match

```yaml
regex_id: 81b033923462d840a477ed963d24f6cf
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:768:26"
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

## usage_mismatch:83b57013c8c1f6e0ef06459980e45669:search

```yaml
regex_id: 83b57013c8c1f6e0ef06459980e45669
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/_pydecimal.py:6114:13"
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

## usage_mismatch:84babd241360e3aa65d86cdd09f1b1b5:search

```yaml
regex_id: 84babd241360e3aa65d86cdd09f1b1b5
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:805:25"
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

## usage_mismatch:84e687a1f6fc81081f63d42c175ea0d9:search

```yaml
regex_id: 84e687a1f6fc81081f63d42c175ea0d9
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:1443:28"
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

## usage_mismatch:858ea0f3afce34acb289e257aee13ea8:search

```yaml
regex_id: 858ea0f3afce34acb289e257aee13ea8
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_smtplib.py:544:17"
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

## usage_mismatch:8a3465ddda4c90e4609127fa380fcbec:search

```yaml
regex_id: 8a3465ddda4c90e4609127fa380fcbec
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Doc/tools/extensions/misc_news.py:33:38"
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

## usage_mismatch:8a9ff904ac3a96762c00bca450b346a1:match

```yaml
regex_id: 8a9ff904ac3a96762c00bca450b346a1
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:740:26"
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

## usage_mismatch:8bfed0cfc79bdca4eb8b4c115e20a5ab:match

```yaml
regex_id: 8bfed0cfc79bdca4eb8b4c115e20a5ab
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:649:25"
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

## usage_mismatch:8c30afedacbc9d182935b74b32785925:match

```yaml
regex_id: 8c30afedacbc9d182935b74b32785925
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:762:24"
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

## usage_mismatch:8dc2dc5dd68fbdd799873a86cd99c308:match

```yaml
regex_id: 8dc2dc5dd68fbdd799873a86cd99c308
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:2520:26"
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

## usage_mismatch:8fed8bf11f3328125337e410283a30a8:search

```yaml
regex_id: 8fed8bf11f3328125337e410283a30a8
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:808:25"
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

## usage_mismatch:9285b79c1e371162a3be8c3a41ce9294:match

```yaml
regex_id: 9285b79c1e371162a3be8c3a41ce9294
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:763:24"
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

## usage_mismatch:94f19d48244b4ea9f1cc47944d1d76ed:search

```yaml
regex_id: 94f19d48244b4ea9f1cc47944d1d76ed
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_smtplib.py:491:17"
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

## usage_mismatch:95695daf22c5a4305b6e2e57875fdb4e:match

```yaml
regex_id: 95695daf22c5a4305b6e2e57875fdb4e
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:758:24"
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

## usage_mismatch:9d3085cc34a2c361eeebde58fc65291a:match

```yaml
regex_id: 9d3085cc34a2c361eeebde58fc65291a
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:716:25"
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

## usage_mismatch:9ea4ef8c05a242a5efa4f0e6d24e218d:search

```yaml
regex_id: 9ea4ef8c05a242a5efa4f0e6d24e218d
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_smtplib.py:635:17"
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

## usage_mismatch:9fa8d2988a9a3dece92e79be3d10b32b:match

```yaml
regex_id: 9fa8d2988a9a3dece92e79be3d10b32b
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:710:25"
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

## usage_mismatch:a06542dc5bd5e7d00b7687d2c433d359:match

```yaml
regex_id: a06542dc5bd5e7d00b7687d2c433d359
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:647:25"
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

## usage_mismatch:a0df531b4f361e073b6e7087cb1589fe:search

```yaml
regex_id: a0df531b4f361e073b6e7087cb1589fe
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_pyrepl/test_pyrepl.py:1686:24"
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

## usage_mismatch:a1d6ff410945148da878fcd088c6ef51:search

```yaml
regex_id: a1d6ff410945148da878fcd088c6ef51
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:807:26"
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

## usage_mismatch:a1f61523667c0bf7fe416d6736f89635:match

```yaml
regex_id: a1f61523667c0bf7fe416d6736f89635
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:739:26"
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

## usage_mismatch:a438d6791e38f7c4b6d5b378017eaa26:search

```yaml
regex_id: a438d6791e38f7c4b6d5b378017eaa26
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Android/android.py:165:20"
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

## usage_mismatch:a7492ef38acdcecc5fd3565f6bbba8a3:match

```yaml
regex_id: a7492ef38acdcecc5fd3565f6bbba8a3
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:715:26"
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

## usage_mismatch:a86499c08f4a3f3f20b683cad95e894a:search

```yaml
regex_id: a86499c08f4a3f3f20b683cad95e894a
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/http/cookiejar.py:135:14"
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

## usage_mismatch:aaa62a4df8529d9035cc7dd91c386c85:search

```yaml
regex_id: aaa62a4df8529d9035cc7dd91c386c85
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_pyrepl/test_pyrepl.py:1676:24"
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

## usage_mismatch:ac887d6e620e90c8da4f00b398641caa:match

```yaml
regex_id: ac887d6e620e90c8da4f00b398641caa
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:764:24"
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

## intent_mismatch:ad0158098f5d4d004882b147180b3f91:email

```yaml
regex_id: ad0158098f5d4d004882b147180b3f91
schema_version: "1"
kind: intent_mismatch
corpus: ver
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/email/feedparser.py:37:11"
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

## usage_mismatch:ad0158098f5d4d004882b147180b3f91:search

```yaml
regex_id: ad0158098f5d4d004882b147180b3f91
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/email/feedparser.py:37:11"
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

## usage_mismatch:b12a51e72db43f628f7dcbd3a1fed9d7:search

```yaml
regex_id: b12a51e72db43f628f7dcbd3a1fed9d7
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/doctest.py:655:27"
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

## intent_mismatch:b1ffa76d5902444ae92e95879ef8c7bd:email

```yaml
regex_id: b1ffa76d5902444ae92e95879ef8c7bd
schema_version: "1"
kind: intent_mismatch
corpus: ver
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/email/_header_value_parser.py:117:18"
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

## usage_mismatch:b464f5dfd4ad2050a23eb9c4f62bf836:match

```yaml
regex_id: b464f5dfd4ad2050a23eb9c4f62bf836
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:747:25"
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

## usage_mismatch:b6b8baa1748b1de4d4e76b73489f9e7b:search

```yaml
regex_id: b6b8baa1748b1de4d4e76b73489f9e7b
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/http/cookiejar.py:344:25"
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

## usage_mismatch:b6d0e8535ecaa070b8cee2b162447433:search

```yaml
regex_id: b6d0e8535ecaa070b8cee2b162447433
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/logging/config.py:379:20"
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

## usage_mismatch:bc099e44234dfabb7cf87208fb94a53f:search

```yaml
regex_id: bc099e44234dfabb7cf87208fb94a53f
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/email/header.py:48:7"
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

## usage_mismatch:c10d2837d73dbaa7052d486f9396ab7d:match

```yaml
regex_id: c10d2837d73dbaa7052d486f9396ab7d
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:641:26"
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

## usage_mismatch:c30918b401632fc5bb71ceb31a4f78da:match

```yaml
regex_id: c30918b401632fc5bb71ceb31a4f78da
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:2522:24"
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

## usage_mismatch:c4d7b955c82aae163c3c54de523d7a35:match

```yaml
regex_id: c4d7b955c82aae163c3c54de523d7a35
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:761:24"
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

## usage_mismatch:c7e47dc92a6835126a061ee7daf5b3bf:match

```yaml
regex_id: c7e47dc92a6835126a061ee7daf5b3bf
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:2526:26"
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

## usage_mismatch:ccecae03f737fe50281e48284df1a9af:match

```yaml
regex_id: ccecae03f737fe50281e48284df1a9af
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:741:26"
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

## usage_mismatch:d6536e935091b51a0bff7e54415dd893:match

```yaml
regex_id: d6536e935091b51a0bff7e54415dd893
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:766:24"
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

## usage_mismatch:d905025bb5fc9f1c6b509ad8971a115d:search

```yaml
regex_id: d905025bb5fc9f1c6b509ad8971a115d
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Tools/c-analyzer/c_parser/preprocessor/gcc.py:37:23"
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

## usage_mismatch:d946dce1510b4ee8787dea7f77cd0b2e:search

```yaml
regex_id: d946dce1510b4ee8787dea7f77cd0b2e
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/logging/config.py:374:22"
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

## usage_mismatch:dc4333345d1fab9e3b0da9731d86ef78:search

```yaml
regex_id: dc4333345d1fab9e3b0da9731d86ef78
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/http/cookiejar.py:1258:14"
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

## usage_mismatch:de3e086798c2639a74e8668b8b6519ff:match

```yaml
regex_id: de3e086798c2639a74e8668b8b6519ff
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:645:25"
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

## usage_mismatch:df3b5ccb1da0d01520057515f49a0159:search

```yaml
regex_id: df3b5ccb1da0d01520057515f49a0159
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/_pydecimal.py:6115:14"
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

## usage_mismatch:e215d487d78ebf0e6888b48cf3484787:search

```yaml
regex_id: e215d487d78ebf0e6888b48cf3484787
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/doctest.py:804:17"
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

## usage_mismatch:e45c9bbb1476f9dfad176a41d660109a:search

```yaml
regex_id: e45c9bbb1476f9dfad176a41d660109a
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:1826:18"
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

## usage_mismatch:e8176446de88dcb17f91621812a502bc:match

```yaml
regex_id: e8176446de88dcb17f91621812a502bc
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:714:26"
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

## usage_mismatch:e82e77dc56f10d86963c46f01d966d6e:match

```yaml
regex_id: e82e77dc56f10d86963c46f01d966d6e
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:769:24"
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

## usage_mismatch:e97aed9c59c857af34fe7317764319e4:search

```yaml
regex_id: e97aed9c59c857af34fe7317764319e4
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/email/utils.py:392:23"
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

## usage_mismatch:ec0464e819e4ec93e8f227c9795b2376:match

```yaml
regex_id: ec0464e819e4ec93e8f227c9795b2376
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:1751:30"
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

## usage_mismatch:f332b14e2839bc055bee821c4dc2a364:search

```yaml
regex_id: f332b14e2839bc055bee821c4dc2a364
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/logging/__init__.py:483:17"
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

## usage_mismatch:f82b12281906fd65c9922ba9abde476a:match

```yaml
regex_id: f82b12281906fd65c9922ba9abde476a
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:1742:29"
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

## usage_mismatch:f8af257743f8d20c8a2095637fe8fa85:match

```yaml
regex_id: f8af257743f8d20c8a2095637fe8fa85
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:754:26"
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

## usage_mismatch:f90512584895ad370766e5d471739793:search

```yaml
regex_id: f90512584895ad370766e5d471739793
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/urllib/request.py:268:15"
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

## usage_mismatch:f90d94798f1d4ee0c50cb8bc12c0d822:match

```yaml
regex_id: f90d94798f1d4ee0c50cb8bc12c0d822
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:2519:26"
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

## usage_mismatch:fb0fdad0dc35f62bed75f1986118681c:search

```yaml
regex_id: fb0fdad0dc35f62bed75f1986118681c
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/http/cookiejar.py:206:17"
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

## usage_mismatch:fb477d8246a54eb02968d07ec46b35a5:match

```yaml
regex_id: fb477d8246a54eb02968d07ec46b35a5
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:749:25"
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

## usage_mismatch:fb5fb1630e0e1a0aaf2baa63a6eba369:search

```yaml
regex_id: fb5fb1630e0e1a0aaf2baa63a6eba369
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:806:25"
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

## usage_mismatch:fd359bcccda827e1ee6546cb73d79ca5:search

```yaml
regex_id: fd359bcccda827e1ee6546cb73d79ca5
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_unittest/test_case.py:1540:46"
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

## usage_mismatch:fe2a65755b18f230be4382e62375c472:search

```yaml
regex_id: fe2a65755b18f230be4382e62375c472
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/test/test_re.py:2022:12"
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

## intent_mismatch:ffa823d73b552ceae41da7a436deb877:email

```yaml
regex_id: ffa823d73b552ceae41da7a436deb877
schema_version: "1"
kind: intent_mismatch
corpus: ver
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/email/feedparser.py:40:16"
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

## usage_mismatch:ffa823d73b552ceae41da7a436deb877:search

```yaml
regex_id: ffa823d73b552ceae41da7a436deb877
schema_version: "1"
kind: usage_mismatch
corpus: ver
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/ver/rules/Lib/email/feedparser.py:40:16"
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

## property:inventory:rc-shape1-injection-alphabet:rc-shape1-injection-alphabet

```yaml
regex_id: "inventory:rc-shape1-injection-alphabet"
schema_version: "1"
kind: property
corpus: ver
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
corpus: ver
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
corpus: ver
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
corpus: ver
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

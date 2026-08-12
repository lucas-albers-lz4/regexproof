---
schema_version: "1"
corpus: nogil-3.12
findings: 140
---

# nogil-3.12 batch findings

## usage_mismatch:02e5e6090cc2075e03a105176bc44074:search

```yaml
regex_id: 02e5e6090cc2075e03a105176bc44074
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Tools/scripts/combinerefs.py:98:25"
```

### Pattern

`^Remaining object addresses:$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:05ece851d551617b7445b7b39148852c:match

```yaml
regex_id: 05ece851d551617b7445b7b39148852c
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:695:24"
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

## usage_mismatch:07ac85120be654811968b080174665b8:search

```yaml
regex_id: 07ac85120be654811968b080174665b8
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/logging/config.py:365:20"
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

## usage_mismatch:082346332fc29af4e5cdedf1cf8e8c3a:search

```yaml
regex_id: 082346332fc29af4e5cdedf1cf8e8c3a
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/logging/__init__.py:474:15"
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

## usage_mismatch:0f1c96df8ec62da0b9c1a9ff8e2a7f1a:match

```yaml
regex_id: 0f1c96df8ec62da0b9c1a9ff8e2a7f1a
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:682:25"
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

## usage_mismatch:11729b17ef40b72d30bb4d21b4ae6ac6:match

```yaml
regex_id: 11729b17ef40b72d30bb4d21b4ae6ac6
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:2303:26"
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

## usage_mismatch:16817239dc3cbdff1143d59c3f8a5e54:match

```yaml
regex_id: 16817239dc3cbdff1143d59c3f8a5e54
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:676:26"
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

## usage_mismatch:17fb5749bd61dfd7a53278ee6082153b:match

```yaml
regex_id: 17fb5749bd61dfd7a53278ee6082153b
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:650:26"
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

## usage_mismatch:19bb505cc05f361306c9c53bd0f57b4a:search

```yaml
regex_id: 19bb505cc05f361306c9c53bd0f57b4a
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:1597:18"
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

## usage_mismatch:215d495e9e3c90e61dfa0c916aa78e59:match

```yaml
regex_id: 215d495e9e3c90e61dfa0c916aa78e59
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:686:25"
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

## usage_mismatch:21b457725780c40e8e3abdc25d95cb8a:match

```yaml
regex_id: 21b457725780c40e8e3abdc25d95cb8a
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:689:26"
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

## usage_mismatch:246baa7a5b2fbc7aaf33c4d6d8ba466f:match

```yaml
regex_id: 246baa7a5b2fbc7aaf33c4d6d8ba466f
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:2300:24"
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

## usage_mismatch:24f91f517c27d79d21c8358ca5d68697:search

```yaml
regex_id: 24f91f517c27d79d21c8358ca5d68697
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:741:25"
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

## usage_mismatch:2918e9855436afabb23536d26af4586f:search

```yaml
regex_id: 2918e9855436afabb23536d26af4586f
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Tools/ssl/make_ssl_data.py:52:10"
```

### Pattern

`^((\w+?)_R_(\w+)):(\d+):`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:29801af54a77fef948a8483873cc649a:match

```yaml
regex_id: 29801af54a77fef948a8483873cc649a
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:691:26"
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

## usage_mismatch:2f71b93e4b7048986f333109ee07eec0:search

```yaml
regex_id: 2f71b93e4b7048986f333109ee07eec0
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_gdb.py:43:12"
```

### Pattern

`^(?:GNU|HP) gdb.*?\b(\d+)\.(\d+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:309825c032115268cc42fa8f45993d5a:search

```yaml
regex_id: 309825c032115268cc42fa8f45993d5a
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_smtplib.py:574:17"
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

## usage_mismatch:315cb55fa67f10a8bfd387dc75bd226a:search

```yaml
regex_id: 315cb55fa67f10a8bfd387dc75bd226a
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/doctest.py:775:17"
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

## usage_mismatch:33dce865139146e78eb937240ecedf4f:search

```yaml
regex_id: 33dce865139146e78eb937240ecedf4f
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/configparser.py:1283:16"
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

## usage_mismatch:353db6cb584d2a58451bd1ea0acff4e1:search

```yaml
regex_id: 353db6cb584d2a58451bd1ea0acff4e1
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_unittest/test_case.py:1322:46"
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

## usage_mismatch:354dd9b1f798845c940a2c38aa403739:search

```yaml
regex_id: 354dd9b1f798845c940a2c38aa403739
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/idlelib/pyshell.py:1342:35"
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

## usage_mismatch:37ce1bd0315f7b2ecbdc17dc4577c6ba:search

```yaml
regex_id: 37ce1bd0315f7b2ecbdc17dc4577c6ba
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:743:26"
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

## usage_mismatch:387a634459d301bd9d925a863802da77:search

```yaml
regex_id: 387a634459d301bd9d925a863802da77
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Tools/ssl/make_ssl_data.py:64:10"
```

### Pattern

`^R\s+((\w+)_R_(\w+))\s+(\d+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:38e17ce860cbb8e62dbac63431fa211a:match

```yaml
regex_id: 38e17ce860cbb8e62dbac63431fa211a
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:2294:25"
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

## usage_mismatch:396c22f0159c93c2727217b6a9dcc99a:search

```yaml
regex_id: 396c22f0159c93c2727217b6a9dcc99a
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/http/cookiejar.py:619:14"
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

## usage_mismatch:39996d3033529c58bda85041f3741d44:match

```yaml
regex_id: 39996d3033529c58bda85041f3741d44
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:700:24"
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

## usage_mismatch:39ab4cffdc95cb6be47ea76720481b8b:match

```yaml
regex_id: 39ab4cffdc95cb6be47ea76720481b8b
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:1523:30"
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

## usage_mismatch:43816ebd62c68c5c093e490e36487cc9:match

```yaml
regex_id: 43816ebd62c68c5c093e490e36487cc9
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:690:26"
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

## usage_mismatch:44b8ae28a06912f5275dd02c9629c36b:match

```yaml
regex_id: 44b8ae28a06912f5275dd02c9629c36b
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:704:26"
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

## usage_mismatch:45fa7f77a218f33dc5ddf4b81e2b02bc:search

```yaml
regex_id: 45fa7f77a218f33dc5ddf4b81e2b02bc
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/lib2to3/pgen2/tokenize.py:227:12"
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

## usage_mismatch:466ecbd81adaa1c8d18ededa2062a10a:match

```yaml
regex_id: 466ecbd81adaa1c8d18ededa2062a10a
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Tools/cases_generator/generate_cases.py:106:16"
```

### Pattern

`^PEEK\((\d+)\)$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:49210d7553297512dd72ca2775ba8d03:search

```yaml
regex_id: 49210d7553297512dd72ca2775ba8d03
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/logging/__init__.py:475:17"
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

## usage_mismatch:49cf7c7b4a00fd64619576f0835d0f33:match

```yaml
regex_id: 49cf7c7b4a00fd64619576f0835d0f33
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:583:25"
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

## usage_mismatch:4c872440d4b19bde5e0604bd4d3adaff:search

```yaml
regex_id: 4c872440d4b19bde5e0604bd4d3adaff
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/_pydecimal.py:6150:13"
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

## usage_mismatch:4f7cf47fd6b434d11165f9345de5edd4:search

```yaml
regex_id: 4f7cf47fd6b434d11165f9345de5edd4
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/logging/config.py:364:20"
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

## usage_mismatch:519eeceaa9ad38e8f60d9702d0e99628:match

```yaml
regex_id: 519eeceaa9ad38e8f60d9702d0e99628
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:683:25"
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

## usage_mismatch:5406cfa13f47d8f9d7301eb4297ed453:match

```yaml
regex_id: 5406cfa13f47d8f9d7301eb4297ed453
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:575:25"
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

## usage_mismatch:5509f3e0f2f971733e2a751d06e18d52:search

```yaml
regex_id: 5509f3e0f2f971733e2a751d06e18d52
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/http/cookiejar.py:345:25"
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

## usage_mismatch:59067193fdf71a01e6842781717e4ae9:match

```yaml
regex_id: 59067193fdf71a01e6842781717e4ae9
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:2293:25"
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

## usage_mismatch:5bd94e073752119b9b45db1a5988feb5:match

```yaml
regex_id: 5bd94e073752119b9b45db1a5988feb5
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:694:24"
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

## usage_mismatch:674c73a117c920b8cc50325d1de9f7d8:match

```yaml
regex_id: 674c73a117c920b8cc50325d1de9f7d8
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:585:25"
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

## usage_mismatch:69a7e402d2916a452777ec62ffdc25ce:search

```yaml
regex_id: 69a7e402d2916a452777ec62ffdc25ce
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/logging/config.py:360:22"
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

## intent_mismatch:69b1b72aec6aede8e96742b0c7314e0e:email

```yaml
regex_id: 69b1b72aec6aede8e96742b0c7314e0e
schema_version: "1"
kind: intent_mismatch
corpus: nogil-3.12
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/email/_header_value_parser.py:100:18"
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

## intent_mismatch:69d4cba3f9e154dc3b09e5d89b0401c1:email

```yaml
regex_id: 69d4cba3f9e154dc3b09e5d89b0401c1
schema_version: "1"
kind: intent_mismatch
corpus: nogil-3.12
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_email/test_email.py:5545:17"
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

## usage_mismatch:69d4cba3f9e154dc3b09e5d89b0401c1:search

```yaml
regex_id: 69d4cba3f9e154dc3b09e5d89b0401c1
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_email/test_email.py:5545:17"
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

## usage_mismatch:6db0276861cde577bbe3acb53afe5a41:search

```yaml
regex_id: 6db0276861cde577bbe3acb53afe5a41
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Tools/c-analyzer/c_parser/preprocessor/gcc.py:15:17"
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

## usage_mismatch:6dcf5579b3e0d47b944fbea624729b9f:match

```yaml
regex_id: 6dcf5579b3e0d47b944fbea624729b9f
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:654:25"
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

## usage_mismatch:6de0ade08ca45304d506189fc31bd17a:search

```yaml
regex_id: 6de0ade08ca45304d506189fc31bd17a
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:742:25"
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

## usage_mismatch:6f478f724f9aab13e6e1807a5ba8acb1:search

```yaml
regex_id: 6f478f724f9aab13e6e1807a5ba8acb1
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:1807:12"
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

## usage_mismatch:729d47af76db0ee317782b5b0da46d90:search

```yaml
regex_id: 729d47af76db0ee317782b5b0da46d90
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/textwrap.py:416:22"
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

## usage_mismatch:73baaec4193fce65b23f10758730d4da:search

```yaml
regex_id: 73baaec4193fce65b23f10758730d4da
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_smtplib.py:158:19"
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

## usage_mismatch:764126b56e12da096aa1330627d8717d:match

```yaml
regex_id: 764126b56e12da096aa1330627d8717d
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:681:25"
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

## usage_mismatch:7907849efb816d60603e0baf0782f74e:match

```yaml
regex_id: 7907849efb816d60603e0baf0782f74e
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:652:25"
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

## usage_mismatch:7a581d1ef14364da55d8a84b916a02c2:search

```yaml
regex_id: 7a581d1ef14364da55d8a84b916a02c2
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/doctest.py:1429:30"
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

## usage_mismatch:7ab0a0b5b4a49345deefc90cc38f866e:search

```yaml
regex_id: 7ab0a0b5b4a49345deefc90cc38f866e
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_smtplib.py:544:17"
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

## usage_mismatch:7fd37fad22c403e0e8e2186ca33015b0:match

```yaml
regex_id: 7fd37fad22c403e0e8e2186ca33015b0
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:579:25"
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

## usage_mismatch:80d3da207fcc3474552d6e76fb942432:search

```yaml
regex_id: 80d3da207fcc3474552d6e76fb942432
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/http/cookiejar.py:288:14"
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

## intent_mismatch:8657a6428fd1bfc8a358a5da35506cbe:email

```yaml
regex_id: 8657a6428fd1bfc8a358a5da35506cbe
schema_version: "1"
kind: intent_mismatch
corpus: nogil-3.12
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/email/feedparser.py:37:11"
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

## usage_mismatch:8657a6428fd1bfc8a358a5da35506cbe:search

```yaml
regex_id: 8657a6428fd1bfc8a358a5da35506cbe
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/email/feedparser.py:37:11"
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

## usage_mismatch:871f873fbdb9dbad8fe11ce5e72a5778:match

```yaml
regex_id: 871f873fbdb9dbad8fe11ce5e72a5778
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:705:24"
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

## intent_mismatch:88c264acaa0d720c033fd4e254f6887a:email

```yaml
regex_id: 88c264acaa0d720c033fd4e254f6887a
schema_version: "1"
kind: intent_mismatch
corpus: nogil-3.12
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/email/header.py:35:7"
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

## usage_mismatch:89ccec7b761ca66b3cbab382e4e2581f:search

```yaml
regex_id: 89ccec7b761ca66b3cbab382e4e2581f
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_smtplib.py:491:17"
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

## usage_mismatch:8a5af399ec8dae1a7f2d5374c5de2ba4:match

```yaml
regex_id: 8a5af399ec8dae1a7f2d5374c5de2ba4
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/idlelib/format.py:181:11"
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

## usage_mismatch:8aeed974826c20de81fe721f09fa4004:search

```yaml
regex_id: 8aeed974826c20de81fe721f09fa4004
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/logging/config.py:280:13"
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

## usage_mismatch:8eae93aba0f6b508c63189a7446b4845:search

```yaml
regex_id: 8eae93aba0f6b508c63189a7446b4845
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/http/cookiejar.py:211:21"
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

## usage_mismatch:91d38e2c8fc0a5de573aebb898729d62:search

```yaml
regex_id: 91d38e2c8fc0a5de573aebb898729d62
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/logging/config.py:362:19"
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

## usage_mismatch:95a7e9b686588f2c59a0938df4e8e1de:match

```yaml
regex_id: 95a7e9b686588f2c59a0938df4e8e1de
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:678:26"
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

## usage_mismatch:97c251e8f16495b76fbac0d3df33e97b:search

```yaml
regex_id: 97c251e8f16495b76fbac0d3df33e97b
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/http/cookiejar.py:209:13"
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

## intent_mismatch:98e3b0f84f1b640c90bbbbabd594cf2a:email

```yaml
regex_id: 98e3b0f84f1b640c90bbbbabd594cf2a
schema_version: "1"
kind: intent_mismatch
corpus: nogil-3.12
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/email/generator.py:22:7"
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

## usage_mismatch:98e3b0f84f1b640c90bbbbabd594cf2a:search

```yaml
regex_id: 98e3b0f84f1b640c90bbbbabd594cf2a
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/email/generator.py:22:7"
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

## usage_mismatch:98eb1c6e7f6e70b3a4bdd1e3bfdf9260:search

```yaml
regex_id: 98eb1c6e7f6e70b3a4bdd1e3bfdf9260
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/http/cookiejar.py:135:14"
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

## usage_mismatch:9937c2f56d9e14a1c9216d034a8ba76c:search

```yaml
regex_id: 9937c2f56d9e14a1c9216d034a8ba76c
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/tokenize.py:38:12"
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

## usage_mismatch:9b6778c5155a5a1ab30e0574939eb506:match

```yaml
regex_id: 9b6778c5155a5a1ab30e0574939eb506
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:2289:26"
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

## usage_mismatch:9c9bc24462aeedc13a306c823fc6c131:match

```yaml
regex_id: 9c9bc24462aeedc13a306c823fc6c131
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:2299:24"
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

## usage_mismatch:9d52e388f3aaca0e9cd3d53bba62db05:search

```yaml
regex_id: 9d52e388f3aaca0e9cd3d53bba62db05
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_regrtest.py:983:16"
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

## usage_mismatch:9de66b7f473792cffcccbbf5a16236db:match

```yaml
regex_id: 9de66b7f473792cffcccbbf5a16236db
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:692:26"
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

## usage_mismatch:9f9ce354baa61cc14c368c6679a5f90e:match

```yaml
regex_id: 9f9ce354baa61cc14c368c6679a5f90e
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:648:25"
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

## usage_mismatch:a42f15df505feca879a446f6b86bf423:search

```yaml
regex_id: a42f15df505feca879a446f6b86bf423
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/http/cookiejar.py:346:25"
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

## usage_mismatch:a46bc07e614a7f616835c36f22f5b9c1:match

```yaml
regex_id: a46bc07e614a7f616835c36f22f5b9c1
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/msilib/__init__.py:184:11"
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

## usage_mismatch:a6f8af8c448d0d6aeb394c634c841aff:search

```yaml
regex_id: a6f8af8c448d0d6aeb394c634c841aff
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/urllib/request.py:296:15"
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

## usage_mismatch:a783d06bc53fd7990433dbb56c33c29a:match

```yaml
regex_id: a783d06bc53fd7990433dbb56c33c29a
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:698:24"
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

## usage_mismatch:a78e289d01dbbd592fc2e726d9f17fe1:match

```yaml
regex_id: a78e289d01dbbd592fc2e726d9f17fe1
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:646:25"
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

## usage_mismatch:a9864f4dc48925b46ecace84f7e88156:search

```yaml
regex_id: a9864f4dc48925b46ecace84f7e88156
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/http/cookiejar.py:451:23"
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

## usage_mismatch:ac64362d2e07b27bcfedefafea4f082e:search

```yaml
regex_id: ac64362d2e07b27bcfedefafea4f082e
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/idlelib/pyshell.py:1341:35"
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

## usage_mismatch:add2d0acd6deb1ccd5ab0c582dc85a19:match

```yaml
regex_id: add2d0acd6deb1ccd5ab0c582dc85a19
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/lib2to3/pgen2/conv.py:71:17"
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

## usage_mismatch:aedf51972e1b32105af7182663af3c2e:search

```yaml
regex_id: aedf51972e1b32105af7182663af3c2e
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:1215:28"
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

## usage_mismatch:b047e20f8abf9e2653a7d820e0135da5:search

```yaml
regex_id: b047e20f8abf9e2653a7d820e0135da5
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Tools/clinic/clinic.py:142:24"
```

### Pattern

`^[A-Za-z_][A-Za-z0-9_]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b1ac4bda9ad89be4d1bbcdf8a13c8d19:search

```yaml
regex_id: b1ac4bda9ad89be4d1bbcdf8a13c8d19
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_smtplib.py:609:16"
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

## usage_mismatch:b205b0d18212d1a63e3b2b0e75961df8:match

```yaml
regex_id: b205b0d18212d1a63e3b2b0e75961df8
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Tools/cases_generator/generate_cases.py:876:31"
```

### Pattern

`^\s*PREDICT\((\w+)\);\s*$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b2d68ebaf4152f0d474a18eb11b7568b:match

```yaml
regex_id: b2d68ebaf4152f0d474a18eb11b7568b
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:2297:26"
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

## usage_mismatch:b30b9f054adc1c4657fc7c76c30ae819:match

```yaml
regex_id: b30b9f054adc1c4657fc7c76c30ae819
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:675:26"
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

## usage_mismatch:b3121160d732e1fb8a0e046048e70038:search

```yaml
regex_id: b3121160d732e1fb8a0e046048e70038
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/pydoc.py:228:14"
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

## usage_mismatch:b47dd6c014c7b577bf00e82cd46d0f3d:search

```yaml
regex_id: b47dd6c014c7b577bf00e82cd46d0f3d
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_smtplib.py:148:19"
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

## usage_mismatch:b4c34c14ed3dd6d6b8d337b88257a329:match

```yaml
regex_id: b4c34c14ed3dd6d6b8d337b88257a329
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:2296:26"
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

## usage_mismatch:b573e38b98881076e2db8a850a73f89a:match

```yaml
regex_id: b573e38b98881076e2db8a850a73f89a
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:2301:24"
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

## usage_mismatch:b6bd027bdf40f82d20752abd65f781e6:search

```yaml
regex_id: b6bd027bdf40f82d20752abd65f781e6
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:568:12"
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

## usage_mismatch:b73bab22c95ca3c7b0b99c2eecfb400b:search

```yaml
regex_id: b73bab22c95ca3c7b0b99c2eecfb400b
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/doctest.py:744:27"
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

## usage_mismatch:b879526324061d5f81158cacc55ade28:search

```yaml
regex_id: b879526324061d5f81158cacc55ade28
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:1602:18"
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

## usage_mismatch:bb6367fdb1c3818c82502635ca2e7823:search

```yaml
regex_id: bb6367fdb1c3818c82502635ca2e7823
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/_pydecimal.py:6151:14"
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

## usage_mismatch:bf4c6549fd983ccffdb9caa4e45dee36:search

```yaml
regex_id: bf4c6549fd983ccffdb9caa4e45dee36
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_unittest/test_case.py:1384:16"
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

## usage_mismatch:c1727cd8d2d8436edd7ec90aced98e7a:match

```yaml
regex_id: c1727cd8d2d8436edd7ec90aced98e7a
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:680:25"
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

## usage_mismatch:c400c1e0583a0c6b517bfadebee32466:search

```yaml
regex_id: c400c1e0583a0c6b517bfadebee32466
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Tools/scripts/combinerefs.py:91:25"
```

### Pattern

`^Remaining objects:$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c798dc80e35d2ed86e68df37c554a723:match

```yaml
regex_id: c798dc80e35d2ed86e68df37c554a723
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:577:26"
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

## usage_mismatch:c9a650e843aec0dc17d8abb437af35f1:match

```yaml
regex_id: c9a650e843aec0dc17d8abb437af35f1
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:651:26"
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

## usage_mismatch:cdd65a2eb01912b789377fe8b72248d2:search

```yaml
regex_id: cdd65a2eb01912b789377fe8b72248d2
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/http/cookiejar.py:1257:14"
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

## usage_mismatch:ce295347f97d5d3cc92f6ce1f2049bf3:match

```yaml
regex_id: ce295347f97d5d3cc92f6ce1f2049bf3
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:702:24"
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

## usage_mismatch:cfe925060c5e932ceb307d5f1722ad87:match

```yaml
regex_id: cfe925060c5e932ceb307d5f1722ad87
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:701:24"
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

## usage_mismatch:d239d6b3199965e8c7bdb5c33fb628ad:match

```yaml
regex_id: d239d6b3199965e8c7bdb5c33fb628ad
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:685:25"
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

## usage_mismatch:d36838c550e1f52e9966bdf618236afd:search

```yaml
regex_id: d36838c550e1f52e9966bdf618236afd
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/logging/config.py:363:18"
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

## usage_mismatch:d5c646c8e8ebecb4aa9b8aff48580132:search

```yaml
regex_id: d5c646c8e8ebecb4aa9b8aff48580132
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_smtplib.py:603:17"
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

## usage_mismatch:d620e8fc2e891f2e1d1a0811c2e57328:match

```yaml
regex_id: d620e8fc2e891f2e1d1a0811c2e57328
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Tools/cases_generator/generate_cases.py:108:18"
```

### Pattern

`^REG\(oparg(\d+)\)$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d71712ad48aeb75cad7adaf537292d60:match

```yaml
regex_id: d71712ad48aeb75cad7adaf537292d60
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:696:24"
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

## usage_mismatch:d737da2f8c32b4bf919cd2276e0dea55:match

```yaml
regex_id: d737da2f8c32b4bf919cd2276e0dea55
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:581:25"
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

## usage_mismatch:d8e7d1a0040a5c287e0757914d9d2f58:match

```yaml
regex_id: d8e7d1a0040a5c287e0757914d9d2f58
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:697:24"
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

## usage_mismatch:daded3f997dc821cbd6c5a11444faf51:search

```yaml
regex_id: daded3f997dc821cbd6c5a11444faf51
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/http/cookiejar.py:206:17"
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

## usage_mismatch:db21b2fb0126bb15cf7ebba781a008b0:match

```yaml
regex_id: db21b2fb0126bb15cf7ebba781a008b0
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:2292:25"
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

## usage_mismatch:dcf360ee2310f3be58914ee8789b8b45:match

```yaml
regex_id: dcf360ee2310f3be58914ee8789b8b45
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:699:24"
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

## usage_mismatch:decd8fe27668a712a48188f088d571fc:search

```yaml
regex_id: decd8fe27668a712a48188f088d571fc
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_smtplib.py:672:17"
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

## usage_mismatch:e1e58af4aead05bce9b9a26a1861af23:search

```yaml
regex_id: e1e58af4aead05bce9b9a26a1861af23
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/email/utils.py:257:23"
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

## usage_mismatch:e29194d7ebb4dbb6952f2467ee46f571:search

```yaml
regex_id: e29194d7ebb4dbb6952f2467ee46f571
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/doctest.py:626:27"
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

## usage_mismatch:e2e479d68d7e265fcc75f898821873cd:match

```yaml
regex_id: e2e479d68d7e265fcc75f898821873cd
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:573:25"
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

## usage_mismatch:e53e737125f0ac84d61f483793014994:search

```yaml
regex_id: e53e737125f0ac84d61f483793014994
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/http/cookiejar.py:1259:15"
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

## usage_mismatch:e5ff0abbdbb7423d275e803bc3a7b3fc:match

```yaml
regex_id: e5ff0abbdbb7423d275e803bc3a7b3fc
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:1514:29"
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

## usage_mismatch:e6bec599729a5c7fc0c4f2f57b2f5399:match

```yaml
regex_id: e6bec599729a5c7fc0c4f2f57b2f5399
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:677:26"
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

## usage_mismatch:e77d92c0d037d104b66e20ad1b5a4525:match

```yaml
regex_id: e77d92c0d037d104b66e20ad1b5a4525
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:578:26"
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

## usage_mismatch:e909ceb1b2f122b52e8da32e5c289bf8:search

```yaml
regex_id: e909ceb1b2f122b52e8da32e5c289bf8
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Doc/tools/extensions/pyspecific.py:469:14"
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

## usage_mismatch:ebec53e3754ce2fcad94aa4d81da7b5d:search

```yaml
regex_id: ebec53e3754ce2fcad94aa4d81da7b5d
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_smtplib.py:635:17"
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

## usage_mismatch:ee7de89b80e8114c22f725bcd286eb67:search

```yaml
regex_id: ee7de89b80e8114c22f725bcd286eb67
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/http/cookiejar.py:534:10"
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

## usage_mismatch:ef111b16f096a3df058c1fa88073f038:search

```yaml
regex_id: ef111b16f096a3df058c1fa88073f038
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Tools/c-analyzer/c_parser/preprocessor/gcc.py:16:23"
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

## usage_mismatch:ef6ee479015900f4c131e1b9d9470ac9:match

```yaml
regex_id: ef6ee479015900f4c131e1b9d9470ac9
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:2290:26"
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

## usage_mismatch:f5e7631dab619fbc25ec3dda0bceb0cd:search

```yaml
regex_id: f5e7631dab619fbc25ec3dda0bceb0cd
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/platform.py:1326:19"
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

## usage_mismatch:f68634220e8de26cc4c52da98303c973:search

```yaml
regex_id: f68634220e8de26cc4c52da98303c973
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/email/header.py:48:7"
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

## usage_mismatch:f8fd9cea4c063d2afceaa690c1f30eaa:match

```yaml
regex_id: f8fd9cea4c063d2afceaa690c1f30eaa
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:684:25"
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

## usage_mismatch:f94fdcf531377e0d7d9516e58e057d30:match

```yaml
regex_id: f94fdcf531377e0d7d9516e58e057d30
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:2304:24"
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

## usage_mismatch:fb7afc7cfe89c03d30ed1b67197c4753:search

```yaml
regex_id: fb7afc7cfe89c03d30ed1b67197c4753
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/http/cookiejar.py:344:25"
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

## usage_mismatch:fced05b2b5f84dddf10d6329fdfcea3e:match

```yaml
regex_id: fced05b2b5f84dddf10d6329fdfcea3e
schema_version: "1"
kind: usage_mismatch
corpus: nogil-3.12
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/nogil-3.12/rules/Lib/test/test_re.py:687:25"
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

## property:inventory:rc-shape1-injection-alphabet:rc-shape1-injection-alphabet

```yaml
regex_id: "inventory:rc-shape1-injection-alphabet"
schema_version: "1"
kind: property
corpus: nogil-3.12
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
corpus: nogil-3.12
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
corpus: nogil-3.12
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
corpus: nogil-3.12
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

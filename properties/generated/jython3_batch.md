---
schema_version: "1"
corpus: jython3
findings: 182
---

# jython3 batch findings

## usage_mismatch:01096c07e68ba0fffc40c905c17d5503:match

```yaml
regex_id: 01096c07e68ba0fffc40c905c17d5503
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:302:25"
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

## usage_mismatch:037bdbeb366b2ba783b838a05f003e73:search

```yaml
regex_id: 037bdbeb366b2ba783b838a05f003e73
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/urllib/parse.py:913:20"
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

## usage_mismatch:054ef07a39540780577a76dcc11b50b5:match

```yaml
regex_id: 054ef07a39540780577a76dcc11b50b5
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:313:25"
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

## usage_mismatch:05bc2bdb2242596c750d760a6e437cec:search

```yaml
regex_id: 05bc2bdb2242596c750d760a6e437cec
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_smtplib.py:367:17"
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

## usage_mismatch:08a89f150a50ca01b12fb9678fd8d7b3:search

```yaml
regex_id: 08a89f150a50ca01b12fb9678fd8d7b3
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:356:25"
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

## usage_mismatch:090d617c6162fdc6f2fcd27b54f7d5e3:search

```yaml
regex_id: 090d617c6162fdc6f2fcd27b54f7d5e3
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/Tools/scripts/h2py.py:32:12"
```

### Pattern

`^[	 ]*#[	 ]*include[	 ]+<([^>
]+)>`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:099c08ac697686bc3553b832c4097af8:search

```yaml
regex_id: 099c08ac697686bc3553b832c4097af8
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/http/cookiejar.py:332:25"
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

## usage_mismatch:0b0770698b63b8f397cd9b8efe9a698a:match

```yaml
regex_id: 0b0770698b63b8f397cd9b8efe9a698a
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/idlelib/FormatParagraph.py:175:11"
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

## usage_mismatch:0b977114a643b35689c60664838d85e0:search

```yaml
regex_id: 0b977114a643b35689c60664838d85e0
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_gdb.py:41:12"
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

## usage_mismatch:0e257943d65c7b1540e724478a3bffb7:match

```yaml
regex_id: 0e257943d65c7b1540e724478a3bffb7
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:254:25"
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

## usage_mismatch:0efeac71b62b6c06778a146d099cf1c8:match

```yaml
regex_id: 0efeac71b62b6c06778a146d099cf1c8
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:547:26"
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

## usage_mismatch:1001dd708ecaf6f02c17a02d7cd6d7af:match

```yaml
regex_id: 1001dd708ecaf6f02c17a02d7cd6d7af
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:305:25"
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

## usage_mismatch:166f52ea73e8b67b466a26c7fdfb86ed:search

```yaml
regex_id: 166f52ea73e8b67b466a26c7fdfb86ed
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/http/cookiejar.py:1234:15"
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

## usage_mismatch:19389a6c6a273c8810aded53802ccbdd:search

```yaml
regex_id: 19389a6c6a273c8810aded53802ccbdd
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/Tools/scripts/combinerefs.py:100:25"
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

## usage_mismatch:1b91d395d9b3c31e0c65a55a08558dc2:match

```yaml
regex_id: 1b91d395d9b3c31e0c65a55a08558dc2
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:316:28"
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

## usage_mismatch:1bdf79decf6a060183153cd9abf4298f:search

```yaml
regex_id: 1bdf79decf6a060183153cd9abf4298f
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/logging/config.py:354:18"
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

## usage_mismatch:1bec4d1650b10dd37f05118abbcbdbde:search

```yaml
regex_id: 1bec4d1650b10dd37f05118abbcbdbde
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/Tools/scripts/h2py.py:28:10"
```

### Pattern

`^[	 ]*#[	 ]*define[	 ]+([a-zA-Z0-9_]+)\(([_a-zA-Z][_a-zA-Z0-9]*)\)[	 ]+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1d4b5f3dd4e0d055b8d5193ff40671f4:match

```yaml
regex_id: 1d4b5f3dd4e0d055b8d5193ff40671f4
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:463:25"
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

## usage_mismatch:1fb89a8eae3edc60e82e2d77ff5ab358:search

```yaml
regex_id: 1fb89a8eae3edc60e82e2d77ff5ab358
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/Tools/scripts/texi2html.py:74:9"
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

## usage_mismatch:1fbf782b199aac73da668fe87375f283:match

```yaml
regex_id: 1fbf782b199aac73da668fe87375f283
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:303:25"
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

## usage_mismatch:226b9aced1335dbf7b3898b47472a6f0:match

```yaml
regex_id: 226b9aced1335dbf7b3898b47472a6f0
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:309:25"
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

## usage_mismatch:22ea46eb78ce33e1823211fb8eae9667:match

```yaml
regex_id: 22ea46eb78ce33e1823211fb8eae9667
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:467:25"
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

## usage_mismatch:232f50b18004d4feffba56439cde5da0:search

```yaml
regex_id: 232f50b18004d4feffba56439cde5da0
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_smtplib.py:464:17"
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

## usage_mismatch:239e4148f62bc727615b8592f69be113:search

```yaml
regex_id: 239e4148f62bc727615b8592f69be113
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/logging/config.py:271:13"
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

## usage_mismatch:25657d96e9fbc9c5370834635e9ea25d:search

```yaml
regex_id: 25657d96e9fbc9c5370834635e9ea25d
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_cookielib.py:1561:21"
```

### Pattern

`^\$version=\"?1\"?`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:25e76525d0b47132ab624ca7b940f413:search

```yaml
regex_id: 25e76525d0b47132ab624ca7b940f413
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:348:25"
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

## usage_mismatch:279b8eca6f7be55066229a635eba55c4:search

```yaml
regex_id: 279b8eca6f7be55066229a635eba55c4
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/email/header.py:48:7"
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

## usage_mismatch:299e4d58b327d26f5e98b50b26f8aa8b:match

```yaml
regex_id: 299e4d58b327d26f5e98b50b26f8aa8b
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:552:24"
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

## usage_mismatch:2aef7f0ebfab84a1fc47706c5391ea04:match

```yaml
regex_id: 2aef7f0ebfab84a1fc47706c5391ea04
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:465:26"
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

## usage_mismatch:2b0fac1acf3b46104863037ee8fea3b8:match

```yaml
regex_id: 2b0fac1acf3b46104863037ee8fea3b8
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:312:25"
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

## usage_mismatch:2bee91b36d1812f3ed81f5607cdbbdf9:match

```yaml
regex_id: 2bee91b36d1812f3ed81f5607cdbbdf9
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:250:25"
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

## usage_mismatch:2c38da662a2d3aa0b389668dd18ab4c1:match

```yaml
regex_id: 2c38da662a2d3aa0b389668dd18ab4c1
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:508:26"
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

## usage_mismatch:2e5ff0c3a634d42b2273ed3e79eac56a:search

```yaml
regex_id: 2e5ff0c3a634d42b2273ed3e79eac56a
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/doctest.py:1397:30"
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

## usage_mismatch:2eab764e88e8ffd4d6eddfcc63da0260:match

```yaml
regex_id: 2eab764e88e8ffd4d6eddfcc63da0260
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:308:25"
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

## usage_mismatch:311fdb23e2037a559979ac2e969ebc0f:match

```yaml
regex_id: 311fdb23e2037a559979ac2e969ebc0f
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:282:25"
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

## usage_mismatch:31634e47a814c40ecb7d03b435250851:match

```yaml
regex_id: 31634e47a814c40ecb7d03b435250851
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:304:25"
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

## usage_mismatch:32251e6b9154fd5f70a73da9f8378310:search

```yaml
regex_id: 32251e6b9154fd5f70a73da9f8378310
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/idlelib/IOBinding.py:65:11"
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

## usage_mismatch:329a3b5959c89fb372bd69cdfefd79f2:search

```yaml
regex_id: 329a3b5959c89fb372bd69cdfefd79f2
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/Tools/scripts/mailerdaemon.py:94:4"
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

## usage_mismatch:34638fdeb54ae6882335a0264da716c9:search

```yaml
regex_id: 34638fdeb54ae6882335a0264da716c9
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/doctest.py:609:27"
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

## usage_mismatch:35625ec61cac23e2104e39209b372491:match

```yaml
regex_id: 35625ec61cac23e2104e39209b372491
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:562:26"
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

## usage_mismatch:35c00740a9525661dacbbb9bbe152d5f:match

```yaml
regex_id: 35c00740a9525661dacbbb9bbe152d5f
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:542:25"
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

## usage_mismatch:35eb745ddf1efd58fc91fa02d8450bed:search

```yaml
regex_id: 35eb745ddf1efd58fc91fa02d8450bed
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/http/cookiejar.py:437:23"
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

## usage_mismatch:37741d1106781f21e0408222c216fdc7:search

```yaml
regex_id: 37741d1106781f21e0408222c216fdc7
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/logging/config.py:356:20"
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

## usage_mismatch:386ec20ab6e2453b4465ea7f102135b8:match

```yaml
regex_id: 386ec20ab6e2453b4465ea7f102135b8
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:256:25"
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

## usage_mismatch:39ab4db29f3e4e6d6ad2875896a0bc72:search

```yaml
regex_id: 39ab4db29f3e4e6d6ad2875896a0bc72
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/http/cookiejar.py:276:14"
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

## usage_mismatch:3a4e040c22a850351337a8deb037ca1d:match

```yaml
regex_id: 3a4e040c22a850351337a8deb037ca1d
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:274:25"
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

## usage_mismatch:3c4bc88b8b32f27021f8db81f65d471c:search

```yaml
regex_id: 3c4bc88b8b32f27021f8db81f65d471c
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/http/cookiejar.py:201:13"
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

## usage_mismatch:3d1614f20dc344d9be1bc63604aaddf7:search

```yaml
regex_id: 3d1614f20dc344d9be1bc63604aaddf7
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:1275:18"
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

## usage_mismatch:3fd48b4bcf22a72003a6a554b634f0dd:search

```yaml
regex_id: 3fd48b4bcf22a72003a6a554b634f0dd
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/Tools/scripts/texi2html.py:73:9"
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

## usage_mismatch:42f3c2204a5d7546d397d49dd3fea5b8:search

```yaml
regex_id: 42f3c2204a5d7546d397d49dd3fea5b8
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/Tools/scripts/mailerdaemon.py:92:4"
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

## usage_mismatch:442bf2959675bffecc0a30c47f56585c:search

```yaml
regex_id: 442bf2959675bffecc0a30c47f56585c
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/Tools/scripts/h2py.py:26:11"
```

### Pattern

`^[	 ]*#[	 ]*define[	 ]+([a-zA-Z0-9_]+)[	 ]+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:44a9ef1563b8dc83748d34bf812e5019:match

```yaml
regex_id: 44a9ef1563b8dc83748d34bf812e5019
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:252:25"
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

## usage_mismatch:46f580e13369007c1c3bf8245cc1c4ce:match

```yaml
regex_id: 46f580e13369007c1c3bf8245cc1c4ce
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:534:26"
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

## usage_mismatch:475328d997844bf3269255dc3013b759:match

```yaml
regex_id: 475328d997844bf3269255dc3013b759
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:554:24"
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

## usage_mismatch:4db1619f19ed4ab42458d21e7ed26610:match

```yaml
regex_id: 4db1619f19ed4ab42458d21e7ed26610
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:1234:30"
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

## usage_mismatch:5105ec027fca20c21333adc6549f8566:search

```yaml
regex_id: 5105ec027fca20c21333adc6549f8566
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/Tools/scripts/texi2html.py:81:9"
```

### Pattern

`^\* ([^:]*):(:|[ 	]*([^	,
.]+)([^ 	
]*))[ 	
]*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:510c1f7879e38799842d9d9963dc14ea:match

```yaml
regex_id: 510c1f7879e38799842d9d9963dc14ea
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:258:25"
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

## usage_mismatch:53038d31c4367f211114c807039e2e84:search

```yaml
regex_id: 53038d31c4367f211114c807039e2e84
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_smtplib.py:148:19"
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

## usage_mismatch:557c276c4e927f0e5b9907d9eb3f1996:match

```yaml
regex_id: 557c276c4e927f0e5b9907d9eb3f1996
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:314:25"
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

## usage_mismatch:57db4c462c0bf2c77079a74106fbd22c:search

```yaml
regex_id: 57db4c462c0bf2c77079a74106fbd22c
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/idlelib/PyShell.py:1208:35"
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

## usage_mismatch:589b19292fb6c5563f8f1d5b3ae0746b:search

```yaml
regex_id: 589b19292fb6c5563f8f1d5b3ae0746b
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/http/cookiejar.py:331:25"
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

## usage_mismatch:5928ef605ae8cf55951102d7b8d3e185:search

```yaml
regex_id: 5928ef605ae8cf55951102d7b8d3e185
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/http/cookiejar.py:130:14"
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

## usage_mismatch:59ca2abe4fe812ba2cef540bb164fc79:match

```yaml
regex_id: 59ca2abe4fe812ba2cef540bb164fc79
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:319:28"
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

## usage_mismatch:5bf489de01c615f153df269a7dc99eb2:search

```yaml
regex_id: 5bf489de01c615f153df269a7dc99eb2
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/xml/Uri.py:39:24"
```

### Pattern

`^(?:(?P<scheme>[^:/?#]+):)?(?://(?P<authority>[^/?#]*))?(?P<path>[^?#]*)(?:\?(?P<query>[^#]*))?(?:#(?P<fragment>.*))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5cd822b813a22cbabfe9f199fae249a0:search

```yaml
regex_id: 5cd822b813a22cbabfe9f199fae249a0
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/idlelib/IOBinding.py:64:12"
```

### Pattern

`^[ \t\f]*#.*coding[:=][ \t]*([-\w.]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5ddb3bcfafa1e68b7bf0ed682650b508:search

```yaml
regex_id: 5ddb3bcfafa1e68b7bf0ed682650b508
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_cookielib.py:29:28"
```

### Pattern

`^\d{4}-\d\d-\d\d \d\d:\d\d:\d\dZ$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5ddd3398b61c87b8eec63fe0a73dc45b:search

```yaml
regex_id: 5ddd3398b61c87b8eec63fe0a73dc45b
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_smtplib.py:527:17"
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

## usage_mismatch:5edbb4b7b5912b748514849b2e22adac:search

```yaml
regex_id: 5edbb4b7b5912b748514849b2e22adac
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/xml/Uri.py:180:24"
```

### Pattern

`^(?:(?:[0-9A-Za-z\-_\.!~*'();&=+$,]|(?:%[0-9A-Fa-f]{2}))*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:60e0b2962db5da849d28c8a260b648a6:search

```yaml
regex_id: 60e0b2962db5da849d28c8a260b648a6
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/http/cookiejar.py:605:14"
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

## usage_mismatch:6132e8129712010538c8fe89fab52a22:match

```yaml
regex_id: 6132e8129712010538c8fe89fab52a22
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:553:24"
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

## usage_mismatch:616f7cccc01a2021ecc4f8a863505109:match

```yaml
regex_id: 616f7cccc01a2021ecc4f8a863505109
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:278:25"
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

## usage_mismatch:64f1caf59112c4e646e90e60c5b4c23d:match

```yaml
regex_id: 64f1caf59112c4e646e90e60c5b4c23d
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:471:25"
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

## usage_mismatch:6637de9a276e42de58aa50fc31119375:match

```yaml
regex_id: 6637de9a276e42de58aa50fc31119375
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:326:28"
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

## usage_mismatch:67d7703369b5f93bc1da1c397636e74f:search

```yaml
regex_id: 67d7703369b5f93bc1da1c397636e74f
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/http/cookiejar.py:520:10"
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

## usage_mismatch:69848c282aaadb8bca596012aac1ab69:match

```yaml
regex_id: 69848c282aaadb8bca596012aac1ab69
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:545:25"
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

## usage_mismatch:6b9f2f4e35731dbead58653269a4ec02:match

```yaml
regex_id: 6b9f2f4e35731dbead58653269a4ec02
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:276:25"
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

## usage_mismatch:6ceb00701fc02cba5754ef5ea1a84297:match

```yaml
regex_id: 6ceb00701fc02cba5754ef5ea1a84297
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:248:25"
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

## usage_mismatch:715f9659d6e78d9f5175319b52950aa8:match

```yaml
regex_id: 715f9659d6e78d9f5175319b52950aa8
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:311:25"
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

## usage_mismatch:71cc97c1df2189d8bfbf97a7e3dda040:search

```yaml
regex_id: 71cc97c1df2189d8bfbf97a7e3dda040
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/configparser.py:1291:16"
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

## usage_mismatch:72f644ab21769a63c8f0276c01894368:match

```yaml
regex_id: 72f644ab21769a63c8f0276c01894368
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:558:24"
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

## usage_mismatch:73320efbd884567bd3a13724fec117fd:match

```yaml
regex_id: 73320efbd884567bd3a13724fec117fd
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:322:28"
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

## usage_mismatch:763937724131f799dd1415a161cd5379:search

```yaml
regex_id: 763937724131f799dd1415a161cd5379
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/Tools/scripts/mailerdaemon.py:168:10"
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

## usage_mismatch:76725b32296dfc4291f4f0b7e402e89c:match

```yaml
regex_id: 76725b32296dfc4291f4f0b7e402e89c
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:538:25"
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

## usage_mismatch:76f80e6806cf7de9b51ce80863f49969:match

```yaml
regex_id: 76f80e6806cf7de9b51ce80863f49969
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:469:25"
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

## usage_mismatch:79b0a48211fea36cbac5bdb907ae53b5:match

```yaml
regex_id: 79b0a48211fea36cbac5bdb907ae53b5
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:321:28"
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

## usage_mismatch:7b0ea200ccb06e11f97b3ec6b87a7de0:search

```yaml
regex_id: 7b0ea200ccb06e11f97b3ec6b87a7de0
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_cookielib.py:1364:24"
```

### Pattern

`^\$Version="?1"?;`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7c081e3eadb74d5b63351669ef024c8c:match

```yaml
regex_id: 7c081e3eadb74d5b63351669ef024c8c
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:253:25"
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

## usage_mismatch:7d384b7c09a23c821d7c1c58df57122d:search

```yaml
regex_id: 7d384b7c09a23c821d7c1c58df57122d
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/distutils/versionpredicate.py:12:11"
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

## usage_mismatch:7ebe14c889dc5289b33451e3a9e4d8d8:match

```yaml
regex_id: 7ebe14c889dc5289b33451e3a9e4d8d8
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:540:25"
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

## usage_mismatch:80fbd5f80d3ce7fae5964c88e55688db:search

```yaml
regex_id: 80fbd5f80d3ce7fae5964c88e55688db
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/http/cookiejar.py:1232:14"
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

## usage_mismatch:81d67a15e36513a3706bf0e9f642c6b4:search

```yaml
regex_id: 81d67a15e36513a3706bf0e9f642c6b4
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/Tools/scripts/mailerdaemon.py:96:20"
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

## usage_mismatch:82c7154aee1c2cb57d9a6053d762cc91:search

```yaml
regex_id: 82c7154aee1c2cb57d9a6053d762cc91
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/doctest.py:758:17"
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

## usage_mismatch:8439f10e5dcaa77e1b9d0ca7997493cb:match

```yaml
regex_id: 8439f10e5dcaa77e1b9d0ca7997493cb
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:260:25"
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

## usage_mismatch:84c2dc200f9c522635b77030dd434d72:search

```yaml
regex_id: 84c2dc200f9c522635b77030dd434d72
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:355:25"
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

## usage_mismatch:8669cc6bcee156df63bcd9afb36ae594:search

```yaml
regex_id: 8669cc6bcee156df63bcd9afb36ae594
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_smtplib.py:138:19"
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

## usage_mismatch:8691a29cdeddd88577475a5e9963e7b3:search

```yaml
regex_id: 8691a29cdeddd88577475a5e9963e7b3
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_cookielib.py:1339:24"
```

### Pattern

`^\$Version="?1"?; Customer="?WILE_E_COYOTE"?; \$Path="/acme"$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8a080cddcad07ebe09dc107bc4db1f9a:search

```yaml
regex_id: 8a080cddcad07ebe09dc107bc4db1f9a
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/distutils/versionpredicate.py:156:24"
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

## usage_mismatch:8d305a60346506d474ae66b60073b49e:search

```yaml
regex_id: 8d305a60346506d474ae66b60073b49e
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/decimal.py:5890:14"
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

## usage_mismatch:8daaabb24dbb1cecd6855d8a3c1a613c:match

```yaml
regex_id: 8daaabb24dbb1cecd6855d8a3c1a613c
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:549:26"
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

## usage_mismatch:8dbef18379f8a37b1ab079de69054ce6:search

```yaml
regex_id: 8dbef18379f8a37b1ab079de69054ce6
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/Tools/scripts/pindent.py:109:22"
```

### Pattern

`^(?:\s|\\\n)*(?P<kw>[a-z]+)((?:\s|\\\n)+(?P<id>[a-zA-Z_]\w*))?[^\w]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8f413821d3739aa1cf181325e266b0b0:search

```yaml
regex_id: 8f413821d3739aa1cf181325e266b0b0
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:1280:18"
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

## usage_mismatch:9009c7cd8a05598af74a2dda75974649:search

```yaml
regex_id: 9009c7cd8a05598af74a2dda75974649
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:601:26"
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

## usage_mismatch:92984142b64f50a5b9cf7229ffcd48e7:match

```yaml
regex_id: 92984142b64f50a5b9cf7229ffcd48e7
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:306:25"
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

## usage_mismatch:92cca0a00a3716fe19ef4dba92321d2e:search

```yaml
regex_id: 92cca0a00a3716fe19ef4dba92321d2e
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:600:25"
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

## usage_mismatch:93162661c08d03864c7c74fa79e08d9e:search

```yaml
regex_id: 93162661c08d03864c7c74fa79e08d9e
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:357:25"
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

## usage_mismatch:93980dbe89e9b40b6e281c18c8ae6398:match

```yaml
regex_id: 93980dbe89e9b40b6e281c18c8ae6398
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:317:28"
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

## usage_mismatch:9438ac030884d9d482a1a104e6f2f721:match

```yaml
regex_id: 9438ac030884d9d482a1a104e6f2f721
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:559:24"
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

## usage_mismatch:959fbb1802e2df965a61ff68797ccb27:match

```yaml
regex_id: 959fbb1802e2df965a61ff68797ccb27
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:533:26"
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

## usage_mismatch:96aadcbe518c7908c5d4d8baabeb68f4:search

```yaml
regex_id: 96aadcbe518c7908c5d4d8baabeb68f4
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/distutils/versionpredicate.py:13:21"
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

## usage_mismatch:96c7fe0595456bcc448fa721582aefcf:search

```yaml
regex_id: 96c7fe0595456bcc448fa721582aefcf
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/Tools/scripts/texi2html.py:1598:19"
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

## usage_mismatch:98b1055fc48b3d0342c6a42039d6a98e:search

```yaml
regex_id: 98b1055fc48b3d0342c6a42039d6a98e
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:467:32"
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

## usage_mismatch:9a5834354fab2da63e16c9ebb72fe0b6:match

```yaml
regex_id: 9a5834354fab2da63e16c9ebb72fe0b6
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:466:26"
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

## usage_mismatch:9cf6f0a990b402d509afb18fcdca473e:search

```yaml
regex_id: 9cf6f0a990b402d509afb18fcdca473e
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/email/utils.py:260:23"
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

## intent_mismatch:a1078f07209f974947d8e4cdddeda4f5:email

```yaml
regex_id: a1078f07209f974947d8e4cdddeda4f5
schema_version: "1"
kind: intent_mismatch
corpus: jython3
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/email/feedparser.py:37:11"
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

## usage_mismatch:a1078f07209f974947d8e4cdddeda4f5:search

```yaml
regex_id: a1078f07209f974947d8e4cdddeda4f5
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/email/feedparser.py:37:11"
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

## usage_mismatch:a27a1c94301190a3d8750be3b513d235:search

```yaml
regex_id: a27a1c94301190a3d8750be3b513d235
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/textwrap.py:412:22"
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

## usage_mismatch:a2e04da3d7abe5b3193d63d22422cfc3:match

```yaml
regex_id: a2e04da3d7abe5b3193d63d22422cfc3
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:323:28"
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

## usage_mismatch:a344b76cffcad969378bc0ce7ec0eb59:search

```yaml
regex_id: a344b76cffcad969378bc0ce7ec0eb59
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/Tools/scripts/pindent.py:117:22"
```

### Pattern

`^[ \t]*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a54e88f6d3edb934dad1f5f84026d7e5:match

```yaml
regex_id: a54e88f6d3edb934dad1f5f84026d7e5
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:297:25"
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

## usage_mismatch:a5a532f891e53d1c1250c273e47773ef:match

```yaml
regex_id: a5a532f891e53d1c1250c273e47773ef
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:543:25"
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

## usage_mismatch:a60a22d09aed7c8f83775f343d4413d8:search

```yaml
regex_id: a60a22d09aed7c8f83775f343d4413d8
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/Tools/scripts/combinerefs.py:93:25"
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

## usage_mismatch:a7ebb5463a1bc9dfe6cabacd06136162:search

```yaml
regex_id: a7ebb5463a1bc9dfe6cabacd06136162
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:599:25"
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

## usage_mismatch:a82c146661aa3f8a654f6263517327c2:search

```yaml
regex_id: a82c146661aa3f8a654f6263517327c2
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/logging/config.py:353:19"
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

## usage_mismatch:abf5ce9f024308fcabfb3b10a9cbaf24:match

```yaml
regex_id: abf5ce9f024308fcabfb3b10a9cbaf24
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:504:25"
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

## usage_mismatch:ad9361f41c7da3ed89333b1f67784d45:match

```yaml
regex_id: ad9361f41c7da3ed89333b1f67784d45
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:280:25"
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

## usage_mismatch:ae376f3c1bf48891e31a6bb78f7735ec:match

```yaml
regex_id: ae376f3c1bf48891e31a6bb78f7735ec
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:535:26"
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

## usage_mismatch:afc62b974c93a54d68300e1fe4f2cc8f:match

```yaml
regex_id: afc62b974c93a54d68300e1fe4f2cc8f
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:563:24"
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

## usage_mismatch:afd5bfbb26d54b520cd8ce82ce5b0b80:match

```yaml
regex_id: afd5bfbb26d54b520cd8ce82ce5b0b80
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:318:28"
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

## usage_mismatch:b0ccfd7e3f46a8b1069a06e905f65da3:search

```yaml
regex_id: b0ccfd7e3f46a8b1069a06e905f65da3
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/http/cookiejar.py:198:17"
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

## usage_mismatch:b3833c8bbbcf785105d02dc4fa084b4c:match

```yaml
regex_id: b3833c8bbbcf785105d02dc4fa084b4c
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:539:25"
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

## usage_mismatch:b449f6e634eb1579050821224af02a96:search

```yaml
regex_id: b449f6e634eb1579050821224af02a96
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/logging/config.py:355:20"
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

## usage_mismatch:b7f70fb1ff79b299944c4c5e81741f45:search

```yaml
regex_id: b7f70fb1ff79b299944c4c5e81741f45
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_smtplib.py:438:17"
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

## usage_mismatch:ba9b8847496ba4baa4ed744f0ecfdca3:match

```yaml
regex_id: ba9b8847496ba4baa4ed744f0ecfdca3
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:298:25"
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

## usage_mismatch:baf7ce30f2ba01eed8cc4615d7deb943:match

```yaml
regex_id: baf7ce30f2ba01eed8cc4615d7deb943
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:299:25"
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

## usage_mismatch:bf621d0abe6aec0b7048c07e914a2d0c:match

```yaml
regex_id: bf621d0abe6aec0b7048c07e914a2d0c
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:300:25"
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

## usage_mismatch:c038b37a592d0ac278185a4a711eb37e:search

```yaml
regex_id: c038b37a592d0ac278185a4a711eb37e
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:1433:12"
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

## usage_mismatch:c227ed74408a64d271c0de27ff862bb1:search

```yaml
regex_id: c227ed74408a64d271c0de27ff862bb1
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/_pydecimal.py:6107:14"
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

## usage_mismatch:c6270a60b77e0763f9a2150cd8071bf2:match

```yaml
regex_id: c6270a60b77e0763f9a2150cd8071bf2
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:560:24"
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

## usage_mismatch:c8b1887f706fb72f652ead121da330fd:search

```yaml
regex_id: c8b1887f706fb72f652ead121da330fd
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/Tools/scripts/pindent.py:113:23"
```

### Pattern

`^(?:\s|\\\n)*#?\s*end\s+(?P<kw>[a-z]+)(\s+(?P<id>[a-zA-Z_]\w*))?[^\w]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c8b2b7f633efad64abfa78b52add2c9b:search

```yaml
regex_id: c8b2b7f633efad64abfa78b52add2c9b
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:924:28"
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

## usage_mismatch:c8f0bf23db372efb86407d6f07b333de:match

```yaml
regex_id: c8f0bf23db372efb86407d6f07b333de
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:279:25"
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

## usage_mismatch:caf0a93131bc1957350ea2b9d8fb8243:match

```yaml
regex_id: caf0a93131bc1957350ea2b9d8fb8243
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:510:25"
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

## usage_mismatch:cd39c00dfb17fb91e2bb2443250c1714:search

```yaml
regex_id: cd39c00dfb17fb91e2bb2443250c1714
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/urllib/request.py:246:15"
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

## usage_mismatch:cd863be21a0df4ba93102a33943080cb:match

```yaml
regex_id: cd863be21a0df4ba93102a33943080cb
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:557:24"
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

## usage_mismatch:ce369d89e8f8c03c92eb68cac0e36f6c:match

```yaml
regex_id: ce369d89e8f8c03c92eb68cac0e36f6c
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:512:25"
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

## usage_mismatch:ce56145b09ca9905b1c37de9e97d3e80:match

```yaml
regex_id: ce56145b09ca9905b1c37de9e97d3e80
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:541:25"
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

## usage_mismatch:d159b57210519c1457ac3d69ccfcd939:search

```yaml
regex_id: d159b57210519c1457ac3d69ccfcd939
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:349:25"
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

## usage_mismatch:d272849271f2e0a246833a9d01ebc36b:match

```yaml
regex_id: d272849271f2e0a246833a9d01ebc36b
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:509:26"
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

## usage_mismatch:d3508f995d3cd6e1198794b3bba5b422:match

```yaml
regex_id: d3508f995d3cd6e1198794b3bba5b422
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:473:25"
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

## intent_mismatch:d5bae28ed17a8127c7da76120d62f250:email

```yaml
regex_id: d5bae28ed17a8127c7da76120d62f250
schema_version: "1"
kind: intent_mismatch
corpus: jython3
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/email/utils.py:118:7"
```

### Pattern

`
  =\?                   # literal =?
  (?P<charset>[^?]*?)   # non-greedy up to the next ? is the charset
  \?                    # literal ?
  (?P<encoding>[qb])    # either a "q" or a "b", case insensitive
  \?                    # literal ?
  (?P<atom>.*?)         # non-greedy up to the next ?= is the atom
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

## usage_mismatch:d7da1b6d768649bb56a9af5a9f2d69a9:match

```yaml
regex_id: d7da1b6d768649bb56a9af5a9f2d69a9
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:506:25"
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

## usage_mismatch:d901a84aa65b742bcadb4d838e1f16c2:match

```yaml
regex_id: d901a84aa65b742bcadb4d838e1f16c2
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:1225:29"
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

## usage_mismatch:d941a340d90e2ee809c6d006fbe3970c:match

```yaml
regex_id: d941a340d90e2ee809c6d006fbe3970c
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:555:24"
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

## usage_mismatch:d94d736713d3a5c44e225f829a014d18:search

```yaml
regex_id: d94d736713d3a5c44e225f829a014d18
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_smtplib.py:470:16"
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

## usage_mismatch:d9a799b219c5ed91f1d3739fccc2c8b9:search

```yaml
regex_id: d9a799b219c5ed91f1d3739fccc2c8b9
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:456:12"
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

## usage_mismatch:dab1714f40ce360b94b7d72e0e4d5a48:match

```yaml
regex_id: dab1714f40ce360b94b7d72e0e4d5a48
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:544:25"
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

## usage_mismatch:de3b59952cef0135a51985a19ebcf0b1:search

```yaml
regex_id: de3b59952cef0135a51985a19ebcf0b1
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/pydoc.py:131:14"
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

## usage_mismatch:dfb987ba731f21a9791a3a4023e90ed4:search

```yaml
regex_id: dfb987ba731f21a9791a3a4023e90ed4
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:350:25"
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

## usage_mismatch:e1ab902d403bea25578f5e503752a0e2:match

```yaml
regex_id: e1ab902d403bea25578f5e503752a0e2
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:325:25"
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

## usage_mismatch:e33517baa2ba2b984f4c4b048c62c4c7:match

```yaml
regex_id: e33517baa2ba2b984f4c4b048c62c4c7
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:461:25"
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

## usage_mismatch:e3b4e482ec27167a3ddf0c1cdcf2a9ae:search

```yaml
regex_id: e3b4e482ec27167a3ddf0c1cdcf2a9ae
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_smtplib.py:493:17"
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

## usage_mismatch:e46dce92d3063acfc1f9e45e1e78345a:match

```yaml
regex_id: e46dce92d3063acfc1f9e45e1e78345a
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:320:28"
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

## usage_mismatch:e8190827a64a13ad12c706dae0c8c048:search

```yaml
regex_id: e8190827a64a13ad12c706dae0c8c048
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/http/cookiejar.py:330:25"
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

## usage_mismatch:eb05950bc5421e4f59fe5a9e4f091700:search

```yaml
regex_id: eb05950bc5421e4f59fe5a9e4f091700
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/idlelib/PyShell.py:1209:35"
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

## usage_mismatch:eb09d62bb2ccfa4a9c837d6934462603:match

```yaml
regex_id: eb09d62bb2ccfa4a9c837d6934462603
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/test/test_re.py:307:25"
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

## usage_mismatch:edd47117e233824d0ddfe9a9a041bbea:match

```yaml
regex_id: edd47117e233824d0ddfe9a9a041bbea
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:548:26"
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

## usage_mismatch:edf5ee6c21dfd12b544108e1f01be70c:match

```yaml
regex_id: edf5ee6c21dfd12b544108e1f01be70c
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:536:26"
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

## usage_mismatch:eed5147e3491aa8e52ed75d3a69e7a8b:match

```yaml
regex_id: eed5147e3491aa8e52ed75d3a69e7a8b
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:550:26"
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

## usage_mismatch:f3f9403a0706da9aa3f320a53ac0578d:search

```yaml
regex_id: f3f9403a0706da9aa3f320a53ac0578d
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/logging/config.py:351:22"
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

## usage_mismatch:f64a248f3f2c60020f41f5e3a0b2045a:match

```yaml
regex_id: f64a248f3f2c60020f41f5e3a0b2045a
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_re.py:556:24"
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

## usage_mismatch:f79356f3c939d08d617685d76fe4a5ab:search

```yaml
regex_id: f79356f3c939d08d617685d76fe4a5ab
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/doctest.py:727:27"
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

## usage_mismatch:f7fa6e9af4b9258cae40095874567e30:search

```yaml
regex_id: f7fa6e9af4b9258cae40095874567e30
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/lib2to3/pgen2/tokenize.py:239:12"
```

### Pattern

`^[ \t\f]*#.*coding[:=][ \t]*([-\w.]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f8b2e2e3b560f5e732416026f56f8fd0:search

```yaml
regex_id: f8b2e2e3b560f5e732416026f56f8fd0
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/Lib/decimal.py:5889:13"
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

## usage_mismatch:fabb79748a2f572ff7c50c99d35be84c:search

```yaml
regex_id: fabb79748a2f572ff7c50c99d35be84c
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/http/cookiejar.py:203:21"
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

## usage_mismatch:fad879c6f9e06365177679f01d63c9e4:search

```yaml
regex_id: fad879c6f9e06365177679f01d63c9e4
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/_pydecimal.py:6106:13"
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

## intent_mismatch:fd8d410c667d715c9eae9ef53b934ef1:email

```yaml
regex_id: fd8d410c667d715c9eae9ef53b934ef1
schema_version: "1"
kind: intent_mismatch
corpus: jython3
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/email/header.py:35:7"
```

### Pattern

`
  =\?                   # literal =?
  (?P<charset>[^?]*?)   # non-greedy up to the next ? is the charset
  \?                    # literal ?
  (?P<encoding>[qb])    # either a "q" or a "b", case insensitive
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

## usage_mismatch:feece3b5a003982388a9e06c69cb9d9f:search

```yaml
regex_id: feece3b5a003982388a9e06c69cb9d9f
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/test/test_smtplib.py:411:17"
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

## usage_mismatch:ff92259f4f1ca1337318f4d1328a6faa:match

```yaml
regex_id: ff92259f4f1ca1337318f4d1328a6faa
schema_version: "1"
kind: usage_mismatch
corpus: jython3
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/jython3/rules/lib-python/3.5.1/lib2to3/pgen2/conv.py:71:17"
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

## property:inventory:rc-shape1-injection-alphabet:rc-shape1-injection-alphabet

```yaml
regex_id: "inventory:rc-shape1-injection-alphabet"
schema_version: "1"
kind: property
corpus: jython3
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
corpus: jython3
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
corpus: jython3
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
corpus: jython3
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

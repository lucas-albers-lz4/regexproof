---
schema_version: "1"
corpus: gilectomy
findings: 140
---

# gilectomy batch findings

## usage_mismatch:012c0c8302d215d7a4af803247640c7f:match

```yaml
regex_id: 012c0c8302d215d7a4af803247640c7f
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:1234:30"
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

## usage_mismatch:01c92587046c5825af2987a256c89a1e:search

```yaml
regex_id: 01c92587046c5825af2987a256c89a1e
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Tools/scripts/h2py.py:28:10"
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

## usage_mismatch:02a2a9e20ee8a1233ea4cba67b9d980f:search

```yaml
regex_id: 02a2a9e20ee8a1233ea4cba67b9d980f
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/setup.py:840:25"
```

### Pattern

`^\s*#\s*define\s+OPENSSL_VERSION_NUMBER\s+(0x[0-9a-fA-F]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:02e9e09e7d365b782bd4d5ac4b63eb2b:match

```yaml
regex_id: 02e9e09e7d365b782bd4d5ac4b63eb2b
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:504:25"
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

## usage_mismatch:07f05ca7a22b83a5fee5e03b68060b05:search

```yaml
regex_id: 07f05ca7a22b83a5fee5e03b68060b05
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/lib2to3/pgen2/tokenize.py:239:12"
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

## usage_mismatch:08458fac8d65b8be5fde91432d3b18c8:match

```yaml
regex_id: 08458fac8d65b8be5fde91432d3b18c8
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/msilib/__init__.py:183:11"
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

## usage_mismatch:0ba710e5baa710dab3b7a15d6e307a42:match

```yaml
regex_id: 0ba710e5baa710dab3b7a15d6e307a42
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:473:25"
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

## usage_mismatch:0d9a974eeb1dee5b8fac385804e1d0d2:search

```yaml
regex_id: 0d9a974eeb1dee5b8fac385804e1d0d2
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/email/header.py:48:7"
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

## usage_mismatch:0db93d13932e86c509dff58757b1e818:search

```yaml
regex_id: 0db93d13932e86c509dff58757b1e818
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/logging/config.py:351:22"
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

## usage_mismatch:0dc55984a9a2e24d98c6e17d027b6ecc:match

```yaml
regex_id: 0dc55984a9a2e24d98c6e17d027b6ecc
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:536:26"
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

## usage_mismatch:0eed96524f532c7a0c97fadb0c60d484:search

```yaml
regex_id: 0eed96524f532c7a0c97fadb0c60d484
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_smtplib.py:148:19"
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

## usage_mismatch:10b102d407bf1ea05971eebfb389dfba:match

```yaml
regex_id: 10b102d407bf1ea05971eebfb389dfba
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Tools/demo/ss1.py:417:16"
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

## usage_mismatch:11f03277063f7b0eb2451d78438dd47f:search

```yaml
regex_id: 11f03277063f7b0eb2451d78438dd47f
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:1280:18"
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

## usage_mismatch:14fb90c7d48644556132cf4754812410:match

```yaml
regex_id: 14fb90c7d48644556132cf4754812410
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:549:26"
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

## usage_mismatch:159ea29c62b392a2ce96d3a769d55348:search

```yaml
regex_id: 159ea29c62b392a2ce96d3a769d55348
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:600:25"
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

## usage_mismatch:15e7793c9d8a66b43eca1ff1bd8f353f:search

```yaml
regex_id: 15e7793c9d8a66b43eca1ff1bd8f353f
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/distutils/versionpredicate.py:13:21"
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

## usage_mismatch:16532078802c0c00f600f7ce039c1586:search

```yaml
regex_id: 16532078802c0c00f600f7ce039c1586
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/http/cookiejar.py:335:25"
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

## usage_mismatch:16e7519201bcdf337e12a15432b115c4:match

```yaml
regex_id: 16e7519201bcdf337e12a15432b115c4
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:469:25"
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

## usage_mismatch:18417bef082e6f97995319cc369cff2d:search

```yaml
regex_id: 18417bef082e6f97995319cc369cff2d
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/doctest.py:737:27"
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

## usage_mismatch:19601d79af808920fe77c8eea97b5abc:match

```yaml
regex_id: 19601d79af808920fe77c8eea97b5abc
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:544:25"
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

## usage_mismatch:1b46b4c54bc27eb53757586eae9b726c:match

```yaml
regex_id: 1b46b4c54bc27eb53757586eae9b726c
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:557:24"
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

## usage_mismatch:1d8ffe0ea7e5506b80f1d8a6d35fa4d3:search

```yaml
regex_id: 1d8ffe0ea7e5506b80f1d8a6d35fa4d3
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/logging/config.py:356:20"
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

## usage_mismatch:1e3b4c04413f5f4e0f494a7a27acb49f:search

```yaml
regex_id: 1e3b4c04413f5f4e0f494a7a27acb49f
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/logging/config.py:354:18"
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

## usage_mismatch:1eb8643164200d7d57bb14a9c4b87718:match

```yaml
regex_id: 1eb8643164200d7d57bb14a9c4b87718
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:535:26"
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

## usage_mismatch:20225b2c90d26eeffe79b97c5b9f6d80:search

```yaml
regex_id: 20225b2c90d26eeffe79b97c5b9f6d80
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/unittest/test/test_case.py:1283:46"
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

## usage_mismatch:20a8b2065ef412c276de1d28f4f615bb:search

```yaml
regex_id: 20a8b2065ef412c276de1d28f4f615bb
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/idlelib/MultiCall.py:266:13"
```

### Pattern

`^[1-5]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:21169c50cd63ca66c4ef7ca26cd7f3a1:search

```yaml
regex_id: 21169c50cd63ca66c4ef7ca26cd7f3a1
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Doc/tools/extensions/pyspecific.py:229:14"
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

## usage_mismatch:242fb34ec35bbacb58d5cfd349091e39:search

```yaml
regex_id: 242fb34ec35bbacb58d5cfd349091e39
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_smtplib.py:367:17"
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

## usage_mismatch:260096ce4afc777742137fe04ff39e28:search

```yaml
regex_id: 260096ce4afc777742137fe04ff39e28
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/http/cookiejar.py:1235:14"
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

## usage_mismatch:29b593ec61071214d14b3ec2b61ef6f9:match

```yaml
regex_id: 29b593ec61071214d14b3ec2b61ef6f9
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:534:26"
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

## usage_mismatch:2b1ae1d051d1603c2bdcd37728663e5e:search

```yaml
regex_id: 2b1ae1d051d1603c2bdcd37728663e5e
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/nntplib.py:612:19"
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

## usage_mismatch:2c5fd571152dd0f95610a0ccbae62b96:search

```yaml
regex_id: 2c5fd571152dd0f95610a0ccbae62b96
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_smtplib.py:470:16"
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

## usage_mismatch:2d9bfb47b8d8118493e4d45208c09535:match

```yaml
regex_id: 2d9bfb47b8d8118493e4d45208c09535
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:553:24"
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

## usage_mismatch:311d75e98aaffaddcae4c2c13c080c1d:match

```yaml
regex_id: 311d75e98aaffaddcae4c2c13c080c1d
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:539:25"
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

## usage_mismatch:322b8b7eb9f32f1cda3d929d2e9c8cc3:match

```yaml
regex_id: 322b8b7eb9f32f1cda3d929d2e9c8cc3
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:560:24"
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

## usage_mismatch:36b1a6f524f9fa9b1127a323f0d0fa4b:search

```yaml
regex_id: 36b1a6f524f9fa9b1127a323f0d0fa4b
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Tools/scripts/texi2html.py:81:9"
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

## usage_mismatch:39cb2a45514f44a3b1dfd8ef9bd36530:search

```yaml
regex_id: 39cb2a45514f44a3b1dfd8ef9bd36530
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/pydoc.py:131:14"
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

## usage_mismatch:3a80db5d437809e59483b18ba66cb212:match

```yaml
regex_id: 3a80db5d437809e59483b18ba66cb212
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:461:25"
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

## usage_mismatch:3bc5264000fa70995cab3b42d908530b:search

```yaml
regex_id: 3bc5264000fa70995cab3b42d908530b
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/http/cookiejar.py:608:14"
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

## usage_mismatch:3d3eb57345c25ac4cff98f8fe0e58a8e:search

```yaml
regex_id: 3d3eb57345c25ac4cff98f8fe0e58a8e
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/doctest.py:1407:30"
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

## usage_mismatch:3d790ec2c06dd68d880182495bc7d724:search

```yaml
regex_id: 3d790ec2c06dd68d880182495bc7d724
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/urllib/parse.py:960:20"
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

## usage_mismatch:3f2a80c04a488e55c7c98002fb39322d:search

```yaml
regex_id: 3f2a80c04a488e55c7c98002fb39322d
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_smtplib.py:493:17"
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

## usage_mismatch:3f6a5b83ebd9644bde47050f800f78fe:search

```yaml
regex_id: 3f6a5b83ebd9644bde47050f800f78fe
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/logging/config.py:353:19"
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

## usage_mismatch:400ab327ca69e7a39672c8d85938c04d:search

```yaml
regex_id: 400ab327ca69e7a39672c8d85938c04d
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/http/cookiejar.py:201:17"
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

## usage_mismatch:400cf1a066364c49912e45dcb19b457d:match

```yaml
regex_id: 400cf1a066364c49912e45dcb19b457d
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/lib2to3/pgen2/conv.py:71:17"
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

## usage_mismatch:449f7fe4df44536b89c1cef697fe8381:match

```yaml
regex_id: 449f7fe4df44536b89c1cef697fe8381
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:508:26"
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

## usage_mismatch:451bfa77ac8a2b5d3fefcb6346881f1e:match

```yaml
regex_id: 451bfa77ac8a2b5d3fefcb6346881f1e
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:541:25"
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

## usage_mismatch:457e556eb9258cfc67d0824b444359f5:search

```yaml
regex_id: 457e556eb9258cfc67d0824b444359f5
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/idlelib/MultiCall.py:265:13"
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

## usage_mismatch:473c25fc0359b53ac30a58e61ab423e9:match

```yaml
regex_id: 473c25fc0359b53ac30a58e61ab423e9
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Tools/demo/ss1.py:436:12"
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

## usage_mismatch:4837cec8a9ec676aa8beb2e32496e518:search

```yaml
regex_id: 4837cec8a9ec676aa8beb2e32496e518
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Tools/scripts/mailerdaemon.py:92:4"
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

## usage_mismatch:4dd347c5df10650c3d23116d5d30a277:search

```yaml
regex_id: 4dd347c5df10650c3d23116d5d30a277
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/_pydecimal.py:6156:13"
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

## usage_mismatch:4f408b5880ddd35ba31b28d37c07cdd4:search

```yaml
regex_id: 4f408b5880ddd35ba31b28d37c07cdd4
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/urllib/request.py:307:15"
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

## usage_mismatch:56c7245104114ac5a9a9ce225f8d84ff:match

```yaml
regex_id: 56c7245104114ac5a9a9ce225f8d84ff
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:510:25"
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

## usage_mismatch:57569d3ede30e6a265202e4acdd6357a:search

```yaml
regex_id: 57569d3ede30e6a265202e4acdd6357a
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/http/cookiejar.py:523:10"
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

## usage_mismatch:576dad3f1867c53d0b53755e8dcdb86b:search

```yaml
regex_id: 576dad3f1867c53d0b53755e8dcdb86b
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/tokenize.py:37:12"
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

## usage_mismatch:5a6bc90acac3a8415a2f4c79d190ba27:match

```yaml
regex_id: 5a6bc90acac3a8415a2f4c79d190ba27
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:540:25"
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

## usage_mismatch:5b8427ec7b81080d9d296d2552cdedb5:search

```yaml
regex_id: 5b8427ec7b81080d9d296d2552cdedb5
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:599:25"
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

## usage_mismatch:5be01957d07f36a17cf4ae82dfd7152e:match

```yaml
regex_id: 5be01957d07f36a17cf4ae82dfd7152e
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:467:25"
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

## usage_mismatch:5cd6b6dab4549cde8c5e336220ac5745:search

```yaml
regex_id: 5cd6b6dab4549cde8c5e336220ac5745
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/idlelib/PyShell.py:1208:35"
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

## usage_mismatch:5dd62b7a9adc3115996f8d620be63671:search

```yaml
regex_id: 5dd62b7a9adc3115996f8d620be63671
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Tools/scripts/texi2html.py:1598:19"
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

## usage_mismatch:603a6a9f4232d31ec4fca25de20cea99:search

```yaml
regex_id: 603a6a9f4232d31ec4fca25de20cea99
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_smtplib.py:464:17"
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

## usage_mismatch:6a9080e4b54cde08b96c0e88072f786d:match

```yaml
regex_id: 6a9080e4b54cde08b96c0e88072f786d
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:559:24"
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

## usage_mismatch:6d8edaa5f204d032920e23e3093cc382:match

```yaml
regex_id: 6d8edaa5f204d032920e23e3093cc382
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:555:24"
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

## usage_mismatch:6f00bf7fd9c007c72b6d032cba7e3ec4:search

```yaml
regex_id: 6f00bf7fd9c007c72b6d032cba7e3ec4
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/configparser.py:1291:16"
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

## usage_mismatch:74c2b191c92e6849999c73959d611be6:search

```yaml
regex_id: 74c2b191c92e6849999c73959d611be6
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_smtplib.py:138:19"
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

## usage_mismatch:75adf7cf39ea4daa8b58c38d8cb47b4a:search

```yaml
regex_id: 75adf7cf39ea4daa8b58c38d8cb47b4a
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/distutils/versionpredicate.py:156:24"
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

## usage_mismatch:7615c7c87d0add9ed9fdf888661121b0:search

```yaml
regex_id: 7615c7c87d0add9ed9fdf888661121b0
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/idlelib/PyShell.py:1209:35"
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

## usage_mismatch:76a5d90f5389de322d4fdd7ea86bc6f8:search

```yaml
regex_id: 76a5d90f5389de322d4fdd7ea86bc6f8
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/nntplib.py:844:19"
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

## usage_mismatch:77a3533d71312e925f42693ff0d4b7ae:search

```yaml
regex_id: 77a3533d71312e925f42693ff0d4b7ae
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:1275:18"
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

## usage_mismatch:77bed13a11256a9748f968d1ad86515e:search

```yaml
regex_id: 77bed13a11256a9748f968d1ad86515e
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/textwrap.py:412:22"
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

## usage_mismatch:791482385338b8c14f98e4a0e11e7f43:match

```yaml
regex_id: 791482385338b8c14f98e4a0e11e7f43
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:556:24"
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

## usage_mismatch:793a1d4106f019b7f8b0df5e0b684d4a:match

```yaml
regex_id: 793a1d4106f019b7f8b0df5e0b684d4a
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/warnings.py:224:7"
```

### Pattern

`^[a-zA-Z0-9_]+$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:79697e187e134964a51a4a4f479715d2:email

```yaml
regex_id: 79697e187e134964a51a4a4f479715d2
schema_version: "1"
kind: intent_mismatch
corpus: gilectomy
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/email/generator.py:21:7"
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

## usage_mismatch:79697e187e134964a51a4a4f479715d2:search

```yaml
regex_id: 79697e187e134964a51a4a4f479715d2
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/email/generator.py:21:7"
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

## usage_mismatch:79b51582ef0e340e915b942953effa0b:search

```yaml
regex_id: 79b51582ef0e340e915b942953effa0b
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Tools/scripts/texi2html.py:74:9"
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

## usage_mismatch:7b46c67c0f0745247a9d79512bdc4e6f:search

```yaml
regex_id: 7b46c67c0f0745247a9d79512bdc4e6f
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Tools/scripts/h2py.py:32:12"
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

## usage_mismatch:7b6b310cdf4bfb800a8031e240173d51:search

```yaml
regex_id: 7b6b310cdf4bfb800a8031e240173d51
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/logging/config.py:355:20"
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

## usage_mismatch:80b15a0d02be715c7cca65f2c69bfed2:search

```yaml
regex_id: 80b15a0d02be715c7cca65f2c69bfed2
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Tools/scripts/h2py.py:26:11"
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

## usage_mismatch:81bdc1ceafe07e1a133fad683a84434b:search

```yaml
regex_id: 81bdc1ceafe07e1a133fad683a84434b
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/http/cookiejar.py:333:25"
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

## usage_mismatch:835ba2f723842909821b2cb712e8c0b6:match

```yaml
regex_id: 835ba2f723842909821b2cb712e8c0b6
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:547:26"
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

## intent_mismatch:83fca23af1a84cc35c3aeb45f159e8c4:email

```yaml
regex_id: 83fca23af1a84cc35c3aeb45f159e8c4
schema_version: "1"
kind: intent_mismatch
corpus: gilectomy
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/email/utils.py:118:7"
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
{"admitted_char": "' '", "keyword": "email", "reason": "name/comment claims validation but pattern admits excluded char"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8965171394b04f67231ce849eae29f50:search

```yaml
regex_id: 8965171394b04f67231ce849eae29f50
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:1433:12"
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

## intent_mismatch:8975bf3b453e7d08d6df5750cda3a983:email

```yaml
regex_id: 8975bf3b453e7d08d6df5750cda3a983
schema_version: "1"
kind: intent_mismatch
corpus: gilectomy
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/email/feedparser.py:37:11"
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

## usage_mismatch:8975bf3b453e7d08d6df5750cda3a983:search

```yaml
regex_id: 8975bf3b453e7d08d6df5750cda3a983
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/email/feedparser.py:37:11"
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

## usage_mismatch:8a25ce152a9447309046d4ef42adb3b4:search

```yaml
regex_id: 8a25ce152a9447309046d4ef42adb3b4
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/http/cookiejar.py:130:14"
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

## usage_mismatch:9524784fcf977fb44a595dd55ccfd835:search

```yaml
regex_id: 9524784fcf977fb44a595dd55ccfd835
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/idlelib/IOBinding.py:66:11"
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

## usage_mismatch:95daf78f9132da0bc426491f25c47bb0:search

```yaml
regex_id: 95daf78f9132da0bc426491f25c47bb0
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_gdb.py:40:12"
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

## usage_mismatch:988274f115688f09c0f104d38f79bc47:match

```yaml
regex_id: 988274f115688f09c0f104d38f79bc47
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:463:25"
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

## usage_mismatch:9c8bcf404ea95d13c9a77eecc2e7ff05:search

```yaml
regex_id: 9c8bcf404ea95d13c9a77eecc2e7ff05
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Tools/scripts/texi2html.py:73:9"
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

## usage_mismatch:9cdb16788310d8a5b84df33936d35221:match

```yaml
regex_id: 9cdb16788310d8a5b84df33936d35221
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:506:25"
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

## usage_mismatch:9dc20b23bd31868ab438155c0ed39cf8:match

```yaml
regex_id: 9dc20b23bd31868ab438155c0ed39cf8
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:512:25"
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

## usage_mismatch:9e883f3e2cbc0473df9bd02452e9b6f8:search

```yaml
regex_id: 9e883f3e2cbc0473df9bd02452e9b6f8
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/email/utils.py:260:23"
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

## usage_mismatch:a012feb9c41d629d162d4e3e8b72a33e:search

```yaml
regex_id: a012feb9c41d629d162d4e3e8b72a33e
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/logging/config.py:271:13"
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

## usage_mismatch:a07ec96ff2c48822cf893db66d3d556c:search

```yaml
regex_id: a07ec96ff2c48822cf893db66d3d556c
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_smtplib.py:411:17"
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

## usage_mismatch:a36a6f5c7800c824d19a1269fdf228fe:match

```yaml
regex_id: a36a6f5c7800c824d19a1269fdf228fe
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:466:26"
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

## usage_mismatch:a41bc169c9a3e8b374bf3ef12de74b36:search

```yaml
regex_id: a41bc169c9a3e8b374bf3ef12de74b36
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/http/cookiejar.py:204:13"
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

## usage_mismatch:a542452d9c0f1a146d38d6cb72fc336d:search

```yaml
regex_id: a542452d9c0f1a146d38d6cb72fc336d
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/http/cookiejar.py:334:25"
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

## usage_mismatch:a868a8908428733b9f9706f9652629eb:search

```yaml
regex_id: a868a8908428733b9f9706f9652629eb
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/http/cookiejar.py:206:21"
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

## usage_mismatch:ab10599c6039939ebb173020bd8d852e:search

```yaml
regex_id: ab10599c6039939ebb173020bd8d852e
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/distutils/versionpredicate.py:12:11"
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

## usage_mismatch:acbb87b40d9b81da1f463d8e1b874a5b:search

```yaml
regex_id: acbb87b40d9b81da1f463d8e1b874a5b
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:601:26"
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

## usage_mismatch:af3dfd3f6bac2cc37f5dcd1242296e8a:match

```yaml
regex_id: af3dfd3f6bac2cc37f5dcd1242296e8a
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:558:24"
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

## usage_mismatch:b5d92f6ccbf388c0c3f41313faad33b5:search

```yaml
regex_id: b5d92f6ccbf388c0c3f41313faad33b5
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Tools/scripts/mailerdaemon.py:96:20"
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

## usage_mismatch:b7e49135dcaf4c06e4923d5afeda924f:match

```yaml
regex_id: b7e49135dcaf4c06e4923d5afeda924f
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:465:26"
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

## usage_mismatch:ba94eee549ef84d13567ba26436c43ab:match

```yaml
regex_id: ba94eee549ef84d13567ba26436c43ab
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:554:24"
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

## usage_mismatch:bc5efd6e5525e546bf5d4df6301393d0:match

```yaml
regex_id: bc5efd6e5525e546bf5d4df6301393d0
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:552:24"
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

## usage_mismatch:bd0b9c5aec60a8e31e5aa8271865c5ac:search

```yaml
regex_id: bd0b9c5aec60a8e31e5aa8271865c5ac
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Tools/scripts/mailerdaemon.py:168:10"
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

## usage_mismatch:be12c8c4642369622738d4d43865d84a:search

```yaml
regex_id: be12c8c4642369622738d4d43865d84a
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/http/cookiejar.py:440:23"
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

## usage_mismatch:c11ac2b8997e243819b2becdc55f8ac3:match

```yaml
regex_id: c11ac2b8997e243819b2becdc55f8ac3
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:538:25"
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

## usage_mismatch:c4732c0db118e56a7c6321887abcadd4:match

```yaml
regex_id: c4732c0db118e56a7c6321887abcadd4
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:542:25"
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

## usage_mismatch:c50aca7c13a44877f7399a4395e4f187:match

```yaml
regex_id: c50aca7c13a44877f7399a4395e4f187
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:563:24"
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

## usage_mismatch:c652224f3d66106cb41af4a9434378b9:match

```yaml
regex_id: c652224f3d66106cb41af4a9434378b9
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:548:26"
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

## usage_mismatch:c686f0866631b3c5529df646cd8d3e04:search

```yaml
regex_id: c686f0866631b3c5529df646cd8d3e04
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Tools/scripts/mailerdaemon.py:94:4"
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

## usage_mismatch:c700719417aac923161fb42194c1713b:search

```yaml
regex_id: c700719417aac923161fb42194c1713b
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_smtplib.py:527:17"
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

## usage_mismatch:c949291edb9c26d925b0e68488ae90e9:match

```yaml
regex_id: c949291edb9c26d925b0e68488ae90e9
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:545:25"
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

## usage_mismatch:cc5d37b9c82d451ddc919040f57be0ae:search

```yaml
regex_id: cc5d37b9c82d451ddc919040f57be0ae
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:924:28"
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

## usage_mismatch:cc6cc566fe6fceb70ccf952abde8ce32:match

```yaml
regex_id: cc6cc566fe6fceb70ccf952abde8ce32
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:543:25"
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

## usage_mismatch:cdb25277ca028da1190a4ecf14d70aae:search

```yaml
regex_id: cdb25277ca028da1190a4ecf14d70aae
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/idlelib/IOBinding.py:65:12"
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

## usage_mismatch:ce6dc01997e58779d92cbae7efde1938:search

```yaml
regex_id: ce6dc01997e58779d92cbae7efde1938
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/http/cookiejar.py:1237:15"
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

## usage_mismatch:d0eca4f984a5c60054e99910c6cadebb:match

```yaml
regex_id: d0eca4f984a5c60054e99910c6cadebb
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/idlelib/FormatParagraph.py:175:11"
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

## usage_mismatch:d408313219c6d5c073938c9c61e0f8bb:match

```yaml
regex_id: d408313219c6d5c073938c9c61e0f8bb
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:471:25"
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

## usage_mismatch:df19945efb8c271f581096e519133840:match

```yaml
regex_id: df19945efb8c271f581096e519133840
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:550:26"
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

## usage_mismatch:dffa32962cdf54dfcb581a897910b54b:search

```yaml
regex_id: dffa32962cdf54dfcb581a897910b54b
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:456:12"
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

## usage_mismatch:e0087dfbbf5104304b99fcef92d4df8a:search

```yaml
regex_id: e0087dfbbf5104304b99fcef92d4df8a
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/unittest/test/test_case.py:1332:16"
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

## usage_mismatch:e423ff2d142cba2a6f5076867d6f2995:match

```yaml
regex_id: e423ff2d142cba2a6f5076867d6f2995
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:509:26"
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

## usage_mismatch:e860158b385471403bad8e696e962c1d:match

```yaml
regex_id: e860158b385471403bad8e696e962c1d
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:1225:29"
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

## usage_mismatch:e9cf6d796c58cf257b4a0d00e697eb39:search

```yaml
regex_id: e9cf6d796c58cf257b4a0d00e697eb39
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/doctest.py:619:27"
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

## intent_mismatch:eb607eebb81ba1f17c1b67d0cbd3d3cd:email

```yaml
regex_id: eb607eebb81ba1f17c1b67d0cbd3d3cd
schema_version: "1"
kind: intent_mismatch
corpus: gilectomy
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_email/test_email.py:5307:17"
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

## usage_mismatch:eb607eebb81ba1f17c1b67d0cbd3d3cd:search

```yaml
regex_id: eb607eebb81ba1f17c1b67d0cbd3d3cd
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_email/test_email.py:5307:17"
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

## usage_mismatch:ebfb0aed20e1c6f215e24065e5488c12:match

```yaml
regex_id: ebfb0aed20e1c6f215e24065e5488c12
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:562:26"
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

## usage_mismatch:eda54d099aa330c1754113af3624c88a:search

```yaml
regex_id: eda54d099aa330c1754113af3624c88a
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_smtplib.py:438:17"
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

## usage_mismatch:f54b28b1bcaa23589349dd477608d48b:search

```yaml
regex_id: f54b28b1bcaa23589349dd477608d48b
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/http/cookiejar.py:279:14"
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

## usage_mismatch:f8baddd4a0813929ce874c4544bad406:match

```yaml
regex_id: f8baddd4a0813929ce874c4544bad406
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/test/test_re.py:533:26"
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

## intent_mismatch:fa07fd9a45f1fe8a0ea543db8a3a254b:email

```yaml
regex_id: fa07fd9a45f1fe8a0ea543db8a3a254b
schema_version: "1"
kind: intent_mismatch
corpus: gilectomy
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/email/header.py:35:7"
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
{"admitted_char": "' '", "keyword": "email", "reason": "name/comment claims validation but pattern admits excluded char"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fb1d22ceb7cedb2a6dc6daa0aae528f4:search

```yaml
regex_id: fb1d22ceb7cedb2a6dc6daa0aae528f4
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/nntplib.py:787:14"
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

## usage_mismatch:fcb61e7eb3e5b9db4f244aa9249a429a:search

```yaml
regex_id: fcb61e7eb3e5b9db4f244aa9249a429a
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/_pydecimal.py:6157:14"
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

## usage_mismatch:fdabed1e3961de694d678cc0d3df4470:search

```yaml
regex_id: fdabed1e3961de694d678cc0d3df4470
schema_version: "1"
kind: usage_mismatch
corpus: gilectomy
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/gilectomy/rules/Lib/doctest.py:768:17"
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

## property:inventory:rc-shape1-injection-alphabet:rc-shape1-injection-alphabet

```yaml
regex_id: "inventory:rc-shape1-injection-alphabet"
schema_version: "1"
kind: property
corpus: gilectomy
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
corpus: gilectomy
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
corpus: gilectomy
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
corpus: gilectomy
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

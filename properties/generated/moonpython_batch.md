---
schema_version: "1"
corpus: moonpython
findings: 129
---

# moonpython batch findings

## usage_mismatch:0264caf9a9a2abde37f1af7dc26ba4f0:match

```yaml
regex_id: 0264caf9a9a2abde37f1af7dc26ba4f0
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:2529:26"
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

## usage_mismatch:05e55a4b213e662eaabf848fda5b7c65:match

```yaml
regex_id: 05e55a4b213e662eaabf848fda5b7c65
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:2526:24"
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

## usage_mismatch:065c63f3fcf9624652cc668798a92a41:search

```yaml
regex_id: 065c63f3fcf9624652cc668798a92a41
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_smtplib.py:608:16"
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

## usage_mismatch:0b8049339409b6a5ad4ee2437dc401a0:search

```yaml
regex_id: 0b8049339409b6a5ad4ee2437dc401a0
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/scripts/run_libtests.py:51:10"
```

### Pattern

`^Ran (\d+) tests? in `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0c344148cc6c6754bd75ee9bc1deef23:search

```yaml
regex_id: 0c344148cc6c6754bd75ee9bc1deef23
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/http/cookiejar.py:344:25"
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

## usage_mismatch:0c735eee73277a1ff36a910c76ed5779:search

```yaml
regex_id: 0c735eee73277a1ff36a910c76ed5779
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/logging/config.py:377:22"
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

## usage_mismatch:0ea6514a6b403197568811f464db1ebe:search

```yaml
regex_id: 0ea6514a6b403197568811f464db1ebe
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/doctest.py:1463:30"
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

## usage_mismatch:111d131fc052c73abfdcde2c19f6cca2:match

```yaml
regex_id: 111d131fc052c73abfdcde2c19f6cca2
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:2522:26"
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

## usage_mismatch:11368f329cb97db1ff238f7320e472b8:search

```yaml
regex_id: 11368f329cb97db1ff238f7320e472b8
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_smtplib.py:490:17"
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

## usage_mismatch:1183c19fd3df8cd514aaae29305ab904:search

```yaml
regex_id: 1183c19fd3df8cd514aaae29305ab904
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/tokenize.py:39:12"
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

## usage_mismatch:13d1e958f5e8db0fafcd2ca22e1fe4b8:match

```yaml
regex_id: 13d1e958f5e8db0fafcd2ca22e1fe4b8
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/msilib/__init__.py:184:11"
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

## usage_mismatch:1696af6c53efdec6083b99c73e65acce:search

```yaml
regex_id: 1696af6c53efdec6083b99c73e65acce
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:1827:18"
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

## usage_mismatch:179c1b8843bff301f9468c7ab86401fa:search

```yaml
regex_id: 179c1b8843bff301f9468c7ab86401fa
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:2018:12"
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

## usage_mismatch:18f070d0ae799f3531e09bf3a3a465bd:match

```yaml
regex_id: 18f070d0ae799f3531e09bf3a3a465bd
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:757:24"
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

## usage_mismatch:199952f693538728a1641253f5364af2:match

```yaml
regex_id: 199952f693538728a1641253f5364af2
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:746:26"
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

## usage_mismatch:1b3cf4916d06eeff4fb685aa4545d071:search

```yaml
regex_id: 1b3cf4916d06eeff4fb685aa4545d071
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:1822:18"
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

## usage_mismatch:1b45ddc939ac85ebbbfd261511b3ad4d:match

```yaml
regex_id: 1b45ddc939ac85ebbbfd261511b3ad4d
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:758:24"
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

## usage_mismatch:1ed1763f821b4e04b4e67eb5ba3b7663:search

```yaml
regex_id: 1ed1763f821b4e04b4e67eb5ba3b7663
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/http/cookiejar.py:1259:15"
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

## usage_mismatch:20ac92ff3917722ca2cf86f192c58722:search

```yaml
regex_id: 20ac92ff3917722ca2cf86f192c58722
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/logging/config.py:380:18"
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

## usage_mismatch:22c6e45ea327b8056c63dcd8de2baf01:match

```yaml
regex_id: 22c6e45ea327b8056c63dcd8de2baf01
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:738:25"
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

## usage_mismatch:24572e9d497a2c640082f31bd001ee64:search

```yaml
regex_id: 24572e9d497a2c640082f31bd001ee64
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/_pydecimal.py:6064:13"
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

## usage_mismatch:25e3b1bfcdfcde5a89d0444e0e235a5c:search

```yaml
regex_id: 25e3b1bfcdfcde5a89d0444e0e235a5c
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/doctest.py:752:27"
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

## usage_mismatch:277a6e60ec9f24c69a65f5834a8ca62d:search

```yaml
regex_id: 277a6e60ec9f24c69a65f5834a8ca62d
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/http/cookiejar.py:619:14"
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

## usage_mismatch:28ccd1ca2544155ee334eb178f2688a3:match

```yaml
regex_id: 28ccd1ca2544155ee334eb178f2688a3
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:707:26"
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

## usage_mismatch:2bfa88d7368ad4e427c7625ebdd1b395:match

```yaml
regex_id: 2bfa88d7368ad4e427c7625ebdd1b395
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:754:24"
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

## usage_mismatch:2c61342a05476300145b3bc032e4dfce:match

```yaml
regex_id: 2c61342a05476300145b3bc032e4dfce
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:2527:24"
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

## usage_mismatch:2c72e7807ac0eb63acae15bbf411ecc7:search

```yaml
regex_id: 2c72e7807ac0eb63acae15bbf411ecc7
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_regrtest.py:1324:16"
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

## usage_mismatch:2eaa48cc5dc61ca716468d312b6db01e:match

```yaml
regex_id: 2eaa48cc5dc61ca716468d312b6db01e
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:732:26"
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

## usage_mismatch:2f67d3086a88d2ba02eb6af843c6de83:match

```yaml
regex_id: 2f67d3086a88d2ba02eb6af843c6de83
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:710:25"
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

## usage_mismatch:317345c13c37302287aca397fe268a60:match

```yaml
regex_id: 317345c13c37302287aca397fe268a60
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:2525:24"
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

## intent_mismatch:3186994b7a54bdb8fe1ad6c9a7c5b4c5:email

```yaml
regex_id: 3186994b7a54bdb8fe1ad6c9a7c5b4c5
schema_version: "1"
kind: intent_mismatch
corpus: moonpython
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/email/feedparser.py:37:11"
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

## usage_mismatch:3186994b7a54bdb8fe1ad6c9a7c5b4c5:search

```yaml
regex_id: 3186994b7a54bdb8fe1ad6c9a7c5b4c5
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/email/feedparser.py:37:11"
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

## usage_mismatch:32a88f76e71a07a96af013f48baaeaec:match

```yaml
regex_id: 32a88f76e71a07a96af013f48baaeaec
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:756:24"
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

## usage_mismatch:372cac047dc386b7c6a404730caac71e:search

```yaml
regex_id: 372cac047dc386b7c6a404730caac71e
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_smtplib.py:543:17"
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

## intent_mismatch:373ac7a59cc2e170f97d2e834e6f1881:email

```yaml
regex_id: 373ac7a59cc2e170f97d2e834e6f1881
schema_version: "1"
kind: intent_mismatch
corpus: moonpython
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/email/generator.py:23:7"
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

## usage_mismatch:373ac7a59cc2e170f97d2e834e6f1881:search

```yaml
regex_id: 373ac7a59cc2e170f97d2e834e6f1881
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/email/generator.py:23:7"
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

## usage_mismatch:3c1180c0130722f7fbaa97e6ccc2a365:search

```yaml
regex_id: 3c1180c0130722f7fbaa97e6ccc2a365
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_smtplib.py:634:17"
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

## usage_mismatch:3c873b34d392c25cca5bbfa2e358ab5e:search

```yaml
regex_id: 3c873b34d392c25cca5bbfa2e358ab5e
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/platform.py:1320:22"
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

## usage_mismatch:4149360222513d0b7bd0b369a31e2cd1:match

```yaml
regex_id: 4149360222513d0b7bd0b369a31e2cd1
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:2515:26"
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

## usage_mismatch:48a94b70b53bc3df55800988b63a9e2c:search

```yaml
regex_id: 48a94b70b53bc3df55800988b63a9e2c
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_smtplib.py:157:19"
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

## usage_mismatch:48e71ba0e037965b5f3f5c58e10293d2:match

```yaml
regex_id: 48e71ba0e037965b5f3f5c58e10293d2
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:2530:24"
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

## usage_mismatch:4a01f6b243dde68f708da8e6fad53c33:search

```yaml
regex_id: 4a01f6b243dde68f708da8e6fad53c33
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/logging/__init__.py:475:17"
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

## intent_mismatch:4a18ddc259bfeef1ca5a2881ad9fd8e1:email

```yaml
regex_id: 4a18ddc259bfeef1ca5a2881ad9fd8e1
schema_version: "1"
kind: intent_mismatch
corpus: moonpython
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/email/header.py:35:7"
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

## usage_mismatch:4b6713f885f7c104c2525e41b24debad:search

```yaml
regex_id: 4b6713f885f7c104c2525e41b24debad
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:1436:28"
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

## usage_mismatch:4cf240159d1c48f21e3bce9bea352142:match

```yaml
regex_id: 4cf240159d1c48f21e3bce9bea352142
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:706:26"
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

## usage_mismatch:4e63b29714ea116d7745bb1f13d7b376:match

```yaml
regex_id: 4e63b29714ea116d7745bb1f13d7b376
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:635:25"
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

## usage_mismatch:4ecbd18e8d58a93b5ab9130ed9082e09:search

```yaml
regex_id: 4ecbd18e8d58a93b5ab9130ed9082e09
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/doctest.py:634:27"
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

## usage_mismatch:5a57b0df8b9ce7144055e4ccb8f49d17:search

```yaml
regex_id: 5a57b0df8b9ce7144055e4ccb8f49d17
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_unittest/test_case.py:1455:16"
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

## usage_mismatch:5c38bfc98e25868cec84c31471c3f3d4:match

```yaml
regex_id: 5c38bfc98e25868cec84c31471c3f3d4
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:734:26"
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

## usage_mismatch:5cc0e2968313fef84617bdab834fa5a6:match

```yaml
regex_id: 5cc0e2968313fef84617bdab834fa5a6
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:704:25"
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

## usage_mismatch:5deeb53484742ac385a8479a27c0b8a5:match

```yaml
regex_id: 5deeb53484742ac385a8479a27c0b8a5
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:747:26"
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

## usage_mismatch:649fa0d4ff218b99453019b0b49227c1:match

```yaml
regex_id: 649fa0d4ff218b99453019b0b49227c1
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:2518:25"
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

## intent_mismatch:681fb5c435f4774bed8f251c24a662b3:email

```yaml
regex_id: 681fb5c435f4774bed8f251c24a662b3
schema_version: "1"
kind: intent_mismatch
corpus: moonpython
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/email/_header_value_parser.py:110:18"
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

## usage_mismatch:68761101c8562b3527c9167a7dd54015:search

```yaml
regex_id: 68761101c8562b3527c9167a7dd54015
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_smtplib.py:573:17"
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

## usage_mismatch:6b6f5349a0105fdc95b7ed1a832325c5:search

```yaml
regex_id: 6b6f5349a0105fdc95b7ed1a832325c5
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/http/cookiejar.py:345:25"
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

## usage_mismatch:6ba9d2ee4788a9607c5239484d1a39a9:match

```yaml
regex_id: 6ba9d2ee4788a9607c5239484d1a39a9
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:1748:30"
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

## usage_mismatch:6e996f0638e98110f448ed640ea768f0:match

```yaml
regex_id: 6e996f0638e98110f448ed640ea768f0
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:751:24"
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

## usage_mismatch:751948e36dfbf823aeb94ce041343401:search

```yaml
regex_id: 751948e36dfbf823aeb94ce041343401
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:799:26"
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

## usage_mismatch:75c914ac575336171ceadc7ce8afbe50:search

```yaml
regex_id: 75c914ac575336171ceadc7ce8afbe50
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/pydoc.py:242:14"
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

## usage_mismatch:7742fddf3e9f9a8f1f9ce7d0cdbb7f6c:search

```yaml
regex_id: 7742fddf3e9f9a8f1f9ce7d0cdbb7f6c
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/http/cookiejar.py:288:14"
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

## usage_mismatch:7eb99188e96081a906372f0ba86bc915:match

```yaml
regex_id: 7eb99188e96081a906372f0ba86bc915
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:737:25"
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

## usage_mismatch:80d4de831b5c84e6e6a3b3947b8d7f3e:match

```yaml
regex_id: 80d4de831b5c84e6e6a3b3947b8d7f3e
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:639:25"
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

## usage_mismatch:81919673dfeb543d1c9a93fdd4d57ea3:match

```yaml
regex_id: 81919673dfeb543d1c9a93fdd4d57ea3
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:750:24"
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

## usage_mismatch:82176f6fb830a737c489bdcab1f0f8b2:match

```yaml
regex_id: 82176f6fb830a737c489bdcab1f0f8b2
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:733:26"
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

## usage_mismatch:83680d2d0b2dfe46e92f732d1188bd2c:match

```yaml
regex_id: 83680d2d0b2dfe46e92f732d1188bd2c
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:2516:26"
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

## usage_mismatch:837f2d4ac9e55da30b64134b82f9232e:match

```yaml
regex_id: 837f2d4ac9e55da30b64134b82f9232e
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:1739:29"
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

## usage_mismatch:8406664d9387af7f081f3790ae3a56f5:search

```yaml
regex_id: 8406664d9387af7f081f3790ae3a56f5
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/logging/config.py:297:13"
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

## usage_mismatch:8447d946965f3ec93aa06b11e0364891:search

```yaml
regex_id: 8447d946965f3ec93aa06b11e0364891
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/http/cookiejar.py:211:21"
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

## usage_mismatch:8503c839c43f6d8c67dcf6a48e63b12b:search

```yaml
regex_id: 8503c839c43f6d8c67dcf6a48e63b12b
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/email/header.py:48:7"
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

## usage_mismatch:867a320ae256f0493dc235d4a70757e9:match

```yaml
regex_id: 867a320ae256f0493dc235d4a70757e9
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:629:25"
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

## usage_mismatch:8970d71f0ea79b68c64c4a42627f691d:match

```yaml
regex_id: 8970d71f0ea79b68c64c4a42627f691d
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:743:25"
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

## usage_mismatch:8cbbd713075ca7531c0e2f59bba6ef4e:match

```yaml
regex_id: 8cbbd713075ca7531c0e2f59bba6ef4e
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:634:26"
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

## usage_mismatch:8def58e27638fc9034c8c5e82f5f6220:match

```yaml
regex_id: 8def58e27638fc9034c8c5e82f5f6220
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:753:24"
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

## usage_mismatch:8e73eba921d8f001981a316e4eda7e9d:search

```yaml
regex_id: 8e73eba921d8f001981a316e4eda7e9d
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/idlelib/pyshell.py:1335:35"
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

## usage_mismatch:9471376a93e539a33d335079fec80c14:match

```yaml
regex_id: 9471376a93e539a33d335079fec80c14
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:2520:25"
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

## usage_mismatch:955e66230ab5b87fe234d1f75a87c9f1:match

```yaml
regex_id: 955e66230ab5b87fe234d1f75a87c9f1
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:708:25"
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

## usage_mismatch:9aa7ab0e3f504ad432be8948ece31ccf:search

```yaml
regex_id: 9aa7ab0e3f504ad432be8948ece31ccf
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_smtplib.py:671:17"
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

## usage_mismatch:9f7fc7c438f93152dba5bcce4c2f423e:search

```yaml
regex_id: 9f7fc7c438f93152dba5bcce4c2f423e
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/logging/config.py:381:20"
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

## usage_mismatch:a069b9830cde4ebdc0b30a20e458fc6a:match

```yaml
regex_id: a069b9830cde4ebdc0b30a20e458fc6a
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:641:25"
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

## usage_mismatch:a11e70df113a3951cc9454810b344031:search

```yaml
regex_id: a11e70df113a3951cc9454810b344031
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/email/utils.py:390:23"
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

## usage_mismatch:a1909448a4d1eefdb4a74ae4e17300a0:search

```yaml
regex_id: a1909448a4d1eefdb4a74ae4e17300a0
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_unittest/test_case.py:1393:46"
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

## usage_mismatch:a3146bb7d1b3f652f69caf00b820d009:match

```yaml
regex_id: a3146bb7d1b3f652f69caf00b820d009
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/idlelib/format.py:181:11"
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

## usage_mismatch:a659a92037b2567f546d00b0b375e20e:match

```yaml
regex_id: a659a92037b2567f546d00b0b375e20e
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:736:25"
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

## usage_mismatch:adb56192201ad79cb145d01b25858b82:search

```yaml
regex_id: adb56192201ad79cb145d01b25858b82
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/_pydecimal.py:6065:14"
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

## usage_mismatch:b0c77d1729f7a511f0421f4644dd9698:match

```yaml
regex_id: b0c77d1729f7a511f0421f4644dd9698
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:755:24"
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

## usage_mismatch:b5f93e356160a44f549994595a003433:search

```yaml
regex_id: b5f93e356160a44f549994595a003433
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/http/cookiejar.py:135:14"
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

## usage_mismatch:b6c993a28570ba62eb70940605690033:match

```yaml
regex_id: b6c993a28570ba62eb70940605690033
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:752:24"
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

## usage_mismatch:b8939d2de475134d8b508756187673c9:search

```yaml
regex_id: b8939d2de475134d8b508756187673c9
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:624:12"
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

## usage_mismatch:ba3896b0d9b073bc1bb341f2fa7d9a19:match

```yaml
regex_id: ba3896b0d9b073bc1bb341f2fa7d9a19
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:748:26"
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

## usage_mismatch:c1ad4194a4730eeb62b273fcf31ee7e2:search

```yaml
regex_id: c1ad4194a4730eeb62b273fcf31ee7e2
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/http/cookiejar.py:209:13"
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

## usage_mismatch:c2aab7bb17af525fdbb315d627d68e4f:search

```yaml
regex_id: c2aab7bb17af525fdbb315d627d68e4f
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_smtplib.py:602:17"
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

## usage_mismatch:c5609b29d36dbc339ec8a2104d10ea35:search

```yaml
regex_id: c5609b29d36dbc339ec8a2104d10ea35
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_smtplib.py:147:19"
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

## usage_mismatch:c6c9a2a8567a884db59de2bea18e9c31:match

```yaml
regex_id: c6c9a2a8567a884db59de2bea18e9c31
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:631:25"
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

## usage_mismatch:c936e7406ac7d386078baa24f0ad5952:search

```yaml
regex_id: c936e7406ac7d386078baa24f0ad5952
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:798:25"
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

## usage_mismatch:cc12a23258783e689940a740c47927fa:search

```yaml
regex_id: cc12a23258783e689940a740c47927fa
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/logging/config.py:379:19"
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

## usage_mismatch:ccfa4742abd600e7975abb8394e35f3e:search

```yaml
regex_id: ccfa4742abd600e7975abb8394e35f3e
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/doctest.py:783:17"
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

## usage_mismatch:cf5f41a3be624d22b3d00a1cdec4ab15:search

```yaml
regex_id: cf5f41a3be624d22b3d00a1cdec4ab15
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/http/cookiejar.py:451:23"
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

## usage_mismatch:d106d02ac0402daeb6615f00a3948848:search

```yaml
regex_id: d106d02ac0402daeb6615f00a3948848
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/logging/config.py:382:20"
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

## usage_mismatch:d54dc72796ea596950da6678678d55a9:match

```yaml
regex_id: d54dc72796ea596950da6678678d55a9
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:742:25"
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

## usage_mismatch:d76c800aed82c626950860b3ae50efea:search

```yaml
regex_id: d76c800aed82c626950860b3ae50efea
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/lib2to3/pgen2/tokenize.py:227:12"
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

## usage_mismatch:dc9fbf902b4fe8d7fb4256af5c1a9fa3:match

```yaml
regex_id: dc9fbf902b4fe8d7fb4256af5c1a9fa3
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:633:26"
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

## usage_mismatch:dcbfc3182730225d153f4a17d9f7e51f:match

```yaml
regex_id: dcbfc3182730225d153f4a17d9f7e51f
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:745:26"
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

## usage_mismatch:dcd67d4c38b4297d9027fa8f02d1ba26:match

```yaml
regex_id: dcd67d4c38b4297d9027fa8f02d1ba26
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:637:25"
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

## usage_mismatch:dd1cf5a2aea6cc65a69e9b87910a6778:match

```yaml
regex_id: dd1cf5a2aea6cc65a69e9b87910a6778
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:760:26"
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

## intent_mismatch:dd1d175058a160068cee1b5ca1faf3e1:email

```yaml
regex_id: dd1d175058a160068cee1b5ca1faf3e1
schema_version: "1"
kind: intent_mismatch
corpus: moonpython
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_email/test_email.py:5840:17"
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

## usage_mismatch:dd1d175058a160068cee1b5ca1faf3e1:search

```yaml
regex_id: dd1d175058a160068cee1b5ca1faf3e1
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_email/test_email.py:5840:17"
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

## usage_mismatch:df2721d957d203f041674c117f2c1a47:search

```yaml
regex_id: df2721d957d203f041674c117f2c1a47
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/http/cookiejar.py:346:25"
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

## usage_mismatch:e026ea628ec72dd56892f384724ffa89:search

```yaml
regex_id: e026ea628ec72dd56892f384724ffa89
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/http/cookiejar.py:1257:14"
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

## usage_mismatch:e039e0ead608dfcdea7c829e16350694:search

```yaml
regex_id: e039e0ead608dfcdea7c829e16350694
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/idlelib/pyshell.py:1336:35"
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

## usage_mismatch:e0e9e09f80e07291eb8711c1de8879f4:search

```yaml
regex_id: e0e9e09f80e07291eb8711c1de8879f4
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/http/cookiejar.py:534:10"
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

## usage_mismatch:e215a07778c8e167fbec17eb948fb2eb:match

```yaml
regex_id: e215a07778c8e167fbec17eb948fb2eb
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:761:24"
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

## usage_mismatch:e318973b3ffaf2b1510dea45e8c5443e:match

```yaml
regex_id: e318973b3ffaf2b1510dea45e8c5443e
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:741:25"
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

## usage_mismatch:e6bc6d3773d565cef899246e384d135b:match

```yaml
regex_id: e6bc6d3773d565cef899246e384d135b
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:702:25"
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

## usage_mismatch:e76a80a6948225202c3150dad8e6b30a:search

```yaml
regex_id: e76a80a6948225202c3150dad8e6b30a
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/configparser.py:1285:16"
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

## usage_mismatch:edee17ac5dbafd6dde65fdbc47153e9b:match

```yaml
regex_id: edee17ac5dbafd6dde65fdbc47153e9b
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:2519:25"
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

## usage_mismatch:ee67fb7344ee1825d90eaabb19dcca1d:search

```yaml
regex_id: ee67fb7344ee1825d90eaabb19dcca1d
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:797:25"
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

## usage_mismatch:f0e7720d2b41a1c385f2b8b99de08772:match

```yaml
regex_id: f0e7720d2b41a1c385f2b8b99de08772
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:731:26"
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

## usage_mismatch:f1929d33a7cd2b44be8574edd58f4c07:search

```yaml
regex_id: f1929d33a7cd2b44be8574edd58f4c07
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/urllib/request.py:296:15"
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

## usage_mismatch:f1a4e606df3c0addd84de19b821c1e85:match

```yaml
regex_id: f1a4e606df3c0addd84de19b821c1e85
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/lib2to3/pgen2/conv.py:71:17"
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

## usage_mismatch:f87433ff97124cc53d14d375db3e773b:search

```yaml
regex_id: f87433ff97124cc53d14d375db3e773b
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/logging/__init__.py:474:15"
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

## usage_mismatch:f9279b189ef76e1a7b74e7558641b896:match

```yaml
regex_id: f9279b189ef76e1a7b74e7558641b896
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:740:25"
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

## usage_mismatch:f9ad80fe329d72461afd701686e62604:search

```yaml
regex_id: f9ad80fe329d72461afd701686e62604
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/http/cookiejar.py:206:17"
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

## usage_mismatch:fa3233329d5c4dd836b8650e028ad3e6:match

```yaml
regex_id: fa3233329d5c4dd836b8650e028ad3e6
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:2523:26"
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

## usage_mismatch:faf063a719982ba2e47ba5258d3c0e57:match

```yaml
regex_id: faf063a719982ba2e47ba5258d3c0e57
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/test/test_re.py:739:25"
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

## usage_mismatch:ff7d4300f62cd463c043fefb666a285f:search

```yaml
regex_id: ff7d4300f62cd463c043fefb666a285f
schema_version: "1"
kind: usage_mismatch
corpus: moonpython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/moonpython/rules/Lib/textwrap.py:419:22"
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

## property:inventory:rc-shape1-injection-alphabet:rc-shape1-injection-alphabet

```yaml
regex_id: "inventory:rc-shape1-injection-alphabet"
schema_version: "1"
kind: property
corpus: moonpython
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
corpus: moonpython
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
corpus: moonpython
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
corpus: moonpython
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

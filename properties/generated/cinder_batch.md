---
schema_version: "1"
corpus: cinder
findings: 132
---

# cinder batch findings

## usage_mismatch:022619b8d46b2f47f4977f9db84c0aa0:match

```yaml
regex_id: 022619b8d46b2f47f4977f9db84c0aa0
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:768:26"
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

## usage_mismatch:0a16ef7fb36f3472e2fa4c68b488d1b5:match

```yaml
regex_id: 0a16ef7fb36f3472e2fa4c68b488d1b5
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:714:26"
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

## usage_mismatch:0a2b4770c33d38332b6f7e182e6271bf:search

```yaml
regex_id: 0a2b4770c33d38332b6f7e182e6271bf
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:1826:18"
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

## usage_mismatch:0c09e4ed84e2a9d1cf1f126f2fd62c96:match

```yaml
regex_id: 0c09e4ed84e2a9d1cf1f126f2fd62c96
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:761:24"
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

## usage_mismatch:0c4be17ab524f11cc0d0bbe99e3332d7:match

```yaml
regex_id: 0c4be17ab524f11cc0d0bbe99e3332d7
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:1742:29"
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

## usage_mismatch:0cfdc5386a318ecd142a2b082abf6f5a:match

```yaml
regex_id: 0cfdc5386a318ecd142a2b082abf6f5a
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:747:25"
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

## usage_mismatch:12102b32ef53cf1b37cfbea851747874:match

```yaml
regex_id: 12102b32ef53cf1b37cfbea851747874
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:740:26"
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

## usage_mismatch:1379c08fb150e85d202d514a48f90ea3:match

```yaml
regex_id: 1379c08fb150e85d202d514a48f90ea3
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:710:25"
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

## usage_mismatch:16a03c0f4e11bf71b57ef78ba22160ed:search

```yaml
regex_id: 16a03c0f4e11bf71b57ef78ba22160ed
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/http/cookiejar.py:1259:14"
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

## usage_mismatch:1bf8d74aea881b4ce06f8bede54bcd46:search

```yaml
regex_id: 1bf8d74aea881b4ce06f8bede54bcd46
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_smtplib.py:609:16"
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

## usage_mismatch:1c7d33f95cdf82266fdc225cdbc3b877:search

```yaml
regex_id: 1c7d33f95cdf82266fdc225cdbc3b877
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/logging/__init__.py:482:15"
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

## usage_mismatch:1d59544732556d5eb17444f03784c5d3:search

```yaml
regex_id: 1d59544732556d5eb17444f03784c5d3
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/doctest.py:1498:30"
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

## usage_mismatch:1d7c15226b1b7001540fc34f2b43f359:search

```yaml
regex_id: 1d7c15226b1b7001540fc34f2b43f359
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:807:26"
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

## usage_mismatch:22628472abe6b665798c430764b2b788:match

```yaml
regex_id: 22628472abe6b665798c430764b2b788
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:637:25"
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

## usage_mismatch:24dadb2020441cf0a685da83c87ea7d6:search

```yaml
regex_id: 24dadb2020441cf0a685da83c87ea7d6
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_smtplib.py:603:17"
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

## usage_mismatch:266ce0018ca169b4662a88db9154dbb4:match

```yaml
regex_id: 266ce0018ca169b4662a88db9154dbb4
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:2527:24"
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

## usage_mismatch:271026be07a03fe6d6d7bb6343ac0962:search

```yaml
regex_id: 271026be07a03fe6d6d7bb6343ac0962
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/_pydecimal.py:6120:13"
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

## usage_mismatch:2796cc10ed2d15aa851425be85ec1da0:search

```yaml
regex_id: 2796cc10ed2d15aa851425be85ec1da0
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/configparser.py:1376:16"
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

## usage_mismatch:28a0ecb080f67d7536f7daa8e3ee3cfa:search

```yaml
regex_id: 28a0ecb080f67d7536f7daa8e3ee3cfa
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/platform.py:1425:22"
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

## intent_mismatch:2af3712660c9b093e33aa6bcfdffdadd:email

```yaml
regex_id: 2af3712660c9b093e33aa6bcfdffdadd
schema_version: "1"
kind: intent_mismatch
corpus: cinder
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/email/feedparser.py:37:11"
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

## usage_mismatch:2af3712660c9b093e33aa6bcfdffdadd:search

```yaml
regex_id: 2af3712660c9b093e33aa6bcfdffdadd
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/email/feedparser.py:37:11"
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

## usage_mismatch:2cffd9386288de8a89ed272c77a9445c:search

```yaml
regex_id: 2cffd9386288de8a89ed272c77a9445c
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/http/cookiejar.py:621:14"
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

## usage_mismatch:2d47e9e50d24c92018e606350b90178c:search

```yaml
regex_id: 2d47e9e50d24c92018e606350b90178c
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/http/cookiejar.py:536:10"
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

## usage_mismatch:2ee351e76f985890fb95b4218cf5474c:match

```yaml
regex_id: 2ee351e76f985890fb95b4218cf5474c
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:712:25"
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

## usage_mismatch:33d81591931ea4ce032f8c82717de450:match

```yaml
regex_id: 33d81591931ea4ce032f8c82717de450
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:2513:26"
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

## usage_mismatch:3446d3df3721efbeadf793c68163bc97:search

```yaml
regex_id: 3446d3df3721efbeadf793c68163bc97
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/logging/config.py:379:20"
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

## usage_mismatch:34990fd40c24084d25361420514a1216:match

```yaml
regex_id: 34990fd40c24084d25361420514a1216
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:647:25"
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

## usage_mismatch:34b5691a2abe60980ea877668e19ac1b:match

```yaml
regex_id: 34b5691a2abe60980ea877668e19ac1b
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:765:24"
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

## usage_mismatch:3579c68d25437c8d337674c69c34f56c:match

```yaml
regex_id: 3579c68d25437c8d337674c69c34f56c
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/idlelib/format.py:181:11"
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

## usage_mismatch:38bb695527065c86d9f78726b35f5a10:search

```yaml
regex_id: 38bb695527065c86d9f78726b35f5a10
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:1831:18"
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

## usage_mismatch:3cae274b5a84bb8f42ade5e45fcb1ed6:search

```yaml
regex_id: 3cae274b5a84bb8f42ade5e45fcb1ed6
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/http/cookiejar.py:207:17"
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

## usage_mismatch:3cf006e779e2d27675721d23b4a2fee5:match

```yaml
regex_id: 3cf006e779e2d27675721d23b4a2fee5
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:649:25"
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

## usage_mismatch:3d327aab94055da3c599835b6da25b08:search

```yaml
regex_id: 3d327aab94055da3c599835b6da25b08
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/logging/config.py:375:22"
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

## usage_mismatch:44776f1127a5d40bc44453f9e30c8f13:search

```yaml
regex_id: 44776f1127a5d40bc44453f9e30c8f13
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_unittest/test_case.py:1602:16"
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

## intent_mismatch:456416ad7b1fe13df97cdbdebd252d0c:email

```yaml
regex_id: 456416ad7b1fe13df97cdbdebd252d0c
schema_version: "1"
kind: intent_mismatch
corpus: cinder
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_email/test_email.py:5807:17"
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

## usage_mismatch:456416ad7b1fe13df97cdbdebd252d0c:search

```yaml
regex_id: 456416ad7b1fe13df97cdbdebd252d0c
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_email/test_email.py:5807:17"
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

## intent_mismatch:45f21d56fd820ffadd0be1b5830de280:email

```yaml
regex_id: 45f21d56fd820ffadd0be1b5830de280
schema_version: "1"
kind: intent_mismatch
corpus: cinder
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/email/generator.py:23:7"
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

## usage_mismatch:45f21d56fd820ffadd0be1b5830de280:search

```yaml
regex_id: 45f21d56fd820ffadd0be1b5830de280
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/email/generator.py:23:7"
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

## usage_mismatch:47fc24904b420a9c3870a07c19ccd821:match

```yaml
regex_id: 47fc24904b420a9c3870a07c19ccd821
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:715:26"
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

## usage_mismatch:49282a472438039347ab8163ce79d88b:search

```yaml
regex_id: 49282a472438039347ab8163ce79d88b
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/http/cookiejar.py:1261:15"
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

## intent_mismatch:4a697ed71dd276bbe302a9a6a10e3bf9:email

```yaml
regex_id: 4a697ed71dd276bbe302a9a6a10e3bf9
schema_version: "1"
kind: intent_mismatch
corpus: cinder
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/email/feedparser.py:40:16"
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

## usage_mismatch:4a697ed71dd276bbe302a9a6a10e3bf9:search

```yaml
regex_id: 4a697ed71dd276bbe302a9a6a10e3bf9
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/email/feedparser.py:40:16"
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

## usage_mismatch:52d8105ed57f62a93ca90416049f9a61:match

```yaml
regex_id: 52d8105ed57f62a93ca90416049f9a61
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:748:25"
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

## usage_mismatch:561387acdc657f19d00de57a7a4c5e94:match

```yaml
regex_id: 561387acdc657f19d00de57a7a4c5e94
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:763:24"
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

## usage_mismatch:59823fe40688271e14cb79986bfffb1e:search

```yaml
regex_id: 59823fe40688271e14cb79986bfffb1e
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/logging/config.py:378:18"
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

## usage_mismatch:5a418d619a22523926d6d56d2598777d:match

```yaml
regex_id: 5a418d619a22523926d6d56d2598777d
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:741:26"
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

## usage_mismatch:5ad46ae07168a7e65061cfccda2970d4:search

```yaml
regex_id: 5ad46ae07168a7e65061cfccda2970d4
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/doctest.py:804:17"
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

## usage_mismatch:5b1e8d72fd77d27dc574b0e08f0da928:search

```yaml
regex_id: 5b1e8d72fd77d27dc574b0e08f0da928
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Android/android.py:165:20"
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

## usage_mismatch:5b70d200cde1e8a84c6235ddcc19d36d:search

```yaml
regex_id: 5b70d200cde1e8a84c6235ddcc19d36d
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_pyrepl/test_pyrepl.py:1689:24"
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

## usage_mismatch:5ca60726cbab723a27efc440fa1508ba:match

```yaml
regex_id: 5ca60726cbab723a27efc440fa1508ba
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:766:24"
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

## usage_mismatch:5d3df6cb355a7a114f3e3b13d1b74b9a:match

```yaml
regex_id: 5d3df6cb355a7a114f3e3b13d1b74b9a
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:746:25"
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

## usage_mismatch:5d49f55acb74aea369ed652964efa4fa:match

```yaml
regex_id: 5d49f55acb74aea369ed652964efa4fa
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:742:26"
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

## usage_mismatch:5d708a4f7303a67cb6aa5f1cc6e34505:search

```yaml
regex_id: 5d708a4f7303a67cb6aa5f1cc6e34505
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/logging/__init__.py:483:17"
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

## usage_mismatch:64e1abaf8674677e5a53aef8ba80460c:search

```yaml
regex_id: 64e1abaf8674677e5a53aef8ba80460c
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_pyrepl/test_pyrepl.py:1699:24"
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

## usage_mismatch:65c2a8526ec910e7e4f562ca50c0bd66:match

```yaml
regex_id: 65c2a8526ec910e7e4f562ca50c0bd66
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:639:25"
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

## usage_mismatch:66bea67803f21274ff44af2eac97488f:match

```yaml
regex_id: 66bea67803f21274ff44af2eac97488f
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:749:25"
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

## usage_mismatch:685561a767e91f869d9a70f5558835b7:match

```yaml
regex_id: 685561a767e91f869d9a70f5558835b7
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:2517:25"
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

## usage_mismatch:6947a626decbd1c81367cd2f305a7946:search

```yaml
regex_id: 6947a626decbd1c81367cd2f305a7946
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_smtplib.py:544:17"
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

## intent_mismatch:72635df9862a4a6369cc8138fe7d045d:email

```yaml
regex_id: 72635df9862a4a6369cc8138fe7d045d
schema_version: "1"
kind: intent_mismatch
corpus: cinder
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/email/header.py:35:7"
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

## usage_mismatch:73792c5b712f9741aee02b897dc7d94e:search

```yaml
regex_id: 73792c5b712f9741aee02b897dc7d94e
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:808:25"
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

## usage_mismatch:77e6fb0ce5ab04fe26936ffd39efed04:search

```yaml
regex_id: 77e6fb0ce5ab04fe26936ffd39efed04
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/http/cookiejar.py:346:25"
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

## usage_mismatch:7fd7a551ae34efde197b72474243e4f2:search

```yaml
regex_id: 7fd7a551ae34efde197b72474243e4f2
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/email/header.py:48:7"
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

## usage_mismatch:80c84cd45223ab489726c7f54f2c03d7:match

```yaml
regex_id: 80c84cd45223ab489726c7f54f2c03d7
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:764:24"
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

## usage_mismatch:81e0e8a0a62827406187b39e4ed6be29:search

```yaml
regex_id: 81e0e8a0a62827406187b39e4ed6be29
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/http/cookiejar.py:345:25"
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

## usage_mismatch:852bd4fde668f9fa533d79450a138a3e:search

```yaml
regex_id: 852bd4fde668f9fa533d79450a138a3e
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Doc/tools/extensions/misc_news.py:33:38"
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

## usage_mismatch:85e28897dce6f37b115fe3864b69b04a:match

```yaml
regex_id: 85e28897dce6f37b115fe3864b69b04a
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:2515:25"
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

## usage_mismatch:8d479f5b7895b97a779e4197f74826a2:search

```yaml
regex_id: 8d479f5b7895b97a779e4197f74826a2
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/email/utils.py:395:23"
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

## usage_mismatch:8e71d09a9fa978a7d218afe089ee3e68:search

```yaml
regex_id: 8e71d09a9fa978a7d218afe089ee3e68
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/http/cookiejar.py:210:13"
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

## usage_mismatch:9056cebbcb918f7f229e2db327cdca3e:search

```yaml
regex_id: 9056cebbcb918f7f229e2db327cdca3e
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:2022:12"
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

## usage_mismatch:9176c5c420565a12ebb2671ce5d88a3c:search

```yaml
regex_id: 9176c5c420565a12ebb2671ce5d88a3c
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/http/cookiejar.py:289:14"
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

## usage_mismatch:98c91d2d8ff8244342c1ca91bdb07801:match

```yaml
regex_id: 98c91d2d8ff8244342c1ca91bdb07801
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:2520:26"
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

## usage_mismatch:9cd7b92593e57ee49ae218f32cdbf98b:match

```yaml
regex_id: 9cd7b92593e57ee49ae218f32cdbf98b
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:744:25"
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

## usage_mismatch:9cdccbe22eccfd21d82e97b3947a09a3:search

```yaml
regex_id: 9cdccbe22eccfd21d82e97b3947a09a3
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_unittest/test_case.py:1540:46"
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

## usage_mismatch:a01310fdd43d2c2fc938b9c045677b56:match

```yaml
regex_id: a01310fdd43d2c2fc938b9c045677b56
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:755:26"
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

## usage_mismatch:a17ee55df7bb74ef5962dc53aec69c3d:search

```yaml
regex_id: a17ee55df7bb74ef5962dc53aec69c3d
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/pydoc.py:278:14"
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

## usage_mismatch:a558dd6bbf7edfa913d30f13244f8398:search

```yaml
regex_id: a558dd6bbf7edfa913d30f13244f8398
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/http/cookiejar.py:212:21"
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

## usage_mismatch:a6ae81b46b3dcb5305fb27eff9d5d38d:search

```yaml
regex_id: a6ae81b46b3dcb5305fb27eff9d5d38d
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/doctest.py:655:27"
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

## usage_mismatch:a6d63d28cc1b5c0d9f0b1ef53e70e7c6:match

```yaml
regex_id: a6d63d28cc1b5c0d9f0b1ef53e70e7c6
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:762:24"
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

## usage_mismatch:a767fa88ff41902b544ccf58d6b7eed2:search

```yaml
regex_id: a767fa88ff41902b544ccf58d6b7eed2
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_smtplib.py:158:19"
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

## intent_mismatch:a8701aa810d7e2e8a13df7e93183536c:email

```yaml
regex_id: a8701aa810d7e2e8a13df7e93183536c
schema_version: "1"
kind: intent_mismatch
corpus: cinder
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/email/_header_value_parser.py:117:18"
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

## usage_mismatch:a87a55fd3c54c87c6e04740323dcb362:search

```yaml
regex_id: a87a55fd3c54c87c6e04740323dcb362
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/logging/config.py:377:19"
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

## usage_mismatch:a87acb96ad2600b28d43ac8d702f045e:search

```yaml
regex_id: a87acb96ad2600b28d43ac8d702f045e
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_smtplib.py:574:17"
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

## usage_mismatch:a9d44975d3282b78c6f97cf4a80ba34c:search

```yaml
regex_id: a9d44975d3282b78c6f97cf4a80ba34c
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/idlelib/pyshell.py:1355:35"
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

## usage_mismatch:aa006fe53a3f39f90e3df39e03d7ba77:search

```yaml
regex_id: aa006fe53a3f39f90e3df39e03d7ba77
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/idlelib/pyshell.py:1354:35"
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

## usage_mismatch:accbc9d4ddc4dec2ce49a0e0c1b624b3:search

```yaml
regex_id: accbc9d4ddc4dec2ce49a0e0c1b624b3
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:806:25"
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

## usage_mismatch:ad61aa0de571853500c51401ae1d1012:match

```yaml
regex_id: ad61aa0de571853500c51401ae1d1012
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:716:25"
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

## usage_mismatch:ad6ff5b4ccff24da6e5c70c482dcd189:match

```yaml
regex_id: ad6ff5b4ccff24da6e5c70c482dcd189
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:758:24"
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

## usage_mismatch:ade64f26064d3c41b8e6719234722f8c:search

```yaml
regex_id: ade64f26064d3c41b8e6719234722f8c
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_regrtest.py:1419:16"
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

## usage_mismatch:aedcba3436016f070e3e326569fcea06:match

```yaml
regex_id: aedcba3436016f070e3e326569fcea06
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:759:24"
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

## usage_mismatch:b0beb6e826f533568dea7c01d831810d:match

```yaml
regex_id: b0beb6e826f533568dea7c01d831810d
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:641:26"
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

## usage_mismatch:b4ab117c4f4a214dd9f37fd5bbdeded7:search

```yaml
regex_id: b4ab117c4f4a214dd9f37fd5bbdeded7
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/_pydecimal.py:6121:14"
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

## usage_mismatch:b6941923c0eb3f6b33cd1c39a03d66ac:match

```yaml
regex_id: b6941923c0eb3f6b33cd1c39a03d66ac
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:645:25"
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

## usage_mismatch:be550364814b9df8652501ed7090d826:search

```yaml
regex_id: be550364814b9df8652501ed7090d826
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/doctest.py:773:27"
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

## usage_mismatch:c04a4ae54682e55bb0d1298790c7a818:search

```yaml
regex_id: c04a4ae54682e55bb0d1298790c7a818
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/urllib/request.py:268:15"
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

## usage_mismatch:c0f10e8f1f04f1c5f576680d2cc791b6:search

```yaml
regex_id: c0f10e8f1f04f1c5f576680d2cc791b6
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_smtplib.py:635:17"
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

## usage_mismatch:c39db1dffdb65e169f423450dc326a88:search

```yaml
regex_id: c39db1dffdb65e169f423450dc326a88
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:805:25"
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

## usage_mismatch:c9999ca3480b1a72a484391d79b01a93:match

```yaml
regex_id: c9999ca3480b1a72a484391d79b01a93
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:643:25"
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

## usage_mismatch:cdfcfc586b161a2f3b10d663ee9b8454:match

```yaml
regex_id: cdfcfc586b161a2f3b10d663ee9b8454
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:2512:26"
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

## usage_mismatch:ceed85406a1fca67e98fd6571e23d198:match

```yaml
regex_id: ceed85406a1fca67e98fd6571e23d198
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:751:25"
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

## usage_mismatch:cffc878450245d6d5828320591ebdebd:match

```yaml
regex_id: cffc878450245d6d5828320591ebdebd
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:760:24"
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

## usage_mismatch:d1154687a4f975edb5b1d19eb87d1326:search

```yaml
regex_id: d1154687a4f975edb5b1d19eb87d1326
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_smtplib.py:148:19"
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

## usage_mismatch:d139ab1a955d3503f2ad514095c4b573:search

```yaml
regex_id: d139ab1a955d3503f2ad514095c4b573
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/http/cookiejar.py:136:14"
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

## usage_mismatch:d15dfc0bd27128de7353775599de5382:match

```yaml
regex_id: d15dfc0bd27128de7353775599de5382
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:769:24"
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

## usage_mismatch:d2681779e44c440bee4cfc782e1d3459:search

```yaml
regex_id: d2681779e44c440bee4cfc782e1d3459
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:809:26"
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

## usage_mismatch:d3a54d4dd5995a0a084c8507aa8b78e7:search

```yaml
regex_id: d3a54d4dd5995a0a084c8507aa8b78e7
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_smtplib.py:672:17"
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

## usage_mismatch:d4900c7334784be0a3dfd449154f7fd3:match

```yaml
regex_id: d4900c7334784be0a3dfd449154f7fd3
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:754:26"
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

## usage_mismatch:d531f0f8a972d1ab40ee296360c04276:match

```yaml
regex_id: d531f0f8a972d1ab40ee296360c04276
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:739:26"
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

## usage_mismatch:d5a4312b63d1f22a8888d5965fa67a1b:search

```yaml
regex_id: d5a4312b63d1f22a8888d5965fa67a1b
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:632:12"
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

## usage_mismatch:d6c2ebfcfed3a3c4089dfcedb7b16c85:search

```yaml
regex_id: d6c2ebfcfed3a3c4089dfcedb7b16c85
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/logging/config.py:380:20"
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

## usage_mismatch:d9236d978e2cf285cb1cad122a158721:match

```yaml
regex_id: d9236d978e2cf285cb1cad122a158721
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:2516:25"
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

## usage_mismatch:daeff2fdca8c0e96eafc207f63914902:match

```yaml
regex_id: daeff2fdca8c0e96eafc207f63914902
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:745:25"
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

## usage_mismatch:df715b4715d66f2656f3d0f96733dbf5:match

```yaml
regex_id: df715b4715d66f2656f3d0f96733dbf5
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:2526:26"
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

## usage_mismatch:e10dd85a1164d3cd68ff71f650f4570c:search

```yaml
regex_id: e10dd85a1164d3cd68ff71f650f4570c
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Tools/c-analyzer/c_parser/preprocessor/gcc.py:36:17"
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

## usage_mismatch:e3453cc35410c3904acc7a6f4e9bf395:search

```yaml
regex_id: e3453cc35410c3904acc7a6f4e9bf395
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/logging/config.py:295:13"
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

## usage_mismatch:e401355564b3eb7599ec724e0daa3402:match

```yaml
regex_id: e401355564b3eb7599ec724e0daa3402
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:753:26"
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

## usage_mismatch:e4823fb1fbd35108b64618a2104e5c4a:match

```yaml
regex_id: e4823fb1fbd35108b64618a2104e5c4a
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:750:25"
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

## usage_mismatch:e5465b051e13587f346b2e2550378a74:match

```yaml
regex_id: e5465b051e13587f346b2e2550378a74
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:642:26"
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

## usage_mismatch:e67c904f42647f87ef6d1f1eb056ad3e:match

```yaml
regex_id: e67c904f42647f87ef6d1f1eb056ad3e
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:756:26"
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

## usage_mismatch:e80a5fa572ba69aff051ee59ab2d6044:match

```yaml
regex_id: e80a5fa572ba69aff051ee59ab2d6044
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:2522:24"
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

## usage_mismatch:eb7f926dce472dc69910e3c80908f55b:search

```yaml
regex_id: eb7f926dce472dc69910e3c80908f55b
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Tools/c-analyzer/c_parser/preprocessor/gcc.py:37:23"
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

## usage_mismatch:ede778b91f2f11980390eac57905e8e8:match

```yaml
regex_id: ede778b91f2f11980390eac57905e8e8
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:718:25"
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

## usage_mismatch:eedf35eb546f966e510766b4668c21f6:match

```yaml
regex_id: eedf35eb546f966e510766b4668c21f6
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:2523:24"
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

## usage_mismatch:efcc81a1a473cd7961f3ea3ed1a6beb0:search

```yaml
regex_id: efcc81a1a473cd7961f3ea3ed1a6beb0
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:1443:28"
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

## usage_mismatch:f277c6d6b261b8487cd711dc25806888:search

```yaml
regex_id: f277c6d6b261b8487cd711dc25806888
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/http/cookiejar.py:347:25"
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

## usage_mismatch:f32377c6a11df4c1fb364741170d7c80:match

```yaml
regex_id: f32377c6a11df4c1fb364741170d7c80
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:2519:26"
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

## usage_mismatch:f6a2432b57a7e7f2b12c422e840313f5:match

```yaml
regex_id: f6a2432b57a7e7f2b12c422e840313f5
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:2524:24"
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

## usage_mismatch:fd2644361f362a0cc0ab7530ff86d42b:match

```yaml
regex_id: fd2644361f362a0cc0ab7530ff86d42b
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_re.py:1751:30"
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

## usage_mismatch:fecc55d82d8161fc731ea06b38ec78ac:search

```yaml
regex_id: fecc55d82d8161fc731ea06b38ec78ac
schema_version: "1"
kind: usage_mismatch
corpus: cinder
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/cinder/rules/Lib/test/test_smtplib.py:491:17"
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

## property:inventory:rc-shape1-injection-alphabet:rc-shape1-injection-alphabet

```yaml
regex_id: "inventory:rc-shape1-injection-alphabet"
schema_version: "1"
kind: property
corpus: cinder
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
corpus: cinder
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
corpus: cinder
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
corpus: cinder
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

---
schema_version: "1"
corpus: pythowon
findings: 144
---

# pythowon batch findings

## usage_mismatch:05852b4476efc41c376a1e5159091862:match

```yaml
regex_id: 05852b4476efc41c376a1e5159091862
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:575:25"
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

## usage_mismatch:09b3f6a2c08f2830f9e2afca6e249152:search

```yaml
regex_id: 09b3f6a2c08f2830f9e2afca6e249152
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_smtplib.py:611:16"
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

## usage_mismatch:0a3b2405fad23d08dff9a7001479cf4e:search

```yaml
regex_id: 0a3b2405fad23d08dff9a7001479cf4e
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/http/cookiejar.py:619:14"
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

## usage_mismatch:0abcdd86ed9acb186843284f2c576a8b:search

```yaml
regex_id: 0abcdd86ed9acb186843284f2c576a8b
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/http/cookiejar.py:135:14"
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

## usage_mismatch:0efeb5eef215fa9a83f91d73a1f3c46d:search

```yaml
regex_id: 0efeb5eef215fa9a83f91d73a1f3c46d
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/idlelib/pyshell.py:1341:35"
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

## usage_mismatch:0fb1b00624837207ba04d24a3f8f9242:match

```yaml
regex_id: 0fb1b00624837207ba04d24a3f8f9242
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:2291:26"
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

## usage_mismatch:13173187d24a8a5bdcdef1966371e1e0:search

```yaml
regex_id: 13173187d24a8a5bdcdef1966371e1e0
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Doc/tools/extensions/pyspecific.py:482:14"
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

## usage_mismatch:142994a71c7102df9aac3c6b12a38147:match

```yaml
regex_id: 142994a71c7102df9aac3c6b12a38147
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:689:24"
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

## usage_mismatch:14673ac6b92b37b9efc672d3f10e4169:match

```yaml
regex_id: 14673ac6b92b37b9efc672d3f10e4169
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:673:26"
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

## usage_mismatch:156953a4f8f26e3db3f459d9ca5bd52d:search

```yaml
regex_id: 156953a4f8f26e3db3f459d9ca5bd52d
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_smtplib.py:674:17"
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

## usage_mismatch:1ad6a9421883719556306acc39b073a3:search

```yaml
regex_id: 1ad6a9421883719556306acc39b073a3
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/doctest.py:744:27"
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

## usage_mismatch:1d1ce30d76a68d10a5ae2bc3fc25e987:match

```yaml
regex_id: 1d1ce30d76a68d10a5ae2bc3fc25e987
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:2284:26"
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

## usage_mismatch:1dc50a9ae43cc26917962b5906cb40d2:search

```yaml
regex_id: 1dc50a9ae43cc26917962b5906cb40d2
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/http/cookiejar.py:345:25"
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

## usage_mismatch:1ed51f12317861c8421c933a95520c3e:match

```yaml
regex_id: 1ed51f12317861c8421c933a95520c3e
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:677:25"
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

## usage_mismatch:212161cb317e2d8157d6bdefc9b4db5b:match

```yaml
regex_id: 212161cb317e2d8157d6bdefc9b4db5b
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:670:26"
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

## usage_mismatch:259674aeb7abe5d6c8bb63f6e6ac9212:search

```yaml
regex_id: 259674aeb7abe5d6c8bb63f6e6ac9212
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/http/cookiejar.py:206:17"
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

## usage_mismatch:262cd28a1b9ff5e4581657fb7ef890ee:match

```yaml
regex_id: 262cd28a1b9ff5e4581657fb7ef890ee
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:699:26"
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

## usage_mismatch:270d0b86c902ec8a51dc744772a78c2c:match

```yaml
regex_id: 270d0b86c902ec8a51dc744772a78c2c
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:684:26"
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

## usage_mismatch:2b8ff84d402938636e21e09aa6a71800:match

```yaml
regex_id: 2b8ff84d402938636e21e09aa6a71800
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/msilib/__init__.py:184:11"
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

## usage_mismatch:2bf893a3fc625ec26c3ef82c6d3f56fa:search

```yaml
regex_id: 2bf893a3fc625ec26c3ef82c6d3f56fa
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Tools/scripts/texi2html.py:73:9"
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

## usage_mismatch:2cdebd8a6386f3a5c27b6bfb7377d71c:search

```yaml
regex_id: 2cdebd8a6386f3a5c27b6bfb7377d71c
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/http/cookiejar.py:346:25"
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

## usage_mismatch:2f7ddc1b1783c5f3708c468004dd8ccd:search

```yaml
regex_id: 2f7ddc1b1783c5f3708c468004dd8ccd
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/urllib/request.py:299:15"
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

## usage_mismatch:30011bebd26518fe27fc0c7dc6fb999a:search

```yaml
regex_id: 30011bebd26518fe27fc0c7dc6fb999a
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/lib2to3/pgen2/tokenize.py:227:12"
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

## usage_mismatch:3378523746352ddc9bd92c16dba256f3:search

```yaml
regex_id: 3378523746352ddc9bd92c16dba256f3
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/http/cookiejar.py:211:21"
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

## usage_mismatch:337a01b173da3ad2eb975fefa453aebd:search

```yaml
regex_id: 337a01b173da3ad2eb975fefa453aebd
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Tools/scripts/texi2html.py:1597:19"
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

## usage_mismatch:363841b616fd92f007a88a1c02cfca05:match

```yaml
regex_id: 363841b616fd92f007a88a1c02cfca05
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:577:26"
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

## usage_mismatch:37b3906d6cc6a358b186baac235e14de:match

```yaml
regex_id: 37b3906d6cc6a358b186baac235e14de
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:671:26"
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

## usage_mismatch:3cd8f578255a3ef6d44b6dea307872e1:match

```yaml
regex_id: 3cd8f578255a3ef6d44b6dea307872e1
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:678:25"
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

## intent_mismatch:3d403ea0a9e4b57368b4e5dbf280e411:email

```yaml
regex_id: 3d403ea0a9e4b57368b4e5dbf280e411
schema_version: "1"
kind: intent_mismatch
corpus: pythowon
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_email/test_email.py:5545:17"
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

## usage_mismatch:3d403ea0a9e4b57368b4e5dbf280e411:search

```yaml
regex_id: 3d403ea0a9e4b57368b4e5dbf280e411
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_email/test_email.py:5545:17"
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

## usage_mismatch:3e890500f4640eed83e50c810e6b914d:search

```yaml
regex_id: 3e890500f4640eed83e50c810e6b914d
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_unittest/test_case.py:1311:46"
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

## usage_mismatch:3f194c1f2db6f24b8ec7379cbdbb22e0:search

```yaml
regex_id: 3f194c1f2db6f24b8ec7379cbdbb22e0
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:737:25"
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

## usage_mismatch:40ac204f46d5e08cdd53f8f885972f3a:search

```yaml
regex_id: 40ac204f46d5e08cdd53f8f885972f3a
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:1597:18"
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

## usage_mismatch:4443070f8bc4a22fcdb9257109cc6d5a:match

```yaml
regex_id: 4443070f8bc4a22fcdb9257109cc6d5a
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:679:25"
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

## usage_mismatch:449476f8cae7e7b71ac3f26310df41ee:search

```yaml
regex_id: 449476f8cae7e7b71ac3f26310df41ee
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/distutils/versionpredicate.py:12:11"
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

## usage_mismatch:49f68b4f0e3238529821602f60e3c550:search

```yaml
regex_id: 49f68b4f0e3238529821602f60e3c550
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/http/cookiejar.py:1259:15"
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

## usage_mismatch:4a73be8195bd5e769e9249cc5acf58b4:match

```yaml
regex_id: 4a73be8195bd5e769e9249cc5acf58b4
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:686:26"
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

## usage_mismatch:4a8b5ee38777d0ce0ac74826d19e5e5b:search

```yaml
regex_id: 4a8b5ee38777d0ce0ac74826d19e5e5b
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_unittest/test_case.py:1373:16"
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

## intent_mismatch:4cbfa7982bbe9a6f938ca788a6a94f96:email

```yaml
regex_id: 4cbfa7982bbe9a6f938ca788a6a94f96
schema_version: "1"
kind: intent_mismatch
corpus: pythowon
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/email/generator.py:22:7"
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

## usage_mismatch:4cbfa7982bbe9a6f938ca788a6a94f96:search

```yaml
regex_id: 4cbfa7982bbe9a6f938ca788a6a94f96
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/email/generator.py:22:7"
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

## usage_mismatch:4e15a6ebdf0e2e36d74ff4aab5cbd7cc:match

```yaml
regex_id: 4e15a6ebdf0e2e36d74ff4aab5cbd7cc
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:641:25"
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

## usage_mismatch:4f6d2cd62d057bc1ea0b77f27f5f9c64:search

```yaml
regex_id: 4f6d2cd62d057bc1ea0b77f27f5f9c64
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Tools/c-analyzer/c_parser/preprocessor/gcc.py:15:17"
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

## usage_mismatch:50b7ae66d7391f938de08c52e082571d:match

```yaml
regex_id: 50b7ae66d7391f938de08c52e082571d
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:692:24"
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

## usage_mismatch:511ae450be17e2676245c6a012f436af:search

```yaml
regex_id: 511ae450be17e2676245c6a012f436af
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/logging/config.py:280:13"
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

## usage_mismatch:5229fcffc31a7e9d29fb866ea6feb3d0:search

```yaml
regex_id: 5229fcffc31a7e9d29fb866ea6feb3d0
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/doctest.py:775:17"
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

## intent_mismatch:5328b4aeea4490123bed7a193b2d862a:email

```yaml
regex_id: 5328b4aeea4490123bed7a193b2d862a
schema_version: "1"
kind: intent_mismatch
corpus: pythowon
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/email/feedparser.py:37:11"
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

## usage_mismatch:5328b4aeea4490123bed7a193b2d862a:search

```yaml
regex_id: 5328b4aeea4490123bed7a193b2d862a
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/email/feedparser.py:37:11"
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

## usage_mismatch:57aba563b3549a2c78d24649ec7fc717:match

```yaml
regex_id: 57aba563b3549a2c78d24649ec7fc717
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:2289:25"
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

## usage_mismatch:585923dedd506fe7d431fe48f4db8540:match

```yaml
regex_id: 585923dedd506fe7d431fe48f4db8540
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Tools/demo/spreadsheet.py:417:16"
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

## usage_mismatch:58c9bbae6abe2642e5fe04d5c9ec1b55:match

```yaml
regex_id: 58c9bbae6abe2642e5fe04d5c9ec1b55
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:1518:30"
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

## usage_mismatch:5b8acf2a6e3ca33353eaac56b274537b:match

```yaml
regex_id: 5b8acf2a6e3ca33353eaac56b274537b
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:691:24"
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

## usage_mismatch:5c97bdf35126329b3668580001f3f912:search

```yaml
regex_id: 5c97bdf35126329b3668580001f3f912
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/platform.py:1324:19"
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

## usage_mismatch:5f426fe11a971f314eae17c5f52871b9:search

```yaml
regex_id: 5f426fe11a971f314eae17c5f52871b9
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/logging/__init__.py:475:17"
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

## usage_mismatch:62e2b876e6a085c98e238bdf33234bec:match

```yaml
regex_id: 62e2b876e6a085c98e238bdf33234bec
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:675:25"
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

## usage_mismatch:634459039a18cbfa8810a44257268051:search

```yaml
regex_id: 634459039a18cbfa8810a44257268051
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/logging/config.py:363:18"
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

## usage_mismatch:63c51682a5a1493e50963261b5072240:match

```yaml
regex_id: 63c51682a5a1493e50963261b5072240
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/idlelib/format.py:181:11"
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

## usage_mismatch:649f09c96b8bfac43e76fc10ac65f05d:search

```yaml
regex_id: 649f09c96b8bfac43e76fc10ac65f05d
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_smtplib.py:605:17"
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

## usage_mismatch:656a93b5ad59c1473e3c1c2377ccdd5e:search

```yaml
regex_id: 656a93b5ad59c1473e3c1c2377ccdd5e
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_smtplib.py:493:17"
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

## usage_mismatch:66c8ce3691e4b28751b33ad10eab32af:search

```yaml
regex_id: 66c8ce3691e4b28751b33ad10eab32af
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/logging/config.py:364:20"
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

## intent_mismatch:68661c0a45a7395df09f029353ff8971:email

```yaml
regex_id: 68661c0a45a7395df09f029353ff8971
schema_version: "1"
kind: intent_mismatch
corpus: pythowon
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/email/_header_value_parser.py:100:18"
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

## usage_mismatch:69e929484d2ab1a055d39b8f63ad30df:search

```yaml
regex_id: 69e929484d2ab1a055d39b8f63ad30df
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_smtplib.py:637:17"
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

## usage_mismatch:6be7b64bbb5fcc0b1eb38a57675379d0:search

```yaml
regex_id: 6be7b64bbb5fcc0b1eb38a57675379d0
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Tools/scripts/texi2html.py:81:9"
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

## usage_mismatch:6ea7d33306b3cf470dd9656e19fcf050:match

```yaml
regex_id: 6ea7d33306b3cf470dd9656e19fcf050
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:647:25"
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

## usage_mismatch:6f1d6b206d6c3a10713ec619d8b65c3c:match

```yaml
regex_id: 6f1d6b206d6c3a10713ec619d8b65c3c
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:694:24"
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

## usage_mismatch:75b22412f3cff003004f2356c047f68b:match

```yaml
regex_id: 75b22412f3cff003004f2356c047f68b
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:695:24"
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

## usage_mismatch:768b8122212171cddeda36257b28db9c:search

```yaml
regex_id: 768b8122212171cddeda36257b28db9c
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/logging/config.py:365:20"
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

## usage_mismatch:7797d6bab83f0c5f5ba37bf4920f567e:search

```yaml
regex_id: 7797d6bab83f0c5f5ba37bf4920f567e
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_smtplib.py:546:17"
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

## usage_mismatch:77c2e8ece5829bbd0328325fd224c6de:search

```yaml
regex_id: 77c2e8ece5829bbd0328325fd224c6de
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Tools/scripts/mailerdaemon.py:96:20"
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

## usage_mismatch:7e4b63aecdbd4b4f4af81d72128c367c:search

```yaml
regex_id: 7e4b63aecdbd4b4f4af81d72128c367c
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/logging/__init__.py:474:15"
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

## usage_mismatch:7e93b24222b5f6943a84f6c89985d710:match

```yaml
regex_id: 7e93b24222b5f6943a84f6c89985d710
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:579:25"
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

## usage_mismatch:8181c062b584009e77818b0160dfbb92:search

```yaml
regex_id: 8181c062b584009e77818b0160dfbb92
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/email/utils.py:257:23"
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

## usage_mismatch:819cf99e162bb62868565d2fb6683e39:match

```yaml
regex_id: 819cf99e162bb62868565d2fb6683e39
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:672:26"
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

## usage_mismatch:84dcfb982bb4a2dcc760860624d514ae:match

```yaml
regex_id: 84dcfb982bb4a2dcc760860624d514ae
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:643:25"
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

## usage_mismatch:8578c4bf14e9c499183eba27cfeab4a9:match

```yaml
regex_id: 8578c4bf14e9c499183eba27cfeab4a9
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:696:24"
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

## usage_mismatch:86fe0bcc55d010996141d2b38c175881:match

```yaml
regex_id: 86fe0bcc55d010996141d2b38c175881
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:685:26"
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

## usage_mismatch:89d6a656d463e2b5d44b24e50fa27a05:match

```yaml
regex_id: 89d6a656d463e2b5d44b24e50fa27a05
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:2285:26"
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

## usage_mismatch:8dbfe0499c232fdd1652948df7317d19:match

```yaml
regex_id: 8dbfe0499c232fdd1652948df7317d19
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:693:24"
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

## usage_mismatch:8e2bc1c40933924c41e6a761df53a414:search

```yaml
regex_id: 8e2bc1c40933924c41e6a761df53a414
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_regrtest.py:977:16"
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

## usage_mismatch:8ea4b940ebb9127080151e61e218eca7:match

```yaml
regex_id: 8ea4b940ebb9127080151e61e218eca7
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:682:25"
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

## usage_mismatch:9209116c943b3a27250cb9d33a4f0bd2:search

```yaml
regex_id: 9209116c943b3a27250cb9d33a4f0bd2
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/distutils/versionpredicate.py:156:24"
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

## usage_mismatch:926ba8979c7fd72b241cd97d91012f88:search

```yaml
regex_id: 926ba8979c7fd72b241cd97d91012f88
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Tools/scripts/mailerdaemon.py:168:10"
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

## usage_mismatch:935197e74a7eaa151d8d5bc594b9f441:search

```yaml
regex_id: 935197e74a7eaa151d8d5bc594b9f441
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:1210:28"
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

## usage_mismatch:955a8d62d30f389f5472025ab9e1d557:search

```yaml
regex_id: 955a8d62d30f389f5472025ab9e1d557
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/doctest.py:626:27"
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

## usage_mismatch:97242cb6a6352468a7518d08512c6569:search

```yaml
regex_id: 97242cb6a6352468a7518d08512c6569
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/http/cookiejar.py:451:23"
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

## usage_mismatch:9bf399e0e70dd1101b9a16160a199b6e:match

```yaml
regex_id: 9bf399e0e70dd1101b9a16160a199b6e
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:676:25"
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

## usage_mismatch:9f979999d71c862c3873c622c689402d:search

```yaml
regex_id: 9f979999d71c862c3873c622c689402d
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/textwrap.py:416:22"
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

## usage_mismatch:a2f0bcacd4dba61d40cb95a754e2d75e:search

```yaml
regex_id: a2f0bcacd4dba61d40cb95a754e2d75e
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:1592:18"
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

## usage_mismatch:a6a091398b61e26036d6fe997c600ede:search

```yaml
regex_id: a6a091398b61e26036d6fe997c600ede
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/idlelib/pyshell.py:1342:35"
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

## usage_mismatch:a9d12eb70d12306c6d00c0338cc10ef1:match

```yaml
regex_id: a9d12eb70d12306c6d00c0338cc10ef1
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:573:25"
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

## usage_mismatch:ad57fe84a9e2bfd26d8f72b558741aeb:match

```yaml
regex_id: ad57fe84a9e2bfd26d8f72b558741aeb
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:2299:24"
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

## usage_mismatch:b0609712743603e71db1da8abbec26d6:search

```yaml
regex_id: b0609712743603e71db1da8abbec26d6
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/http/cookiejar.py:534:10"
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

## usage_mismatch:b2f8e2aa75e98661a7d37283c9ab134b:match

```yaml
regex_id: b2f8e2aa75e98661a7d37283c9ab134b
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:649:25"
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

## usage_mismatch:b3041ff0b4aa70897658e2ddcd64b858:match

```yaml
regex_id: b3041ff0b4aa70897658e2ddcd64b858
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:687:26"
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

## usage_mismatch:b3085f9fcac25d723b88ed5268ab824a:match

```yaml
regex_id: b3085f9fcac25d723b88ed5268ab824a
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:1509:29"
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

## usage_mismatch:b757cd20643ab877971547e63815aab3:search

```yaml
regex_id: b757cd20643ab877971547e63815aab3
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_smtplib.py:160:19"
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

## usage_mismatch:b82adf2681d87b0cebecf34287f970c9:search

```yaml
regex_id: b82adf2681d87b0cebecf34287f970c9
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/http/cookiejar.py:288:14"
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

## usage_mismatch:b9af684a7aaa01da80618287011a7e0d:search

```yaml
regex_id: b9af684a7aaa01da80618287011a7e0d
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/http/cookiejar.py:344:25"
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

## usage_mismatch:ba3f60c162e359c79531e92bbed45aae:search

```yaml
regex_id: ba3f60c162e359c79531e92bbed45aae
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:736:25"
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

## usage_mismatch:be810d47c6d79cdc5977233a54832d24:search

```yaml
regex_id: be810d47c6d79cdc5977233a54832d24
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_gdb.py:43:12"
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

## usage_mismatch:c2f066473e178f04c48d575a5a5af2a0:match

```yaml
regex_id: c2f066473e178f04c48d575a5a5af2a0
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:645:26"
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

## usage_mismatch:c5bb4bef805b2c007d572376c48ef2fe:match

```yaml
regex_id: c5bb4bef805b2c007d572376c48ef2fe
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:2295:24"
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

## usage_mismatch:c68fd3ccfc194ed8ccc6ca131b50f245:search

```yaml
regex_id: c68fd3ccfc194ed8ccc6ca131b50f245
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/_pydecimal.py:6150:13"
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

## usage_mismatch:c97d39db85d23fc8d87d050e6f473cee:match

```yaml
regex_id: c97d39db85d23fc8d87d050e6f473cee
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:2296:24"
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

## usage_mismatch:c98242459f166d8aaaaab5962d661286:search

```yaml
regex_id: c98242459f166d8aaaaab5962d661286
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_smtplib.py:150:19"
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

## usage_mismatch:cca704f2f2f58476d6ad8adc85aba8ed:search

```yaml
regex_id: cca704f2f2f58476d6ad8adc85aba8ed
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/configparser.py:1282:16"
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

## usage_mismatch:ccbfc4fcb53ea82e4d763e3ee974f67a:match

```yaml
regex_id: ccbfc4fcb53ea82e4d763e3ee974f67a
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/lib2to3/pgen2/conv.py:71:17"
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

## usage_mismatch:d34681a551fc4aa7fd91908f4051b415:search

```yaml
regex_id: d34681a551fc4aa7fd91908f4051b415
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/doctest.py:1428:30"
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

## usage_mismatch:d5aaa2642de55907168ce676a942ceda:match

```yaml
regex_id: d5aaa2642de55907168ce676a942ceda
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:2288:25"
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

## usage_mismatch:d6580ccf590feacf5dfdd921b3bcfe3d:match

```yaml
regex_id: d6580ccf590feacf5dfdd921b3bcfe3d
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:2298:26"
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

## usage_mismatch:d80e2f88db7be0a96fccf94854ed2502:match

```yaml
regex_id: d80e2f88db7be0a96fccf94854ed2502
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:681:25"
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

## usage_mismatch:d810ae3bb088bf85db5a46eca66bd873:search

```yaml
regex_id: d810ae3bb088bf85db5a46eca66bd873
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/distutils/versionpredicate.py:13:21"
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

## usage_mismatch:db332d71a036f648157f93b1a7cf567b:search

```yaml
regex_id: db332d71a036f648157f93b1a7cf567b
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Tools/scripts/mailerdaemon.py:94:4"
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

## usage_mismatch:dc34c1cdaabc5195c1eca342f6cc51f3:match

```yaml
regex_id: dc34c1cdaabc5195c1eca342f6cc51f3
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:583:25"
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

## usage_mismatch:defa191a58be60522301b91113a213f7:search

```yaml
regex_id: defa191a58be60522301b91113a213f7
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/email/header.py:48:7"
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

## usage_mismatch:dff8cf333dbac894fe874ac9593dcc38:match

```yaml
regex_id: dff8cf333dbac894fe874ac9593dcc38
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:585:25"
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

## usage_mismatch:e06c1ffd853ce76c3b5fcffacdcb34ec:match

```yaml
regex_id: e06c1ffd853ce76c3b5fcffacdcb34ec
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:697:24"
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

## usage_mismatch:e145ac8e69f07cf6c1c15626d3c5eaf2:match

```yaml
regex_id: e145ac8e69f07cf6c1c15626d3c5eaf2
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:680:25"
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

## usage_mismatch:e3b03b6b3072647309153b0e0d061e9f:search

```yaml
regex_id: e3b03b6b3072647309153b0e0d061e9f
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/pydoc.py:228:14"
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

## usage_mismatch:e3cf1a8dfdd913224ecbc9e357f29aec:search

```yaml
regex_id: e3cf1a8dfdd913224ecbc9e357f29aec
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/http/cookiejar.py:209:13"
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

## usage_mismatch:e4bb5b064459f1fb857b6b3a0ac40c07:match

```yaml
regex_id: e4bb5b064459f1fb857b6b3a0ac40c07
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:2294:24"
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

## usage_mismatch:e7da6d476fd232ec5e5df2a2465d727f:match

```yaml
regex_id: e7da6d476fd232ec5e5df2a2465d727f
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:2287:25"
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

## usage_mismatch:e86bc28fdee1c0982c909fc56e2ff6f5:search

```yaml
regex_id: e86bc28fdee1c0982c909fc56e2ff6f5
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/http/cookiejar.py:1257:14"
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

## usage_mismatch:e9376d25b023afcfb5a171869437a047:search

```yaml
regex_id: e9376d25b023afcfb5a171869437a047
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Tools/c-analyzer/c_parser/preprocessor/gcc.py:16:23"
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

## usage_mismatch:ea6afcd580a0eae16bf2674fa840eb5a:match

```yaml
regex_id: ea6afcd580a0eae16bf2674fa840eb5a
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:2292:26"
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

## usage_mismatch:ea81fef58ca2bc6278ce730ffbfaa953:search

```yaml
regex_id: ea81fef58ca2bc6278ce730ffbfaa953
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:738:26"
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

## usage_mismatch:eaa1e829fcf642106f9b9b619ab6a918:search

```yaml
regex_id: eaa1e829fcf642106f9b9b619ab6a918
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/logging/config.py:362:19"
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

## usage_mismatch:eefc52a24fa34ebaf9d1f1f71e0f737e:search

```yaml
regex_id: eefc52a24fa34ebaf9d1f1f71e0f737e
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:1802:12"
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

## usage_mismatch:f08cb1ea63a3abd4e86303c6c2f94eeb:match

```yaml
regex_id: f08cb1ea63a3abd4e86303c6c2f94eeb
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:690:24"
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

## usage_mismatch:f2e149220df6966cff37b8c85292307b:search

```yaml
regex_id: f2e149220df6966cff37b8c85292307b
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:568:12"
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

## usage_mismatch:f344f26fb3b68489976c826ea9d2506f:search

```yaml
regex_id: f344f26fb3b68489976c826ea9d2506f
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_smtplib.py:576:17"
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

## usage_mismatch:f349d7084b788d069f77514b91e4375c:search

```yaml
regex_id: f349d7084b788d069f77514b91e4375c
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/logging/config.py:360:22"
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

## usage_mismatch:f4098c86e7cc314c17fe8a2449c17988:match

```yaml
regex_id: f4098c86e7cc314c17fe8a2449c17988
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:581:25"
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

## usage_mismatch:f5bf22a2453c330bb963519968a50ad2:match

```yaml
regex_id: f5bf22a2453c330bb963519968a50ad2
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:700:24"
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

## usage_mismatch:f856d1774322c7e0c982474039dbe2bd:match

```yaml
regex_id: f856d1774322c7e0c982474039dbe2bd
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:578:26"
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

## usage_mismatch:f870927b59d77aa02b6dc803a390453f:match

```yaml
regex_id: f870927b59d77aa02b6dc803a390453f
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/test/test_re.py:646:26"
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

## usage_mismatch:f88b80960499e6cc5574773a293f167a:search

```yaml
regex_id: f88b80960499e6cc5574773a293f167a
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/_pydecimal.py:6151:14"
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

## usage_mismatch:f8a1ed464a7cbfb8e413a7f1d08b99cf:match

```yaml
regex_id: f8a1ed464a7cbfb8e413a7f1d08b99cf
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Tools/demo/spreadsheet.py:436:12"
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

## usage_mismatch:f948230cf484cdf9886ce46ad0a4ec8c:search

```yaml
regex_id: f948230cf484cdf9886ce46ad0a4ec8c
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Tools/scripts/texi2html.py:74:9"
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

## usage_mismatch:fdc03bdb27cb60964ae38dc8274bf33d:search

```yaml
regex_id: fdc03bdb27cb60964ae38dc8274bf33d
schema_version: "1"
kind: usage_mismatch
corpus: pythowon
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Tools/scripts/mailerdaemon.py:92:4"
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

## intent_mismatch:ffddb080a8fc5897b5ca3e1c588b1521:email

```yaml
regex_id: ffddb080a8fc5897b5ca3e1c588b1521
schema_version: "1"
kind: intent_mismatch
corpus: pythowon
shape: null
result: finding
disclosure: null
site: "batch/corpora/pythowon/rules/Lib/email/header.py:35:7"
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

## property:inventory:rc-shape1-injection-alphabet:rc-shape1-injection-alphabet

```yaml
regex_id: "inventory:rc-shape1-injection-alphabet"
schema_version: "1"
kind: property
corpus: pythowon
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
corpus: pythowon
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
corpus: pythowon
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
corpus: pythowon
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

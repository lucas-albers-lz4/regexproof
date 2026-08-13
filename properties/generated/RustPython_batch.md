---
schema_version: "1"
corpus: RustPython
findings: 131
---

# RustPython batch findings

## usage_mismatch:0096ce2ec9405da0588f0555fb759dc3:search

```yaml
regex_id: 0096ce2ec9405da0588f0555fb759dc3
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/logging/config.py:376:19"
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

## usage_mismatch:05f29abb6bfa27673ea54b8d3a019700:search

```yaml
regex_id: 05f29abb6bfa27673ea54b8d3a019700
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_smtplib.py:574:17"
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

## usage_mismatch:08e21e3789e3c8f9c42b4322125a43a8:match

```yaml
regex_id: 08e21e3789e3c8f9c42b4322125a43a8
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:770:24"
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

## usage_mismatch:09c67244b2addd8aee09c46c87872c33:search

```yaml
regex_id: 09c67244b2addd8aee09c46c87872c33
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/http/cookiejar.py:1260:15"
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

## usage_mismatch:100621789f305ffd5bb5a3a3c206bbd3:search

```yaml
regex_id: 100621789f305ffd5bb5a3a3c206bbd3
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/http/cookiejar.py:535:10"
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

## intent_mismatch:118f7f1e428354bcace2acc528107f74:email

```yaml
regex_id: 118f7f1e428354bcace2acc528107f74
schema_version: "1"
kind: intent_mismatch
corpus: RustPython
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/email/_header_value_parser.py:117:18"
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

## usage_mismatch:141432fe3d79345dd27ad535c548dd18:match

```yaml
regex_id: 141432fe3d79345dd27ad535c548dd18
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:769:26"
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

## usage_mismatch:175bf3505ca9475108f025f2592ad4e8:match

```yaml
regex_id: 175bf3505ca9475108f025f2592ad4e8
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:765:24"
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

## usage_mismatch:179498e5c673cbeb67fb6810bb6306bb:search

```yaml
regex_id: 179498e5c673cbeb67fb6810bb6306bb
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/logging/__init__.py:483:17"
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

## usage_mismatch:1962b317ebf011ad946a3e0878d3b510:match

```yaml
regex_id: 1962b317ebf011ad946a3e0878d3b510
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:756:26"
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

## intent_mismatch:19a5063a0930d79665f70b9f85c0579b:email

```yaml
regex_id: 19a5063a0930d79665f70b9f85c0579b
schema_version: "1"
kind: intent_mismatch
corpus: RustPython
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/email/feedparser.py:40:16"
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

## usage_mismatch:19a5063a0930d79665f70b9f85c0579b:search

```yaml
regex_id: 19a5063a0930d79665f70b9f85c0579b
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/email/feedparser.py:40:16"
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

## usage_mismatch:1ba59bf8df1094cc53e19e453290e9ee:match

```yaml
regex_id: 1ba59bf8df1094cc53e19e453290e9ee
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:638:25"
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

## usage_mismatch:1e7fef548c581970119b47883a0164d5:search

```yaml
regex_id: 1e7fef548c581970119b47883a0164d5
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_smtplib.py:544:17"
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

## usage_mismatch:1f759fb23bf5b2d439c59765b257602e:search

```yaml
regex_id: 1f759fb23bf5b2d439c59765b257602e
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_smtplib.py:609:16"
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

## usage_mismatch:20c1f709d6c2cb15ffc1c36910e1aeb3:search

```yaml
regex_id: 20c1f709d6c2cb15ffc1c36910e1aeb3
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:809:26"
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

## usage_mismatch:21f12f043ce77adc71f9b7c23fbf8f43:search

```yaml
regex_id: 21f12f043ce77adc71f9b7c23fbf8f43
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/http/cookiejar.py:346:25"
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

## usage_mismatch:241c9f98a9dedc61d8cbd935312dba24:match

```yaml
regex_id: 241c9f98a9dedc61d8cbd935312dba24
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:646:25"
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

## usage_mismatch:2803b3ab2f8565eb16c261a1479865ce:search

```yaml
regex_id: 2803b3ab2f8565eb16c261a1479865ce
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/doctest.py:773:27"
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

## usage_mismatch:28993e373e104c3cd90ce324c90eb8db:match

```yaml
regex_id: 28993e373e104c3cd90ce324c90eb8db
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:650:25"
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

## usage_mismatch:2dc26c438b5793e221a24962e29233b2:search

```yaml
regex_id: 2dc26c438b5793e221a24962e29233b2
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/platform.py:1430:22"
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

## usage_mismatch:31650354bd320386689b6458168ac78e:match

```yaml
regex_id: 31650354bd320386689b6458168ac78e
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:643:26"
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

## usage_mismatch:354906e303d765c9dd99e98befc9b830:search

```yaml
regex_id: 354906e303d765c9dd99e98befc9b830
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:633:12"
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

## usage_mismatch:363671590349bbdb231f1873effddc98:search

```yaml
regex_id: 363671590349bbdb231f1873effddc98
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/doctest.py:804:17"
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

## usage_mismatch:37f0a4e06007f23566d50a747193f7c1:search

```yaml
regex_id: 37f0a4e06007f23566d50a747193f7c1
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_unittest/test_case.py:1540:46"
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

## usage_mismatch:3ac4f3082e55b9d222130e1d6c4ea784:match

```yaml
regex_id: 3ac4f3082e55b9d222130e1d6c4ea784
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:763:24"
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

## usage_mismatch:3d247ff9bc158d0ceb4d16e458e6df97:match

```yaml
regex_id: 3d247ff9bc158d0ceb4d16e458e6df97
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:748:25"
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

## usage_mismatch:3faf61fd5da188394716f03811daa26f:match

```yaml
regex_id: 3faf61fd5da188394716f03811daa26f
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:757:26"
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

## usage_mismatch:40cad4f89da0839aa2c8d1fb037be9b5:search

```yaml
regex_id: 40cad4f89da0839aa2c8d1fb037be9b5
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/http/cookiejar.py:135:14"
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

## usage_mismatch:42e781344b811178ccd22b473a539fbd:search

```yaml
regex_id: 42e781344b811178ccd22b473a539fbd
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/http/cookiejar.py:288:14"
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

## usage_mismatch:436e273e842effd1206ea8de3638b1c9:match

```yaml
regex_id: 436e273e842effd1206ea8de3638b1c9
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:715:26"
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

## usage_mismatch:442ff92c6efed789ce40b0820d198faf:match

```yaml
regex_id: 442ff92c6efed789ce40b0820d198faf
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:2521:25"
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

## usage_mismatch:4527fae1cd5208dfdedb76028b2e5cba:search

```yaml
regex_id: 4527fae1cd5208dfdedb76028b2e5cba
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/logging/__init__.py:482:15"
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

## usage_mismatch:457dccbae7979e03750dabd97077e006:search

```yaml
regex_id: 457dccbae7979e03750dabd97077e006
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/email/header.py:48:7"
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

## usage_mismatch:498151e4886ecf4a01e6d6657632079a:search

```yaml
regex_id: 498151e4886ecf4a01e6d6657632079a
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/crates/wasm/Lib/_microdistlib.py:9:21"
```

### Pattern

`^([\w\.*+-]+)\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:49c0ad2894c4c604714cdad711f88feb:match

```yaml
regex_id: 49c0ad2894c4c604714cdad711f88feb
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:764:24"
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

## usage_mismatch:4a5e875d2c403fa85bd02d3ec35e9214:search

```yaml
regex_id: 4a5e875d2c403fa85bd02d3ec35e9214
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/_pydecimal.py:6120:14"
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

## usage_mismatch:4a86e09a6121a84270a4491f23f81922:match

```yaml
regex_id: 4a86e09a6121a84270a4491f23f81922
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:742:26"
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

## usage_mismatch:4b711c0de51f79610679957653e0f4f9:search

```yaml
regex_id: 4b711c0de51f79610679957653e0f4f9
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_smtplib.py:148:19"
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

## usage_mismatch:4fd69f75020141a345a88c856db45b3e:match

```yaml
regex_id: 4fd69f75020141a345a88c856db45b3e
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:745:25"
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

## usage_mismatch:52e1e8ae6034d172f5271ed2eac8e046:match

```yaml
regex_id: 52e1e8ae6034d172f5271ed2eac8e046
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:2532:24"
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

## usage_mismatch:58ec84ba1a25793daca757f624264389:match

```yaml
regex_id: 58ec84ba1a25793daca757f624264389
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:741:26"
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

## usage_mismatch:5a39ad65e3d3c60758de83af775c6d12:match

```yaml
regex_id: 5a39ad65e3d3c60758de83af775c6d12
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:767:24"
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

## usage_mismatch:5b5f796c266a2d85de1a8c49a66c63a0:search

```yaml
regex_id: 5b5f796c266a2d85de1a8c49a66c63a0
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/logging/config.py:374:22"
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

## usage_mismatch:5b96a7d80ce285bc05a3e98f86ec44cf:search

```yaml
regex_id: 5b96a7d80ce285bc05a3e98f86ec44cf
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_smtplib.py:603:17"
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

## usage_mismatch:5be1ccb61ebdf4a58b5234c546446445:search

```yaml
regex_id: 5be1ccb61ebdf4a58b5234c546446445
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_regrtest.py:1424:16"
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

## usage_mismatch:5f1af181065227a2ec5b71fa4b5b32c1:search

```yaml
regex_id: 5f1af181065227a2ec5b71fa4b5b32c1
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:1834:18"
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

## usage_mismatch:60991676ade80f0c6841aff856ba05f0:match

```yaml
regex_id: 60991676ade80f0c6841aff856ba05f0
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:751:25"
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

## usage_mismatch:61b534de195ee8ecbbd8b4c6b7bd8c88:match

```yaml
regex_id: 61b534de195ee8ecbbd8b4c6b7bd8c88
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:740:26"
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

## usage_mismatch:636dff6a3f8b6ec35c596518da81ec6b:search

```yaml
regex_id: 636dff6a3f8b6ec35c596518da81ec6b
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/http/cookiejar.py:206:17"
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

## usage_mismatch:68966fba87c4b179eccfa3dc73610a88:match

```yaml
regex_id: 68966fba87c4b179eccfa3dc73610a88
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:2528:24"
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

## usage_mismatch:6a102e8d7d2a297bb949a7b4907bfb65:search

```yaml
regex_id: 6a102e8d7d2a297bb949a7b4907bfb65
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/http/cookiejar.py:1258:14"
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

## usage_mismatch:6a9457398b7ee1b8430fb11ce1da014f:search

```yaml
regex_id: 6a9457398b7ee1b8430fb11ce1da014f
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:811:26"
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

## usage_mismatch:6ab4b636aaeefea634c494feaf53098f:match

```yaml
regex_id: 6ab4b636aaeefea634c494feaf53098f
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:719:25"
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

## usage_mismatch:6baaea52629da80415181b6d532178c6:search

```yaml
regex_id: 6baaea52629da80415181b6d532178c6
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/pydoc.py:278:14"
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

## usage_mismatch:7048b0e7b1b4c955fbb8277155f0fac0:search

```yaml
regex_id: 7048b0e7b1b4c955fbb8277155f0fac0
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_pyrepl/test_pyrepl.py:1683:24"
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

## usage_mismatch:72f803138b978c2c320b659e7e9a4958:match

```yaml
regex_id: 72f803138b978c2c320b659e7e9a4958
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/idlelib/format.py:181:11"
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

## usage_mismatch:7377714fc10a0ba549efb99e3814feec:search

```yaml
regex_id: 7377714fc10a0ba549efb99e3814feec
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:807:25"
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

## usage_mismatch:7c2167d31fb78b9623e6aab7fd5f8b59:match

```yaml
regex_id: 7c2167d31fb78b9623e6aab7fd5f8b59
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:716:26"
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

## usage_mismatch:7e6ec65e73b9ead1f2447d0bc880cbe2:match

```yaml
regex_id: 7e6ec65e73b9ead1f2447d0bc880cbe2
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:766:24"
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

## usage_mismatch:7fb5f820f6d7c5a5101d5e8bd5e8ffee:search

```yaml
regex_id: 7fb5f820f6d7c5a5101d5e8bd5e8ffee
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/http/cookiejar.py:344:25"
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

## usage_mismatch:7fea72ae4f0eea577a45538622daaf9d:match

```yaml
regex_id: 7fea72ae4f0eea577a45538622daaf9d
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:713:25"
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

## usage_mismatch:85f060253b8ac666a7781474fa415128:search

```yaml
regex_id: 85f060253b8ac666a7781474fa415128
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/logging/config.py:377:18"
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

## usage_mismatch:88dce060a7f277406900126515efe8d3:search

```yaml
regex_id: 88dce060a7f277406900126515efe8d3
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/crates/wasm/Lib/_microdistlib.py:8:13"
```

### Pattern

`^([\w\.-]+)\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8955be6f2a67a41b62d7a354a2d8a808:match

```yaml
regex_id: 8955be6f2a67a41b62d7a354a2d8a808
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:2518:26"
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

## usage_mismatch:8b462e210822a6a0fbcf8111eecc768e:match

```yaml
regex_id: 8b462e210822a6a0fbcf8111eecc768e
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:752:25"
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

## usage_mismatch:8d27a5afd3ccd089df55bab4fcdfe569:search

```yaml
regex_id: 8d27a5afd3ccd089df55bab4fcdfe569
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/crates/wasm/Lib/_microdistlib.py:10:13"
```

### Pattern

`^(<=?|>=?|={2,3}|[~!]=)\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8e90f58b59206f260c152fd7a99cec8c:match

```yaml
regex_id: 8e90f58b59206f260c152fd7a99cec8c
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:642:26"
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

## usage_mismatch:90972c5986e987fabf7e08d47799fb32:search

```yaml
regex_id: 90972c5986e987fabf7e08d47799fb32
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_unittest/test_case.py:1602:16"
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

## usage_mismatch:90e14bf4f8d14208b1602658ddc1c8f7:match

```yaml
regex_id: 90e14bf4f8d14208b1602658ddc1c8f7
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:749:25"
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

## usage_mismatch:91f8e2d8eb6cfed39d9f96b8f47eecc6:match

```yaml
regex_id: 91f8e2d8eb6cfed39d9f96b8f47eecc6
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:711:25"
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

## usage_mismatch:9323bc43f2fb73dcf878f76d5a120368:match

```yaml
regex_id: 9323bc43f2fb73dcf878f76d5a120368
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:2522:25"
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

## usage_mismatch:93637b095f33e95b9eb1db8a76b1e5c1:match

```yaml
regex_id: 93637b095f33e95b9eb1db8a76b1e5c1
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:762:24"
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

## usage_mismatch:93a13d28e2528d05fa593ba5f3f1db54:search

```yaml
regex_id: 93a13d28e2528d05fa593ba5f3f1db54
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/urllib/request.py:268:15"
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

## usage_mismatch:9442d7376e7477e2bced5aba6537024f:match

```yaml
regex_id: 9442d7376e7477e2bced5aba6537024f
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:760:24"
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

## usage_mismatch:96204006ea9f2d552c0db3dc1af2b6c8:search

```yaml
regex_id: 96204006ea9f2d552c0db3dc1af2b6c8
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/idlelib/pyshell.py:1340:35"
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

## intent_mismatch:9b97f8282b7abb4fcf053ddea81a32b2:email

```yaml
regex_id: 9b97f8282b7abb4fcf053ddea81a32b2
schema_version: "1"
kind: intent_mismatch
corpus: RustPython
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/email/feedparser.py:37:11"
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

## usage_mismatch:9b97f8282b7abb4fcf053ddea81a32b2:search

```yaml
regex_id: 9b97f8282b7abb4fcf053ddea81a32b2
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/email/feedparser.py:37:11"
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

## usage_mismatch:9fbd9f856d8a1cf4466f373e3798fb89:search

```yaml
regex_id: 9fbd9f856d8a1cf4466f373e3798fb89
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_smtplib.py:491:17"
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

## usage_mismatch:a58c147341300bc40d50ed7fb5bcc581:match

```yaml
regex_id: a58c147341300bc40d50ed7fb5bcc581
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:717:25"
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

## usage_mismatch:a5d3dd57a2ec1ece8cd6fa2753f79d1e:search

```yaml
regex_id: a5d3dd57a2ec1ece8cd6fa2753f79d1e
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/http/cookiejar.py:345:25"
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

## usage_mismatch:a630dd86fe87726772040e691b055ce2:match

```yaml
regex_id: a630dd86fe87726772040e691b055ce2
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:2520:25"
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

## usage_mismatch:a638e5bce603a630005c84e6988628e5:match

```yaml
regex_id: a638e5bce603a630005c84e6988628e5
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:640:25"
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

## usage_mismatch:ad113560801190a8548727551da9be3e:search

```yaml
regex_id: ad113560801190a8548727551da9be3e
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_smtplib.py:672:17"
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

## usage_mismatch:ad48a040946ac7d04e856d6964328a2e:search

```yaml
regex_id: ad48a040946ac7d04e856d6964328a2e
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:808:25"
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

## usage_mismatch:ad5fd6d543b42e8b66a01f2ae50feabd:search

```yaml
regex_id: ad5fd6d543b42e8b66a01f2ae50feabd
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_pyrepl/test_pyrepl.py:1693:24"
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

## usage_mismatch:af08473cf254c794a63cb21a603f3cf0:match

```yaml
regex_id: af08473cf254c794a63cb21a603f3cf0
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:743:26"
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

## usage_mismatch:af5cede5883a6156a293221237113ee3:match

```yaml
regex_id: af5cede5883a6156a293221237113ee3
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:2524:26"
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

## usage_mismatch:b046389aff76631527b85b31d08aceff:match

```yaml
regex_id: b046389aff76631527b85b31d08aceff
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:747:25"
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

## usage_mismatch:b0adda6de3f2ad403ec058a83b90ae6a:search

```yaml
regex_id: b0adda6de3f2ad403ec058a83b90ae6a
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:2025:12"
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

## usage_mismatch:b24d74f201ddb57ac369a47452380bff:search

```yaml
regex_id: b24d74f201ddb57ac369a47452380bff
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/_pydecimal.py:6119:13"
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

## intent_mismatch:b4e814cd55bc9b81dce8ae45ff786d05:email

```yaml
regex_id: b4e814cd55bc9b81dce8ae45ff786d05
schema_version: "1"
kind: intent_mismatch
corpus: RustPython
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/email/generator.py:23:7"
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

## usage_mismatch:b4e814cd55bc9b81dce8ae45ff786d05:search

```yaml
regex_id: b4e814cd55bc9b81dce8ae45ff786d05
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/email/generator.py:23:7"
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

## usage_mismatch:b860cb188590b392a9c5c55cd6350128:match

```yaml
regex_id: b860cb188590b392a9c5c55cd6350128
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:2527:24"
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

## usage_mismatch:bbaa54251f03ef469ecc1d76bc033e92:match

```yaml
regex_id: bbaa54251f03ef469ecc1d76bc033e92
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:2517:26"
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

## usage_mismatch:bc6a234d67fa8b8aedfeaac25a2c57d8:search

```yaml
regex_id: bc6a234d67fa8b8aedfeaac25a2c57d8
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:1829:18"
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

## usage_mismatch:bd2633584dbd68f690a0adb40b15dd9f:search

```yaml
regex_id: bd2633584dbd68f690a0adb40b15dd9f
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/http/cookiejar.py:211:21"
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

## usage_mismatch:bf1f9c26edb2565ed988bac296545326:match

```yaml
regex_id: bf1f9c26edb2565ed988bac296545326
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:755:26"
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

## usage_mismatch:c075366c8091dc0377318565e75a4358:search

```yaml
regex_id: c075366c8091dc0377318565e75a4358
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/doctest.py:1498:30"
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

## usage_mismatch:c43436933ca8a8cd9548461c7fda2c26:search

```yaml
regex_id: c43436933ca8a8cd9548461c7fda2c26
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:810:25"
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

## usage_mismatch:c9ccd2b085ae1ecf16aa6546812cb006:search

```yaml
regex_id: c9ccd2b085ae1ecf16aa6546812cb006
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/logging/config.py:294:13"
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

## usage_mismatch:cb4d3ff2929ead63ed06527644b7616a:search

```yaml
regex_id: cb4d3ff2929ead63ed06527644b7616a
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/http/cookiejar.py:620:14"
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

## usage_mismatch:cfafeb0c96c623a3f222fbdf9d62917f:match

```yaml
regex_id: cfafeb0c96c623a3f222fbdf9d62917f
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:759:24"
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

## usage_mismatch:d08eda9b02c559de98469057c3de6744:search

```yaml
regex_id: d08eda9b02c559de98469057c3de6744
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/logging/config.py:378:20"
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

## usage_mismatch:d61c9a5ea820af28ef581b7c1629d191:search

```yaml
regex_id: d61c9a5ea820af28ef581b7c1629d191
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/doctest.py:655:27"
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

## usage_mismatch:d64303ce4acb79e995c3d93b5cb35430:match

```yaml
regex_id: d64303ce4acb79e995c3d93b5cb35430
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:2529:24"
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

## usage_mismatch:d7d0714da82206d2ba44a9ece293c18c:match

```yaml
regex_id: d7d0714da82206d2ba44a9ece293c18c
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:761:24"
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

## usage_mismatch:daad06fde1bbb6e2d97f7f89c04a8969:match

```yaml
regex_id: daad06fde1bbb6e2d97f7f89c04a8969
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:1745:29"
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

## usage_mismatch:de9ba7258d1774b217ab4b517ca33966:match

```yaml
regex_id: de9ba7258d1774b217ab4b517ca33966
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:2525:26"
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

## usage_mismatch:e018d9468469f3bfe73c76f65d81c528:match

```yaml
regex_id: e018d9468469f3bfe73c76f65d81c528
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:1754:30"
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

## usage_mismatch:e2b89cf82c3ffaa57b058d8f3b085e0b:search

```yaml
regex_id: e2b89cf82c3ffaa57b058d8f3b085e0b
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/logging/config.py:379:20"
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

## usage_mismatch:e4704e8273b97871279ec18e4cabd138:match

```yaml
regex_id: e4704e8273b97871279ec18e4cabd138
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:754:26"
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

## usage_mismatch:e6ecfa98f77dc535fd5fba31f7dddddb:match

```yaml
regex_id: e6ecfa98f77dc535fd5fba31f7dddddb
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:750:25"
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

## usage_mismatch:e9c053a1c5dd83268af4e693db0cd21e:match

```yaml
regex_id: e9c053a1c5dd83268af4e693db0cd21e
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:746:25"
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

## intent_mismatch:e9d00f4798db16508a39ced39a980cec:email

```yaml
regex_id: e9d00f4798db16508a39ced39a980cec
schema_version: "1"
kind: intent_mismatch
corpus: RustPython
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/email/header.py:35:7"
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

## usage_mismatch:ec75773a6358c74fe0259de9c7cf5c64:match

```yaml
regex_id: ec75773a6358c74fe0259de9c7cf5c64
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:2531:26"
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

## usage_mismatch:edcd22751544a05a33dd159904533076:search

```yaml
regex_id: edcd22751544a05a33dd159904533076
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:1446:28"
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

## usage_mismatch:f14ffbe37318dcb4e569cd83b44f77df:search

```yaml
regex_id: f14ffbe37318dcb4e569cd83b44f77df
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/http/cookiejar.py:209:13"
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

## usage_mismatch:f4020211d4a6ffef4f290f079f5f3464:search

```yaml
regex_id: f4020211d4a6ffef4f290f079f5f3464
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/email/utils.py:392:23"
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

## usage_mismatch:f60c2a0f93bcac9dc08751e1758f3b2f:search

```yaml
regex_id: f60c2a0f93bcac9dc08751e1758f3b2f
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/configparser.py:1374:16"
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

## usage_mismatch:f87fca5d87a8b49c365a2d5954f08483:search

```yaml
regex_id: f87fca5d87a8b49c365a2d5954f08483
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_smtplib.py:158:19"
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

## usage_mismatch:f945b4178df4fdb6e8d565cd3f52ec93:search

```yaml
regex_id: f945b4178df4fdb6e8d565cd3f52ec93
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/idlelib/pyshell.py:1341:35"
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

## usage_mismatch:fc90a1f106cbf0818c0a539e5aa77e77:match

```yaml
regex_id: fc90a1f106cbf0818c0a539e5aa77e77
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:648:25"
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

## usage_mismatch:fccd5e9ecf890f929045d65db92b294e:match

```yaml
regex_id: fccd5e9ecf890f929045d65db92b294e
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_re.py:644:25"
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

## usage_mismatch:fdc3af2a3bc1de63beff5877ab0159bc:search

```yaml
regex_id: fdc3af2a3bc1de63beff5877ab0159bc
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_smtplib.py:635:17"
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

## intent_mismatch:fe21aca315a12402d1622513b0d65ae7:email

```yaml
regex_id: fe21aca315a12402d1622513b0d65ae7
schema_version: "1"
kind: intent_mismatch
corpus: RustPython
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_email/test_email.py:5813:17"
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

## usage_mismatch:fe21aca315a12402d1622513b0d65ae7:search

```yaml
regex_id: fe21aca315a12402d1622513b0d65ae7
schema_version: "1"
kind: usage_mismatch
corpus: RustPython
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/RustPython/rules/Lib/test/test_email/test_email.py:5813:17"
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

## property:inventory:rc-shape1-injection-alphabet:rc-shape1-injection-alphabet

```yaml
regex_id: "inventory:rc-shape1-injection-alphabet"
schema_version: "1"
kind: property
corpus: RustPython
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
corpus: RustPython
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
corpus: RustPython
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
corpus: RustPython
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

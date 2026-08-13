---
schema_version: "1"
corpus: pyparallel
findings: 173
---

# pyparallel batch findings

## usage_mismatch:0099d18f27b30e42dd2981504aeab6b7:match

```yaml
regex_id: 0099d18f27b30e42dd2981504aeab6b7
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/lib2to3/pgen2/conv.py:71:17"
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

## usage_mismatch:019d01fa03d3b79049bd738d0fb11c9f:match

```yaml
regex_id: 019d01fa03d3b79049bd738d0fb11c9f
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:333:25"
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

## usage_mismatch:0272e1df5121d0e4ed392e8b5f8bb2f9:search

```yaml
regex_id: 0272e1df5121d0e4ed392e8b5f8bb2f9
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:385:25"
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

## usage_mismatch:06a6e5c920ad8d85cc7d473c9ad9293f:search

```yaml
regex_id: 06a6e5c920ad8d85cc7d473c9ad9293f
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/http/cookiejar.py:1217:14"
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

## usage_mismatch:08771dd9c75f98b919329215d6e3bbe0:search

```yaml
regex_id: 08771dd9c75f98b919329215d6e3bbe0
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/ipython-4.0.0-py3.3.egg/IPython/core/inputsplitter.py:107:22"
```

### Pattern

`.+\n\s*\n\s+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:08a7e5d75bed57f653e847dfbd8d5a3d:match

```yaml
regex_id: 08a7e5d75bed57f653e847dfbd8d5a3d
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:826:29"
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

## usage_mismatch:097930057945ad9e31961eaeb14a688d:search

```yaml
regex_id: 097930057945ad9e31961eaeb14a688d
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/http/cookiejar.py:589:14"
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

## usage_mismatch:0af16d83ab5d792e7357b1e901ada92c:search

```yaml
regex_id: 0af16d83ab5d792e7357b1e901ada92c
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/Cython-0.23.4-py3.3-win-amd64.egg/Cython/Compiler/Code.py:78:21"
```

### Pattern

` *(\w+) = (\1);\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0b6e8256b68f7a5d3415ad8a4c3a24b2:search

```yaml
regex_id: 0b6e8256b68f7a5d3415ad8a4c3a24b2
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/async/http/cookiejar.py:201:13"
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

## usage_mismatch:0fe8fafc2c44f71a278432800d048b02:search

```yaml
regex_id: 0fe8fafc2c44f71a278432800d048b02
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/ipython-4.0.0-py3.3.egg/IPython/core/inputsplitter.py:63:16"
```

### Pattern

`^([ \t\r\f\v]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:11e93651ff4130ca155ddde7c8bc1be5:match

```yaml
regex_id: 11e93651ff4130ca155ddde7c8bc1be5
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:344:28"
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

## usage_mismatch:13d7eca09427f08e44b916bb031ebd54:search

```yaml
regex_id: 13d7eca09427f08e44b916bb031ebd54
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/logging/config.py:364:20"
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

## usage_mismatch:14a03a529104ad07466d5d39683a5d80:search

```yaml
regex_id: 14a03a529104ad07466d5d39683a5d80
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/setup.py:772:25"
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

## usage_mismatch:1519c02b2f8f0d9b6c7598f453fefa3c:search

```yaml
regex_id: 1519c02b2f8f0d9b6c7598f453fefa3c
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/Cython-0.23.4-py3.3-win-amd64.egg/Cython/Compiler/Code.py:169:37"
```

### Pattern

`^\s*//.*|/\*[^*]*\*/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:154cf8a63b7586b94e3a561018262083:search

```yaml
regex_id: 154cf8a63b7586b94e3a561018262083
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/pygments-2.0.2-py3.3.egg/pygments/lexers/parsers.py:559:12"
```

### Pattern

`^\s*language\s*=\s*C\s*;`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:15e94923c6df99d2fb51892073e89f75:match

```yaml
regex_id: 15e94923c6df99d2fb51892073e89f75
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:340:25"
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

## usage_mismatch:17392b265b36787ae467fdb815579c4a:search

```yaml
regex_id: 17392b265b36787ae467fdb815579c4a
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/async/http/cookiejar.py:276:14"
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

## usage_mismatch:1778248fa89de8e42eec8e190e8642ac:search

```yaml
regex_id: 1778248fa89de8e42eec8e190e8642ac
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/pip-7.1.2-py3.3.egg/pip/compat/dictconfig.py:31:13"
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

## usage_mismatch:1838465b476820584f794fa5204075b7:match

```yaml
regex_id: 1838465b476820584f794fa5204075b7
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/pip-7.1.2-py3.3.egg/pip/req/req_install.py:1072:8"
```

### Pattern

`^(.+)(\[[^\]]+\])$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1928e73bd43cfb57232e7be4c9d7135e:match

```yaml
regex_id: 1928e73bd43cfb57232e7be4c9d7135e
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:351:28"
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

## usage_mismatch:1b3661dc48dac5b95115a413f35325d6:search

```yaml
regex_id: 1b3661dc48dac5b95115a413f35325d6
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/async/http/cookiejar.py:331:25"
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

## usage_mismatch:1b42cd05b0af3042dd7f6384e9486257:search

```yaml
regex_id: 1b42cd05b0af3042dd7f6384e9486257
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:565:32"
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

## usage_mismatch:1c328fa1967908665c89d8c36c5d251c:search

```yaml
regex_id: 1c328fa1967908665c89d8c36c5d251c
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:384:25"
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

## usage_mismatch:1eb269f30a047d956abe31028b9b775b:match

```yaml
regex_id: 1eb269f30a047d956abe31028b9b775b
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:331:25"
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

## usage_mismatch:1f2631a3d61f5cf966e86f24021397ca:match

```yaml
regex_id: 1f2631a3d61f5cf966e86f24021397ca
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:288:25"
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

## usage_mismatch:1f62316873a9274096768bf47aa80ebb:search

```yaml
regex_id: 1f62316873a9274096768bf47aa80ebb
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/urllib/parse.py:943:21"
```

### Pattern

`^(.*)\?([^?]*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:259b10d3948f7b6b41a6cdc6abb0479a:search

```yaml
regex_id: 259b10d3948f7b6b41a6cdc6abb0479a
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/pygments-2.0.2-py3.3.egg/pygments/lexers/sql.py:232:18"
```

### Pattern

`(\s*)(\\.+?)(\s+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:25fac343b76a52cf3e0e5da663b569ed:search

```yaml
regex_id: 25fac343b76a52cf3e0e5da663b569ed
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/Cython-0.23.4-py3.3-win-amd64.egg/Cython/Tempita/_tempita.py:52:9"
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

## usage_mismatch:282b7a24a07f82f9045941ec0baae941:search

```yaml
regex_id: 282b7a24a07f82f9045941ec0baae941
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/http/cookiejar.py:332:25"
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

## usage_mismatch:2b8ef08859f14ddcb22eb3767cac48b5:search

```yaml
regex_id: 2b8ef08859f14ddcb22eb3767cac48b5
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:383:25"
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

## usage_mismatch:2c9eb6a900030cf0864710917a56cfae:search

```yaml
regex_id: 2c9eb6a900030cf0864710917a56cfae
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/async/http/cookiejar.py:1217:14"
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

## usage_mismatch:2cac16395bf05a6bbea71a09f2dfe0d4:search

```yaml
regex_id: 2cac16395bf05a6bbea71a09f2dfe0d4
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/textwrap.py:338:22"
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

## usage_mismatch:2cd1f5e21106dafeb3add851c834f069:search

```yaml
regex_id: 2cd1f5e21106dafeb3add851c834f069
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/pygments-2.0.2-py3.3.egg/pygments/lexers/parsers.py:700:12"
```

### Pattern

`^\s*language\s*=\s*ActionScript\s*;`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2de12177af2887625e93f619cb68265a:search

```yaml
regex_id: 2de12177af2887625e93f619cb68265a
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/pygments-2.0.2-py3.3.egg/pygments/lexers/parsers.py:599:12"
```

### Pattern

`^\s*language\s*=\s*CSharp2\s*;`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:31e1c70f3723add3fbcf60fb6db07ae0:match

```yaml
regex_id: 31e1c70f3723add3fbcf60fb6db07ae0
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:353:25"
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

## usage_mismatch:31f3582c90e9739d8fff4f10c84a5a18:search

```yaml
regex_id: 31f3582c90e9739d8fff4f10c84a5a18
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/doctest.py:1387:30"
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

## usage_mismatch:331b28e17eb752358c199efeb9ebf71c:search

```yaml
regex_id: 331b28e17eb752358c199efeb9ebf71c
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/urllib/parse.py:906:20"
```

### Pattern

`^(.*):([0-9]*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3637c8a53cb9b73799289ddd6ac4ed05:search

```yaml
regex_id: 3637c8a53cb9b73799289ddd6ac4ed05
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/pip-7.1.2-py3.3.egg/pip/req/req_install.py:1018:12"
```

### Pattern

`^(.*?)(?:-dev|-\d.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:38a57c93b91f06af1a7dcdf9bec87b1d:search

```yaml
regex_id: 38a57c93b91f06af1a7dcdf9bec87b1d
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/ipython-4.0.0-py3.3.egg/IPython/core/inputsplitter.py:106:21"
```

### Pattern

`\n\s*\n\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3a4d593fb6474e26dac716fc9882dded:match

```yaml
regex_id: 3a4d593fb6474e26dac716fc9882dded
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:342:25"
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

## intent_mismatch:3f45b1ab827b66612a45216be02b81e1:email

```yaml
regex_id: 3f45b1ab827b66612a45216be02b81e1
schema_version: "1"
kind: intent_mismatch
corpus: pyparallel
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/email/feedparser.py:36:11"
```

### Pattern

`^(From |[\041-\071\073-\176]{1,}:|[\t ])`

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

## usage_mismatch:3f45b1ab827b66612a45216be02b81e1:search

```yaml
regex_id: 3f45b1ab827b66612a45216be02b81e1
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/email/feedparser.py:36:11"
```

### Pattern

`^(From |[\041-\071\073-\176]{1,}:|[\t ])`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:401964379a2cea55fb6f93283791ea0f:search

```yaml
regex_id: 401964379a2cea55fb6f93283791ea0f
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/async/http/cookiejar.py:589:14"
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

## usage_mismatch:420406f51862a7b0f3862c49fdad7427:search

```yaml
regex_id: 420406f51862a7b0f3862c49fdad7427
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/logging/config.py:360:22"
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

## usage_mismatch:43a0a9a8b4d206a5500ea98ecfc90f40:search

```yaml
regex_id: 43a0a9a8b4d206a5500ea98ecfc90f40
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/pip-7.1.2-py3.3.egg/pip/compat/dictconfig.py:151:18"
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

## usage_mismatch:450b0e846309285ca22ba8e411cb11c1:search

```yaml
regex_id: 450b0e846309285ca22ba8e411cb11c1
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Tools/scripts/texi2html.py:74:9"
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

## usage_mismatch:49b3d36114e532ce0f3943fe146250f6:search

```yaml
regex_id: 49b3d36114e532ce0f3943fe146250f6
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/http/cookiejar.py:130:14"
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

## usage_mismatch:4b9af293dfa5c80b65e46db935b9cfb4:search

```yaml
regex_id: 4b9af293dfa5c80b65e46db935b9cfb4
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/Cython-0.23.4-py3.3-win-amd64.egg/Cython/Tempita/_tempita.py:695:21"
```

### Pattern

`^[\t ]*\n`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4c5049c7da4a29a2a58801f1f744b08b:match

```yaml
regex_id: 4c5049c7da4a29a2a58801f1f744b08b
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:348:28"
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

## usage_mismatch:4c60121a9466735fa9b8fc543505e10e:search

```yaml
regex_id: 4c60121a9466735fa9b8fc543505e10e
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/ipython-4.0.0-py3.3.egg/IPython/core/inputtransformer.py:456:16"
```

### Pattern

`^(>>>|\.\.\.)( |$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4c96b284d8648c5dff8063eef95210d5:search

```yaml
regex_id: 4c96b284d8648c5dff8063eef95210d5
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/http/cookiejar.py:198:17"
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

## usage_mismatch:4e2565c0eff3bf572bf3ed5d537b28fe:match

```yaml
regex_id: 4e2565c0eff3bf572bf3ed5d537b28fe
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:278:25"
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

## usage_mismatch:4f3ee324552e0b1afc758aedafe1eabd:search

```yaml
regex_id: 4f3ee324552e0b1afc758aedafe1eabd
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Tools/scripts/mailerdaemon.py:94:4"
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

## usage_mismatch:5451c79e7858feddb2e48431eea265af:search

```yaml
regex_id: 5451c79e7858feddb2e48431eea265af
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/urllib/parse.py:924:21"
```

### Pattern

`^(.*):(.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:580b21ab78afa723f53567dd87f615d5:search

```yaml
regex_id: 580b21ab78afa723f53567dd87f615d5
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_smtplib.py:384:17"
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

## usage_mismatch:5a610bfecf677045ee02bd0c30ae8881:search

```yaml
regex_id: 5a610bfecf677045ee02bd0c30ae8881
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/urllib/parse.py:893:22"
```

### Pattern

`^([^:]*):(.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5b2e52a4b5e1ebf40d2a20a961b5e20a:match

```yaml
regex_id: 5b2e52a4b5e1ebf40d2a20a961b5e20a
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:310:25"
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

## usage_mismatch:5d25e5c1a9e1112fcb4cded1c55e608c:search

```yaml
regex_id: 5d25e5c1a9e1112fcb4cded1c55e608c
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_smtplib.py:437:17"
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

## usage_mismatch:5d3a43acac399311a24cc985d9bee417:search

```yaml
regex_id: 5d3a43acac399311a24cc985d9bee417
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/urllib/request.py:239:15"
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

## usage_mismatch:5e39ff8dab407c751a0bca8be0fb6776:match

```yaml
regex_id: 5e39ff8dab407c751a0bca8be0fb6776
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:308:25"
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

## usage_mismatch:5f1817c6d3e3b6becfa78c41656667c6:match

```yaml
regex_id: 5f1817c6d3e3b6becfa78c41656667c6
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:346:28"
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

## usage_mismatch:60633d71e0332584327a8548aadbb5ba:search

```yaml
regex_id: 60633d71e0332584327a8548aadbb5ba
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/ipython-4.0.0-py3.3.egg/IPython/utils/text.py:283:14"
```

### Pattern

`^`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:60ee8131d693fd1cb50c188086677965:match

```yaml
regex_id: 60ee8131d693fd1cb50c188086677965
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:332:25"
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

## usage_mismatch:635b62c7322c58ff936ce9e40a35884b:search

```yaml
regex_id: 635b62c7322c58ff936ce9e40a35884b
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/pygments-2.0.2-py3.3.egg/pygments/lexers/parsers.py:619:12"
```

### Pattern

`^\s*language\s*=\s*Python\s*;`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:653b3a6c65bbe0740443fcf2566dafc7:search

```yaml
regex_id: 653b3a6c65bbe0740443fcf2566dafc7
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Tools/scripts/texi2html.py:1598:19"
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

## usage_mismatch:6653cb53ab14252b3c4461900caba49f:search

```yaml
regex_id: 6653cb53ab14252b3c4461900caba49f
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/ipython-4.0.0-py3.3.egg/IPython/utils/text.py:355:13"
```

### Pattern

`\\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:66eaeb50a1d0a21f699fd7e4392f4ab9:match

```yaml
regex_id: 66eaeb50a1d0a21f699fd7e4392f4ab9
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:281:25"
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

## usage_mismatch:66ee643db3fed9e2b42cd7cabed7af78:match

```yaml
regex_id: 66ee643db3fed9e2b42cd7cabed7af78
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:337:25"
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

## usage_mismatch:671cb5366022a2bd774db2afd391d0b4:search

```yaml
regex_id: 671cb5366022a2bd774db2afd391d0b4
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/ipython-4.0.0-py3.3.egg/IPython/core/inputtransformer.py:457:17"
```

### Pattern

`^>>>( |$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:687f18efbb1f15495f1182aeb6c75866:search

```yaml
regex_id: 687f18efbb1f15495f1182aeb6c75866
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/doctest.py:759:17"
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

## usage_mismatch:6909c5f386459971c80bd54020477c1e:match

```yaml
regex_id: 6909c5f386459971c80bd54020477c1e
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:336:25"
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

## usage_mismatch:6b82e343faad6390c77349ff27d78e87:search

```yaml
regex_id: 6b82e343faad6390c77349ff27d78e87
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/Cython-0.23.4-py3.3-win-amd64.egg/Cython/Compiler/Code.py:165:37"
```

### Pattern

`^\s*#.*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6baa78955f096a3cb5cd0e9139940814:match

```yaml
regex_id: 6baa78955f096a3cb5cd0e9139940814
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:286:25"
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

## usage_mismatch:6c46a9ac6be52500913f7001650f1be5:search

```yaml
regex_id: 6c46a9ac6be52500913f7001650f1be5
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/Cython-0.23.4-py3.3-win-amd64.egg/Cython/Compiler/Code.py:170:29"
```

### Pattern

`\s+(\\?)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6fe17e4fa7525a6dea6e4807b45b0809:search

```yaml
regex_id: 6fe17e4fa7525a6dea6e4807b45b0809
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/http/cookiejar.py:504:10"
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

## usage_mismatch:71534405e52ba5a6244fdcc7ddaf2473:search

```yaml
regex_id: 71534405e52ba5a6244fdcc7ddaf2473
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/http/cookiejar.py:437:23"
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

## usage_mismatch:71a046b9464ddcf407ca8808b60237d6:search

```yaml
regex_id: 71a046b9464ddcf407ca8808b60237d6
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/async/http/cookiejar.py:130:14"
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

## usage_mismatch:76188297cb822ced299c119fc4b645f1:match

```yaml
regex_id: 76188297cb822ced299c119fc4b645f1
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:284:25"
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

## usage_mismatch:7709b660c839fea0cbce6964b64bf10f:match

```yaml
regex_id: 7709b660c839fea0cbce6964b64bf10f
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:835:30"
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

## usage_mismatch:79f4c13d05591c8276827d975e574234:match

```yaml
regex_id: 79f4c13d05591c8276827d975e574234
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:306:25"
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

## usage_mismatch:7c070adc89e0aa579f5d393a0aa0bafe:search

```yaml
regex_id: 7c070adc89e0aa579f5d393a0aa0bafe
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/async/http/cookiejar.py:332:25"
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

## usage_mismatch:7d3ba89569456bd590f80a6cd7fba8cf:search

```yaml
regex_id: 7d3ba89569456bd590f80a6cd7fba8cf
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/urllib/parse.py:864:20"
```

### Pattern

`^//([^/?]*)(.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7dc043b0838e8cc7a4e3bd3746b16036:match

```yaml
regex_id: 7dc043b0838e8cc7a4e3bd3746b16036
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:335:25"
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

## usage_mismatch:7de60c4e4bffe389d7cf2c60b021a4f3:search

```yaml
regex_id: 7de60c4e4bffe389d7cf2c60b021a4f3
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/http/cookiejar.py:276:14"
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

## usage_mismatch:80a0d627f6d70ad2b6d6527fb4e210c4:search

```yaml
regex_id: 80a0d627f6d70ad2b6d6527fb4e210c4
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Tools/scripts/texi2html.py:81:9"
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

## usage_mismatch:838d7f3cbd5d6c499449bd5bcea01b15:search

```yaml
regex_id: 838d7f3cbd5d6c499449bd5bcea01b15
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_smtplib.py:411:17"
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

## usage_mismatch:848b65a7931dbe6884a47ef30f120128:search

```yaml
regex_id: 848b65a7931dbe6884a47ef30f120128
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/urllib/parse.py:850:20"
```

### Pattern

`^([^/:]+):`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:85e02285e71a4f1e197b2bc70b7d5db0:search

```yaml
regex_id: 85e02285e71a4f1e197b2bc70b7d5db0
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/async/http/cookiejar.py:203:21"
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

## usage_mismatch:8672089c3f69bf0264ef0c3c10c5529a:search

```yaml
regex_id: 8672089c3f69bf0264ef0c3c10c5529a
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_smtplib.py:340:17"
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

## usage_mismatch:868e11e5271d8619d9c14820fc1cfcaa:match

```yaml
regex_id: 868e11e5271d8619d9c14820fc1cfcaa
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/pygments-2.0.2-py3.3.egg/pygments/lexers/perl.py:595:15"
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

## usage_mismatch:86bd738fa3808eac8b8293c99e575704:search

```yaml
regex_id: 86bd738fa3808eac8b8293c99e575704
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/ipython-4.0.0-py3.3.egg/IPython/utils/text.py:338:16"
```

### Pattern

`^(\s+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:875bb221bd1ff62991da791327de6ffc:match

```yaml
regex_id: 875bb221bd1ff62991da791327de6ffc
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:349:28"
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

## usage_mismatch:87ea001294b606d0d110448636863db0:match

```yaml
regex_id: 87ea001294b606d0d110448636863db0
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:304:25"
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

## usage_mismatch:88d734d9447a1f2de9996ac7177bec94:match

```yaml
regex_id: 88d734d9447a1f2de9996ac7177bec94
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:341:25"
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

## usage_mismatch:8925580dcb15619e39268ca651f0264f:search

```yaml
regex_id: 8925580dcb15619e39268ca651f0264f
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/logging/config.py:264:13"
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

## usage_mismatch:89a8ba2094cb80fda4a63aab68e25c70:search

```yaml
regex_id: 89a8ba2094cb80fda4a63aab68e25c70
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:881:18"
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

## usage_mismatch:89cc073b7a1457c664610b39e5ac6879:search

```yaml
regex_id: 89cc073b7a1457c664610b39e5ac6879
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/ipython-4.0.0-py3.3.egg/IPython/core/inputtransformer.py:464:16"
```

### Pattern

`^(In \[\d+\]: |\s*\.{3,}: ?)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8afe8f2d02ee2a8bffb199a5b25f854e:search

```yaml
regex_id: 8afe8f2d02ee2a8bffb199a5b25f854e
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/logging/config.py:365:20"
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

## usage_mismatch:8ccd432024b687d880eb8c9d6e425266:search

```yaml
regex_id: 8ccd432024b687d880eb8c9d6e425266
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/http/cookiejar.py:203:21"
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

## usage_mismatch:8ead6976b3db53b566cf466eb91f7916:match

```yaml
regex_id: 8ead6976b3db53b566cf466eb91f7916
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:325:25"
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

## usage_mismatch:8f9386a7b38345c9847d7481a6f534dc:search

```yaml
regex_id: 8f9386a7b38345c9847d7481a6f534dc
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/ipython-4.0.0-py3.3.egg/IPython/core/completer.py:640:32"
```

### Pattern

`^[\w|\s.]+\(([^)]*)\).*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8fd13398f0e49873c18a2b43743b2a95:search

```yaml
regex_id: 8fd13398f0e49873c18a2b43743b2a95
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/urllib/parse.py:973:21"
```

### Pattern

`^([^=]*)=(.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8fd913ca3a4257c29ac2a941a09e4f42:search

```yaml
regex_id: 8fd913ca3a4257c29ac2a941a09e4f42
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/pygments-2.0.2-py3.3.egg/pygments/lexers/parsers.py:516:15"
```

### Pattern

`^\s*grammar\s+[a-zA-Z0-9]+\s*;`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:90056d9b235544de1b2e06e53a0329b0:search

```yaml
regex_id: 90056d9b235544de1b2e06e53a0329b0
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/http/cookiejar.py:331:25"
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

## usage_mismatch:91f5b800a35ebbb51fed7eb25e55a747:search

```yaml
regex_id: 91f5b800a35ebbb51fed7eb25e55a747
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/async/http/cookiejar.py:330:25"
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

## usage_mismatch:943d848921f4991453681ccfbfda69ef:search

```yaml
regex_id: 943d848921f4991453681ccfbfda69ef
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/urllib/parse.py:955:19"
```

### Pattern

`^(.*)#([^#]*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:97617181d8ef25c989e3d767e72ed903:match

```yaml
regex_id: 97617181d8ef25c989e3d767e72ed903
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:327:25"
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

## usage_mismatch:978cc44079622c70a28e083729d10669:search

```yaml
regex_id: 978cc44079622c70a28e083729d10669
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Tools/scripts/mailerdaemon.py:92:4"
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

## usage_mismatch:98f91212bb00a9bb2aeace1de418b2f4:match

```yaml
regex_id: 98f91212bb00a9bb2aeace1de418b2f4
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:307:25"
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

## usage_mismatch:99a47f77bbc1e88d8b5c681af79bce84:match

```yaml
regex_id: 99a47f77bbc1e88d8b5c681af79bce84
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:350:28"
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

## usage_mismatch:9af3ded64960e953d29068077f5de10a:search

```yaml
regex_id: 9af3ded64960e953d29068077f5de10a
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/pip-7.1.2-py3.3.egg/pip/compat/dictconfig.py:150:19"
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

## usage_mismatch:9d7284a3487af755e6728507f77592e3:search

```yaml
regex_id: 9d7284a3487af755e6728507f77592e3
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:876:18"
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

## usage_mismatch:9d7c4237afd237ab64960e823653711a:match

```yaml
regex_id: 9d7c4237afd237ab64960e823653711a
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:345:28"
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

## usage_mismatch:9e2500b3ee3bde3efcb8a9a821e5370d:search

```yaml
regex_id: 9e2500b3ee3bde3efcb8a9a821e5370d
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Tools/scripts/mailerdaemon.py:168:10"
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

## usage_mismatch:9e4fe98ece7f00ddff074330b2dbe876:search

```yaml
regex_id: 9e4fe98ece7f00ddff074330b2dbe876
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/async/http/cookiejar.py:437:23"
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

## usage_mismatch:a2cab8221809353108c0b3779081eb2d:search

```yaml
regex_id: a2cab8221809353108c0b3779081eb2d
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/logging/config.py:363:18"
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

## usage_mismatch:a32bde044f738bd4a89c3f9929f3ef5c:search

```yaml
regex_id: a32bde044f738bd4a89c3f9929f3ef5c
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/ipython-4.0.0-py3.3.egg/IPython/core/completer.py:887:15"
```

### Pattern

`\w+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a89fedfea048e6c6bb55656fa25b4355:search

```yaml
regex_id: a89fedfea048e6c6bb55656fa25b4355
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/urllib/parse.py:881:20"
```

### Pattern

`^(.*)@(.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a9a43a554ee4d49ae278a38aef1b2d14:search

```yaml
regex_id: a9a43a554ee4d49ae278a38aef1b2d14
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:391:25"
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

## usage_mismatch:ab2cf56706f1c1fad8746df94f52ab21:search

```yaml
regex_id: ab2cf56706f1c1fad8746df94f52ab21
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/ipython-4.0.0-py3.3.egg/IPython/core/inputtransformer.py:475:15"
```

### Pattern

`^[ \t]+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:abdb2d1dee57b318b5f8422ea4b0ea45:search

```yaml
regex_id: abdb2d1dee57b318b5f8422ea4b0ea45
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/Cython-0.23.4-py3.3-win-amd64.egg/Cython/Tempita/_tempita.py:694:22"
```

### Pattern

`\n\r?[\t ]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:aea16541e4e1f416e0f11f306a8b0c45:search

```yaml
regex_id: aea16541e4e1f416e0f11f306a8b0c45
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/doctest.py:610:27"
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

## usage_mismatch:b01a1b525284d31a19f65b5783b0ac0f:match

```yaml
regex_id: b01a1b525284d31a19f65b5783b0ac0f
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:302:25"
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

## usage_mismatch:b15269510e123f7d92ab32efee76d512:search

```yaml
regex_id: b15269510e123f7d92ab32efee76d512
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_smtplib.py:500:17"
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

## usage_mismatch:b2cd1fd2ddaf410b55e00415052dc518:search

```yaml
regex_id: b2cd1fd2ddaf410b55e00415052dc518
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/pip-7.1.2-py3.3.egg/pip/compat/dictconfig.py:153:20"
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

## usage_mismatch:b5b62801f09489a17ecaa9e9f94fa58a:search

```yaml
regex_id: b5b62801f09489a17ecaa9e9f94fa58a
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/pygments-2.0.2-py3.3.egg/pygments/lexers/sql.py:229:12"
```

### Pattern

`^(\S.*?)??[=\-\(\$\'\"][#>]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b73138d89608876087ca68dbe3ee4835:search

```yaml
regex_id: b73138d89608876087ca68dbe3ee4835
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/Cython-0.23.4-py3.3-win-amd64.egg/Cython/Tempita/_tempita.py:692:15"
```

### Pattern

`^(?:if |elif |for |def |inherit |default |py:)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b781b1cb2a89effbbcb2e5cdea5b0388:search

```yaml
regex_id: b781b1cb2a89effbbcb2e5cdea5b0388
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/ipython-4.0.0-py3.3.egg/IPython/utils/text.py:281:14"
```

### Pattern

`^\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b87a48a7d2a636ddb843a74ff4522a6b:search

```yaml
regex_id: b87a48a7d2a636ddb843a74ff4522a6b
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Tools/scripts/h2py.py:32:12"
```

### Pattern

`^[	 ]*#[	 ]*include[	 ]+<([a-zA-Z0-9_/\.]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b94abea0562e511cde40f019b09e0496:match

```yaml
regex_id: b94abea0562e511cde40f019b09e0496
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:328:25"
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

## usage_mismatch:bab9b9e85c462d2ff8dd4d01db73dfb2:search

```yaml
regex_id: bab9b9e85c462d2ff8dd4d01db73dfb2
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/async/http/cookiejar.py:504:10"
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

## usage_mismatch:be4aabc89f6b2d5575791fd7a54fe52c:match

```yaml
regex_id: be4aabc89f6b2d5575791fd7a54fe52c
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:354:28"
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

## usage_mismatch:c17fface4b51f61d33d806791dddd5d5:match

```yaml
regex_id: c17fface4b51f61d33d806791dddd5d5
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:330:25"
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

## usage_mismatch:c1a1043d31a24d2c4c6e44ec4f7b11b9:search

```yaml
regex_id: c1a1043d31a24d2c4c6e44ec4f7b11b9
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:390:25"
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

## usage_mismatch:c3efeaac77f634308ded016603882dd5:search

```yaml
regex_id: c3efeaac77f634308ded016603882dd5
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/Cython-0.23.4-py3.3-win-amd64.egg/Cython/Debugger/libpython.py:2034:23"
```

### Pattern

`^Value returned is \$\d+ = (.*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c79a73353e8617f393aea2a3ab8a848c:search

```yaml
regex_id: c79a73353e8617f393aea2a3ab8a848c
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_smtplib.py:443:16"
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

## usage_mismatch:c8c64bf9c97d62fb7416f0c62d3b15b6:match

```yaml
regex_id: c8c64bf9c97d62fb7416f0c62d3b15b6
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/pip-7.1.2-py3.3.egg/pip/req/req_install.py:48:8"
```

### Pattern

`^(.+)(\[[^\]]+\])$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c8fd606ec2b1daa718d96dc8726f705c:search

```yaml
regex_id: c8fd606ec2b1daa718d96dc8726f705c
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Tools/scripts/h2py.py:28:10"
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

## usage_mismatch:ca08d296ae7742cd189787039d4bc05e:search

```yaml
regex_id: ca08d296ae7742cd189787039d4bc05e
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/http/cookiejar.py:1219:15"
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

## usage_mismatch:cdb13e20f8d386f7e66d46f3d7cb2849:match

```yaml
regex_id: cdb13e20f8d386f7e66d46f3d7cb2849
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:347:28"
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

## usage_mismatch:d16e6059256c4430a28b49c0d33c4145:search

```yaml
regex_id: d16e6059256c4430a28b49c0d33c4145
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/numpy-1.10.0.dev0_046311a-py3.3-win-amd64.egg/numpy/distutils/misc_util.py:559:21"
```

### Pattern

`(?:[~#]|\.py[co]|\.o)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d2c79f728aa95be6fb428da97895ae1f:search

```yaml
regex_id: d2c79f728aa95be6fb428da97895ae1f
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/http/cookiejar.py:330:25"
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

## usage_mismatch:d3433dcc8b6f688e96bf6a395816632d:search

```yaml
regex_id: d3433dcc8b6f688e96bf6a395816632d
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:985:12"
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

## usage_mismatch:d543d12de9f8fcb7cda9b86bbfdf4ffc:search

```yaml
regex_id: d543d12de9f8fcb7cda9b86bbfdf4ffc
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Tools/scripts/h2py.py:26:11"
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

## usage_mismatch:d693dbbe9f6485db07d8365b449d7481:search

```yaml
regex_id: d693dbbe9f6485db07d8365b449d7481
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/pip-7.1.2-py3.3.egg/pip/compat/dictconfig.py:148:22"
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

## usage_mismatch:d7c6eba90aa50ad33a661ba305d36fde:search

```yaml
regex_id: d7c6eba90aa50ad33a661ba305d36fde
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/logging/config.py:362:19"
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

## usage_mismatch:d8d3aa03726a9fe9514e0523ce0149bb:match

```yaml
regex_id: d8d3aa03726a9fe9514e0523ce0149bb
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:280:25"
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

## usage_mismatch:db7d3606fec05df28732d76f5f8e5ccc:search

```yaml
regex_id: db7d3606fec05df28732d76f5f8e5ccc
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/ipython-4.0.0-py3.3.egg/IPython/core/inputsplitter.py:67:18"
```

### Pattern

`^\s*\#`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dddcacad8aeb32c9ec4d909e6162377f:match

```yaml
regex_id: dddcacad8aeb32c9ec4d909e6162377f
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:276:25"
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

## usage_mismatch:deb7df05a82205f110d717fdeef0e46a:search

```yaml
regex_id: deb7df05a82205f110d717fdeef0e46a
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/pygments-2.0.2-py3.3.egg/pygments/lexers/parsers.py:679:12"
```

### Pattern

`^\s*language\s*=\s*Perl5\s*;`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:df32d612221162acf01c1d20e0bc9d7a:match

```yaml
regex_id: df32d612221162acf01c1d20e0bc9d7a
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:339:25"
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

## usage_mismatch:e06ca3bf58eda916e829ee78c299ea85:search

```yaml
regex_id: e06ca3bf58eda916e829ee78c299ea85
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/async/http/cookiejar.py:1219:15"
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

## usage_mismatch:e08ed269983cbe6b43b7a07d7a5120c0:search

```yaml
regex_id: e08ed269983cbe6b43b7a07d7a5120c0
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/pygments-2.0.2-py3.3.egg/pygments/lexers/sql.py:231:17"
```

### Pattern

`;\s*(--.*?)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e0bcf6bfdcd838e0f40a0417ec82217b:search

```yaml
regex_id: e0bcf6bfdcd838e0f40a0417ec82217b
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/async/http/cookiejar.py:198:17"
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

## usage_mismatch:e313f428e24ee9a0da426e354c02beb1:search

```yaml
regex_id: e313f428e24ee9a0da426e354c02beb1
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/http/cookiejar.py:201:13"
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

## usage_mismatch:e550e91a454c29e8adb0fb244df0dfc7:search

```yaml
regex_id: e550e91a454c29e8adb0fb244df0dfc7
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/doctest.py:728:27"
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

## usage_mismatch:e5944bd558b1c1ced6718620653816a4:search

```yaml
regex_id: e5944bd558b1c1ced6718620653816a4
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/pygments-2.0.2-py3.3.egg/pygments/lexers/parsers.py:659:12"
```

### Pattern

`^\s*language\s*=\s*Ruby\s*;`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e5fbbbb89b921d35608ba233033ea44f:search

```yaml
regex_id: e5fbbbb89b921d35608ba233033ea44f
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/pygments-2.0.2-py3.3.egg/pygments/lexers/parsers.py:579:12"
```

### Pattern

`^\s*language\s*=\s*ObjC\s*;`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e729f6dc531633b02baffef48b38277d:search

```yaml
regex_id: e729f6dc531633b02baffef48b38277d
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_smtplib.py:466:17"
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

## usage_mismatch:e8861827ad4d7210601106b41f43ac0f:search

```yaml
regex_id: e8861827ad4d7210601106b41f43ac0f
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/numpy-1.10.0.dev0_046311a-py3.3-win-amd64.egg/numpy/distutils/misc_util.py:546:21"
```

### Pattern

`(?:[~#]|\.py[co]|\.o)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:eb11f69368a14d00c84c72c73d70c17d:match

```yaml
regex_id: eb11f69368a14d00c84c72c73d70c17d
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:282:25"
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

## usage_mismatch:ef3eb86e352065335e42612455aee1ad:search

```yaml
regex_id: ef3eb86e352065335e42612455aee1ad
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:392:25"
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

## usage_mismatch:f5530bd9529ef27e4eaf653ad6291b5f:match

```yaml
regex_id: f5530bd9529ef27e4eaf653ad6291b5f
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:326:25"
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

## usage_mismatch:f5bd98a08804314412dc7eb0c477ede9:match

```yaml
regex_id: f5bd98a08804314412dc7eb0c477ede9
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/test/test_re.py:334:25"
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

## usage_mismatch:f8ea4daf8a1b693d75ca5cc1f49b2b7b:search

```yaml
regex_id: f8ea4daf8a1b693d75ca5cc1f49b2b7b
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Tools/scripts/mailerdaemon.py:96:20"
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

## usage_mismatch:f98c9d4acd5ff6139afbdeefcef790fc:search

```yaml
regex_id: f98c9d4acd5ff6139afbdeefcef790fc
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/pip-7.1.2-py3.3.egg/pip/compat/dictconfig.py:152:20"
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

## usage_mismatch:fac563e5084bfd49900a6dd87228ab2a:search

```yaml
regex_id: fac563e5084bfd49900a6dd87228ab2a
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Tools/scripts/texi2html.py:73:9"
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

## intent_mismatch:fd1acb0c670df35856bf492b76c7d4d7:url

```yaml
regex_id: fd1acb0c670df35856bf492b76c7d4d7
schema_version: "1"
kind: intent_mismatch
corpus: pyparallel
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/pip-7.1.2-py3.3.egg/pip/vcs/subversion.py:19:23"
```

### Pattern

`<url>(.*)</url>`

### Context

```json
{"admitted_char": "'\\n'", "keyword": "url", "reason": "name/comment claims validation but pattern admits excluded char"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fea300d717c3645c18955cc256e039ad:search

```yaml
regex_id: fea300d717c3645c18955cc256e039ad
schema_version: "1"
kind: usage_mismatch
corpus: pyparallel
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pyparallel/rules/Lib/site-packages/Cython-0.23.4-py3.3-win-amd64.egg/Cython/Compiler/Code.py:175:21"
```

### Pattern

`(.+)[.](proto|impl|init|cleanup)$`

### Context

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
corpus: pyparallel
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
corpus: pyparallel
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
corpus: pyparallel
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
corpus: pyparallel
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

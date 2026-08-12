---
schema_version: "1"
corpus: whohk
findings: 18
---

# whohk batch findings

## usage_mismatch:17004dabd8ce0b34e3dcda3ef317d6c5:search

```yaml
regex_id: 17004dabd8ce0b34e3dcda3ef317d6c5
schema_version: "1"
kind: usage_mismatch
corpus: whohk
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/whohk/rules/rules/webshells/WShell_THOR_Webshells.yar:7574:2"
```

### Pattern

`\$License:\ NRV\ for\ UPX\ is\ distributed\ under\ special\ license\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1900fba60921c2015bba5a228dd31054:search

```yaml
regex_id: 1900fba60921c2015bba5a228dd31054
schema_version: "1"
kind: usage_mismatch
corpus: whohk
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/whohk/rules/rules/webshells/WShell_THOR_Webshells.yar:1880:2"
```

### Pattern

`if\(eregi\('WHERE\|LIMIT',\$_POST\['nsql'\]\)\ \&\&\ eregi\('SELECT\|FROM',\$_POST\['nsql'\]\)\)\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4ca4aa6a463676ce15abf9e22b853026:search

```yaml
regex_id: 4ca4aa6a463676ce15abf9e22b853026
schema_version: "1"
kind: usage_mismatch
corpus: whohk
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/whohk/rules/rules/webshells/WShell_PHP_in_images.yar:12:8"
```

### Pattern

`^GIF8[79]a`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:53698e1817ea7d54c34502ed65ed4203:search

```yaml
regex_id: 53698e1817ea7d54c34502ed65ed4203
schema_version: "1"
kind: usage_mismatch
corpus: whohk
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/whohk/rules/rules/webshells/WShell_THOR_Webshells.yar:621:2"
```

### Pattern

`echo\ \\"\ <font\ color='\#0000FF'>CHMODU\ \\"\.substr\(base_convert\(@fileperms\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:56df53d635acccf718e4d5f634ae00b5:search

```yaml
regex_id: 56df53d635acccf718e4d5f634ae00b5
schema_version: "1"
kind: usage_mismatch
corpus: whohk
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/whohk/rules/rules/webshells/WShell_THOR_Webshells.yar:3813:2"
```

### Pattern

`\ \$fileEditInfo\ =\ \\"\&nbsp;\&nbsp;:::::::\&nbsp;\&nbsp;Owner:\ <font\ color=\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:74a6fdb08a3a4c652497c6ac7e56ea1e:search

```yaml
regex_id: 74a6fdb08a3a4c652497c6ac7e56ea1e
schema_version: "1"
kind: usage_mismatch
corpus: whohk
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/whohk/rules/rules/webshells/WShell_THOR_Webshells.yar:6547:2"
```

### Pattern

`\$Info:\ This\ file\ is\ packed\ with\ the\ UPX\ executable\ packer\ http://upx\.tsx\.org\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7fc2c9a4731036a042713c6e0ccaa868:search

```yaml
regex_id: 7fc2c9a4731036a042713c6e0ccaa868
schema_version: "1"
kind: usage_mismatch
corpus: whohk
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/whohk/rules/rules/webshells/WShell_THOR_Webshells.yar:3274:2"
```

### Pattern

`echo\ \\"Command\ :\ <INPUT\ TYPE=text\ NAME=cmd\ value=\\"\.@stripslashes\(htmlentities\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8554618ddb3da59b089e30ed46b4b328:search

```yaml
regex_id: 8554618ddb3da59b089e30ed46b4b328
schema_version: "1"
kind: usage_mismatch
corpus: whohk
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/whohk/rules/rules/webshells/WShell_THOR_Webshells.yar:7573:2"
```

### Pattern

`\$Info:\ This\ file\ is\ packed\ with\ the\ UPX\ executable\ packer\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:93d8019209f770f5fc720a64d3a41920:search

```yaml
regex_id: 93d8019209f770f5fc720a64d3a41920
schema_version: "1"
kind: usage_mismatch
corpus: whohk
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/whohk/rules/rules/webshells/WShell_THOR_Webshells.yar:89:2"
```

### Pattern

`if\ \(\$l\)\ echo\ '<a\ href=\\"'\ \.\ \$self\ \.\ '\?action=permission\&amp;file='\ \.\ urlencode\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cc077227532b1729300aa41957b5895c:search

```yaml
regex_id: cc077227532b1729300aa41957b5895c
schema_version: "1"
kind: usage_mismatch
corpus: whohk
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/whohk/rules/rules/webshells/WShell_THOR_Webshells.yar:6872:2"
```

### Pattern

`\$Info:\ This\ file\ is\ packed\ with\ the\ UPX\ executable\ packer\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cd452e054eb5ca937e5afed237929476:search

```yaml
regex_id: cd452e054eb5ca937e5afed237929476
schema_version: "1"
kind: usage_mismatch
corpus: whohk
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/whohk/rules/rules/webshells/WShell_THOR_Webshells.yar:6262:2"
```

### Pattern

`\$_REQUEST\['command'\]\ =\ \$aliases\[\$token\]\ \.\ substr\(\$_REQUEST\['command'\],\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d465bcdb77dca96f73de6379cf8752be:search

```yaml
regex_id: d465bcdb77dca96f73de6379cf8752be
schema_version: "1"
kind: usage_mismatch
corpus: whohk
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/whohk/rules/rules/webshells/WShell_THOR_Webshells.yar:50:2"
```

### Pattern

`<INPUT\ TYPE=\\"text\\"\ NAME=\\"cmd\\"\ value=\\"<\?php\ echo\ stripslashes\(htmlentities\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d9b185c40bccf2c23969784ed11c9646:search

```yaml
regex_id: d9b185c40bccf2c23969784ed11c9646
schema_version: "1"
kind: usage_mismatch
corpus: whohk
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/whohk/rules/rules/webshells/WShell_THOR_Webshells.yar:6554:2"
```

### Pattern

`\$Id:\ UPX\ 1\.07\ Copyright\ \(C\)\ 1996\-2001\ the\ UPX\ Team\.\ All\ Rights\ Reserved\.\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ddf80c1a01122a24837277f523acb44f:search

```yaml
regex_id: ddf80c1a01122a24837277f523acb44f
schema_version: "1"
kind: usage_mismatch
corpus: whohk
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/whohk/rules/rules/webshells/WShell_THOR_Webshells.yar:7335:2"
```

### Pattern

`\$Info:\ This\ file\ is\ packed\ with\ the\ UPX\ executable\ packer\ http://upx\.tsx\.org\ \$`

### Context

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
corpus: whohk
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
corpus: whohk
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
corpus: whohk
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
corpus: whohk
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

---
schema_version: "1"
corpus: patrolaroid
findings: 22
---

# patrolaroid batch findings

## usage_mismatch:05fe43e933eefb45aa348cce1e9ddacc:search

```yaml
regex_id: 05fe43e933eefb45aa348cce1e9ddacc
schema_version: "1"
kind: usage_mismatch
corpus: patrolaroid
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/patrolaroid/rules/Derubsi_Malware.yara:265:8"
```

### Pattern

`Wrod\-\-\$\$\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:103b43af38af9babb74e394df5855d1e:search

```yaml
regex_id: 103b43af38af9babb74e394df5855d1e
schema_version: "1"
kind: usage_mismatch
corpus: patrolaroid
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/patrolaroid/rules/Thor_Webshells.yara:3814:2"
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

## usage_mismatch:104579a8bbfe6a6abc4f34958fd8ff2e:search

```yaml
regex_id: 104579a8bbfe6a6abc4f34958fd8ff2e
schema_version: "1"
kind: usage_mismatch
corpus: patrolaroid
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/patrolaroid/rules/Thor_Webshells.yara:6555:2"
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

## usage_mismatch:1968511d6d85cbe5e1b8bf3859b26a54:search

```yaml
regex_id: 1968511d6d85cbe5e1b8bf3859b26a54
schema_version: "1"
kind: usage_mismatch
corpus: patrolaroid
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/patrolaroid/rules/Thor_Webshells.yara:1881:2"
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

## usage_mismatch:1f61c039a11f1c2cc271b88f231a45a2:search

```yaml
regex_id: 1f61c039a11f1c2cc271b88f231a45a2
schema_version: "1"
kind: usage_mismatch
corpus: patrolaroid
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/patrolaroid/rules/Thor_Webshells.yara:7574:2"
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

## usage_mismatch:306e0cf295a5659a1d244ca3f18f28fc:search

```yaml
regex_id: 306e0cf295a5659a1d244ca3f18f28fc
schema_version: "1"
kind: usage_mismatch
corpus: patrolaroid
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/patrolaroid/rules/Thor_Webshells.yara:6548:2"
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

## usage_mismatch:484a37e4a11bda828097697618839caa:search

```yaml
regex_id: 484a37e4a11bda828097697618839caa
schema_version: "1"
kind: usage_mismatch
corpus: patrolaroid
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/patrolaroid/rules/Thor_Webshells.yara:51:2"
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

## usage_mismatch:49124b9de33b3c83b24dd4287b81f660:search

```yaml
regex_id: 49124b9de33b3c83b24dd4287b81f660
schema_version: "1"
kind: usage_mismatch
corpus: patrolaroid
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/patrolaroid/rules/Thor_Webshells.yara:3275:2"
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

## usage_mismatch:6a0592b1a19118636edfc5bd60442325:search

```yaml
regex_id: 6a0592b1a19118636edfc5bd60442325
schema_version: "1"
kind: usage_mismatch
corpus: patrolaroid
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/patrolaroid/rules/Thor_Webshells.yara:90:2"
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

## usage_mismatch:6c05b8f269e8797e7cc89f7723e677de:search

```yaml
regex_id: 6c05b8f269e8797e7cc89f7723e677de
schema_version: "1"
kind: usage_mismatch
corpus: patrolaroid
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/patrolaroid/rules/Thor_Toolkit.yara:2770:2"
```

### Pattern

`WScript\.Echo\ \\"\ \ \ \$\$\\\\\ \ \ \ \ \ \$\$\\\\\ \$\$\\\\\ \ \ \ \ \ \$\$\\\\\ \$\$\$\$\$\$\\\\\ \$\$\$\$\$\$\$\$\\\\\ \$\$\\\\\ \ \ \$\$\\\\\ \$\$\$\$\$\$\$\$\\\\\ \ \$\$\$\$\$\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8065205dd620508b63c670e8b1aba7b0:search

```yaml
regex_id: 8065205dd620508b63c670e8b1aba7b0
schema_version: "1"
kind: usage_mismatch
corpus: patrolaroid
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/patrolaroid/rules/Derubsi_Malware.yara:320:8"
```

### Pattern

`Wrod\-\-\$\$\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8573a4f0f861c8f0ba1619ee9d5f6de8:search

```yaml
regex_id: 8573a4f0f861c8f0ba1619ee9d5f6de8
schema_version: "1"
kind: usage_mismatch
corpus: patrolaroid
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/patrolaroid/rules/Derubsi_Malware.yara:283:8"
```

### Pattern

`PS1=RK\#\ \\\\u@\\\\h:\\\\w\ \\\\\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9ef41a17e4f2194df882ab4164aaebf9:search

```yaml
regex_id: 9ef41a17e4f2194df882ab4164aaebf9
schema_version: "1"
kind: usage_mismatch
corpus: patrolaroid
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/patrolaroid/rules/Thor_Webshells.yara:6263:2"
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

## usage_mismatch:ab748b0b42f7fd903b47e6cb492229bf:search

```yaml
regex_id: ab748b0b42f7fd903b47e6cb492229bf
schema_version: "1"
kind: usage_mismatch
corpus: patrolaroid
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/patrolaroid/rules/Thor_Webshells.yara:7575:2"
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

## usage_mismatch:d29867026616835a0fd6842b673dfa06:search

```yaml
regex_id: d29867026616835a0fd6842b673dfa06
schema_version: "1"
kind: usage_mismatch
corpus: patrolaroid
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/patrolaroid/rules/Thor_Webshells.yara:622:2"
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

## usage_mismatch:dd96b9a07fd83ca7100258846b2a1e36:search

```yaml
regex_id: dd96b9a07fd83ca7100258846b2a1e36
schema_version: "1"
kind: usage_mismatch
corpus: patrolaroid
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/patrolaroid/rules/Thor_Webshells.yara:6873:2"
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

## usage_mismatch:faa1f13211ec75ce826d4878a4e68a5e:search

```yaml
regex_id: faa1f13211ec75ce826d4878a4e68a5e
schema_version: "1"
kind: usage_mismatch
corpus: patrolaroid
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/patrolaroid/rules/Equation_Group_Toolkit.yara:2122:6"
```

### Pattern

`By\ default,\ the\ shellcode\ will\ attempt\ to\ immediately\ connect\ s\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fd66d746482035e002db9b67f713a6d4:search

```yaml
regex_id: fd66d746482035e002db9b67f713a6d4
schema_version: "1"
kind: usage_mismatch
corpus: patrolaroid
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/patrolaroid/rules/Thor_Webshells.yara:7336:2"
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
corpus: patrolaroid
shape: 1
result: planned
disclosure: private_first
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
corpus: patrolaroid
shape: 2
result: planned
disclosure: private_first
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
corpus: patrolaroid
shape: 3
result: planned
disclosure: private_first
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
corpus: patrolaroid
shape: 4
result: planned
disclosure: private_first
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

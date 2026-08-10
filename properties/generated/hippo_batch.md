---
schema_version: "1"
corpus: hippo
findings: 30
---

# hippo batch findings

## usage_mismatch:04b60448348c185c7082486d26e3a26e:search

```yaml
regex_id: 04b60448348c185c7082486d26e3a26e
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:373:29"
```

### Pattern

`^confirm\[`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0c1227c30a2b34910c5464cd672c2b2c:search

```yaml
regex_id: 0c1227c30a2b34910c5464cd672c2b2c
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:576:33"
```

### Pattern

`^[\\s\\S]{"+ ruleArgs[0] +","+ ruleArgs[1] +"}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:18dec20f634a9f04cc445d5ce0f4bc34:search

```yaml
regex_id: 18dec20f634a9f04cc445d5ce0f4bc34
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:361:19"
```

### Pattern

`^validate(\[.+\])$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3506c9dc9cc0f4ddcf71e1b837b08f4e:search

```yaml
regex_id: 3506c9dc9cc0f4ddcf71e1b837b08f4e
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:370:39"
```

### Pattern

`^validate(\[.+\])$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3813cfbbe9a236071901afa8cc02f2ee:search

```yaml
regex_id: 3813cfbbe9a236071901afa8cc02f2ee
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:531:18"
```

### Pattern

`%[A-Z0-9\._-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3e2a82bc19e8b71c7f46f2421e272305:search

```yaml
regex_id: 3e2a82bc19e8b71c7f46f2421e272305
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:283:9"
```

### Pattern

`^(http|https|ftp)\:\/\/[a-z0-9\-\.]+\.[a-z]{2,3}(:[a-z0-9]*)?\/?([a-z0-9\-\._\?\,\'\/\\\+&amp;%\$#\=~])*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:41da108655dd44fbc04abd9ffe757a50:search

```yaml
regex_id: 41da108655dd44fbc04abd9ffe757a50
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:573:33"
```

### Pattern

`^[\\s\\S]{"+ ruleArgs[0] +"}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:43cd0ae7f4a0343086aafb484989f98e:search

```yaml
regex_id: 43cd0ae7f4a0343086aafb484989f98e
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:277:13"
```

### Pattern

`^[^0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5172a4355b67bcdc3bb590c83e6d8b5f:search

```yaml
regex_id: 5172a4355b67bcdc3bb590c83e6d8b5f
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/eforms.js:63:23"
```

### Pattern

`^\d*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:52318b8098f3c678737391669bc87f29:search

```yaml
regex_id: 52318b8098f3c678737391669bc87f29
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:278:12"
```

### Pattern

`^[-+]?\d*\.?\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5e5abe4749281c80845d920c1074ee0e:search

```yaml
regex_id: 5e5abe4749281c80845d920c1074ee0e
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:993:43"
```

### Pattern

`formcheck\.css$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6378142ef54cb45cc16db435e6760aa9:search

```yaml
regex_id: 6378142ef54cb45cc16db435e6760aa9
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:281:11"
```

### Pattern

`^[\d\s ().-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6a9896d6a21d38e3dcde7d75edc13e3b:search

```yaml
regex_id: 6a9896d6a21d38e3dcde7d75edc13e3b
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:495:18"
```

### Pattern

`^.+\[`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6b838ee62109ae7c20efba8dffd5506a:search

```yaml
regex_id: 6b838ee62109ae7c20efba8dffd5506a
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:531:64"
```

### Pattern

`~[A-Z0-9\._-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7478abdfabed78baa9c66e88ef478cf5:search

```yaml
regex_id: 7478abdfabed78baa9c66e88ef478cf5
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:282:17"
```

### Pattern

`^\+{0,1}[0-9 \(\)\.\-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:857c9a0af075fb77b1f0ec882a376c46:search

```yaml
regex_id: 857c9a0af075fb77b1f0ec882a376c46
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/eforms.js:66:23"
```

### Pattern

`^\d*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:91c77eca19b31621f7487c4b9d0189b9:search

```yaml
regex_id: 91c77eca19b31621f7487c4b9d0189b9
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:379:28"
```

### Pattern

`^target:.+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:93b14830ae437bf201ee2e984547dd26:search

```yaml
regex_id: 93b14830ae437bf201ee2e984547dd26
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/eforms.js:69:23"
```

### Pattern

`^\d*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a21ecb57eb50dba004ab67764a1191c0:search

```yaml
regex_id: a21ecb57eb50dba004ab67764a1191c0
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:580:32"
```

### Pattern

`^.{0,"+ ruleArgs[0] +"}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a24644860963f186d09bd0718ab4be7e:search

```yaml
regex_id: a24644860963f186d09bd0718ab4be7e
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:279:11"
```

### Pattern

`^([a-zA-Z0-9_\.\-\+%])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ab784eb8724bb8ea5a31c2c2417d87ea:search

```yaml
regex_id: ab784eb8724bb8ea5a31c2c2417d87ea
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:275:14"
```

### Pattern

`^[a-z0-9 ._-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b144bb38ec65482ca7b3334f0eb703f0:search

```yaml
regex_id: b144bb38ec65482ca7b3334f0eb703f0
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:276:11"
```

### Pattern

`^[-+]?[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bc8df5148653cee0fb9d26e12b47f4cb:search

```yaml
regex_id: bc8df5148653cee0fb9d26e12b47f4cb
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:380:38"
```

### Pattern

`^target:(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e6598c7a0adaae90672c80e5cd06ad4e:search

```yaml
regex_id: e6598c7a0adaae90672c80e5cd06ad4e
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:274:11"
```

### Pattern

`^[a-z ._-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f18d440ddff8c9f2692382d3d5a759ce:search

```yaml
regex_id: f18d440ddff8c9f2692382d3d5a759ce
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:280:11"
```

### Pattern

`.(jpg|jpeg|png|gif|bmp)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f40e55414135bb9de80df1c7a42c61b1:search

```yaml
regex_id: f40e55414135bb9de80df1c7a42c61b1
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:570:33"
```

### Pattern

`^[\\s\\S]{"+ ruleArgs[0] +",}$`

### Context

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
corpus: hippo
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
corpus: hippo
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
corpus: hippo
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
corpus: hippo
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

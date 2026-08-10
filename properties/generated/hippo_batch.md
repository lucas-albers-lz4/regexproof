---
schema_version: "1"
corpus: hippo
findings: 11
---

# hippo batch findings

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

## usage_mismatch:ee60cc81cfcb20ba33517b2a64bdaa39:search

```yaml
regex_id: ee60cc81cfcb20ba33517b2a64bdaa39
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:283:30"
```

### Pattern

`\/[a-z0-9\-\.]+\.[a-z]{2,3}(:[a-z0-9]*)?\/?([a-z0-9\-\._\?\,\'\/\\\+&amp;%\$#\=~])*$`

### Context

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

## usage_mismatch:f59217c0a3b8de20e4419f7f718f3b8b:search

```yaml
regex_id: f59217c0a3b8de20e4419f7f718f3b8b
schema_version: "1"
kind: usage_mismatch
corpus: hippo
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/hippo/rules/repository-data/webfiles/src/main/resources/site/src/js/eforms/formcheck/formcheck.js:67:23"
```

### Pattern

`^[A-Z]`

### Context

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

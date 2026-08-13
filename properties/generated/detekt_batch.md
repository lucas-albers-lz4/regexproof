---
schema_version: "1"
corpus: detekt
findings: 10
---

# detekt batch findings

## intent_mismatch:3f593f42398070e2d6d1a15824d637c1:email

```yaml
regex_id: 3f593f42398070e2d6d1a15824d637c1
schema_version: "1"
kind: intent_mismatch
corpus: detekt
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/detekt/rules/rules/finfisher.yar:7:8"
```

### Pattern

`\/scomma kbd101\.sys`

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

## intent_mismatch:733d887a380bbafe0c02ebf603a9f3cc:email

```yaml
regex_id: 733d887a380bbafe0c02ebf603a9f3cc
schema_version: "1"
kind: intent_mismatch
corpus: detekt
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/detekt/rules/rules/finfisher.yar:9:8"
```

### Pattern

`\/scomma excel2010\.part`

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

## intent_mismatch:7a4e24ac9b78be73eedd4fefee08c42f:email

```yaml
regex_id: 7a4e24ac9b78be73eedd4fefee08c42f
schema_version: "1"
kind: intent_mismatch
corpus: detekt
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/detekt/rules/rules/finfisher.yar:8:8"
```

### Pattern

`(N)AME,EMAIL CLIENT,EMAIL ADDRESS,SERVER NAME,SERVER TYPE,USERNAME,PASSWORD,PROFILE`

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

## intent_mismatch:a1bdcdf7e3a5edab51cd91e356b639d0:email

```yaml
regex_id: a1bdcdf7e3a5edab51cd91e356b639d0
schema_version: "1"
kind: intent_mismatch
corpus: detekt
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/detekt/rules/rules/finfisher.yar:8:8"
```

### Pattern

`(N)AME,EMAIL CLIENT,EMAIL ADDRESS,SERVER NAME,SERVER TYPE,USERNAME,PASSWORD,PROFILE`

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

## intent_mismatch:c6dddd7590059833cadfb8d1942c4c13:email

```yaml
regex_id: c6dddd7590059833cadfb8d1942c4c13
schema_version: "1"
kind: intent_mismatch
corpus: detekt
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/detekt/rules/rules/finfisher.yar:9:8"
```

### Pattern

`\/scomma excel2010\.part`

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

## intent_mismatch:e5445a44edc4a2c54655dbfc48de3a5e:email

```yaml
regex_id: e5445a44edc4a2c54655dbfc48de3a5e
schema_version: "1"
kind: intent_mismatch
corpus: detekt
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/detekt/rules/rules/finfisher.yar:7:8"
```

### Pattern

`\/scomma kbd101\.sys`

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
corpus: detekt
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
corpus: detekt
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
corpus: detekt
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
corpus: detekt
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

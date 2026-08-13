---
schema_version: "1"
corpus: json-editor
findings: 10
---

# json-editor batch findings

## usage_mismatch:226fb4b6272e271f85bc85f1139cab9f:search

```yaml
regex_id: 226fb4b6272e271f85bc85f1139cab9f
schema_version: "1"
kind: usage_mismatch
corpus: json-editor
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/json-editor/rules/validator.js:921:12"
```

### Pattern

`^(\d{4}\D\d{2}\D\d{2})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2a4cc517e2f842bac67340b0f9c6200c:search

```yaml
regex_id: 2a4cc517e2f842bac67340b0f9c6200c
schema_version: "1"
kind: usage_mismatch
corpus: json-editor
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/json-editor/rules/validator.js:922:12"
```

### Pattern

`^(\d{2}:\d{2}(?::\d{2})?)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4df73f31d8f4442b5cacb36a6a563614:search

```yaml
regex_id: 4df73f31d8f4442b5cacb36a6a563614
schema_version: "1"
kind: usage_mismatch
corpus: json-editor
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/json-editor/rules/utilities.js:72:22"
```

### Pattern

`^\s*(-|\+)?(\d+|(\d*(\.\d*)))([eE][+-]?\d+)?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c90a2ad40cabb77d7ea51df8f9d66b15:search

```yaml
regex_id: c90a2ad40cabb77d7ea51df8f9d66b15
schema_version: "1"
kind: usage_mismatch
corpus: json-editor
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/json-editor/rules/validator.js:836:10"
```

### Pattern

`^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ddf64ae0351b35d6cee11b9868004c05:search

```yaml
regex_id: ddf64ae0351b35d6cee11b9868004c05
schema_version: "1"
kind: usage_mismatch
corpus: json-editor
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/json-editor/rules/utilities.js:81:23"
```

### Pattern

`^\s*(-|\+)?(\d+)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f208ef468423a37407f90d73ef1c355f:search

```yaml
regex_id: f208ef468423a37407f90d73ef1c355f
schema_version: "1"
kind: usage_mismatch
corpus: json-editor
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/json-editor/rules/validator.js:923:24"
```

### Pattern

`^(\d{4}\D\d{2}\D\d{2}[ T]\d{2}:\d{2}(?::\d{2})?)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## property:inventory:v-shape1-injection-chars:v-shape1-injection-chars

```yaml
regex_id: "inventory:v-shape1-injection-chars"
schema_version: "1"
kind: property
corpus: json-editor
shape: 1
result: planned
disclosure: null
site: "inventory:v-shape1-injection-chars"
```

### Pattern

``

### Context

```json
{"question_id": "v-shape1-injection-chars", "threat": "Validator alphabet admits shell/HTML injection characters"}
```

### Witness

```json
null
```

### Ground-truth

None

## property:inventory:v-shape2-whitelist-space:v-shape2-whitelist-space

```yaml
regex_id: "inventory:v-shape2-whitelist-space"
schema_version: "1"
kind: property
corpus: json-editor
shape: 2
result: planned
disclosure: null
site: "inventory:v-shape2-whitelist-space"
```

### Pattern

``

### Context

```json
{"question_id": "v-shape2-whitelist-space", "threat": "Whitelisted string of bounded length contains forbidden separator"}
```

### Witness

```json
null
```

### Ground-truth

None

## property:inventory:v-shape3-prefix-vs-full:v-shape3-prefix-vs-full

```yaml
regex_id: "inventory:v-shape3-prefix-vs-full"
schema_version: "1"
kind: property
corpus: json-editor
shape: 3
result: planned
disclosure: null
site: "inventory:v-shape3-prefix-vs-full"
```

### Pattern

``

### Context

```json
{"question_id": "v-shape3-prefix-vs-full", "threat": "Prefix match accepts values that fail full-string validation intent"}
```

### Witness

```json
null
```

### Ground-truth

None

## property:inventory:v-shape4-escape-image:v-shape4-escape-image

```yaml
regex_id: "inventory:v-shape4-escape-image"
schema_version: "1"
kind: property
corpus: json-editor
shape: 4
result: planned
disclosure: null
site: "inventory:v-shape4-escape-image"
```

### Pattern

``

### Context

```json
{"question_id": "v-shape4-escape-image", "threat": "Escaped output still contains raw control characters"}
```

### Witness

```json
null
```

### Ground-truth

None

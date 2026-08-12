---
schema_version: "1"
corpus: xibo-cms
findings: 12
---

# xibo-cms batch findings

## usage_mismatch:57a8678043843c990ef726d3d3d4e684:search

```yaml
regex_id: 57a8678043843c990ef726d3d3d4e684
schema_version: "1"
kind: usage_mismatch
corpus: xibo-cms
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/xibo-cms/rules/frontend/src/utils/stringUtils.ts:35:16"
```

### Pattern

`^(.*?)(?:\s\((\d+)\))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:629a4e3be6e0d691a34043e1f3fce5a4:search

```yaml
regex_id: 629a4e3be6e0d691a34043e1f3fce5a4
schema_version: "1"
kind: usage_mismatch
corpus: xibo-cms
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/xibo-cms/rules/frontend/src/schema/command.ts:37:19"
```

### Pattern

`^[a-zA-Z0-9_]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:91905f8ef27b1af8a986fd5e434e5c8b:search

```yaml
regex_id: 91905f8ef27b1af8a986fd5e434e5c8b
schema_version: "1"
kind: usage_mismatch
corpus: xibo-cms
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/xibo-cms/rules/frontend/src/schema/display.ts:67:13"
```

### Pattern

`^([01]\d|2[0-3]):[0-5]\d$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ae15722895c3414a70090dd8c4fd90ca:search

```yaml
regex_id: ae15722895c3414a70090dd8c4fd90ca
schema_version: "1"
kind: usage_mismatch
corpus: xibo-cms
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/xibo-cms/rules/frontend/src/utils/date.ts:116:30"
```

### Pattern

`^(\d{4})-(\d{2})-(\d{2})`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b74b2f13687fb3517e962b7e4b4b8667:search

```yaml
regex_id: b74b2f13687fb3517e962b7e4b4b8667
schema_version: "1"
kind: usage_mismatch
corpus: xibo-cms
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/xibo-cms/rules/ui/src/helpers/date-format-helper.js:4:20"
```

### Pattern

`^%(\+|\-)[0-9]([0-9])?(d|h|m|s)%$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:bdc4999c952a6eb3467bdb2f52572b6e:email

```yaml
regex_id: bdc4999c952a6eb3467bdb2f52572b6e
schema_version: "1"
kind: intent_mismatch
corpus: xibo-cms
shape: null
result: finding
disclosure: null
site: "batch/corpora/xibo-cms/rules/frontend/src/components/help/FeedbackForm.tsx:42:17"
```

### Pattern

`^[^\s@]+@[^\s@]+\.[^\s@]+$`

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

## usage_mismatch:bdc4999c952a6eb3467bdb2f52572b6e:search

```yaml
regex_id: bdc4999c952a6eb3467bdb2f52572b6e
schema_version: "1"
kind: usage_mismatch
corpus: xibo-cms
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/xibo-cms/rules/frontend/src/components/help/FeedbackForm.tsx:42:17"
```

### Pattern

`^[^\s@]+@[^\s@]+\.[^\s@]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:da4cd6cf27096e1faef63ba41e57ddfb:search

```yaml
regex_id: da4cd6cf27096e1faef63ba41e57ddfb
schema_version: "1"
kind: usage_mismatch
corpus: xibo-cms
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/xibo-cms/rules/ui/src/helpers/date-format-helper.js:80:26"
```

### Pattern

`^\-`

### Context

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
corpus: xibo-cms
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
corpus: xibo-cms
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
corpus: xibo-cms
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
corpus: xibo-cms
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

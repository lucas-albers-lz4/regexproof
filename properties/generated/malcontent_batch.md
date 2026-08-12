---
schema_version: "1"
corpus: malcontent
findings: 9
---

# malcontent batch findings

## usage_mismatch:107c7b1d0efdf826f2fb8a036fdd1602:search

```yaml
regex_id: 107c7b1d0efdf826f2fb8a036fdd1602
schema_version: "1"
kind: usage_mismatch
corpus: malcontent
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/malcontent/rules/impact/exploit/cve-2025-48384.yara:25:4"
```

### Pattern

`[\n\x00][ \t]*url[ \t]*=[ \t]*"?[^\r\n]*\r$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1bd3cd2bfc5607dbf3be54c87b8eebe6:search

```yaml
regex_id: 1bd3cd2bfc5607dbf3be54c87b8eebe6
schema_version: "1"
kind: usage_mismatch
corpus: malcontent
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/malcontent/rules/impact/exploit/cve-2025-48384.yara:24:4"
```

### Pattern

`[\n\x00][ \t]*path[ \t]*=[ \t]*"?[^\r\n]*\r$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3f723987db7902f9b0fcbad675bd409e:search

```yaml
regex_id: 3f723987db7902f9b0fcbad675bd409e
schema_version: "1"
kind: usage_mismatch
corpus: malcontent
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/malcontent/rules/exec/remote_commands/code_eval.yara:231:4"
```

### Pattern

`create_function\([\'\"]{2},\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:abed3d951b3300df5f549acaa9a3abf5:search

```yaml
regex_id: abed3d951b3300df5f549acaa9a3abf5
schema_version: "1"
kind: usage_mismatch
corpus: malcontent
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/malcontent/rules/crypto/rc4.yara:36:4"
```

### Pattern

`'\&%\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d1d65d2aa84500027d41f558cfb0dfcd:search

```yaml
regex_id: d1d65d2aa84500027d41f558cfb0dfcd
schema_version: "1"
kind: usage_mismatch
corpus: malcontent
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/malcontent/rules/exfil/stealer/php.yara:12:4"
```

### Pattern

`copy\(\$`

### Context

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
corpus: malcontent
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
corpus: malcontent
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
corpus: malcontent
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
corpus: malcontent
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

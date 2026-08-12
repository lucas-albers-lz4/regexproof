---
schema_version: "1"
corpus: crust
findings: 8
---

# crust batch findings

## usage_mismatch:4e0606dcbd9c7dcb8e1e03ba41a19690:search

```yaml
regex_id: 4e0606dcbd9c7dcb8e1e03ba41a19690
schema_version: "1"
kind: usage_mismatch
corpus: crust
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/crust/rules/internal/configscan/scan.go:23:0"
```

### Pattern

`^([A-Z_]*(?:BASE_URL|API_BASE|API_URL|ENDPOINT))\s*=\s*["']?(\S+?)["']?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8c6762c92d05ce0a19afc9244a85e120:search

```yaml
regex_id: 8c6762c92d05ce0a19afc9244a85e120
schema_version: "1"
kind: usage_mismatch
corpus: crust
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/crust/rules/internal/rules/builtin_verify.go:81:0"
```

### Pattern

`(?m)^\s*- name:\s+(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b0d13af0775f50bd0bc7606e92675070:search

```yaml
regex_id: b0d13af0775f50bd0bc7606e92675070
schema_version: "1"
kind: usage_mismatch
corpus: crust
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/crust/rules/internal/configscan/scan.go:287:0"
```

### Pattern

`(?i)^\s*(yarnPath|npmRegistryServer)\s*:\s*["']?(\S+?)["']?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cd02a478d34b68dc650ef96f2cec2f4c:search

```yaml
regex_id: cd02a478d34b68dc650ef96f2cec2f4c
schema_version: "1"
kind: usage_mismatch
corpus: crust
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/crust/rules/internal/configscan/scan.go:200:0"
```

### Pattern

`(?i)^\s*(?:@[a-z0-9_-]+:)?registry\s*=\s*["']?(\S+?)["']?\s*$`

### Context

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
corpus: crust
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
corpus: crust
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
corpus: crust
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
corpus: crust
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

---
schema_version: "1"
corpus: snyk-ls
findings: 10
---

# snyk-ls batch findings

## usage_mismatch:188020b7d54a1be5a28a93cf47b333dd:search

```yaml
regex_id: 188020b7d54a1be5a28a93cf47b333dd
schema_version: "1"
kind: usage_mismatch
corpus: snyk-ls
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/snyk-ls/rules/internal/uri/uri_util.go:41:0"
```

### Pattern

`^(.+)://((.*)@)?(.+?)(:(\d*))?/?((.*)\?)?((.*)#)L?(\d+)(?:,(\d+))?(-L?(\d+)(?:,(\d+))?)?`

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

## usage_mismatch:559183f89e637a3aad536e44cd257297:search

```yaml
regex_id: 559183f89e637a3aad536e44cd257297
schema_version: "1"
kind: usage_mismatch
corpus: snyk-ls
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/snyk-ls/rules/infrastructure/configuration/config_html_test.go:894:0"
```

### Pattern

`^trustedFolder_\d+$`

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

## usage_mismatch:56c1a46dd9221f65167668ae05bb4278:search

```yaml
regex_id: 56c1a46dd9221f65167668ae05bb4278
schema_version: "1"
kind: usage_mismatch
corpus: snyk-ls
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/snyk-ls/rules/infrastructure/configuration/config_html_test.go:895:0"
```

### Pattern

`^folder_\d+_(.+)$`

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

## usage_mismatch:57f85ddcc6cce6d98b79573ec12127d2:search

```yaml
regex_id: 57f85ddcc6cce6d98b79573ec12127d2
schema_version: "1"
kind: usage_mismatch
corpus: snyk-ls
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/snyk-ls/rules/infrastructure/oss/code_actions.go:349:0"
```

### Pattern

`^\s*\$\{([^}]+)\}\s*$`

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

## usage_mismatch:8135f5d370b8502064b332fded56e4e2:search

```yaml
regex_id: 8135f5d370b8502064b332fded56e4e2
schema_version: "1"
kind: usage_mismatch
corpus: snyk-ls
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/snyk-ls/rules/application/config/config.go:657:0"
```

### Pattern

`^(ap[pi]\.)?`

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

## usage_mismatch:9badcaec7a75b985e365ca6803d25ee6:search

```yaml
regex_id: 9badcaec7a75b985e365ca6803d25ee6
schema_version: "1"
kind: usage_mismatch
corpus: snyk-ls
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/snyk-ls/rules/infrastructure/code/snyk_code_http_client.go:46:0"
```

### Pattern

`^(deeproxy\.)?`

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
corpus: snyk-ls
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
corpus: snyk-ls
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
corpus: snyk-ls
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
corpus: snyk-ls
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

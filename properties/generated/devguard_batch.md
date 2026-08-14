---
schema_version: "1"
corpus: devguard
findings: 13
---

# devguard batch findings

## usage_mismatch:194c4c16576183f6284f738077f9b958:search

```yaml
regex_id: 194c4c16576183f6284f738077f9b958
schema_version: "1"
kind: usage_mismatch
corpus: devguard
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/devguard/rules/controllers/dependencyfirewall/python.go:43:0"
```

### Pattern

`^([a-zA-Z0-9_-]+)-([0-9\.]+[a-zA-Z0-9\.]*)(?:-|\.).*$`

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

## usage_mismatch:24d20cda2e26d619de3993ac517c5b4e:search

```yaml
regex_id: 24d20cda2e26d619de3993ac517c5b4e
schema_version: "1"
kind: usage_mismatch
corpus: devguard
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/devguard/rules/controllers/dependencyfirewall/python.go:42:0"
```

### Pattern

`^/api/v1/dependency-proxy/(?:[^/]+/)?pypi(?:/|$)`

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

## usage_mismatch:25c0ba4c85ed36a783d0b14892dacee9:search

```yaml
regex_id: 25c0ba4c85ed36a783d0b14892dacee9
schema_version: "1"
kind: usage_mismatch
corpus: devguard
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/devguard/rules/controllers/dependencyfirewall/oci.go:47:0"
```

### Pattern

`^[a-z0-9]+(?:(?:[._]|__|[-]+)[a-z0-9]+)*$`

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

## usage_mismatch:260597b9ebd9823c8617bd35fee6d0f6:search

```yaml
regex_id: 260597b9ebd9823c8617bd35fee6d0f6
schema_version: "1"
kind: usage_mismatch
corpus: devguard
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/devguard/rules/controllers/dependencyfirewall/oci.go:49:0"
```

### Pattern

`^[a-zA-Z0-9_][a-zA-Z0-9_.-]{0,127}$`

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

## usage_mismatch:46f7360aa8dd0031922f0b5e785fdbc6:search

```yaml
regex_id: 46f7360aa8dd0031922f0b5e785fdbc6
schema_version: "1"
kind: usage_mismatch
corpus: devguard
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/devguard/rules/controllers/dependencyfirewall/golang.go:39:0"
```

### Pattern

`^/api/v1/dependency-proxy/(?:[^/]+/)?go(?:/|$)`

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

## usage_mismatch:56f4730a1ef37b7da68c6438a1e7cfb5:search

```yaml
regex_id: 56f4730a1ef37b7da68c6438a1e7cfb5
schema_version: "1"
kind: usage_mismatch
corpus: devguard
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/devguard/rules/controllers/dependencyfirewall/golang.go:40:0"
```

### Pattern

`^([^@]+)(?:@v/([^/]+))?`

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

## usage_mismatch:7c55b780198ce0b9d14053a633d979e5:search

```yaml
regex_id: 7c55b780198ce0b9d14053a633d979e5
schema_version: "1"
kind: usage_mismatch
corpus: devguard
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/devguard/rules/controllers/dependencyfirewall/npm.go:26:0"
```

### Pattern

`^/api/v1/dependency-proxy/(?:[^/]+/)?npm(?:/|$)`

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

## usage_mismatch:e5b64d58172eca494b09a85a33c3435b:search

```yaml
regex_id: e5b64d58172eca494b09a85a33c3435b
schema_version: "1"
kind: usage_mismatch
corpus: devguard
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/devguard/rules/controllers/dependencyfirewall/oci.go:51:0"
```

### Pattern

`^sha256:[a-f0-9]{64}$`

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

## usage_mismatch:fdb28681ff9807c12e3f706fbfc84f88:search

```yaml
regex_id: fdb28681ff9807c12e3f706fbfc84f88
schema_version: "1"
kind: usage_mismatch
corpus: devguard
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/devguard/rules/controllers/dependencyfirewall/oci.go:40:0"
```

### Pattern

`^/api/v1/dependency-proxy/(?:[^/]+/)?oci(?:/|$)`

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
corpus: devguard
shape: 1
result: planned
ground_truth_status: planned
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

planned

## property:inventory:rc-shape2-missing-keyword:rc-shape2-missing-keyword

```yaml
regex_id: "inventory:rc-shape2-missing-keyword"
schema_version: "1"
kind: property
corpus: devguard
shape: 2
result: planned
ground_truth_status: planned
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

planned

## property:inventory:rc-shape3-capture-truncation:rc-shape3-capture-truncation

```yaml
regex_id: "inventory:rc-shape3-capture-truncation"
schema_version: "1"
kind: property
corpus: devguard
shape: 3
result: planned
ground_truth_status: planned
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

planned

## property:inventory:rc-shape4-escape-image:rc-shape4-escape-image

```yaml
regex_id: "inventory:rc-shape4-escape-image"
schema_version: "1"
kind: property
corpus: devguard
shape: 4
result: planned
ground_truth_status: planned
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

planned

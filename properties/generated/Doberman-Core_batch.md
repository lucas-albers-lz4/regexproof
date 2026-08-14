---
schema_version: "1"
corpus: Doberman-Core
findings: 11
---

# Doberman-Core batch findings

## usage_mismatch:3d8b072238019df695bfb8b67b00270e:search

```yaml
regex_id: 3d8b072238019df695bfb8b67b00270e
schema_version: "1"
kind: usage_mismatch
corpus: Doberman-Core
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Doberman-Core/rules/src/doberman/engine/rules/secrets.py:241:17"
```

### Pattern

`^[A-Za-z0-9+/=_\-]+$`

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

## usage_mismatch:8b0d550db752677679056268505aa4c9:search

```yaml
regex_id: 8b0d550db752677679056268505aa4c9
schema_version: "1"
kind: usage_mismatch
corpus: Doberman-Core
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Doberman-Core/rules/src/doberman/engine/rules/secrets.py:273:16"
```

### Pattern

`^(?:[A-Za-z]+|[0-9]+)$`

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

## usage_mismatch:99be3fbf630b3f6745d3a2ee1c3bde7c:search

```yaml
regex_id: 99be3fbf630b3f6745d3a2ee1c3bde7c
schema_version: "1"
kind: usage_mismatch
corpus: Doberman-Core
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Doberman-Core/rules/src/doberman/engine/rules/commands.py:434:13"
```

### Pattern

`^(?:mkfs(?:\.\w+)?|shred|wipefs|format-volume|clear-disk|format)$`

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

## usage_mismatch:a059cdd0c487bcf140da701a5407c1c3:search

```yaml
regex_id: a059cdd0c487bcf140da701a5407c1c3
schema_version: "1"
kind: usage_mismatch
corpus: Doberman-Core
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Doberman-Core/rules/src/doberman/engine/rules/secrets.py:102:21"
```

### Pattern

`(?i)^(?:your[_\-].*|.*[_\-]here|change[_\-]?me|placeholder.*|redacted.*|dummy.*|example[_\-].*|sample[_\-].*|test[_\-]?(?:key|token|secret).*|<.*>|\$\{.*\}|\*{3,}|x{4,})$`

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

## usage_mismatch:c64d6556b7b3b3aff3650681dca07bf3:search

```yaml
regex_id: c64d6556b7b3b3aff3650681dca07bf3
schema_version: "1"
kind: usage_mismatch
corpus: Doberman-Core
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Doberman-Core/rules/src/doberman/engine/rules/commands.py:82:18"
```

### Pattern

`^[A-Za-z_][A-Za-z0-9_]*=`

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

## usage_mismatch:c7e8e7b6a8373d4a009b57e9e72831ec:search

```yaml
regex_id: c7e8e7b6a8373d4a009b57e9e72831ec
schema_version: "1"
kind: usage_mismatch
corpus: Doberman-Core
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Doberman-Core/rules/src/doberman/engine/rules/commands.py:266:19"
```

### Pattern

`^[A-Za-z]:[/\\]?(\*)?$`

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

## intent_mismatch:d0ef06782c11c736e18164d01637c060:email

```yaml
regex_id: d0ef06782c11c736e18164d01637c060
schema_version: "1"
kind: intent_mismatch
corpus: Doberman-Core
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Doberman-Core/rules/src/doberman/turngate/signatures.py:108:4"
```

### Pattern

`\b(send|email|e-mail|post|upload|exfiltrate|print|show|reveal|give me|tell me|output|paste|share|leak|export|transmit|curl|fetch|dump)\b[^.?!]{0,40}\b(api[ _-]?key|api[ _-]?keys|secret|secret key|access key|token|tokens|password|passwd|credential|credentials|private key|ssh key|\.env|env file|aws[ _-]?key)\b`

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
corpus: Doberman-Core
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
corpus: Doberman-Core
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
corpus: Doberman-Core
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
corpus: Doberman-Core
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

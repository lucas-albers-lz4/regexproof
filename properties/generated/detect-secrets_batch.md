---
schema_version: "1"
corpus: detect-secrets
findings: 5
---

# detect-secrets batch findings

## usage_mismatch:e7bddec159659c5738754898341489fe:search

- result: `finding`
- site: `pilots/detect-secrets/sample_plugins.py:15:13`
- ground_truth_status: `N/A`
- disclosure: `private_first`

### Pattern

`^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## property:inventory:rc-shape1-injection-alphabet:rc-shape1-injection-alphabet

- result: `planned`
- site: `inventory:rc-shape1-injection-alphabet`
- ground_truth_status: `N/A`
- disclosure: `private_first`

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

N/A

## property:inventory:rc-shape2-missing-keyword:rc-shape2-missing-keyword

- result: `planned`
- site: `inventory:rc-shape2-missing-keyword`
- ground_truth_status: `N/A`
- disclosure: `private_first`

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

N/A

## property:inventory:rc-shape3-capture-truncation:rc-shape3-capture-truncation

- result: `planned`
- site: `inventory:rc-shape3-capture-truncation`
- ground_truth_status: `N/A`
- disclosure: `private_first`

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

N/A

## property:inventory:rc-shape4-escape-image:rc-shape4-escape-image

- result: `planned`
- site: `inventory:rc-shape4-escape-image`
- ground_truth_status: `N/A`
- disclosure: `private_first`

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

N/A

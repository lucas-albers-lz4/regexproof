---
schema_version: "1"
corpus: canvas-drop
findings: 21
---

# canvas-drop batch findings

## usage_mismatch:207d66ed3a8656b910b7b8a2c624b7ab:search

```yaml
regex_id: 207d66ed3a8656b910b7b8a2c624b7ab
schema_version: "1"
kind: usage_mismatch
corpus: canvas-drop
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/canvas-drop/rules/apps/server/src/http/rate-limit.ts:118:34"
```

### Pattern

`^\/v1\/c\/([^/]+)(\/|$)`

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

## usage_mismatch:263e595805f0896259c331f26f393a54:search

```yaml
regex_id: 263e595805f0896259c331f26f393a54
schema_version: "1"
kind: usage_mismatch
corpus: canvas-drop
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/canvas-drop/rules/apps/server/src/upload/service.ts:154:43"
```

### Pattern

`^[0-9a-f]{64}$`

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

## usage_mismatch:2cc35035e1f854404039a0c508b87954:search

```yaml
regex_id: 2cc35035e1f854404039a0c508b87954
schema_version: "1"
kind: usage_mismatch
corpus: canvas-drop
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/canvas-drop/rules/packages/shared/src/config/env.ts:109:49"
```

### Pattern

`^\d{1,3}$`

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

## usage_mismatch:35eb74ab674a56001921cacbac5e8880:search

```yaml
regex_id: 35eb74ab674a56001921cacbac5e8880
schema_version: "1"
kind: usage_mismatch
corpus: canvas-drop
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/canvas-drop/rules/apps/server/src/routing/resolve-request.ts:23:24"
```

### Pattern

`^\/v1\/c\/([^/]+)`

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

## usage_mismatch:4744b33fbb4e5bbc7841f268cdebb0f1:search

```yaml
regex_id: 4744b33fbb4e5bbc7841f268cdebb0f1
schema_version: "1"
kind: usage_mismatch
corpus: canvas-drop
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/canvas-drop/rules/packages/shared/src/tenancy/domain.ts:15:19"
```

### Pattern

`^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(?:\.[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)+$`

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

## usage_mismatch:61f862fdbbf0a895133aa68d51e5c6af:search

```yaml
regex_id: 61f862fdbbf0a895133aa68d51e5c6af
schema_version: "1"
kind: usage_mismatch
corpus: canvas-drop
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/canvas-drop/rules/apps/server/src/docs/routes.ts:35:19"
```

### Pattern

`^[a-z0-9][a-z0-9-]*\.webp$`

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

## usage_mismatch:74f5f40d8e366850e2d8b042a3ab87d7:search

```yaml
regex_id: 74f5f40d8e366850e2d8b042a3ab87d7
schema_version: "1"
kind: usage_mismatch
corpus: canvas-drop
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/canvas-drop/rules/apps/dashboard/src/lib/cosmetic-slug.ts:14:16"
```

### Pattern

`^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

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

## usage_mismatch:7979de340c4f5fcc980732c339f11e80:search

```yaml
regex_id: 7979de340c4f5fcc980732c339f11e80
schema_version: "1"
kind: usage_mismatch
corpus: canvas-drop
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/canvas-drop/rules/packages/sdk/src/index.ts:195:16"
```

### Pattern

`^\/c\/([^/]+)`

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

## usage_mismatch:841d0b7f44f0a4de5d3612f52f844040:search

```yaml
regex_id: 841d0b7f44f0a4de5d3612f52f844040
schema_version: "1"
kind: usage_mismatch
corpus: canvas-drop
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/canvas-drop/rules/packages/shared/src/tenancy/domain.ts:19:47"
```

### Pattern

`\.$`

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

## usage_mismatch:8a668e216e89491ea90f8bc54514b6eb:search

```yaml
regex_id: 8a668e216e89491ea90f8bc54514b6eb
schema_version: "1"
kind: usage_mismatch
corpus: canvas-drop
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/canvas-drop/rules/examples/showcase/js/files.js:4:17"
```

### Pattern

`\.(png|jpe?g|gif|webp|svg|avif)$`

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

## usage_mismatch:8bb10116e41d7e4c4a6edc39240a58cd:search

```yaml
regex_id: 8bb10116e41d7e4c4a6edc39240a58cd
schema_version: "1"
kind: usage_mismatch
corpus: canvas-drop
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/canvas-drop/rules/packages/shared/src/canvas/slug-policy.ts:78:7"
```

### Pattern

`^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$`

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

## usage_mismatch:a046a97749ac4d1d1d36190c9ffb7339:search

```yaml
regex_id: a046a97749ac4d1d1d36190c9ffb7339
schema_version: "1"
kind: usage_mismatch
corpus: canvas-drop
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/canvas-drop/rules/apps/server/src/routing/resolve-request.ts:24:23"
```

### Pattern

`^\/c\/([^/]+)`

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

## usage_mismatch:ab3376be58be18d5d9118d2b2c5e6047:search

```yaml
regex_id: ab3376be58be18d5d9118d2b2c5e6047
schema_version: "1"
kind: usage_mismatch
corpus: canvas-drop
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/canvas-drop/rules/apps/server/src/http/rate-limit.ts:125:8"
```

### Pattern

`^\/v1\/c\/[^/]+\/ai(\/|$)`

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

## usage_mismatch:cc2847d1ce26681a2facd519929078f5:search

```yaml
regex_id: cc2847d1ce26681a2facd519929078f5
schema_version: "1"
kind: usage_mismatch
corpus: canvas-drop
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/canvas-drop/rules/apps/server/src/app.ts:539:26"
```

### Pattern

`\.html?$`

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

## intent_mismatch:ddc73c1d22be7d17ac868ff84ec80b8c:email

```yaml
regex_id: ddc73c1d22be7d17ac868ff84ec80b8c
schema_version: "1"
kind: intent_mismatch
corpus: canvas-drop
shape: null
result: finding
disclosure: null
site: "batch/corpora/canvas-drop/rules/apps/server/src/email/templates.ts:243:26"
```

### Pattern

`\{\{\s*([a-zA-Z]+)\s*\}\}`

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

## usage_mismatch:e2a4504a789f278c12045d00b9eb23ad:search

```yaml
regex_id: e2a4504a789f278c12045d00b9eb23ad
schema_version: "1"
kind: usage_mismatch
corpus: canvas-drop
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/canvas-drop/rules/apps/server/src/ops/backup.ts:80:30"
```

### Pattern

`^canvases\/[^/]+\/blobs\/([0-9a-f]{64})$`

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

## usage_mismatch:eab649809fad2cae3fb87a07a02e3db3:search

```yaml
regex_id: eab649809fad2cae3fb87a07a02e3db3
schema_version: "1"
kind: usage_mismatch
corpus: canvas-drop
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/canvas-drop/rules/apps/server/src/canvas/serve.ts:19:24"
```

### Pattern

`\.[0-9a-f]{8,}\.[a-z0-9]+$`

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
corpus: canvas-drop
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
corpus: canvas-drop
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
corpus: canvas-drop
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
corpus: canvas-drop
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

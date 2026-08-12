---
schema_version: "1"
corpus: gigachad-grc
findings: 33
---

# gigachad-grc batch findings

## usage_mismatch:06371fed882b6ea4bb0dca8c4dddf38c:search

```yaml
regex_id: 06371fed882b6ea4bb0dca8c4dddf38c
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/services/controls/src/collectors/collectors.service.ts:742:15"
```

### Pattern

`^[A-Za-z0-9_-]+$`

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

## usage_mismatch:0f58baf655964ba9ca75e9d9047cee59:search

```yaml
regex_id: 0f58baf655964ba9ca75e9d9047cee59
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/services/tprm/src/security-scanner/security-scanner.service.ts:90:4"
```

### Pattern

`^172\.(1[6-9]|2[0-9]|3[0-1])\.`

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

## usage_mismatch:1873a865a4d24835160c3868e433334e:search

```yaml
regex_id: 1873a865a4d24835160c3868e433334e
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/services/tprm/src/security-scanner/security-scanner.service.ts:407:6"
```

### Pattern

`^Only HTTP\/HTTPS URLs are allowed`

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

## usage_mismatch:1d5c22649f54985fb17be3db9df01684:search

```yaml
regex_id: 1d5c22649f54985fb17be3db9df01684
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/mcp-servers/grc-evidence/src/tools/google-workspace-evidence.ts:70:4"
```

### Pattern

`^\$\{`

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

## usage_mismatch:2dedd81ad4c63869bdb41c32722c9ab3:search

```yaml
regex_id: 2dedd81ad4c63869bdb41c32722c9ab3
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/mcp-servers/grc-evidence/src/tools/google-workspace-evidence.ts:65:4"
```

### Pattern

`^\/dev\/`

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

## usage_mismatch:30d7f4bf623a6694ecfd0259ea0b89e8:search

```yaml
regex_id: 30d7f4bf623a6694ecfd0259ea0b89e8
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/services/shared/src/utils/validation.ts:65:25"
```

### Pattern

`^[A-Z]{1,3}[-.]?\d{1,5}(\.\d{1,5}){0,10}$`

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

## usage_mismatch:39f87ee966b671c5c0f4db708cc08d39:search

```yaml
regex_id: 39f87ee966b671c5c0f4db708cc08d39
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/services/tprm/src/security-scanner/security-scanner.service.ts:88:4"
```

### Pattern

`^192\.168\.`

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

## usage_mismatch:3af56131e7c1186e175ede3d9cd37fbf:search

```yaml
regex_id: 3af56131e7c1186e175ede3d9cd37fbf
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/mcp-servers/grc-evidence/src/tools/google-workspace-evidence.ts:64:4"
```

### Pattern

`^\/sys\/`

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

## usage_mismatch:48cd2befb95545c4d85f422563326d7e:search

```yaml
regex_id: 48cd2befb95545c4d85f422563326d7e
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/services/shared/src/utils/validation.ts:18:38"
```

### Pattern

`^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+$`

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

## usage_mismatch:53ee99f58ac2e77ee27366d7e3b506b6:search

```yaml
regex_id: 53ee99f58ac2e77ee27366d7e3b506b6
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/services/controls/src/scim/dto/scim.dto.ts:277:11"
```

### Pattern

`^[a-zA-Z0-9\s\-_.,@"'()[\]{}:=<>!&|*+/\\^%$#~`]*$`

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

## usage_mismatch:552021ca5b22ea8536a72dd44ebbc383:search

```yaml
regex_id: 552021ca5b22ea8536a72dd44ebbc383
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/mcp-servers/grc-evidence/src/tools/google-workspace-evidence.ts:63:4"
```

### Pattern

`^\/proc\/`

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

## usage_mismatch:5f87a5ad1459199ac1dbd96afc59b7f0:search

```yaml
regex_id: 5f87a5ad1459199ac1dbd96afc59b7f0
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/services/shared/src/utils/validation.ts:38:20"
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

## usage_mismatch:6162bedcd9ff5ec81bfe869a32cf5ba4:search

```yaml
regex_id: 6162bedcd9ff5ec81bfe869a32cf5ba4
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/mcp-servers/grc-evidence/src/tools/google-workspace-evidence.ts:66:4"
```

### Pattern

`^\/root\/`

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

## usage_mismatch:68a4b3439e104709361ac5e3b2be60f4:search

```yaml
regex_id: 68a4b3439e104709361ac5e3b2be60f4
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/services/shared/src/utils/validation.ts:25:5"
```

### Pattern

`^[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?)+$`

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

## usage_mismatch:73858c81a05dbb6ca338022729c43d36:search

```yaml
regex_id: 73858c81a05dbb6ca338022729c43d36
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/services/tprm/src/security-scanner/security-scanner.service.ts:405:6"
```

### Pattern

`^Vendor with ID .* not found$`

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

## usage_mismatch:75f24c864a3918e488cac5ef9b5ba649:search

```yaml
regex_id: 75f24c864a3918e488cac5ef9b5ba649
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/services/tprm/src/security-scanner/security-scanner.service.ts:93:4"
```

### Pattern

`^0\.`

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

## usage_mismatch:7bafe4ac77edf198b80704c32c0c0515:search

```yaml
regex_id: 7bafe4ac77edf198b80704c32c0c0515
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/services/tprm/src/security-scanner/security-scanner.service.ts:408:6"
```

### Pattern

`^Cannot scan localhost`

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

## usage_mismatch:8885ec239d4e2f055844a8e477cd805c:search

```yaml
regex_id: 8885ec239d4e2f055844a8e477cd805c
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/services/tprm/src/security-scanner/security-scanner.service.ts:403:6"
```

### Pattern

`^Security scan timed out`

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

## usage_mismatch:89b5d85390037cef1046dc30f4a2dfc2:search

```yaml
regex_id: 89b5d85390037cef1046dc30f4a2dfc2
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/services/tprm/src/security-scanner/security-scanner.service.ts:89:4"
```

### Pattern

`^10\.`

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

## usage_mismatch:89d0f8d7f54f52d1647135ea8d1b9f6a:search

```yaml
regex_id: 89d0f8d7f54f52d1647135ea8d1b9f6a
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/services/tprm/src/security-scanner/security-scanner.service.ts:409:6"
```

### Pattern

`^Cannot scan private`

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

## usage_mismatch:900f7b12d4a4ab9a3af5140c66725067:search

```yaml
regex_id: 900f7b12d4a4ab9a3af5140c66725067
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/mcp-servers/grc-evidence/src/tools/google-workspace-evidence.ts:62:4"
```

### Pattern

`^\/etc\/`

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

## usage_mismatch:a1a324ddb1ecba4300e9ffbb010fd3c2:search

```yaml
regex_id: a1a324ddb1ecba4300e9ffbb010fd3c2
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/mcp-servers/grc-evidence/src/tools/google-workspace-evidence.ts:69:4"
```

### Pattern

`^~\/`

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

## usage_mismatch:af043d9767d51b57612cc9e55a763e90:search

```yaml
regex_id: af043d9767d51b57612cc9e55a763e90
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/mcp-servers/grc-evidence/src/tools/google-workspace-evidence.ts:67:4"
```

### Pattern

`^\/var\/log\/`

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

## usage_mismatch:bc2a77b9ac4a5496b1f546580c9ef356:search

```yaml
regex_id: bc2a77b9ac4a5496b1f546580c9ef356
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/services/tprm/src/security-scanner/security-scanner.service.ts:404:6"
```

### Pattern

`^No target URL provided`

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

## usage_mismatch:ca388d0f8f6c6f74cf08eb6a0a75367e:search

```yaml
regex_id: ca388d0f8f6c6f74cf08eb6a0a75367e
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/services/tprm/src/security-scanner/security-scanner.service.ts:92:4"
```

### Pattern

`^169\.254\.`

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

## usage_mismatch:d478281faacf3938299d739d859c6402:search

```yaml
regex_id: d478281faacf3938299d739d859c6402
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/services/tprm/src/security-scanner/security-scanner.service.ts:91:4"
```

### Pattern

`^127\.`

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

## usage_mismatch:e19470ebe94dd4fb521d3d437e02a78d:search

```yaml
regex_id: e19470ebe94dd4fb521d3d437e02a78d
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/mcp-servers/grc-evidence/src/tools/google-workspace-evidence.ts:68:4"
```

### Pattern

`^\/var\/run\/`

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

## usage_mismatch:e32e4cb003d7bffb1baa37876757d6c2:search

```yaml
regex_id: e32e4cb003d7bffb1baa37876757d6c2
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/services/tprm/src/security-scanner/security-scanner.service.ts:406:6"
```

### Pattern

`^Invalid URL format$`

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

## usage_mismatch:ffd524f382062fc22a97a4dcdbff0638:search

```yaml
regex_id: ffd524f382062fc22a97a4dcdbff0638
schema_version: "1"
kind: usage_mismatch
corpus: gigachad-grc
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gigachad-grc/rules/services/tprm/src/security-scanner/security-scanner.service.ts:410:6"
```

### Pattern

`^Cannot scan cloud metadata`

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
corpus: gigachad-grc
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
corpus: gigachad-grc
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
corpus: gigachad-grc
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
corpus: gigachad-grc
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

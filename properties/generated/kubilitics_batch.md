---
schema_version: "1"
corpus: kubilitics
findings: 28
---

# kubilitics batch findings

## usage_mismatch:012e723f8869e0bc0b7f00eb400937df:search

```yaml
regex_id: 012e723f8869e0bc0b7f00eb400937df
schema_version: "1"
kind: usage_mismatch
corpus: kubilitics
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/kubilitics/rules/kubilitics-frontend/src/pages/StatefulSetDetail.tsx:389:36"
```

### Pattern

`^(\d+(?:\.\d+)?)\s*Mi?$`

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

## usage_mismatch:02a43e604da64a9b4d709a1504faaa2c:search

```yaml
regex_id: 02a43e604da64a9b4d709a1504faaa2c
schema_version: "1"
kind: usage_mismatch
corpus: kubilitics
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/kubilitics/rules/kubilitics-frontend/src/lib/dark-mode-audit.ts:134:2"
```

### Pattern

`\.spec\.(ts|tsx)$`

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

## usage_mismatch:04606953b1750f421e4efcddcfbd9374:search

```yaml
regex_id: 04606953b1750f421e4efcddcfbd9374
schema_version: "1"
kind: usage_mismatch
corpus: kubilitics
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/kubilitics/rules/kubilitics-frontend/src/features/dashboard/components/ClusterCapacity.tsx:42:24"
```

### Pattern

`^(\d+(?:\.\d+)?)\s*([EPTGMK]i?|[eptgmk])?$`

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

## usage_mismatch:06eaf3e83304a063e3c77507c2888f43:search

```yaml
regex_id: 06eaf3e83304a063e3c77507c2888f43
schema_version: "1"
kind: usage_mismatch
corpus: kubilitics
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/kubilitics/rules/kubilitics-frontend/src/pages/ConfigMapDetail.tsx:41:6"
```

### Pattern

`^[\w.-]+=.*`

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

## usage_mismatch:11ca85afdedfa8fb87ea73905e270bbd:search

```yaml
regex_id: 11ca85afdedfa8fb87ea73905e270bbd
schema_version: "1"
kind: usage_mismatch
corpus: kubilitics
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/kubilitics/rules/kubilitics-frontend/src/pages/Jobs.tsx:222:19"
```

### Pattern

`^(\d+)(s|m|h)$`

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

## usage_mismatch:1e685786a9e6289d604710de1d667d66:search

```yaml
regex_id: 1e685786a9e6289d604710de1d667d66
schema_version: "1"
kind: usage_mismatch
corpus: kubilitics
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/kubilitics/rules/kubilitics-frontend/src/pages/Deployments.tsx:137:23"
```

### Pattern

`^(\d+)\/(\d+)$`

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

## usage_mismatch:283c3b9f1dcdd216d395cefd3ada54db:search

```yaml
regex_id: 283c3b9f1dcdd216d395cefd3ada54db
schema_version: "1"
kind: usage_mismatch
corpus: kubilitics
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/kubilitics/rules/kubilitics-frontend/src/components/resources/YamlDiffUtils.tsx:102:21"
```

### Pattern

`^['"]|['"]$`

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

## usage_mismatch:2cd4a7edeb32c96317ba3ea7705d89f6:search

```yaml
regex_id: 2cd4a7edeb32c96317ba3ea7705d89f6
schema_version: "1"
kind: usage_mismatch
corpus: kubilitics
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/kubilitics/rules/kubilitics-frontend/src/pages/CronJobDetail.tsx:730:53"
```

### Pattern

`^\S+\s+\S+\s+\S+\s+\S+\s+\S+$`

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

## usage_mismatch:407e0e50b97209b91e8ec687382c35a3:search

```yaml
regex_id: 407e0e50b97209b91e8ec687382c35a3
schema_version: "1"
kind: usage_mismatch
corpus: kubilitics
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/kubilitics/rules/kubilitics-frontend/src/lib/crdRelationshipMatcher.ts:368:33"
```

### Pattern

`^([^.]+)\.([^.]+)\.svc`

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

## usage_mismatch:41685a3d22ed06d9cc13dae29c53ba38:search

```yaml
regex_id: 41685a3d22ed06d9cc13dae29c53ba38
schema_version: "1"
kind: usage_mismatch
corpus: kubilitics
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/kubilitics/rules/kubilitics-frontend/src/pages/Deployments.tsx:318:23"
```

### Pattern

`^(\d+)\/(\d+)$`

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

## usage_mismatch:428349fb97c6b64e3344a11e7d2c9372:search

```yaml
regex_id: 428349fb97c6b64e3344a11e7d2c9372
schema_version: "1"
kind: usage_mismatch
corpus: kubilitics
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/kubilitics/rules/kubilitics-frontend/src/lib/crdRelationshipMatcher.ts:287:16"
```

### Pattern

`[Cc]onfig[Mm]ap[Nn]ame$`

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

## usage_mismatch:44a1376de2d3be9fe69f176c8682ffa4:search

```yaml
regex_id: 44a1376de2d3be9fe69f176c8682ffa4
schema_version: "1"
kind: usage_mismatch
corpus: kubilitics
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/kubilitics/rules/kubilitics-frontend/src/lib/dark-mode-audit.ts:139:2"
```

### Pattern

`vite-env\.d\.ts$`

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

## usage_mismatch:49dff3bc8d763efe5865c104ed57450e:search

```yaml
regex_id: 49dff3bc8d763efe5865c104ed57450e
schema_version: "1"
kind: usage_mismatch
corpus: kubilitics
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/kubilitics/rules/kubilitics-frontend/src/lib/crdRelationshipMatcher.ts:289:16"
```

### Pattern

`[Nn]amespace$`

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

## usage_mismatch:4a3274da773bb0d1b87aa50ccc438a62:search

```yaml
regex_id: 4a3274da773bb0d1b87aa50ccc438a62
schema_version: "1"
kind: usage_mismatch
corpus: kubilitics
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/kubilitics/rules/kubilitics-frontend/src/lib/dark-mode-audit.ts:138:2"
```

### Pattern

`\.d\.ts$`

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

## usage_mismatch:58b1d1e54f646a889d455a0bd46cd5a8:search

```yaml
regex_id: 58b1d1e54f646a889d455a0bd46cd5a8
schema_version: "1"
kind: usage_mismatch
corpus: kubilitics
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/kubilitics/rules/kubilitics-frontend/src/lib/crdRelationshipMatcher.ts:286:16"
```

### Pattern

`[Ss]ecret[Nn]ame$`

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

## usage_mismatch:6ca26116f5df8f24d9fcae2163ab6d93:search

```yaml
regex_id: 6ca26116f5df8f24d9fcae2163ab6d93
schema_version: "1"
kind: usage_mismatch
corpus: kubilitics
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/kubilitics/rules/kubilitics-frontend/src/pages/ConfigMapDetail.tsx:40:26"
```

### Pattern

`^[\w-]+:`

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

## usage_mismatch:903b2ee80bc69ea29e4f1a31303d9bd8:search

```yaml
regex_id: 903b2ee80bc69ea29e4f1a31303d9bd8
schema_version: "1"
kind: usage_mismatch
corpus: kubilitics
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/kubilitics/rules/kubilitics-frontend/src/lib/crdRelationshipMatcher.ts:288:16"
```

### Pattern

`[Dd]eployment[Nn]ame$`

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

## usage_mismatch:9c8f9580c1ed8a2b61148a00ddf9ef46:search

```yaml
regex_id: 9c8f9580c1ed8a2b61148a00ddf9ef46
schema_version: "1"
kind: usage_mismatch
corpus: kubilitics
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/kubilitics/rules/kubilitics-frontend/src/lib/crdRelationshipMatcher.ts:285:16"
```

### Pattern

`[Ss]ervice[Nn]ame$`

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

## usage_mismatch:a5e677443e36c81a55db2c40a41e57e9:search

```yaml
regex_id: a5e677443e36c81a55db2c40a41e57e9
schema_version: "1"
kind: usage_mismatch
corpus: kubilitics
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/kubilitics/rules/kubilitics-frontend/src/pages/StatefulSets.tsx:263:23"
```

### Pattern

`^(\d+)\/(\d+)$`

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

## usage_mismatch:b5072c8930408ce604c8d9989ab3b199:search

```yaml
regex_id: b5072c8930408ce604c8d9989ab3b199
schema_version: "1"
kind: usage_mismatch
corpus: kubilitics
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/kubilitics/rules/kubilitics-frontend/src/pages/StatefulSetDetail.tsx:386:32"
```

### Pattern

`^(\d+(?:\.\d+)?)\s*Gi?$`

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

## usage_mismatch:bfe354b45ed00e3f45e1207ad3be7884:search

```yaml
regex_id: bfe354b45ed00e3f45e1207ad3be7884
schema_version: "1"
kind: usage_mismatch
corpus: kubilitics
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/kubilitics/rules/kubilitics-frontend/src/lib/dark-mode-audit.ts:133:2"
```

### Pattern

`\.stories\.(ts|tsx)$`

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

## usage_mismatch:cefeedfc4f6f204c79615dcfcfb3f625:search

```yaml
regex_id: cefeedfc4f6f204c79615dcfcfb3f625
schema_version: "1"
kind: usage_mismatch
corpus: kubilitics
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/kubilitics/rules/kubilitics-frontend/src/pages/StatefulSets.tsx:113:23"
```

### Pattern

`^(\d+)\/(\d+)$`

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

## usage_mismatch:f9038269d22470a339c6ffdc176e861b:search

```yaml
regex_id: f9038269d22470a339c6ffdc176e861b
schema_version: "1"
kind: usage_mismatch
corpus: kubilitics
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/kubilitics/rules/kubilitics-frontend/src/components/resources/YamlDiffUtils.tsx:103:21"
```

### Pattern

`^-?\d+(\.\d+)?$`

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

## usage_mismatch:ff0634824784776a2475892a076b6e0e:search

```yaml
regex_id: ff0634824784776a2475892a076b6e0e
schema_version: "1"
kind: usage_mismatch
corpus: kubilitics
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/kubilitics/rules/kubilitics-frontend/src/lib/dark-mode-audit.ts:132:2"
```

### Pattern

`\.test\.(ts|tsx)$`

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
corpus: kubilitics
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
corpus: kubilitics
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
corpus: kubilitics
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
corpus: kubilitics
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

---
schema_version: "1"
corpus: panther-labs-panther-analysis
findings: 22
---

# panther-labs-panther-analysis batch findings

## usage_mismatch:01baa1fd78ecdd28e497faaa209c1329:search

```yaml
regex_id: 01baa1fd78ecdd28e497faaa209c1329
schema_version: "1"
kind: usage_mismatch
corpus: panther-labs-panther-analysis
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/panther-labs-panther-analysis/rules/rules/aws_waf_rules/aws_waf_managed_ip_reputation.py:5:23"
```

### Pattern

`\.(css|js|png|jpg|jpeg|gif|svg|woff2?|ttf|ico|map)$`

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

## usage_mismatch:0d44b297f93fe1c25e052739d7ff048c:search

```yaml
regex_id: 0d44b297f93fe1c25e052739d7ff048c
schema_version: "1"
kind: usage_mismatch
corpus: panther-labs-panther-analysis
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/panther-labs-panther-analysis/rules/global_helpers/panther_gcp_helpers.py:108:4"
```

### Pattern

`^.*\.svc\.id\.goog\[kube-system/.*\]$`

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

## usage_mismatch:1d4758484ec46fb6f0609301c60037b5:search

```yaml
regex_id: 1d4758484ec46fb6f0609301c60037b5
schema_version: "1"
kind: usage_mismatch
corpus: panther-labs-panther-analysis
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/panther-labs-panther-analysis/rules/global_helpers/panther_gcp_helpers.py:104:4"
```

### Pattern

`^service-[\d]+@container-engine-robot\.iam\.gserviceaccount\.com$`

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

## usage_mismatch:48df58012b29e9de976cc0fdc3e69385:match

```yaml
regex_id: 48df58012b29e9de976cc0fdc3e69385
schema_version: "1"
kind: usage_mismatch
corpus: panther-labs-panther-analysis
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/panther-labs-panther-analysis/rules/global_helpers/panther_base_helpers.py:200:11"
```

### Pattern

`^[A-Za-z0-9+/]*={0,2}$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4c7582eb6eacfa2e8cc2de597d6985ce:search

```yaml
regex_id: 4c7582eb6eacfa2e8cc2de597d6985ce
schema_version: "1"
kind: usage_mismatch
corpus: panther-labs-panther-analysis
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/panther-labs-panther-analysis/rules/.scripts/mitre_mapping_check.py:13:16"
```

### Pattern

`^TA\d+\:T\d+(\.\d+)?$`

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

## usage_mismatch:4e81aad9682ed62f99db4247085ccfa5:search

```yaml
regex_id: 4e81aad9682ed62f99db4247085ccfa5
schema_version: "1"
kind: usage_mismatch
corpus: panther-labs-panther-analysis
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/panther-labs-panther-analysis/rules/global_helpers/panther_gcp_helpers.py:105:4"
```

### Pattern

`^service-[\d]+@containerregistry\.iam\.gserviceaccount\.com$`

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

## usage_mismatch:50367392bbf9ebc4fa3a67711953db9a:search

```yaml
regex_id: 50367392bbf9ebc4fa3a67711953db9a
schema_version: "1"
kind: usage_mismatch
corpus: panther-labs-panther-analysis
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/panther-labs-panther-analysis/rules/.scripts/deleted_rules.py:13:15"
```

### Pattern

`^[+-](?:RuleID|PolicyID|QueryName):\s*"?(.+?)["\n]`

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

## usage_mismatch:5d60244b495362ebd3dbcd7a35390d11:search

```yaml
regex_id: 5d60244b495362ebd3dbcd7a35390d11
schema_version: "1"
kind: usage_mismatch
corpus: panther-labs-panther-analysis
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/panther-labs-panther-analysis/rules/global_helpers/panther_gcp_helpers.py:110:4"
```

### Pattern

`^.*\.svc\.id\.goog\[gke-managed-system/.*\]$`

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

## usage_mismatch:639d7e2b94d502e8f1b1c7f09b63dc79:search

```yaml
regex_id: 639d7e2b94d502e8f1b1c7f09b63dc79
schema_version: "1"
kind: usage_mismatch
corpus: panther-labs-panther-analysis
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/panther-labs-panther-analysis/rules/global_helpers/panther_gcp_helpers.py:101:4"
```

### Pattern

`^container-engine-robot@.*\.iam\.gserviceaccount\.com$`

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

## usage_mismatch:898d1fc8d1bd64ed282463480e0480dd:search

```yaml
regex_id: 898d1fc8d1bd64ed282463480e0480dd
schema_version: "1"
kind: usage_mismatch
corpus: panther-labs-panther-analysis
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/panther-labs-panther-analysis/rules/rules/aws_cloudtrail_rules/aws_imds_credential_exfiltration.py:9:27"
```

### Pattern

`:assumed-role/.+/i-[0-9a-f]+$`

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

## usage_mismatch:af8393b00eda22f34d9a196b4d6ba39e:search

```yaml
regex_id: af8393b00eda22f34d9a196b4d6ba39e
schema_version: "1"
kind: usage_mismatch
corpus: panther-labs-panther-analysis
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/panther-labs-panther-analysis/rules/.scripts/claude_review.py:252:7"
```

### Pattern

`^\*{0,2}Overall:?\*{0,2}\s*\*{0,2}PASS\*{0,2}`

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

## usage_mismatch:b110bf8bbb509c7c8d89ae320932746c:search

```yaml
regex_id: b110bf8bbb509c7c8d89ae320932746c
schema_version: "1"
kind: usage_mismatch
corpus: panther-labs-panther-analysis
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/panther-labs-panther-analysis/rules/.scripts/claude_review.py:246:7"
```

### Pattern

`^\*{0,2}Overall:?\*{0,2}\s*\*{0,2}ISSUES FOUND\*{0,2}`

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

## usage_mismatch:bae5029a315cd646f83f80ee3de0ed97:search

```yaml
regex_id: bae5029a315cd646f83f80ee3de0ed97
schema_version: "1"
kind: usage_mismatch
corpus: panther-labs-panther-analysis
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/panther-labs-panther-analysis/rules/global_helpers/panther_gcp_helpers.py:100:4"
```

### Pattern

`^[\d]+-compute@developer\.gserviceaccount\.com$`

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

## usage_mismatch:c454c9bbf6bb8ce0c6b26a30f064c9ab:search

```yaml
regex_id: c454c9bbf6bb8ce0c6b26a30f064c9ab
schema_version: "1"
kind: usage_mismatch
corpus: panther-labs-panther-analysis
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/panther-labs-panther-analysis/rules/global_helpers/panther_gcp_helpers.py:106:4"
```

### Pattern

`^[\d]+@cloudservices\.gserviceaccount\.com$`

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

## usage_mismatch:c91bf448f7bbbe977ad96ca105a42301:search

```yaml
regex_id: c91bf448f7bbbe977ad96ca105a42301
schema_version: "1"
kind: usage_mismatch
corpus: panther-labs-panther-analysis
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/panther-labs-panther-analysis/rules/global_helpers/panther_gcp_helpers.py:109:4"
```

### Pattern

`^.*\.svc\.id\.goog\[gke-system/.*\]$`

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

## usage_mismatch:d34a25664644f7ddc30dd81878fc5db1:search

```yaml
regex_id: d34a25664644f7ddc30dd81878fc5db1
schema_version: "1"
kind: usage_mismatch
corpus: panther-labs-panther-analysis
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/panther-labs-panther-analysis/rules/global_helpers/panther_gcp_helpers.py:102:4"
```

### Pattern

`^gke-[\d]+@.*\.iam\.gserviceaccount\.com$`

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

## usage_mismatch:d3578b51bc77b6df15e0ad727ed1ad4d:match

```yaml
regex_id: d3578b51bc77b6df15e0ad727ed1ad4d
schema_version: "1"
kind: usage_mismatch
corpus: panther-labs-panther-analysis
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/panther-labs-panther-analysis/rules/global_helpers/panther_base_helpers.py:197:26"
```

### Pattern

`^[A-Za-z0-9]{32}$`

### Context

```json
{"call_kind": "match", "reason": "full-anchored pattern via match (fullmatch likely intended)"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d4e8aeaa777b69214e57b826d908c049:search

```yaml
regex_id: d4e8aeaa777b69214e57b826d908c049
schema_version: "1"
kind: usage_mismatch
corpus: panther-labs-panther-analysis
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/panther-labs-panther-analysis/rules/rules/auth0_rules/auth0_user_invitation_created.py:5:9"
```

### Pattern

`^/api/v2/organizations/[^/\s]+/invitations$`

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
corpus: panther-labs-panther-analysis
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
corpus: panther-labs-panther-analysis
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
corpus: panther-labs-panther-analysis
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
corpus: panther-labs-panther-analysis
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

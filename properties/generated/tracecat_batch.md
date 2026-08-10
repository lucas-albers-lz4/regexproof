---
schema_version: "1"
corpus: tracecat
findings: 24
---

# tracecat batch findings

## usage_mismatch:12a071ba38675c43bb751e01ee05955f:search

```yaml
regex_id: 12a071ba38675c43bb751e01ee05955f
schema_version: "1"
kind: usage_mismatch
corpus: tracecat
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/tracecat/rules/tracecat/agent/sandbox/config.py:46:23"
```

### Pattern

`^[A-Za-z_][A-Za-z0-9_]*$`

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

## usage_mismatch:154d796b41276180a16da6b701da42fe:match

```yaml
regex_id: 154d796b41276180a16da6b701da42fe
schema_version: "1"
kind: usage_mismatch
corpus: tracecat
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/tracecat/rules/tracecat/integrations/mcp_validation.py:267:11"
```

### Pattern

`^[a-zA-Z0-9_-]+$`

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

## usage_mismatch:15b392c7309faca5c29c7ade9a5546a8:search

```yaml
regex_id: 15b392c7309faca5c29c7ade9a5546a8
schema_version: "1"
kind: usage_mismatch
corpus: tracecat
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/tracecat/rules/tracecat/sandbox/executor.py:71:23"
```

### Pattern

`^[A-Za-z_][A-Za-z0-9_]*$`

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

## usage_mismatch:17aa40eb89435c5c4bbf66d2ed12186d:search

```yaml
regex_id: 17aa40eb89435c5c4bbf66d2ed12186d
schema_version: "1"
kind: usage_mismatch
corpus: tracecat
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/tracecat/rules/tracecat/sanitization.py:9:24"
```

### Pattern

`^(https?://)[^/@]*@`

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

## usage_mismatch:23809e0604cf2c9c81f9dbf7a4ebf02f:search

```yaml
regex_id: 23809e0604cf2c9c81f9dbf7a4ebf02f
schema_version: "1"
kind: usage_mismatch
corpus: tracecat
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/tracecat/rules/tracecat/registry/sync/jobs.py:37:23"
```

### Pattern

`^(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)(?:-(?P<stage>alpha|a|beta|b|rc|dev|post)\.(?P<number>\d+)(?:-(?P<sub_stage>alpha|a|beta|b|rc|dev|post)\.(?P<sub_number>\d+))?)?$`

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

## usage_mismatch:23852de6a700aa5dd611b01251e49c57:search

```yaml
regex_id: 23852de6a700aa5dd611b01251e49c57
schema_version: "1"
kind: usage_mismatch
corpus: tracecat
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/tracecat/rules/tracecat/tables/schemas.py:17:21"
```

### Pattern

`^[a-zA-Z_][a-zA-Z0-9_]*$`

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

## usage_mismatch:366827647204d158db9d4878d1312d40:search

```yaml
regex_id: 366827647204d158db9d4878d1312d40
schema_version: "1"
kind: usage_mismatch
corpus: tracecat
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/tracecat/rules/tracecat/expressions/patterns.py:8:22"
```

### Pattern

`^\${{\s*(?:(?!\${{).)*?\s*}}$`

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

## usage_mismatch:4a759cd1bee01306573adb6b652c0f38:search

```yaml
regex_id: 4a759cd1bee01306573adb6b652c0f38
schema_version: "1"
kind: usage_mismatch
corpus: tracecat
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/tracecat/rules/tracecat/cases/service.py:187:19"
```

### Pattern

`^(?:CASE-)?(\d{1,10})$`

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

## usage_mismatch:51cad7fdc41227a1f864ebb16a8bb830:search

```yaml
regex_id: 51cad7fdc41227a1f864ebb16a8bb830
schema_version: "1"
kind: usage_mismatch
corpus: tracecat
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/tracecat/rules/tracecat/authz/controls.py:18:16"
```

### Pattern

`^[a-z0-9:_.*-]+$`

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

## usage_mismatch:69ede7ea5d9a354473ebb063912f6433:search

```yaml
regex_id: 69ede7ea5d9a354473ebb063912f6433
schema_version: "1"
kind: usage_mismatch
corpus: tracecat
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/tracecat/rules/tracecat/git/constants.py:3:20"
```

### Pattern

`^git\+ssh://(?P<user>[^/@:]+)@(?P<host>[^/:]+)(?::(?P<port>\d+))?/(?P<path>[^/@]+?(?:/[^/@]+?)+?)(?:\.git)?(?:@(?P<ref>[^@]+))?$`

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

## usage_mismatch:701a289f28885aa00dbee78d9233a721:match

```yaml
regex_id: 701a289f28885aa00dbee78d9233a721
schema_version: "1"
kind: usage_mismatch
corpus: tracecat
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/tracecat/rules/tracecat/integrations/mcp_validation.py:178:11"
```

### Pattern

`^[A-Za-z_][A-Za-z0-9_]*$`

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

## usage_mismatch:76e4541721f81a8305434eef16f1237e:search

```yaml
regex_id: 76e4541721f81a8305434eef16f1237e
schema_version: "1"
kind: usage_mismatch
corpus: tracecat
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/tracecat/rules/tracecat/mcp/auth.py:88:20"
```

### Pattern

`^(?:organization|org|organization_id|org_id):(?P<uuid>[0-9a-fA-F-]{36})$`

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

## usage_mismatch:7cabb0df7172df3891340dfb39e35b58:search

```yaml
regex_id: 7cabb0df7172df3891340dfb39e35b58
schema_version: "1"
kind: usage_mismatch
corpus: tracecat
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/tracecat/rules/tracecat/agent/sandbox/llm_proxy.py:40:33"
```

### Pattern

`/v\d+/?$`

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

## usage_mismatch:93227dd370c3f940f04b7a3deb5b6ab3:search

```yaml
regex_id: 93227dd370c3f940f04b7a3deb5b6ab3
schema_version: "1"
kind: usage_mismatch
corpus: tracecat
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/tracecat/rules/tracecat/tables/common.py:320:26"
```

### Pattern

`::[A-Za-z_][\w\. ]*(\[\])?\s*$`

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

## usage_mismatch:97d19e22886bd64520c9b7045a243be4:search

```yaml
regex_id: 97d19e22886bd64520c9b7045a243be4
schema_version: "1"
kind: usage_mismatch
corpus: tracecat
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/tracecat/rules/tracecat/sandbox/executor.py:74:21"
```

### Pattern

`^[a-f0-9]+$`

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

## usage_mismatch:b77a3864e88544088e1974d4b3bc0156:search

```yaml
regex_id: b77a3864e88544088e1974d4b3bc0156
schema_version: "1"
kind: usage_mismatch
corpus: tracecat
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/tracecat/rules/tracecat/middleware/request.py:11:28"
```

### Pattern

`^(?P<product>Mozilla|TracecatClient|curl|python-httpx|Claude-Code|Codex)/(?P<version>\d{1,4}(?:\.\d{1,4}){0,3})\b`

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

## usage_mismatch:f1328fa9b045ef510ee1c4c325542541:search

```yaml
regex_id: f1328fa9b045ef510ee1c4c325542541
schema_version: "1"
kind: usage_mismatch
corpus: tracecat
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/tracecat/rules/packages/tracecat-registry/tracecat_registry/core/email.py:18:21"
```

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

None

## usage_mismatch:f32ef33ea03232c1f5e7b4fc736d362c:search

```yaml
regex_id: f32ef33ea03232c1f5e7b4fc736d362c
schema_version: "1"
kind: usage_mismatch
corpus: tracecat
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/tracecat/rules/tracecat/executor/secret_preprocessors.py:89:24"
```

### Pattern

`^arn:aws(?:-[a-z0-9-]+)?:iam::\d{12}:role/[\w+=,.@\-/]+$`

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

## usage_mismatch:f967b20b9b7641182a72ef5402948e56:search

```yaml
regex_id: f967b20b9b7641182a72ef5402948e56
schema_version: "1"
kind: usage_mismatch
corpus: tracecat
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/tracecat/rules/tracecat/mcp/auth.py:91:17"
```

### Pattern

`^(?:workspace|workspace_id):(?P<uuid>[0-9a-fA-F-]{36})$`

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

## intent_mismatch:fb72fc2a7e4841d47c5f44edbda5b4d6:url

```yaml
regex_id: fb72fc2a7e4841d47c5f44edbda5b4d6
schema_version: "1"
kind: intent_mismatch
corpus: tracecat
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/tracecat/rules/tracecat/sanitization.py:51:15"
```

### Pattern

`[?#].*$`

### Context

```json
{"admitted_char": "'\\n'", "keyword": "url", "reason": "name/comment claims validation but pattern admits excluded char"}
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
corpus: tracecat
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
corpus: tracecat
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
corpus: tracecat
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
corpus: tracecat
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

---
schema_version: "1"
corpus: octo-server
findings: 34
---

# octo-server batch findings

## usage_mismatch:07d0031da6f60f25f39751c5f0037148:search

```yaml
regex_id: 07d0031da6f60f25f39751c5f0037148
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/internal/cardactiondispatch/registry.go:31:0"
```

### Pattern

`^[a-z][a-z0-9-]{0,63}$`

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

## usage_mismatch:1a69c6e465cea917c12a9260402182ee:search

```yaml
regex_id: 1a69c6e465cea917c12a9260402182ee
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/tools/migrate-rename/main.go:85:0"
```

### Pattern

`^(?P<date>\d{8})(?P<seq>\d{6})_(?P<module>[a-z][a-z_0-9]*?)(?:_legacy(?P<nn>\d{2}))?(?:_[a-z0-9_]+)?\.sql$`

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

## usage_mismatch:30952b9e764bc4620cf68e6b025f729c:search

```yaml
regex_id: 30952b9e764bc4620cf68e6b025f729c
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/pkg/space/channel.go:11:0"
```

### Pattern

`^s([0-9a-f]{32})_`

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

## usage_mismatch:324a2e3e8f445aff932d0e5aaa520569:search

```yaml
regex_id: 324a2e3e8f445aff932d0e5aaa520569
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/pkg/cardtmpl/json_artifact.go:59:0"
```

### Pattern

`^[a-z][a-z0-9_.-]{0,127}$`

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

## usage_mismatch:4282ab619ff5325820d760e4bdd76c34:search

```yaml
regex_id: 4282ab619ff5325820d760e4bdd76c34
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/modules/sticker/model.go:69:0"
```

### Pattern

`^[a-z0-9_]{2,32}$`

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

## usage_mismatch:593112dae18f7e132d34e302f4ea2814:search

```yaml
regex_id: 593112dae18f7e132d34e302f4ea2814
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/modules/common/api.go:513:0"
```

### Pattern

`^[a-z0-9][a-z0-9_-]{0,63}$`

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

## usage_mismatch:59de3810875b81d49a78fcf43ac4003a:search

```yaml
regex_id: 59de3810875b81d49a78fcf43ac4003a
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/internal/cardactiondispatch/registry.go:33:0"
```

### Pattern

`^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$`

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

## usage_mismatch:5ccd32884b9bf3482b20beaaa3346f59:search

```yaml
regex_id: 5ccd32884b9bf3482b20beaaa3346f59
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/modules/card_template_catalog/api_state.go:22:0"
```

### Pattern

`^[a-z][a-z0-9]*(?:[.-][a-z0-9][a-z0-9-]*)+$`

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

## usage_mismatch:5e62fdfffc7b4e671f884c98261edfe6:search

```yaml
regex_id: 5e62fdfffc7b4e671f884c98261edfe6
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/pkg/cardtmpl/approval_request.go:30:0"
```

### Pattern

`^[a-z][a-z0-9_.-]{0,127}$`

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

## usage_mismatch:67e09a72ab489c847c2a678e115cf9cb:search

```yaml
regex_id: 67e09a72ab489c847c2a678e115cf9cb
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/modules/bot_api/commands.go:57:0"
```

### Pattern

`^s\d+_(.+)$`

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

## usage_mismatch:6a3a1be104b88137a73b2e6f65029c21:search

```yaml
regex_id: 6a3a1be104b88137a73b2e6f65029c21
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/modules/oidc/config.go:17:0"
```

### Pattern

`^[a-z0-9][a-z0-9_-]{0,63}$`

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

## usage_mismatch:6fd39f233cb01f450ef70299f2df786d:search

```yaml
regex_id: 6fd39f233cb01f450ef70299f2df786d
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/pkg/cardtmpl/approval_request.go:29:0"
```

### Pattern

`^[a-z][a-z0-9-]{0,63}$`

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

## usage_mismatch:74ab9df93f19ce954c47426ac3df73a6:search

```yaml
regex_id: 74ab9df93f19ce954c47426ac3df73a6
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/modules/sticker/model.go:135:0"
```

### Pattern

`(?:^|/)sticker/([^/]+)/[^/]+\.([A-Za-z0-9]+)$`

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

## usage_mismatch:760234a031449bd65447b0e60f53fdb3:search

```yaml
regex_id: 760234a031449bd65447b0e60f53fdb3
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/modules/sticker/model.go:177:0"
```

### Pattern

`^sticker/([^/]+)/([^/]+)\.([A-Za-z0-9]+)$`

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

## usage_mismatch:7b9856dfaf6eacf1d625b92d826a67a8:search

```yaml
regex_id: 7b9856dfaf6eacf1d625b92d826a67a8
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/internal/cardactiondispatch/registry.go:32:0"
```

### Pattern

`^[a-z][a-z0-9_.-]{0,127}$`

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

## usage_mismatch:87ff7e20c37e21c9ee970d346347c210:search

```yaml
regex_id: 87ff7e20c37e21c9ee970d346347c210
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/internal/cardactiondispatch/registry.go:34:0"
```

### Pattern

`^[A-Z][A-Z0-9_]{0,127}$`

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

## usage_mismatch:89c2ca19a273c9699302b4e2e0c7d474:search

```yaml
regex_id: 89c2ca19a273c9699302b4e2e0c7d474
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/pkg/i18n/codes/registry.go:43:0"
```

### Pattern

`^err\.(shared|server)\.[a-z0-9_]+(\.[a-z0-9_]+)*$`

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

## usage_mismatch:9ede286fc6411041d97dc68db0d155b8:search

```yaml
regex_id: 9ede286fc6411041d97dc68db0d155b8
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/pkg/cardtmpl/json_artifact.go:52:0"
```

### Pattern

`^[a-z][a-z0-9_.-]{0,63}$`

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

## usage_mismatch:a00b78506007a2260c608ca4df3a59bd:search

```yaml
regex_id: a00b78506007a2260c608ca4df3a59bd
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/pkg/cardtmpl/json_artifact.go:53:0"
```

### Pattern

`^[a-z][a-z0-9]*(?:[.-][a-z0-9][a-z0-9-]*)+$`

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

## usage_mismatch:a1e5d04b9046a7b615514460692eb8f9:search

```yaml
regex_id: a1e5d04b9046a7b615514460692eb8f9
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/pkg/cardtmpl/approval_request.go:35:0"
```

### Pattern

`^[a-z][a-z0-9_.-]{0,47}$`

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

## usage_mismatch:a1eb94c44dd84e4775faf2c0f622a497:search

```yaml
regex_id: a1eb94c44dd84e4775faf2c0f622a497
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/modules/app_bot/app_bot.go:60:0"
```

### Pattern

`^[a-z0-9][a-z0-9_-]{0,29}$`

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

## usage_mismatch:a205ae6071b4167cc1f998378ede7854:search

```yaml
regex_id: a205ae6071b4167cc1f998378ede7854
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/tools/migrate-rename/rewrite_initdb.go:60:0"
```

### Pattern

`(?m)^(INSERT INTO `gorp_migrations` VALUES\s*\(\s*')([^']+)('.*)$`

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

## usage_mismatch:ae98ef329bc3345e0e7560d1f8a76066:search

```yaml
regex_id: ae98ef329bc3345e0e7560d1f8a76066
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/modules/openapi/api.go:42:0"
```

### Pattern

`^[a-zA-Z0-9_\-]+$`

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

## usage_mismatch:b15b129b803adc1e8acaf2c2ae1ce830:search

```yaml
regex_id: b15b129b803adc1e8acaf2c2ae1ce830
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/pkg/cardmsg/inputs.go:36:0"
```

### Pattern

`^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][-+]?[0-9]+)?$`

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

## usage_mismatch:c993ed4afa9ae6cb23b2048699bc4a8a:search

```yaml
regex_id: c993ed4afa9ae6cb23b2048699bc4a8a
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/modules/sticker/model.go:178:0"
```

### Pattern

`(?:^|/)sticker/([^/]+)/([^/]+)\.([A-Za-z0-9]+)$`

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

## usage_mismatch:d019a3f407a4da8f51496e9c9f0f816c:search

```yaml
regex_id: d019a3f407a4da8f51496e9c9f0f816c
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/modules/common/system_settings.go:416:0"
```

### Pattern

`^[a-z0-9][a-z0-9_-]{0,63}$`

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

## usage_mismatch:d1a9dad77c01e985efd273964fa9bb97:search

```yaml
regex_id: d1a9dad77c01e985efd273964fa9bb97
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/modules/oidc/api.go:51:0"
```

### Pattern

`^[A-Za-z0-9_-]{1,128}$`

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

## usage_mismatch:e47de23ae4c9d36b8c50171fbf50d290:search

```yaml
regex_id: e47de23ae4c9d36b8c50171fbf50d290
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/internal/carddispatch/registry.go:16:0"
```

### Pattern

`^[a-z][a-z0-9-]{0,63}$`

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

## usage_mismatch:f381190bc5efc1545aa0e3bb42ad63db:search

```yaml
regex_id: f381190bc5efc1545aa0e3bb42ad63db
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/pkg/cardtmpl/approval_request.go:31:0"
```

### Pattern

`^[a-z][a-z0-9_.-]{0,63}$`

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

## usage_mismatch:f3984dd8d415c11d25d2bdad7d18d118:search

```yaml
regex_id: f3984dd8d415c11d25d2bdad7d18d118
schema_version: "1"
kind: usage_mismatch
corpus: octo-server
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/octo-server/rules/tools/migrate-rename/main.go:76:0"
```

### Pattern

`^(?P<module>[a-z][a-z_]*?)[-_](?P<date>\d{8}(?:\d{4})?)(?:-(?P<nn>\d{2}))?\.sql$`

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
corpus: octo-server
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
corpus: octo-server
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
corpus: octo-server
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
corpus: octo-server
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

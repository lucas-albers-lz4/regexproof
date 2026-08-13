---
schema_version: "1"
corpus: mobissh
findings: 29
---

# mobissh batch findings

## usage_mismatch:320172819ae17cae5f6a56767b48f321:search

```yaml
regex_id: 320172819ae17cae5f6a56767b48f321
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/src/modules/ime.ts:220:21"
```

### Pattern

`(?:password|passphrase|PIN)[^:]*:\s*$`

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

## usage_mismatch:33d8ff5b7c945670971eea613fca262b:search

```yaml
regex_id: 33d8ff5b7c945670971eea613fca262b
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/server/index.js:102:4"
```

### Pattern

`^mobissh-[\w.+-]+\.aab$`

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

## usage_mismatch:3828c1203000a44a7e92091c8df9a077:search

```yaml
regex_id: 3828c1203000a44a7e92091c8df9a077
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/src/modules/forwards.ts:275:9"
```

### Pattern

`^[A-Za-z0-9+/]*={0,2}$`

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

## usage_mismatch:418ec3ec9e2026d67cfe634db20b8c78:search

```yaml
regex_id: 418ec3ec9e2026d67cfe634db20b8c78
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/src/modules/sftp-preview.ts:187:26"
```

### Pattern

`^## (.+)`

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

## usage_mismatch:481b69beba70f6725669e30e8f9a0e2d:search

```yaml
regex_id: 481b69beba70f6725669e30e8f9a0e2d
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/src/modules/sftp-preview.ts:146:19"
```

### Pattern

`^````

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

## usage_mismatch:54ecfb2120256106dde4473131183e06:search

```yaml
regex_id: 54ecfb2120256106dde4473131183e06
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/server/index.js:1263:25"
```

### Pattern

`^::ffff:(\d+\.\d+\.\d+\.\d+)$`

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

## usage_mismatch:5f3d9a58225fc5520686e8105268f153:search

```yaml
regex_id: 5f3d9a58225fc5520686e8105268f153
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/tools/review-server/serve.js:394:26"
```

### Pattern

`^(.+?)-\d+-`

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

## usage_mismatch:6661647ff32435103b784766d361b0cb:search

```yaml
regex_id: 6661647ff32435103b784766d361b0cb
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/src/modules/ime.ts:932:33"
```

### Pattern

`\S+\s*$`

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

## usage_mismatch:708ba406c4742a1e6300e6a8edeb8fc1:search

```yaml
regex_id: 708ba406c4742a1e6300e6a8edeb8fc1
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/server/index.js:1275:24"
```

### Pattern

`^(\d+)\.(\d+)\.(\d+)\.(\d+)$`

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

## usage_mismatch:73690725d99d843ba6284f9958da2930:search

```yaml
regex_id: 73690725d99d843ba6284f9958da2930
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/server/index.js:97:4"
```

### Pattern

`^mobissh-native-macos(-[\w.+-]+)?\.zip$`

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

## usage_mismatch:751706f825184e6329cc8184ac5e18b0:search

```yaml
regex_id: 751706f825184e6329cc8184ac5e18b0
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/src/modules/sftp-preview.ts:165:31"
```

### Pattern

`^\|.+\|$`

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

## usage_mismatch:7c33a65628f8e534178d8e79face7ac3:search

```yaml
regex_id: 7c33a65628f8e534178d8e79face7ac3
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/server/index.js:1240:24"
```

### Pattern

`^(\d+)\.(\d+)\.(\d+)\.(\d+)$`

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

## usage_mismatch:9e054174e4bb0f4c454e566615d716f7:search

```yaml
regex_id: 9e054174e4bb0f4c454e566615d716f7
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/src/modules/sftp-preview.ts:281:27"
```

### Pattern

`^([a-z][a-z0-9+\-.]*):`

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

## usage_mismatch:a408937a95409e70728a02afcecdd765:search

```yaml
regex_id: a408937a95409e70728a02afcecdd765
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/src/modules/sftp-preview.ts:165:90"
```

### Pattern

`^\|[\s|:-]+$`

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

## usage_mismatch:a6dff3b282561635be195dc94148efaa:search

```yaml
regex_id: a6dff3b282561635be195dc94148efaa
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/tools/review-server/serve.js:537:35"
```

### Pattern

`\.(mp4|webm)$`

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

## usage_mismatch:a83a5d42e37443e946f1fc355d451812:search

```yaml
regex_id: a83a5d42e37443e946f1fc355d451812
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/server/index.js:92:4"
```

### Pattern

`^mobissh-native(-[\w.+-]+)?\.apk$`

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

## usage_mismatch:ac3714597876f9cde3e179b4753959ba:search

```yaml
regex_id: ac3714597876f9cde3e179b4753959ba
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/src/modules/sftp-preview.ts:272:9"
```

### Pattern

`^[a-z][a-z0-9+\-.]*:`

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

## usage_mismatch:be6e5d8ee83c371486c9bdbaedd0c062:search

```yaml
regex_id: be6e5d8ee83c371486c9bdbaedd0c062
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/server-feedback/test.js:174:23"
```

### Pattern

`-native-crash\.json$`

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

## usage_mismatch:c2d6a476d3956e5b92ccec550b11a51b:search

```yaml
regex_id: c2d6a476d3956e5b92ccec550b11a51b
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/tools/review-server/serve.js:536:35"
```

### Pattern

`\.(png|jpg|jpeg|webp)$`

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

## usage_mismatch:c3c170ef4b4f0975fbad3cc9fdff2799:search

```yaml
regex_id: c3c170ef4b4f0975fbad3cc9fdff2799
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/src/modules/sftp-preview.ts:193:26"
```

### Pattern

`^- (.+)`

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

## usage_mismatch:d5936ec2d2720beefe6434837e9bbd5b:search

```yaml
regex_id: d5936ec2d2720beefe6434837e9bbd5b
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/src/modules/selection.ts:107:22"
```

### Pattern

`^at\s+(<anonymous>|\(<anonymous>\))$`

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

## usage_mismatch:da32bd55d8fabd20a3fe5638100474ae:search

```yaml
regex_id: da32bd55d8fabd20a3fe5638100474ae
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/server-feedback/test.js:184:23"
```

### Pattern

`-native-crash\.raw$`

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

## usage_mismatch:dd340b1771c76320e946c2976131e831:search

```yaml
regex_id: dd340b1771c76320e946c2976131e831
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/src/modules/sftp-preview.ts:185:26"
```

### Pattern

`^### (.+)`

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

## usage_mismatch:edd25911296d3ebb164bdbbefeb80f03:search

```yaml
regex_id: edd25911296d3ebb164bdbbefeb80f03
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/src/modules/sftp-preview.ts:175:21"
```

### Pattern

`^\|.+\|$`

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

## usage_mismatch:f5e8b27b2a41f68715edea03b7f7bd63:search

```yaml
regex_id: f5e8b27b2a41f68715edea03b7f7bd63
schema_version: "1"
kind: usage_mismatch
corpus: mobissh
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/mobissh/rules/src/modules/sftp-preview.ts:189:26"
```

### Pattern

`^# (.+)`

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
corpus: mobissh
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
corpus: mobissh
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
corpus: mobissh
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
corpus: mobissh
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

---
schema_version: "1"
corpus: lyrie-ai
findings: 171
---

# lyrie-ai batch findings

## usage_mismatch:01215d60f08bcac1cd2d0a40d5a8e764:search

```yaml
regex_id: 01215d60f08bcac1cd2d0a40d5a8e764
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/skills/ai-pentest/scanner.ts:64:8"
```

### Pattern

`^[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$`

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

## usage_mismatch:0302759f688c57ac58f6a3c1d96e8b9f:search

```yaml
regex_id: 0302759f688c57ac58f6a3c1d96e8b9f
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/stages-validator.ts:273:23"
```

### Pattern

`^\s*(\/\/|#|\*|--)`

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

## usage_mismatch:0338e8126e6ef6af280f0f5095a8c976:search

```yaml
regex_id: 0338e8126e6ef6af280f0f5095a8c976
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/ui/src/sarif-viewer/parse.ts:110:50"
```

### Pattern

`^https?:\/\/`

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

## usage_mismatch:03b59dcb76080900dbde954f7d9b483a:search

```yaml
regex_id: 03b59dcb76080900dbde954f7d9b483a
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/scripts/backend.ts:33:22"
```

### Pattern

`^--([^=]+)=(.*)$`

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

## usage_mismatch:06e99ff44fa77644636b4426f860ac1b:search

```yaml
regex_id: 06e99ff44fa77644636b4426f860ac1b
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/action/runner.ts:125:4"
```

### Pattern

`edit-engine\.test\.ts$`

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

## usage_mismatch:0733bba315200833f3bfa481ea7c1709:search

```yaml
regex_id: 0733bba315200833f3bfa481ea7c1709
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/action/runner.ts:119:4"
```

### Pattern

`\.lock$`

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

## usage_mismatch:07aed20b7bb091d14c6cb286e69c3a61:search

```yaml
regex_id: 07aed20b7bb091d14c6cb286e69c3a61
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/scanners/taint-engine.ts:315:55"
```

### Pattern

`^(\s*)`

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

## usage_mismatch:0809fee4666d4d27da739c23d4f9dbb3:search

```yaml
regex_id: 0809fee4666d4d27da739c23d4f9dbb3
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/tools-catalog/catalog.test.ts:46:30"
```

### Pattern

`^[a-z0-9-]+$`

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

## usage_mismatch:09ea95f9e6d22a4575b7820163ebffd7:search

```yaml
regex_id: 09ea95f9e6d22a4575b7820163ebffd7
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/memory/integrity-checker.test.ts:84:11"
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

## usage_mismatch:0b96ca165466450a70a98198b4f7a415:search

```yaml
regex_id: 0b96ca165466450a70a98198b4f7a415
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/stages-validator.ts:444:4"
```

### Pattern

`\.seed\.[jt]sx?$`

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

## usage_mismatch:0ef89b6b599de80aab810768dec172ba:search

```yaml
regex_id: 0ef89b6b599de80aab810768dec172ba
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/attack-surface.ts:202:2"
```

### Pattern

`\.min\.(js|css)$`

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

## usage_mismatch:1018adb9579d9c31f999ee2d7ba2d1e1:search

```yaml
regex_id: 1018adb9579d9c31f999ee2d7ba2d1e1
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/proxy/proxy.test.ts:313:34"
```

### Pattern

`^lyrie-http-proxy-`

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

## usage_mismatch:118fabd58457af1108f871276c40942a:search

```yaml
regex_id: 118fabd58457af1108f871276c40942a
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/attack-surface.ts:201:2"
```

### Pattern

`\.lock$`

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

## usage_mismatch:1191266ff9524c7541d6e948e43870b8:search

```yaml
regex_id: 1191266ff9524c7541d6e948e43870b8
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/hack/dependency-graph.ts:324:28"
```

### Pattern

`^([A-Za-z0-9_.\-]+)(?:\[[^\]]*\])?\s*(?:([<>=!~]=?)\s*([\d.\w]+))?`

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

## usage_mismatch:11e555bb459a9ab43740717b9d4c9619:search

```yaml
regex_id: 11e555bb459a9ab43740717b9d4c9619
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/hack/secret-detector.ts:373:4"
```

### Pattern

`^x+$`

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

## usage_mismatch:1245ae58e05be95003865f21f5c458a0:search

```yaml
regex_id: 1245ae58e05be95003865f21f5c458a0
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/oss-scan/service.ts:257:4"
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

## usage_mismatch:15650ba3ac115980e05cca6ffbba2061:search

```yaml
regex_id: 15650ba3ac115980e05cca6ffbba2061
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/attack-surface.ts:437:17"
```

### Pattern

`^\s*([a-zA-Z0-9_\-]+)\s*=\s*["'][^"']+["']`

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

## usage_mismatch:15e08e31ecb101e6174d1e1a09aacc6e:search

```yaml
regex_id: 15e08e31ecb101e6174d1e1a09aacc6e
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/action/runner.ts:118:4"
```

### Pattern

`\.pyo$`

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

## usage_mismatch:1741430ecb89a47caa7f1bb7d4d1264c:search

```yaml
regex_id: 1741430ecb89a47caa7f1bb7d4d1264c
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/skills/ai-pentest/vuln-scanner.ts:516:37"
```

### Pattern

`^[A-Z_]+=.+`

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

## usage_mismatch:19277a316e40344156e6bd57e7bb1fef:search

```yaml
regex_id: 19277a316e40344156e6bd57e7bb1fef
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/scanners/taint-engine.ts:340:10"
```

### Pattern

`^\s*([A-Za-z_$][\w$]*)\s*[:=]\s*`

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

## intent_mismatch:1c4e0e4ee577fe9c6e59419bc0abc786:url

```yaml
regex_id: 1c4e0e4ee577fe9c6e59419bc0abc786
schema_version: "1"
kind: intent_mismatch
corpus: lyrie-ai
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/security/url-guard.ts:68:26"
```

### Pattern

`^(.*:)?(\d+\.\d+\.\d+\.\d+)$`

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

## usage_mismatch:1c4e0e4ee577fe9c6e59419bc0abc786:search

```yaml
regex_id: 1c4e0e4ee577fe9c6e59419bc0abc786
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/security/url-guard.ts:68:26"
```

### Pattern

`^(.*:)?(\d+\.\d+\.\d+\.\d+)$`

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

## usage_mismatch:1d0e97f7a8c481330fbcfe6b83340a82:search

```yaml
regex_id: 1d0e97f7a8c481330fbcfe6b83340a82
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/hack/auto-remediation.ts:200:88"
```

### Pattern

`\.(?:js|ts|tsx|mjs)$`

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

## usage_mismatch:1dcc09769a38802dfef3a13471ef886d:search

```yaml
regex_id: 1dcc09769a38802dfef3a13471ef886d
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/stages-validator.ts:434:4"
```

### Pattern

`(^|\/)app\.[jt]sx?$`

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

## usage_mismatch:20c38ab880f923ee826e688fc7e40d92:search

```yaml
regex_id: 20c38ab880f923ee826e688fc7e40d92
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/hack/secret-detector.ts:375:4"
```

### Pattern

`^0+$`

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

## usage_mismatch:2201ee5a0ef74e0deb09f3f9d075ef29:search

```yaml
regex_id: 2201ee5a0ef74e0deb09f3f9d075ef29
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/governance/scorecard.test.ts:144:32"
```

### Pattern

`^(GOVERN|MAP|MEASURE|MANAGE)-`

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

## usage_mismatch:226386e96b19fdb3a96e89c04b9c0b73:search

```yaml
regex_id: 226386e96b19fdb3a96e89c04b9c0b73
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/aav/reporter.test.ts:68:52"
```

### Pattern

`^LLM\d{2}-\d{3}$`

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

## usage_mismatch:2377d6ca719154563da0452462bfe218:search

```yaml
regex_id: 2377d6ca719154563da0452462bfe218
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/hack/dependency-graph.ts:449:19"
```

### Pattern

`^\s*([A-Za-z0-9_.\-]+)\s*=\s*(?:\{[^}]*version\s*=\s*["']([^"']+)["']|["']([^"'\n]+)["'])`

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

## usage_mismatch:243612e477dd0d6217013dec63d1bc2c:search

```yaml
regex_id: 243612e477dd0d6217013dec63d1bc2c
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/stages-validator.ts:622:15"
```

### Pattern

`\.py$`

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

## usage_mismatch:24d76d2c52977932cd65ae790e87810f:search

```yaml
regex_id: 24d76d2c52977932cd65ae790e87810f
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/hack/dependency-graph.ts:353:27"
```

### Pattern

`^([A-Za-z0-9_.\-]+)(?:\[[^\]]*\])?\s*(?:([<>=!~]=?)\s*([\d.\w]+))?`

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

## usage_mismatch:2669f75e61d04fd134fa33b6d53f4f0d:search

```yaml
regex_id: 2669f75e61d04fd134fa33b6d53f4f0d
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/security/mcp-scanner.ts:357:29"
```

### Pattern

`@(latest|next|beta|alpha|canary|unstable|rc)$`

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

## usage_mismatch:271c108dfa46bc3e3a3caf3e1d642351:search

```yaml
regex_id: 271c108dfa46bc3e3a3caf3e1d642351
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/migrate/autogpt.ts:238:27"
```

### Pattern

`^([A-Z_]+)=(.+)$`

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

## intent_mismatch:278689c8317f1b27180dba7ada2061aa:email

```yaml
regex_id: 278689c8317f1b27180dba7ada2061aa
schema_version: "1"
kind: intent_mismatch
corpus: lyrie-ai
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/scanners/taint-engine.ts:173:10"
```

### Pattern

`\bvalidator\.(escape|isEmail|isURL|isInt)\s*\(`

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

## usage_mismatch:2c03bde88827dcb1ed1133ecb79e0f8e:search

```yaml
regex_id: 2c03bde88827dcb1ed1133ecb79e0f8e
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/hack/dependency-graph.ts:400:19"
```

### Pattern

`^\s*([A-Za-z0-9_.\-]+)\s*=\s*["']?([^"'\n#]+)["']?`

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

## usage_mismatch:2ca8be7b7ca3ab782c302a03711ea1e1:search

```yaml
regex_id: 2ca8be7b7ca3ab782c302a03711ea1e1
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/skills/skill-loader.ts:13:16"
```

### Pattern

`^---\r?\n([\s\S]*?)\n---\r?\n?([\s\S]*)$`

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

## usage_mismatch:2e6552d8c6e9cd2673f4fb343d725683:search

```yaml
regex_id: 2e6552d8c6e9cd2673f4fb343d725683
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/gateway/src/telegram/media-processor.ts:448:21"
```

### Pattern

`\.(txt|md|json|yaml|yml|xml|csv|log|py|js|ts|sh|bash|rs|go|java|c|cpp|h|hpp|toml|ini|cfg|env|html|css|sql)$`

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

## usage_mismatch:2eaa6da637be78b013b8bd799cc7aad9:search

```yaml
regex_id: 2eaa6da637be78b013b8bd799cc7aad9
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/scripts/redteam.test.ts:106:38"
```

### Pattern

`^aav-`

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

## usage_mismatch:314b5ba6d4c3b66bc82bba7146b8ffb8:search

```yaml
regex_id: 314b5ba6d4c3b66bc82bba7146b8ffb8
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/stages-validator.ts:445:4"
```

### Pattern

`\.migration\.[jt]sx?$`

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

## usage_mismatch:333389c99d2bd444c9b8fd82cdac6356:search

```yaml
regex_id: 333389c99d2bd444c9b8fd82cdac6356
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/oss-scan/service.ts:261:4"
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

## usage_mismatch:334d7747fd528f0be071449db30e9a1b:search

```yaml
regex_id: 334d7747fd528f0be071449db30e9a1b
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/hack/dependency-graph.ts:424:35"
```

### Pattern

`^([\w.\-/]+)\s+(v[\d.\-+\w]+)`

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

## usage_mismatch:34585a10194278da56981277e9c62c0b:search

```yaml
regex_id: 34585a10194278da56981277e9c62c0b
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/hack/secret-detector.test.ts:178:44"
```

### Pattern

`^lyrie-`

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

## usage_mismatch:3490ac1673c82769279181fc93204b54:search

```yaml
regex_id: 3490ac1673c82769279181fc93204b54
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/attack-surface.ts:208:2"
```

### Pattern

`\.webp$`

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

## usage_mismatch:34b2d28bd7ee29f4759426e51879d678:search

```yaml
regex_id: 34b2d28bd7ee29f4759426e51879d678
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/attack-surface.ts:423:17"
```

### Pattern

`^\s*([a-zA-Z0-9_\-]+)\s*=\s*["'][^"']+["']`

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

## usage_mismatch:35d1647082cd40e5ebe426aa4fc0fa04:search

```yaml
regex_id: 35d1647082cd40e5ebe426aa4fc0fa04
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/scanners/taint-engine.ts:270:34"
```

### Pattern

`^\s*(?:async\s+)?def\s+([A-Za-z_]\w*)\s*\(([^)]*)\)`

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

## usage_mismatch:362be927451eddd2436bcbb7f838400b:search

```yaml
regex_id: 362be927451eddd2436bcbb7f838400b
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/action/runner.ts:123:4"
```

### Pattern

`dm-pairing\.(ts|test\.ts)$`

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

## intent_mismatch:3a89c6ba190947c29dd813eec639435e:url

```yaml
regex_id: 3a89c6ba190947c29dd813eec639435e
schema_version: "1"
kind: intent_mismatch
corpus: lyrie-ai
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/security/url-guard.ts:60:25"
```

### Pattern

`%.*$`

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

## usage_mismatch:3a89c6ba190947c29dd813eec639435e:search

```yaml
regex_id: 3a89c6ba190947c29dd813eec639435e
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/security/url-guard.ts:60:25"
```

### Pattern

`%.*$`

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

## usage_mismatch:3fa74c7be6657c17462b2231c58253cf:search

```yaml
regex_id: 3fa74c7be6657c17462b2231c58253cf
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/action/runner.ts:126:4"
```

### Pattern

`memory-core\.test\.ts$`

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

## usage_mismatch:40fa39e8807e085bf87f8c18f1b32cd2:search

```yaml
regex_id: 40fa39e8807e085bf87f8c18f1b32cd2
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/attack-surface.ts:206:2"
```

### Pattern

`\.jpeg$`

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

## intent_mismatch:434e00de7e8761c579a0cfb15ed6a79c:email

```yaml
regex_id: 434e00de7e8761c579a0cfb15ed6a79c
schema_version: "1"
kind: intent_mismatch
corpus: lyrie-ai
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/scanners/taint-engine.ts:129:10"
```

### Pattern

`\bsmtplib\..*sendmail\s*\(`

### Context

```json
{"admitted_char": "'\\n'", "keyword": "email", "reason": "name/comment claims validation but pattern admits excluded char"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:476f64953abceb60a952c733adb01c43:search

```yaml
regex_id: 476f64953abceb60a952c733adb01c43
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/attack-surface.ts:570:43"
```

### Pattern

`^app\/(.+)\/page\.(tsx?|jsx?)$`

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

## usage_mismatch:4d1e6b9c790b2935097376ed19369c31:search

```yaml
regex_id: 4d1e6b9c790b2935097376ed19369c31
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/scanners/taint-engine.ts:314:32"
```

### Pattern

`^(\s*)`

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

## usage_mismatch:4d2c39b7566b74b2b125c355eabbf6dd:search

```yaml
regex_id: 4d2c39b7566b74b2b125c355eabbf6dd
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/stages-validator.ts:446:4"
```

### Pattern

`migrate\.[jt]sx?$`

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

## usage_mismatch:4e5e16a5c685ec8087c0955742ea3750:search

```yaml
regex_id: 4e5e16a5c685ec8087c0955742ea3750
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/hack/dependency-graph.ts:512:13"
```

### Pattern

`^\s*gem\s+["']([^"']+)["'](?:\s*,\s*["']([^"']+)["'])?`

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

## usage_mismatch:4e6d7f284be0e5196f74808e5cbbb37e:search

```yaml
regex_id: 4e6d7f284be0e5196f74808e5cbbb37e
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/attack-surface.ts:319:30"
```

### Pattern

`^[A-Za-z]:\\`

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

## usage_mismatch:51e1fbdad9256def5f545c832fb20a5b:search

```yaml
regex_id: 51e1fbdad9256def5f545c832fb20a5b
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/stages-validator.ts:621:15"
```

### Pattern

`\.(js|jsx|mjs|cjs)$`

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

## usage_mismatch:51f47e0c6eed6cc2c00d5e97beb34c25:search

```yaml
regex_id: 51f47e0c6eed6cc2c00d5e97beb34c25
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/attack-surface.ts:211:2"
```

### Pattern

`\.tar\.gz$`

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

## usage_mismatch:551e166b2b5748369bf9e4f44c67328a:search

```yaml
regex_id: 551e166b2b5748369bf9e4f44c67328a
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/scanners/taint-engine.ts:272:34"
```

### Pattern

`^\s*def\s+([A-Za-z_]\w*[!?]?)\s*(?:\(([^)]*)\))?`

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

## usage_mismatch:558fbda68311ec2625650259e4fdc1ad:search

```yaml
regex_id: 558fbda68311ec2625650259e4fdc1ad
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/scanners/scanners.test.ts:40:32"
```

### Pattern

`^lyrie-`

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

## usage_mismatch:55cb0489ccb88ff2d5f9e2e8f0193c8a:search

```yaml
regex_id: 55cb0489ccb88ff2d5f9e2e8f0193c8a
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/attack-surface.ts:207:2"
```

### Pattern

`\.gif$`

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

## usage_mismatch:56fc2fbfef5c76d92e227fc691c877d4:search

```yaml
regex_id: 56fc2fbfef5c76d92e227fc691c877d4
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/scanners/taint-engine.ts:271:34"
```

### Pattern

`^\s*func\s+(?:\([^)]*\)\s+)?([A-Za-z_]\w*)\s*\(([^)]*)\)`

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

## usage_mismatch:583de6ca384106d07aaa806476b40002:search

```yaml
regex_id: 583de6ca384106d07aaa806476b40002
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/action/runner.test.ts:150:55"
```

### Pattern

`^(none|note|warning|error)$`

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

## usage_mismatch:5acf4aed666cbf71da7f0f219fefb887:search

```yaml
regex_id: 5acf4aed666cbf71da7f0f219fefb887
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/memory/memory-core.ts:901:35"
```

### Pattern

`^##\s+`

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

## intent_mismatch:5d93d54e11c26681157b00a8a3dc994b:url

```yaml
regex_id: 5d93d54e11c26681157b00a8a3dc994b
schema_version: "1"
kind: intent_mismatch
corpus: lyrie-ai
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/security/url-guard.ts:66:23"
```

### Pattern

`%.*$`

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

## usage_mismatch:5e20ea82f54e5129e37621dfeeac1024:search

```yaml
regex_id: 5e20ea82f54e5129e37621dfeeac1024
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/hack/dependency-graph.test.ts:112:45"
```

### Pattern

`^lyrie-`

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

## usage_mismatch:60c5fba5f692a731e904b93289141f07:search

```yaml
regex_id: 60c5fba5f692a731e904b93289141f07
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/hack/auto-remediation.test.ts:55:45"
```

### Pattern

`^lyrie-`

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

## usage_mismatch:614afaf7b8d90223ceef811f9b0dbd99:search

```yaml
regex_id: 614afaf7b8d90223ceef811f9b0dbd99
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/agents/verifier.ts:117:38"
```

### Pattern

`^VERDICT:\s*(PASS|FAIL|PARTIAL)\s*$`

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

## usage_mismatch:6452b01677d135979a104618046aef18:search

```yaml
regex_id: 6452b01677d135979a104618046aef18
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/memory/memory-core.ts:914:102"
```

### Pattern

`^\d+\.`

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

## usage_mismatch:6a3f98dad03703f68e4684f65fc9e5aa:search

```yaml
regex_id: 6a3f98dad03703f68e4684f65fc9e5aa
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/stages-validator.ts:378:32"
```

### Pattern

`\.[jt]sx$`

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

## usage_mismatch:6a55bf8780775f3e505a0b3153b8534d:search

```yaml
regex_id: 6a55bf8780775f3e505a0b3153b8534d
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/atp/tests/aic.test.ts:34:29"
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

## usage_mismatch:6c2e38fb01ca9a6161fdbaed6c9ff5b9:search

```yaml
regex_id: 6c2e38fb01ca9a6161fdbaed6c9ff5b9
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/agents/message-bus.test.ts:123:35"
```

### Pattern

`^msg-\d+-\d+$`

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

## usage_mismatch:6c553d8df13f01e83e7bae81a8090339:search

```yaml
regex_id: 6c553d8df13f01e83e7bae81a8090339
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/mcp/src/registry.ts:219:38"
```

### Pattern

`^mcp:([^:]+):(.+)$`

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

## usage_mismatch:6d9acbc7c005c59f686d4bc9e7b315d2:search

```yaml
regex_id: 6d9acbc7c005c59f686d4bc9e7b315d2
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/stages-validator.test.ts:183:38"
```

### Pattern

`^lyrie-stages-`

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

## usage_mismatch:6dbe65fcc611409d649e778d8e310d83:search

```yaml
regex_id: 6dbe65fcc611409d649e778d8e310d83
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/agents/verifier.ts:120:36"
```

### Pattern

`^### Check:`

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

## usage_mismatch:6e53bc3af9518958a5295b39333be419:search

```yaml
regex_id: 6e53bc3af9518958a5295b39333be419
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/hack/dependency-graph.ts:307:13"
```

### Pattern

`^\s+\/((?:@[\w.-]+\/)?[\w.-]+)\/([\d.]+(?:-[\w.-]+)?)[:_]`

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

## usage_mismatch:73b85e9b9076c373a06ea93a51346e03:search

```yaml
regex_id: 73b85e9b9076c373a06ea93a51346e03
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/poc-gen/poc-gen.test.ts:176:32"
```

### Pattern

`^#!\/usr\/bin\/env python3`

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

## usage_mismatch:743f2e387efbc01711652a6d77ca6da4:search

```yaml
regex_id: 743f2e387efbc01711652a6d77ca6da4
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/skills/builtin-executors.ts:153:8"
```

### Pattern

`^https?:\/\/`

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

## usage_mismatch:75c816832f3872d32a2d266b828621e0:search

```yaml
regex_id: 75c816832f3872d32a2d266b828621e0
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/attack-surface.ts:203:2"
```

### Pattern

`\.map$`

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

## usage_mismatch:7606c396503d85feb2acec869c5ee787:search

```yaml
regex_id: 7606c396503d85feb2acec869c5ee787
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/atp/tests/delegation.test.ts:42:28"
```

### Pattern

`^atp:del:[0-9a-f-]{36}$`

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

## usage_mismatch:781c95b979ca7750d4844df34a354d53:search

```yaml
regex_id: 781c95b979ca7750d4844df34a354d53
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/atp/src/breach.ts:144:44"
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

## usage_mismatch:78d919030e95af796a5fb27a3ca48bfd:search

```yaml
regex_id: 78d919030e95af796a5fb27a3ca48bfd
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/migrate/dify.ts:74:27"
```

### Pattern

`^([A-Z_][A-Z0-9_]*)=(.*)$`

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

## usage_mismatch:78efbc164c272fb041cee4c1e2f5bcb1:search

```yaml
regex_id: 78efbc164c272fb041cee4c1e2f5bcb1
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/security/domain-verify.ts:65:6"
```

### Pattern

`^[a-zA-Z]:\\`

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

## usage_mismatch:7a087f764b39e1f10576d93888d8a5e0:search

```yaml
regex_id: 7a087f764b39e1f10576d93888d8a5e0
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/scripts/daemon.ts:92:6"
```

### Pattern

`^\d+$`

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

## usage_mismatch:7b948cd181573c32226ada25da2959d0:search

```yaml
regex_id: 7b948cd181573c32226ada25da2959d0
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/remediation-pr/dependency-fix.ts:68:42"
```

### Pattern

`^[\^~>=<]+`

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

## usage_mismatch:7bbc8b37ac8a2803f3881c16ea2dbef0:search

```yaml
regex_id: 7bbc8b37ac8a2803f3881c16ea2dbef0
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/stages-validator.ts:623:15"
```

### Pattern

`\.php$`

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

## usage_mismatch:7d155e394e6cf6646c76ea0926797f46:search

```yaml
regex_id: 7d155e394e6cf6646c76ea0926797f46
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/hack/secret-detector.ts:374:4"
```

### Pattern

`^a+$`

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

## usage_mismatch:7f2eaf7a8120480773df4940fe23f11a:search

```yaml
regex_id: 7f2eaf7a8120480773df4940fe23f11a
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/gateway/src/telegram/pentest-handler.ts:306:11"
```

### Pattern

`^[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$`

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

## usage_mismatch:7f7e8c48472600642878d2aec03a6969:search

```yaml
regex_id: 7f7e8c48472600642878d2aec03a6969
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/tools/exec/exec.test.ts:350:6"
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

## usage_mismatch:84f414ed111ae65ed0784ffbc3e87459:search

```yaml
regex_id: 84f414ed111ae65ed0784ffbc3e87459
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/attack-surface.ts:204:2"
```

### Pattern

`\.png$`

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

## usage_mismatch:85ab36ef6c513ce8c4293d006671a400:search

```yaml
regex_id: 85ab36ef6c513ce8c4293d006671a400
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/aav/red-team.test.ts:141:34"
```

### Pattern

`^aav-`

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

## usage_mismatch:87824946d6f102dc7b17341b65e0c9bd:search

```yaml
regex_id: 87824946d6f102dc7b17341b65e0c9bd
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/security/url-guard.ts:61:9"
```

### Pattern

`^[0-9a-f:]+$`

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

## usage_mismatch:8f6a81e12bb5520bd8c8972ea1c63420:search

```yaml
regex_id: 8f6a81e12bb5520bd8c8972ea1c63420
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/hack/secret-detector.ts:199:8"
```

### Pattern

`(?:^|\n)\s*(?:export\s+)?([A-Z][A-Z0-9_]{2,})\s*=\s*["']?([A-Za-z0-9+/=_\-]{20,})["']?\s*$`

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

## usage_mismatch:9043859a2d0af1f7b5b9928777ab9b95:search

```yaml
regex_id: 9043859a2d0af1f7b5b9928777ab9b95
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/threat-intel/client.test.ts:68:41"
```

### Pattern

`^lyrie-threat-intel-`

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

## usage_mismatch:913aa9c0d50432baa8d07e07b42cb7ab:search

```yaml
regex_id: 913aa9c0d50432baa8d07e07b42cb7ab
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/oast/server.test.ts:56:33"
```

### Pattern

`^\d+\.\d+\.\d+$`

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

## usage_mismatch:93cfd15417d1c99edf97ef587ae1c425:search

```yaml
regex_id: 93cfd15417d1c99edf97ef587ae1c425
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/stages-validator.ts:433:4"
```

### Pattern

`(^|\/)server\.[jt]sx?$`

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

## usage_mismatch:948239d088427ccecf6ad4484e8fdb55:search

```yaml
regex_id: 948239d088427ccecf6ad4484e8fdb55
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/scanners/taint-engine.ts:268:34"
```

### Pattern

`^\s*(?:export\s+)?(?:async\s+)?function\s+([A-Za-z_$][\w$]*)\s*\(([^)]*)\)`

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

## usage_mismatch:98f6113fb898c71ccd538bc5344c0093:search

```yaml
regex_id: 98f6113fb898c71ccd538bc5344c0093
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/attack-surface.ts:450:29"
```

### Pattern

`^\s*([\w.\-/]+)\s+v[\d.]+`

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

## usage_mismatch:9ae38276b82a209efd8c73369cf23d27:search

```yaml
regex_id: 9ae38276b82a209efd8c73369cf23d27
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/stages-validator.ts:264:2"
```

### Pattern

`\.test\.[jt]sx?$`

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

## usage_mismatch:9ce13bb576177c1542d11d808c61f3f8:search

```yaml
regex_id: 9ce13bb576177c1542d11d808c61f3f8
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/action/runner.ts:122:4"
```

### Pattern

`shield-(guard|manager)\.ts$`

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

## usage_mismatch:9ff610fee88894be933490f513c538e8:search

```yaml
regex_id: 9ff610fee88894be933490f513c538e8
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/tests/memory-core.test.ts:55:23"
```

### Pattern

`^lyrie_`

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

## usage_mismatch:a0863a2440c68fc08009d302d05fd8ef:search

```yaml
regex_id: a0863a2440c68fc08009d302d05fd8ef
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/scanners/taint-engine.ts:273:35"
```

### Pattern

`^\s*(?:public|private|protected|static)?\s*function\s+([A-Za-z_]\w*)\s*\(([^)]*)\)`

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

## usage_mismatch:a0c391206adb21a9d5b751147128dcfe:search

```yaml
regex_id: a0c391206adb21a9d5b751147128dcfe
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/hack/dependency-graph.ts:372:19"
```

### Pattern

`^\s*([A-Za-z0-9_.\-]+)\s*=\s*["']?([^"'\n#]+)["']?`

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

## usage_mismatch:a0f0367db682a8c580903d7421a1202c:search

```yaml
regex_id: a0f0367db682a8c580903d7421a1202c
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/stages-validator.ts:435:4"
```

### Pattern

`\.(controller|router|handler)\.[jt]sx?$`

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

## usage_mismatch:a1678e097e7e2eaed2c7ee36cdb0aae9:search

```yaml
regex_id: a1678e097e7e2eaed2c7ee36cdb0aae9
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/gateway/src/security/dm-pairing.test.ts:54:36"
```

### Pattern

`^[A-Z2-9]{4}-[A-Z2-9]{4}$`

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

## usage_mismatch:a33352f5c49b70c7b16285ab0e46fd7b:search

```yaml
regex_id: a33352f5c49b70c7b16285ab0e46fd7b
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/threat-intel/client.ts:389:32"
```

### Pattern

`^(<=|>=|<|>|=|\^|~)?\s*([0-9].*)$`

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

## usage_mismatch:a39c8c585639de2f0d5d8c9e6f7a4aa3:search

```yaml
regex_id: a39c8c585639de2f0d5d8c9e6f7a4aa3
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/scanners/taint-engine.ts:269:34"
```

### Pattern

`^\s*(?:export\s+)?(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*(?:async\s+)?\(?([^)]*)\)?\s*=>`

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

## usage_mismatch:a3c64cf9a2aa4754335eead9870924fb:search

```yaml
regex_id: a3c64cf9a2aa4754335eead9870924fb
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/remediation-pr/header-fix.test.ts:72:45"
```

### Pattern

`^lyrie-auto-fix\/`

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

## usage_mismatch:a423d3472fe3fa2742d5d54c608f94ca:search

```yaml
regex_id: a423d3472fe3fa2742d5d54c608f94ca
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/migrate/autogpt.ts:95:29"
```

### Pattern

`^(\w+(?:_\w+)*):\s*(.+)$`

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

## usage_mismatch:a4849dec633970e0a3b9a861a250bb21:search

```yaml
regex_id: a4849dec633970e0a3b9a861a250bb21
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/stages-validator.ts:298:6"
```

### Pattern

`^\s*\*\s*@(param|returns?|example|typedef|type|see|deprecated)\b`

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

## usage_mismatch:a4e16a4c845ba25abcfe6b7581852d35:search

```yaml
regex_id: a4e16a4c845ba25abcfe6b7581852d35
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/stages-validator.ts:531:4"
```

### Pattern

`\.min\.[a-z]+$`

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

## usage_mismatch:a571b20f4e2a6557e15fe186550fbe10:search

```yaml
regex_id: a571b20f4e2a6557e15fe186550fbe10
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/aav/adversarial-loop.test.ts:249:36"
```

### Pattern

`-MUT-([A-Z0-9]+)$`

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

## usage_mismatch:a6ac3e810ff7371159e9ba706d7656ee:search

```yaml
regex_id: a6ac3e810ff7371159e9ba706d7656ee
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/oss-scan/service.ts:279:7"
```

### Pattern

`^[A-Za-z0-9._\-]{1,100}$`

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

## usage_mismatch:a70257a37eef049d8a71b26745000cff:search

```yaml
regex_id: a70257a37eef049d8a71b26745000cff
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/oss-scan/service.ts:279:50"
```

### Pattern

`^[A-Za-z0-9._\-]{1,100}$`

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

## usage_mismatch:ab37c4b85bf2e287a2f05530e0d04865:search

```yaml
regex_id: ab37c4b85bf2e287a2f05530e0d04865
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/attack-surface.ts:582:44"
```

### Pattern

`^app\/(.+)\/route\.(ts|js)$`

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

## usage_mismatch:abb6b7c806808bff4d6e165f5d0013c5:search

```yaml
regex_id: abb6b7c806808bff4d6e165f5d0013c5
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/hack/reachability.ts:367:26"
```

### Pattern

`^(<=|>=|<|>|=|\^|~)?\s*([0-9].*)$`

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

## usage_mismatch:ac15a73d6eab62f2e0800120d66317fd:search

```yaml
regex_id: ac15a73d6eab62f2e0800120d66317fd
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/action/runner.test.ts:149:61"
```

### Pattern

`^\d+(\.\d+)?$`

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

## usage_mismatch:af3fb2fefcadd6a8412dd5d2e0064016:search

```yaml
regex_id: af3fb2fefcadd6a8412dd5d2e0064016
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/atp/tests/breach.test.ts:38:22"
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

## usage_mismatch:b32b83329ac82c57704ec9ec42db6a39:search

```yaml
regex_id: b32b83329ac82c57704ec9ec42db6a39
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/oss-scan/service.ts:100:18"
```

### Pattern

`^[A-Za-z0-9._\/\-]{1,128}$`

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

## usage_mismatch:b4a4daacb308d06058f2ee08c2a7d343:search

```yaml
regex_id: b4a4daacb308d06058f2ee08c2a7d343
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/hack/dependency-graph.ts:293:13"
```

### Pattern

`^"?([@\w][^@"\n]*?)@[^\n"]+"?:?\s*\n(?:\s+resolution:[^\n]*\n)?\s+version[: ]+"?([^"\n]+)"?`

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

## usage_mismatch:b50e1c16f3aa8b0a045f49750725d96a:search

```yaml
regex_id: b50e1c16f3aa8b0a045f49750725d96a
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/oss-scan/service.ts:258:4"
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

## usage_mismatch:b6e647b73d8214a0a5363923cfd9405f:search

```yaml
regex_id: b6e647b73d8214a0a5363923cfd9405f
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/migrate/grip-ai.ts:148:27"
```

### Pattern

`^(\w+):\s*(.+)$`

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

## usage_mismatch:b9103fe2d2e38925b0954fcf1c2d37a4:search

```yaml
regex_id: b9103fe2d2e38925b0954fcf1c2d37a4
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/adapters/trufflehog.ts:108:6"
```

### Pattern

`^[A-Z_]{10,}$`

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

## usage_mismatch:ba2a04a4c3a1ef67fc0f4094b93fbb89:search

```yaml
regex_id: ba2a04a4c3a1ef67fc0f4094b93fbb89
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/attack-surface.ts:210:2"
```

### Pattern

`\.zip$`

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

## usage_mismatch:ba2f2ece6e904d98271582152181103f:search

```yaml
regex_id: ba2f2ece6e904d98271582152181103f
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/hack/orchestrator.ts:453:6"
```

### Pattern

`^https?:\/\/`

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

## usage_mismatch:ba59cb97f54f1fee229fa0615616e363:search

```yaml
regex_id: ba59cb97f54f1fee229fa0615616e363
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/attack-surface.ts:866:15"
```

### Pattern

`^\d+\.\d+$`

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

## usage_mismatch:bd966190d8d399e7e9e1e52ff06fec21:search

```yaml
regex_id: bd966190d8d399e7e9e1e52ff06fec21
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/governance/scorecard.test.ts:99:34"
```

### Pattern

`^(GOVERN|MAP|MEASURE|MANAGE)-`

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

## usage_mismatch:bdbea661d88975017587e9956c8b756d:search

```yaml
regex_id: bdbea661d88975017587e9956c8b756d
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/scanners/taint-engine.ts:362:39"
```

### Pattern

`^\s*(?:const|let|var|:=)?\s*([A-Za-z_$][\w$]*)\s*[:=]`

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

## usage_mismatch:be29b720d176891253d9116ef3f5a1ba:search

```yaml
regex_id: be29b720d176891253d9116ef3f5a1ba
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/attack-surface.ts:865:15"
```

### Pattern

`^\d+$`

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

## usage_mismatch:c10f31bbfebb22c33bf837f0c835bd4c:search

```yaml
regex_id: c10f31bbfebb22c33bf837f0c835bd4c
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/action/runner.ts:124:4"
```

### Pattern

`fts-search\.(ts|test\.ts)$`

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

## usage_mismatch:c26b7a16b4b1ee632c219839f142e831:search

```yaml
regex_id: c26b7a16b4b1ee632c219839f142e831
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/tools/exec/exec.test.ts:99:6"
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

## usage_mismatch:c4400585a2a8c8a0f580491fb46424cb:search

```yaml
regex_id: c4400585a2a8c8a0f580491fb46424cb
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/oss-scan/service.ts:259:4"
```

### Pattern

`^172\.(1[6-9]|2\d|3[01])\.`

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

## usage_mismatch:c5b71fd5eeb9d58b47e7845e34fbb4fe:search

```yaml
regex_id: c5b71fd5eeb9d58b47e7845e34fbb4fe
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/governance/scorecard.test.ts:84:39"
```

### Pattern

`^\d{4}-\d{2}-\d{2}T`

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

## usage_mismatch:c76fe85cd8b525b9d6cb973a7daa78dd:search

```yaml
regex_id: c76fe85cd8b525b9d6cb973a7daa78dd
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/proxy/proxy.ts:280:31"
```

### Pattern

`\/api\/\w+\/?$`

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

## usage_mismatch:cbe3876f1c01bad4328577bc819fc694:search

```yaml
regex_id: cbe3876f1c01bad4328577bc819fc694
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/stages-validator.ts:299:7"
```

### Pattern

`^\s*("""|'''|\/\*\*|\*\/)`

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

## usage_mismatch:ccfb3c5783bb515711de32534b3305fe:search

```yaml
regex_id: ccfb3c5783bb515711de32534b3305fe
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/remediation-pr/dependency-fix.test.ts:97:45"
```

### Pattern

`^lyrie-auto-fix\/bump-lodash`

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

## usage_mismatch:cefd6858fb49bee23b05ecdf4e14c3ea:search

```yaml
regex_id: cefd6858fb49bee23b05ecdf4e14c3ea
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/skills/ai-pentest/vuln-scanner.ts:525:37"
```

### Pattern

`^\d+`

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

## usage_mismatch:d0f11d2234f344a853a28885893f969c:search

```yaml
regex_id: d0f11d2234f344a853a28885893f969c
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/scanners/taint-engine.ts:388:35"
```

### Pattern

`^\s*(?:const|let|var|:=)?\s*([A-Za-z_$][\w$]*)\s*[:=]\s*(.+)$`

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

## usage_mismatch:d1116d0c5888c443d243e20ff7341e70:search

```yaml
regex_id: d1116d0c5888c443d243e20ff7341e70
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/agents/message-bus.ts:157:45"
```

### Pattern

`^re:([^\n]+)\n`

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

## usage_mismatch:d41be93bf797994354451c3ed913d7c2:search

```yaml
regex_id: d41be93bf797994354451c3ed913d7c2
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/oss-scan/service.ts:260:4"
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

## usage_mismatch:d4ef0988972a1a617543fb91178e42e9:search

```yaml
regex_id: d4ef0988972a1a617543fb91178e42e9
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/migrate/superagi.ts:80:27"
```

### Pattern

`^(\w+(?:_\w+)*):\s*(.+)$`

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

## usage_mismatch:d5a99ffcf3fd88a4f16b4f78ebe9cd6b:search

```yaml
regex_id: d5a99ffcf3fd88a4f16b4f78ebe9cd6b
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/hack/orchestrator.test.ts:58:41"
```

### Pattern

`^lyrie-`

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

## usage_mismatch:d60285b92fdcf6f38a019a3957abfe3a:search

```yaml
regex_id: d60285b92fdcf6f38a019a3957abfe3a
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/tools-catalog/catalog.test.ts:75:36"
```

### Pattern

`^lyrie-tools-catalog-`

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

## usage_mismatch:d616b3f640ae1eb25384334d2c5feaa0:search

```yaml
regex_id: d616b3f640ae1eb25384334d2c5feaa0
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/security/domain-verify.ts:60:22"
```

### Pattern

`^(127\.|10\.|172\.(1[6-9]|2\d|3[01])\.|192\.168\.|0\.|169\.254\.|::1|\[::1\]|fc00:|fd[0-9a-f]{2}:)`

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

## usage_mismatch:d9ab589202b16119e876a0ace0cb74b3:search

```yaml
regex_id: d9ab589202b16119e876a0ace0cb74b3
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/atp/tests/aic.test.ts:31:35"
```

### Pattern

`^[0-9a-f-]{36}$`

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

## usage_mismatch:db1abae77f136057697d3ddbc7326235:search

```yaml
regex_id: db1abae77f136057697d3ddbc7326235
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/hack/auto-remediation.test.ts:157:35"
```

### Pattern

`^https?:\/\/`

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

## usage_mismatch:db3a470250ef2bed03efc35a7ca3ec13:search

```yaml
regex_id: db3a470250ef2bed03efc35a7ca3ec13
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/action/runner.ts:120:4"
```

### Pattern

`-shield(-[a-z]+)?\.test\.ts$`

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

## usage_mismatch:dd55751643075b09adacb242e963dad3:search

```yaml
regex_id: dd55751643075b09adacb242e963dad3
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/hack/orchestrator.ts:453:37"
```

### Pattern

`^\d+\.\d+\.\d+\.\d+(?::\d+)?$`

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

## usage_mismatch:dff50065ed4a84b26a02f4caf6fad401:search

```yaml
regex_id: dff50065ed4a84b26a02f4caf6fad401
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/action/runner.ts:121:4"
```

### Pattern

`shield-(guard|manager)\.test\.ts$`

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

## usage_mismatch:e126ab9d2839011fd1b4cc8a30b9b6a8:search

```yaml
regex_id: e126ab9d2839011fd1b4cc8a30b9b6a8
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/attack-surface.ts:832:34"
```

### Pattern

`^([^:]+):\s*(.*)$`

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

## usage_mismatch:e6d9358a039afc613349a2a6112072b3:search

```yaml
regex_id: e6d9358a039afc613349a2a6112072b3
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/skills/skill-loader.ts:33:31"
```

### Pattern

`^(\w[\w-]*)\s*:\s*(.*)?$`

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

## usage_mismatch:e84851edc364dcca9414be8198927ede:search

```yaml
regex_id: e84851edc364dcca9414be8198927ede
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/attack-surface.ts:600:44"
```

### Pattern

`^pages\/api\/(.+)\.(ts|js|tsx|jsx)$`

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

## usage_mismatch:e8d13f719c6b4514a01b5184dab94e4d:search

```yaml
regex_id: e8d13f719c6b4514a01b5184dab94e4d
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/attack-surface.ts:209:2"
```

### Pattern

`\.pdf$`

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

## usage_mismatch:e8e1be5d828e741e051d05a4bf8f6eb6:search

```yaml
regex_id: e8e1be5d828e741e051d05a4bf8f6eb6
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/tools/memory/memory-tools.test.ts:153:23"
```

### Pattern

`^lm_`

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

## usage_mismatch:e9816f0d414e988a5845799919dde92f:search

```yaml
regex_id: e9816f0d414e988a5845799919dde92f
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/scripts/evolve.ts:183:36"
```

### Pattern

`^# (.+)$`

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

## usage_mismatch:ea3fb538996a4f8bee50c86fb12aeeb0:search

```yaml
regex_id: ea3fb538996a4f8bee50c86fb12aeeb0
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/action/runner.ts:117:4"
```

### Pattern

`\.pyc$`

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

## usage_mismatch:eb3a07fdc56c0a507949f7d3d993d30b:search

```yaml
regex_id: eb3a07fdc56c0a507949f7d3d993d30b
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/attack-surface.ts:205:2"
```

### Pattern

`\.jpg$`

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

## usage_mismatch:eff95a8e71f60f2ec22e86fc374cf4a4:search

```yaml
regex_id: eff95a8e71f60f2ec22e86fc374cf4a4
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/scanners/taint-engine.ts:339:10"
```

### Pattern

`^\s*(?:const|let|var|:=)\s+([A-Za-z_$][\w$]*)\s*[:=]`

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

## usage_mismatch:f01633b31c4f31482224fbbde1c02cda:search

```yaml
regex_id: f01633b31c4f31482224fbbde1c02cda
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/migrate/grip-ai.ts:71:24"
```

### Pattern

`^[A-Z_a-z][A-Z_a-z0-9]*$`

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

## usage_mismatch:f167b31a2d7dfc06558dfafb9be5ed87:search

```yaml
regex_id: f167b31a2d7dfc06558dfafb9be5ed87
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/hack/reachability.test.ts:74:41"
```

### Pattern

`^lyrie-`

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

## usage_mismatch:f55f6b9d91d903b63d119377e14ab95e:search

```yaml
regex_id: f55f6b9d91d903b63d119377e14ab95e
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/governance/permissions.test.ts:116:38"
```

### Pattern

`^\d{4}-\d{2}-\d{2}T`

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

## usage_mismatch:f73e4d534617162825d05bb733ca4b64:search

```yaml
regex_id: f73e4d534617162825d05bb733ca4b64
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/tools/media/tts.test.ts:63:36"
```

### Pattern

`\.mp3$`

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

## usage_mismatch:f90d523b62f5426a5cda607190986bb4:search

```yaml
regex_id: f90d523b62f5426a5cda607190986bb4
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/agents/message-bus.test.ts:238:34"
```

### Pattern

`^re:msg-`

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

## usage_mismatch:f93a269e297c78249430b2ab8c8000d6:search

```yaml
regex_id: f93a269e297c78249430b2ab8c8000d6
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/migrate/grip-ai.ts:125:27"
```

### Pattern

`^([A-Z_][A-Z0-9_]*)=(.+)$`

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

## usage_mismatch:faf6241a2b5a9d1cbf78f59166906709:search

```yaml
regex_id: faf6241a2b5a9d1cbf78f59166906709
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/aav/adversarial-loop.test.ts:65:43"
```

### Pattern

`\n\n([A-Za-z0-9+/=]+)$`

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

## usage_mismatch:fe2e0be69957acf7c38fe06150535427:search

```yaml
regex_id: fe2e0be69957acf7c38fe06150535427
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/stages-validator.ts:620:10"
```

### Pattern

`\.(ts|tsx)$`

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

## usage_mismatch:ffae76e269df54c7bfaff16b5ac23142:search

```yaml
regex_id: ffae76e269df54c7bfaff16b5ac23142
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/migrate/superagi.ts:122:22"
```

### Pattern

`agent.*\.(json|yaml|yml)$`

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

## usage_mismatch:ffb9abfcc175f04f8c31682903bc9289:search

```yaml
regex_id: ffb9abfcc175f04f8c31682903bc9289
schema_version: "1"
kind: usage_mismatch
corpus: lyrie-ai
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lyrie-ai/rules/packages/core/src/pentest/stages-validator.ts:265:2"
```

### Pattern

`\.spec\.[jt]sx?$`

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
corpus: lyrie-ai
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
corpus: lyrie-ai
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
corpus: lyrie-ai
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
corpus: lyrie-ai
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

---
schema_version: "1"
corpus: bike4mind
findings: 194
---

# bike4mind batch findings

## usage_mismatch:032c217193568120737957ade6bfd57c:search

```yaml
regex_id: 032c217193568120737957ade6bfd57c
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/artifactParser.ts:571:4"
```

### Pattern

`^I'll`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:04ea5cdeb03af673265458d417519848:search

```yaml
regex_id: 04ea5cdeb03af673265458d417519848
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/common/src/queryComplexityClassifier.ts:45:4"
```

### Pattern

`^(what do you think|your opinion)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:05b8876832e0071144d4dbf757410011:search

```yaml
regex_id: 05b8876832e0071144d4dbf757410011
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/artifactParser.ts:558:4"
```

### Pattern

`^%%`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0788e734a6561762962da717b0e23a4b:search

```yaml
regex_id: 0788e734a6561762962da717b0e23a4b
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/services/liveopsTriageService.ts:409:6"
```

### Pattern

`^(sk-|pk-|xox[bsap]-|ghp_|gho_|ghu_|ghs_|ghr_)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:09373380fb380d01f5889b92ca036baa:email

```yaml
regex_id: 09373380fb380d01f5889b92ca036baa
schema_version: "1"
kind: intent_mismatch
corpus: bike4mind
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/integrations/slack/emailMirror.ts:80:15"
```

### Pattern

`\s+`

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

## usage_mismatch:0b53424a2f11901bdce0538a01c6e742:search

```yaml
regex_id: 0b53424a2f11901bdce0538a01c6e742
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/help/validate-help-content.ts:111:31"
```

### Pattern

`\{#([^}]+)\}\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0d5ff928fb34b81fdf16fdc67129d49e:search

```yaml
regex_id: 0d5ff928fb34b81fdf16fdc67129d49e
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/fab-pipeline/src/chunk.ts:489:19"
```

### Pattern

`^ppt\/slides\/slide\d+\.xml$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0d914de2ad6e83d989afe6ab23258f58:search

```yaml
regex_id: 0d914de2ad6e83d989afe6ab23258f58
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/src/checkDeprecatedModelUsage.ts:45:2"
```

### Pattern

`models\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0fb3c9d31591b00faaee75ccd85604f0:search

```yaml
regex_id: 0fb3c9d31591b00faaee75ccd85604f0
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/slack/src/handlers/channel-manager.ts:226:7"
```

### Pattern

`^[a-z0-9-_]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:10f21f4fce22ff772fe480503f41d574:search

```yaml
regex_id: 10f21f4fce22ff772fe480503f41d574
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/services/publish/viewerSecurity.ts:166:61"
```

### Pattern

`^\[[0-9a-fA-F:.]+\](:\d+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1209804d7ebdf4c415554bc07cc4a4e8:search

```yaml
regex_id: 1209804d7ebdf4c415554bc07cc4a4e8
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/src/checkDeprecatedModelUsage.ts:60:2"
```

### Pattern

`package\.json$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:13c1f0309dc22ab2f93eee958ca027c0:search

```yaml
regex_id: 13c1f0309dc22ab2f93eee958ca027c0
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/utils/fileFormatUtils.ts:420:8"
```

### Pattern

`^[a-zA-Z_][a-zA-Z0-9_]*\s*:\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:171293115d336d66f68687460830b069:search

```yaml
regex_id: 171293115d336d66f68687460830b069
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/src/checkDeprecatedModelUsage.ts:62:2"
```

### Pattern

`pnpm-lock\.yaml$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:172780be4a85d11c09082e32d5f01286:search

```yaml
regex_id: 172780be4a85d11c09082e32d5f01286
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/cli/src/utils/imageDetector.ts:261:22"
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

## intent_mismatch:17aef06d68316f1396cc757113405ad7:email

```yaml
regex_id: 17aef06d68316f1396cc757113405ad7
schema_version: "1"
kind: intent_mismatch
corpus: bike4mind
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/integrations/slack/emailMirror.ts:82:15"
```

### Pattern

`\s+([.,!?;:])`

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

## usage_mismatch:17f1210b7ee3d3967a67aac0725e69de:search

```yaml
regex_id: 17f1210b7ee3d3967a67aac0725e69de
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/services/liveopsTriageService.ts:410:6"
```

### Pattern

`^sk-ant-`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:18a557341b0eb2fa92eb24efd00e0874:search

```yaml
regex_id: 18a557341b0eb2fa92eb24efd00e0874
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/services/src/modelDiscoveryService/sources/openaiDocs.ts:31:15"
```

### Pattern

`^short context output$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:19ac965339c5d1e025877a2e491daab1:search

```yaml
regex_id: 19ac965339c5d1e025877a2e491daab1
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/artifactParser.ts:547:4"
```

### Pattern

`^(graph|flowchart|sequenceDiagram|classDiagram|stateDiagram|gantt|pie|mindmap)\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1ab3eb748ba1688119ac51539149bcf5:search

```yaml
regex_id: 1ab3eb748ba1688119ac51539149bcf5
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/services/liveopsFingerprint.ts:61:2"
```

### Pattern

`^<anonymous>$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1b0b151150c8acc7fb3512b3c8df5dfb:search

```yaml
regex_id: 1b0b151150c8acc7fb3512b3c8df5dfb
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/services/liveopsFingerprint.ts:22:13"
```

### Pattern

`^(?:(?:Runtime\.)?UnhandledPromiseRejection:\s*)?(\w+(?:Error|Exception)?)\s*:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1bcf77b39f9c87fb1a422ae2982f3dd8:search

```yaml
regex_id: 1bcf77b39f9c87fb1a422ae2982f3dd8
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/artifactParser.ts:555:4"
```

### Pattern

`^subgraph\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1c13af54734b0bf9b541e17493e8c45b:search

```yaml
regex_id: 1c13af54734b0bf9b541e17493e8c45b
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/utils/fileFormatUtils.ts:524:6"
```

### Pattern

`^\s*[-*+]\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1e7036570cd47fc6c312a08e4046ec63:search

```yaml
regex_id: 1e7036570cd47fc6c312a08e4046ec63
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/utils/fileFormatUtils.ts:447:8"
```

### Pattern

`^\[[a-zA-Z0-9_.-]+\]\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1ed2973ed1659c9b771f8b119dd7fc3f:search

```yaml
regex_id: 1ed2973ed1659c9b771f8b119dd7fc3f
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/src/checkDeprecatedModelUsage.ts:55:2"
```

### Pattern

`aggregatorKeys\.json$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1f9fde03cee94ed010252a6123abac62:search

```yaml
regex_id: 1f9fde03cee94ed010252a6123abac62
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/services/liveopsTriageService.ts:117:45"
```

### Pattern

`#(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1fc33ff018139d39b0097447fc9affa2:search

```yaml
regex_id: 1fc33ff018139d39b0097447fc9affa2
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/services/src/modelDiscoveryService/sources/openaiDocs.ts:94:7"
```

### Pattern

`^[a-z0-9][a-z0-9._:-]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:20e133c1ba71228db4febc75f216e8c4:email

```yaml
regex_id: 20e133c1ba71228db4febc75f216e8c4
schema_version: "1"
kind: intent_mismatch
corpus: bike4mind
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/integrations/slack/emailMirror.ts:61:6"
```

### Pattern

`(email\s*change|change.*email|new email)`

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

## usage_mismatch:2149351f3fb06411380ba36f60a0fb52:search

```yaml
regex_id: 2149351f3fb06411380ba36f60a0fb52
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/src/checkDeprecatedModelUsage.ts:50:2"
```

### Pattern

`resolveDeprecatedModel\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:24193e4668caf280b9a3290cf868e47c:search

```yaml
regex_id: 24193e4668caf280b9a3290cf868e47c
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/utils/fileFormatUtils.ts:497:6"
```

### Pattern

`^\s*(def|class|import|from|function|const|let|var)\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:27b0cf0653cb35e571f4972591d4827f:search

```yaml
regex_id: 27b0cf0653cb35e571f4972591d4827f
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/slack/src/handlers/slack-github-mapper.ts:208:66"
```

### Pattern

`^[a-zA-Z0-9]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:287a931e1f6f87a570db9833194151bb:search

```yaml
regex_id: 287a931e1f6f87a570db9833194151bb
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/slack/src/agent-parser.ts:105:37"
```

### Pattern

`^(?:<@[^>]+>\s*)*@(\w+)\s+([\s\S]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2a256f00b3ebc60f0dee0d993ee81742:search

```yaml
regex_id: 2a256f00b3ebc60f0dee0d993ee81742
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/services/publish/viewerSecurity.ts:166:21"
```

### Pattern

`^[a-zA-Z0-9.-]+(:\d+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2a9ffde2c52099a9872343c93a4023f7:search

```yaml
regex_id: 2a9ffde2c52099a9872343c93a4023f7
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/services/src/sreAgentService/index.ts:1453:54"
```

### Pattern

`\.(test|spec)\.[jt]sx?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2e265fe7de708cfe0122ad19187cdc14:search

```yaml
regex_id: 2e265fe7de708cfe0122ad19187cdc14
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/utils/ip.ts:7:73"
```

### Pattern

`^172\.(1[6-9]|2\d|3[0-1])\.`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2fed3c66e0a3ad34a8f1d6bbe88ace5a:search

```yaml
regex_id: 2fed3c66e0a3ad34a8f1d6bbe88ace5a
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/services/src/modelDiscoveryService/sources/openaiDocs.ts:24:25"
```

### Pattern

`^standard pricing`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:31f7e0e92e31acb2bdb27bcbb68df2a6:search

```yaml
regex_id: 31f7e0e92e31acb2bdb27bcbb68df2a6
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/slack/src/handlers/slack-github-mapper.ts:196:55"
```

### Pattern

`^U[A-Z0-9]{10}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:321c8d77c02421059302f3ddbe5336ed:search

```yaml
regex_id: 321c8d77c02421059302f3ddbe5336ed
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/llm-adapters/src/syncModelDescriptions.ts:700:43"
```

### Pattern

`-(\d{8})-?(.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:32e1d5e2fa8b55f85da286326c5a4852:search

```yaml
regex_id: 32e1d5e2fa8b55f85da286326c5a4852
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/utils/ip.ts:7:39"
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

## intent_mismatch:350f29051dd31063be4b3f55ea471830:email

```yaml
regex_id: 350f29051dd31063be4b3f55ea471830
schema_version: "1"
kind: intent_mismatch
corpus: bike4mind
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/components/admin/email/EmailTemplateEditor.tsx:63:13"
```

### Pattern

`\s+`

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

## usage_mismatch:37f9c792b061a53abc7bb320ea6c826b:search

```yaml
regex_id: 37f9c792b061a53abc7bb320ea6c826b
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/slack/src/thread-intelligence/patterns.ts:23:34"
```

### Pattern

`\?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3862ae01171e5e25bf96ba0087395807:search

```yaml
regex_id: 3862ae01171e5e25bf96ba0087395807
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/artifactParser.ts:551:4"
```

### Pattern

`^[A-Za-z0-9_]+(\[[^\]]*\]|\([^)]*\)|\{[^}]*\})?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:38b44fd659c65c544bc01abbd93d96f2:search

```yaml
regex_id: 38b44fd659c65c544bc01abbd93d96f2
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/slack/src/handlers/slack-github-mapper.ts:208:9"
```

### Pattern

`^[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:39692e3f6c0be1eec6e75af64b64eacc:search

```yaml
regex_id: 39692e3f6c0be1eec6e75af64b64eacc
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/utils/artifactParser.ts:894:32"
```

### Pattern

`^class\s+([A-Z][a-zA-Z0-9_]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3a1763332424ac128ef43525ff97b7c1:search

```yaml
regex_id: 3a1763332424ac128ef43525ff97b7c1
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/src/checkDeprecatedModelUsage.ts:52:2"
```

### Pattern

`fallback\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3b0b744877abf93d16b0ce32f080f826:search

```yaml
regex_id: 3b0b744877abf93d16b0ce32f080f826
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/src/checkDeprecatedModelUsage.ts:63:2"
```

### Pattern

`tsconfig.*\.json$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3b4f813c34d6584ac0c753d476fc2d2a:search

```yaml
regex_id: 3b4f813c34d6584ac0c753d476fc2d2a
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/src/checkDeprecatedModelUsage.ts:51:2"
```

### Pattern

`checkDeprecatedModelUsage\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3c3db1fc9d430df92b74949dd8b55963:search

```yaml
regex_id: 3c3db1fc9d430df92b74949dd8b55963
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/services/liveopsFingerprint.ts:58:2"
```

### Pattern

`^node:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3e69213bd9ecf9bd56e761ab01ad5196:search

```yaml
regex_id: 3e69213bd9ecf9bd56e761ab01ad5196
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/services/publish/transpileReactArtifact.ts:208:6"
```

### Pattern

`^\s*import\s+['"]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3fe8ec505e909abb2f7cb39d122b68c6:search

```yaml
regex_id: 3fe8ec505e909abb2f7cb39d122b68c6
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/src/checkDeprecatedModelUsage.ts:58:2"
```

### Pattern

`telemetryFingerprint\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:41252b904400708844d547b5f2890652:search

```yaml
regex_id: 41252b904400708844d547b5f2890652
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/utils/ip.ts:7:48"
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

## usage_mismatch:414c45ab415e65573b923664944bff20:search

```yaml
regex_id: 414c45ab415e65573b923664944bff20
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/utils/fileFormatUtils.ts:521:6"
```

### Pattern

`^#{1,6}\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:43f3cce7dd6de50a2f082ec7e7aec36c:email

```yaml
regex_id: 43f3cce7dd6de50a2f082ec7e7aec36c
schema_version: "1"
kind: intent_mismatch
corpus: bike4mind
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/integrations/slack/emailMirror.ts:76:15"
```

### Pattern

`<style[\s\S]*?<\/style>`

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

## usage_mismatch:441342d8af76106e02e3c220d4f35021:search

```yaml
regex_id: 441342d8af76106e02e3c220d4f35021
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/help/utils.ts:147:31"
```

### Pattern

`^###`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:454f87692ea81e0e57948e8577f133cf:email

```yaml
regex_id: 454f87692ea81e0e57948e8577f133cf
schema_version: "1"
kind: intent_mismatch
corpus: bike4mind
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/integrations/slack/emailMirror.ts:77:15"
```

### Pattern

`<script[\s\S]*?<\/script>`

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

## usage_mismatch:46b7649504d9080762433fa78c4935cd:search

```yaml
regex_id: 46b7649504d9080762433fa78c4935cd
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/utils/codeBlockTitleExtractor.ts:399:34"
```

### Pattern

`^(?:\/\/|#|\/\*|\<!--)\s*([^\n*>]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4992cb43ea21bfc2ef4b6c8cc9ff0ebd:search

```yaml
regex_id: 4992cb43ea21bfc2ef4b6c8cc9ff0ebd
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/scripts/secrets-scan-summarize-and-ingest.mjs:56:2"
```

### Pattern

`\.env\.example$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4c1735cb2f127fe6f34c2ba80e3303a3:search

```yaml
regex_id: 4c1735cb2f127fe6f34c2ba80e3303a3
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/scripts/secrets-scan-summarize-and-ingest.mjs:69:2"
```

### Pattern

`^AKIAIOSFODNN7EXAMPLE$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4c44974b3bb0d40c4a4dd64ec45c70f9:search

```yaml
regex_id: 4c44974b3bb0d40c4a4dd64ec45c70f9
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/utils/artifactParser.ts:703:27"
```

### Pattern

`^(?:def|class)\s+\w+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4c5dae951f2de5b7d0cad0141041b0a5:search

```yaml
regex_id: 4c5dae951f2de5b7d0cad0141041b0a5
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/utils/artifactParser.ts:902:31"
```

### Pattern

`^def\s+([a-z_][a-z0-9_]*)\s*\(`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4ce322acbb2c0f4283e9854849778f6a:search

```yaml
regex_id: 4ce322acbb2c0f4283e9854849778f6a
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/services/adminTools/modalToolHelpers.ts:211:6"
```

### Pattern

`message[:\s]+["']?(.+?)["']?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4d1bc179fb96dc9159ed8f129327a2f4:search

```yaml
regex_id: 4d1bc179fb96dc9159ed8f129327a2f4
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/components/Session/UserPrompt.tsx:94:50"
```

### Pattern

`^\s{2,}`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4f68d084c50cce9e0f4d1c41c78a329d:search

```yaml
regex_id: 4f68d084c50cce9e0f4d1c41c78a329d
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/services/publish/viewerSecurity.ts:107:12"
```

### Pattern

`^\s*(javascript|vbscript):`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4f7e599f7b4ae50ed1edd7f3f5139b2c:search

```yaml
regex_id: 4f7e599f7b4ae50ed1edd7f3f5139b2c
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/office/officeEdit.ts:101:36"
```

### Pattern

`^<w:p\b([^>]*)\/>$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:51ca9265c9bb6c04ceb9b001e950bb67:search

```yaml
regex_id: 51ca9265c9bb6c04ceb9b001e950bb67
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/services/src/llm/tools/implementation/bashExecute/index.ts:210:30"
```

### Pattern

`^(\S+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:54036bce899b51bd5fb691d46af7ad6a:search

```yaml
regex_id: 54036bce899b51bd5fb691d46af7ad6a
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/services/src/modelDiscoveryService/sources/openaiDocs.ts:29:18"
```

### Pattern

`^short context cached input$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:589f6ed3c20896bf97f999269e37bd38:search

```yaml
regex_id: 589f6ed3c20896bf97f999269e37bd38
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/slack/src/thread-intelligence/patterns.ts:23:41"
```

### Pattern

`^(?:what|how|why|when|where|who)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:59949874e2100d738ef3ef2e9827c425:search

```yaml
regex_id: 59949874e2100d738ef3ef2e9827c425
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/artifactParser.ts:572:4"
```

### Pattern

`^Here's`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5b625eced654dd3dca6f11153c7712eb:search

```yaml
regex_id: 5b625eced654dd3dca6f11153c7712eb
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/office/officeEdit.ts:26:28"
```

### Pattern

`^\s*\[(\d+)\]\s?([\s\S]*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:5c37c70ed0beb06caec2d1ed9258c8fc:email

```yaml
regex_id: 5c37c70ed0beb06caec2d1ed9258c8fc
schema_version: "1"
kind: intent_mismatch
corpus: bike4mind
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/integrations/slack/emailMirror.ts:78:15"
```

### Pattern

`<[^>]+>`

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

## usage_mismatch:5ddc04073ba1543d7c5871edb5ef0ff3:search

```yaml
regex_id: 5ddc04073ba1543d7c5871edb5ef0ff3
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/utils/ip.ts:16:2"
```

### Pattern

`^fe[89ab][0-9a-f]:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5ecf18747722fce6be47a1e8bfdc8510:search

```yaml
regex_id: 5ecf18747722fce6be47a1e8bfdc8510
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/common/src/jira/format.ts:733:30"
```

### Pattern

`\/role\/(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5f8ce5f25a4ad8dbeb55c77fd024e24f:search

```yaml
regex_id: 5f8ce5f25a4ad8dbeb55c77fd024e24f
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/artifactParser.ts:564:4"
```

### Pattern

`^direction\s+(TB|BT|LR|RL)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:61116d36fdbd76f8f9ada5dcb7a9f9b1:search

```yaml
regex_id: 61116d36fdbd76f8f9ada5dcb7a9f9b1
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/help/utils.ts:225:31"
```

### Pattern

`^####`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6115986044175c172b272438eb0361ad:search

```yaml
regex_id: 6115986044175c172b272438eb0361ad
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/utils/ip.ts:23:27"
```

### Pattern

`^::ffff:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6270a84e39ef5c98778e49d25387c569:search

```yaml
regex_id: 6270a84e39ef5c98778e49d25387c569
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/services/adminTools/modalToolHelpers.ts:241:22"
```

### Pattern

`description[:\s]+["']?(.+?)["']?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:6348d5cc689e35f5459a4ae733c779be:url

```yaml
regex_id: 6348d5cc689e35f5459a4ae733c779be
schema_version: "1"
kind: intent_mismatch
corpus: bike4mind
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/queueHandlers/questExport.ts:484:39"
```

### Pattern

`[.*+?^${}()|[\]\\]`

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

## intent_mismatch:63d5a176cbfb8b479635b5427f6c5a35:url

```yaml
regex_id: 63d5a176cbfb8b479635b5427f6c5a35
schema_version: "1"
kind: intent_mismatch
corpus: bike4mind
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/services/src/lib/turndown.ts:84:42"
```

### Pattern

`(?<!!)\[(.*?)\]\((.*?)\)`

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

## usage_mismatch:6460517e397b977ec27225c0656ccbba:search

```yaml
regex_id: 6460517e397b977ec27225c0656ccbba
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/services/liveopsFingerprint.ts:62:2"
```

### Pattern

`^\[native code\]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6605c56f046603cdd0c1463055c1dd0b:search

```yaml
regex_id: 6605c56f046603cdd0c1463055c1dd0b
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/utils/fileFormatUtils.ts:603:49"
```

### Pattern

`^\s{2,}`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:66d17e8c12368f238ade1769abc4e19a:search

```yaml
regex_id: 66d17e8c12368f238ade1769abc4e19a
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/utils/fileFormatUtils.ts:760:6"
```

### Pattern

`^<\?php`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:67c6617fcdc70026d5eec1f324d9fb41:search

```yaml
regex_id: 67c6617fcdc70026d5eec1f324d9fb41
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/utils/codeBlockTitleExtractor.ts:319:34"
```

### Pattern

`^#!.*\n#\s*([^\n]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:684c81204604959665e1d85ee3b441e6:search

```yaml
regex_id: 684c81204604959665e1d85ee3b441e6
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/services/liveopsTriageService.ts:122:45"
```

### Pattern

`-(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6872f90d7218bc4c0fbc4685f21f1457:search

```yaml
regex_id: 6872f90d7218bc4c0fbc4685f21f1457
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/services/src/modelDiscoveryService/sources/openaiDocs.ts:30:19"
```

### Pattern

`^short context cache writes$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:69c1437107d3e4c7e9d41da3ebb2bd16:search

```yaml
regex_id: 69c1437107d3e4c7e9d41da3ebb2bd16
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/common/src/queryComplexityClassifier.ts:47:4"
```

### Pattern

`^\s*(hi|hello|hey)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:69d4f0272520402979d37b6eae0313ab:search

```yaml
regex_id: 69d4f0272520402979d37b6eae0313ab
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/services/src/llm/tools/implementation/excelGeneration/index.ts:221:7"
```

### Pattern

`^[0-9A-Fa-f]{6}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6a0fe1e09d9adc8a21f8379ab9fb36b3:search

```yaml
regex_id: 6a0fe1e09d9adc8a21f8379ab9fb36b3
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/utils/ip.ts:7:58"
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

## usage_mismatch:6b8734d41f5ca142b17df7b93d09a22a:search

```yaml
regex_id: 6b8734d41f5ca142b17df7b93d09a22a
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/utils/artifactParser.ts:336:47"
```

### Pattern

`^from\s+(\w+)\s+import`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6c9d6cee768bfc184de0bffb2a84c120:search

```yaml
regex_id: 6c9d6cee768bfc184de0bffb2a84c120
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/services/src/modelDiscoveryService/sources/openaiDocs.ts:35:14"
```

### Pattern

`^long context output$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6cef96a7c4ee208fcc7aa5c7ab137363:search

```yaml
regex_id: 6cef96a7c4ee208fcc7aa5c7ab137363
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/hooks/useLatticeLocalDev.ts:119:39"
```

### Pattern

`^(.+?)\s*(?:=|equals?)\s*(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6db3aa693d486ff21a0d9b28fbfc2852:search

```yaml
regex_id: 6db3aa693d486ff21a0d9b28fbfc2852
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/src/checkDeprecatedModelUsage.ts:53:2"
```

### Pattern

`modelCatalog\.seed\.json$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6e2254bac540c5c3e9326171e2aa441a:search

```yaml
regex_id: 6e2254bac540c5c3e9326171e2aa441a
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/utils/fileFormatUtils.ts:660:6"
```

### Pattern

`^<\?php`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6e3aa02659bac9bd4a2d0ef4bf1a6a77:search

```yaml
regex_id: 6e3aa02659bac9bd4a2d0ef4bf1a6a77
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/artifactParser.ts:549:4"
```

### Pattern

`^[A-Za-z0-9_]+(\[[^\]]*\]|\([^)]*\)|\{[^}]*\})?(\s*-->?\s*|\s*==>\s*|\s*-\.\s*|\s*-\.-\s*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6e85b9c9fe3aa9e32d1699507fbf03d4:search

```yaml
regex_id: 6e85b9c9fe3aa9e32d1699507fbf03d4
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/src/checkDeprecatedModelUsage.ts:61:2"
```

### Pattern

`package-lock\.json$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7005c2b9902e4f06f5b96e4093892e40:search

```yaml
regex_id: 7005c2b9902e4f06f5b96e4093892e40
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/utils/fileFormatUtils.ts:448:13"
```

### Pattern

`^[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:71f0c4c7c19c2bbf2f9e442138541f3f:search

```yaml
regex_id: 71f0c4c7c19c2bbf2f9e442138541f3f
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/services/src/modelDiscoveryService/sources/openaiDocs.ts:32:13"
```

### Pattern

`^long context input$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:74f2357aa5991fdb30d8844e20b7b49e:search

```yaml
regex_id: 74f2357aa5991fdb30d8844e20b7b49e
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/artifactParser.ts:392:4"
```

### Pattern

`^(graph|flowchart|sequenceDiagram|classDiagram|stateDiagram|entityRelationshipDiagram|gantt|pie|mindmap|timeline|journey|gitgraph|requirementDiagram|c4Context|quadrantChart|xyChart|sankey|packet|architecture|block)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:75cfe49e382d443481bd0499fa89e576:search

```yaml
regex_id: 75cfe49e382d443481bd0499fa89e576
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/src/checkDeprecatedModelUsage.ts:105:17"
```

### Pattern

`\.(ts|tsx|js|mjs|cjs|json)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:75e2ae7db8a2288cdaa78d7f8bb2a92b:search

```yaml
regex_id: 75e2ae7db8a2288cdaa78d7f8bb2a92b
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/slack/src/agent-parser.ts:156:34"
```

### Pattern

`^(?:<@[^>]+>\s*)*@datalake\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:790af7f633438c39d0f3e441693b19d8:search

```yaml
regex_id: 790af7f633438c39d0f3e441693b19d8
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/artifactParser.ts:556:4"
```

### Pattern

`^end\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7a7a4e129d1f33e8247a3f18b131fec6:search

```yaml
regex_id: 7a7a4e129d1f33e8247a3f18b131fec6
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/src/checkDeprecatedModelUsage.ts:54:2"
```

### Pattern

`modelPrices\.seed\.json$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:7ad1448851aa5c03001e328e8d67dee4:email

```yaml
regex_id: 7ad1448851aa5c03001e328e8d67dee4
schema_version: "1"
kind: intent_mismatch
corpus: bike4mind
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/integrations/slack/emailMirror.ts:67:6"
```

### Pattern

`what.?s new|release|update`

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

## usage_mismatch:7bae0831451802a1e4162759ee37b86f:search

```yaml
regex_id: 7bae0831451802a1e4162759ee37b86f
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/services/publish/viewerSecurity.ts:104:12"
```

### Pattern

`^\s*(javascript|vbscript|data):`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7f86c7ef06ee482508a2f7cb1cf39dbc:search

```yaml
regex_id: 7f86c7ef06ee482508a2f7cb1cf39dbc
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/src/checkDeprecatedModelUsage.ts:88:15"
```

### Pattern

`\.(ts|tsx|js|mjs|cjs|json)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:80a309f87ddfcb78575d880876d2fb78:search

```yaml
regex_id: 80a309f87ddfcb78575d880876d2fb78
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/common/src/queryComplexityClassifier.ts:44:4"
```

### Pattern

`^(can you )?(recommend|suggest)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8169bcb3b5da26bc9ae5a8346390fffc:search

```yaml
regex_id: 8169bcb3b5da26bc9ae5a8346390fffc
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/src/checkDeprecatedModelUsage.ts:49:2"
```

### Pattern

`syncModelDescriptions\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:83dda7de726ee28224988604bf9f1040:search

```yaml
regex_id: 83dda7de726ee28224988604bf9f1040
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/utils/ip.ts:7:104"
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

## usage_mismatch:8478d1218a4dead3fd82d301ea41fa74:search

```yaml
regex_id: 8478d1218a4dead3fd82d301ea41fa74
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/services/src/llm/tools/implementation/lattice/index.ts:675:49"
```

### Pattern

`^[a-f0-9]{24}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:854803e4ed206d9670be7698d87a3c22:search

```yaml
regex_id: 854803e4ed206d9670be7698d87a3c22
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/services/src/modelDiscoveryService/sources/anthropicDocs.ts:166:17"
```

### Pattern

`^model$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:85acd651b19e640d062cd4bd5b10e84a:search

```yaml
regex_id: 85acd651b19e640d062cd4bd5b10e84a
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/services/src/llm/tools/implementation/lattice/index.ts:934:39"
```

### Pattern

`^(.+?)\s*(?:=|equals?)\s*(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:87373d5db2abe9f9722b47cb1c9b7f0b:search

```yaml
regex_id: 87373d5db2abe9f9722b47cb1c9b7f0b
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/fab-pipeline/src/chunk.ts:492:36"
```

### Pattern

`slide(\d+)\.xml$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:88ae5c055e0f6ca3da0c8929873319c4:search

```yaml
regex_id: 88ae5c055e0f6ca3da0c8929873319c4
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/artifactElision.ts:1150:8"
```

### Pattern

`\b(?:function|class)\s*\*?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:89386550cc6515976d37fac536cd31a9:search

```yaml
regex_id: 89386550cc6515976d37fac536cd31a9
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/scripts/secrets-scan-summarize-and-ingest.mjs:65:2"
```

### Pattern

`^your[-_]api[-_]key$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:897aab287416333b025abda9b63dbc83:search

```yaml
regex_id: 897aab287416333b025abda9b63dbc83
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/slack/src/handlers/channel-manager.ts:103:7"
```

### Pattern

`^[a-z0-9-_]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8b94685782e7cbfdd428959562bc6eca:search

```yaml
regex_id: 8b94685782e7cbfdd428959562bc6eca
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/scripts/secrets-scan-summarize-and-ingest.mjs:68:2"
```

### Pattern

`^my[-_]secret[-_]placeholder[-_]value$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8c0491939003a6918c5cb943f08d0b43:search

```yaml
regex_id: 8c0491939003a6918c5cb943f08d0b43
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/scripts/secrets-scan-summarize-and-ingest.mjs:66:2"
```

### Pattern

`^changeme$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8c192264d74a657f640a50d816648ba7:search

```yaml
regex_id: 8c192264d74a657f640a50d816648ba7
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/utils/artifactParser.ts:886:36"
```

### Pattern

`^(?:'''|""")([^'"]+)(?:'''|""")`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8dac3c743bb3fdc48a91ad5e32d0083c:search

```yaml
regex_id: 8dac3c743bb3fdc48a91ad5e32d0083c
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/services/liveopsTriageService.ts:2861:55"
```

### Pattern

`#(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9909101882e223eebd843c8ff09c6e16:search

```yaml
regex_id: 9909101882e223eebd843c8ff09c6e16
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/artifactParser.ts:569:4"
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

## intent_mismatch:9c64a8390817002f813142d8a3b7fba7:email

```yaml
regex_id: 9c64a8390817002f813142d8a3b7fba7
schema_version: "1"
kind: intent_mismatch
corpus: bike4mind
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/integrations/slack/emailMirror.ts:62:6"
```

### Pattern

`(reset|forgot).*(password)|password.*reset`

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

## usage_mismatch:9cba42a8caa8a099d8c6b4b33da8e7e1:search

```yaml
regex_id: 9cba42a8caa8a099d8c6b4b33da8e7e1
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/src/checkDeprecatedModelUsage.ts:57:2"
```

### Pattern

`test-config\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9f01942bad96afab3806c3ed430d4eed:search

```yaml
regex_id: 9f01942bad96afab3806c3ed430d4eed
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/help/utils.ts:146:31"
```

### Pattern

`^##\s+(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a1379d63dd0b49c19952935a1a7d29ba:search

```yaml
regex_id: a1379d63dd0b49c19952935a1a7d29ba
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/utils/ip.ts:13:2"
```

### Pattern

`^::1$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a6a9e298e06ae6fe12371c9b48c0c4cf:search

```yaml
regex_id: a6a9e298e06ae6fe12371c9b48c0c4cf
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/services/adminTools/modalToolHelpers.ts:210:6"
```

### Pattern

`banner[:\s]+["']?(.+?)["']?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a725861c5c60c435787bb9346fe8f9ef:search

```yaml
regex_id: a725861c5c60c435787bb9346fe8f9ef
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/services/src/modelDiscoveryService/sources/openaiDocs.ts:28:14"
```

### Pattern

`^short context input$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a762ca8d7fe253397601a60d61965877:search

```yaml
regex_id: a762ca8d7fe253397601a60d61965877
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/utils/artifactParser.ts:801:5"
```

### Pattern

`^(build|create|render|make|generate|write)[-_]?(html|artifact|page|webpage|website|ui)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a81d502f0145c7498fd1dab64b88471a:search

```yaml
regex_id: a81d502f0145c7498fd1dab64b88471a
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/artifactParser.ts:573:4"
```

### Pattern

`^This`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a85ca40bd3ed7976f808ca89e0c802e5:search

```yaml
regex_id: a85ca40bd3ed7976f808ca89e0c802e5
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/common/src/queryComplexityClassifier.ts:49:4"
```

### Pattern

`^\s*(bye|goodbye|see you)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a87a0b3e82a5b8dd196d1e1cd63e0cea:search

```yaml
regex_id: a87a0b3e82a5b8dd196d1e1cd63e0cea
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/auth/trustedDevice.ts:49:21"
```

### Pattern

`^([a-f0-9]{24})\.([A-Za-z0-9_-]{20,128})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ac2bb7eac401a612d915f372178f7374:search

```yaml
regex_id: ac2bb7eac401a612d915f372178f7374
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/scripts/secrets-scan-summarize-and-ingest.mjs:64:2"
```

### Pattern

`^your[-_]secret[-_]here$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ac2faa012253973b00730ca901433107:search

```yaml
regex_id: ac2faa012253973b00730ca901433107
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/artifactParser.ts:41:6"
```

### Pattern

`^\s*<svg\b[^>]*\/>\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:acec16520635bf0a3a8ca5fb100c098f:search

```yaml
regex_id: acec16520635bf0a3a8ca5fb100c098f
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/artifactParser.ts:553:4"
```

### Pattern

`^[A-Za-z0-9_]+\s*-*>?\|\w+\|\s*[A-Za-z0-9_]+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ae8fbc4f80b539e52663fa026ae73211:search

```yaml
regex_id: ae8fbc4f80b539e52663fa026ae73211
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/llm-adapters/src/syncModelDescriptions.ts:697:39"
```

### Pattern

`^us\.(\w+)\.(.+)-v\d+:\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b2f0375f8dfda2342b005c52c0ce6e30:search

```yaml
regex_id: b2f0375f8dfda2342b005c52c0ce6e30
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/components/Session/UserPrompt.tsx:35:39"
```

### Pattern

`^\#{1,6}\s|^\*\*|^-\s|^\d+\.\s|^\*\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:b36bebcab5656ca9e1e2f09d8044f506:email

```yaml
regex_id: b36bebcab5656ca9e1e2f09d8044f506
schema_version: "1"
kind: intent_mismatch
corpus: bike4mind
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/integrations/slack/emailMirror.ts:68:6"
```

### Pattern

`system health|health check`

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

## usage_mismatch:b4af861e444b6b98fbcffb5ba603ff99:search

```yaml
regex_id: b4af861e444b6b98fbcffb5ba603ff99
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/cli/src/tools/findDefinitionTool.ts:145:6"
```

### Pattern

`^\s*(\/\/|\/\*|\*|#|"""|''')`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b4b302e226aded96cbce36ab796675cb:search

```yaml
regex_id: b4b302e226aded96cbce36ab796675cb
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/artifactParser.ts:562:4"
```

### Pattern

`^style\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b4c9535bd088dd71abd849b907f2ac2c:search

```yaml
regex_id: b4c9535bd088dd71abd849b907f2ac2c
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/services/publish/transpileReactArtifact.ts:148:29"
```

### Pattern

`^(\w+)\s+as\s+(\w+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b7bef3393a087db0eedd86f833b73f37:search

```yaml
regex_id: b7bef3393a087db0eedd86f833b73f37
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/utils/artifactParser.ts:898:31"
```

### Pattern

`^def\s+(main|run|execute|process)\s*\(`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bb3e1df841a0cbb32f1df86406065789:search

```yaml
regex_id: bb3e1df841a0cbb32f1df86406065789
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/services/src/modelDiscoveryService/sources/openaiDocs.ts:34:18"
```

### Pattern

`^long context cache writes$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bba18688469c34870938756270d1550b:search

```yaml
regex_id: bba18688469c34870938756270d1550b
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/services/publish/transpileReactArtifact.ts:108:25"
```

### Pattern

`^type\s+(?!as\b)\w`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bc9fc2532dbecc0d24638f911c8be84e:search

```yaml
regex_id: bc9fc2532dbecc0d24638f911c8be84e
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/services/publish/viewerSecurity.ts:143:48"
```

### Pattern

`^(localhost|127\.0\.0\.1)(:|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:be49899faead82ca2e42cd4c4f67d1de:search

```yaml
regex_id: be49899faead82ca2e42cd4c4f67d1de
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/artifactParser.ts:307:5"
```

### Pattern

`^(build|create|render|make|generate|write)[-_]?(html|artifact|page|webpage|website|ui)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:be92381b1acf8378ac169e597101e600:search

```yaml
regex_id: be92381b1acf8378ac169e597101e600
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/utils/artifactParser.ts:702:23"
```

### Pattern

`^(?:import|from)\s+\w+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c1b550ec808cbf4ecdd15c10233cb1af:search

```yaml
regex_id: c1b550ec808cbf4ecdd15c10233cb1af
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/common/src/queryComplexityClassifier.ts:46:4"
```

### Pattern

`^(define|what is|explain)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c288d972e964eadee519fc8ca47a0228:search

```yaml
regex_id: c288d972e964eadee519fc8ca47a0228
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/services/publish/transpileReactArtifact.ts:167:33"
```

### Pattern

`^(\w+)\s+as\s+(\w+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c599ac75adc038ae473d3ad6cfffeb7a:search

```yaml
regex_id: c599ac75adc038ae473d3ad6cfffeb7a
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/services/liveopsTriageService.ts:412:6"
```

### Pattern

`^AIza[A-Za-z0-9_-]{35}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c60eb68dce30f538ed9653b4f3f86036:search

```yaml
regex_id: c60eb68dce30f538ed9653b4f3f86036
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/src/checkDeprecatedModelUsage.ts:47:2"
```

### Pattern

`Types\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cb8c66056efb21390f681cc80a5797aa:search

```yaml
regex_id: cb8c66056efb21390f681cc80a5797aa
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/artifactParser.ts:560:4"
```

### Pattern

`^class\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cc8ed1fab1c466cfe3eba78afa606799:search

```yaml
regex_id: cc8ed1fab1c466cfe3eba78afa606799
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/scripts/secrets-scan-summarize-and-ingest.mjs:51:2"
```

### Pattern

`\.spec\.[tj]sx?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ccf876d3cfc4883a87651075bf505c59:search

```yaml
regex_id: ccf876d3cfc4883a87651075bf505c59
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/utils/artifactParser.ts:336:26"
```

### Pattern

`^import\s+(\w+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ce65ee618a10652461b59bf830879748:search

```yaml
regex_id: ce65ee618a10652461b59bf830879748
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/artifactParser.ts:575:4"
```

### Pattern

`^In this`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ceba8840e1d6fdea034b0d10f683a131:search

```yaml
regex_id: ceba8840e1d6fdea034b0d10f683a131
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/src/checkDeprecatedModelUsage.ts:43:2"
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

## usage_mismatch:cf77b2adab6d2b2846070a16bcce5c7c:search

```yaml
regex_id: cf77b2adab6d2b2846070a16bcce5c7c
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/services/liveopsTriageService.ts:2865:55"
```

### Pattern

`-(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d052420d83483a6effef44fe7448d41f:search

```yaml
regex_id: d052420d83483a6effef44fe7448d41f
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/utils/codeBlockTitleExtractor.ts:375:31"
```

### Pattern

`^name\s*:\s*(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d1a3d23a67751267fb195ae8ef8fd09a:search

```yaml
regex_id: d1a3d23a67751267fb195ae8ef8fd09a
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/artifactParser.ts:574:4"
```

### Pattern

`^The above`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d55a91979f7bee0955dd05f88727249a:search

```yaml
regex_id: d55a91979f7bee0955dd05f88727249a
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/services/publish/transpileReactArtifact.ts:157:34"
```

### Pattern

`^(\w+)\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d6fb682c19d6559ea811d0861c871c16:search

```yaml
regex_id: d6fb682c19d6559ea811d0861c871c16
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/services/src/llm/tools/implementation/lattice/index.ts:399:49"
```

### Pattern

`^[a-f0-9]{24}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d734d1c45e8569893ab05b09a5399a57:search

```yaml
regex_id: d734d1c45e8569893ab05b09a5399a57
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/utils/codeBlockTitleExtractor.ts:328:39"
```

### Pattern

`^#\s*([^\n]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:da9b3283d0a535a4457f888f2957d861:search

```yaml
regex_id: da9b3283d0a535a4457f888f2957d861
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/services/liveopsFingerprint.ts:63:2"
```

### Pattern

`^native `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:db4b6daf8938a0f5144844c301f3fa94:search

```yaml
regex_id: db4b6daf8938a0f5144844c301f3fa94
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/artifactElision.ts:1154:8"
```

### Pattern

`\bnew$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dd307cee1c7589923605955779d1dacb:search

```yaml
regex_id: dd307cee1c7589923605955779d1dacb
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/services/src/modelDiscoveryService/sources/openaiDocs.ts:33:17"
```

### Pattern

`^long context cached input$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dd3abae88aa0715d29730cd404e3ff2d:search

```yaml
regex_id: dd3abae88aa0715d29730cd404e3ff2d
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/help/utils.ts:224:31"
```

### Pattern

`^###\s+(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dee95c740923767879da600eeafe4584:search

```yaml
regex_id: dee95c740923767879da600eeafe4584
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/src/checkDeprecatedModelUsage.ts:48:2"
```

### Pattern

`Backend\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dfd5d5f4b19544fe5219a21f6d5b9afd:search

```yaml
regex_id: dfd5d5f4b19544fe5219a21f6d5b9afd
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/scripts/secrets-scan-summarize-and-ingest.mjs:50:2"
```

### Pattern

`\.test\.[tj]sx?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e0b0bace9500d0a70d967f7e6be6ae35:search

```yaml
regex_id: e0b0bace9500d0a70d967f7e6be6ae35
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/common/src/queryComplexityClassifier.ts:42:4"
```

### Pattern

`^what('s| is) your (favorite|preferred|best)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e1e9e5948712b06baa3920fb50ea5f54:search

```yaml
regex_id: e1e9e5948712b06baa3920fb50ea5f54
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/common/src/queryComplexityClassifier.ts:48:4"
```

### Pattern

`^\s*(thanks|thank you|thx)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e4ec955f1c200d7fecb43ca2f38a6813:search

```yaml
regex_id: e4ec955f1c200d7fecb43ca2f38a6813
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/help/validate-help-content.ts:104:23"
```

### Pattern

`^(#{1,6})\s+(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e5084f26c02329d08729b01334ebfccb:search

```yaml
regex_id: e5084f26c02329d08729b01334ebfccb
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/services/src/llm/tools/implementation/excelGeneration/xlsxTestReader.ts:70:12"
```

### Pattern

`\/$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:e575f99bd092b358adf1781f07873223:url

```yaml
regex_id: e575f99bd092b358adf1781f07873223
schema_version: "1"
kind: intent_mismatch
corpus: bike4mind
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/queueHandlers/questExport.ts:457:41"
```

### Pattern

`[.*+?^${}()|[\]\\]`

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

## usage_mismatch:e6da191ef235d95fbbfc0b96d6d5d6f6:search

```yaml
regex_id: e6da191ef235d95fbbfc0b96d6d5d6f6
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/src/checkDeprecatedModelUsage.ts:46:2"
```

### Pattern

`Model\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e859c0a70bcfebf2e5d8a689f49b5413:search

```yaml
regex_id: e859c0a70bcfebf2e5d8a689f49b5413
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/services/src/llm/tools/implementation/excelGeneration/xlsxTestReader.ts:117:26"
```

### Pattern

`^([A-Z]+)(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e8ab5d2198e3df80defe0657bc220290:search

```yaml
regex_id: e8ab5d2198e3df80defe0657bc220290
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/services/liveopsTriageService.ts:411:6"
```

### Pattern

`^AKIA[A-Z0-9]{16}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e8c683a80e8be55d924a897798c62759:search

```yaml
regex_id: e8c683a80e8be55d924a897798c62759
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/utils/ip.ts:14:2"
```

### Pattern

`^(?:0{1,4}:){7}0{0,3}1$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ea1a1131698f806c875bd29037217ab0:search

```yaml
regex_id: ea1a1131698f806c875bd29037217ab0
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/utils/artifactParser.ts:48:6"
```

### Pattern

`^\s*<svg\b[^>]*\/>\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ec59e7fb40f725b31982550ea609618b:search

```yaml
regex_id: ec59e7fb40f725b31982550ea609618b
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/llm-adapters/src/syncModelDescriptions.ts:726:36"
```

### Pattern

`^(.+)-(\d{4}-\d{2}-\d{2})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ecc107cfabe98b2db168a5baf9a9989e:search

```yaml
regex_id: ecc107cfabe98b2db168a5baf9a9989e
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/fab-pipeline/src/chunk.ts:491:36"
```

### Pattern

`slide(\d+)\.xml$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ecd34f6d8182d1252b122da421c6523e:search

```yaml
regex_id: ecd34f6d8182d1252b122da421c6523e
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/packages/scripts/src/checkDeprecatedModelUsage.ts:44:2"
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

## usage_mismatch:edd37f143e70ad837594aa3dca50cbbc:search

```yaml
regex_id: edd37f143e70ad837594aa3dca50cbbc
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/scripts/secrets-scan-summarize-and-ingest.mjs:67:2"
```

### Pattern

`^not[-_]configured$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ef64d1ede7d12ccd5e00f61ef9e98e0b:search

```yaml
regex_id: ef64d1ede7d12ccd5e00f61ef9e98e0b
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/artifactParser.ts:570:4"
```

### Pattern

`^Let me`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:efe9ce979136fddd6f67f71d26a08034:email

```yaml
regex_id: efe9ce979136fddd6f67f71d26a08034
schema_version: "1"
kind: intent_mismatch
corpus: bike4mind
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/integrations/slack/emailMirror.ts:63:6"
```

### Pattern

`verif|confirm your email|activate`

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

## usage_mismatch:f043403d10657e87951c159edc928c0a:search

```yaml
regex_id: f043403d10657e87951c159edc928c0a
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/common/src/queryComplexityClassifier.ts:43:4"
```

### Pattern

`^(tell me about|what about|how about)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f0b16ea60880cdd763cbadce227bdf03:search

```yaml
regex_id: f0b16ea60880cdd763cbadce227bdf03
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/utils/ip.ts:17:2"
```

### Pattern

`^f[cd][0-9a-f]{2}:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f2ad60e833064f1250840f004919caaf:search

```yaml
regex_id: f2ad60e833064f1250840f004919caaf
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/utils/src/artifactParser.ts:42:40"
```

### Pattern

`^\s*<svg\b[^>]*>`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f7224334dd309f176a577087f51d9967:search

```yaml
regex_id: f7224334dd309f176a577087f51d9967
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/server/utils/ip.ts:15:2"
```

### Pattern

`^::$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:f87129f7a4a8878899033a2e76b27325:email

```yaml
regex_id: f87129f7a4a8878899033a2e76b27325
schema_version: "1"
kind: intent_mismatch
corpus: bike4mind
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/services/src/lib/turndown.ts:114:28"
```

### Pattern

`<!--\s*email signature\s*-->[\s\S]*?<!--\s*\/email signature\s*-->`

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

## usage_mismatch:fbaff008257bcea86fc246ffbb38f72c:search

```yaml
regex_id: fbaff008257bcea86fc246ffbb38f72c
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/scripts/secrets-scan-summarize-and-ingest.mjs:57:2"
```

### Pattern

`README\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fbfd987992995601b03ebaa62135fe21:search

```yaml
regex_id: fbfd987992995601b03ebaa62135fe21
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/services/src/llm/tools/implementation/lattice/index.ts:536:49"
```

### Pattern

`^[a-f0-9]{24}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fec285fec94aa196fac127e09c7bccc2:search

```yaml
regex_id: fec285fec94aa196fac127e09c7bccc2
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/apps/client/app/utils/artifactParser.ts:49:40"
```

### Pattern

`^\s*<svg\b[^>]*>`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fedb1b23dfd200d39dd93003aa23f3a4:search

```yaml
regex_id: fedb1b23dfd200d39dd93003aa23f3a4
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/slack/src/agent-parser.ts:214:18"
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

## usage_mismatch:ff5e329c62a58f66c5ed4a5ba618b623:search

```yaml
regex_id: ff5e329c62a58f66c5ed4a5ba618b623
schema_version: "1"
kind: usage_mismatch
corpus: bike4mind
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/bike4mind/rules/b4m-core/llm-adapters/src/syncModelDescriptions.ts:713:35"
```

### Pattern

`^(\w+)\.(.+)-v\d+$`

### Context

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
corpus: bike4mind
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
corpus: bike4mind
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
corpus: bike4mind
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
corpus: bike4mind
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

---
schema_version: "1"
corpus: JARVIS
findings: 95
---

# JARVIS batch findings

## usage_mismatch:039f40a08235d09d32aee8a4a6d6e224:search

```yaml
regex_id: 039f40a08235d09d32aee8a4a6d6e224
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/governance/providers.py:1956:21"
```

### Pattern

`^\s*(?:from|import)\s+([\w.]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0e0232f814f05acc8a4d7fc18f0fec57:search

```yaml
regex_id: 0e0232f814f05acc8a4d7fc18f0fec57
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:218:16"
```

### Pattern

`\[\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0e3b3bc5c8d508d41535340c45793233:search

```yaml
regex_id: 0e3b3bc5c8d508d41535340c45793233
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/scripts/migrate_memory_topics.py:481:16"
```

### Pattern

`^modules:\s*\[([^\]]*)\]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0e93272e8c9091e274b979bf4ae13ac5:search

```yaml
regex_id: 0e93272e8c9091e274b979bf4ae13ac5
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/scripts/a1_graduation_auditor.py:663:26"
```

### Pattern

`\[CommProtocol\]\s+INTENT\s+op=(?P<op>[\w.:-]+)\s+seq=(?P<seq>\d+)\s.*?\bpayload=(?P<payload>\{.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0f1a3d4b33cdbc8f140af5f9b227d32b:search

```yaml
regex_id: 0f1a3d4b33cdbc8f140af5f9b227d32b
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/scripts/bake_jprime_golden_image.py:479:4"
```

### Pattern

`^[^#]*exit [1-9]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1bf5491457edc13cd20d62f9e37f64cc:search

```yaml
regex_id: 1bf5491457edc13cd20d62f9e37f64cc
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:214:16"
```

### Pattern

`^\s+\w+.*[^,\[\{\(]\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1dadcfda1a555f6e9bed69decea04aeb:search

```yaml
regex_id: 1dadcfda1a555f6e9bed69decea04aeb
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:236:12"
```

### Pattern

`^["\']`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1f4d318d71377c4b0e7cb3af94ec778a:search

```yaml
regex_id: 1f4d318d71377c4b0e7cb3af94ec778a
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/engines/nlp_engine.py:101:16"
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

## usage_mismatch:1f7ed9e6a99be52ae54ab6da533143ca:search

```yaml
regex_id: 1f7ed9e6a99be52ae54ab6da533143ca
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/context_intelligence/handlers/math_solver.py:48:19"
```

### Pattern

`^[\d a-zA-Z\+\-\*/\^\(\)\.\,\=\s]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1f840d267c020f08d9a7eacb47bda0a4:search

```yaml
regex_id: 1f840d267c020f08d9a7eacb47bda0a4
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/api/query_handler.py:294:21"
```

### Pattern

`^\s*(?:h(?:ello|i|ey)|good\s+(?:morning|afternoon|evening|night)|what\'?s?\s+up|howdy|yo|sup|greetings|hi+\s+(?:how\s+are\s+you|there|jarvis)|how\s+are\s+you|how\'?s?\s+it\s+going|thanks?|thank\s+you)\s*[?!.]*\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:22773b2e1e1b9e976fc3a5c99959e9f6:search

```yaml
regex_id: 22773b2e1e1b9e976fc3a5c99959e9f6
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/engines/nlp_engine.py:100:16"
```

### Pattern

`^(what|when|where|who|why|how|which|can|could|would|should|is|are|do|does)\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:23ce2439550aa64ac6c7281165f21a48:search

```yaml
regex_id: 23ce2439550aa64ac6c7281165f21a48
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:244:12"
```

### Pattern

`^__all__\s*=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2b9b1954a9e3b918d96b83fd7efa039c:search

```yaml
regex_id: 2b9b1954a9e3b918d96b83fd7efa039c
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/governance/intent_classifier.py:175:23"
```

### Pattern

`^\s*(explain|describe|tell me|summarize|recap|compare|contrast|document|clarify)\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2cbc99aa8e6fc46486583fa6ccce5771:search

```yaml
regex_id: 2cbc99aa8e6fc46486583fa6ccce5771
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:226:12"
```

### Pattern

`^\s*#\s*Module truncated`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2d3c2857e697b3dc75bdb9c50010912b:search

```yaml
regex_id: 2d3c2857e697b3dc75bdb9c50010912b
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/governance/providers.py:1856:15"
```

### Pattern

`^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2f51c3e08ad74f540b3cf3270eef42c3:search

```yaml
regex_id: 2f51c3e08ad74f540b3cf3270eef42c3
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/brainstem/action_dispatcher.py:41:24"
```

### Pattern

`^(?:message|msg|text)\s+(.+?)\s+on\s+(\S+)\s+(?:saying\s+)?(.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:323e4d32dd0835bad587eb4aeefdc6d3:search

```yaml
regex_id: 323e4d32dd0835bad587eb4aeefdc6d3
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/brainstem/action_dispatcher.py:55:4"
```

### Pattern

`^text\s+(\S+)\s+(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:37c565da32906463ad701b57109eae3b:search

```yaml
regex_id: 37c565da32906463ad701b57109eae3b
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:239:12"
```

### Pattern

`^\s*\}\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:418035ac24281234a34347a4224bb930:search

```yaml
regex_id: 418035ac24281234a34347a4224bb930
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/scripts/migrate_memory_topics.py:337:14"
```

### Pattern

`^#\s+(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:41e78aa48e2c27c2e3e4505be997397e:search

```yaml
regex_id: 41e78aa48e2c27c2e3e4505be997397e
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/brainstem/action_dispatcher.py:112:8"
```

### Pattern

`(saying\s+)(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:485ca5f8d2da229d3b084f90df5dfd56:search

```yaml
regex_id: 485ca5f8d2da229d3b084f90df5dfd56
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:196:16"
```

### Pattern

`f"[^"]*\{[^}]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4bde15c091f38d4ba6b6e87c9d0af4dd:search

```yaml
regex_id: 4bde15c091f38d4ba6b6e87c9d0af4dd
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/audio/conversation_pipeline.py:90:16"
```

### Pattern

`^(?:(?:hey\s+)?jarvis[,\s]*)?(?:goodbye|good\s*bye|bye(?:\s+bye)?|stop|exit|quit|end\s+(?:the\s+)?conversation|that'?s\s+all|i'?m\s+done|stop\s+(?:talking|listening|the\s+conversation)|jarvis\s+(?:stop|quit))[\s.!?]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5501b6b7fe4d6c88524c55f0d0d01542:search

```yaml
regex_id: 5501b6b7fe4d6c88524c55f0d0d01542
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:227:12"
```

### Pattern

`^\s*#\s*TODO:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:581c5bd6a054665fac9f46d280236e51:match

```yaml
regex_id: 581c5bd6a054665fac9f46d280236e51
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/governance/ide_observability.py:1586:15"
```

### Pattern

`^JARVIS_[A-Za-z0-9_]{1,128}$`

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

## usage_mismatch:5a6c803afaa6ef63a2219fda65877cb1:search

```yaml
regex_id: 5a6c803afaa6ef63a2219fda65877cb1
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:208:16"
```

### Pattern

`^\s*from\s+\w+\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5b68955ffd010433d8bae50921d2d1fb:search

```yaml
regex_id: 5b68955ffd010433d8bae50921d2d1fb
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:220:16"
```

### Pattern

`\(\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6222db609696b6ea8d714d04e71459ee:search

```yaml
regex_id: 6222db609696b6ea8d714d04e71459ee
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/voice/intelligent_command_handler.py:686:26"
```

### Pattern

`^(?:\d+\s+(?:second|minute|hour|min|sec|hr)s?\s+)?(?:when\s+it\s+says?\s+)?`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:645cf06337803194247b573ea6187903:search

```yaml
regex_id: 645cf06337803194247b573ea6187903
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:238:12"
```

### Pattern

`^\s*\]\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:68d9c34b5a30ecc167394c8d64ab2b0f:search

```yaml
regex_id: 68d9c34b5a30ecc167394c8d64ab2b0f
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:219:16"
```

### Pattern

`\{\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6bd62c0c952d94f5a7bc170f3aeba57f:search

```yaml
regex_id: 6bd62c0c952d94f5a7bc170f3aeba57f
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:235:12"
```

### Pattern

`^\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:71fe8c915ef9595abe4e3aa4babe38e1:search

```yaml
regex_id: 71fe8c915ef9595abe4e3aa4babe38e1
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:189:16"
```

### Pattern

`'''[^']*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7c431bb2216438a931ac67d234b19226:search

```yaml
regex_id: 7c431bb2216438a931ac67d234b19226
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:194:16"
```

### Pattern

`"[^"\n\\]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7cdf1b73e4e0d436d48f83d004d721c7:search

```yaml
regex_id: 7cdf1b73e4e0d436d48f83d004d721c7
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:190:16"
```

### Pattern

`^\s*""".*(?!""")\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7ff2dcd1a3f06a276df5b88d498bb8dd:search

```yaml
regex_id: 7ff2dcd1a3f06a276df5b88d498bb8dd
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/governance/patch_domain_guard.py:48:4"
```

### Pattern

`(^|/)conftest\.py$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:838ca4362f67762fabe0104f94e00fe9:search

```yaml
regex_id: 838ca4362f67762fabe0104f94e00fe9
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:204:16"
```

### Pattern

`^\s*class\s+\w+.*:\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8763cb4fc18c8cda1ae0fe1f73b4465b:search

```yaml
regex_id: 8763cb4fc18c8cda1ae0fe1f73b4465b
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/brainstem/action_dispatcher.py:30:24"
```

### Pattern

`^(?:open|launch|start)\s+(?:the\s+)?(.+?)\s+and\s+(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8797d214644b3a3e8423218ff82939bc:search

```yaml
regex_id: 8797d214644b3a3e8423218ff82939bc
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/governance/patch_domain_guard.py:47:4"
```

### Pattern

`\.spec\.[a-z0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:8819d5e384f44d1fc8f1cb1ab9eb3788:email

```yaml
regex_id: 8819d5e384f44d1fc8f1cb1ab9eb3788
schema_version: "1"
kind: intent_mismatch
corpus: JARVIS
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/api/unified_command_processor.py:2967:26"
```

### Pattern

`(?i)(?:ignore\s+(?:all\s+)?previous|forget\s+(?:all\s+)?instructions)|(?:system\s*:\s*)|(?:<\|(?:im_start|im_end|endoftext)\|>)|(?:\[INST\]|\[/INST\])|(?:```(?:system|instruction))|(?:you\s+are\s+now\s+(?:a|an|in))|(?:new\s+instructions?:)|(?:override\s+(?:all\s+)?(?:previous|above))|(?:</?\s*workspace_data\s*/?\s*>)|(?:</?\s*system\s*>)|(?:(?:human|assistant|user)\s*:)`

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

## usage_mismatch:88397fdaac7e7b9fbf5d75daf77320ba:search

```yaml
regex_id: 88397fdaac7e7b9fbf5d75daf77320ba
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/governance/patch_domain_guard.py:45:4"
```

### Pattern

`-test\.[a-z0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8f45eca97a18d23e8837d0b1699ac43f:search

```yaml
regex_id: 8f45eca97a18d23e8837d0b1699ac43f
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:201:16"
```

### Pattern

`^\s*async\s+def\s+\w+\s*\([^)]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9a7ff36ff4669036d69fcca3daa2b109:search

```yaml
regex_id: 9a7ff36ff4669036d69fcca3daa2b109
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/scripts/migrate_memory_topics.py:206:17"
```

### Pattern

`[`',\)\]>:]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9c4ab5b91cab35d2774dae773b31d7ad:search

```yaml
regex_id: 9c4ab5b91cab35d2774dae773b31d7ad
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/governance/providers.py:1733:15"
```

### Pattern

`^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9c55359b402d591225a8e1e796b0bb01:search

```yaml
regex_id: 9c55359b402d591225a8e1e796b0bb01
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:209:16"
```

### Pattern

`^\s*import\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9cabda45a2cef87b522841b3201f534f:search

```yaml
regex_id: 9cabda45a2cef87b522841b3201f534f
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:200:16"
```

### Pattern

`^\s*def\s+\w+\s*\([^)]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9d3bc45a4e7a8ba13c926d927c2d6826:search

```yaml
regex_id: 9d3bc45a4e7a8ba13c926d927c2d6826
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/scripts/migrate_memory_topics.py:209:20"
```

### Pattern

`\.(py|ts|tsx|kt|rs|js)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9db84c27527c16692d6fc39c43b9200d:search

```yaml
regex_id: 9db84c27527c16692d6fc39c43b9200d
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:195:16"
```

### Pattern

`'[^'\n\\]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9deac50c86a67e7d47dc7b9586ce6da3:search

```yaml
regex_id: 9deac50c86a67e7d47dc7b9586ce6da3
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/context_intelligence/handlers/query_complexity_manager.py:369:17"
```

### Pattern

`^(?:is|are|was|were|do|does|did|can|could|will|would|should)\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a372a272e56f010ba52bfc2b98552351:search

```yaml
regex_id: a372a272e56f010ba52bfc2b98552351
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:210:16"
```

### Pattern

`^\s*from\s+[\w.]+\s+import\s*\($`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a435372fe5cb5a35c30afcf15397b350:search

```yaml
regex_id: a435372fe5cb5a35c30afcf15397b350
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/brainstem/action_dispatcher.py:51:4"
```

### Pattern

`^send\s+(.+?)\s+a\s+message\s+saying\s+(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a77fc5fbb70debc160081df8828152e6:search

```yaml
regex_id: a77fc5fbb70debc160081df8828152e6
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/governance/intent_classifier.py:165:18"
```

### Pattern

`^\s*(why|how|what|when|where|which|who|is\s|are\s|does\s|do\s|can\s|could\s|should\s|would\s|will\s)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a798c35dc68b2c8eda0899890007ec00:search

```yaml
regex_id: a798c35dc68b2c8eda0899890007ec00
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:243:12"
```

### Pattern

`^\s*#.*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a8313367e9d9b967d7677abd6771742f:search

```yaml
regex_id: a8313367e9d9b967d7677abd6771742f
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/governance/ide_observability.py:153:12"
```

### Pattern

`^[A-Za-z0-9_\-]{1,128}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a897741b20cfccd79b131da50aa4e5dd:search

```yaml
regex_id: a897741b20cfccd79b131da50aa4e5dd
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/brainstem/action_dispatcher.py:24:20"
```

### Pattern

`^(?:open|launch|start|run)\s+(?:the\s+)?(.+?)(?:\s+app)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a8ce2ca9ed135f78acac71ae51753af1:search

```yaml
regex_id: a8ce2ca9ed135f78acac71ae51753af1
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/governance/patch_domain_guard.py:42:4"
```

### Pattern

`(^|/)test_[^/]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a971d942b295a4e0710821732ccc828a:search

```yaml
regex_id: a971d942b295a4e0710821732ccc828a
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:242:12"
```

### Pattern

`^\s*raise\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:aad058c986d532fc5f41ba202f7f1934:match

```yaml
regex_id: aad058c986d532fc5f41ba202f7f1934
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/governance/ide_observability.py:2137:32"
```

### Pattern

`^[A-Za-z0-9_\-:.]{1,128}$`

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

## usage_mismatch:ab3be77f1a82a5f939d7b274247ca182:search

```yaml
regex_id: ab3be77f1a82a5f939d7b274247ca182
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/vision/screen_vision.py:513:12"
```

### Pattern

`^(\w+(?:\s+\w+)?)\s+update`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:acd1ed96cc2b4afa91a7364db3cb0773:match

```yaml
regex_id: acd1ed96cc2b4afa91a7364db3cb0773
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/native_integration.py:18177:15"
```

### Pattern

`^[a-zA-Z_][a-zA-Z0-9_]*$`

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

## usage_mismatch:af94bade620b71dd28fbeead835629af:search

```yaml
regex_id: af94bade620b71dd28fbeead835629af
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/brainstem/action_dispatcher.py:49:4"
```

### Pattern

`^(?:message|msg)\s+(.+?)\s+saying\s+(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b09bd7470f55db52a9b028c09e44da16:search

```yaml
regex_id: b09bd7470f55db52a9b028c09e44da16
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/scripts/migrate_memory_topics.py:338:18"
```

### Pattern

`^---\s*\n.*?^---\s*\n`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b5b60c39cfa78eaf056eaa9d8974c35c:match

```yaml
regex_id: b5b60c39cfa78eaf056eaa9d8974c35c
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/governance/ide_observability.py:2260:34"
```

### Pattern

`^[A-Za-z0-9_\-:.]{1,128}$`

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

## usage_mismatch:b9db8b8cf439a0106eb5af5c68c48d1c:search

```yaml
regex_id: b9db8b8cf439a0106eb5af5c68c48d1c
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/governance/failure_mode_memory.py:1002:16"
```

### Pattern

`^\+\s*def\s+(\w+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ba858d30d10edb0522b9737feb63b445:search

```yaml
regex_id: ba858d30d10edb0522b9737feb63b445
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/brainstem/action_dispatcher.py:54:4"
```

### Pattern

`^(?:message|msg)\s+(\S+)\s+(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bc6a8bae29dc94069ffd540962c5a8ea:search

```yaml
regex_id: bc6a8bae29dc94069ffd540962c5a8ea
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/governance/intent_classifier.py:196:15"
```

### Pattern

`^[ \t]{2,}\S`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:be4911b3e171b0c6fa67e3c269395a70:search

```yaml
regex_id: be4911b3e171b0c6fa67e3c269395a70
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/intelligence/context_engine.py:809:28"
```

### Pattern

`^\s*(class|struct|interface|type)\s+(\w+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c057d2e4141b8d7f6de81f6d9f4cbf9e:search

```yaml
regex_id: c057d2e4141b8d7f6de81f6d9f4cbf9e
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:240:12"
```

### Pattern

`^\s*return\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c3fd808af53c7e3bcab4f95c330b1889:search

```yaml
regex_id: c3fd808af53c7e3bcab4f95c330b1889
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/governance/failure_mode_memory.py:1003:18"
```

### Pattern

`^\+\s*class\s+(\w+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c49284cabe6979bdad8422379e6d106a:search

```yaml
regex_id: c49284cabe6979bdad8422379e6d106a
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/governance/intent_classifier.py:206:13"
```

### Pattern

`^\s*(?:hi|hiya|hey|heya|hello|yo|sup|howdy|greetings|gm|gn|good\s+(?:morning|afternoon|evening|night)|thanks|thank\s+you|thx|ty|ok|okay|kk|cool|nice|great|awesome|perfect|bye|goodbye|later|cya|ping|test)(?:[\s,!.]+(?:karen|jarvis|ov|there))?[\s!.,?]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c669f81ad8cf9a2a1e9992d549169c1b:search

```yaml
regex_id: c669f81ad8cf9a2a1e9992d549169c1b
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/governance/patch_domain_guard.py:46:4"
```

### Pattern

`_spec\.[a-z0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c8535734c2c22d3f5f6b0c1113488832:search

```yaml
regex_id: c8535734c2c22d3f5f6b0c1113488832
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/brainstem/action_dispatcher.py:58:4"
```

### Pattern

`^send\s+(\S+(?:\s+\S+)?)\s+a\s+message$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c8a215aec466490e504d0785aa0d4dd2:search

```yaml
regex_id: c8a215aec466490e504d0785aa0d4dd2
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:241:12"
```

### Pattern

`^\s*pass\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c9c2b314f51c2a47b8594ace824e3fec:search

```yaml
regex_id: c9c2b314f51c2a47b8594ace824e3fec
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:188:16"
```

### Pattern

`"""[^"]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cc09e2bf7fd263bcdc05f97609051b76:search

```yaml
regex_id: cc09e2bf7fd263bcdc05f97609051b76
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/governance/patch_domain_guard.py:44:4"
```

### Pattern

`\.test\.[a-z0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cc843af544028d80aec712deac00dbdd:search

```yaml
regex_id: cc843af544028d80aec712deac00dbdd
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/brainstem/action_dispatcher.py:52:4"
```

### Pattern

`^text\s+(.+?)\s+saying\s+(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cf1f263e774e2fd48d4778d554d2ed53:search

```yaml
regex_id: cf1f263e774e2fd48d4778d554d2ed53
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/brainstem/action_dispatcher.py:50:4"
```

### Pattern

`^send\s+(?:a\s+)?message\s+to\s+(.+?)\s+saying\s+(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cf7edb1dd3d661a8b28ee492c9e10a31:search

```yaml
regex_id: cf7edb1dd3d661a8b28ee492c9e10a31
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:237:12"
```

### Pattern

`^\s*\)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cf9a036c879028bb46b000c07d1029b5:search

```yaml
regex_id: cf9a036c879028bb46b000c07d1029b5
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/governance/failure_mode_memory.py:1009:22"
```

### Pattern

`^\+\s*async\s+def\s+(\w+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d1657a455d737975287c205d6300b2dd:search

```yaml
regex_id: d1657a455d737975287c205d6300b2dd
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/governance/ide_observability.py:164:16"
```

### Pattern

`^[A-Za-z0-9_\-:.]{1,256}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d26550226e84ff6de7856b76b51873eb:search

```yaml
regex_id: d26550226e84ff6de7856b76b51873eb
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/governance/patch_domain_guard.py:43:4"
```

### Pattern

`_test\.[a-z0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d71dd7f4785650e72ee3f2f1377e0836:search

```yaml
regex_id: d71dd7f4785650e72ee3f2f1377e0836
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/scripts/trace_qwen_tool_syntax.py:133:8"
```

### Pattern

`^\s*(diff --git|--- a/|\+\+\+ b/|@@ )`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d8c8646a1a590a735490bd840960472a:search

```yaml
regex_id: d8c8646a1a590a735490bd840960472a
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/brainstem/action_dispatcher.py:59:4"
```

### Pattern

`^send\s+(?:a\s+)?message\s+to\s+(\S+(?:\s+\S+)?)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:da5a7269e9b60b258062fdab70fae2c2:search

```yaml
regex_id: da5a7269e9b60b258062fdab70fae2c2
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/governance/failure_mode_memory.py:1006:26"
```

### Pattern

`^\+\s*@dataclass`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:db8278b38aa52ae880531bdf6fd01111:search

```yaml
regex_id: db8278b38aa52ae880531bdf6fd01111
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/intelligence/context_engine.py:808:27"
```

### Pattern

`^\s*(function|def|fn|func|pub fn|async fn)\s+(\w+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e0706e8166343ff89d21a8075b1b472a:search

```yaml
regex_id: e0706e8166343ff89d21a8075b1b472a
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:229:12"
```

### Pattern

`^\s*pass\s*#.*truncat`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e673686957842718e729c73b4f2e0def:search

```yaml
regex_id: e673686957842718e729c73b4f2e0def
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:230:12"
```

### Pattern

`^\s*\.\.\.\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e6840339b657851dc7f9a5fd7cf15e98:search

```yaml
regex_id: e6840339b657851dc7f9a5fd7cf15e98
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/brainstem/action_dispatcher.py:57:4"
```

### Pattern

`^(?:message|msg|text)\s+(\S+(?:\s+\S+)?)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e73e0f8246b1c28eab62ecf168b56b44:search

```yaml
regex_id: e73e0f8246b1c28eab62ecf168b56b44
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/governance/ide_observability.py:158:17"
```

### Pattern

`^[A-Za-z0-9_\-:.]{1,128}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ea378390a6ad7130a2b72a28d2e7c310:search

```yaml
regex_id: ea378390a6ad7130a2b72a28d2e7c310
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/context_intelligence/handlers/query_complexity_manager.py:366:17"
```

### Pattern

`^(?:spell|translate)\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ed4bf2a4135f318e2837815fd844c8d2:search

```yaml
regex_id: ed4bf2a4135f318e2837815fd844c8d2
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/audio/conversation_pipeline.py:56:30"
```

### Pattern

`^\s*(?:please\s+)?(?:open|close|launch|run|execute|send|set|switch|turn|enable|disable|connect|disconnect|start|stop|restart|shutdown|lock|unlock|schedule|create|delete|kill|play|pause|resume|show|hide|find|search|check|mute|unmute|move|resize|minimize|maximize|take|navigate|scan|refresh|update|install|uninstall|download|upload|sync|compose|forward|reply|share|print|save|(?:read\s+(?!me\b))|(?:go\s+(?!ahead\b|on\b|figure))|(?:look\s+(?!at\s+(?:this|that)\b))|(?:copy\s+(?!that\b)))\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f985ff8ae9765f4a918141d710718332:search

```yaml
regex_id: f985ff8ae9765f4a918141d710718332
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/file_integrity_guardian.py:228:12"
```

### Pattern

`^\s*#\s*FIXME:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f987d574f181464ffc32084b16c459e4:search

```yaml
regex_id: f987d574f181464ffc32084b16c459e4
schema_version: "1"
kind: usage_mismatch
corpus: JARVIS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/JARVIS/rules/backend/core/ouroboros/integration.py:961:21"
```

### Pattern

`^@\w+`

### Context

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
corpus: JARVIS
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
corpus: JARVIS
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
corpus: JARVIS
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
corpus: JARVIS
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

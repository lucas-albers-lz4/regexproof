---
schema_version: "1"
corpus: caia
findings: 124
---

# caia batch findings

## usage_mismatch:04a57061bfd48efb78f904c8e687c579:search

```yaml
regex_id: 04a57061bfd48efb78f904c8e687c579
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/local-llm-router/src/caveman-output.ts:72:2"
```

### Pattern

`^Let me (?:help|walk|explain|show|break|go through)\b[^\n]{0,120}\n+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:04ae4fc663ae8f4d1603dc6b30ceda57:search

```yaml
regex_id: 04ae4fc663ae8f4d1603dc6b30ceda57
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/librarian/src/source-readers.ts:223:6"
```

### Pattern

`^cci_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:071c95838632b7261a3aa9cbe745ee4b:search

```yaml
regex_id: 071c95838632b7261a3aa9cbe745ee4b
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/local-llm-router/src/caveman-output.ts:79:2"
```

### Pattern

`\n+(?:Would|Do) you (?:like|want) (?:me to|to)\b[^\n]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0966cdf9f5073001b95aa044a57d44ef:search

```yaml
regex_id: 0966cdf9f5073001b95aa044a57d44ef
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/ea-drift-sentinel/src/principle-rules.ts:26:22"
```

### Pattern

`^(deploy|infra|build|spend)\.`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:09f978f9173a81cb2e05b6e414571c55:search

```yaml
regex_id: 09f978f9173a81cb2e05b6e414571c55
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/policy-linter/src/policies/subscription-only-build.ts:43:2"
```

### Pattern

`_API_KEY$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0a23a610c61eb74a0c3681a84c47e290:search

```yaml
regex_id: 0a23a610c61eb74a0c3681a84c47e290
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/business-proposal-generator/src/proposal/word-count.ts:47:27"
```

### Pattern

`^#\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1194ebb86a6cd2b4f73e718367c20dfd:search

```yaml
regex_id: 1194ebb86a6cd2b4f73e718367c20dfd
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/local-llm-router/src/caveman-output.ts:80:2"
```

### Pattern

`\n+I hope (?:this|that)\b[^\n]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:121da0b169e3af3baad5a4fa4015af63:search

```yaml
regex_id: 121da0b169e3af3baad5a4fa4015af63
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/librarian/src/source-readers.ts:224:6"
```

### Pattern

`^mac_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:13abf3aea13c11faea4e1c33efb756b4:search

```yaml
regex_id: 13abf3aea13c11faea4e1c33efb756b4
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/apprentice-corpus/src/quality.ts:86:21"
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

## usage_mismatch:153027009f0de2d148f18d470a23adcd:search

```yaml
regex_id: 153027009f0de2d148f18d470a23adcd
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/policy-linter/src/policies/subscription-only-build.ts:42:2"
```

### Pattern

`^MAX_TOKENS$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:16792236d056eec578ad039f31b6be12:search

```yaml
regex_id: 16792236d056eec578ad039f31b6be12
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/scripts/reuse-check.js:127:2"
```

### Pattern

`^\s*(?:export\s+)?enum\s+([A-Za-z_$][\w$]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1a853611c6de6ba6cf3bf0bd20494bba:search

```yaml
regex_id: 1a853611c6de6ba6cf3bf0bd20494bba
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/scripts/reuse-check.js:114:2"
```

### Pattern

`^\s*export\s+enum\s+([A-Za-z_$][\w$]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2027311046b2f8f664d747b683709bd2:search

```yaml
regex_id: 2027311046b2f8f664d747b683709bd2
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/policy-linter/src/policies/ea-agent-gate.ts:46:2"
```

### Pattern

`packages\/[^/]+\/package\.json$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:215cbad90aa81ab617d9ffe1cd50e67c:search

```yaml
regex_id: 215cbad90aa81ab617d9ffe1cd50e67c
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/local-llm-router/src/caveman-output.ts:76:2"
```

### Pattern

`\n+Let me know\b[^\n]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:225c7eac6c1ca51bb0e433cfceda902d:search

```yaml
regex_id: 225c7eac6c1ca51bb0e433cfceda902d
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/librarian/src/source-readers.ts:212:6"
```

### Pattern

`^feedback_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:250a2064194c449c91e3f661c1fe8d3c:search

```yaml
regex_id: 250a2064194c449c91e3f661c1fe8d3c
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/librarian/src/source-readers.ts:220:33"
```

### Pattern

`^evidence_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:31657dd52bed49b45554c8f4a65d7fca:search

```yaml
regex_id: 31657dd52bed49b45554c8f4a65d7fca
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/prompt-optimizer/src/stage1.ts:70:15"
```

### Pattern

`^﻿`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:33c9364044f071d7bea6b59c79a3e0a6:search

```yaml
regex_id: 33c9364044f071d7bea6b59c79a3e0a6
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/policy-linter/src/policies/subscription-only-build.ts:38:2"
```

### Pattern

`^OPENAI_API_KEY$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:37145313af2ef41467668147b1895491:search

```yaml
regex_id: 37145313af2ef41467668147b1895491
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/critic/src/detectors/decision-classifier.ts:27:21"
```

### Pattern

`^\s*(?:\/\/|#|--|\*)\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3740f333a8048a91db4fdccd44fc2e0f:search

```yaml
regex_id: 3740f333a8048a91db4fdccd44fc2e0f
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/policy-linter/src/policies/no-idle-research.ts:61:2"
```

### Pattern

`^#{1,6}\s*conclusion[s]?\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:386fecdc14f0b1735bc05f705ceccfa5:search

```yaml
regex_id: 386fecdc14f0b1735bc05f705ceccfa5
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/architecture-registry/src/extractors/drizzle-extractor.ts:124:14"
```

### Pattern

`^uniqueIndex\(`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3b38d9d2c582883e8807773d74244ba8:search

```yaml
regex_id: 3b38d9d2c582883e8807773d74244ba8
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/reviewer/src/detectors/shared.ts:84:9"
```

### Pattern

`\.(ts|tsx|js|jsx|mjs|cjs)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3b51cefc0d6d8d144f03597fe62ae173:search

```yaml
regex_id: 3b51cefc0d6d8d144f03597fe62ae173
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/policy-linter/src/policies/no-idle-research.ts:60:2"
```

### Pattern

`^#{1,6}\s*outcome[s]?\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3c32adb218f785a9fd2aa26272008501:search

```yaml
regex_id: 3c32adb218f785a9fd2aa26272008501
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/ea-architect/src/repository-loader.ts:116:30"
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

## usage_mismatch:3d0559a8fb797eadb2539ff33c67bf6c:search

```yaml
regex_id: 3d0559a8fb797eadb2539ff33c67bf6c
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/architecture-registry/src/extractors/component-extractor.ts:56:26"
```

### Pattern

`^[A-Z][A-Za-z0-9]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3f27df21cc43c1c0a6756983bf0d8956:search

```yaml
regex_id: 3f27df21cc43c1c0a6756983bf0d8956
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/apprentice-corpus/src/quality.ts:85:21"
```

### Pattern

`^[-*]\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3f759a737891b4d8f93c6e6a7365cfcd:search

```yaml
regex_id: 3f759a737891b4d8f93c6e6a7365cfcd
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/librarian/src/source-readers.ts:229:33"
```

### Pattern

`^orchestrator_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:43e2bd8c43e5ffd4bf9babaa668b94ae:search

```yaml
regex_id: 43e2bd8c43e5ffd4bf9babaa668b94ae
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/local-llm-router/src/caveman-output.ts:67:2"
```

### Pattern

`^Certainly[!.,]?\s+[^\n]{0,120}\n+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:441a8dadb3586ee186579e8e973f7b12:search

```yaml
regex_id: 441a8dadb3586ee186579e8e973f7b12
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/chain-runner/bin/consumption-probe.js:172:24"
```

### Pattern

`(^|\/)package\.json$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:46914cb21ec6bedb6bd4d7ad435e2044:search

```yaml
regex_id: 46914cb21ec6bedb6bd4d7ad435e2044
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/librarian/src/source-readers.ts:222:6"
```

### Pattern

`^daemon_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:49c2c3903ed5fce68deca953a6e4c34c:search

```yaml
regex_id: 49c2c3903ed5fce68deca953a6e4c34c
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/policy-linter/src/policies/subscription-only-build.ts:49:2"
```

### Pattern

`^openai-api$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4a27d75f78c1ebd32fc4365802d1a8a8:search

```yaml
regex_id: 4a27d75f78c1ebd32fc4365802d1a8a8
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/librarian/src/source-readers.ts:221:6"
```

### Pattern

`^consolidation_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4b03db55229cf81d045e14d248c50468:search

```yaml
regex_id: 4b03db55229cf81d045e14d248c50468
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/librarian/src/source-readers.ts:227:6"
```

### Pattern

`^phase`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4c1e233f26aa4d9fbdcc951f95c09f60:search

```yaml
regex_id: 4c1e233f26aa4d9fbdcc951f95c09f60
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/policy-linter/src/policies/no-idle-research.ts:35:13"
```

### Pattern

`^#{1,6}\s*next\s+dispatch\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4cb266ac0c4921894414feb6005e4507:search

```yaml
regex_id: 4cb266ac0c4921894414feb6005e4507
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/ea-drift-sentinel/src/principle-rules.ts:73:22"
```

### Pattern

`^(llm|claude|gpt)\.`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4d67c3581a86c753d21645fe01e52575:search

```yaml
regex_id: 4d67c3581a86c753d21645fe01e52575
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/librarian/src/source-readers.ts:225:6"
```

### Pattern

`^mcp_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4f6bf54ce82bd838cd366294231be7f8:search

```yaml
regex_id: 4f6bf54ce82bd838cd366294231be7f8
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/ea-architect/src/repository-loader.ts:121:37"
```

### Pattern

`^(P\d+)\s*[—\-:]\s*(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:50856f3745adc2c4a7e1f316a969f966:search

```yaml
regex_id: 50856f3745adc2c4a7e1f316a969f966
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/scripts/reuse-check-strict.js:65:18"
```

### Pattern

`^packages\/persistence-[a-z0-9-]+\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:51c0ef91f45e78018f043aa5cc88147e:search

```yaml
regex_id: 51c0ef91f45e78018f043aa5cc88147e
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/ea-architect/src/repository-loader.ts:91:32"
```

### Pattern

`^#\s*ADR-\d+\s*[—\-:]\s*(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:599c6fcaf821d8f4f7fc1b08017cd9d0:search

```yaml
regex_id: 599c6fcaf821d8f4f7fc1b08017cd9d0
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/librarian/src/source-readers.ts:232:6"
```

### Pattern

`_directive\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5a7d6bf2b1a20d57b401c727131465a4:search

```yaml
regex_id: 5a7d6bf2b1a20d57b401c727131465a4
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/policy-linter/src/policies/subscription-only-build.ts:41:2"
```

### Pattern

`^COHERE_API_KEY$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5b98542b08bd649c58ea512d5b8aa909:search

```yaml
regex_id: 5b98542b08bd649c58ea512d5b8aa909
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/librarian/src/source-readers.ts:229:6"
```

### Pattern

`^caia_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5e576dc95fb0f4a724a24a421e239611:search

```yaml
regex_id: 5e576dc95fb0f4a724a24a421e239611
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/apps/orchestrator/src/http/health.ts:228:51"
```

### Pattern

`^\/blockers\/([^/]+)\/resolve$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5eb428a67f8719e836f27a97f4e95660:search

```yaml
regex_id: 5eb428a67f8719e836f27a97f4e95660
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/apps/orchestrator/src/http/health.ts:264:45"
```

### Pattern

`^\/questions\/([^/]+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:614a23aa4f88decfdd1644083c4de61f:search

```yaml
regex_id: 614a23aa4f88decfdd1644083c4de61f
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/local-llm-router/src/caveman-output.ts:78:2"
```

### Pattern

`\n+Hope (?:this|that) (?:helps|answers|clarifies)\b[^\n]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:64ea1188ee6de90e769ea81ec771b3ec:search

```yaml
regex_id: 64ea1188ee6de90e769ea81ec771b3ec
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/policy-linter/src/policies/no-idle-research.ts:59:2"
```

### Pattern

`^#{1,6}\s*status\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:667b888fb4288f809d23b5f03b0b6320:search

```yaml
regex_id: 667b888fb4288f809d23b5f03b0b6320
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/ea-architect/src/repository-loader.ts:184:24"
```

### Pattern

`^---\s*\nname:\s*([^\n]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:68369863338c9e7c42b82404789d2256:search

```yaml
regex_id: 68369863338c9e7c42b82404789d2256
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/scripts/reuse-check-strict.js:71:18"
```

### Pattern

`\.(test|spec)\.(ts|tsx|js|jsx)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:68e8da19ea5f771ff25bd327ccdb6704:search

```yaml
regex_id: 68e8da19ea5f771ff25bd327ccdb6704
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/local-llm-router/src/caveman-output.ts:65:2"
```

### Pattern

`^Here(?:'s| is| are)\b[^\n]{0,120}:\s*\n+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6b4d4afaae786a6b6c24db7fd52da1f5:search

```yaml
regex_id: 6b4d4afaae786a6b6c24db7fd52da1f5
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/policy-linter/src/policies/no-idle-research.ts:63:2"
```

### Pattern

`^#{1,6}\s*findings?\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6be41f8d82849d2aa2d18d7d696dc756:search

```yaml
regex_id: 6be41f8d82849d2aa2d18d7d696dc756
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/architecture-registry/src/extractors/drizzle-extractor.ts:279:30"
```

### Pattern

`^(\d{4})_(.+)\.sql$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6cf8bf5ed040ebbee11e6eb60057afdb:search

```yaml
regex_id: 6cf8bf5ed040ebbee11e6eb60057afdb
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/local-llm-router/src/caveman-output.ts:77:2"
```

### Pattern

`\n+Feel free to\b[^\n]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:704f73fb1d7517ea355636202bc3a33e:search

```yaml
regex_id: 704f73fb1d7517ea355636202bc3a33e
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/behavior-suite/scripts/scope-tests.ts:41:20"
```

### Pattern

`^src\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:74aae64c6030522b02029f63500ef2fc:search

```yaml
regex_id: 74aae64c6030522b02029f63500ef2fc
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/policy-linter/src/policies/subscription-only-build.ts:39:2"
```

### Pattern

`^GROQ_API_KEY$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7639e69c9e516bbdf2c4d672946fe99c:search

```yaml
regex_id: 7639e69c9e516bbdf2c4d672946fe99c
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/architecture-registry/src/extractors/component-extractor.ts:482:35"
```

### Pattern

`Page$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:77cc03793ba81574dbf202544ab95ac1:search

```yaml
regex_id: 77cc03793ba81574dbf202544ab95ac1
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/ea-architect/src/repository-loader.ts:159:30"
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

## usage_mismatch:792507e31ab03630d0c6f850a0da1245:search

```yaml
regex_id: 792507e31ab03630d0c6f850a0da1245
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/scripts/reuse-check.js:108:2"
```

### Pattern

`^\s*export\s+(?:const|let|var)\s+([A-Za-z_$][\w$]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7b0f1932c3f040b0bf476e360d71fcce:search

```yaml
regex_id: 7b0f1932c3f040b0bf476e360d71fcce
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/policy-linter/src/policies/subscription-only-build.ts:48:2"
```

### Pattern

`^anthropic-api$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7e22242026db278fe2447c8c56a7e9a2:search

```yaml
regex_id: 7e22242026db278fe2447c8c56a7e9a2
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/prompt-optimizer/src/stage3.ts:279:10"
```

### Pattern

`^\d`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7e620f6e83edaba23dcf4604359a1eaa:search

```yaml
regex_id: 7e620f6e83edaba23dcf4604359a1eaa
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/apps/orchestrator/scripts/check-observability.ts:20:26"
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

## usage_mismatch:7e6bb8b1bbff5da21db5cf796471add9:search

```yaml
regex_id: 7e6bb8b1bbff5da21db5cf796471add9
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/chain-runner/bin/consumption-probe.js:171:21"
```

### Pattern

`\.(ts|tsx|js|jsx|mjs|cjs|py)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7f43584a038f8da6869964374a28531a:search

```yaml
regex_id: 7f43584a038f8da6869964374a28531a
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/apps/orchestrator/src/http/health.ts:189:42"
```

### Pattern

`^\/requirements\/([^/]+)\/notes$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:80fdaee49d029dea3801e9d168ef4f7c:search

```yaml
regex_id: 80fdaee49d029dea3801e9d168ef4f7c
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/apps/orchestrator/src/requirements/migrate.ts:117:52"
```

### Pattern

`\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8243a2bbb946062ac80fecb9e10e59d5:search

```yaml
regex_id: 8243a2bbb946062ac80fecb9e10e59d5
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/librarian/src/source-readers.ts:214:6"
```

### Pattern

`_architecture\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:864d399b92922c42d7aee4828d83f762:search

```yaml
regex_id: 864d399b92922c42d7aee4828d83f762
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/local-llm-router/src/caveman-output.ts:70:2"
```

### Pattern

`^Absolutely[!.,]?\s+[^\n]{0,120}\n+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8a5c995178f71ff3197f467a13f6d196:search

```yaml
regex_id: 8a5c995178f71ff3197f467a13f6d196
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/scripts/reuse-check.js:104:2"
```

### Pattern

`^\s*export\s+(?:default\s+)?(?:async\s+)?function\s+([A-Za-z_$][\w$]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9042c7a4d3cc38a6ff568d439f6bc6c7:search

```yaml
regex_id: 9042c7a4d3cc38a6ff568d439f6bc6c7
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/local-llm-router/src/caveman-output.ts:66:2"
```

### Pattern

`^Sure[!.,]\s+[^\n]{0,120}\n+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:932b17613761ad55d0a0490a2fb24148:search

```yaml
regex_id: 932b17613761ad55d0a0490a2fb24148
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/apps/orchestrator/src/http/health.ts:238:50"
```

### Pattern

`^\/blockers\/([^/]+)\/cancel$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:93ddf18679325bc6674282cf2cb9cff2:search

```yaml
regex_id: 93ddf18679325bc6674282cf2cb9cff2
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/scripts/reuse-check.js:112:2"
```

### Pattern

`^\s*export\s+type\s+([A-Za-z_$][\w$]*)\s*=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:95b3a466ae9debfd8c090fb5e44e042e:search

```yaml
regex_id: 95b3a466ae9debfd8c090fb5e44e042e
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/apps/orchestrator/src/requirements/migrate.ts:27:30"
```

### Pattern

`^---\n([\s\S]*?)\n---`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9633ebd6bc50e1eb93aa99935313314d:search

```yaml
regex_id: 9633ebd6bc50e1eb93aa99935313314d
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/policy-linter/src/policies/subscription-only-build.ts:37:2"
```

### Pattern

`^ANTHROPIC_API_KEY$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9738a2a9776f63eecea1851f9a4a8f3c:search

```yaml
regex_id: 9738a2a9776f63eecea1851f9a4a8f3c
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/reviewer/src/detectors/shared.ts:73:7"
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

## usage_mismatch:9956c22b43e2731aa46bdfdbafcb0453:search

```yaml
regex_id: 9956c22b43e2731aa46bdfdbafcb0453
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/policy-linter/src/policies/no-calendar-time-estimates.ts:110:6"
```

### Pattern

`^#{0,6}\s*\d{4}-\d{2}-\d{2}(?:T\d{2}:\d{2}(?::\d{2})?(?:Z|[+-]\d{2}:?\d{2})?)?\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9cb25e7c9061c358cccf1943b7e8a7ef:search

```yaml
regex_id: 9cb25e7c9061c358cccf1943b7e8a7ef
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/image-provider/scripts/check-uniqueness.ts:104:6"
```

### Pattern

`^[a-z0-9-]{5,}-[a-z0-9]{4}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9edd7e4006e669535264c23dd6714e76:search

```yaml
regex_id: 9edd7e4006e669535264c23dd6714e76
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/ea-architect/src/repository-loader.ts:34:24"
```

### Pattern

`^ADR-(\d+)-(.+)\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9f163dc313dad755f89e7692835fe2da:search

```yaml
regex_id: 9f163dc313dad755f89e7692835fe2da
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/ea-drift-sentinel/src/principle-rules.ts:48:22"
```

### Pattern

`\.(approved|rejected|completed|failed)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a02645c69c83a4fcfd4f044fcf370808:search

```yaml
regex_id: a02645c69c83a4fcfd4f044fcf370808
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/local-llm-router/src/caveman-output.ts:71:2"
```

### Pattern

`^I'?ll (?:help|walk|show|explain|go through)\b[^\n]{0,120}\n+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a0c10921c22f1a1b8b9edbbab2c9ebdb:search

```yaml
regex_id: a0c10921c22f1a1b8b9edbbab2c9ebdb
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/image-provider/scripts/check-uniqueness.ts:109:6"
```

### Pattern

`^[0-9a-f-]{32,}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a2e7e419a4bd7c410e99e9df620b2fc9:search

```yaml
regex_id: a2e7e419a4bd7c410e99e9df620b2fc9
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/scripts/reuse-check.js:123:2"
```

### Pattern

`^\s*(?:export\s+(?:default\s+|abstract\s+)?)?class\s+([A-Za-z_$][\w$]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a3ace6b8c5cb8bdcedfa8fe5d6ffafa5:search

```yaml
regex_id: a3ace6b8c5cb8bdcedfa8fe5d6ffafa5
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/ea-drift-sentinel/src/principle-rules.ts:62:22"
```

### Pattern

`^(deploy|prod|release)\.`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:abb169ab96cb2eadb7f017560f1599e7:search

```yaml
regex_id: abb169ab96cb2eadb7f017560f1599e7
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/chain-runner/src/doctor.ts:430:35"
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

## usage_mismatch:abef570f207552aabf508561964025b5:search

```yaml
regex_id: abef570f207552aabf508561964025b5
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/policy-linter/src/policies/ea-agent-gate.ts:44:2"
```

### Pattern

`^caia-ea\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b2745b79fa8ea44b4ba9efaefd12418f:search

```yaml
regex_id: b2745b79fa8ea44b4ba9efaefd12418f
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/librarian/src/source-readers.ts:228:6"
```

### Pattern

`^backlog_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b720acae76191ebddfb2dca5f3724133:search

```yaml
regex_id: b720acae76191ebddfb2dca5f3724133
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/librarian/src/source-readers.ts:213:6"
```

### Pattern

`_registry(_directive)?\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ba4360119e5c0a875c8e547c3205365d:search

```yaml
regex_id: ba4360119e5c0a875c8e547c3205365d
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/apps/orchestrator/src/http/health.ts:178:42"
```

### Pattern

`^\/requirements\/([^/]+)\/state$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bcc542da3d3ac0fac54004ef8630ed4f:search

```yaml
regex_id: bcc542da3d3ac0fac54004ef8630ed4f
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/ea-architect/src/repository-loader.ts:138:32"
```

### Pattern

`^#\s+(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bdf582f7c677fd5622852c09ad0a740a:search

```yaml
regex_id: bdf582f7c677fd5622852c09ad0a740a
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/policy-linter/src/policies/no-idle-research.ts:62:2"
```

### Pattern

`^#{1,6}\s*summary\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c1ddda69791d60e1a26900f7572cf333:search

```yaml
regex_id: c1ddda69791d60e1a26900f7572cf333
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/policy-linter/src/policies/subscription-only-build.ts:51:2"
```

### Pattern

`-billable$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c46131e0d993a939953c607ba6256a60:search

```yaml
regex_id: c46131e0d993a939953c607ba6256a60
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/apps/orchestrator/scripts/check-observability.ts:44:23"
```

### Pattern

`^export\s+(?:async\s+)?function\s+(\w+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c60ba77771ef9f136c627bf92aeda0a0:search

```yaml
regex_id: c60ba77771ef9f136c627bf92aeda0a0
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/critic/src/detectors/decision-classifier.ts:26:29"
```

### Pattern

`\.(md|mdx|markdown|txt)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ca6ecd5f7f3dab1b0f8d569409b8faf2:search

```yaml
regex_id: ca6ecd5f7f3dab1b0f8d569409b8faf2
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/scripts/reuse-check.js:122:2"
```

### Pattern

`^\s*(?:export\s+(?:default\s+)?)?(?:async\s+)?function\s+([A-Za-z_$][\w$]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ce19b4159d8a5eaa015d88c62fe213eb:search

```yaml
regex_id: ce19b4159d8a5eaa015d88c62fe213eb
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/librarian/src/source-readers.ts:226:6"
```

### Pattern

`^safety_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d38dd07e6dcef678e0ce26c759124cfd:search

```yaml
regex_id: d38dd07e6dcef678e0ce26c759124cfd
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/apps/orchestrator/src/http/health.ts:157:40"
```

### Pattern

`^\/requirements\/([^/]+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d56391403ab6dc9c6fa0254a320b997a:search

```yaml
regex_id: d56391403ab6dc9c6fa0254a320b997a
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/local-llm-router/src/caveman-output.ts:69:2"
```

### Pattern

`^Great question[!.,]?\s+[^\n]{0,120}\n+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d97281a5afa5739f2ea8fb5a9e765626:search

```yaml
regex_id: d97281a5afa5739f2ea8fb5a9e765626
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/scripts/reuse-check.js:106:2"
```

### Pattern

`^\s*export\s+(?:default\s+|abstract\s+)?class\s+([A-Za-z_$][\w$]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:da9604b03ed76f958370861e2beca58b:search

```yaml
regex_id: da9604b03ed76f958370861e2beca58b
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/policy-linter/src/policies/no-idle-research.ts:58:2"
```

### Pattern

`^#{1,6}\s*results?\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dab90d628cdb6c1f1e98b2b53c50a921:search

```yaml
regex_id: dab90d628cdb6c1f1e98b2b53c50a921
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/local-llm-router/src/caveman-output.ts:81:2"
```

### Pattern

`\n+Is there anything else\b[^\n]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:daea07446ff9d8aa895ee84348ee2d55:search

```yaml
regex_id: daea07446ff9d8aa895ee84348ee2d55
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/business-proposal-generator/src/proposal/word-count.ts:47:52"
```

### Pattern

`^##\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:db29b2ed9ec728fa6f5004b885fa2ddd:search

```yaml
regex_id: db29b2ed9ec728fa6f5004b885fa2ddd
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/analytics-architect/src/invariants.ts:83:2"
```

### Pattern

`^ip$|ipv4|ipv6|ip_addr`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dfb5fd6f4efb790d9b859aa2054784a0:search

```yaml
regex_id: dfb5fd6f4efb790d9b859aa2054784a0
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/scripts/reuse-check.js:126:2"
```

### Pattern

`^\s*(?:export\s+)?type\s+([A-Za-z_$][\w$]*)\s*=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e09732b26a78dc23f46484e2e26a16eb:search

```yaml
regex_id: e09732b26a78dc23f46484e2e26a16eb
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/librarian/src/source-readers.ts:220:6"
```

### Pattern

`^gate_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e22b1cde1e31eeb16333b9b2228043ee:search

```yaml
regex_id: e22b1cde1e31eeb16333b9b2228043ee
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/policy-linter/src/policies/subscription-only-build.ts:40:2"
```

### Pattern

`^MISTRAL_API_KEY$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e36e8306891266de79f93cbbb8b2ca46:search

```yaml
regex_id: e36e8306891266de79f93cbbb8b2ca46
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/librarian/src/source-readers.ts:219:6"
```

### Pattern

`^master_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e3f970ba4799526536965b9ba46d766a:search

```yaml
regex_id: e3f970ba4799526536965b9ba46d766a
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/scripts/reuse-check.js:265:6"
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

## usage_mismatch:e7250d5aa4871500744b1e8c482ae125:search

```yaml
regex_id: e7250d5aa4871500744b1e8c482ae125
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/reviewer/src/detectors/shared.ts:83:7"
```

### Pattern

`^(?:packages|apps)\/[^/]+\/src\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e7a2403ef1e77046f0231e15e1217ba6:search

```yaml
regex_id: e7a2403ef1e77046f0231e15e1217ba6
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/reviewer/src/detectors/shared.ts:78:9"
```

### Pattern

`\.(md|mdx|markdown)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e7a359c7dcad4c0a8250190f9e153bd2:search

```yaml
regex_id: e7a359c7dcad4c0a8250190f9e153bd2
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/policy-linter/src/policies/subscription-only-build.ts:50:2"
```

### Pattern

`^paid-api`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e912b2bc5800c92c95c997c577dea017:search

```yaml
regex_id: e912b2bc5800c92c95c997c577dea017
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/business-proposal-generator/src/proposal/word-count.ts:47:64"
```

### Pattern

`^###\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ea25a309359bd596cc023b240bfa300b:search

```yaml
regex_id: ea25a309359bd596cc023b240bfa300b
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/apps/orchestrator/src/requirements/migrate.ts:117:25"
```

### Pattern

`^BL-.*\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ea4edbb238cbb29c2ac0a5bb045a7ca2:search

```yaml
regex_id: ea4edbb238cbb29c2ac0a5bb045a7ca2
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/scripts/reuse-check.js:110:2"
```

### Pattern

`^\s*export\s+interface\s+([A-Za-z_$][\w$]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:eba7e48434c6b02837fdd21f19b745fb:search

```yaml
regex_id: eba7e48434c6b02837fdd21f19b745fb
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/ea-architect/src/repository-loader.ts:71:25"
```

### Pattern

`^-\s+(?:\*\*)?([A-Za-z][A-Za-z0-9 -]*?)(?:\*\*)?:\s*(.+?)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ed05db208e770ba5185962bb1570603d:search

```yaml
regex_id: ed05db208e770ba5185962bb1570603d
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/scripts/reuse-check.js:125:2"
```

### Pattern

`^\s*(?:export\s+)?interface\s+([A-Za-z_$][\w$]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ed67ed3c774fd001901c76e9b248f707:search

```yaml
regex_id: ed67ed3c774fd001901c76e9b248f707
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/librarian/src/source-readers.ts:216:37"
```

### Pattern

`^enterprise_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f10a96bf2bbf8722691bb46859d6c4ba:search

```yaml
regex_id: f10a96bf2bbf8722691bb46859d6c4ba
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/scripts/reuse-check.js:124:2"
```

### Pattern

`^\s*(?:export\s+)?(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f205997582c0a31c005019ab8c8459df:search

```yaml
regex_id: f205997582c0a31c005019ab8c8459df
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/apps/orchestrator/src/http/health.ts:275:51"
```

### Pattern

`^\/questions\/([^/]+)\/answer$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f73a2136baa5196647baa2c10ac2d3e4:search

```yaml
regex_id: f73a2136baa5196647baa2c10ac2d3e4
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/chain-runner/bin/consumption-probe.js:173:26"
```

### Pattern

`(^|\/)pnpm-workspace\.yaml$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f8042389d47bb8aaeb5376898221401c:search

```yaml
regex_id: f8042389d47bb8aaeb5376898221401c
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/local-llm-router/src/caveman-output.ts:68:2"
```

### Pattern

`^Of course[!.,]?\s+[^\n]{0,120}\n+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f8bf9b5562f0ce2685b148c9f60e3e53:search

```yaml
regex_id: f8bf9b5562f0ce2685b148c9f60e3e53
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/apps/orchestrator/src/http/health.ts:217:44"
```

### Pattern

`^\/blockers\/([^/]+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f91df7cb41129a7d0d9b4515507fe1a7:search

```yaml
regex_id: f91df7cb41129a7d0d9b4515507fe1a7
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/apps/orchestrator/src/http/health.ts:285:51"
```

### Pattern

`^\/questions\/([^/]+)\/cancel$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fbbc7f4ff5121fda96a543ed2d99ad9b:search

```yaml
regex_id: fbbc7f4ff5121fda96a543ed2d99ad9b
schema_version: "1"
kind: usage_mismatch
corpus: caia
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/caia/rules/packages/librarian/src/source-readers.ts:215:6"
```

### Pattern

`^architecture`

### Context

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
corpus: caia
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
corpus: caia
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
corpus: caia
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
corpus: caia
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

---
schema_version: "1"
corpus: sonash-v0
findings: 481
---

# sonash-v0 batch findings

## usage_mismatch:02b9b356c9428c9cbd899e7625b1c6ba:search

```yaml
regex_id: 02b9b356c9428c9cbd899e7625b1c6ba
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/security-check.js:117:14"
```

### Pattern

`storage\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0333829d45592a8609f1a0bdd9fb5a4a:search

```yaml
regex_id: 0333829d45592a8609f1a0bdd9fb5a4a
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:387:17"
```

### Pattern

`(?:^|[\\/])ci\.yml$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:03ea7570642993698e39d3f66c1c26e6:search

```yaml
regex_id: 03ea7570642993698e39d3f66c1c26e6
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:271:4"
```

### Pattern

`^recommended\s+(next\s+)?steps`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0400587d839b8c4c0a043939f4ef73dd:search

```yaml
regex_id: 0400587d839b8c4c0a043939f4ef73dd
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:1421:17"
```

### Pattern

`(?:^|[\\/])check-pattern-compliance\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:04389d4c13b9502e07a5d3c38adaa404:search

```yaml
regex_id: 04389d4c13b9502e07a5d3c38adaa404
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/security-check.js:51:6"
```

### Pattern

`(?:^|[\\/])check-pattern-compliance\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:04b18925bbf204c2a210286909375a2c:search

```yaml
regex_id: 04b18925bbf204c2a210286909375a2c
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:288:4"
```

### Pattern

`^\d+\.\d+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0500c411792d20f1bba6083edf8fcfa2:search

```yaml
regex_id: 0500c411792d20f1bba6083edf8fcfa2
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:195:2"
```

### Pattern

`^scripts\/migrate-.*\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:05082057ae2b17028bb212d3a2a80db1:search

```yaml
regex_id: 05082057ae2b17028bb212d3a2a80db1
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/analyze-learning-effectiveness.js:342:21"
```

### Pattern

`^## `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:06460f8aa61a312ec4e7ddce61da7beb:search

```yaml
regex_id: 06460f8aa61a312ec4e7ddce61da7beb
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:181:2"
```

### Pattern

`^scripts\/ai-review\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:06711b8b97e24eae015eb3c9dab9138e:search

```yaml
regex_id: 06711b8b97e24eae015eb3c9dab9138e
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-propagation.js:297:2"
```

### Pattern

`^\+\s+([a-zA-Z_$][a-zA-Z0-9_$]*)\s*\([^)]*\)\s*\{`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:06c87f5330789d59b34a4477fa3e93ea:search

```yaml
regex_id: 06c87f5330789d59b34a4477fa3e93ea
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/multi-ai/normalize-format.js:210:41"
```

### Pattern

`^\d+\.\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:06dcecd796f1821117c2ea39de388074:search

```yaml
regex_id: 06dcecd796f1821117c2ea39de388074
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-triggers.js:178:4"
```

### Pattern

`^\.claude\/commands\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:070c865fff73b19f5966ee706210f624:search

```yaml
regex_id: 070c865fff73b19f5966ee706210f624
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/docs/generate-llms-txt.js:91:31"
```

### Pattern

`^\s+\S`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:079e162878f6d58aae6a6525017de7d8:search

```yaml
regex_id: 079e162878f6d58aae6a6525017de7d8
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:256:4"
```

### Pattern

`^(decision|change)\s+log`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:07f17e2f385e880a14bd9a39e352bc80:search

```yaml
regex_id: 07f17e2f385e880a14bd9a39e352bc80
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:101:6"
```

### Pattern

`^package\.json$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0802f3c4a1a8f8fb5150b7443eace8d9:search

```yaml
regex_id: 0802f3c4a1a8f8fb5150b7443eace8d9
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-triggers.js:189:4"
```

### Pattern

`\.jsonl$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:089f5ca662c31e56968eea4fa322b38d:search

```yaml
regex_id: 089f5ca662c31e56968eea4fa322b38d
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:252:4"
```

### Pattern

`^step\s+\d+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:08aa929ce75f9435e96f809428ffa529:search

```yaml
regex_id: 08aa929ce75f9435e96f809428ffa529
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:1054:17"
```

### Pattern

`(?:^|[\\/])check-pattern-compliance\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:08fbed5dbcfda185126c954aab97eba2:search

```yaml
regex_id: 08fbed5dbcfda185126c954aab97eba2
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:87:6"
```

### Pattern

`^lib\/rate-limiter\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:098d326ddd56b93b3df843442ce4afc4:search

```yaml
regex_id: 098d326ddd56b93b3df843442ce4afc4
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/pr-ecosystem-audit/scripts/checkers/pattern-lifecycle.js:98:44"
```

### Pattern

`^##+ .+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:09986d49d89fee96d79a177803e3a27f:search

```yaml
regex_id: 09986d49d89fee96d79a177803e3a27f
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/archive/sync-reviews-to-jsonl.js:657:47"
```

### Pattern

`^- \*\*([^*]+)\*\*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0ad05f613454140bcf19caf310a6e1a9:search

```yaml
regex_id: 0ad05f613454140bcf19caf310a6e1a9
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/doc-ecosystem-audit/scripts/checkers/content-quality.js:92:29"
```

### Pattern

`^\s*---\s*\n[\s\S]*?\n---\s*(?:\n|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0ad17f5bfcaee7dddc8120080f1b9d05:search

```yaml
regex_id: 0ad17f5bfcaee7dddc8120080f1b9d05
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/aggregate-audit-findings.js:287:41"
```

### Pattern

`^### S(\d) `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0ba090822527438e4a937970d9cee24c:search

```yaml
regex_id: 0ba090822527438e4a937970d9cee24c
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/aggregate-audit-findings.js:286:19"
```

### Pattern

`^### S(\d) `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0ba392d94629c71cd1c1e8e209c8f505:search

```yaml
regex_id: 0ba392d94629c71cd1c1e8e209c8f505
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/hook-ecosystem-audit/scripts/checkers/cicd-pipeline.js:126:29"
```

### Pattern

`^\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0bc13dfe2d232343ade031087947c422:search

```yaml
regex_id: 0bc13dfe2d232343ade031087947c422
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-cc.js:496:14"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0cb0201020a45fcdeca58f43498516fe:search

```yaml
regex_id: 0cb0201020a45fcdeca58f43498516fe
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-doc-placement.js:63:6"
```

### Pattern

`^AI_WORKFLOW\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0d0cb41ebf419223476a9e72ef534c8c:search

```yaml
regex_id: 0d0cb41ebf419223476a9e72ef534c8c
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-roadmap-debt.js:240:40"
```

### Pattern

`^[-*+]\s*\[([ xX])\]\s+(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0d7a9797763c333c966459fdcbe7b8af:search

```yaml
regex_id: 0d7a9797763c333c966459fdcbe7b8af
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/doc-ecosystem-audit/scripts/checkers/content-quality.js:403:10"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0d8d88f1982beaca8d18f436fd6f7172:search

```yaml
regex_id: 0d8d88f1982beaca8d18f436fd6f7172
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:1797:17"
```

### Pattern

`(?:^|[\\/])check-pattern-compliance\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0dc01ad72b43b7739c6d6eb625a4c9e5:search

```yaml
regex_id: 0dc01ad72b43b7739c6d6eb625a4c9e5
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/hook-ecosystem-audit/scripts/checkers/cicd-pipeline.js:129:40"
```

### Pattern

`^run:\s+(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0f1240894f5b65a597ba6493e38d86e4:search

```yaml
regex_id: 0f1240894f5b65a597ba6493e38d86e4
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:684:4"
```

### Pattern

`^app\/admin\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1021a8e5b0624462986c2d7994751f41:search

```yaml
regex_id: 1021a8e5b0624462986c2d7994751f41
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/archive-doc.js:109:8"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:10d6c66d1f5fa478014f3b00a5c964c4:search

```yaml
regex_id: 10d6c66d1f5fa478014f3b00a5c964c4
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/hook-ecosystem-audit/scripts/checkers/cicd-pipeline.js:530:48"
```

### Pattern

`^\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:10d9cb480339edc54d68ffb6571ec4c6:search

```yaml
regex_id: 10d9cb480339edc54d68ffb6571ec4c6
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:250:4"
```

### Pattern

`^glossary`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:10f836a526499a0d2d9f66d56ad96187:search

```yaml
regex_id: 10f836a526499a0d2d9f66d56ad96187
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:254:4"
```

### Pattern

`^(success|quality|quantitative|qualitative)\s+metrics`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1100535bb909b1492aeca45125d303f9:search

```yaml
regex_id: 1100535bb909b1492aeca45125d303f9
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-triggers.js:177:4"
```

### Pattern

`^docs\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1104fabd383ce569c162e201dd9898e9:search

```yaml
regex_id: 1104fabd383ce569c162e201dd9898e9
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/review-lifecycle.js:274:69"
```

### Pattern

`^\s*##+\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:113aac8b97bf35a1d59df678663a771b:search

```yaml
regex_id: 113aac8b97bf35a1d59df678663a771b
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:192:2"
```

### Pattern

`^scripts\/update-readme-status\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:11bc79917789269194ea316a6449055a:search

```yaml
regex_id: 11bc79917789269194ea316a6449055a
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:219:6"
```

### Pattern

`^\s*✅\s*(completed|resolved|done|fixed)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:12ac220310d04d5d98bcc8b9dbcf4a83:search

```yaml
regex_id: 12ac220310d04d5d98bcc8b9dbcf4a83
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/review-lifecycle.js:308:69"
```

### Pattern

`^\s*##+\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:137fb99d7ad8efd865a523b09f7e7657:search

```yaml
regex_id: 137fb99d7ad8efd865a523b09f7e7657
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:64:6"
```

### Pattern

`\.stories\.tsx$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:13daf0e864f80aa7d3fd4a072930a8eb:search

```yaml
regex_id: 13daf0e864f80aa7d3fd4a072930a8eb
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/generate-test-registry.js:427:9"
```

### Pattern

`\.(?:(?:property|integration|e2e|contract|perf)\.)?test\.(?:js|ts|mjs)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:14a55b369d3da6d9dcd55131b3890e62:search

```yaml
regex_id: 14a55b369d3da6d9dcd55131b3890e62
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:1938:17"
```

### Pattern

`(?:^|[\\/])(?:check-pattern-compliance|parse-jsonl-line)\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:14dd4c2822f41b49fedd407561517b7d:search

```yaml
regex_id: 14dd4c2822f41b49fedd407561517b7d
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/archive-doc.js:605:24"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:154ec80a1dee52670d429e6d36fd819d:search

```yaml
regex_id: 154ec80a1dee52670d429e6d36fd819d
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/multi-ai/normalize-format.js:581:43"
```

### Pattern

`^\[([^\]]+)\]\s*(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:160faa2ad5a1c6eba39796ee5f4237a8:search

```yaml
regex_id: 160faa2ad5a1c6eba39796ee5f4237a8
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:191:2"
```

### Pattern

`^scripts\/mcp\/sonarcloud-server\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:17fe104ff01d96f18bac0346b683d657:search

```yaml
regex_id: 17fe104ff01d96f18bac0346b683d657
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:179:2"
```

### Pattern

`^docs\/archive\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:18d525dee80f499c2d67b09a1c4bb047:search

```yaml
regex_id: 18d525dee80f499c2d67b09a1c4bb047
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:1605:17"
```

### Pattern

`(?:^|[\\/])(?:check-pattern-compliance|eslint-plugin-sonash\.test)\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:194eefcbb6de9215b5d13389bb0b3cba:search

```yaml
regex_id: 194eefcbb6de9215b5d13389bb0b3cba
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/user-prompt-handler.js:648:4"
```

### Pattern

`^(?:ok|okay|yes|yeah|yep|no|nope|thanks?|thx|ty|sure|go|lgtm|ack)\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1956b6e9ee1406025a3b00309f2a76b6:search

```yaml
regex_id: 1956b6e9ee1406025a3b00309f2a76b6
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/hook-ecosystem-audit/scripts/checkers/cicd-pipeline.js:535:34"
```

### Pattern

`^\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:19911ef5b8f2577c9c9e860438ba4cae:search

```yaml
regex_id: 19911ef5b8f2577c9c9e860438ba4cae
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:531:7"
```

### Pattern

`^(?:app|components)\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:19b65cbe98e71c836b7f2aa6cc5e5cd1:search

```yaml
regex_id: 19b65cbe98e71c836b7f2aa6cc5e5cd1
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:227:6"
```

### Pattern

`✅\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:19f9a2cc1eabf7ece4765d07d26bbbac:search

```yaml
regex_id: 19f9a2cc1eabf7ece4765d07d26bbbac
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:297:6"
```

### Pattern

`^[A-Z][a-zA-Z.\s]+ \d+\.\d+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1b47502ea2c1624d0046f1ab8d8c170d:search

```yaml
regex_id: 1b47502ea2c1624d0046f1ab8d8c170d
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:968:17"
```

### Pattern

`(?:^|[\\/])(?:check-pattern-compliance|parse-jsonl-line)\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1b5c2c9438ab42c46268945e3660b4a4:search

```yaml
regex_id: 1b5c2c9438ab42c46268945e3660b4a4
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-context-debt.js:114:33"
```

### Pattern

`^[-*]?\s*(?:\*\*)?Gap(?:\*\*)?:\s*(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1b81d7bba5cc22b368b310eb848a6f46:search

```yaml
regex_id: 1b81d7bba5cc22b368b310eb848a6f46
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/doc-ecosystem-audit/scripts/checkers/link-reference-integrity.js:339:10"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1c2e70952d2c3b6358624e0e64352523:search

```yaml
regex_id: 1c2e70952d2c3b6358624e0e64352523
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/script-ecosystem-audit/scripts/checkers/registration-reachability.js:247:12"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1caf8926f6b8937e74e384539b1948f0:search

```yaml
regex_id: 1caf8926f6b8937e74e384539b1948f0
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:63:6"
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

## usage_mismatch:1d4d04c5426a593104b7a714cd5a53e6:search

```yaml
regex_id: 1d4d04c5426a593104b7a714cd5a53e6
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/aggregate-audit-findings.js:521:37"
```

### Pattern

`^(.+):(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1e39ad9154670ad6537fef2bd2911b25:search

```yaml
regex_id: 1e39ad9154670ad6537fef2bd2911b25
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/script-ecosystem-audit/scripts/checkers/module-consistency.js:104:11"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1e507d5b816e3714f23093d5d928eef1:search

```yaml
regex_id: 1e507d5b816e3714f23093d5d928eef1
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/review-lifecycle.js:302:6"
```

### Pattern

`^\s*\*\*(Takeaway|Lesson|Learnings):\*\*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1e7209b9058bea8675ecfa025721ecc1:search

```yaml
regex_id: 1e7209b9058bea8675ecfa025721ecc1
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-docs-light.js:285:4"
```

### Pattern

`^\.\.\.$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1f7b5c720b4e6cce5eb5209fd7b45061:search

```yaml
regex_id: 1f7b5c720b4e6cce5eb5209fd7b45061
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:258:4"
```

### Pattern

`^(implementation|execution|remediation)\s+(timeline|strategy|plan|order)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1f8bac0b16ac8164901af6f56e041bf0:search

```yaml
regex_id: 1f8bac0b16ac8164901af6f56e041bf0
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/multi-ai/normalize-format.js:564:38"
```

### Pattern

`^#{2,4}\s+(.+?)(?:\n|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1f9b13d04a95c707a86d6e3f7286d972:search

```yaml
regex_id: 1f9b13d04a95c707a86d6e3f7286d972
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/script-ecosystem-audit/scripts/checkers/registration-reachability.js:137:11"
```

### Pattern

`^\.\.(?:\/|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2026692ca4be30964fd7079188274b32:search

```yaml
regex_id: 2026692ca4be30964fd7079188274b32
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:76:6"
```

### Pattern

`^hooks\/.*\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2027121454015fd81cc2f271ba703bbf:search

```yaml
regex_id: 2027121454015fd81cc2f271ba703bbf
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/docs/generate-llms-txt.js:160:16"
```

### Pattern

`^["']|["']$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2067b07573f70f71a1599c584846514c:search

```yaml
regex_id: 2067b07573f70f71a1599c584846514c
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:1399:38"
```

### Pattern

`^\^?\(?[\w:\-|./]+\)?\$?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:20ce6db91a95643b6d6a1027d841b559:search

```yaml
regex_id: 20ce6db91a95643b6d6a1027d841b559
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:207:4"
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

## usage_mismatch:2143011bed3aedf1f80fc64637c355ac:search

```yaml
regex_id: 2143011bed3aedf1f80fc64637c355ac
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:1443:17"
```

### Pattern

`(?:^|[\\/])check-pattern-compliance\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2202aee96052456f0a12091f54624c26:search

```yaml
regex_id: 2202aee96052456f0a12091f54624c26
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:623:8"
```

### Pattern

`^#{1,4}\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:223de12604ab5ba0fdf432ecb792d4c9:search

```yaml
regex_id: 223de12604ab5ba0fdf432ecb792d4c9
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/review-lifecycle.js:198:17"
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

## usage_mismatch:22a35cb65cf75ea3f4db23499db10e29:search

```yaml
regex_id: 22a35cb65cf75ea3f4db23499db10e29
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/docs/generate-llms-txt.js:41:8"
```

### Pattern

`^##\s+Purpose\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:22ab988776d4f84cb6e0034dc55cadec:search

```yaml
regex_id: 22ab988776d4f84cb6e0034dc55cadec
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-doc-placement.js:62:6"
```

### Pattern

`^DOCUMENTATION_STANDARDS\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:22fd659690b02d62410a9e3047b44418:search

```yaml
regex_id: 22fd659690b02d62410a9e3047b44418
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/multi-ai/normalize-format.js:479:10"
```

### Pattern

`^\|[-: |]{1,500}\|?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2311f1d3be720d60629729e72bae68b1:search

```yaml
regex_id: 2311f1d3be720d60629729e72bae68b1
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/reviews/lib/promote-patterns.ts:22:6"
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

## usage_mismatch:233410f521e94336ecaccee7f82092ec:search

```yaml
regex_id: 233410f521e94336ecaccee7f82092ec
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/user-prompt-handler.js:455:4"
```

### Pattern

`^nothing\s+(?:else|more)\s*[.!]?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:23fb85385fe0168711f2a5b66dbe718d:search

```yaml
regex_id: 23fb85385fe0168711f2a5b66dbe718d
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/aggregate-audit-findings.js:415:36"
```

### Pattern

`^####\s+(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:24a7350da38dc14988087c89c3e1802c:search

```yaml
regex_id: 24a7350da38dc14988087c89c3e1802c
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:184:2"
```

### Pattern

`^scripts\/check-document-sync\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:24d469ec67c86af387bef195dad44ad2:search

```yaml
regex_id: 24d469ec67c86af387bef195dad44ad2
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:286:4"
```

### Pattern

`^parallel\s+execution`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:25fac8e7ca00514e17015080f0f447af:search

```yaml
regex_id: 25fac8e7ca00514e17015080f0f447af
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-content-accuracy.js:261:4"
```

### Pattern

`^\s*-\s*\[ \]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2613347590b78d8f5e3f1d346d402186:search

```yaml
regex_id: 2613347590b78d8f5e3f1d346d402186
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-triggers.js:180:4"
```

### Pattern

`^\.claude\/hooks\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:265cbf439283eea7a53eae56b9d394de:search

```yaml
regex_id: 265cbf439283eea7a53eae56b9d394de
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:1230:17"
```

### Pattern

`(?:^|[\\/])check-pattern-compliance\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:265fe21388b4c1b3a5b80a851167665c:search

```yaml
regex_id: 265fe21388b4c1b3a5b80a851167665c
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:1978:12"
```

### Pattern

`^\w+,?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:26bb3206b82d56977d01db05e95715d0:search

```yaml
regex_id: 26bb3206b82d56977d01db05e95715d0
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:185:2"
```

### Pattern

`^scripts\/check-review-needed\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:272f5ae9ba55b7e83e3c969a2ea03354:search

```yaml
regex_id: 272f5ae9ba55b7e83e3c969a2ea03354
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/archive-doc.js:522:42"
```

### Pattern

`^# .+\n`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2748d047824e249a61b5e281ddf3cc54:search

```yaml
regex_id: 2748d047824e249a61b5e281ddf3cc54
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/user-prompt-handler.js:666:4"
```

### Pattern

`^\s*wait\b(?!\s+(?:for|until|on))`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:275d2ed0c8566b0a9cbd649808dcd7d6:search

```yaml
regex_id: 275d2ed0c8566b0a9cbd649808dcd7d6
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:100:6"
```

### Pattern

`^\.firebaserc$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:285f85f7028527106c74bf5a5227efd5:search

```yaml
regex_id: 285f85f7028527106c74bf5a5227efd5
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:277:6"
```

### Pattern

`^(?:app\/admin|functions)\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2881af485ac53120669242804bb398ae:search

```yaml
regex_id: 2881af485ac53120669242804bb398ae
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-roadmap-debt.js:405:27"
```

### Pattern

`^INTAKE-ROAD-(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:28cdafad927a0fa1be31f8f98e720ae7:search

```yaml
regex_id: 28cdafad927a0fa1be31f8f98e720ae7
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-propagation.js:304:2"
```

### Pattern

`^-.*\b(?:const|let|var)\s+([a-zA-Z_$][a-zA-Z0-9_$]*)\s*=\s*(?:function|\(|async\s)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:28d3fca9da9aedc6d82b2be261802b27:search

```yaml
regex_id: 28d3fca9da9aedc6d82b2be261802b27
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-content-accuracy.js:249:4"
```

### Pattern

`^node\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:28e94717b80fcdb75bb6e1bc860769f8:search

```yaml
regex_id: 28e94717b80fcdb75bb6e1bc860769f8
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-propagation.js:299:2"
```

### Pattern

`^\+.*\bexport\s+(?:default\s+)?function\s+([a-zA-Z_$][a-zA-Z0-9_$]*)\s*\(`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2913dc5a581c4c82b085683bbb0550cf:search

```yaml
regex_id: 2913dc5a581c4c82b085683bbb0550cf
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/aggregate-audit-findings.js:307:10"
```

### Pattern

`^E\d$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:291cf057613f1dcce26d81a1bd504586:search

```yaml
regex_id: 291cf057613f1dcce26d81a1bd504586
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-content-accuracy.js:295:31"
```

### Pattern

`^\.\.?[\\/]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:29731037a6aa6adcaf3a79baa6aee3c0:search

```yaml
regex_id: 29731037a6aa6adcaf3a79baa6aee3c0
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/doc-ecosystem-audit/scripts/checkers/index-registry-health.js:451:10"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2983b3d231e18476558856679c03889a:search

```yaml
regex_id: 2983b3d231e18476558856679c03889a
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/lib/ai-pattern-checks.js:85:31"
```

### Pattern

`^[A-Za-z]:[\\/]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:29e9b84ae83d44db2997cf58f0f0dec2:search

```yaml
regex_id: 29e9b84ae83d44db2997cf58f0f0dec2
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/reviews/lib/parse-review.ts:314:26"
```

### Pattern

`^\*\*[^*]+:\*\*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2a376a55b5f3eab16dbccf0a3da8dd57:search

```yaml
regex_id: 2a376a55b5f3eab16dbccf0a3da8dd57
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:257:4"
```

### Pattern

`^open\s+questions`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2b62a198b7fb9995133a1cb301e9bd9b:search

```yaml
regex_id: 2b62a198b7fb9995133a1cb301e9bd9b
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/user-prompt-handler.js:446:4"
```

### Pattern

`^(?:i'?m\s+)?finished\s*(?:for\s+(?:now|today))?\s*[.!]?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2bfdd5bd278ea3fea14cc5331d8bf570:search

```yaml
regex_id: 2bfdd5bd278ea3fea14cc5331d8bf570
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/user-prompt-handler.js:449:4"
```

### Pattern

`^(?:that'?s?\s+)?(?:enough|good)\s+for\s+(?:now|today)\s*[.!]?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2d4eef30a3a2e0492311b4916de9f114:search

```yaml
regex_id: 2d4eef30a3a2e0492311b4916de9f114
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:205:4"
```

### Pattern

`^functions\/src\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2dcfbe3999939ab5614639a9249782b5:search

```yaml
regex_id: 2dcfbe3999939ab5614639a9249782b5
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/security-check.js:72:41"
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

## usage_mismatch:2e91ea98de5973a44cd6ff1e15f1b8f5:search

```yaml
regex_id: 2e91ea98de5973a44cd6ff1e15f1b8f5
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/doc-ecosystem-audit/scripts/checkers/index-registry-health.js:508:8"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2ee9e9f00efaad68d439f9d01c6f3867:search

```yaml
regex_id: 2ee9e9f00efaad68d439f9d01c6f3867
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:932:6"
```

### Pattern

`(?:^|[\\/])(?:check-pattern-compliance|safe-fs|security-helpers|session-start)\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2f7ba12b802259a77006edf86e895729:search

```yaml
regex_id: 2f7ba12b802259a77006edf86e895729
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:624:38"
```

### Pattern

`^#+\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2fde2da76cc0ec1974c24579d3063b84:search

```yaml
regex_id: 2fde2da76cc0ec1974c24579d3063b84
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/aggregate-audit-findings.js:352:38"
```

### Pattern

`^### \[([^\]]+)\] ([^\n]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2fe7604542654d8032ff04bebaaf8af3:search

```yaml
regex_id: 2fe7604542654d8032ff04bebaaf8af3
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-content-accuracy.js:231:4"
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

## usage_mismatch:31f236656e34aca384401c39f64d793d:search

```yaml
regex_id: 31f236656e34aca384401c39f64d793d
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:166:13"
```

### Pattern

`(^|[/\\])\.env(\.[a-zA-Z0-9_-]{1,30})*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:321fa9577e52d36ae9c3582404944eb1:search

```yaml
regex_id: 321fa9577e52d36ae9c3582404944eb1
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-cross-doc-deps.js:177:47"
```

### Pattern

`^[+-]{3}`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:33be51f4c177f1c507631ee5ad4e8b2b:search

```yaml
regex_id: 33be51f4c177f1c507631ee5ad4e8b2b
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/user-prompt-handler.js:564:4"
```

### Pattern

`^(?:just\s+)?(?:fix|update|change|modify)\s+(?:the\s+)?(?:one|single|this)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:348d512fd4f852c6b1fc9a3f43762607:search

```yaml
regex_id: 348d512fd4f852c6b1fc9a3f43762607
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:266:4"
```

### Pattern

`^(before|after)\s+(refactoring|phase|this)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:377d242edcd96e18508f094d0831cf32:search

```yaml
regex_id: 377d242edcd96e18508f094d0831cf32
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:246:4"
```

### Pattern

`^strengths`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:38f1df570d6fc4798590bc43df18b72f:search

```yaml
regex_id: 38f1df570d6fc4798590bc43df18b72f
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:248:4"
```

### Pattern

`^appendix`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:390c299aa3009a8e50895eabb532c262:search

```yaml
regex_id: 390c299aa3009a8e50895eabb532c262
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/reviews/lib/parse-review.ts:49:18"
```

### Pattern

`^#{2,4}\s+Review\s+#(\d+)(?::|\s+--|\s+\u2014)\s*(.*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:39556f30dfcabaad9ee1f6a03302c84b:search

```yaml
regex_id: 39556f30dfcabaad9ee1f6a03302c84b
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:274:4"
```

### Pattern

`^no\s+(major\s+)?contradictions`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:39ae8df5c542b21c1708706a2c397ca6:search

```yaml
regex_id: 39ae8df5c542b21c1708706a2c397ca6
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/user-prompt-handler.js:447:4"
```

### Pattern

`^(?:we'?re\s+)?done\s*(?:here)?\s*[.!]?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3a1ce4203d99ca0356836be9bee30512:search

```yaml
regex_id: 3a1ce4203d99ca0356836be9bee30512
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/lib/reference-graph.js:323:6"
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

## usage_mismatch:3a2e944d2c18f78ad18fe356000ae088:search

```yaml
regex_id: 3a2e944d2c18f78ad18fe356000ae088
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-docs-light.js:283:4"
```

### Pattern

`^link$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3a57ebda1f8fbad707776c30ffc2de68:search

```yaml
regex_id: 3a57ebda1f8fbad707776c30ffc2de68
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/doc-ecosystem-audit/scripts/checkers/link-reference-integrity.js:369:10"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3a66b9989de22e6dfdaa9764acda0d82:search

```yaml
regex_id: 3a66b9989de22e6dfdaa9764acda0d82
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/archive/sync-reviews-to-jsonl.js:753:32"
```

### Pattern

`^###\s+PR\s+#(\d+)\s+Retrospective\s*\((\d{4}-\d{2}-\d{2})\)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3b6cdd38a5aea7d98f6efb71fdad8153:search

```yaml
regex_id: 3b6cdd38a5aea7d98f6efb71fdad8153
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:189:2"
```

### Pattern

`^scripts\/validate-audit\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3c3f0f4a343a9e24f1316c6366620f30:search

```yaml
regex_id: 3c3f0f4a343a9e24f1316c6366620f30
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-cross-doc-deps.js:296:6"
```

### Pattern

`COMMAND_REFERENCE\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3d6650ad0a7f5f8c9acb706af35ff64f:search

```yaml
regex_id: 3d6650ad0a7f5f8c9acb706af35ff64f
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-docs-light.js:422:6"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3e2c4af76f06aca12711e380149a7af2:search

```yaml
regex_id: 3e2c4af76f06aca12711e380149a7af2
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-docs-light.js:282:4"
```

### Pattern

`^file$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3ecd674485d1466f651effd77a4a4f94:search

```yaml
regex_id: 3ecd674485d1466f651effd77a4a4f94
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:2049:69"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3efb58fc91a236b93c7fcbeb1df73dc0:search

```yaml
regex_id: 3efb58fc91a236b93c7fcbeb1df73dc0
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/script-ecosystem-audit/scripts/checkers/module-consistency.js:298:9"
```

### Pattern

`^(?:#!\/usr\/bin\/env(?:\s+-S)?\s+node(?:\s+[-\w=]+)*|#!\/usr\/bin\/node)\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3f57c248cb451d0a3650e1ce7d3c5719:search

```yaml
regex_id: 3f57c248cb451d0a3650e1ce7d3c5719
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/multi-ai/normalize-format.js:823:6"
```

### Pattern

`^E[0-3]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:406eccc4d3aca54812e0e3470b94dc0a:search

```yaml
regex_id: 406eccc4d3aca54812e0e3470b94dc0a
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-doc-placement.js:61:6"
```

### Pattern

`^docs\/[^/]+\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:408d0e2ff75294b6bded85365c1e5c64:search

```yaml
regex_id: 408d0e2ff75294b6bded85365c1e5c64
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/lib/ai-pattern-checks.js:107:4"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4176bae948513d63da968ac7b513fe7e:search

```yaml
regex_id: 4176bae948513d63da968ac7b513fe7e
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/security-check.js:108:14"
```

### Pattern

`\.test\.[jt]s$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:417f9e8ff7010ec78daf02ef9ffe8a1b:search

```yaml
regex_id: 417f9e8ff7010ec78daf02ef9ffe8a1b
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/archive/sync-reviews-to-jsonl.js:307:39"
```

### Pattern

`\((\d{4}-\d{2}-\d{2})\)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:431b221eec691b0daa9bdcc5ddd2fd96:search

```yaml
regex_id: 431b221eec691b0daa9bdcc5ddd2fd96
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-triggers.js:179:4"
```

### Pattern

`^\.claude\/skills\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:435c8ae13b9817bc4976c997941464a7:search

```yaml
regex_id: 435c8ae13b9817bc4976c997941464a7
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-triggers.js:184:4"
```

### Pattern

`^tests\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:457f4e31d2afc13efa7b22ac15cfb70d:search

```yaml
regex_id: 457f4e31d2afc13efa7b22ac15cfb70d
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:2049:23"
```

### Pattern

`^(?:[A-Za-z]:[\\/]|\\\\|\/\/)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:46a94a25c4c29c33b4fa53a0f5fd390b:search

```yaml
regex_id: 46a94a25c4c29c33b4fa53a0f5fd390b
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/lib/reference-graph.js:224:53"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:47b78f28a7f83d6f56e7d74978821fd0:search

```yaml
regex_id: 47b78f28a7f83d6f56e7d74978821fd0
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/user-prompt-handler.js:665:4"
```

### Pattern

`^\s*stop\b(?!\s+(?:the|a|this|that|it|loop|server|process|running|execution|polling))`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:47e6f0837b243ecfe0c15a125977f85b:search

```yaml
regex_id: 47e6f0837b243ecfe0c15a125977f85b
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:244:4"
```

### Pattern

`^conclusion`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:482e5da7ecfd47d2e6b9ad74cfb0cf00:search

```yaml
regex_id: 482e5da7ecfd47d2e6b9ad74cfb0cf00
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:77:6"
```

### Pattern

`^context\/.*\.tsx$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4935c4f11054c5db0e71d40ff2b19c74:search

```yaml
regex_id: 4935c4f11054c5db0e71d40ff2b19c74
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:584:6"
```

### Pattern

`\.(test|spec)\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4bbdfb95baf10361b98784dd23316b5e:search

```yaml
regex_id: 4bbdfb95baf10361b98784dd23316b5e
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/skill-ecosystem-audit/scripts/checkers/coverage-consistency.js:201:42"
```

### Pattern

`^\|\s*[`/]*([a-z][a-z0-9-]+)\s*[`]*\s*\|([^|]+)\|`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4ccde736f9899fc726fd09626c4ea9d1:search

```yaml
regex_id: 4ccde736f9899fc726fd09626c4ea9d1
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/script-ecosystem-audit/scripts/checkers/code-quality.js:288:20"
```

### Pattern

`^\w+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4cd2f9058e910356e82409984c7cae30:search

```yaml
regex_id: 4cd2f9058e910356e82409984c7cae30
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:103:6"
```

### Pattern

`^next\.config\.(js|mjs)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4d9bbb3a6e62bff8e62abab1d7df36d4:search

```yaml
regex_id: 4d9bbb3a6e62bff8e62abab1d7df36d4
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/aggregate-audit-findings.js:424:6"
```

### Pattern

`^[-*]\s*\[([ xX])\]\s*\*\*([A-Z][A-Z0-9-]*\d+):\*\*\s*(.{1,1000})`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4dc0d77008e7df4b4bb071ec6735e6c2:search

```yaml
regex_id: 4dc0d77008e7df4b4bb071ec6735e6c2
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:243:4"
```

### Pattern

`^(key\s+)?findings$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4e953c7ab79e76e15f2c54e4d9dcaf7c:search

```yaml
regex_id: 4e953c7ab79e76e15f2c54e4d9dcaf7c
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/phase-complete-check.js:385:21"
```

### Pattern

`^\.\.(?:[/\\]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4ec75894d0c7db4a7c4de949621608f2:search

```yaml
regex_id: 4ec75894d0c7db4a7c4de949621608f2
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-review-needed.js:453:10"
```

### Pattern

`^#{2,3}\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:503ea86d5a195e607646e5dc43d7ffe2:search

```yaml
regex_id: 503ea86d5a195e607646e5dc43d7ffe2
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/hook-ecosystem-audit/scripts/checkers/cicd-pipeline.js:192:11"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5051a968f72d3b796d194fb78a4e1010:search

```yaml
regex_id: 5051a968f72d3b796d194fb78a4e1010
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:731:17"
```

### Pattern

`(?:^|[\\/])check-pattern-compliance\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:51b72a748820c78ee8a12997a6b9a0c0:search

```yaml
regex_id: 51b72a748820c78ee8a12997a6b9a0c0
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:188:2"
```

### Pattern

`^scripts\/add-false-positive\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:51fda2e17c650360d3860b00bf8a8569:search

```yaml
regex_id: 51fda2e17c650360d3860b00bf8a8569
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:240:4"
```

### Pattern

`^(executive\s+)?summary$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:53010abe3938b84c6b3d7170cd684b19:search

```yaml
regex_id: 53010abe3938b84c6b3d7170cd684b19
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/hook-ecosystem-audit/scripts/checkers/code-quality-security.js:70:21"
```

### Pattern

`\.(js|ts)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:532bf6ebce09a505530f2dcb1e71ab46:search

```yaml
regex_id: 532bf6ebce09a505530f2dcb1e71ab46
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/doc-ecosystem-audit/scripts/checkers/content-quality.js:195:31"
```

### Pattern

`^```(\S*)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:53374d685d020c667fd34a2ffed60681:search

```yaml
regex_id: 53374d685d020c667fd34a2ffed60681
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/multi-ai/normalize-format.js:200:6"
```

### Pattern

`^#{2,4}\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:53a2c9cb29a1fbd7634091a691a942fc:search

```yaml
regex_id: 53a2c9cb29a1fbd7634091a691a942fc
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/lib/ai-pattern-checks.js:85:62"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5458228f958df76dd085e680019a44d1:search

```yaml
regex_id: 5458228f958df76dd085e680019a44d1
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:1668:17"
```

### Pattern

`(?:^|[\\/])check-pattern-compliance\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:559d82ef18049221c4f879cf5b1f6949:search

```yaml
regex_id: 559d82ef18049221c4f879cf5b1f6949
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:540:8"
```

### Pattern

`^#{1,5}\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:55aee069d33a20e8b88f02993ac5fd0b:search

```yaml
regex_id: 55aee069d33a20e8b88f02993ac5fd0b
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:259:4"
```

### Pattern

`^testing\s+(strategy|recommendations)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:55cf0c544968e3cae68d4b58213fd355:search

```yaml
regex_id: 55cf0c544968e3cae68d4b58213fd355
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:1615:17"
```

### Pattern

`(?:^|[\\/])(?:check-pattern-compliance|cookie-utils?)\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:56389a25ba391b55c4d79f1c7be0144f:search

```yaml
regex_id: 56389a25ba391b55c4d79f1c7be0144f
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:464:6"
```

### Pattern

`(?:^|[\\/])(?:phase-complete-check|check-doc-headers|sync-claude-settings|transform-jsonl-schema|eval-check-stage|eval-snapshot|eval-sonarcloud-snapshot|state-utils)\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5669b06a89cc07305174561847dc71e5:search

```yaml
regex_id: 5669b06a89cc07305174561847dc71e5
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:269:4"
```

### Pattern

`^(duplicate|comparison|contradiction)\s+analysis`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5684ab91dd0fed489f47f72296505b3b:search

```yaml
regex_id: 5684ab91dd0fed489f47f72296505b3b
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:261:4"
```

### Pattern

`^(cost-?benefit|backward\s+compat)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:5749406051d40b1f715ad7bb7afaf510:email

```yaml
regex_id: 5749406051d40b1f715ad7bb7afaf510
schema_version: "1"
kind: intent_mismatch
corpus: sonash-v0
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-roadmap-debt.js:136:4"
```

### Pattern

`\b(notification|alert\s+system|email|sms)\b`

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

## usage_mismatch:57bd9960155ceb52f865d7e3b0e42a8f:search

```yaml
regex_id: 57bd9960155ceb52f865d7e3b0e42a8f
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:532:6"
```

### Pattern

`\.(test|spec)\.tsx$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:58184e7e416fae91682d025573935483:search

```yaml
regex_id: 58184e7e416fae91682d025573935483
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-review-needed.js:522:28"
```

### Pattern

`^\|\s*(\d{4}-\d{2}-\d{2})\s*\|`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:584687ad2332a8d3f664c0d795d9d186:search

```yaml
regex_id: 584687ad2332a8d3f664c0d795d9d186
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/user-prompt-handler.js:448:4"
```

### Pattern

`^(?:let'?s?\s+)?(?:stop|end|wrap\s*up)\s*(?:here|now|for\s+today)?\s*[.!]?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:58b6d1f9cd457a1bf9a4dc389c044f6e:search

```yaml
regex_id: 58b6d1f9cd457a1bf9a4dc389c044f6e
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/multi-ai/normalize-format.js:40:20"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:58f13d8bda3e99e8fdb28c1b7417a348:search

```yaml
regex_id: 58f13d8bda3e99e8fdb28c1b7417a348
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/analyze-learning-effectiveness.js:226:29"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5ad3a82968f85eebe22f66c3b694fcc5:search

```yaml
regex_id: 5ad3a82968f85eebe22f66c3b694fcc5
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/docs/generate-llms-txt.js:143:8"
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

## usage_mismatch:5b0d624a3ce064824c9ccfda8fd501cf:search

```yaml
regex_id: 5b0d624a3ce064824c9ccfda8fd501cf
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/hook-ecosystem-audit/scripts/checkers/cicd-pipeline.js:138:32"
```

### Pattern

`^\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5b49ee3722ff6613aa9b76cf287dddb4:search

```yaml
regex_id: 5b49ee3722ff6613aa9b76cf287dddb4
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:276:4"
```

### Pattern

`^(external|internal)\s+links`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5bb2d02c6f85ecb9b05676b3b36c96bb:search

```yaml
regex_id: 5bb2d02c6f85ecb9b05676b3b36c96bb
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/aggregate-audit-findings.js:532:17"
```

### Pattern

`\.(?:tsx?|jsx?|mjs|cjs|json|md)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5bbb4b71e153562dd7d62836eb956ecd:search

```yaml
regex_id: 5bbb4b71e153562dd7d62836eb956ecd
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-triggers.js:182:4"
```

### Pattern

`^scripts\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5c8fe511f3740952c213bb8606c728dc:search

```yaml
regex_id: 5c8fe511f3740952c213bb8606c728dc
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/archive/sync-reviews-to-jsonl.js:427:65"
```

### Pattern

`^#{2,4}\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5d338ae8bbb2be25459f59effb1b771e:search

```yaml
regex_id: 5d338ae8bbb2be25459f59effb1b771e
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/health-ecosystem-audit/scripts/checkers/coverage-completeness.js:283:41"
```

### Pattern

`^not ok\s+\d+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5d46107ef4674e772029dabad3632500:search

```yaml
regex_id: 5d46107ef4674e772029dabad3632500
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/pr-ecosystem-audit/scripts/checkers/pattern-lifecycle.js:508:38"
```

### Pattern

`^##+ Template \d+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5deea1cb50f18749e36701aec4b2b391:search

```yaml
regex_id: 5deea1cb50f18749e36701aec4b2b391
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/alerts/scripts/run-alerts.js:3422:37"
```

### Pattern

`^✖\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5e77f17a1195e511edf2cdcf7618c584:search

```yaml
regex_id: 5e77f17a1195e511edf2cdcf7618c584
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-doc-placement.js:93:13"
```

### Pattern

`^(archive-|archived-|\.archive)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5fdb996a881b1ca4d1f533b6bf955bb7:search

```yaml
regex_id: 5fdb996a881b1ca4d1f533b6bf955bb7
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/user-prompt-handler.js:453:4"
```

### Pattern

`^(?:ok|okay|great),?\s*(?:that'?s?\s+)?(?:all|it|enough)\s*[.!]?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6111133cefd34bf31fdd5acc0609ba43:search

```yaml
regex_id: 6111133cefd34bf31fdd5acc0609ba43
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/review-lifecycle.js:308:30"
```

### Pattern

`^\s*\*\*[^*]+:\*\*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:61ec9f54a0ad07d6b362200ec8825ab1:search

```yaml
regex_id: 61ec9f54a0ad07d6b362200ec8825ab1
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/doc-ecosystem-audit/scripts/checkers/content-quality.js:110:27"
```

### Pattern

`^##\s+Changelog`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:622a7a85c6025995de572f53125d136c:search

```yaml
regex_id: 622a7a85c6025995de572f53125d136c
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:199:2"
```

### Pattern

`^scripts\/retry-failures\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:62e0ed11619f8c8b321f0dbabb0fb188:search

```yaml
regex_id: 62e0ed11619f8c8b321f0dbabb0fb188
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/aggregate-audit-findings.js:580:6"
```

### Pattern

`^\|\s*\*?\*?([\w-]+)\*?\*?\s*\|\s*([^|]{1,500})\s*\|\s*([^|]{1,500})\s*\|\s*([^|]{1,500})\s*\|`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:64365b7795ef4e4237a9f45e6e9b19ac:search

```yaml
regex_id: 64365b7795ef4e4237a9f45e6e9b19ac
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-content-accuracy.js:233:4"
```

### Pattern

`^#`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:64688a21f126fa5744d20f1c5327fbb8:search

```yaml
regex_id: 64688a21f126fa5744d20f1c5327fbb8
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:148:19"
```

### Pattern

`\.(ts|tsx|js|jsx)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:659b10ad62be65e6c391f9cc454b28a4:search

```yaml
regex_id: 659b10ad62be65e6c391f9cc454b28a4
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/docs/generate-llms-txt.js:135:8"
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

## usage_mismatch:670683026b2a2c6e404fc4641c9c5254:search

```yaml
regex_id: 670683026b2a2c6e404fc4641c9c5254
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:190:2"
```

### Pattern

`^scripts\/validate-canon-schema\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:67163279faf9954c8be1adc27378c9bf:search

```yaml
regex_id: 67163279faf9954c8be1adc27378c9bf
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:78:6"
```

### Pattern

`^functions\/src\/(?!auth|security).*\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:67d6d6bddb46e76c4a2826c153d4e3a4:search

```yaml
regex_id: 67d6d6bddb46e76c4a2826c153d4e3a4
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:264:4"
```

### Pattern

`^(?:short|medium).?term\s*(?:actions?|next\s+steps?)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6884e836c0b503b39817ec26deeeb7c3:search

```yaml
regex_id: 6884e836c0b503b39817ec26deeeb7c3
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/multi-ai/normalize-format.js:752:37"
```

### Pattern

`^(?:issue|finding|problem|bug|vuln\w*)\s*[:.-]\s*(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:698c0202ac5268d22b392909c9ab835e:search

```yaml
regex_id: 698c0202ac5268d22b392909c9ab835e
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:280:4"
```

### Pattern

`^(fetching|context7)\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:69cd35d70f531e00301bd71905017704:search

```yaml
regex_id: 69cd35d70f531e00301bd71905017704
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:149:27"
```

### Pattern

`\.(js|ts|tsx|jsx|sh|yml|yaml)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:69d92fd9da1a0fe6bef3adcc869a9255:search

```yaml
regex_id: 69d92fd9da1a0fe6bef3adcc869a9255
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-context-debt.js:180:8"
```

### Pattern

`^#{1,4}\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6ae38c3f3e2dab852132a5527c665b74:search

```yaml
regex_id: 6ae38c3f3e2dab852132a5527c665b74
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:183:2"
```

### Pattern

`^scripts\/check-docs-light\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6af6f6ab51488a28bc12d47a913861f9:search

```yaml
regex_id: 6af6f6ab51488a28bc12d47a913861f9
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:1640:17"
```

### Pattern

`(?:^|[\\/])(?:check-pattern-compliance|decrypt-secrets)\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6b66f52f9f16884082bc621b3ef35d51:search

```yaml
regex_id: 6b66f52f9f16884082bc621b3ef35d51
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/docs/generate-llms-txt.js:46:8"
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

## usage_mismatch:6b9819aaee27057b9bbb636b3ba0a960:search

```yaml
regex_id: 6b9819aaee27057b9bbb636b3ba0a960
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:1013:17"
```

### Pattern

`(?:^|[\\/])(?:check-pattern-compliance|safe-fs|parse-jsonl-line)\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6c30ddc74eb60a4ddff70e23fac47314:search

```yaml
regex_id: 6c30ddc74eb60a4ddff70e23fac47314
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:175:2"
```

### Pattern

`^tests\/pattern-compliance\.test\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6c4fd3d1c2c1330f578ac987040b487f:search

```yaml
regex_id: 6c4fd3d1c2c1330f578ac987040b487f
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-triggers.js:175:25"
```

### Pattern

`\.(ts|tsx|js|jsx|py|sh|go|rs|rb|php|java|kt|swift)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6c78b2b9bf119d350d62a1661b68132b:search

```yaml
regex_id: 6c78b2b9bf119d350d62a1661b68132b
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:210:2"
```

### Pattern

`^tests\/semgrep\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6ce7be9ded906a37d572127c2157b9ed:search

```yaml
regex_id: 6ce7be9ded906a37d572127c2157b9ed
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:480:56"
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

## usage_mismatch:6e7997d8412ca76b58478b3ed519ae0d:search

```yaml
regex_id: 6e7997d8412ca76b58478b3ed519ae0d
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/docs/generate-llms-txt.js:169:8"
```

### Pattern

`^#\s+\S`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6f44cc8dc7bf389ce46ea9ec3f18cefc:search

```yaml
regex_id: 6f44cc8dc7bf389ce46ea9ec3f18cefc
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:321:10"
```

### Pattern

`\.[a-zA-Z]{1,5}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6f63cc91b3c68ab73e4fe3fa9b49ee1f:search

```yaml
regex_id: 6f63cc91b3c68ab73e4fe3fa9b49ee1f
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:281:4"
```

### Pattern

`^(architecture|roadmap\s+phasing|business|compliance|accessibility|data\s+model|ui\/ux|quality)\s+(comparison|analysis|recommendations?)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6fae3daa7a9b14d130a347b30779dab2:search

```yaml
regex_id: 6fae3daa7a9b14d130a347b30779dab2
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/multi-ai/normalize-format.js:878:50"
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

## usage_mismatch:70d0f60576535ab7a1a8dd479dc13597:search

```yaml
regex_id: 70d0f60576535ab7a1a8dd479dc13597
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:241:4"
```

### Pattern

`^overview$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:70df59782d2f3c3f5c9fa46df0aeb147:search

```yaml
regex_id: 70df59782d2f3c3f5c9fa46df0aeb147
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:277:4"
```

### Pattern

`^(core|ui|backend|utility|developer)\s+(framework\s+)?libraries$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:70e35139b6e54e35fdbf42c5ccb64b68:search

```yaml
regex_id: 70e35139b6e54e35fdbf42c5ccb64b68
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-roadmap-debt.js:227:17"
```

### Pattern

`^#+\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:70ebf06f92f26fbc5637d1484ad857f1:search

```yaml
regex_id: 70ebf06f92f26fbc5637d1484ad857f1
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/doc-ecosystem-audit/scripts/checkers/index-registry-health.js:107:8"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:71fde7d3bb1be5ec891b8abc01f9861c:search

```yaml
regex_id: 71fde7d3bb1be5ec891b8abc01f9861c
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/archive/sync-reviews-to-jsonl.js:395:39"
```

### Pattern

`^(?:\d+\.|-)\s+\*\*([^*]+)\*\*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:720d0b7585a3cbe4357cc3d64e3fbd5f:search

```yaml
regex_id: 720d0b7585a3cbe4357cc3d64e3fbd5f
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-context-debt.js:140:37"
```

### Pattern

`^###?\s*(?:\*\*)?FINDING-([A-Z0-9]+)(?:\*\*)?:\s*(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:73bd458fa869348172ffd337ca364e34:search

```yaml
regex_id: 73bd458fa869348172ffd337ca364e34
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/script-ecosystem-audit/scripts/checkers/safety-error-handling.js:78:12"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7438111a99fbf8fdbd8dd853248d35b4:search

```yaml
regex_id: 7438111a99fbf8fdbd8dd853248d35b4
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:641:8"
```

### Pattern

`^\s*(\/\/|\/\*|\*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:74e9a387dbd13afeb9d5cd184e32b25b:search

```yaml
regex_id: 74e9a387dbd13afeb9d5cd184e32b25b
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/pr-ecosystem-audit/scripts/checkers/pattern-lifecycle.js:108:45"
```

### Pattern

`^##+ Template \d+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7549a1bbc07fc1b289dea24bc866f61a:search

```yaml
regex_id: 7549a1bbc07fc1b289dea24bc866f61a
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-content-accuracy.js:235:4"
```

### Pattern

`^node_modules\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:76cae8fee49de24df4ddd6de23bd7627:search

```yaml
regex_id: 76cae8fee49de24df4ddd6de23bd7627
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:777:17"
```

### Pattern

`(?:^|[\\/])check-pattern-compliance\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:773d35eb8a5dc8c4f8f77d3476272240:search

```yaml
regex_id: 773d35eb8a5dc8c4f8f77d3476272240
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:253:4"
```

### Pattern

`^(pre-?|post-?)deployment`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:79be5e3666c625e2319dee65f4fa4896:search

```yaml
regex_id: 79be5e3666c625e2319dee65f4fa4896
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:200:2"
```

### Pattern

`^scripts\/sync-geocache\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7a6f8f9dce31cb47e06f86c3485ce689:search

```yaml
regex_id: 7a6f8f9dce31cb47e06f86c3485ce689
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/hook-ecosystem-audit/scripts/checkers/cicd-pipeline.js:118:8"
```

### Pattern

`^run:\s*\|?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7c2f622a4be5cdb4b3d1c32155b7245b:search

```yaml
regex_id: 7c2f622a4be5cdb4b3d1c32155b7245b
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/aggregate-audit-findings.js:460:6"
```

### Pattern

`^[-*]\s*(?:\u2705|\u{1F504}|\u{1F4CB}|\u23F3|\u26A0)+\s*\*\*([A-Z][A-Z0-9-]*\d+):?\*?\*?\s*(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7cfa2bd2fb2ea4c50602fd63dc67870d:search

```yaml
regex_id: 7cfa2bd2fb2ea4c50602fd63dc67870d
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/lib/ai-pattern-checks.js:219:6"
```

### Pattern

`^@`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7dc5a7ad0dcde3e45e8bb846d6607c87:search

```yaml
regex_id: 7dc5a7ad0dcde3e45e8bb846d6607c87
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:2001:17"
```

### Pattern

`(?:^|[\\/])(?:check-pattern-compliance|safe-fs)\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7de9c8eff1da2da044ac90860f98569f:search

```yaml
regex_id: 7de9c8eff1da2da044ac90860f98569f
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:287:4"
```

### Pattern

`^no\s+conflicts`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7df9208a98a617dfe75253b25eb5fee7:search

```yaml
regex_id: 7df9208a98a617dfe75253b25eb5fee7
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/phase-complete-check.js:58:20"
```

### Pattern

`^\.\.(?:[/\\]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7e258d77d8e5adda11728e36c06be6db:search

```yaml
regex_id: 7e258d77d8e5adda11728e36c06be6db
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/user-prompt-handler.js:566:4"
```

### Pattern

`^(?:small|minor|quick)\s+(?:fix|change|update)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7fcc646e9561031e4a290d584016eb88:search

```yaml
regex_id: 7fcc646e9561031e4a290d584016eb88
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/aggregate-audit-findings.js:582:22"
```

### Pattern

`^[A-Z]+-\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:803affa9cd6dbf5a7f7c69ca98db3c52:search

```yaml
regex_id: 803affa9cd6dbf5a7f7c69ca98db3c52
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-review-needed.js:144:25"
```

### Pattern

`^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2}(\.\d{3})?Z?)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:80c3eb6b76acfb261e244e6d3bbf9264:search

```yaml
regex_id: 80c3eb6b76acfb261e244e6d3bbf9264
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:434:5"
```

### Pattern

`^docs\/audits\/[^.][^/]*\.jsonl$|^docs\/audits\/[^.][^/]*\/[^.][^/]*\.jsonl$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:80e0c1290c1ccbb0cca944975c38a1de:search

```yaml
regex_id: 80e0c1290c1ccbb0cca944975c38a1de
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:761:17"
```

### Pattern

`(?:^|[\\/])check-pattern-compliance\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8154e7dbb3573945f9b21a0446beaef0:search

```yaml
regex_id: 8154e7dbb3573945f9b21a0446beaef0
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:416:6"
```

### Pattern

`(?:^|[\\/])(?:check-pattern-compliance|eval-check-stage|eval-snapshot|unify-findings|normalize-format|no-empty-path-check|eslint-plugin-sonash\.test)\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:81b8e87d3c8a0ccd367e688efa458cc7:search

```yaml
regex_id: 81b8e87d3c8a0ccd367e688efa458cc7
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/aggregate-audit-findings.js:407:34"
```

### Pattern

`^###\s+Track\s+([A-Z])\s*[-–—]?\s*(.+)?`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:81e1fca453cf69156472b14b9f5f1a6c:search

```yaml
regex_id: 81e1fca453cf69156472b14b9f5f1a6c
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:205:2"
```

### Pattern

`^scripts\/lighthouse-audit\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:82ef73c158d14cedbf763da34069983a:search

```yaml
regex_id: 82ef73c158d14cedbf763da34069983a
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-content-accuracy.js:242:4"
```

### Pattern

`\.tmp$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:83dedf19e21f949a8796d0291121b782:search

```yaml
regex_id: 83dedf19e21f949a8796d0291121b782
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-context-debt.js:66:42"
```

### Pattern

`^INTAKE-CTX-(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:85023d91466f16ae7f6c4f59160ad347:search

```yaml
regex_id: 85023d91466f16ae7f6c4f59160ad347
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:278:4"
```

### Pattern

`^(validation|forms|data)\s+&`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:855ea1965f5b0d77dac4b87d39de58d4:search

```yaml
regex_id: 855ea1965f5b0d77dac4b87d39de58d4
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-propagation.js:295:2"
```

### Pattern

`^\+.*\b(?:const|let|var)\s+([a-zA-Z_$][a-zA-Z0-9_$]*)\s*=\s*(?:function|\(|async\s)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:858e466d39e825ca9deb5fceb7da23d1:search

```yaml
regex_id: 858e466d39e825ca9deb5fceb7da23d1
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:99:6"
```

### Pattern

`^firebase\.json$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:865a0337c901d4cd671d73fc59607bf6:search

```yaml
regex_id: 865a0337c901d4cd671d73fc59607bf6
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/analyze-learning-effectiveness.js:374:36"
```

### Pattern

`^\|\s*([🔴🟡⚪])\s*\|([^|]*)\|([^|]*)\|([^|]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:868d43327fa4249207f1888e77c311ce:search

```yaml
regex_id: 868d43327fa4249207f1888e77c311ce
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/user-prompt-handler.js:444:4"
```

### Pattern

`^(?:that'?s?\s+)?(?:all|it)\s*(?:for\s+(?:now|today))?\s*[.!]?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:86c55dab2e61e9d06dc5523db5491ff3:search

```yaml
regex_id: 86c55dab2e61e9d06dc5523db5491ff3
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-doc-placement.js:55:15"
```

### Pattern

`^ROADMAP\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:879287db305849b496dce0f7b42658af:search

```yaml
regex_id: 879287db305849b496dce0f7b42658af
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-propagation.js:253:37"
```

### Pattern

`^a\/(.+?) b\/(.+?)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:87b4f7e71d3685f1cb9ea9c1f5f140ec:search

```yaml
regex_id: 87b4f7e71d3685f1cb9ea9c1f5f140ec
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:173:2"
```

### Pattern

`^scripts\/check-propagation\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:87ffdd12943d5c5b31808348e2f6be37:search

```yaml
regex_id: 87ffdd12943d5c5b31808348e2f6be37
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-doc-placement.js:64:6"
```

### Pattern

`^SECURITY\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:888ffd1651e8658f728e0e7424523474:search

```yaml
regex_id: 888ffd1651e8658f728e0e7424523474
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/aggregate-audit-findings.js:506:22"
```

### Pattern

`^[A-Z][A-Z0-9.-]{0,200}\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:89e10cbe83a9b7b672677f5edf65d1e0:search

```yaml
regex_id: 89e10cbe83a9b7b672677f5edf65d1e0
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:380:13"
```

### Pattern

`^\s*if:\s+(?!.{0,500}\$\{\{).{0,500}(?:steps|github|env|inputs|needs)\.`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8a0aae2cf957bf7603ded7e556ac3bbb:search

```yaml
regex_id: 8a0aae2cf957bf7603ded7e556ac3bbb
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/doc-ecosystem-audit/scripts/checkers/link-reference-integrity.js:109:10"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8ad6956c7b6cc41e475e81d4152e3e84:search

```yaml
regex_id: 8ad6956c7b6cc41e475e81d4152e3e84
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:605:17"
```

### Pattern

`(?:^|[\\/])(?:check-pattern-compliance|eslint-plugin-sonash\.test)\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8b4b61341c6736a334505befb3429981:search

```yaml
regex_id: 8b4b61341c6736a334505befb3429981
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/doc-ecosystem-audit/scripts/checkers/content-quality.js:93:29"
```

### Pattern

`^description:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8b6cb33eb8c69a9a649753bce8120d6d:search

```yaml
regex_id: 8b6cb33eb8c69a9a649753bce8120d6d
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:122:2"
```

### Pattern

`^[A-Za-z]:\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8bb25c4f3e35c29bb5c0d8497cf0119a:search

```yaml
regex_id: 8bb25c4f3e35c29bb5c0d8497cf0119a
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/user-prompt-handler.js:681:4"
```

### Pattern

`^(?:YES|YEAH|YEP|ABSOLUTELY|PERFECT|GREAT|LOVE|AMAZING|AWESOME|NICE|GOOD|OK|OKAY|LGTM|ACK)\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8cc2f402434d473bf44e8efd1f17a8ba:search

```yaml
regex_id: 8cc2f402434d473bf44e8efd1f17a8ba
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:73:6"
```

### Pattern

`^app\/.*\.(ts|tsx)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8dba5eb60c7781258c9bcbd53827dc09:search

```yaml
regex_id: 8dba5eb60c7781258c9bcbd53827dc09
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:289:4"
```

### Pattern

`^(questions|next\s+steps)\s*(&|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8e311554a147994b4fd5ac39aa26f4b6:search

```yaml
regex_id: 8e311554a147994b4fd5ac39aa26f4b6
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/docs/generate-llms-txt.js:170:26"
```

### Pattern

`^#\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8edfb1cee218d4beb823eaa864ff8992:search

```yaml
regex_id: 8edfb1cee218d4beb823eaa864ff8992
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/skill-ecosystem-audit/scripts/checkers/coverage-consistency.js:411:42"
```

### Pattern

`^\|\s*[`/]*([a-z][a-z0-9-]+)\s*[`]*\s*\|`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:90ca3ca0169580313bb5b67dd2eddd8c:search

```yaml
regex_id: 90ca3ca0169580313bb5b67dd2eddd8c
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/user-prompt-handler.js:660:23"
```

### Pattern

`^\s*(?:[A-Z]{2,}\s+){2,}[A-Z]{2,}`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:90f88a354837bbd465357ce5861fd0b8:search

```yaml
regex_id: 90f88a354837bbd465357ce5861fd0b8
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:62:6"
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

## usage_mismatch:911561d604324960028e2db61dbc396b:search

```yaml
regex_id: 911561d604324960028e2db61dbc396b
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/health-ecosystem-audit/scripts/checkers/coverage-completeness.js:282:38"
```

### Pattern

`^ok\s+\d+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:91868a689208c8798c08a03a3c23604a:search

```yaml
regex_id: 91868a689208c8798c08a03a3c23604a
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-review-needed.js:482:28"
```

### Pattern

`^## Single-Session Audit Thresholds`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:921bb4ab08db8539f7623c561c422df0:search

```yaml
regex_id: 921bb4ab08db8539f7623c561c422df0
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/doc-ecosystem-audit/scripts/checkers/content-quality.js:213:25"
```

### Pattern

`^[\t ]*\*\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9283ec9d4c4b6410195591a6729676be:search

```yaml
regex_id: 9283ec9d4c4b6410195591a6729676be
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:198:2"
```

### Pattern

`^scripts\/import-.*\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9361e44af6188b857897b9bbcffe5c88:search

```yaml
regex_id: 9361e44af6188b857897b9bbcffe5c88
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-roadmap-debt.js:161:6"
```

### Pattern

`^\*\*[A-Z]\d+(?:\.\d+)?:\*\*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:94aeeb09fe222954e82b58532e896ac9:search

```yaml
regex_id: 94aeeb09fe222954e82b58532e896ac9
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:686:4"
```

### Pattern

`^scripts\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9514fa700bc5841600d1cc20974ad7ed:search

```yaml
regex_id: 9514fa700bc5841600d1cc20974ad7ed
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/aggregate-audit-findings.js:504:34"
```

### Pattern

`^\|\s*([\w.-]+)\s*\|\s*([^|]{1,500})\s*\|\s*([^|]{1,500})\s*\|`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:974757a4894347566598860207a8cfdf:search

```yaml
regex_id: 974757a4894347566598860207a8cfdf
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/alerts/scripts/run-alerts.js:1415:6"
```

### Pattern

`\.(tsx?|jsx?|mjs|cjs)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9a04da54e15a3c75fad14246b44f5db8:search

```yaml
regex_id: 9a04da54e15a3c75fad14246b44f5db8
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:89:6"
```

### Pattern

`^firestore\.rules$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9a7810538956bffddb5539dd98ef5f16:search

```yaml
regex_id: 9a7810538956bffddb5539dd98ef5f16
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/alerts/scripts/run-alerts.js:2214:37"
```

### Pattern

`^\s+[•·]\s+.+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9b964a8f4b878a91f68d605387cdcd76:search

```yaml
regex_id: 9b964a8f4b878a91f68d605387cdcd76
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:265:4"
```

### Pattern

`^(week|phase|sprint)\s+\d`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9bac35cd7ea9893493fdc59b8a8768c8:search

```yaml
regex_id: 9bac35cd7ea9893493fdc59b8a8768c8
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/reviews/lib/promote-patterns.ts:220:18"
```

### Pattern

`^-|-$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9bd092f7d6b5e7f139c2e9a0fa3b333a:search

```yaml
regex_id: 9bd092f7d6b5e7f139c2e9a0fa3b333a
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/health-ecosystem-audit/scripts/checkers/coverage-completeness.js:164:10"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9c3ee159fc0413a4abf50f4aa257e862:search

```yaml
regex_id: 9c3ee159fc0413a4abf50f4aa257e862
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:691:32"
```

### Pattern

`^\s*[-*+#]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9c86ef2cfde36196a8934a499ec9094c:search

```yaml
regex_id: 9c86ef2cfde36196a8934a499ec9094c
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/archive-doc.js:97:6"
```

### Pattern

`^[A-Za-z]:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9cc3d6a51cb3ad58155f804838319d73:search

```yaml
regex_id: 9cc3d6a51cb3ad58155f804838319d73
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:720:39"
```

### Pattern

`^#+\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9da8f3aac4fe9463e12ac21e6840afa6:search

```yaml
regex_id: 9da8f3aac4fe9463e12ac21e6840afa6
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-docs-light.js:276:4"
```

### Pattern

`\.[a-z0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9df1ee94eacfdd534b2e7a37c79da909:search

```yaml
regex_id: 9df1ee94eacfdd534b2e7a37c79da909
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:91:6"
```

### Pattern

`^\.env\.example$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9f47f65726f822f4fc4fa9871678c0b9:search

```yaml
regex_id: 9f47f65726f822f4fc4fa9871678c0b9
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-context-debt.js:182:17"
```

### Pattern

`^#+\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9f7271a502f097bedb4c1cbefcba84f6:search

```yaml
regex_id: 9f7271a502f097bedb4c1cbefcba84f6
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-review-needed.js:516:49"
```

### Pattern

`^## Multi-AI Audit Log`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a07601225dd5beb476be49f2a2b2a969:search

```yaml
regex_id: a07601225dd5beb476be49f2a2b2a969
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-docs-light.js:279:4"
```

### Pattern

`^<[a-z_-]+>$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a07b04e4f2f30e7af71f1214bf4bc053:search

```yaml
regex_id: a07b04e4f2f30e7af71f1214bf4bc053
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/doc-ecosystem-audit/scripts/checkers/link-reference-integrity.js:544:16"
```

### Pattern

`^-+|-+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a1d1f7c21aa280d05bcf6e7266abfaa3:search

```yaml
regex_id: a1d1f7c21aa280d05bcf6e7266abfaa3
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/multi-ai/normalize-format.js:202:40"
```

### Pattern

`^#{2,4}\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a3b35d78a13b61f7d0bbfa7d160935a9:search

```yaml
regex_id: a3b35d78a13b61f7d0bbfa7d160935a9
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/generate-test-registry.js:655:10"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a3e97916c2e7f4d76d8fd01edbec8cc9:search

```yaml
regex_id: a3e97916c2e7f4d76d8fd01edbec8cc9
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:145:19"
```

### Pattern

`\.(ts|tsx|js|jsx|py|sh|go|rs|rb|php|java|kt|swift)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a402a55eee82ee866d539efd93bed2a0:search

```yaml
regex_id: a402a55eee82ee866d539efd93bed2a0
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/security-check.js:141:2"
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

## usage_mismatch:a40956278ed333f0fb87e2bca2f96138:search

```yaml
regex_id: a40956278ed333f0fb87e2bca2f96138
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/script-ecosystem-audit/scripts/checkers/registration-reachability.js:127:11"
```

### Pattern

`^\.\.(?:\/|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a42155d43844e8cd46093a9425e9f7bd:search

```yaml
regex_id: a42155d43844e8cd46093a9425e9f7bd
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-content-accuracy.js:232:4"
```

### Pattern

`^mailto:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a461e9b38d88f3d3712a15e7d73f4c02:search

```yaml
regex_id: a461e9b38d88f3d3712a15e7d73f4c02
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/multi-ai/normalize-format.js:209:6"
```

### Pattern

`^\d+\.\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a46f7ca348813bcf21ca3c70c3efbe0f:search

```yaml
regex_id: a46f7ca348813bcf21ca3c70c3efbe0f
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:1324:17"
```

### Pattern

`(?:^|[\\/])check-pattern-compliance\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a67310cda20cfaa87b9397e81d26987c:search

```yaml
regex_id: a67310cda20cfaa87b9397e81d26987c
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:874:6"
```

### Pattern

`(?:^|[\\/])(?:check-pattern-compliance|security-helpers|session-start|commit-tracker)\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a70825d4848b1e04b883c6422f4c1eb3:search

```yaml
regex_id: a70825d4848b1e04b883c6422f4c1eb3
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-doc-placement.js:98:13"
```

### Pattern

`TEMPLATE\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a89ec4435ab3393b2eaf46fe925b94f7:search

```yaml
regex_id: a89ec4435ab3393b2eaf46fe925b94f7
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:74:6"
```

### Pattern

`^components\/.*\.tsx$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a8ad5e7d3100c8003efb7ae1308c1692:search

```yaml
regex_id: a8ad5e7d3100c8003efb7ae1308c1692
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/user-prompt-handler.js:459:4"
```

### Pattern

`^(?:thanks?|thx|ty|thank\s+you)\s*[!.]?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a8e55e6f70664829ed6744f4b6072a96:search

```yaml
regex_id: a8e55e6f70664829ed6744f4b6072a96
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/analyze-learning-effectiveness.js:291:41"
```

### Pattern

`^\d+\.\s+\*\*([^*]+)\*\*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a93a1f9864f1f341dd219cb0e1577850:search

```yaml
regex_id: a93a1f9864f1f341dd219cb0e1577850
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:255:4"
```

### Pattern

`^(risk|impact)\s+(assessment|summary|analysis)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a9a7529526902ceeda4c1d9c451dc589:search

```yaml
regex_id: a9a7529526902ceeda4c1d9c451dc589
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/security-check.js:50:6"
```

### Pattern

`(?:^|[\\/])security-check\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a9b2436491fd86e28d4ddd21b6440371:search

```yaml
regex_id: a9b2436491fd86e28d4ddd21b6440371
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:283:4"
```

### Pattern

`^(already|existing)\s+(in\s+roadmap|quality)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:aa34ed4651b8e5e6b9855bcdb1240fef:search

```yaml
regex_id: aa34ed4651b8e5e6b9855bcdb1240fef
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:260:4"
```

### Pattern

`^(deployment|migration)\s+checklist$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:aa6432f757fa0a95d554c9adcf62f689:search

```yaml
regex_id: aa6432f757fa0a95d554c9adcf62f689
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:75:6"
```

### Pattern

`^lib\/(?!firebase-config|rate-limiter).*\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:aa81ef884f90b9f152f93cf0331975c4:search

```yaml
regex_id: aa81ef884f90b9f152f93cf0331975c4
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/lib/ai-pattern-checks.js:238:6"
```

### Pattern

`^@\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ac7303b3ae439fb42bf26dd3e1a168be:search

```yaml
regex_id: ac7303b3ae439fb42bf26dd3e1a168be
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/lib/security-helpers.js:475:16"
```

### Pattern

`^-+|-+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ad454c76e421a10c494e899b28ca562a:search

```yaml
regex_id: ad454c76e421a10c494e899b28ca562a
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:275:4"
```

### Pattern

`^overall\s+assessment`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ae41bb442ca16429c21bc73fca6269af:search

```yaml
regex_id: ae41bb442ca16429c21bc73fca6269af
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:392:25"
```

### Pattern

`^\.\.(?:[/\\]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ae92b38f3e7339308336fc8a623627c9:search

```yaml
regex_id: ae92b38f3e7339308336fc8a623627c9
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:688:4"
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

## usage_mismatch:aebfa267711d17f7b76dbb1314484f6e:search

```yaml
regex_id: aebfa267711d17f7b76dbb1314484f6e
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:285:4"
```

### Pattern

`^(code\s+)?changes\s+\(already`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:af2a7d0dd3bcd54e697a43641ba3cf09:search

```yaml
regex_id: af2a7d0dd3bcd54e697a43641ba3cf09
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/lib/ai-pattern-checks.js:252:6"
```

### Pattern

`^[/\\]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:af981f430cfa9f0dad275176ec2a6266:search

```yaml
regex_id: af981f430cfa9f0dad275176ec2a6266
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/review-lifecycle.js:274:30"
```

### Pattern

`^\s*\*\*[^*]+:\*\*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:afc2bbdbd4b9d5a7780a183b9ab116d4:search

```yaml
regex_id: afc2bbdbd4b9d5a7780a183b9ab116d4
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-cross-doc-deps.js:177:24"
```

### Pattern

`^[+-]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b08e535952b180fa4643d881c2d7efe2:search

```yaml
regex_id: b08e535952b180fa4643d881c2d7efe2
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:1102:17"
```

### Pattern

`(?:^|[\\/])check-pattern-compliance\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b15095b7636505ec2f9aa2ca09c61ade:search

```yaml
regex_id: b15095b7636505ec2f9aa2ca09c61ade
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:177:2"
```

### Pattern

`^tests\/semgrep\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b1630a5544f75eb760fb87979b6c78cb:search

```yaml
regex_id: b1630a5544f75eb760fb87979b6c78cb
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:583:7"
```

### Pattern

`^functions\/src\/.*\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b19fc14e055a6b5d5e1dd3483295d00c:search

```yaml
regex_id: b19fc14e055a6b5d5e1dd3483295d00c
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:916:17"
```

### Pattern

`(?:^|[\\/])(?:check-pattern-compliance|session-start)\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b1db8fd93dc27122fbc2c456e47f2950:search

```yaml
regex_id: b1db8fd93dc27122fbc2c456e47f2950
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:146:17"
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

## usage_mismatch:b2c929e71e4f822f3b8a4093fc4814b9:search

```yaml
regex_id: b2c929e71e4f822f3b8a4093fc4814b9
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:98:6"
```

### Pattern

`^\.github\/workflows\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b3777ef002d5a85207545ac93199235b:search

```yaml
regex_id: b3777ef002d5a85207545ac93199235b
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/user-prompt-handler.js:454:4"
```

### Pattern

`^(?:i\s+)?(?:think\s+)?we'?re\s+(?:good|done)\s*[.!]?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b75666ea5295413889a6a5ec5c33e586:search

```yaml
regex_id: b75666ea5295413889a6a5ec5c33e586
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/generate-test-registry.js:596:12"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b88c5af6da404686425de6353d156338:search

```yaml
regex_id: b88c5af6da404686425de6353d156338
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-doc-placement.js:55:32"
```

### Pattern

`^README\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b88dfcd0e36a96137a0a589a93e850e6:search

```yaml
regex_id: b88dfcd0e36a96137a0a589a93e850e6
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:671:36"
```

### Pattern

`^\s*[-*+]\s+(?:\[ \]\s+)?(\S+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b8e20f43b6847fae8251e220a2cacb75:search

```yaml
regex_id: b8e20f43b6847fae8251e220a2cacb75
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/commit-tracker.js:447:26"
```

### Pattern

`^gitdir:\s*(.+)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b91601eb59d544978cd940a6e099837c:search

```yaml
regex_id: b91601eb59d544978cd940a6e099837c
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/reviews/build-enforcement-manifest.ts:312:23"
```

### Pattern

`^\|\s*([^|]+?)\s*\|`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b918a30019c053ae566f1e958a43ae94:search

```yaml
regex_id: b918a30019c053ae566f1e958a43ae94
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:170:2"
```

### Pattern

`^docs\/AI_REVIEW_LEARNINGS_LOG\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b9e4a00c79e23ed227a1b53496d529a6:search

```yaml
regex_id: b9e4a00c79e23ed227a1b53496d529a6
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-docs-light.js:281:4"
```

### Pattern

`^url$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b9e67b0789f0402202aff0a70509dbac:search

```yaml
regex_id: b9e67b0789f0402202aff0a70509dbac
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/multi-ai/normalize-format.js:575:37"
```

### Pattern

`^([A-Z]+-\d+)\s*[:.-]\s*(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b9f19838237544a615aa9d9a90e8e780:search

```yaml
regex_id: b9f19838237544a615aa9d9a90e8e780
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/health-ecosystem-audit/scripts/checkers/checker-infrastructure.js:68:10"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ba5303482ddcc1aad36d25ea4a0cda49:search

```yaml
regex_id: ba5303482ddcc1aad36d25ea4a0cda49
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/alerts/scripts/run-alerts.js:3424:69"
```

### Pattern

`^[\s*-]*[a-z@]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bab233440f100cc669c3f758ef351e99:search

```yaml
regex_id: bab233440f100cc669c3f758ef351e99
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:202:2"
```

### Pattern

`^scripts\/dedupe-quotes\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bb0f927c9585bb5bed5ff45dd6e8841d:search

```yaml
regex_id: bb0f927c9585bb5bed5ff45dd6e8841d
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-triggers.js:188:4"
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

## usage_mismatch:bb83b3972c1bf2c3b4ab31968e527f7d:search

```yaml
regex_id: bb83b3972c1bf2c3b4ab31968e527f7d
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/review-lifecycle.js:483:31"
```

### Pattern

`^review-pr(\d+)-r(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bbd6d39833da827b171a79b279ce22bc:search

```yaml
regex_id: bbd6d39833da827b171a79b279ce22bc
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/doc-ecosystem-audit/scripts/checkers/link-reference-integrity.js:253:12"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bc35584095a837438fa96cc30ed42766:search

```yaml
regex_id: bc35584095a837438fa96cc30ed42766
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:720:8"
```

### Pattern

`^\s*import\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bc9c8083f0db4b96fa3f8ea1a2589585:search

```yaml
regex_id: bc9c8083f0db4b96fa3f8ea1a2589585
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:245:4"
```

### Pattern

`^(how|what|why)\s+(to|it|this|react|we)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bd491d981e72b5f2e1c60a81a3d998b5:search

```yaml
regex_id: bd491d981e72b5f2e1c60a81a3d998b5
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-propagation.js:250:37"
```

### Pattern

`^diff --git `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bdab0e7c9df59182870b668b925476a8:search

```yaml
regex_id: bdab0e7c9df59182870b668b925476a8
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/doc-ecosystem-audit/scripts/checkers/content-quality.js:212:25"
```

### Pattern

`^[\t ]*-\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bdf79746f3ebe4ad1e29afc1bec3523d:search

```yaml
regex_id: bdf79746f3ebe4ad1e29afc1bec3523d
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:61:6"
```

### Pattern

`^docs\/(?!ROADMAP|README|DOCUMENTATION_STANDARDS|GLOBAL_SECURITY_STANDARDS|TRIGGERS).*\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bdfc94344e93b69f8a8c7409c6f622d1:search

```yaml
regex_id: bdfc94344e93b69f8a8c7409c6f622d1
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:685:4"
```

### Pattern

`^functions\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:be2cdc9c6ac58c91b836838a2c3d7bb4:search

```yaml
regex_id: be2cdc9c6ac58c91b836838a2c3d7bb4
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/multi-ai/normalize-format.js:795:6"
```

### Pattern

`^S[0-3]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:be41f02e6ad76b457f6f7fa94e29b434:search

```yaml
regex_id: be41f02e6ad76b457f6f7fa94e29b434
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/user-prompt-handler.js:451:4"
```

### Pattern

`^(?:good)?bye\s*[.!]?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:be42782d7b20b7963a5f70bd33cee9e4:search

```yaml
regex_id: be42782d7b20b7963a5f70bd33cee9e4
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/doc-ecosystem-audit/scripts/checkers/link-reference-integrity.js:456:10"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:be6639537004d612d9919cef4599ce2e:search

```yaml
regex_id: be6639537004d612d9919cef4599ce2e
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/hook-ecosystem-audit/scripts/checkers/precommit-pipeline.js:742:35"
```

### Pattern

`^([A-Z_]+)="\$\(mktemp\)"`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bfd395386875662b269a361992228a2e:search

```yaml
regex_id: bfd395386875662b269a361992228a2e
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:683:4"
```

### Pattern

`^lib\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bff7fc09e5d558f9ffc87bd6d1a2d9d0:search

```yaml
regex_id: bff7fc09e5d558f9ffc87bd6d1a2d9d0
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:49:6"
```

### Pattern

`^docs\/archive\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c0304fd14e503515ac0840de4a355f01:search

```yaml
regex_id: c0304fd14e503515ac0840de4a355f01
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-docs-light.js:280:4"
```

### Pattern

`^path$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c076124dfb155b189e386e3488565bdd:search

```yaml
regex_id: c076124dfb155b189e386e3488565bdd
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/update-readme-status.js:198:4"
```

### Pattern

`^\|\s{0,100}[-:]{1,200}\s{0,100}(\|\s{0,100}[-:]{1,200}\s{0,100}){1,50}\|?\s{0,100}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c1082620f8ef119dd4e1f37c863a94e6:search

```yaml
regex_id: c1082620f8ef119dd4e1f37c863a94e6
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:720:37"
```

### Pattern

`^\s*(\/\/|\/\*|\*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c14a21a3164d8b8ffba9ac7f353020c6:search

```yaml
regex_id: c14a21a3164d8b8ffba9ac7f353020c6
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:687:4"
```

### Pattern

`^hooks\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c1e0e81c88bd508867af51404eac8f4d:search

```yaml
regex_id: c1e0e81c88bd508867af51404eac8f4d
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/alerts/scripts/run-alerts.js:2025:34"
```

### Pattern

`^## `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c20321dc25e2beff549a51273b7468db:search

```yaml
regex_id: c20321dc25e2beff549a51273b7468db
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/reviews/lib/parse-review.ts:60:27"
```

### Pattern

`^#{2,4}\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c2fa62add5618f431a15419528ede4d8:search

```yaml
regex_id: c2fa62add5618f431a15419528ede4d8
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:781:8"
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

## usage_mismatch:c4d472d2cb6ec2107c80c936a9b02b02:search

```yaml
regex_id: c4d472d2cb6ec2107c80c936a9b02b02
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:131:18"
```

### Pattern

`^\.\.(?:[/\\]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c514d276ab2d887a6657690120c64292:search

```yaml
regex_id: c514d276ab2d887a6657690120c64292
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/archive/sync-reviews-to-jsonl.js:298:33"
```

### Pattern

`^#{2,4}\s+Review\s+#(\d+):?\s*(.*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c6140bd80b5fb5da1c6bc8ea8c3455f8:search

```yaml
regex_id: c6140bd80b5fb5da1c6bc8ea8c3455f8
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/analyze-learning-effectiveness.js:256:37"
```

### Pattern

`^####\s+Review\s+#(\d+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c625b3c236245b12744ece9bd6444247:search

```yaml
regex_id: c625b3c236245b12744ece9bd6444247
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/doc-ecosystem-audit/scripts/checkers/content-quality.js:84:21"
```

### Pattern

`^#\s+.+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c655e5970b196e9e3f4daed0b351aa6a:search

```yaml
regex_id: c655e5970b196e9e3f4daed0b351aa6a
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/review-lifecycle.js:268:6"
```

### Pattern

`^\s*\*\*(Key Patterns|Patterns):\*\*\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c6699b0f5d496dcd2a26b58c20b573b0:search

```yaml
regex_id: c6699b0f5d496dcd2a26b58c20b573b0
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-doc-placement.js:430:6"
```

### Pattern

`^(temp[-_.]|tmp[-_.]|scratch[-_.]|delete[-_.]|remove[-_.])`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c67e20f4d90d51d747cb9017bc327f7f:search

```yaml
regex_id: c67e20f4d90d51d747cb9017bc327f7f
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:273:4"
```

### Pattern

`^(strong|perfect)\s+alignment`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c7e4a227cb2ad59eed88500ddbe52ba0:search

```yaml
regex_id: c7e4a227cb2ad59eed88500ddbe52ba0
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-cross-doc-deps.js:291:6"
```

### Pattern

`ROADMAP\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c7fa1f5b0370910772ebb86a2c1c142d:search

```yaml
regex_id: c7fa1f5b0370910772ebb86a2c1c142d
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/pr-ecosystem-audit/scripts/checkers/pattern-lifecycle.js:315:32"
```

### Pattern

`^##+ `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c840ce3e3cfb26a5630b777a963ecb6a:search

```yaml
regex_id: c840ce3e3cfb26a5630b777a963ecb6a
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-cross-doc-deps.js:216:14"
```

### Pattern

`^\*\*(?:Status|Last Updated|Document Version):\*\*\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c85f53a08c38cd3c5da8b3b96c7b276e:search

```yaml
regex_id: c85f53a08c38cd3c5da8b3b96c7b276e
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:279:4"
```

### Pattern

`^(library\s+)?(id\s+)?index$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c8fb68cd03db8ad9380d565e1b2e6c85:search

```yaml
regex_id: c8fb68cd03db8ad9380d565e1b2e6c85
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:284:4"
```

### Pattern

`^(documentation\s+)?(created|updated|added)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c905c8bc81e2993efd98b50b9dcdb200:search

```yaml
regex_id: c905c8bc81e2993efd98b50b9dcdb200
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/multi-ai/normalize-format.js:661:29"
```

### Pattern

`^\d+\.\s+(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cb53612c08a1c5858d2abb3f5412d36c:search

```yaml
regex_id: cb53612c08a1c5858d2abb3f5412d36c
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/generate-test-registry.js:307:6"
```

### Pattern

`^(test|lint|check|validate|verify|audit|format|security|patterns|review|crossdoc|backlog|agents|hooks:test|docs:|roadmap:|skills:)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cb7306586529159123edf75b3fb55471:search

```yaml
regex_id: cb7306586529159123edf75b3fb55471
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:215:6"
```

### Pattern

`^\s*-\s*\[x\]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cbeea112614df728580eb85e59154643:search

```yaml
regex_id: cbeea112614df728580eb85e59154643
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:477:17"
```

### Pattern

`(?:^|[\\/])check-pattern-compliance\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ccbde5f8a3c2e4b861595cbe86e28f82:search

```yaml
regex_id: ccbde5f8a3c2e4b861595cbe86e28f82
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/docs/generate-llms-txt.js:82:7"
```

### Pattern

`^\w+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ccc49ed3002337f9012e808a514bbb42:search

```yaml
regex_id: ccc49ed3002337f9012e808a514bbb42
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-docs-light.js:633:7"
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

## usage_mismatch:ceb0ef1362eff0038c6e71b33562ce12:search

```yaml
regex_id: ceb0ef1362eff0038c6e71b33562ce12
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:172:2"
```

### Pattern

`^scripts\/check-pattern-compliance\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cebf37a8492ecad76b1d789429ec3436:search

```yaml
regex_id: cebf37a8492ecad76b1d789429ec3436
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/pr-ecosystem-audit/scripts/checkers/pattern-lifecycle.js:507:38"
```

### Pattern

`^##+ .+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ced660bd4eb9b324cb1f6cde7bd0a77a:search

```yaml
regex_id: ced660bd4eb9b324cb1f6cde7bd0a77a
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:66:6"
```

### Pattern

`^styles\/.*\.css$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cf1a3d6a75a840abf376005f0ed92944:search

```yaml
regex_id: cf1a3d6a75a840abf376005f0ed92944
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:262:4"
```

### Pattern

`^key\s+(learnings|deliverables|documents)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cf4184bb79c62395c36c69519ea7747a:search

```yaml
regex_id: cf4184bb79c62395c36c69519ea7747a
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/lib/ai-pattern-checks.js:209:36"
```

### Pattern

`^[/\\]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cf5e67757c196e329d1065f21106215d:search

```yaml
regex_id: cf5e67757c196e329d1065f21106215d
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:186:2"
```

### Pattern

`^scripts\/generate-documentation-index\.mjs$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d006479470ed68227b04e69e9d515895:search

```yaml
regex_id: d006479470ed68227b04e69e9d515895
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:197:2"
```

### Pattern

`^scripts\/enrich-.*\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d04d06adc73465257ba0a2866d9ed824:search

```yaml
regex_id: d04d06adc73465257ba0a2866d9ed824
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/archive-doc.js:96:6"
```

### Pattern

`^[A-Za-z]:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d0c3b8df06fe7bf1b8e7577292946ac1:search

```yaml
regex_id: d0c3b8df06fe7bf1b8e7577292946ac1
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/archive/sync-reviews-to-jsonl.js:671:48"
```

### Pattern

`^\d+\.\s+\*\*([^*]+)\*\*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d1aa3976f21803444b992abb0f965f8f:search

```yaml
regex_id: d1aa3976f21803444b992abb0f965f8f
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/doc-ecosystem-audit/scripts/checkers/content-quality.js:179:35"
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

## usage_mismatch:d27b0e510fe6001860aab3930886c03b:search

```yaml
regex_id: d27b0e510fe6001860aab3930886c03b
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/doc-ecosystem-audit/scripts/checkers/link-reference-integrity.js:524:25"
```

### Pattern

`^#{1,6}\s+(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d2b20f20536ef902c761f3bd4f744853:search

```yaml
regex_id: d2b20f20536ef902c761f3bd4f744853
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/aggregate-audit-findings.js:282:19"
```

### Pattern

`^## Category: (.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d401117a18b4e9e0e4957d4d47426d3a:search

```yaml
regex_id: d401117a18b4e9e0e4957d4d47426d3a
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-cross-doc-deps.js:191:49"
```

### Pattern

`^[+-]{3}`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d4b5f0c655ee285516d4a7b74babb6bd:search

```yaml
regex_id: d4b5f0c655ee285516d4a7b74babb6bd
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:263:4"
```

### Pattern

`^(?:immediate|long.?term)\s*(?:actions?|next\s+steps?)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d4d94a6181c6a93cb38cb661faff8400:search

```yaml
regex_id: d4d94a6181c6a93cb38cb661faff8400
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/script-ecosystem-audit/scripts/checkers/code-quality.js:102:4"
```

### Pattern

`^\/\/\s+\w+.*\n\/\/\s+\w+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d4f209c03e95f90840070a305dbc433d:search

```yaml
regex_id: d4f209c03e95f90840070a305dbc433d
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/alerts/scripts/run-alerts.js:2229:37"
```

### Pattern

`^\s+[•·]\s+.+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d53324e8dfbfb57df5f44c96e0c74f5a:search

```yaml
regex_id: d53324e8dfbfb57df5f44c96e0c74f5a
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-docs-light.js:171:33"
```

### Pattern

`^(#{1,6})\s+(.{1,500})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d5aed896eaff56f08d80521ce6194715:search

```yaml
regex_id: d5aed896eaff56f08d80521ce6194715
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:152:21"
```

### Pattern

`\.(env|env\..+|config|cfg|ini|yaml|yml|json)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d5bd90ffaefb04d6100d6151649eb318:search

```yaml
regex_id: d5bd90ffaefb04d6100d6151649eb318
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/user-prompt-handler.js:445:4"
```

### Pattern

`^(?:i'?m\s+)?done\s*(?:for\s+(?:now|today))?\s*[.!]?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d654822312d08f0a4167fe9b673adbca:search

```yaml
regex_id: d654822312d08f0a4167fe9b673adbca
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:216:6"
```

### Pattern

`^#{1,4}\s*✅\s*(completed|resolved|done|fixed)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d698c0471799440916128b046b52db11:search

```yaml
regex_id: d698c0471799440916128b046b52db11
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/multi-ai/normalize-format.js:676:42"
```

### Pattern

`^([^.!?]+[.!?])`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d6b7c7f585914f5e0dbe22227e510b47:search

```yaml
regex_id: d6b7c7f585914f5e0dbe22227e510b47
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/archive-doc.js:573:29"
```

### Pattern

`^[A-Za-z]:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d730d452b7c0f92386dee80ad2e26ec4:search

```yaml
regex_id: d730d452b7c0f92386dee80ad2e26ec4
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:573:7"
```

### Pattern

`^#{2,5}\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d7bfe4b3e0bf4fc40e218dffd4af3b8f:search

```yaml
regex_id: d7bfe4b3e0bf4fc40e218dffd4af3b8f
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:102:6"
```

### Pattern

`^tsconfig\.json$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d80d5a39f2816af4c8e05b935033c275:search

```yaml
regex_id: d80d5a39f2816af4c8e05b935033c275
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/doc-ecosystem-audit/scripts/checkers/link-reference-integrity.js:487:10"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d82cfcad6f1a17e1214f70aae1ffdd53:search

```yaml
regex_id: d82cfcad6f1a17e1214f70aae1ffdd53
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:201:2"
```

### Pattern

`^scripts\/set-admin-claim\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d8306a8073dcf9bacab9c67c61268f22:search

```yaml
regex_id: d8306a8073dcf9bacab9c67c61268f22
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-cross-doc-deps.js:191:26"
```

### Pattern

`^[+-]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d875e26dccb1aab84c75d09ebacf766a:search

```yaml
regex_id: d875e26dccb1aab84c75d09ebacf766a
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:144:19"
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

## usage_mismatch:d8c3e356b3a88931db3416333f2b781f:search

```yaml
regex_id: d8c3e356b3a88931db3416333f2b781f
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-roadmap-debt.js:161:55"
```

### Pattern

`^\s*-\s*\[.\]\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d994a205f0f0330a7f54b4a08b716043:search

```yaml
regex_id: d994a205f0f0330a7f54b4a08b716043
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-roadmap-debt.js:225:8"
```

### Pattern

`^#{1,4}\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d9e08fc8a2270aff0c15773c2680be7f:search

```yaml
regex_id: d9e08fc8a2270aff0c15773c2680be7f
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-content-accuracy.js:503:34"
```

### Pattern

`^```(\w*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:db1ff832472a5ac1cdd437d5cc832d5b:search

```yaml
regex_id: db1ff832472a5ac1cdd437d5cc832d5b
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/lib/security-helpers.js:379:8"
```

### Pattern

`^(\d{1,3}\.){3}\d{1,3}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:db36f6cca926081f7ad1abe7296818ec:search

```yaml
regex_id: db36f6cca926081f7ad1abe7296818ec
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/archive/sync-reviews-to-jsonl.js:572:35"
```

### Pattern

`^- \*\*[^*]+\*\*.*?R\d+-R\d+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dceeec5427aaa6a67c809c8d5f08a14c:search

```yaml
regex_id: dceeec5427aaa6a67c809c8d5f08a14c
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/phase-complete-check.js:137:23"
```

### Pattern

`^\.\.(?:[/\\]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dd624aa44d1cbfff634799ea175feb19:search

```yaml
regex_id: dd624aa44d1cbfff634799ea175feb19
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:86:6"
```

### Pattern

`^functions\/src\/security\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dde36971a6633533d712a10d59914906:search

```yaml
regex_id: dde36971a6633533d712a10d59914906
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/user-prompt-handler.js:450:4"
```

### Pattern

`^(?:i'?m\s+)?(?:signing|logging)\s*off\s*[.!]?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:de6f300c45715f636b5d34762db8f88b:search

```yaml
regex_id: de6f300c45715f636b5d34762db8f88b
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:1856:17"
```

### Pattern

`(?:^|[\\/])check-pattern-compliance\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ded5420b0e8d21c4eb2e801e61d92425:search

```yaml
regex_id: ded5420b0e8d21c4eb2e801e61d92425
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/health-ecosystem-audit/scripts/checkers/coverage-completeness.js:103:10"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:df88ec1b825a2df4263f1d7c1920f580:search

```yaml
regex_id: df88ec1b825a2df4263f1d7c1920f580
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/lib/ai-pattern-checks.js:106:4"
```

### Pattern

`^[A-Za-z]:[\\/]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e0055e0d2b43645d1b2b7beba18f1eda:search

```yaml
regex_id: e0055e0d2b43645d1b2b7beba18f1eda
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/user-prompt-handler.js:456:4"
```

### Pattern

`^no(?:pe|thing)?\s*(?:,?\s*(?:that'?s?\s+)?(?:all|it))?\s*[.!]?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e1bc499e7629a8a1a08276c3d10ea0ff:search

```yaml
regex_id: e1bc499e7629a8a1a08276c3d10ea0ff
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/lib/security-helpers.js:241:16"
```

### Pattern

`^-+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e210f059e2b407d43179c4082c9eba4c:search

```yaml
regex_id: e210f059e2b407d43179c4082c9eba4c
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-review-needed.js:679:4"
```

### Pattern

`^(next\.config\.(js|mjs|ts)|webpack\.config\.js|vite\.config\.(js|ts)|rollup\.config\.(js|mjs))$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e2356fa0e53ce104e9805350bdeac328:search

```yaml
regex_id: e2356fa0e53ce104e9805350bdeac328
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:1266:17"
```

### Pattern

`(?:^|[\\/])check-pattern-compliance\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e299943ca938363eb7e3369d01ac80d1:search

```yaml
regex_id: e299943ca938363eb7e3369d01ac80d1
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:90:6"
```

### Pattern

`^storage\.rules$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e2bb1efca0a26760a610301ca4300a36:search

```yaml
regex_id: e2bb1efca0a26760a610301ca4300a36
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:182:2"
```

### Pattern

`^scripts\/assign-review-tier\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e2f57d7ba950fbcbe59fba576b9666a5:search

```yaml
regex_id: e2f57d7ba950fbcbe59fba576b9666a5
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/doc-ecosystem-audit/scripts/checkers/content-quality.js:109:32"
```

### Pattern

`^##\s+Version History`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e522bc9256c12d2351b219f0edd8cb80:search

```yaml
regex_id: e522bc9256c12d2351b219f0edd8cb80
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/lib/security-helpers.js:118:20"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e53459cdc66317666241593705bf14a5:search

```yaml
regex_id: e53459cdc66317666241593705bf14a5
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-context-debt.js:89:10"
```

### Pattern

`^(?:\/|[a-zA-Z]:\/)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e678d4a2811466d2fef0fb53cf1da72a:search

```yaml
regex_id: e678d4a2811466d2fef0fb53cf1da72a
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/aggregate-audit-findings.js:283:35"
```

### Pattern

`^## Category: (.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e6dbeb9114ee6835a2e29b0a475c9f13:search

```yaml
regex_id: e6dbeb9114ee6835a2e29b0a475c9f13
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:268:4"
```

### Pattern

`^(code\s+quality|performance|security)\s+(improvements?|enhancements?|metrics)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e7ad63770a7a186e82d3800d551da71c:search

```yaml
regex_id: e7ad63770a7a186e82d3800d551da71c
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-docs-light.js:286:4"
```

### Pattern

`^example$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e81c66c466e0391c9cc70d0f14e5c736:search

```yaml
regex_id: e81c66c466e0391c9cc70d0f14e5c736
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/user-prompt-handler.js:565:4"
```

### Pattern

`^(?:can\s+you\s+)?(?:quickly|just)\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e84d882f3eab1e353a817a93147620f3:search

```yaml
regex_id: e84d882f3eab1e353a817a93147620f3
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/lib/inline-patterns.js:36:17"
```

### Pattern

`session-start\.(?:sh|js)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e8653984838ef85bf493d2f7cde39bf2:search

```yaml
regex_id: e8653984838ef85bf493d2f7cde39bf2
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-doc-placement.js:65:6"
```

### Pattern

`^DEVELOPMENT\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e89bb128b92665721a6beed2c05e46df:search

```yaml
regex_id: e89bb128b92665721a6beed2c05e46df
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:206:4"
```

### Pattern

`^scripts\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e910148380b0d715e29773e026cd2d11:search

```yaml
regex_id: e910148380b0d715e29773e026cd2d11
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:208:2"
```

### Pattern

`^\.claude\/skills\/artifacts-builder\/scripts\/init-artifact\.sh$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e93203094d17df35516bd5b9e1f2b976:search

```yaml
regex_id: e93203094d17df35516bd5b9e1f2b976
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/lib/ai-pattern-checks.js:209:7"
```

### Pattern

`^[@.]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e93ebf1c5d394e63b483ab9b814ae7ee:search

```yaml
regex_id: e93ebf1c5d394e63b483ab9b814ae7ee
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-propagation.js:303:2"
```

### Pattern

`^-.*\bfunction\s+([a-zA-Z_$][a-zA-Z0-9_$]*)\s*\(`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e9b24add6aab776e94f37283ccad1d6f:search

```yaml
regex_id: e9b24add6aab776e94f37283ccad1d6f
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:247:4"
```

### Pattern

`^current\s+(architecture|state|status)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e9b7f92706de077059d64c67cb313d94:search

```yaml
regex_id: e9b7f92706de077059d64c67cb313d94
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-content-accuracy.js:371:21"
```

### Pattern

`^#\s+npm\s+run\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e9e0c144ddd0b50762bd28bd99662297:search

```yaml
regex_id: e9e0c144ddd0b50762bd28bd99662297
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:272:4"
```

### Pattern

`^(prioritized\s+)?action\s+(items?|plan)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e9ec2a955fb8d8a791f2755bca95bb51:search

```yaml
regex_id: e9ec2a955fb8d8a791f2755bca95bb51
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:719:8"
```

### Pattern

`^#{1,4}\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e9f4767a5c67728db73e850ae6fae3e8:search

```yaml
regex_id: e9f4767a5c67728db73e850ae6fae3e8
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/doc-ecosystem-audit/scripts/checkers/content-quality.js:91:25"
```

### Pattern

`^##\s+Purpose`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ea6f511d6f2297e15b7cf2acca7ddfff:search

```yaml
regex_id: ea6f511d6f2297e15b7cf2acca7ddfff
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:338:17"
```

### Pattern

`session-start\.(?:sh|js)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ea8a2fc70a4daa5d65972ec8a3267532:search

```yaml
regex_id: ea8a2fc70a4daa5d65972ec8a3267532
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:65:6"
```

### Pattern

`^public\/locales\/.*\.json$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:eac5d47c86fcd93e482f838e411d7b1f:search

```yaml
regex_id: eac5d47c86fcd93e482f838e411d7b1f
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:196:2"
```

### Pattern

`^scripts\/seed-.*\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:eb4f0ab9ab843d7edc7cc3719145cbc5:search

```yaml
regex_id: eb4f0ab9ab843d7edc7cc3719145cbc5
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:2042:32"
```

### Pattern

`^(?:\/|[A-Za-z]:[\\/]|\\\\|\/\/|\\(?!\\))`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:eb68febb351440bf93ce2b212d919df4:search

```yaml
regex_id: eb68febb351440bf93ce2b212d919df4
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:251:4"
```

### Pattern

`^table\s+of\s+contents`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:eba6129d4cc718e130393759619a72e0:search

```yaml
regex_id: eba6129d4cc718e130393759619a72e0
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:52:6"
```

### Pattern

`^\.github\/PULL_REQUEST_TEMPLATE\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ec551fb22bf224df346ca37efc25edfc:search

```yaml
regex_id: ec551fb22bf224df346ca37efc25edfc
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-doc-placement.js:88:13"
```

### Pattern

`PLAN\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ec6952f86f26837e3332e449092a59f4:search

```yaml
regex_id: ec6952f86f26837e3332e449092a59f4
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:270:4"
```

### Pattern

`^(feature\s+)?comparison\s+matrix`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ecd7660a3499f1c32ebf8b1c0f2930ff:search

```yaml
regex_id: ecd7660a3499f1c32ebf8b1c0f2930ff
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:104:6"
```

### Pattern

`^firestore\.indexes\.json$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ed69acde09e2f4b8e5bff3f3683238d2:search

```yaml
regex_id: ed69acde09e2f4b8e5bff3f3683238d2
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/hook-ecosystem-audit/scripts/checkers/cicd-pipeline.js:118:43"
```

### Pattern

`^run:\s+[^|]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ee1a002e765760f3d89f65d0bce80563:search

```yaml
regex_id: ee1a002e765760f3d89f65d0bce80563
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:88:6"
```

### Pattern

`^middleware\/.*\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ef09f8eb5d78fb0582773015a754199c:search

```yaml
regex_id: ef09f8eb5d78fb0582773015a754199c
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-cyclomatic-cc.js:313:29"
```

### Pattern

`^(.+?):(\d+):\d+:\s.*complexity of (\d+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ef347249d36ea63252984149d745d35e:search

```yaml
regex_id: ef347249d36ea63252984149d745d35e
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:835:12"
```

### Pattern

`^\w+,?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:efdb868bd99f8e1d24a311924cadea09:search

```yaml
regex_id: efdb868bd99f8e1d24a311924cadea09
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/post-write-validator.js:204:4"
```

### Pattern

`^app\/admin\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f09e5ce664aee1e75b5fc81001703a56:search

```yaml
regex_id: f09e5ce664aee1e75b5fc81001703a56
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/lib/ai-pattern-checks.js:246:6"
```

### Pattern

`^\.`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f13a879ac82da3aa88b5a86493621963:search

```yaml
regex_id: f13a879ac82da3aa88b5a86493621963
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-triggers.js:278:39"
```

### Pattern

`^####\s+Review\s+#(\d+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f15e67abf87b517792070517e44254b0:search

```yaml
regex_id: f15e67abf87b517792070517e44254b0
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/aggregate-audit-findings.js:710:8"
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

## usage_mismatch:f1837bb6d0e6f891b970a4df7bc6e421:search

```yaml
regex_id: f1837bb6d0e6f891b970a4df7bc6e421
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-triggers.js:181:4"
```

### Pattern

`^\.husky\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f257a9d99c6fd8d04b39195df059c8f0:search

```yaml
regex_id: f257a9d99c6fd8d04b39195df059c8f0
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/archive/sync-reviews-to-jsonl.js:832:25"
```

### Pattern

`^REVIEWS_\d+-\d+\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f2f0b2af5a74feebe7688d7113bd037d:search

```yaml
regex_id: f2f0b2af5a74feebe7688d7113bd037d
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/hooks/user-prompt-handler.js:452:4"
```

### Pattern

`^thanks?,?\s*(?:that'?s?\s+)?(?:all|it)\s*[.!]?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f3151edcfd9da456041ca335d099e5ea:search

```yaml
regex_id: f3151edcfd9da456041ca335d099e5ea
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/doc-ecosystem-audit/scripts/checkers/content-quality.js:306:10"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f3a61d7c13c49ce401c22d48253640ee:search

```yaml
regex_id: f3a61d7c13c49ce401c22d48253640ee
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/doc-ecosystem-audit/scripts/checkers/index-registry-health.js:221:43"
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

## usage_mismatch:f3aa43d925ce4989ad13264f7e5e43b9:search

```yaml
regex_id: f3aa43d925ce4989ad13264f7e5e43b9
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:51:6"
```

### Pattern

`^\.vscode\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f3f8ded7e2825cfae110a919128ce351:search

```yaml
regex_id: f3f8ded7e2825cfae110a919128ce351
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/reviews/lib/parse-review.ts:50:16"
```

### Pattern

`\((\d{4}-\d{2}-\d{2})\)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f5058c8f79453796d732b9c44a104017:search

```yaml
regex_id: f5058c8f79453796d732b9c44a104017
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-doc-placement.js:307:6"
```

### Pattern

`PLAN\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f578c624861772c94274005e7f280e01:search

```yaml
regex_id: f578c624861772c94274005e7f280e01
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:55:29"
```

### Pattern

`^package-lock\.json$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f5e6cde76a96d5e032f658a8611e036b:search

```yaml
regex_id: f5e6cde76a96d5e032f658a8611e036b
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:50:6"
```

### Pattern

`\.log$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f68de2fef3749a61c4156e6f41ab2981:search

```yaml
regex_id: f68de2fef3749a61c4156e6f41ab2981
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:282:4"
```

### Pattern

`^not\s+in\s+(technical\s+)?roadmap`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f6e7c6d7d43e8c18c03cd413ec817cdb:search

```yaml
regex_id: f6e7c6d7d43e8c18c03cd413ec817cdb
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:85:6"
```

### Pattern

`^functions\/src\/auth\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f70c9c0a28a8a2f9dd4720780ceda654:search

```yaml
regex_id: f70c9c0a28a8a2f9dd4720780ceda654
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-docs-light.js:284:4"
```

### Pattern

`^filename$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f74c547cae89c41e37d57cc8d48c229f:search

```yaml
regex_id: f74c547cae89c41e37d57cc8d48c229f
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:362:41"
```

### Pattern

`^line$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f8bcc477968020e146fc15cda6fe279e:search

```yaml
regex_id: f8bcc477968020e146fc15cda6fe279e
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:267:4"
```

### Pattern

`^for\s+each\s+fix`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f95a1c50e6063e0780dbff1ab4183630:search

```yaml
regex_id: f95a1c50e6063e0780dbff1ab4183630
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-content-accuracy.js:241:4"
```

### Pattern

`\/(file|X)\.\w+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f9907df72d925daec518a5fd780d9389:search

```yaml
regex_id: f9907df72d925daec518a5fd780d9389
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-propagation.js:293:2"
```

### Pattern

`^\+.*\bfunction\s+([a-zA-Z_$][a-zA-Z0-9_$]*)\s*\(`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fa405fe4a2acb2a7ac476344cebfa3e3:search

```yaml
regex_id: fa405fe4a2acb2a7ac476344cebfa3e3
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/assign-review-tier.js:105:6"
```

### Pattern

`^lib\/firebase-config\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fa5ecb159115e60594ec5c5969920680:search

```yaml
regex_id: fa5ecb159115e60594ec5c5969920680
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:249:4"
```

### Pattern

`^reference`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fb10643871e95901e764339d100cd012:search

```yaml
regex_id: fb10643871e95901e764339d100cd012
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/multi-ai/normalize-format.js:670:36"
```

### Pattern

`^\*\*([^*]+)\*\*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fb4ea7de8d7b12bc35ad98e674fca85c:search

```yaml
regex_id: fb4ea7de8d7b12bc35ad98e674fca85c
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/lib/ai-pattern-checks.js:238:33"
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

## usage_mismatch:fb76fbaf95a02441b9b70688ac777632:search

```yaml
regex_id: fb76fbaf95a02441b9b70688ac777632
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/health-ecosystem-audit/scripts/checkers/checker-infrastructure.js:80:10"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fbbccd9c1f43b30c06277f7edc0675b6:search

```yaml
regex_id: fbbccd9c1f43b30c06277f7edc0675b6
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:590:17"
```

### Pattern

`(?:^|[\\/])(?:check-pattern-compliance|inline-patterns|check-pattern-sync)\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fc51918b046855aedf6ece22334ab6fb:search

```yaml
regex_id: fc51918b046855aedf6ece22334ab6fb
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:1704:17"
```

### Pattern

`(?:^|[\\/])check-pattern-compliance\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fca82177060c976e39766103897d751e:search

```yaml
regex_id: fca82177060c976e39766103897d751e
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/debt/extract-audit-reports.js:242:4"
```

### Pattern

`^background$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fca83ec905e03c800fc31823d981bb8c:search

```yaml
regex_id: fca83ec905e03c800fc31823d981bb8c
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-doc-placement.js:55:48"
```

### Pattern

`^ARCHITECTURE\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fcd2e13ba5634c2e97c9534dfcade6cd:search

```yaml
regex_id: fcd2e13ba5634c2e97c9534dfcade6cd
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:807:17"
```

### Pattern

`(?:^|[\\/])check-pattern-compliance\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fd121d3de4c3574991d8dbf0ceb66c97:search

```yaml
regex_id: fd121d3de4c3574991d8dbf0ceb66c97
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-docs-light.js:735:10"
```

### Pattern

`^PHASE_\d+[A-Z]?_AUDIT\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fd7328372c9520fd58c4f5e2efa9a722:search

```yaml
regex_id: fd7328372c9520fd58c4f5e2efa9a722
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:193:2"
```

### Pattern

`^scripts\/archive-doc\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fdc4459547a2f21b7a5c8eae773a4eb1:search

```yaml
regex_id: fdc4459547a2f21b7a5c8eae773a4eb1
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:1456:17"
```

### Pattern

`(?:^|[\\/])check-pattern-compliance\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fdd47ce444ac90c1af2f88a15e00a464:search

```yaml
regex_id: fdd47ce444ac90c1af2f88a15e00a464
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/.claude/skills/alerts/scripts/run-alerts.js:3487:39"
```

### Pattern

`^\s{2,}-\s+\S`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ff95d3fcb4fcc98e3a09f1f887fe4cb0:search

```yaml
regex_id: ff95d3fcb4fcc98e3a09f1f887fe4cb0
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-pattern-compliance.js:187:2"
```

### Pattern

`^scripts\/normalize-canon-ids\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ffeddd739d12d1c5ffec07febf6958e0:search

```yaml
regex_id: ffeddd739d12d1c5ffec07febf6958e0
schema_version: "1"
kind: usage_mismatch
corpus: sonash-v0
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/sonash-v0/rules/scripts/check-content-accuracy.js:300:12"
```

### Pattern

`^\.\.(?:[\\/]|$)`

### Context

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
corpus: sonash-v0
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
corpus: sonash-v0
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
corpus: sonash-v0
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
corpus: sonash-v0
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

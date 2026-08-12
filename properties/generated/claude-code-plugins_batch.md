---
schema_version: "1"
corpus: claude-code-plugins
findings: 429
---

# claude-code-plugins batch findings

## usage_mismatch:006a648ea7dfc35bd9ae4bbd127a5ade:search

```yaml
regex_id: 006a648ea7dfc35bd9ae4bbd127a5ade
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/github/github.test.sh:144:5"
```

### Pattern

`^## (Cost-control levers|Posture heuristics)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:009870e069ba62b20210c00f3f67118a:search

```yaml
regex_id: 009870e069ba62b20210c00f3f67118a
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-ops/skills/lanes/scripts/restart-consumer.sh:416:2"
```

### Pattern

`^[A-Za-z0-9._-]+/[A-Za-z0-9._-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:00c3f31500532beeb5e1080c972db827:search

```yaml
regex_id: 00c3f31500532beeb5e1080c972db827
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/go-format/hooks/hook-utils.sh:574:9"
```

### Pattern

`^[0-9]+(\.[0-9]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:00f517bf36616a31d0ff3a2204934a1d:search

```yaml
regex_id: 00f517bf36616a31d0ff3a2204934a1d
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/work-items/tools/work-item-tracker/adapters/jira/list-items.test.sh:36:10"
```

### Pattern

`^--data$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:01c501564786d4f8341cbeea13359502:search

```yaml
regex_id: 01c501564786d4f8341cbeea13359502
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/code-tidying/skills/audit-comment-residue/scripts/lib/comment-shapes.sh:46:2"
```

### Pattern

`^[[:space:]]*#!`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:026cb0a36dec79907bc5ed4b333b5533:search

```yaml
regex_id: 026cb0a36dec79907bc5ed4b333b5533
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/eol-normalizer/hooks/hook-utils.sh:1485:22"
```

### Pattern

`^[0-9]+([.][0-9]+)?(s|m|h|d)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:027fe3ab9a2793f89e1ea1d968d00652:search

```yaml
regex_id: 027fe3ab9a2793f89e1ea1d968d00652
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-config/lib/state-key.sh:145:31"
```

### Pattern

`^[a-z0-9][a-z0-9._-]*(/[a-z0-9][a-z0-9._-]*)*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:02e98295e8a0e6f48c8adcb33fa8954b:search

```yaml
regex_id: 02e98295e8a0e6f48c8adcb33fa8954b
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/autonomy/hooks/hook-utils.sh:576:9"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:035918e77b818f6de827849ed7011d68:search

```yaml
regex_id: 035918e77b818f6de827849ed7011d68
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/bash-format/hooks/hook-utils.sh:629:60"
```

### Pattern

`^0+\.0+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0368b679c5f926de72486106819fbb4e:search

```yaml
regex_id: 0368b679c5f926de72486106819fbb4e
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/typos-format/hooks/hook-utils.sh:574:46"
```

### Pattern

`^0+(\.0+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:044dc54c0869d0201f08a0be2231113e:search

```yaml
regex_id: 044dc54c0869d0201f08a0be2231113e
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-ops/skills/lanes/scripts/telemetry-upsert.sh:231:0"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:054168e4644a3f49762ed632aeb27ae6:search

```yaml
regex_id: 054168e4644a3f49762ed632aeb27ae6
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-hygiene/skills/clean/scripts/preflight.sh:50:42"
```

### Pattern

`^(dotnet|aspire|node|devenv|rider64?|fleet)\.exe`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:05f76dcf74fa02b53d2cb5ddb26b8475:search

```yaml
regex_id: 05f76dcf74fa02b53d2cb5ddb26b8475
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/actionlint/hooks/hook-utils.sh:1770:11"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:093639cf3238b5255969a3b705d44937:search

```yaml
regex_id: 093639cf3238b5255969a3b705d44937
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/bash-format/hooks/bash-format.test.sh:194:5"
```

### Pattern

`^echo hi$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:099871657c1f6424fdd5581987900818:search

```yaml
regex_id: 099871657c1f6424fdd5581987900818
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/github/github.test.sh:151:11"
```

### Pattern

`^## Audit-question checklist$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0a1c3b303b8ac3179028e25b641e335a:search

```yaml
regex_id: 0a1c3b303b8ac3179028e25b641e335a
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/desktop-notification/hooks/hook-utils.sh:1770:11"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0a23cffacf707caa231dab574224de87:search

```yaml
regex_id: 0a23cffacf707caa231dab574224de87
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/typos-format/hooks/hook-utils.sh:1485:22"
```

### Pattern

`^[0-9]+([.][0-9]+)?(s|m|h|d)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0ab59afc73a3e194bf408ae530a30fee:search

```yaml
regex_id: 0ab59afc73a3e194bf408ae530a30fee
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/cli-flag-verify.sh:247:11"
```

### Pattern

`^(--[a-zA-Z][a-zA-Z0-9-]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0c0b00157505b4c76c7460c1157d59b3:search

```yaml
regex_id: 0c0b00157505b4c76c7460c1157d59b3
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/biome-format/hooks/hook-utils.sh:1770:11"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0d1ce6bb65fe465ebcf5bfd86405ce2f:search

```yaml
regex_id: 0d1ce6bb65fe465ebcf5bfd86405ce2f
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/hooks/hook-utils.sh:576:9"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0d65953e3b4b6fe4846975b92e26ea2f:search

```yaml
regex_id: 0d65953e3b4b6fe4846975b92e26ea2f
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/lib/powershell/ps-command.sh:687:4"
```

### Pattern

`^[0-9]+([.][0-9]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0d67cb67a02b7b4057f643b055524e71:search

```yaml
regex_id: 0d67cb67a02b7b4057f643b055524e71
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-fleet-hygiene/skills/audit/scripts/audit-fleet.test.sh:917:0"
```

### Pattern

`^[[:space:]]*#`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:104362856ac2e9dd133edfcdbfd2ee66:search

```yaml
regex_id: 104362856ac2e9dd133edfcdbfd2ee66
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/stale-path-verify.sh:233:55"
```

### Pattern

`^[[:space:]]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:109983acc0853da68ea82393d638c8ff:search

```yaml
regex_id: 109983acc0853da68ea82393d638c8ff
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-ops/skills/plugins/scripts/fleet-state.test.sh:941:21"
```

### Pattern

`^[[:space:]]*#`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:112470580567d99b950d5f155de4de37:search

```yaml
regex_id: 112470580567d99b950d5f155de4de37
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/ruff-format/hooks/hook-utils.sh:1348:18"
```

### Pattern

`^-[i0v](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:11a94a6041ad32544407482b13a7687f:search

```yaml
regex_id: 11a94a6041ad32544407482b13a7687f
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/context-guard/hooks/hook-utils.sh:574:46"
```

### Pattern

`^0+(\.0+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:11c80d2ce1fe53be517dbdad593f4eec:search

```yaml
regex_id: 11c80d2ce1fe53be517dbdad593f4eec
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-ops/hooks/hook-utils.sh:950:5"
```

### Pattern

`^[a-zA-Z_][a-zA-Z0-9_]*(\[.*\])?\+?=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:138e56cd79b9e0c188688cc01f2d83fc:search

```yaml
regex_id: 138e56cd79b9e0c188688cc01f2d83fc
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/desktop-notification/hooks/hook-utils.sh:950:5"
```

### Pattern

`^[a-zA-Z_][a-zA-Z0-9_]*(\[.*\])?\+?=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:13df3cfb887bbbad0bbc3d9af986a05c:search

```yaml
regex_id: 13df3cfb887bbbad0bbc3d9af986a05c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/autonomy/hooks/hook-utils.sh:629:60"
```

### Pattern

`^0+\.0+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1421e1c6aaa9e7a9f1fba0a5305afc1d:search

```yaml
regex_id: 1421e1c6aaa9e7a9f1fba0a5305afc1d
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/context-guard/hooks/zone-gate.sh:60:0"
```

### Pattern

`^[A-Za-z0-9_-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:14735d7c3dbf338ef4f8065be6060640:search

```yaml
regex_id: 14735d7c3dbf338ef4f8065be6060640
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/skill-quality/scripts/check-skill.sh:624:32"
```

### Pattern

`^metadata:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:152a3b0a117b1dc39a6f327bcec83b9b:search

```yaml
regex_id: 152a3b0a117b1dc39a6f327bcec83b9b
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/biome-format/hooks/hook-utils.sh:1485:22"
```

### Pattern

`^[0-9]+([.][0-9]+)?(s|m|h|d)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:15a5fb4df4e6d7e82b6bc19f65b02f0c:search

```yaml
regex_id: 15a5fb4df4e6d7e82b6bc19f65b02f0c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/cli-flag-verify.sh:210:11"
```

### Pattern

`^[A-Za-z_][A-Za-z0-9_]*=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1678b2349038a3a7d3ec1d2a3a05a57c:search

```yaml
regex_id: 1678b2349038a3a7d3ec1d2a3a05a57c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/work-items/tools/work-item-tracker/adapters/local-markdown/renew-lease.sh:27:0"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:174312eedcb2a03159c440f0530c4410:search

```yaml
regex_id: 174312eedcb2a03159c440f0530c4410
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/eol-normalizer/hooks/hook-utils.sh:629:60"
```

### Pattern

`^0+\.0+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:185d7b2d743c7e05538c3413d6181dc9:search

```yaml
regex_id: 185d7b2d743c7e05538c3413d6181dc9
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/eol-normalizer/hooks/hook-utils.sh:574:46"
```

### Pattern

`^0+(\.0+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:189e31e8132ec0fbe67d3b27eb4b0487:search

```yaml
regex_id: 189e31e8132ec0fbe67d3b27eb4b0487
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/markdown-format.test.sh:2368:25"
```

### Pattern

`^\* star item$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:196bcb592670f49f98bbaa81262b3701:search

```yaml
regex_id: 196bcb592670f49f98bbaa81262b3701
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/skill-reference-verify.sh:629:57"
```

### Pattern

`^[[:space:]]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:19ab177699a9c898fad64c81292e4208:search

```yaml
regex_id: 19ab177699a9c898fad64c81292e4208
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/typos-format/hooks/hook-utils.sh:621:5"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1a4e83f59ff14a2808d230bed990c993:search

```yaml
regex_id: 1a4e83f59ff14a2808d230bed990c993
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-hygiene/skills/clean/scripts/git-branch-audit.sh:57:81"
```

### Pattern

`^branch`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1a8d36618f3bf077a2096583fa27584c:search

```yaml
regex_id: 1a8d36618f3bf077a2096583fa27584c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/bash-format/hooks/bash-format.test.sh:259:5"
```

### Pattern

`^echo hi$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1aafb51551dc5b5cd005afe028b61064:search

```yaml
regex_id: 1aafb51551dc5b5cd005afe028b61064
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/eol-normalizer/hooks/hook-utils.sh:574:9"
```

### Pattern

`^[0-9]+(\.[0-9]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1bc84c645907b43376096a0013793623:search

```yaml
regex_id: 1bc84c645907b43376096a0013793623
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-hygiene/skills/clean/scripts/lib/cleanup-paths.test.sh:90:80"
```

### Pattern

`^git `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1c70a76afc2e86eea34b3d1abd019e55:search

```yaml
regex_id: 1c70a76afc2e86eea34b3d1abd019e55
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/hooks/hook-utils.sh:1439:22"
```

### Pattern

`^-?[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1e448c42bf4f2855dbff1e5b6b27bc75:search

```yaml
regex_id: 1e448c42bf4f2855dbff1e5b6b27bc75
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/markdown-format.test.sh:486:32"
```

### Pattern

`^- star item$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1e44e78581b2dbacadb388612ce8b94c:search

```yaml
regex_id: 1e44e78581b2dbacadb388612ce8b94c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/go-format/hooks/hook-utils.sh:1770:11"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1e4cfcc7991b7053e6327f571da8c476:search

```yaml
regex_id: 1e4cfcc7991b7053e6327f571da8c476
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/cli-flag-verify.sh:177:34"
```

### Pattern

`^[[:space:]]*#`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1f99f035ba06405f709c9a487cd2b438:search

```yaml
regex_id: 1f99f035ba06405f709c9a487cd2b438
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/lib/hook-utils.sh:621:5"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1fe5989437afb26ef607327a85b3addc:search

```yaml
regex_id: 1fe5989437afb26ef607327a85b3addc
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-memory/skills/audit/scripts/orphan-rule-check.sh:80:22"
```

### Pattern

`^paths:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:205aa1e5f3f203380183ca91c83b2e18:search

```yaml
regex_id: 205aa1e5f3f203380183ca91c83b2e18
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/actionlint/hooks/hook-utils.sh:621:5"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:20d855999a87b74a04ef853f5c938825:search

```yaml
regex_id: 20d855999a87b74a04ef853f5c938825
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/context-guard/scripts/context-zone.sh:100:0"
```

### Pattern

`^[A-Za-z0-9_-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:219223ae05bbc9353cd14b226132201c:search

```yaml
regex_id: 219223ae05bbc9353cd14b226132201c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-config/skills/audit-permission-grants/scripts/permission-rule-check.sh:380:6"
```

### Pattern

`(^|/)\.claude/commands/[^/]+\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:22145782b6509b8383b75822dbcfc416:search

```yaml
regex_id: 22145782b6509b8383b75822dbcfc416
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/autonomy/hooks/hook-utils.sh:1348:18"
```

### Pattern

`^-[i0v](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2298112bdb5502c42fa694b288638a65:search

```yaml
regex_id: 2298112bdb5502c42fa694b288638a65
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/context-guard/scripts/statusline-tee.sh:129:2"
```

### Pattern

`^[A-Za-z0-9_-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:23a5b186376b77c31b6b9d947052925c:search

```yaml
regex_id: 23a5b186376b77c31b6b9d947052925c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-hygiene/skills/clean/scripts/clean-batch.test.sh:336:32"
```

### Pattern

`^GITDIR	`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:23c3bc5ede01ef684610eac38d934acb:search

```yaml
regex_id: 23c3bc5ede01ef684610eac38d934acb
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-hygiene/skills/clean/scripts/lib/clean-common.sh:651:4"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2517ff86dfac244211415088a4402908:search

```yaml
regex_id: 2517ff86dfac244211415088a4402908
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/require-jq-posture.test.sh:76:5"
```

### Pattern

`^MAX_COMMAND_LEN=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2556e639c381f12d27077bc8261c7dde:search

```yaml
regex_id: 2556e639c381f12d27077bc8261c7dde
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-fleet-hygiene/skills/audit/scripts/audit-fleet.sh:751:52"
```

### Pattern

`^$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:255fff117e53ce97d7a1d4a573dd663e:search

```yaml
regex_id: 255fff117e53ce97d7a1d4a573dd663e
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/rate-limit-guard/hooks/hook-utils.sh:574:46"
```

### Pattern

`^0+(\.0+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2649acf68564e6a3eb054174d1fe66ea:search

```yaml
regex_id: 2649acf68564e6a3eb054174d1fe66ea
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/mcp-tools/skills/audit/scripts/discover.sh:210:36"
```

### Pattern

`^[[:space:]]*(public|private|internal|protected).*[[:alnum:]_][[:alnum:]_]*[[:space:]]*\(`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:267300357224f4fe32d5afdd5ac03edd:search

```yaml
regex_id: 267300357224f4fe32d5afdd5ac03edd
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/rate-limit-guard/hooks/record-rate-limit-stop.test.sh:78:37"
```

### Pattern

`^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:26a236f5843593993ab8dbc256c3c01c:search

```yaml
regex_id: 26a236f5843593993ab8dbc256c3c01c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/hooks/pr-linkage-validator.sh:129:7"
```

### Pattern

`^#+[[:space:]]+[^[:space:]]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2768863a40142650644fbfbeb6f92fba:search

```yaml
regex_id: 2768863a40142650644fbfbeb6f92fba
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-config/skills/audit-permission-state/scripts/permission-merge.test.sh:195:28"
```

### Pattern

`^inert `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:27d7e6df87a9f228596c9f7a4e14825a:search

```yaml
regex_id: 27d7e6df87a9f228596c9f7a4e14825a
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/autonomy/hooks/lane-stop-gate-arm.sh:136:0"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:28244237a39d9611b5bd82fd0bcb0327:search

```yaml
regex_id: 28244237a39d9611b5bd82fd0bcb0327
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/scripts/check-changelog-parity.sh:236:4"
```

### Pattern

`^##[[:space:]]+\[?[0-9]+\.[0-9]+(\.[0-9]+)?([+-][0-9A-Za-z][0-9A-Za-z.-]*)?\]?(\(|$|[[:space:]])`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:286f670f89463f940aee290d37a5b03b:search

```yaml
regex_id: 286f670f89463f940aee290d37a5b03b
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/autonomy/hooks/lane-notify.test.sh:86:8"
```

### Pattern

`^PROG<<`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2881ae55ddd1df88c4ad3c1a2cfb81d4:search

```yaml
regex_id: 2881ae55ddd1df88c4ad3c1a2cfb81d4
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-hygiene/skills/clean/scripts/clean-batch.test.sh:322:9"
```

### Pattern

`^GITDIR	`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:297ebde9f4feec0191f6227b17da5bec:search

```yaml
regex_id: 297ebde9f4feec0191f6227b17da5bec
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/skills/commit/scripts/exec-bit-check.test.sh:686:73"
```

### Pattern

`^C`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2a201b94045a09a8efbc415357908c98:search

```yaml
regex_id: 2a201b94045a09a8efbc415357908c98
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/context-guard/hooks/hook-utils.sh:1348:18"
```

### Pattern

`^-[i0v](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2a2e07e8283a74ec14b933088078ca39:search

```yaml
regex_id: 2a2e07e8283a74ec14b933088078ca39
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/desktop-notification/hooks/desktop-notification.test.sh:372:8"
```

### Pattern

`^PROG<<`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2a67e63c56aaf1f7136b7568bc56b6dc:search

```yaml
regex_id: 2a67e63c56aaf1f7136b7568bc56b6dc
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/hooks/hook-utils.sh:574:46"
```

### Pattern

`^0+(\.0+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2ac1970ae2c8c61902cf41fd12d80588:search

```yaml
regex_id: 2ac1970ae2c8c61902cf41fd12d80588
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-fleet-hygiene/skills/audit/scripts/audit-fleet.test.sh:836:5"
```

### Pattern

`^(Repo|Canonical): $(printf '%s' `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2c1bb4d89d242b4405e5af4e6109081a:search

```yaml
regex_id: 2c1bb4d89d242b4405e5af4e6109081a
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/hook-utils.sh:950:5"
```

### Pattern

`^[a-zA-Z_][a-zA-Z0-9_]*(\[.*\])?\+?=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2c837f28b0648d0e30667a0d914bfbf9:search

```yaml
regex_id: 2c837f28b0648d0e30667a0d914bfbf9
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/hook-utils.sh:1439:22"
```

### Pattern

`^-?[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2ca932323f671f297fe4542c2e89cd7c:search

```yaml
regex_id: 2ca932323f671f297fe4542c2e89cd7c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/bash-format/hooks/bash-format.test.sh:246:5"
```

### Pattern

`^echo hi$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2cab44f40fb0080b2c1351afa30d155a:search

```yaml
regex_id: 2cab44f40fb0080b2c1351afa30d155a
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/autonomy/hooks/hook-utils.sh:1485:22"
```

### Pattern

`^[0-9]+([.][0-9]+)?(s|m|h|d)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2cdc46d811a13de4ced3b114d2b5cf89:search

```yaml
regex_id: 2cdc46d811a13de4ced3b114d2b5cf89
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/discovery/scripts/check-coverage-complete.sh:36:2"
```

### Pattern

`^# Deterministic gate`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2ce4a4d965c6c3572d541a6c982635bc:search

```yaml
regex_id: 2ce4a4d965c6c3572d541a6c982635bc
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/github/github.test.sh:111:30"
```

### Pattern

`^\| `[a-z0-9-]+``

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2d39a5b558def5038bf5398d1ed66a5a:search

```yaml
regex_id: 2d39a5b558def5038bf5398d1ed66a5a
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/eol-normalizer/hooks/hook-utils.sh:1348:18"
```

### Pattern

`^-[i0v](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2e136608e6ea2a46e722ecfbab09898d:search

```yaml
regex_id: 2e136608e6ea2a46e722ecfbab09898d
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/docs-hygiene/skills/audit-encapsulation/scripts/detect.sh:149:7"
```

### Pattern

`^\.claude/skills/([^/]+)/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2e56eefd6b987edc16589e656082b844:search

```yaml
regex_id: 2e56eefd6b987edc16589e656082b844
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/powershell-format/hooks/hook-utils.sh:1770:11"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2e764775a197ecae3a0c1b30553600c6:search

```yaml
regex_id: 2e764775a197ecae3a0c1b30553600c6
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-hygiene/skills/clean/scripts/git-branch-audit.sh:59:115"
```

### Pattern

`^${DEFAULT_BRANCH}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2e94a61886fc1a468955dc72a6d17f7c:search

```yaml
regex_id: 2e94a61886fc1a468955dc72a6d17f7c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/resolve-convention-pattern.sh:127:10"
```

### Pattern

`^${k}:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2eab3272c5408e3636a8374260654b3c:search

```yaml
regex_id: 2eab3272c5408e3636a8374260654b3c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/go-format/hooks/hook-utils.sh:574:46"
```

### Pattern

`^0+(\.0+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2ec15c83de989020cc52c6859412623f:search

```yaml
regex_id: 2ec15c83de989020cc52c6859412623f
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/lib/hook-utils.sh:1485:22"
```

### Pattern

`^[0-9]+([.][0-9]+)?(s|m|h|d)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2ef406418afe2e3c3977f984021267ef:search

```yaml
regex_id: 2ef406418afe2e3c3977f984021267ef
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/lib/hook-utils.sh:1770:11"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:314dde7d13f2449f669ee7910ced4381:search

```yaml
regex_id: 314dde7d13f2449f669ee7910ced4381
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-fleet-hygiene/skills/audit/scripts/audit-fleet.sh:749:40"
```

### Pattern

`^$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:31d8b23136fc4416389e1a8fbda9eb6f:search

```yaml
regex_id: 31d8b23136fc4416389e1a8fbda9eb6f
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/rate-limit-guard/hooks/hook-utils.sh:950:5"
```

### Pattern

`^[a-zA-Z_][a-zA-Z0-9_]*(\[.*\])?\+?=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:31e6c2bd2808541adcf995f54eb9bb70:search

```yaml
regex_id: 31e6c2bd2808541adcf995f54eb9bb70
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/typos-format/hooks/typos-format.sh:459:0"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:32171536cd7f44fed0437018e5fb59e6:search

```yaml
regex_id: 32171536cd7f44fed0437018e5fb59e6
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/docs-hygiene/skills/audit-noise/scripts/lib/noise-shapes.sh:101:5"
```

### Pattern

`^[[:space:]]*-[[:space:]]+\`?/[a-z][a-z0-9_-]*\`?[[:space:]]—`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:32410d99e2962d45f96cdb98cabfb296:search

```yaml
regex_id: 32410d99e2962d45f96cdb98cabfb296
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/skill-quality/scripts/check-skill.sh:497:28"
```

### Pattern

`^[^[:space:]]+:[0-9]+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:334998b7b8deafd606a35f7274535df3:search

```yaml
regex_id: 334998b7b8deafd606a35f7274535df3
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/ruff-format/hooks/hook-utils.sh:950:5"
```

### Pattern

`^[a-zA-Z_][a-zA-Z0-9_]*(\[.*\])?\+?=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3354e302d0d658c6aa460e4395308f2c:search

```yaml
regex_id: 3354e302d0d658c6aa460e4395308f2c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/actionlint/hooks/hook-utils.sh:1348:18"
```

### Pattern

`^-[i0v](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:339a9cb953b08f8c3da28e814664b016:search

```yaml
regex_id: 339a9cb953b08f8c3da28e814664b016
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/lib/hook-utils.sh:1348:18"
```

### Pattern

`^-[i0v](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:33cd0291c5306103adf11a5d6b6d47ca:search

```yaml
regex_id: 33cd0291c5306103adf11a5d6b6d47ca
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/planning/scripts/check-open-questions.sh:138:5"
```

### Pattern

`^[[:space:]]*(\`\`\`|~~~)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3410883cd88af2894a91341a5da384a8:search

```yaml
regex_id: 3410883cd88af2894a91341a5da384a8
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/typos-format/hooks/hook-utils.sh:1770:11"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3413620650f1bbe75603676da2e0dd47:search

```yaml
regex_id: 3413620650f1bbe75603676da2e0dd47
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-fleet-hygiene/skills/audit/scripts/audit-fleet.sh:79:5"
```

### Pattern

`^[[:print:]]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:34f57fee979d73b281d3a4ad47a9a77b:search

```yaml
regex_id: 34f57fee979d73b281d3a4ad47a9a77b
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/typos-format/hooks/typos-format.sh:460:0"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3740f0b3cd204849dd454ebb4fa5f7a6:search

```yaml
regex_id: 3740f0b3cd204849dd454ebb4fa5f7a6
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/block-no-verify.sh:208:4"
```

### Pattern

`^(${HM_ALT})[_a-z0-9]*=(0|false)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:375e4a19c24c5b403be61f1a9cb96f11:search

```yaml
regex_id: 375e4a19c24c5b403be61f1a9cb96f11
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/plugin-quality/scripts/packet-prune.sh:109:0"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:37c52170ce396d2a7ac87e43296526df:search

```yaml
regex_id: 37c52170ce396d2a7ac87e43296526df
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/autonomy/hooks/lane-stop-gate.sh:227:2"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:37fc753c2ac03fbbab721d2a305f824d:search

```yaml
regex_id: 37fc753c2ac03fbbab721d2a305f824d
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/scripts/check-skill-portability.sh:160:5"
```

### Pattern

`^[[:space:]]*(#|((>|[-*+]|[0-9]+[.)])[[:space:]]+)*<!--)[[:space:]]*portability-scope:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:38fe52eccdb4074d17b442efa49d333b:search

```yaml
regex_id: 38fe52eccdb4074d17b442efa49d333b
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/go-format/hooks/hook-utils.sh:576:9"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3996c4edcd8ea6d582f91b597bb3c073:search

```yaml
regex_id: 3996c4edcd8ea6d582f91b597bb3c073
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/discovery/agents/tool-honesty.test.sh:158:21"
```

### Pattern

`^(scope|topic)_as_received: `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:39b3d673edac2178e8876ed3b8a59316:search

```yaml
regex_id: 39b3d673edac2178e8876ed3b8a59316
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/scripts/worktree-create.sh:413:7"
```

### Pattern

`^[A-Za-z]:/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:39b465e6baeeaa552bbd0003905b07cf:search

```yaml
regex_id: 39b465e6baeeaa552bbd0003905b07cf
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/rate-limit-guard/hooks/hook-utils.sh:1485:22"
```

### Pattern

`^[0-9]+([.][0-9]+)?(s|m|h|d)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:39dfe768481b5809646f03df722f4ccc:search

```yaml
regex_id: 39dfe768481b5809646f03df722f4ccc
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/rate-limit-guard/hooks/hook-utils.sh:1770:11"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3a23d072ae9c10707bc7cd37c1af4871:search

```yaml
regex_id: 3a23d072ae9c10707bc7cd37c1af4871
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/skill-quality/scripts/check-skill.sh:631:16"
```

### Pattern

`^metadata:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3a6aa5ecb7b4958d1f976f33d07318e4:search

```yaml
regex_id: 3a6aa5ecb7b4958d1f976f33d07318e4
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/wizard/skills/generate/template.sh:145:2"
```

### Pattern

`^[Yy]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3b32f170c2fdde4807c2ca39e8861aa8:search

```yaml
regex_id: 3b32f170c2fdde4807c2ca39e8861aa8
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/biome-format/hooks/hook-utils.sh:950:5"
```

### Pattern

`^[a-zA-Z_][a-zA-Z0-9_]*(\[.*\])?\+?=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3b9b8f4156f847205ebbe62efd08d881:search

```yaml
regex_id: 3b9b8f4156f847205ebbe62efd08d881
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/hooks/hook-utils.sh:1485:22"
```

### Pattern

`^[0-9]+([.][0-9]+)?(s|m|h|d)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3c372a46e79706511a866755329fc469:search

```yaml
regex_id: 3c372a46e79706511a866755329fc469
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/scripts/affected-tests.sh:206:2"
```

### Pattern

`^copies=(`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3c94dc3f464f6d55649b13acccdc338c:search

```yaml
regex_id: 3c94dc3f464f6d55649b13acccdc338c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/biome-format/hooks/hook-utils.sh:574:46"
```

### Pattern

`^0+(\.0+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3ce7e23db11b0c60f59b398710ce5c3f:search

```yaml
regex_id: 3ce7e23db11b0c60f59b398710ce5c3f
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/autonomy/hooks/hook-utils.sh:621:5"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3d2dc07a3b2992f61828ea4c108cca7b:search

```yaml
regex_id: 3d2dc07a3b2992f61828ea4c108cca7b
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/work-items/tools/work-item-tracker/lib/binding.sh:44:2"
```

### Pattern

`^[a-zA-Z0-9_-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3ed944d4c5fb206d794a0d398fe4736c:search

```yaml
regex_id: 3ed944d4c5fb206d794a0d398fe4736c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/hook-utils.sh:629:60"
```

### Pattern

`^0+\.0+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3f0cea8deae497df6341e9d112dc4868:search

```yaml
regex_id: 3f0cea8deae497df6341e9d112dc4868
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/actionlint/hooks/hook-utils.sh:1439:22"
```

### Pattern

`^-?[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3fd618e64953890e09ec77f67b7bfca4:search

```yaml
regex_id: 3fd618e64953890e09ec77f67b7bfca4
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-config/skills/audit/scripts/check-plugin-drift.sh:172:77"
```

### Pattern

`^$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:404c79dab94e8d2ef6a45958e20bfe3d:search

```yaml
regex_id: 404c79dab94e8d2ef6a45958e20bfe3d
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/go-format/hooks/hook-utils.sh:950:5"
```

### Pattern

`^[a-zA-Z_][a-zA-Z0-9_]*(\[.*\])?\+?=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4073fb895b2949832b1634a3e7ade614:search

```yaml
regex_id: 4073fb895b2949832b1634a3e7ade614
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-hygiene/skills/clean/scripts/clean-build.test.sh:83:3"
```

### Pattern

`^caches`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:41abcdd62dea7231c6ea1e800eb0e6d2:search

```yaml
regex_id: 41abcdd62dea7231c6ea1e800eb0e6d2
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-ops/skills/morning-brief/morning-brief.test.sh:431:47"
```

### Pattern

`^[[:space:]]+\[P[0-9]\]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:420175034d01c412b7c74eaf633510b3:search

```yaml
regex_id: 420175034d01c412b7c74eaf633510b3
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/skills/commit/scripts/exec-bit-check.test.sh:469:65"
```

### Pattern

`^C`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4247969451631b9f324e3a0fcf1d8ff5:search

```yaml
regex_id: 4247969451631b9f324e3a0fcf1d8ff5
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-fleet-hygiene/skills/audit/scripts/audit-fleet.test.sh:922:0"
```

### Pattern

`^\| ${bt}[a-z-]+${bt} \|`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4372690ce5110990b0eb9deb93b9128d:search

```yaml
regex_id: 4372690ce5110990b0eb9deb93b9128d
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/desktop-notification/hooks/desktop-notification.test.sh:370:3"
```

### Pattern

`^ARG=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:44221fd155e126592705b4e14bdd77df:search

```yaml
regex_id: 44221fd155e126592705b4e14bdd77df
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/skill-quality/scripts/check-skill.sh:851:5"
```

### Pattern

`^shell:[[:space:]]*[^[:space:]]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4436722c84d585749fcac460f9ea464a:search

```yaml
regex_id: 4436722c84d585749fcac460f9ea464a
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/biome-format/hooks/hook-utils.sh:574:9"
```

### Pattern

`^[0-9]+(\.[0-9]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:447692ef70651a385019b500fa3d1c32:search

```yaml
regex_id: 447692ef70651a385019b500fa3d1c32
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-memory/skills/audit/scripts/memory-dir-stats.test.sh:323:5"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:45fb33b3740340aa7cb3c99e259b954d:search

```yaml
regex_id: 45fb33b3740340aa7cb3c99e259b954d
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/scripts/check-orphaned-fixtures.sh:63:94"
```

### Pattern

`^$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:465605123fee6a29e6f438677a88b38b:search

```yaml
regex_id: 465605123fee6a29e6f438677a88b38b
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/review/tests/standards-binding.test.sh:57:9"
```

### Pattern

`^disable-model-invocation: true`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:48456fbe44491451af7907ee2fb9f757:search

```yaml
regex_id: 48456fbe44491451af7907ee2fb9f757
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-ops/hooks/hook-utils.sh:574:9"
```

### Pattern

`^[0-9]+(\.[0-9]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:484b3b99671b0433257b6980b1f165ca:search

```yaml
regex_id: 484b3b99671b0433257b6980b1f165ca
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/skills/pull-request/scripts/fetch-annotations.test.sh:193:36"
```

### Pattern

`^{`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4946faea995a6e6dc6b6f3d670fba0b1:search

```yaml
regex_id: 4946faea995a6e6dc6b6f3d670fba0b1
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/ruff-format/hooks/hook-utils.sh:574:9"
```

### Pattern

`^[0-9]+(\.[0-9]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:49e9264c380eb896a47daa30edd511d0:search

```yaml
regex_id: 49e9264c380eb896a47daa30edd511d0
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/lib/hook-utils.sh:574:9"
```

### Pattern

`^[0-9]+(\.[0-9]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4a6d179148d732bc2a34a5b6cb2fdc9e:search

```yaml
regex_id: 4a6d179148d732bc2a34a5b6cb2fdc9e
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/typos-format/hooks/hook-utils.sh:1439:22"
```

### Pattern

`^-?[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4ab046cd6d7afeec229bf12d4d2af3ba:search

```yaml
regex_id: 4ab046cd6d7afeec229bf12d4d2af3ba
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/hardcoded-path-check.sh:248:16"
```

### Pattern

`detected:$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4b38216c90235f84ad4ceccd003301dd:search

```yaml
regex_id: 4b38216c90235f84ad4ceccd003301dd
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/scripts/babysit-readiness-gate.test.sh:637:39"
```

### Pattern

`^READINESS_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4bafc865c22b524c412ab07da65057e1:search

```yaml
regex_id: 4bafc865c22b524c412ab07da65057e1
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-ops/skills/lanes/scripts/lane-launcher.sh:138:2"
```

### Pattern

`^[0-9]+(\.[0-9]+)*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4c36c7070ef6fa6d93d495a4b0aafdc1:search

```yaml
regex_id: 4c36c7070ef6fa6d93d495a4b0aafdc1
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/lib/hook-utils.test.sh:170:5"
```

### Pattern

`^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4c40d3e7ffbb83110bfc9a9d9b8cb541:search

```yaml
regex_id: 4c40d3e7ffbb83110bfc9a9d9b8cb541
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/bash-format/hooks/bash-format.test.sh:182:5"
```

### Pattern

`^  echo hi$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4ccfa54c1ca88c421207f231e0ddf603:search

```yaml
regex_id: 4ccfa54c1ca88c421207f231e0ddf603
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/discovery/scripts/contract.test.sh:170:13"
```

### Pattern

`^maxTurns:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4dadaf12e5dc77be3798c3bbb022ed5d:search

```yaml
regex_id: 4dadaf12e5dc77be3798c3bbb022ed5d
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/lib/hook-utils.sh:629:60"
```

### Pattern

`^0+\.0+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4e4089ae5fbd044767ff5b0e6c31ead6:search

```yaml
regex_id: 4e4089ae5fbd044767ff5b0e6c31ead6
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/desktop-notification/hooks/hook-utils.sh:574:46"
```

### Pattern

`^0+(\.0+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4e6a4288d8e3e3385a84fea7600dc9a2:search

```yaml
regex_id: 4e6a4288d8e3e3385a84fea7600dc9a2
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/bash-format/hooks/bash-format.test.sh:231:5"
```

### Pattern

`^echo hi$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4e7eb069d7a0ec6d79fc778552a8d307:search

```yaml
regex_id: 4e7eb069d7a0ec6d79fc778552a8d307
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/skill-quality/scripts/check-skill.sh:553:7"
```

### Pattern

`^[[:space:]]*$key:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4e98cac58158b2f0f5441d9261164b21:search

```yaml
regex_id: 4e98cac58158b2f0f5441d9261164b21
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-config/skills/audit-permission-state/scripts/permission-state.test.sh:114:33"
```

### Pattern

`^managed dropin-file:[^ ]+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4ef9ffb26a246ec124053e61ddd3a0d7:search

```yaml
regex_id: 4ef9ffb26a246ec124053e61ddd3a0d7
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/hooks/hook-utils.sh:621:5"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:514accf2b743e873e53819ec909a6721:search

```yaml
regex_id: 514accf2b743e873e53819ec909a6721
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/work-items/tests/no-hardcoded-priority-scheme.test.sh:85:4"
```

### Pattern

`/CHANGELOG\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5224e943b1d141157d562f363b725d13:search

```yaml
regex_id: 5224e943b1d141157d562f363b725d13
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/planning/scripts/goal-condition-length.sh:108:5"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:52405cb50f6568d9a703319b45d4b757:search

```yaml
regex_id: 52405cb50f6568d9a703319b45d4b757
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/planning/scripts/check-open-questions.sh:150:2"
```

### Pattern

`^[[:space:]]*-[[:space:]]+[Qq][0-9]+([^0-9]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:526524881e2cea30bcfcf77a432208cf:search

```yaml
regex_id: 526524881e2cea30bcfcf77a432208cf
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/rate-limit-guard/hooks/hook-utils.sh:574:9"
```

### Pattern

`^[0-9]+(\.[0-9]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5336dc313713a0857dd648116eb95b35:search

```yaml
regex_id: 5336dc313713a0857dd648116eb95b35
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-config/skills/audit-permission-state/scripts/automode-entry-diff.sh:362:67"
```

### Pattern

`^$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5479d8d79a03fcca40c32d80fa83a869:search

```yaml
regex_id: 5479d8d79a03fcca40c32d80fa83a869
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/ruff-format/hooks/hook-utils.sh:576:9"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:555f33265100dd8dd171ae438116d5bd:search

```yaml
regex_id: 555f33265100dd8dd171ae438116d5bd
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/bash-format/hooks/bash-format.test.sh:274:5"
```

### Pattern

`^  echo hi$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:55d61af6837249e4c9723ddd533e6a3e:search

```yaml
regex_id: 55d61af6837249e4c9723ddd533e6a3e
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-ops/skills/lanes/scripts/telemetry-upsert.sh:333:0"
```

### Pattern

`^[A-Za-z0-9._-]+/[A-Za-z0-9._-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5677fc67c71fcfcbe1e97d886c9f974b:search

```yaml
regex_id: 5677fc67c71fcfcbe1e97d886c9f974b
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/bash-format/hooks/hook-utils.sh:1348:18"
```

### Pattern

`^-[i0v](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:568c2c653dc38b5764fe3418c694ddc0:search

```yaml
regex_id: 568c2c653dc38b5764fe3418c694ddc0
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/autonomy/hooks/hook-utils.sh:1439:22"
```

### Pattern

`^-?[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:57d28ce0021a20d053f7bc2dfb57fa04:search

```yaml
regex_id: 57d28ce0021a20d053f7bc2dfb57fa04
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/code-tidying/scripts/allowed-tools-pairing.test.sh:49:4"
```

### Pattern

`^allowed-tools:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:57ed4dea6a365af4c507e0747c49ebf2:search

```yaml
regex_id: 57ed4dea6a365af4c507e0747c49ebf2
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-ops/skills/morning-brief/scripts/morning-brief.sh:94:2"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:595e6b16bca7c89b98e76b18dccd1835:search

```yaml
regex_id: 595e6b16bca7c89b98e76b18dccd1835
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/markdown-format.test.sh:546:28"
```

### Pattern

`^- star item$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5bd67c9ff866f92f0d4c92526b77d4aa:search

```yaml
regex_id: 5bd67c9ff866f92f0d4c92526b77d4aa
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/biome-format/hooks/hook-utils.sh:576:9"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5dca26e361df0080dd5c68215de4e73d:search

```yaml
regex_id: 5dca26e361df0080dd5c68215de4e73d
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/work-items/tools/work-item-tracker/adapters/local-markdown/common.sh:223:6"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5e1a6ba55e83aa6ee17894c258ff8407:search

```yaml
regex_id: 5e1a6ba55e83aa6ee17894c258ff8407
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-ops/hooks/hook-utils.sh:1439:22"
```

### Pattern

`^-?[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5e2576035ac8b0ab245e8de5c9308bed:search

```yaml
regex_id: 5e2576035ac8b0ab245e8de5c9308bed
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/hook-utils.sh:574:46"
```

### Pattern

`^0+(\.0+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5ec580466d18f412bff8ced3f9a5759e:search

```yaml
regex_id: 5ec580466d18f412bff8ced3f9a5759e
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/work-items/tools/work-item-tracker/adapters/github/create-item.sh:90:0"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:609afbf3886f5aba7288dfd7d8cd0791:search

```yaml
regex_id: 609afbf3886f5aba7288dfd7d8cd0791
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/typos-format/hooks/typos-format.test.sh:494:27"
```

### Pattern

`^  "[^"]*" -> "[^"]*" \(line 2\)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:60d5670821576134ac540f08c0d6d5bd:search

```yaml
regex_id: 60d5670821576134ac540f08c0d6d5bd
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/eol-normalizer/hooks/hook-utils.sh:950:5"
```

### Pattern

`^[a-zA-Z_][a-zA-Z0-9_]*(\[.*\])?\+?=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:60d5774059798c5481969b88ab994799:search

```yaml
regex_id: 60d5774059798c5481969b88ab994799
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/hooks/hook-utils.sh:1348:18"
```

### Pattern

`^-[i0v](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:617dcc05e1f353c96143ccca2487a4a4:search

```yaml
regex_id: 617dcc05e1f353c96143ccca2487a4a4
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/rate-limit-guard/hooks/hook-utils.sh:621:5"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:61cb8678c9f25fd7bf6c704229389245:search

```yaml
regex_id: 61cb8678c9f25fd7bf6c704229389245
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/hook-utils.sh:574:9"
```

### Pattern

`^[0-9]+(\.[0-9]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:62efda0c9741cb3a0526aa7e6fa7137e:search

```yaml
regex_id: 62efda0c9741cb3a0526aa7e6fa7137e
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/lib/resolve-convention-pattern.sh:215:2"
```

### Pattern

`^${k}:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6301a37223fa6df51a331b2a272d08a1:search

```yaml
regex_id: 6301a37223fa6df51a331b2a272d08a1
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/skill-quality/scripts/check-skill.sh:554:6"
```

### Pattern

`^[[:space:]]*$key:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:643c167d29fc6c9f26b43d3b1a174e25:search

```yaml
regex_id: 643c167d29fc6c9f26b43d3b1a174e25
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/bash-format/hooks/hook-utils.sh:1770:11"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:64e3f1c6da9681fe6283de32e6c1720b:search

```yaml
regex_id: 64e3f1c6da9681fe6283de32e6c1720b
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-config/skills/audit-pass/scripts/run-state.sh:659:2"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:660fab106cf824dd93a60fa4fad769c8:search

```yaml
regex_id: 660fab106cf824dd93a60fa4fad769c8
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/ruff-format/hooks/hook-utils.sh:621:5"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:66bf732b8b0f92e8e27f0eb21166e402:search

```yaml
regex_id: 66bf732b8b0f92e8e27f0eb21166e402
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/context-guard/scripts/context-zone.sh:146:0"
```

### Pattern

`^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:66fead86e4ed829fa4ec95da43c83b07:search

```yaml
regex_id: 66fead86e4ed829fa4ec95da43c83b07
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/work-items/tools/work-item-tracker/conformance/run-conformance.sh:221:35"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:674cffb4f647071ebea0520b9dcfd779:search

```yaml
regex_id: 674cffb4f647071ebea0520b9dcfd779
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/work-items/tools/work-item-tracker/adapters/local-markdown/common.sh:295:4"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:67e6f615c932ed1bf3123927dc3f87f0:search

```yaml
regex_id: 67e6f615c932ed1bf3123927dc3f87f0
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/block-dangerous-git.sh:338:2"
```

### Pattern

`^[0-9a-fA-F]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:68ea60fd328dd4d3a3f94ebd961b9d93:search

```yaml
regex_id: 68ea60fd328dd4d3a3f94ebd961b9d93
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/mcp-tools/skills/audit/scripts/discover.sh:192:11"
```

### Pattern

`^[[:space:]]*@mcp\.tool`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:68fa1df93460f61a202d3954d74674ef:search

```yaml
regex_id: 68fa1df93460f61a202d3954d74674ef
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/work-items/tools/work-item-tracker/adapters/github/renew-lease.sh:26:0"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6926ba7d8fe4746dfe61572ab1aa4b92:search

```yaml
regex_id: 6926ba7d8fe4746dfe61572ab1aa4b92
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/rate-limit-guard/hooks/record-rate-limit-stop.test.sh:122:3"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6948f5768c9037ab4152bf40c73289f9:search

```yaml
regex_id: 6948f5768c9037ab4152bf40c73289f9
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/prototype/scripts/allowed-tools-pairing.test.sh:49:4"
```

### Pattern

`^allowed-tools:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:69856975103dee874fe0193afe7acc8d:search

```yaml
regex_id: 69856975103dee874fe0193afe7acc8d
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-config/skills/audit-permission-grants/scripts/permission-rule-check.sh:375:6"
```

### Pattern

`^plugins/[^/]+/skills/[^/]+/SKILL\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6992ae47dfb8ec4d8eb2d6b9bd7dfa39:search

```yaml
regex_id: 6992ae47dfb8ec4d8eb2d6b9bd7dfa39
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/block-dangerous-git.sh:1257:11"
```

### Pattern

`^-[A-Za-z]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6a8b2893a8ab5f4fb6d8a0f02be5330f:search

```yaml
regex_id: 6a8b2893a8ab5f4fb6d8a0f02be5330f
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/markdown-format.test.sh:2333:25"
```

### Pattern

`^\* star item$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6b1dbff0bf84da98f0b8bf7ec78463d5:search

```yaml
regex_id: 6b1dbff0bf84da98f0b8bf7ec78463d5
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/actionlint/hooks/hook-utils.sh:576:9"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6bf6c3048e080f262733c8f857c4d3b1:search

```yaml
regex_id: 6bf6c3048e080f262733c8f857c4d3b1
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/bash-format/hooks/hook-utils.sh:621:5"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6c4eed189f5ff4386f4dcd2d322232e3:search

```yaml
regex_id: 6c4eed189f5ff4386f4dcd2d322232e3
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/markdown-format.test.sh:192:3"
```

### Pattern

`^- star item$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6cc5b3c4f7f56b09c3a3404bc02524f6:search

```yaml
regex_id: 6cc5b3c4f7f56b09c3a3404bc02524f6
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/context-guard/hooks/hook-utils.sh:950:5"
```

### Pattern

`^[a-zA-Z_][a-zA-Z0-9_]*(\[.*\])?\+?=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6d923f6fd5aa0f53093fe2e8ce315727:search

```yaml
regex_id: 6d923f6fd5aa0f53093fe2e8ce315727
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/typos-format/hooks/hook-utils.sh:576:9"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6e79884026902ef1548ff2189c5f05db:search

```yaml
regex_id: 6e79884026902ef1548ff2189c5f05db
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-ops/hooks/hook-utils.sh:1485:22"
```

### Pattern

`^[0-9]+([.][0-9]+)?(s|m|h|d)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6ebcbeb18785eb813e732d515cb2a523:search

```yaml
regex_id: 6ebcbeb18785eb813e732d515cb2a523
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-ops/hooks/hook-utils.sh:629:60"
```

### Pattern

`^0+\.0+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6efa63730e13bbbdeb944d8ab21e1385:search

```yaml
regex_id: 6efa63730e13bbbdeb944d8ab21e1385
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/desktop-notification/hooks/hook-utils.sh:1439:22"
```

### Pattern

`^-?[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6f57025ac8bea9d6085576e6c27730e3:search

```yaml
regex_id: 6f57025ac8bea9d6085576e6c27730e3
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/bash-format/hooks/hook-utils.sh:1439:22"
```

### Pattern

`^-?[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:704a8e1c0c84846174b4b4a256d6711c:search

```yaml
regex_id: 704a8e1c0c84846174b4b4a256d6711c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/context-guard/scripts/context-zone.sh:230:2"
```

### Pattern

`^[0-9]+(\.[0-9]+)*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7062066825d92a658e411ebb473a635b:search

```yaml
regex_id: 7062066825d92a658e411ebb473a635b
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/markdown-format.test.sh:524:35"
```

### Pattern

`^- star item$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:71283d595f7deeed79e582faa2a956e9:search

```yaml
regex_id: 71283d595f7deeed79e582faa2a956e9
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/powershell-format/hooks/hook-utils.sh:576:9"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:71dad4067e8a87b51392621d6c2dfbd8:search

```yaml
regex_id: 71dad4067e8a87b51392621d6c2dfbd8
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/hook-utils.sh:629:60"
```

### Pattern

`^0+\.0+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:72cbfe68df12e4fac88b546a5ec9a887:search

```yaml
regex_id: 72cbfe68df12e4fac88b546a5ec9a887
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-hygiene/scripts/allowed-tools-pairing.test.sh:65:4"
```

### Pattern

`^allowed-tools:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7304f9f73f4a59be7a2fd94e7ae45cce:search

```yaml
regex_id: 7304f9f73f4a59be7a2fd94e7ae45cce
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/planning/tests/standards-binding.test.sh:33:8"
```

### Pattern

`^### Step 3:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:734827999bd6e634c90ee47474a27044:search

```yaml
regex_id: 734827999bd6e634c90ee47474a27044
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/plugin-quality/scripts/packet-prune.sh:65:2"
```

### Pattern

`^# Retention pruning`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:742ee2344a91b1f4db8913ae2ecadded:search

```yaml
regex_id: 742ee2344a91b1f4db8913ae2ecadded
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/actionlint/hooks/hook-utils.sh:629:60"
```

### Pattern

`^0+\.0+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:749c8e8acea240fb703220bed4c14b65:search

```yaml
regex_id: 749c8e8acea240fb703220bed4c14b65
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/biome-format/hooks/biome-format.sh:221:11"
```

### Pattern

`^::(warning|error|notice)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:74a94eb9c9aae269bf168a12cecf4ef4:search

```yaml
regex_id: 74a94eb9c9aae269bf168a12cecf4ef4
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/skill-quality/scripts/check-skill.sh:610:3"
```

### Pattern

`^##+[[:space:]]+Actions?([^[:alnum:]_]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:755fcd673a466c7c5971b783fc797ddd:search

```yaml
regex_id: 755fcd673a466c7c5971b783fc797ddd
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/planning/scripts/check-open-questions.sh:49:2"
```

### Pattern

`^# Mechanical`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:763ca07684f72f48b43b6ef2b56a8e92:search

```yaml
regex_id: 763ca07684f72f48b43b6ef2b56a8e92
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-config/skills/audit-permission-grants/scripts/permission-rule-check.sh:381:6"
```

### Pattern

`^plugins/[^/]+/agents/[^/]+\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:76b27a9c258cb5af15c5b9aee3bc8101:search

```yaml
regex_id: 76b27a9c258cb5af15c5b9aee3bc8101
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/scripts/babysit-readiness-gate.test.sh:736:13"
```

### Pattern

`^[[:space:]]*exit [34]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:770f249a2a47000e3e756810bc19f927:search

```yaml
regex_id: 770f249a2a47000e3e756810bc19f927
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/bash-format/hooks/bash-format.test.sh:217:5"
```

### Pattern

`^echo hi$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7888526f03653a3a534b772dd2a34ec8:search

```yaml
regex_id: 7888526f03653a3a534b772dd2a34ec8
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/discovery/scripts/check-dispatch-artifact.sh:87:2"
```

### Pattern

`^# Deterministic acceptance gate`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:78a1f5664547b0c722dc4b5cab59b2f1:search

```yaml
regex_id: 78a1f5664547b0c722dc4b5cab59b2f1
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/lib/hook-utils.sh:574:46"
```

### Pattern

`^0+(\.0+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:78e0be0e4d38d388578b9db3afd6085c:search

```yaml
regex_id: 78e0be0e4d38d388578b9db3afd6085c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/work-items/tools/work-item-tracker/adapters/github/lease-coordination.test.sh:95:3"
```

### Pattern

`^PATCH`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:79f8674f5ae6b77c8d2403f2748f3f77:search

```yaml
regex_id: 79f8674f5ae6b77c8d2403f2748f3f77
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/work-items/tools/work-item-tracker/lib/binding.sh:46:2"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7a270ac18a7761974989bf26520e0ce7:search

```yaml
regex_id: 7a270ac18a7761974989bf26520e0ce7
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/scripts/check-discriminating-test-skips.test.sh:104:19"
```

### Pattern

`^DISCRIMINATING SKIP:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7a6cc6b61fe7537e9f7128c41574473e:search

```yaml
regex_id: 7a6cc6b61fe7537e9f7128c41574473e
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/biome-format/hooks/hook-utils.sh:1439:22"
```

### Pattern

`^-?[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7a90191f3e7b46d58bffa0ac54d3cfb8:search

```yaml
regex_id: 7a90191f3e7b46d58bffa0ac54d3cfb8
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/ruff-format/hooks/ruff-format.test.sh:193:43"
```

### Pattern

`^y = 2$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7bca52307a075ff7c332a190068b0f4e:search

```yaml
regex_id: 7bca52307a075ff7c332a190068b0f4e
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/context-guard/hooks/zone-gate.sh:119:0"
```

### Pattern

`^[0-9]{1,9}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7c81af8e243a1f07d6b0c0c86fee046c:search

```yaml
regex_id: 7c81af8e243a1f07d6b0c0c86fee046c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/go-format/hooks/hook-utils.sh:621:5"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7c94ada92b9d52161a3e9dac8937cb6d:search

```yaml
regex_id: 7c94ada92b9d52161a3e9dac8937cb6d
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-ops/skills/lanes/scripts/telemetry-upsert.sh:235:0"
```

### Pattern

`^[A-Za-z0-9:@._-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7f849427205a3ced6f6e6c5dad108f55:search

```yaml
regex_id: 7f849427205a3ced6f6e6c5dad108f55
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/scripts/sync-standards-contract.sh:31:2"
```

### Pattern

`^standards-contract:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:80a3e8bd6f29bd9c5f53e4b63d5d38e5:search

```yaml
regex_id: 80a3e8bd6f29bd9c5f53e4b63d5d38e5
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/context-guard/hooks/hook-utils.sh:574:9"
```

### Pattern

`^[0-9]+(\.[0-9]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8145e5fd79c7cc149407304716ef8d25:search

```yaml
regex_id: 8145e5fd79c7cc149407304716ef8d25
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/actionlint/hooks/hook-utils.sh:1485:22"
```

### Pattern

`^[0-9]+([.][0-9]+)?(s|m|h|d)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8201359bbd69f490c75433c77859e8f6:search

```yaml
regex_id: 8201359bbd69f490c75433c77859e8f6
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/bash-format/hooks/hook-utils.sh:574:46"
```

### Pattern

`^0+(\.0+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8220de6a0dddc2fa79ef8aeb0af99653:search

```yaml
regex_id: 8220de6a0dddc2fa79ef8aeb0af99653
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/skill-quality/scripts/check-skill.sh:234:2"
```

### Pattern

`^description:[[:space:]]*[^[:space:]]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8248c7847e0fde21aede744f1ca59290:search

```yaml
regex_id: 8248c7847e0fde21aede744f1ca59290
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/work-items/tools/work-item-tracker/adapters/local-markdown/common.sh:113:4"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8297235a7586e23435780cce4fe68b29:search

```yaml
regex_id: 8297235a7586e23435780cce4fe68b29
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-config/skills/audit-permission-grants/scripts/permission-rule-check.sh:374:6"
```

### Pattern

`(^|/)\.claude/skills/[^/]+/SKILL\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:83c001d677b664b6c99e9ebf4add4fcd:search

```yaml
regex_id: 83c001d677b664b6c99e9ebf4add4fcd
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/markdown-format.test.sh:2291:3"
```

### Pattern

`^- star item$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8456e198ba12b467973cdeef06142811:search

```yaml
regex_id: 8456e198ba12b467973cdeef06142811
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/skill-quality/scripts/check-evals-quality.test.sh:111:63"
```

### Pattern

`^FAIL:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:84e52387862d2a4f84ae99c169467d12:search

```yaml
regex_id: 84e52387862d2a4f84ae99c169467d12
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-config/skills/audit-permission-grants/scripts/permission-rule-check.sh:382:6"
```

### Pattern

`^plugins/[^/]+/commands/[^/]+\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:85e10b32fc65fe1b293b7c278dcd1271:search

```yaml
regex_id: 85e10b32fc65fe1b293b7c278dcd1271
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/markdown-format.test.sh:635:4"
```

### Pattern

`^- inside item$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:85e99bfb84521ff3016c4d25c1c0adc3:search

```yaml
regex_id: 85e99bfb84521ff3016c4d25c1c0adc3
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/block-dangerous-git.sh:556:4"
```

### Pattern

`^[./*?]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:868f8b931b8210ee7ae655093c273fc8:search

```yaml
regex_id: 868f8b931b8210ee7ae655093c273fc8
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/markdown-format.test.sh:2323:3"
```

### Pattern

`^- star item$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:87c1234904eab1312010881ddfe7a677:search

```yaml
regex_id: 87c1234904eab1312010881ddfe7a677
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-fleet-hygiene/skills/audit/scripts/audit-fleet.sh:449:4"
```

### Pattern

`^github\.com/[^/[:cntrl:][:space:]]+/[^/[:cntrl:][:space:]]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:88163d619d30bf81fe5fdbb0def28c48:search

```yaml
regex_id: 88163d619d30bf81fe5fdbb0def28c48
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/scripts/babysit-readiness-gate.sh:513:13"
```

### Pattern

`^[[:space:]]*-[[:space:]]\[[[:space:]]\]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:883def4c045ac7771cb7ec78388bd29e:search

```yaml
regex_id: 883def4c045ac7771cb7ec78388bd29e
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-hygiene/skills/clean/scripts/clean-caches.test.sh:58:3"
```

### Pattern

`^caches`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:88c31fa5a147b6cd28b296d8e2297b20:search

```yaml
regex_id: 88c31fa5a147b6cd28b296d8e2297b20
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-ops/skills/lanes/scripts/restart-consumer.sh:502:2"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:88ffe137b44b89e4b8ab616931427261:search

```yaml
regex_id: 88ffe137b44b89e4b8ab616931427261
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/discovery/agents/tool-honesty.test.sh:147:21"
```

### Pattern

`^persistence: `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:89199c1c84f8595415a429c2f8a32e55:search

```yaml
regex_id: 89199c1c84f8595415a429c2f8a32e55
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/biome-format/hooks/hook-utils.sh:621:5"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:89938d9dd21c4b68a7a405a063f19c63:search

```yaml
regex_id: 89938d9dd21c4b68a7a405a063f19c63
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/planning/tests/standards-binding.test.sh:32:8"
```

### Pattern

`^### Step 2: Formulate the Plan`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8a2ad95daea3c22939450dcc1a74f79a:search

```yaml
regex_id: 8a2ad95daea3c22939450dcc1a74f79a
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-ops/skills/lanes/scripts/restart-consumer.sh:207:2"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8aa3eed587193a5e8d4e15b4e8b1ddb0:search

```yaml
regex_id: 8aa3eed587193a5e8d4e15b4e8b1ddb0
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/actionlint/hooks/hook-utils.sh:574:46"
```

### Pattern

`^0+(\.0+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8acb5c131ec6f5e1e19cb3bd9fabe5a7:search

```yaml
regex_id: 8acb5c131ec6f5e1e19cb3bd9fabe5a7
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/powershell-format/hooks/hook-utils.sh:1348:18"
```

### Pattern

`^-[i0v](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8b57c2cb169a48f293eacd275fda76db:search

```yaml
regex_id: 8b57c2cb169a48f293eacd275fda76db
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/work-items/tools/work-item-tracker/adapters/local-markdown/common.sh:124:4"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8bbdb00c69de0153083ac2032a6562a8:search

```yaml
regex_id: 8bbdb00c69de0153083ac2032a6562a8
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/biome-format/hooks/hook-utils.sh:1348:18"
```

### Pattern

`^-[i0v](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8bbeff74587aa3fa20c10dae1a6f4c4a:search

```yaml
regex_id: 8bbeff74587aa3fa20c10dae1a6f4c4a
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/eol-normalizer/hooks/hook-utils.sh:1770:11"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8c70b0cf9710c25b6a382aeadb344998:search

```yaml
regex_id: 8c70b0cf9710c25b6a382aeadb344998
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/scripts/check-discriminating-test-skips.test.sh:162:55"
```

### Pattern

`^DISCRIMINATING SKIP:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8ce529035a18e88d3306320ba4e55ae0:search

```yaml
regex_id: 8ce529035a18e88d3306320ba4e55ae0
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/context-guard/hooks/hook-utils.sh:1439:22"
```

### Pattern

`^-?[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8d282328cc57b2e04b36c19127cfa57f:search

```yaml
regex_id: 8d282328cc57b2e04b36c19127cfa57f
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/context-guard/hooks/zone-crossing-inject.sh:127:0"
```

### Pattern

`^[A-Za-z0-9_-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8e8ce6d67f4baf77ac2a3f1c5f75bd26:search

```yaml
regex_id: 8e8ce6d67f4baf77ac2a3f1c5f75bd26
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/lib/hook-utils.sh:1439:22"
```

### Pattern

`^-?[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8f0d3ce5590b7be2aeaa2f5d61c02640:search

```yaml
regex_id: 8f0d3ce5590b7be2aeaa2f5d61c02640
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/bash-format/hooks/hook-utils.sh:1485:22"
```

### Pattern

`^[0-9]+([.][0-9]+)?(s|m|h|d)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:90fa3944530ff640bc6af00e942af651:search

```yaml
regex_id: 90fa3944530ff640bc6af00e942af651
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/eol-normalizer/hooks/hook-utils.sh:1439:22"
```

### Pattern

`^-?[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9100e87c171f93fee0ec9b3639315da6:search

```yaml
regex_id: 9100e87c171f93fee0ec9b3639315da6
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/scripts/check-docs-only.sh:55:94"
```

### Pattern

`^$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9103b0a20c4226f5e352708f4a0d7693:search

```yaml
regex_id: 9103b0a20c4226f5e352708f4a0d7693
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-config/skills/audit-permission-grants/scripts/permission-rule-check.sh:379:6"
```

### Pattern

`(^|/)\.claude/agents/[^/]+\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:910574484f402dda99bd8b5b1c25a506:search

```yaml
regex_id: 910574484f402dda99bd8b5b1c25a506
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/hook-utils.sh:1485:22"
```

### Pattern

`^[0-9]+([.][0-9]+)?(s|m|h|d)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:93243d5f66edfc1a1ef779b952838952:search

```yaml
regex_id: 93243d5f66edfc1a1ef779b952838952
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/scripts/check-discriminating-test-skips.test.sh:162:19"
```

### Pattern

`^SKIP:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:938a2a5ad9ada85d38f9b6daa1085c61:search

```yaml
regex_id: 938a2a5ad9ada85d38f9b6daa1085c61
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/hook-utils.sh:574:46"
```

### Pattern

`^0+(\.0+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:93d4d7acc9e31508dc8226b9958dd0a7:search

```yaml
regex_id: 93d4d7acc9e31508dc8226b9958dd0a7
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/resolve-convention-pattern.sh:215:2"
```

### Pattern

`^${k}:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:93e638929bb99be4d7f8bbc1a3697e0c:search

```yaml
regex_id: 93e638929bb99be4d7f8bbc1a3697e0c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-fleet-hygiene/skills/audit/scripts/audit-fleet.sh:770:7"
```

### Pattern

`^[^@]+@([^:]+):(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:94d397f7b3862624f42dc9d28aba17b8:search

```yaml
regex_id: 94d397f7b3862624f42dc9d28aba17b8
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/hooks/hook-utils.sh:574:9"
```

### Pattern

`^[0-9]+(\.[0-9]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:953b1e68047f738b94469c80218442ec:search

```yaml
regex_id: 953b1e68047f738b94469c80218442ec
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/hook-utils.sh:1770:11"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9543c3164897e95bad4e80d5b84e0dc5:search

```yaml
regex_id: 9543c3164897e95bad4e80d5b84e0dc5
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/scripts/landed-work.test.sh:525:57"
```

### Pattern

`^worktree `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9568d12512fd3ade3d8b60c60781fe8a:search

```yaml
regex_id: 9568d12512fd3ade3d8b60c60781fe8a
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/actionlint/hooks/hook-utils.sh:574:9"
```

### Pattern

`^[0-9]+(\.[0-9]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:95750bee8dd204d1e80e43f1d337ded7:search

```yaml
regex_id: 95750bee8dd204d1e80e43f1d337ded7
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/ruff-format/hooks/hook-utils.sh:1485:22"
```

### Pattern

`^[0-9]+([.][0-9]+)?(s|m|h|d)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9686a5777dfc492ff62efae5345bca4c:search

```yaml
regex_id: 9686a5777dfc492ff62efae5345bca4c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-hygiene/skills/clean/scripts/preflight.sh:58:37"
```

### Pattern

`^(devenv|rider64?|fleet|webstorm|pycharm)\.exe`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:96971d4ce1eade780f745bb5cc6cd3ee:search

```yaml
regex_id: 96971d4ce1eade780f745bb5cc6cd3ee
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/docs-hygiene/skills/audit-noise/scripts/detect.sh:114:7"
```

### Pattern

`^##[[:space:]]+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:988fe90a93a1c78451de6f93687b2e9c:search

```yaml
regex_id: 988fe90a93a1c78451de6f93687b2e9c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/hook-utils.sh:621:5"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:98b5c8f688006849e7138cf6d33e7481:search

```yaml
regex_id: 98b5c8f688006849e7138cf6d33e7481
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/typos-format/hooks/hook-utils.sh:950:5"
```

### Pattern

`^[a-zA-Z_][a-zA-Z0-9_]*(\[.*\])?\+?=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:98f260124a46bce5f37fc5a45c5d4c97:search

```yaml
regex_id: 98f260124a46bce5f37fc5a45c5d4c97
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-hygiene/skills/clean/scripts/clean-batch.test.sh:325:30"
```

### Pattern

`^GITDIR	`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:98f679508d6303ad45d8fc7afa23f52f:search

```yaml
regex_id: 98f679508d6303ad45d8fc7afa23f52f
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/discovery/scripts/contract.test.sh:153:38"
```

### Pattern

`^allowed-tools:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:99264a3f2d466407be4843c8a190dcad:url

```yaml
regex_id: 99264a3f2d466407be4843c8a190dcad
schema_version: "1"
kind: intent_mismatch
corpus: claude-code-plugins
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-ops/skills/lanes/scripts/telemetry-upsert.test.sh:571:2"
```

### Pattern

`method=GET url=repos/.*/issues/comments/`

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

## usage_mismatch:9937bff6471927ae42f71f52b96ec88d:search

```yaml
regex_id: 9937bff6471927ae42f71f52b96ec88d
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/ruff-format/hooks/hook-utils.sh:1439:22"
```

### Pattern

`^-?[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:99eb56c5c44486944c9ed9d89168861e:search

```yaml
regex_id: 99eb56c5c44486944c9ed9d89168861e
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-hygiene/skills/clean/scripts/clean-batch.test.sh:336:3"
```

### Pattern

`^REPO	`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9a098c94a4b04d6b932e97acb1784181:search

```yaml
regex_id: 9a098c94a4b04d6b932e97acb1784181
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-ops/hooks/hook-utils.sh:1348:18"
```

### Pattern

`^-[i0v](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9b23995f42b08646e86a6b83713ab5b2:search

```yaml
regex_id: 9b23995f42b08646e86a6b83713ab5b2
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/cli-flag-verify.sh:270:34"
```

### Pattern

`^[a-z][a-z0-9-]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9b657446418a79a38bb97cbee088bc32:search

```yaml
regex_id: 9b657446418a79a38bb97cbee088bc32
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/cli-flag-verify.test.sh:283:20"
```

### Pattern

`^DEFAULT_BINS=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9c85fed6c0ec9cd73ab7de360744dec1:search

```yaml
regex_id: 9c85fed6c0ec9cd73ab7de360744dec1
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/docs-hygiene/skills/audit-noise/scripts/lib/noise-shapes.sh:85:5"
```

### Pattern

`^##[[:space:]]+Why[[:space:]]+this[[:space:]]+file[[:space:]]+exists`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9d73f5d60b50ad2d80894e6ea3cf0682:search

```yaml
regex_id: 9d73f5d60b50ad2d80894e6ea3cf0682
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-config/skills/audit-pass/scripts/run-state.sh:658:2"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9ec7d7349fd0b239d2d556f1e62bbc71:search

```yaml
regex_id: 9ec7d7349fd0b239d2d556f1e62bbc71
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/wizard/skills/generate/template.sh:157:9"
```

### Pattern

`^${1}=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9f86d93363e8b906a64c5a135d7e1314:search

```yaml
regex_id: 9f86d93363e8b906a64c5a135d7e1314
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/desktop-notification/hooks/hook-utils.sh:1348:18"
```

### Pattern

`^-[i0v](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9fd366562d9b8c47f39337db9d1ed09c:search

```yaml
regex_id: 9fd366562d9b8c47f39337db9d1ed09c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/context-guard/hooks/zone-gate.sh:146:0"
```

### Pattern

`^[0-9]{1,9}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a0497687e24cce31117cfe8df2d64509:search

```yaml
regex_id: a0497687e24cce31117cfe8df2d64509
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-hygiene/skills/clean/scripts/remove-path.sh:275:46"
```

### Pattern

`^worktree `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a0eb20fb103a3dfb2e34fa604ddfc14c:search

```yaml
regex_id: a0eb20fb103a3dfb2e34fa604ddfc14c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/markdown-format.test.sh:2310:3"
```

### Pattern

`^- star item$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a1070a4bde4c12615b57ea72c8d02a2a:search

```yaml
regex_id: a1070a4bde4c12615b57ea72c8d02a2a
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/go-format/hooks/hook-utils.sh:1485:22"
```

### Pattern

`^[0-9]+([.][0-9]+)?(s|m|h|d)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a23737bb6d82361e50fe775496baf16f:search

```yaml
regex_id: a23737bb6d82361e50fe775496baf16f
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/code-tidying/skills/audit-comment-residue/scripts/lib/comment-shapes.sh:48:5"
```

### Pattern

`^[[:space:]]*\*[[:space:]]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a2fec5d0976d1c4312b5d061164f5d20:search

```yaml
regex_id: a2fec5d0976d1c4312b5d061164f5d20
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/markdown-format.test.sh:684:28"
```

### Pattern

`^- star item$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a321805af30e570540ce8ce8764a4d3d:search

```yaml
regex_id: a321805af30e570540ce8ce8764a4d3d
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/scripts/run-plugin-tests.sh:55:15"
```

### Pattern

`^SKIP:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a3d12ac360df1864dbd2994f5d48718f:search

```yaml
regex_id: a3d12ac360df1864dbd2994f5d48718f
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/hooks/hook-utils.sh:1770:11"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a49996be14304f1eee71c878ce261cc6:search

```yaml
regex_id: a49996be14304f1eee71c878ce261cc6
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-fleet-hygiene/scripts/allowed-tools-pairing.test.sh:49:4"
```

### Pattern

`^allowed-tools:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a574e34fdd156d331785de625b3b0c21:search

```yaml
regex_id: a574e34fdd156d331785de625b3b0c21
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/require-jq-notice-isolation.test.sh:102:14"
```

### Pattern

`^FIRED:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a5954e8d627f74dbe2c34869d37ec477:search

```yaml
regex_id: a5954e8d627f74dbe2c34869d37ec477
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/scripts/run-plugin-tests.sh:60:20"
```

### Pattern

`^SKIP:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a6f39f2f6d66e1cfe481154e92384aac:search

```yaml
regex_id: a6f39f2f6d66e1cfe481154e92384aac
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/work-items/tools/work-item-tracker/adapters/github/claim.sh:31:0"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a7e459b49fac04f5eb978f7825a840dd:search

```yaml
regex_id: a7e459b49fac04f5eb978f7825a840dd
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/desktop-notification/hooks/desktop-notification.test.sh:365:13"
```

### Pattern

`^ARG=\[-danger`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a7ee2a0e32ddd206edfc06a39d153f9a:search

```yaml
regex_id: a7ee2a0e32ddd206edfc06a39d153f9a
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/playbooks/skills/boris/scripts/update.sh:84:2"
```

### Pattern

`^metadata:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a84d2219bf2f34bdaf924f9223eb1bac:search

```yaml
regex_id: a84d2219bf2f34bdaf924f9223eb1bac
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/rate-limit-guard/hooks/record-rate-limit-stop.sh:84:2"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:abfac7f46f49b708644fc3641e4bd65d:search

```yaml
regex_id: abfac7f46f49b708644fc3641e4bd65d
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/skill-quality/scripts/check-skill.sh:727:47"
```

### Pattern

`^[[:space:]]*```+!`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ac4d1726fed189af5915b1afb21ca0ef:search

```yaml
regex_id: ac4d1726fed189af5915b1afb21ca0ef
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/markdown-format.test.sh:279:29"
```

### Pattern

`^- nested item$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ac54678efd683abaad0373c4eb391b44:search

```yaml
regex_id: ac54678efd683abaad0373c4eb391b44
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-config/skills/audit/scripts/check-plugin-drift.sh:171:72"
```

### Pattern

`^$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ad0d6dc086091a9740b8b64906e18a6f:search

```yaml
regex_id: ad0d6dc086091a9740b8b64906e18a6f
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/markdown-format.test.sh:828:4"
```

### Pattern

`^- symlink item$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ae17311ec327da6ad92cf2ba9a89b363:search

```yaml
regex_id: ae17311ec327da6ad92cf2ba9a89b363
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/hook-utils.sh:576:9"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:aecfe60b2314ae2803ff5e9b07a58697:search

```yaml
regex_id: aecfe60b2314ae2803ff5e9b07a58697
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/hook-utils.sh:1348:18"
```

### Pattern

`^-[i0v](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:af788ca63ef152bf7403f6791a31c030:search

```yaml
regex_id: af788ca63ef152bf7403f6791a31c030
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/docs-hygiene/skills/audit-noise/scripts/detect.sh:76:50"
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

## usage_mismatch:b00015559e5e8231aab796d7569ecbf5:search

```yaml
regex_id: b00015559e5e8231aab796d7569ecbf5
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/context-guard/scripts/context-zone.sh:153:0"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b07021cf6ac39d72ef91b9e56c0bfd57:search

```yaml
regex_id: b07021cf6ac39d72ef91b9e56c0bfd57
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/hook-utils.sh:1439:22"
```

### Pattern

`^-?[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b078470260b2675d85d31faf6e94bbca:search

```yaml
regex_id: b078470260b2675d85d31faf6e94bbca
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-hygiene/skills/clean/scripts/clean-batch.test.sh:97:3"
```

### Pattern

`^REPO	`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b112e865fed0695712b9e96b06792a06:search

```yaml
regex_id: b112e865fed0695712b9e96b06792a06
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/lib/hook-utils.sh:576:9"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b2882d37f0d45f82f705525f74034ae4:search

```yaml
regex_id: b2882d37f0d45f82f705525f74034ae4
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-fleet-hygiene/skills/audit/scripts/audit-fleet.test.sh:806:9"
```

### Pattern

`^Resolved to main worktree:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b3981e344998dfd9f13ebcb82605264c:search

```yaml
regex_id: b3981e344998dfd9f13ebcb82605264c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/skill-quality/scripts/check-skill.sh:495:7"
```

### Pattern

`^[^[:space:]]+:[0-9]+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b46c4898f6525ea861d88eabe80e0232:search

```yaml
regex_id: b46c4898f6525ea861d88eabe80e0232
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/lib/hook-utils.sh:950:5"
```

### Pattern

`^[a-zA-Z_][a-zA-Z0-9_]*(\[.*\])?\+?=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b484335555e41a3dc80bfd9862b0efb3:search

```yaml
regex_id: b484335555e41a3dc80bfd9862b0efb3
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/context-guard/hooks/post-compact-mark.sh:54:0"
```

### Pattern

`^[A-Za-z0-9_-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b8068ea515556d1c72071b02c4ac6250:search

```yaml
regex_id: b8068ea515556d1c72071b02c4ac6250
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/go-format/hooks/hook-utils.sh:1439:22"
```

### Pattern

`^-?[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b8590eb510c133afa5bf6f5822f6187c:search

```yaml
regex_id: b8590eb510c133afa5bf6f5822f6187c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-memory/lib/state-key.sh:145:31"
```

### Pattern

`^[a-z0-9][a-z0-9._-]*(/[a-z0-9][a-z0-9._-]*)*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b886e1e42d7eec334236b469150463f6:search

```yaml
regex_id: b886e1e42d7eec334236b469150463f6
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/scripts/check-changelog-parity.sh:675:39"
```

### Pattern

`^##[[:space:]]+${esc}([[:space:]]|\$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b89be88aae08b2d8a96e2af962e3bc73:search

```yaml
regex_id: b89be88aae08b2d8a96e2af962e3bc73
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/scripts/check-queue-front-matter.sh:82:9"
```

### Pattern

`^(${VALID_STATUSES})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b8ff64f762ef8cc7e1897a10963cf850:search

```yaml
regex_id: b8ff64f762ef8cc7e1897a10963cf850
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-ops/hooks/hook-utils.sh:574:46"
```

### Pattern

`^0+(\.0+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b9374652bc00bd8e27db8d7c2053ee30:search

```yaml
regex_id: b9374652bc00bd8e27db8d7c2053ee30
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/review/skills/fanout/scripts/diff-vs-base.sh:51:2"
```

### Pattern

`^ref:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b95349d480b51dde3a44299bd533db7e:search

```yaml
regex_id: b95349d480b51dde3a44299bd533db7e
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/scripts/sync-standards-contract.sh:81:7"
```

### Pattern

`^## ${head_contract_re}( |$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b99b273f7c0f0f7485d02c5cca9b3fa9:search

```yaml
regex_id: b99b273f7c0f0f7485d02c5cca9b3fa9
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/scripts/run-plugin-tests.sh:56:16"
```

### Pattern

`^DISCRIMINATING SKIP:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:baa2fe3e6696f1d915be32c0aff56def:search

```yaml
regex_id: baa2fe3e6696f1d915be32c0aff56def
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/bash-format/hooks/bash-format.sh:144:11"
```

### Pattern

`^[[:space:]]*\[(.+)\][[:space:]]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bb3303d14067770f3ed7f648000468a1:search

```yaml
regex_id: bb3303d14067770f3ed7f648000468a1
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/powershell-format/hooks/hook-utils.sh:629:60"
```

### Pattern

`^0+\.0+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bb809e7cb4653f24cd3c1abe8dead51d:search

```yaml
regex_id: bb809e7cb4653f24cd3c1abe8dead51d
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/desktop-notification/hooks/hook-utils.sh:574:9"
```

### Pattern

`^[0-9]+(\.[0-9]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bca4ce0e865ac5b3b3828d1e6cee411a:search

```yaml
regex_id: bca4ce0e865ac5b3b3828d1e6cee411a
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/markdown-format.test.sh:331:5"
```

### Pattern

`^\* bullet$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bcdf766c06dc704690d4b82a6019bff2:search

```yaml
regex_id: bcdf766c06dc704690d4b82a6019bff2
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/work-items/tools/work-item-tracker/conformance/run-conformance.sh:133:5"
```

### Pattern

`^[a-z0-9][a-z0-9-]*:[^#[:space:]]+#[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bd3a9d8bd5edc878775b3c1b005b9ad3:search

```yaml
regex_id: bd3a9d8bd5edc878775b3c1b005b9ad3
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/rate-limit-guard/hooks/hook-utils.sh:1348:18"
```

### Pattern

`^-[i0v](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bd8af80af16ffdb2b2850a88966e207f:search

```yaml
regex_id: bd8af80af16ffdb2b2850a88966e207f
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/hook-utils.sh:621:5"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:be19b56d7f767b97037cbe0b7414934b:search

```yaml
regex_id: be19b56d7f767b97037cbe0b7414934b
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/rate-limit-guard/hooks/hook-utils.sh:1439:22"
```

### Pattern

`^-?[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bea64a132fc7779fc6fdb47dd95b54eb:search

```yaml
regex_id: bea64a132fc7779fc6fdb47dd95b54eb
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/typos-format/hooks/hook-utils.sh:1348:18"
```

### Pattern

`^-[i0v](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:beba2f838bb87b71961576fd98904279:search

```yaml
regex_id: beba2f838bb87b71961576fd98904279
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/docs-hygiene/scripts/allowed-tools-pairing.test.sh:49:4"
```

### Pattern

`^allowed-tools:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bee87b31258aace29014bc416a46d66c:search

```yaml
regex_id: bee87b31258aace29014bc416a46d66c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/markdown-format.test.sh:804:3"
```

### Pattern

`^- local item$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bffebedbb7305a888b15f443eea83848:search

```yaml
regex_id: bffebedbb7305a888b15f443eea83848
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/typos-format/hooks/hook-utils.sh:574:9"
```

### Pattern

`^[0-9]+(\.[0-9]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c079c985ff3e8c327e02946e9478b993:search

```yaml
regex_id: c079c985ff3e8c327e02946e9478b993
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/stale-path-verify.sh:284:38"
```

### Pattern

`^[[:space:]]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c2ed62308730da7533af4c8563b87cf3:search

```yaml
regex_id: c2ed62308730da7533af4c8563b87cf3
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/context-guard/hooks/hook-utils.sh:1485:22"
```

### Pattern

`^[0-9]+([.][0-9]+)?(s|m|h|d)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c3aeb639a3e980e9675e778f2006b900:search

```yaml
regex_id: c3aeb639a3e980e9675e778f2006b900
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/powershell-format/hooks/hook-utils.sh:1439:22"
```

### Pattern

`^-?[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c3d74f4ee53dfcb56eba3c85617a05df:search

```yaml
regex_id: c3d74f4ee53dfcb56eba3c85617a05df
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/markdown-format.test.sh:192:38"
```

### Pattern

`^\* star item$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c3e2d3791e86fff43d3fb8bbef70b6b2:search

```yaml
regex_id: c3e2d3791e86fff43d3fb8bbef70b6b2
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/powershell-format/hooks/hook-utils.sh:1485:22"
```

### Pattern

`^[0-9]+([.][0-9]+)?(s|m|h|d)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c403b802b9949c3ebb5af2e3ec2b25ff:search

```yaml
regex_id: c403b802b9949c3ebb5af2e3ec2b25ff
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-ops/skills/lanes/scripts/telemetry-upsert.sh:437:0"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c46890798dfe8a72242217b6fcf8fa7e:search

```yaml
regex_id: c46890798dfe8a72242217b6fcf8fa7e
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/actionlint/hooks/hook-utils.sh:950:5"
```

### Pattern

`^[a-zA-Z_][a-zA-Z0-9_]*(\[.*\])?\+?=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c5df73d556c392d078304d61adb65f40:search

```yaml
regex_id: c5df73d556c392d078304d61adb65f40
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/markdown-format.test.sh:2278:3"
```

### Pattern

`^\* star item$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c6865d8693e11bade0e8900d66aa3480:search

```yaml
regex_id: c6865d8693e11bade0e8900d66aa3480
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-ops/hooks/hook-utils.sh:1770:11"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c6d538fb39f2aaf7565c2e8334145ef6:search

```yaml
regex_id: c6d538fb39f2aaf7565c2e8334145ef6
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/ruff-format/hooks/hook-utils.sh:1770:11"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c6dfca12cc18d7fdad0757c5350dfb87:search

```yaml
regex_id: c6dfca12cc18d7fdad0757c5350dfb87
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/rate-limit-guard/scripts/statusline-tee.test.sh:83:38"
```

### Pattern

`^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c76e0a3316b7aaf8bbf7e08688310b70:search

```yaml
regex_id: c76e0a3316b7aaf8bbf7e08688310b70
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/skills/commit/scripts/exec-bit-check.test.sh:831:72"
```

### Pattern

`^C`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c7a4b593325f5e672f54260f2836be5b:search

```yaml
regex_id: c7a4b593325f5e672f54260f2836be5b
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/markdown-format.test.sh:2347:27"
```

### Pattern

`^\* star item$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c88f5ae6c19581d3636cca5a39feb99f:search

```yaml
regex_id: c88f5ae6c19581d3636cca5a39feb99f
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/context-guard/scripts/statusline-tee.test.sh:80:36"
```

### Pattern

`^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cb29f3f908b0b2fe712277c923296d50:search

```yaml
regex_id: cb29f3f908b0b2fe712277c923296d50
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/autonomy/hooks/hook-utils.sh:1770:11"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cc66deaeb2047a3b56a2782c53294add:search

```yaml
regex_id: cc66deaeb2047a3b56a2782c53294add
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/block-dangerous-git.sh:1055:9"
```

### Pattern

`^-[A-Za-z]*e[A-Za-z]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cd4acd3c99cd2b68073b474beb5b1f03:search

```yaml
regex_id: cd4acd3c99cd2b68073b474beb5b1f03
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-ops/skills/lanes/scripts/restart-consumer.sh:495:2"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cd8372d0e355fad11631165c179c3888:search

```yaml
regex_id: cd8372d0e355fad11631165c179c3888
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/hook-utils.sh:574:9"
```

### Pattern

`^[0-9]+(\.[0-9]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ce2a54e64ec5646ef4f7a22c8b1b83b8:search

```yaml
regex_id: ce2a54e64ec5646ef4f7a22c8b1b83b8
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/planning/scripts/check-open-questions.sh:182:7"
```

### Pattern

`^[1-9][0-9]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ce78760ce3c17969cc59099403d87635:search

```yaml
regex_id: ce78760ce3c17969cc59099403d87635
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-ops/hooks/hook-utils.sh:576:9"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ce8a12358c0695d7d019578ea49f866d:search

```yaml
regex_id: ce8a12358c0695d7d019578ea49f866d
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/desktop-notification/hooks/hook-utils.sh:621:5"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ce8ab51ae8f80b60013a6b580c1814de:search

```yaml
regex_id: ce8ab51ae8f80b60013a6b580c1814de
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/wizard/skills/generate/template.sh:234:2"
```

### Pattern

`^${key}=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cf5c95362d0e86e3ab8bb38c859d1f15:search

```yaml
regex_id: cf5c95362d0e86e3ab8bb38c859d1f15
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/skills/pull-request/scripts/fetch-annotations.test.sh:184:36"
```

### Pattern

`^{`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d010ee7320a1f69dd28b81e178e039d5:search

```yaml
regex_id: d010ee7320a1f69dd28b81e178e039d5
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/mcp-tools/skills/audit/scripts/discover.sh:223:11"
```

### Pattern

`^[[:space:]]*\[McpServerTool[^A-Za-z0-9_]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d1f36982adefd4c705bffd502cb38f1f:search

```yaml
regex_id: d1f36982adefd4c705bffd502cb38f1f
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/work-items/tools/work-item-tracker/adapters/local-markdown/common.sh:236:4"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d2eeb7e1f556dc4dbf457759e83ec92d:search

```yaml
regex_id: d2eeb7e1f556dc4dbf457759e83ec92d
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/bash-format/hooks/bash-format.sh:146:13"
```

### Pattern

`^[[:space:]]*[Rr][Oo][Oo][Tt][[:space:]]*=[[:space:]]*[Tt][Rr][Uu][Ee][[:space:]]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d30d8d95cbbaff3677e604d70c1ebcdf:search

```yaml
regex_id: d30d8d95cbbaff3677e604d70c1ebcdf
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/context-guard/hooks/hook-utils.sh:629:60"
```

### Pattern

`^0+\.0+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d329f8da256fd432a8abcf3c83cf2d4f:search

```yaml
regex_id: d329f8da256fd432a8abcf3c83cf2d4f
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/autonomy/hooks/hook-utils.sh:574:9"
```

### Pattern

`^[0-9]+(\.[0-9]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d32ef9c40f4343806207b994f63ba1a3:search

```yaml
regex_id: d32ef9c40f4343806207b994f63ba1a3
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/powershell-format/hooks/hook-utils.sh:574:46"
```

### Pattern

`^0+(\.0+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d354daef18f803e674a89e7524af0dfe:search

```yaml
regex_id: d354daef18f803e674a89e7524af0dfe
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/lib/resolve-convention-pattern.sh:127:10"
```

### Pattern

`^${k}:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d378bceb5dc5d1f918365f5c2789501b:search

```yaml
regex_id: d378bceb5dc5d1f918365f5c2789501b
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/skill-quality/scripts/check-skill.sh:568:5"
```

### Pattern

`^##+[[:space:]]+(gotchas|quirks)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d3c1ab8bfe9ea5c54b54dbf115838fbe:search

```yaml
regex_id: d3c1ab8bfe9ea5c54b54dbf115838fbe
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-hygiene/skills/clean/scripts/clean-batch.test.sh:307:3"
```

### Pattern

`^REPO	.*	build	`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d5f605e288ba20f0651ee587689c09a1:search

```yaml
regex_id: d5f605e288ba20f0651ee587689c09a1
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/markdown-format.test.sh:469:3"
```

### Pattern

`^- star item$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d62a2b7eff18c981713ec8ebfcbddd14:search

```yaml
regex_id: d62a2b7eff18c981713ec8ebfcbddd14
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/ruff-format/hooks/ruff-format.test.sh:193:3"
```

### Pattern

`^x = 1$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d64b0edf7cbfe292f8fe95ad2bf06f7c:search

```yaml
regex_id: d64b0edf7cbfe292f8fe95ad2bf06f7c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/powershell-format/hooks/hook-utils.sh:950:5"
```

### Pattern

`^[a-zA-Z_][a-zA-Z0-9_]*(\[.*\])?\+?=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d6d6245698fa201dac92be7c9e31c5fb:search

```yaml
regex_id: d6d6245698fa201dac92be7c9e31c5fb
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/skills/pull-request/scripts/fetch-annotations.test.sh:287:44"
```

### Pattern

`^{`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d7760fa6da4f486b2eeb21056a58a17d:search

```yaml
regex_id: d7760fa6da4f486b2eeb21056a58a17d
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/block-dangerous-git.sh:549:4"
```

### Pattern

`^[./*?]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d785028b7c0ba2c0ffee2dddcbfe2538:search

```yaml
regex_id: d785028b7c0ba2c0ffee2dddcbfe2538
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/ruff-format/hooks/hook-utils.sh:629:60"
```

### Pattern

`^0+\.0+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d79552233f1ddc908b4d8ea689eb5730:search

```yaml
regex_id: d79552233f1ddc908b4d8ea689eb5730
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/ruff-format/hooks/ruff-format.sh:156:4"
```

### Pattern

`^[[:space:]]*\[tool\.ruff(\]|[.])`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d80fd138a1d076b61dc722660f881c7e:search

```yaml
regex_id: d80fd138a1d076b61dc722660f881c7e
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/ruff-format/hooks/hook-utils.sh:574:46"
```

### Pattern

`^0+(\.0+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d8842ffe956c66311c9c5242284cfb86:search

```yaml
regex_id: d8842ffe956c66311c9c5242284cfb86
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/powershell-format/hooks/hook-utils.sh:574:9"
```

### Pattern

`^[0-9]+(\.[0-9]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d9071e7a97883cb9f6e5f4930a747d02:search

```yaml
regex_id: d9071e7a97883cb9f6e5f4930a747d02
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/skills/commit/scripts/exec-bit-check.test.sh:757:70"
```

### Pattern

`^A.*copy\.sh`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:da590f2a08412d1a74bed3e2edc7f986:search

```yaml
regex_id: da590f2a08412d1a74bed3e2edc7f986
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/hooks/pr-linkage-validator.sh:119:4"
```

### Pattern

`^##[[:space:]]+related$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:da67659f51b38207e1ecdebb897b380f:search

```yaml
regex_id: da67659f51b38207e1ecdebb897b380f
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/skills/commit/scripts/exec-bit-check.test.sh:761:69"
```

### Pattern

`^C`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:da909246020279dce137f1c9cd57a1a7:search

```yaml
regex_id: da909246020279dce137f1c9cd57a1a7
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/context-guard/hooks/hook-utils.sh:576:9"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dabfb4842c7e631faa4a32c4bbfa3eaa:search

```yaml
regex_id: dabfb4842c7e631faa4a32c4bbfa3eaa
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/firecrawl/skills/update/scripts/update.sh:113:2"
```

### Pattern

`^- $1:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dad180e7da905eaea8799ffd95cd445c:search

```yaml
regex_id: dad180e7da905eaea8799ffd95cd445c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/planning/scripts/goal-condition-length.sh:76:5"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:db10df1ddb5359aec7c31225a015ee27:search

```yaml
regex_id: db10df1ddb5359aec7c31225a015ee27
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/work-items/tools/work-item-tracker/conformance/e2e-probe.sh:114:3"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dbafebe6e8f52df5436404e842ee8a02:search

```yaml
regex_id: dbafebe6e8f52df5436404e842ee8a02
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/bash-format/hooks/hook-utils.sh:574:9"
```

### Pattern

`^[0-9]+(\.[0-9]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dca12f59908c442659c538f5bd78034d:search

```yaml
regex_id: dca12f59908c442659c538f5bd78034d
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/hook-utils.sh:576:9"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dd6784cb81985637b5e1c8a09e3daaff:search

```yaml
regex_id: dd6784cb81985637b5e1c8a09e3daaff
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/rate-limit-guard/hooks/hook-utils.sh:629:60"
```

### Pattern

`^0+\.0+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ddb70f69d42ecfbb87d1ce133958af46:search

```yaml
regex_id: ddb70f69d42ecfbb87d1ce133958af46
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/scripts/check-skill-portability.test.sh:963:3"
```

### Pattern

`^[[:space:]]*(#|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ddd36579923fbe842478c25de9af92df:search

```yaml
regex_id: ddd36579923fbe842478c25de9af92df
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/go-format/hooks/hook-utils.sh:1348:18"
```

### Pattern

`^-[i0v](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:de54e18551a201b49f5f8171f92e5068:search

```yaml
regex_id: de54e18551a201b49f5f8171f92e5068
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/bash-format/hooks/bash-format.test.sh:289:5"
```

### Pattern

`^  echo hi$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:def317131495847635d5db60cd25ef53:search

```yaml
regex_id: def317131495847635d5db60cd25ef53
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/biome-format/hooks/hook-utils.sh:629:60"
```

### Pattern

`^0+\.0+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:df7841f714dae0f853085f5c987c20ac:search

```yaml
regex_id: df7841f714dae0f853085f5c987c20ac
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/desktop-notification/hooks/hook-utils.sh:576:9"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e0337573864e077c56527a50a2605893:search

```yaml
regex_id: e0337573864e077c56527a50a2605893
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/repo-hygiene/skills/clean/scripts/clean-build.test.sh:78:3"
```

### Pattern

`^build`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e15637942403eddda4349ef553f0f157:search

```yaml
regex_id: e15637942403eddda4349ef553f0f157
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/block-dangerous-git.sh:1087:9"
```

### Pattern

`^-[A-Za-z]*e[A-Za-z]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e27b06c40a84a9f3cf15554f94fe7510:search

```yaml
regex_id: e27b06c40a84a9f3cf15554f94fe7510
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/eol-normalizer/hooks/hook-utils.sh:621:5"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e41e24dbeb09c58050b039f17dfffe9f:search

```yaml
regex_id: e41e24dbeb09c58050b039f17dfffe9f
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/desktop-notification/hooks/hook-utils.sh:1485:22"
```

### Pattern

`^[0-9]+([.][0-9]+)?(s|m|h|d)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e658d62b148a7fa91f5cf911a4e68da1:search

```yaml
regex_id: e658d62b148a7fa91f5cf911a4e68da1
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/markdown-format.test.sh:506:33"
```

### Pattern

`^- star item$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e72722e479041def4f97c3b02ac95ff6:search

```yaml
regex_id: e72722e479041def4f97c3b02ac95ff6
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-config/skills/audit-pass/scripts/run-state.sh:555:5"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e81b29cb4a6919e366dfc86260accec7:search

```yaml
regex_id: e81b29cb4a6919e366dfc86260accec7
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/autonomy/hooks/hook-utils.sh:950:5"
```

### Pattern

`^[a-zA-Z_][a-zA-Z0-9_]*(\[.*\])?\+?=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e85bf53e20cc71518e7a5f8d91ad7777:search

```yaml
regex_id: e85bf53e20cc71518e7a5f8d91ad7777
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/work-items/tools/work-item-tracker/adapters/local-markdown/claim.sh:33:0"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e86cd6611b98ce2ff5b531645085c5a3:search

```yaml
regex_id: e86cd6611b98ce2ff5b531645085c5a3
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/bash-format/hooks/bash-format.test.sh:331:3"
```

### Pattern

`^  echo hi$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e891c6163c287f2ca5a0b0d34fb3f43e:search

```yaml
regex_id: e891c6163c287f2ca5a0b0d34fb3f43e
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/planning/scripts/goal-condition-length.sh:29:2"
```

### Pattern

`^# Mechanical`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e89465e0d66d0c9d1c3afef0c1018df3:search

```yaml
regex_id: e89465e0d66d0c9d1c3afef0c1018df3
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/claude-ops/hooks/hook-utils.sh:621:5"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e8dd99b2fdf3964577017947d8e776cf:search

```yaml
regex_id: e8dd99b2fdf3964577017947d8e776cf
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/block-dangerous-git.sh:553:4"
```

### Pattern

`^:?[./*?]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e92b070e84890615fd4d285c9c9e92af:search

```yaml
regex_id: e92b070e84890615fd4d285c9c9e92af
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/hook-utils.sh:1348:18"
```

### Pattern

`^-[i0v](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e9812b96cd84c57803b1d0eef2cc9f1f:search

```yaml
regex_id: e9812b96cd84c57803b1d0eef2cc9f1f
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/powershell-format/hooks/hook-utils.sh:621:5"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e992ea3872c16d43651892f999dc124c:search

```yaml
regex_id: e992ea3872c16d43651892f999dc124c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/scripts/check-queue-front-matter.sh:89:9"
```

### Pattern

`^(${VALID_PRIORITIES})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e9f2298ca260c65ac37a0bab8812d47b:search

```yaml
regex_id: e9f2298ca260c65ac37a0bab8812d47b
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/block-hook-bypass.sh:767:5"
```

### Pattern

`^([A-Za-z]):(/.*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ea03e212f41bb5526215a5efac763a04:search

```yaml
regex_id: ea03e212f41bb5526215a5efac763a04
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/autonomy/hooks/lane-notify.test.sh:94:13"
```

### Pattern

`^ARG=\[lane`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:eba3657bbf3e9dc9ece30e07af10314a:search

```yaml
regex_id: eba3657bbf3e9dc9ece30e07af10314a
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/go-format/hooks/hook-utils.sh:629:60"
```

### Pattern

`^0+\.0+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ecc4164fdedd23395a86d1961fb566d8:search

```yaml
regex_id: ecc4164fdedd23395a86d1961fb566d8
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/plugin-quality/scripts/packet-seal.sh:72:2"
```

### Pattern

`^# Tamper-evidence`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ee4a96a8141d6482a17d638a9d4bbccf:search

```yaml
regex_id: ee4a96a8141d6482a17d638a9d4bbccf
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/rate-limit-guard/hooks/hook-utils.sh:576:9"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:eeae62e72e31c4deb54349fdc6bc74de:search

```yaml
regex_id: eeae62e72e31c4deb54349fdc6bc74de
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/autonomy/hooks/hook-utils.sh:574:46"
```

### Pattern

`^0+(\.0+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:eef1497fd53ddfa27a4f435734821618:search

```yaml
regex_id: eef1497fd53ddfa27a4f435734821618
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/typos-format/hooks/hook-utils.sh:629:60"
```

### Pattern

`^0+\.0+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ef9839d65ac68897e14eb789a6411f85:search

```yaml
regex_id: ef9839d65ac68897e14eb789a6411f85
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/context-guard/hooks/hook-utils.sh:1770:11"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f0ad4ddddf14ef17a9db46d98e6fc3d1:search

```yaml
regex_id: f0ad4ddddf14ef17a9db46d98e6fc3d1
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/hooks/hook-utils.sh:950:5"
```

### Pattern

`^[a-zA-Z_][a-zA-Z0-9_]*(\[.*\])?\+?=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f1133ce908b5b7fc3b28559c09696b4d:search

```yaml
regex_id: f1133ce908b5b7fc3b28559c09696b4d
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/hook-utils.sh:1485:22"
```

### Pattern

`^[0-9]+([.][0-9]+)?(s|m|h|d)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f1a3a736dcfc1ceb27b04e7a234fb9fc:search

```yaml
regex_id: f1a3a736dcfc1ceb27b04e7a234fb9fc
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/mcp-tools/skills/audit/scripts/discover.sh:165:11"
```

### Pattern

`^[[:space:]]*[A-Za-z_$][A-Za-z0-9_$]*\.(register)?[tT]ool\(`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f31ba993908dc50cd246256cb72f3274:search

```yaml
regex_id: f31ba993908dc50cd246256cb72f3274
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/skill-quality/scripts/check-skill.sh:632:5"
```

### Pattern

`^[0-9]{4}-[0-9]{2}-[0-9]{2}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f5167a5955656decef585fa7a2c73fc8:search

```yaml
regex_id: f5167a5955656decef585fa7a2c73fc8
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/hook-utils.sh:1770:11"
```

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f54de2718bb872a187c3041de29bce7c:search

```yaml
regex_id: f54de2718bb872a187c3041de29bce7c
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/planning/scripts/check-open-questions.sh:152:7"
```

### Pattern

`^[[:space:]]*-[[:space:]]+[Qq][0-9]+[[:space:]]*\|`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f69349c9dfd2e409fc304cf5a93aa844:search

```yaml
regex_id: f69349c9dfd2e409fc304cf5a93aa844
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/context-guard/hooks/hook-utils.sh:621:5"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f74059fa85c8750753afb76b163d9cbc:search

```yaml
regex_id: f74059fa85c8750753afb76b163d9cbc
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/docs-hygiene/skills/audit-encapsulation/scripts/detect.sh:152:9"
```

### Pattern

`^plugins/[^/]+/skills/([^/]+)/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f785901aac4d56d952b57a7d9355bb30:search

```yaml
regex_id: f785901aac4d56d952b57a7d9355bb30
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/source-control/hooks/hook-utils.sh:629:60"
```

### Pattern

`^0+\.0+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f93beeb88765af838ee3fa5ed5fd2688:search

```yaml
regex_id: f93beeb88765af838ee3fa5ed5fd2688
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/desktop-notification/hooks/hook-utils.sh:629:60"
```

### Pattern

`^0+\.0+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f95775d784930fb6e2f999d83fb97d46:search

```yaml
regex_id: f95775d784930fb6e2f999d83fb97d46
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/markdown-format/hooks/hook-utils.sh:950:5"
```

### Pattern

`^[a-zA-Z_][a-zA-Z0-9_]*(\[.*\])?\+?=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fb1a535adb96f685cbb889dcf5d4c596:search

```yaml
regex_id: fb1a535adb96f685cbb889dcf5d4c596
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/guardrails/hooks/cli-flag-verify.sh:316:29"
```

### Pattern

`^[[:space:]]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fbf505db4055c61107633bb43cdb2977:search

```yaml
regex_id: fbf505db4055c61107633bb43cdb2977
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/bash-format/hooks/hook-utils.sh:950:5"
```

### Pattern

`^[a-zA-Z_][a-zA-Z0-9_]*(\[.*\])?\+?=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fc62af09cd8b0d8353e9feab46a05b72:search

```yaml
regex_id: fc62af09cd8b0d8353e9feab46a05b72
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/wizard/skills/generate/template.sh:58:2"
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

## usage_mismatch:fca29548ecf0ee1a69d6aec3fceabc2d:search

```yaml
regex_id: fca29548ecf0ee1a69d6aec3fceabc2d
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/playbooks/skills/boris/scripts/update.sh:77:2"
```

### Pattern

`^metadata:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fdf13a7a23e5af53b5ffc70776794f4d:search

```yaml
regex_id: fdf13a7a23e5af53b5ffc70776794f4d
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/eol-normalizer/hooks/hook-utils.sh:576:9"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ff74382d9c25d1332101a36be4aa9ab5:search

```yaml
regex_id: ff74382d9c25d1332101a36be4aa9ab5
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/bash-format/hooks/hook-utils.sh:576:9"
```

### Pattern

`^([0-9]+)(\.([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ffc0f3d8aa0da1cbfdd7107ffc25cfac:search

```yaml
regex_id: ffc0f3d8aa0da1cbfdd7107ffc25cfac
schema_version: "1"
kind: usage_mismatch
corpus: claude-code-plugins
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/claude-code-plugins/rules/plugins/autonomy/hooks/lane-stop-gate.sh:339:5"
```

### Pattern

`^[[:space:]]*${SENTINEL_RE}[[:space:]]*$`

### Context

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
corpus: claude-code-plugins
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
corpus: claude-code-plugins
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
corpus: claude-code-plugins
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
corpus: claude-code-plugins
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

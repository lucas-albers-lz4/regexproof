---
schema_version: "1"
corpus: forge-cli
findings: 84
---

# forge-cli batch findings

## usage_mismatch:040763faebf6690be98c7d49ec0384a4:search

```yaml
regex_id: 040763faebf6690be98c7d49ec0384a4
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/forge/federation.py:112:19"
```

### Pattern

`^[A-Za-z0-9_.-]{1,64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:078eb65aea465936548026c91362e853:search

```yaml
regex_id: 078eb65aea465936548026c91362e853
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/build_runners/hooks/dlp_scan.py:34:12"
```

### Pattern

`^[^\s@]+@[^\s@]+\.[^\s@]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:096b5bfe7e3892d2d71fe81f98dae220:search

```yaml
regex_id: 096b5bfe7e3892d2d71fe81f98dae220
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/iac/providers/snowflake.py:551:17"
```

### Pattern

`^\s*USING\s+CRON\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:14f63d192ac04b50e143f45f0233d15c:search

```yaml
regex_id: 14f63d192ac04b50e143f45f0233d15c
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/copilot/missions/spec.py:75:19"
```

### Pattern

`^[a-z0-9][a-z0-9_-]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:16bb1f8911f18e0c730643e2a752f3af:search

```yaml
regex_id: 16bb1f8911f18e0c730643e2a752f3af
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/copilot/catalog/bigquery.py:91:15"
```

### Pattern

`^[A-Za-z][A-Za-z0-9-]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:17611532e0fd0f6f62eb3607c6b0ea68:match

```yaml
regex_id: 17611532e0fd0f6f62eb3607c6b0ea68
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/providers/gcp/util/names.py:337:15"
```

### Pattern

`^\d+\.\d+\.\d+\.\d+$`

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

## usage_mismatch:1a90906991e97ff25a4fbe06e34bbf27:match

```yaml
regex_id: 1a90906991e97ff25a4fbe06e34bbf27
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/cli/security.py:739:15"
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

## usage_mismatch:1d11b2739c1bdd39595b1f84bef39e5e:match

```yaml
regex_id: 1d11b2739c1bdd39595b1f84bef39e5e
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/providers/gcp/util/names.py:153:7"
```

### Pattern

`^\d+\.\d+\.\d+\.\d+$`

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

## usage_mismatch:1dafc8c3e882b01b0f4372d93fc32e14:search

```yaml
regex_id: 1dafc8c3e882b01b0f4372d93fc32e14
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/providers/snowflake/util/config.py:40:29"
```

### Pattern

`^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1e4a77f7941a434ca5b1bc56ccb3e5bb:search

```yaml
regex_id: 1e4a77f7941a434ca5b1bc56ccb3e5bb
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/copilot/missions/spec.py:73:14"
```

### Pattern

`^([A-Za-z_][A-Za-z0-9_-]*)(\[\*\])?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:210c6af1ce28f8c8d729a7acc75f14a3:search

```yaml
regex_id: 210c6af1ce28f8c8d729a7acc75f14a3
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/providers/quality_engine.py:199:16"
```

### Pattern

`^P(\d+)W$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:225d1cc789e436114ed3a194ac86cd8b:search

```yaml
regex_id: 225d1cc789e436114ed3a194ac86cd8b
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/scripts/e2e_all_modes.py:123:11"
```

### Pattern

`^sat_[a-z][a-z0-9_]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:250bcba5fce7f56ef6b3b4f5b1a686f1:search

```yaml
regex_id: 250bcba5fce7f56ef6b3b4f5b1a686f1
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/providers/_sql_safety.py:146:17"
```

### Pattern

`^[A-Za-z0-9_ ()',]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:32eda47591f7e5e804aba7ad2b5f254b:search

```yaml
regex_id: 32eda47591f7e5e804aba7ad2b5f254b
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/output_ports/mcp/query_compiler.py:1099:21"
```

### Pattern

`(?is)\blimit\s+(\d+)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:33636d602f0b5883d9adf881fd888f49:search

```yaml
regex_id: 33636d602f0b5883d9adf881fd888f49
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/scripts/e2e_all_modes.py:122:11"
```

### Pattern

`^hub_[a-z][a-z0-9_]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:33a96fb72ce6c0844aeeb065a251c6c3:search

```yaml
regex_id: 33a96fb72ce6c0844aeeb065a251c6c3
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/providers/aws/util/validation.py:41:28"
```

### Pattern

`^[a-z0-9_]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:35bef1aea2c793d87dd3fda59cd73584:search

```yaml
regex_id: 35bef1aea2c793d87dd3fda59cd73584
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/scripts/gemini_industry_scenarios.py:76:11"
```

### Pattern

`^lnk_[a-z][a-z0-9_]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:388c9b50c1443c817a24295d37cbdfc1:search

```yaml
regex_id: 388c9b50c1443c817a24295d37cbdfc1
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/cli/import_workflow/dbt.py:67:17"
```

### Pattern

`^[A-Za-z0-9_][A-Za-z0-9_.-]*[A-Za-z0-9_]$|^[A-Za-z0-9_]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3cff2ff73a965d86ec30496fd2616c26:search

```yaml
regex_id: 3cff2ff73a965d86ec30496fd2616c26
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/cli/forge_domain_enrichment.py:50:18"
```

### Pattern

`^[A-Za-z0-9][A-Za-z0-9._-]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3f5d479f1312f274f19cb58d4bbdf05b:search

```yaml
regex_id: 3f5d479f1312f274f19cb58d4bbdf05b
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/cli/forge_prompt_overlays.py:99:19"
```

### Pattern

`^[A-Za-z0-9][A-Za-z0-9._-]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:43436559697faf43beac13b492dc4d67:search

```yaml
regex_id: 43436559697faf43beac13b492dc4d67
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/scripts/e2e_all_modes.py:124:11"
```

### Pattern

`^lnk_[a-z][a-z0-9_]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:48d0c5dcd124756dca33176cfb220311:search

```yaml
regex_id: 48d0c5dcd124756dca33176cfb220311
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/providers/snowflake/util/config.py:39:22"
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

## usage_mismatch:490c09a3512b3c43f39f7c1b076f66b3:search

```yaml
regex_id: 490c09a3512b3c43f39f7c1b076f66b3
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/build_runners/hooks/dlp_scan.py:37:9"
```

### Pattern

`^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:49ba36b65dd15c2e5858cd42d59c804e:search

```yaml
regex_id: 49ba36b65dd15c2e5858cd42d59c804e
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/scripts/gemini_industry_scenarios.py:77:12"
```

### Pattern

`^fact_[a-z][a-z0-9_]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4c24ffd1f444114faf595eaf46538c3d:search

```yaml
regex_id: 4c24ffd1f444114faf595eaf46538c3d
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/cli/schedule_sync.py:99:17"
```

### Pattern

`^[A-Za-z0-9_.\-]{1,128}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4d61098051ed2fff41a97caf2570403e:search

```yaml
regex_id: 4d61098051ed2fff41a97caf2570403e
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/scripts/e2e_all_modes.py:126:11"
```

### Pattern

`^dim_[a-z][a-z0-9_]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4d998060f4598f4211f49ff0537e3712:search

```yaml
regex_id: 4d998060f4598f4211f49ff0537e3712
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/copilot/agents/ai_ready_agent.py:113:17"
```

### Pattern

`^[a-z0-9][a-z0-9-_.]*[a-z0-9]$|^[a-z0-9]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:561c94c85e9898fcee11c65640ab37a2:search

```yaml
regex_id: 561c94c85e9898fcee11c65640ab37a2
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/scripts/check_pinned_actions.py:65:11"
```

### Pattern

`^\s*"(?P<owner>[A-Za-z0-9_-]+)/(?P<repo>[A-Za-z0-9_/-]+)@(?P<tag>v[\w.]+)"\s*:\s*"[A-Za-z0-9_/-]+@(?P<sha>[0-9a-f]{40})"\s*,?\s*#\s*(?P<pinned_version>v[\S]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:56c3f8dcc535253c2ade4c2e5d999dfc:search

```yaml
regex_id: 56c3f8dcc535253c2ade4c2e5d999dfc
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/forge_datamodel/from_ddl/parser.py:57:21"
```

### Pattern

`^\s*([`"\[]?\w+[`"\]]?)\s+(\w+(?:<[^>]+>)?(?:\([^)]+\))?)\s*(.*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:570ef4138ea37b8a014d97af91ba0ee7:search

```yaml
regex_id: 570ef4138ea37b8a014d97af91ba0ee7
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/cli/discover/_jdbc_introspect.py:253:12"
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

## usage_mismatch:59f40c7a6952668c5cf9a4caad6f0470:search

```yaml
regex_id: 59f40c7a6952668c5cf9a4caad6f0470
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/iac/providers/snowflake.py:1232:16"
```

### Pattern

`^\s*\((.*?)\)\s*RETURNS\s+(.+?)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5ed7235f2bfc50ac5c6f0cb8245d2129:search

```yaml
regex_id: 5ed7235f2bfc50ac5c6f0cb8245d2129
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/build_runners/hooks/dlp_scan.py:36:10"
```

### Pattern

`^\d{3}-\d{2}-\d{4}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6412797324f8718f66510086c98e3a03:search

```yaml
regex_id: 6412797324f8718f66510086c98e3a03
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/copilot/catalog/bigquery.py:93:15"
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

## usage_mismatch:680362221d049bc140930d310b90f589:search

```yaml
regex_id: 680362221d049bc140930d310b90f589
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/providers/_sql_safety.py:135:26"
```

### Pattern

`^[0-9]+(\s*,\s*[0-9]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:693a0dcdf70cfe3bb9e58105bd3370af:search

```yaml
regex_id: 693a0dcdf70cfe3bb9e58105bd3370af
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/cli/discover/_jdbc_introspect.py:292:21"
```

### Pattern

`^\s*\(?\s*\w+\s+IS\s+NOT\s+NULL\s*\)?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6b333a0d6c2e0c162721de280dccea50:search

```yaml
regex_id: 6b333a0d6c2e0c162721de280dccea50
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/build_runners/meltano/runner.py:113:18"
```

### Pattern

`^target-[a-z0-9](?:[a-z0-9._-]*[a-z0-9])?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6cef6bc9870de051cafd512e2edccc05:match

```yaml
regex_id: 6cef6bc9870de051cafd512e2edccc05
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/llm/providers.py:1650:12"
```

### Pattern

`^([\d.]+)\s*([BM]?)$`

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

## usage_mismatch:724ba3f9daab8e75afe94527dc20fce0:match

```yaml
regex_id: 724ba3f9daab8e75afe94527dc20fce0
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/cli/forge_validation.py:150:11"
```

### Pattern

`^[a-z][a-z0-9-]*$`

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

## usage_mismatch:79b9935d783e5984af5230e95c94b8be:search

```yaml
regex_id: 79b9935d783e5984af5230e95c94b8be
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/forge_datamodel/from_ddl/parser.py:64:22"
```

### Pattern

`--\s*(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7c850765f427604243a58c80e44f5cd9:search

```yaml
regex_id: 7c850765f427604243a58c80e44f5cd9
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/providers/aws/util/validation.py:43:30"
```

### Pattern

`^[a-zA-Z0-9\-_]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7c8fab5bdb38bda984b516ac9be5b916:search

```yaml
regex_id: 7c8fab5bdb38bda984b516ac9be5b916
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/build_runners/dbt/runner.py:329:19"
```

### Pattern

`^\s*dbt\s+v?([0-9][\w.+-]*)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7d2e29b1c299bca71bb02b4ebf820bac:search

```yaml
regex_id: 7d2e29b1c299bca71bb02b4ebf820bac
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/scripts/gemini_industry_scenarios.py:75:11"
```

### Pattern

`^sat_[a-z][a-z0-9_]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:80c1336ab2f37705467dd0ab0ae7f8f6:search

```yaml
regex_id: 80c1336ab2f37705467dd0ab0ae7f8f6
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/providers/_sql_safety.py:20:14"
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

## usage_mismatch:83750a43be33f8c63c140bd0893df8cf:match

```yaml
regex_id: 83750a43be33f8c63c140bd0893df8cf
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/providers/gcp/util/names.py:149:11"
```

### Pattern

`^[a-z0-9][a-z0-9\-]*[a-z0-9]$`

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

## usage_mismatch:854073ebf77a8aaf8d82873a7d6c92b3:search

```yaml
regex_id: 854073ebf77a8aaf8d82873a7d6c92b3
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/build_runners/hooks/dlp_scan.py:35:12"
```

### Pattern

`^[+]?[\d\s\-().]{7,}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8556e5dcc76aa5a9ae362b4dfd97c0aa:search

```yaml
regex_id: 8556e5dcc76aa5a9ae362b4dfd97c0aa
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/build_runners/soda/runner.py:37:25"
```

### Pattern

`^\[\d{2}:\d{2}:\d{2}\]\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8682bb7ee2fc5f5a41e8e4409e4b76d9:search

```yaml
regex_id: 8682bb7ee2fc5f5a41e8e4409e4b76d9
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/copilot/agents/ai_ready_agent.py:119:14"
```

### Pattern

`(^|_)(id|uuid|guid|key|pk|sk)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8781a7050932ddaa6d76ec74560bbf7a:search

```yaml
regex_id: 8781a7050932ddaa6d76ec74560bbf7a
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/scripts/e2e_all_modes.py:125:12"
```

### Pattern

`^fact_[a-z][a-z0-9_]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:896df97bb82ed9bf608e33ab7a4a8fc6:search

```yaml
regex_id: 896df97bb82ed9bf608e33ab7a4a8fc6
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/forge_datamodel/semantics_builder.py:49:21"
```

### Pattern

`(?is)^\s*(sum|avg|min|max|median|count)\s*\((.*)\)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:93c29ba02504f11708534e69e49d97c6:search

```yaml
regex_id: 93c29ba02504f11708534e69e49d97c6
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/scripts/gemini_industry_scenarios.py:74:11"
```

### Pattern

`^hub_[a-z][a-z0-9_]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9560afa7f0765c76337015eb89de1d56:search

```yaml
regex_id: 9560afa7f0765c76337015eb89de1d56
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/iac/providers/snowflake.py:550:14"
```

### Pattern

`^\s*(\d+)\s*MINUTES?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9a566fc7cffa3d29824d05e5b90aac1f:search

```yaml
regex_id: 9a566fc7cffa3d29824d05e5b90aac1f
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/providers/aws/util/validation.py:40:24"
```

### Pattern

`^[a-z0-9][a-z0-9\-]{1,61}[a-z0-9]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9b0c99b40bb1c685b36beb3d54ed4d2a:search

```yaml
regex_id: 9b0c99b40bb1c685b36beb3d54ed4d2a
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/build_runners/meltano/runner.py:112:15"
```

### Pattern

`^tap-[a-z0-9](?:[a-z0-9._-]*[a-z0-9])?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9de942625e43f8a6c56af6b74c23e70c:search

```yaml
regex_id: 9de942625e43f8a6c56af6b74c23e70c
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/cli/import_workflow/dbt.py:1182:26"
```

### Pattern

`^\{\{\s*(?:Dimension|TimeDimension|Entity|Metric)\s*\(`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a0dbda08cbb26345162762eecb5457b2:search

```yaml
regex_id: a0dbda08cbb26345162762eecb5457b2
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/observability/secret_redactor.py:230:30"
```

### Pattern

`(?ix)\b(?:[A-Za-z0-9_]*_)?(?:api[_-]?key|authorization|aws_secret_access_key|secret[_-]access[_-]key|client_secret|credentials?|oauth[_-]?token|password|passphrase|private[_-]?key(?:_passphrase)?|session[_-]token|secret|token)\b\s*[:=]\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a64a21ffb63175304f6d753c5a373909:search

```yaml
regex_id: a64a21ffb63175304f6d753c5a373909
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/scripts/gemini_industry_scenarios.py:78:11"
```

### Pattern

`^dim_[a-z][a-z0-9_]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:aa87dbfef6c674a76da279ca802eed5e:search

```yaml
regex_id: aa87dbfef6c674a76da279ca802eed5e
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/copilot/catalog/bigquery.py:94:13"
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

## usage_mismatch:ac2899a44d3f1536a7a84d4a55ca5448:search

```yaml
regex_id: ac2899a44d3f1536a7a84d4a55ca5448
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/cli/_untrusted_content.py:50:15"
```

### Pattern

`^\s*(?:#{1,}\s*)?(system|assistant|user|developer|tool|function)\s*[:>\]]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ac3450cbc3862fa5c599bd0faff1b7d2:match

```yaml
regex_id: ac3450cbc3862fa5c599bd0faff1b7d2
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/providers/aws/util/validation.py:103:11"
```

### Pattern

`^\d+\.\d+\.\d+\.\d+$`

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

## usage_mismatch:ad2ddf6e76fb03c23bb2674ed982ab8d:search

```yaml
regex_id: ad2ddf6e76fb03c23bb2674ed982ab8d
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/scripts/check_pinned_actions.py:42:19"
```

### Pattern

`^\s*-?\s*uses:\s*(?P<action>[A-Za-z0-9][A-Za-z0-9._-]*/[A-Za-z0-9._/-]+)@(?P<ref>[^\s#]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bc76f5b3f9d042e26ebb1d8b59f572f6:search

```yaml
regex_id: bc76f5b3f9d042e26ebb1d8b59f572f6
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/build_runners/hooks/dlp_scan.py:38:10"
```

### Pattern

`^https?://`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c57b7bcbb84416fb5c1ef93d65a72064:match

```yaml
regex_id: c57b7bcbb84416fb5c1ef93d65a72064
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/providers/gcp/util/names.py:347:19"
```

### Pattern

`^[a-zA-Z][a-zA-Z0-9\-\._~%+]*$`

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

## usage_mismatch:c674d66268d2ddd113a272c51af28673:search

```yaml
regex_id: c674d66268d2ddd113a272c51af28673
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/cli/import_workflow/dbt.py:1603:10"
```

### Pattern

`^[a-z0-9][a-z0-9-]*[a-z0-9]$|^[a-z0-9]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c840c16813cb1b11cb0cd76e6837c5b5:search

```yaml
regex_id: c840c16813cb1b11cb0cd76e6837c5b5
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/providers/aws/util/validation.py:42:25"
```

### Pattern

`^[a-z0-9_]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cb28f419d47f43143fd9b7521a50e172:search

```yaml
regex_id: cb28f419d47f43143fd9b7521a50e172
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/cli/forge_copilot_schema_inference.py:528:17"
```

### Pattern

`^\s+[`\"\[]?(\w+)[`\"\]]?\s+([\w()]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cb6b76c58a777ab4f33993016ceb3989:match

```yaml
regex_id: cb6b76c58a777ab4f33993016ceb3989
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/cli/_init_dag_helpers.py:105:15"
```

### Pattern

`^[@a-zA-Z0-9_ */,-]+$`

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

## usage_mismatch:d232070cb25c2dfb2ea6c3d87088281c:search

```yaml
regex_id: d232070cb25c2dfb2ea6c3d87088281c
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/build_runners/soda/runner.py:41:18"
```

### Pattern

`^(?P<count>\d+)/(?P<total>\d+)\s+checks?\s+(?P<outcome>PASSED|WARNED|FAILED|NOT EVALUATED)\s*:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d75518d6819dc3cc7dc39f60cee737a6:search

```yaml
regex_id: d75518d6819dc3cc7dc39f60cee737a6
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/forge_datamodel/semantics_builder.py:52:22"
```

### Pattern

`(?is)^\s*distinct\s+(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d940e7ad88574ce7fc8bf774a8be76a3:match

```yaml
regex_id: d940e7ad88574ce7fc8bf774a8be76a3
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/providers/gcp/util/names.py:335:19"
```

### Pattern

`^[a-z0-9][a-z0-9\-]*[a-z0-9]$`

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

## usage_mismatch:ddca3e2537dff97db0a6bdad0d877f64:match

```yaml
regex_id: ddca3e2537dff97db0a6bdad0d877f64
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/providers/gcp/util/names.py:327:19"
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

## usage_mismatch:defa2432cc04532bfe9945f4515de2e4:search

```yaml
regex_id: defa2432cc04532bfe9945f4515de2e4
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/providers/quality_engine.py:192:15"
```

### Pattern

`^(\d+)\s*([smhd])$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e58f2e263395931b34b334e47099eae6:match

```yaml
regex_id: e58f2e263395931b34b334e47099eae6
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/cli/forge_validation.py:49:11"
```

### Pattern

`^[a-z][a-z0-9-]*[a-z0-9]$`

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

## usage_mismatch:e5e85f15198999cad25790d7dd4102fe:search

```yaml
regex_id: e5e85f15198999cad25790d7dd4102fe
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/providers/quality_engine.py:44:14"
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

## usage_mismatch:e848cd1315823a77380ee8c8cc67dbc9:search

```yaml
regex_id: e848cd1315823a77380ee8c8cc67dbc9
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/scripts/check_pinned_actions.py:50:9"
```

### Pattern

`^[0-9a-f]{40}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ebc2093b33a724cd62786833944b8811:search

```yaml
regex_id: ebc2093b33a724cd62786833944b8811
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/providers/gcp/plan/planner.py:39:18"
```

### Pattern

`^[a-z][a-z0-9-]{4,28}[a-z0-9]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f44b308a3b3a7c610739e41af97baee1:search

```yaml
regex_id: f44b308a3b3a7c610739e41af97baee1
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/providers/_sql_safety.py:31:19"
```

### Pattern

`^[A-Za-z0-9_\s().,<>=!'+\-*/%|&\"`:\[\]]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f98fdf6e66e5786a2dd35918a5558556:search

```yaml
regex_id: f98fdf6e66e5786a2dd35918a5558556
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/cli/import_workflow/dbt.py:1039:19"
```

### Pattern

`^P(?!$)(\d+Y)?(\d+M)?(\d+W)?(\d+D)?(T(\d+H)?(\d+M)?(\d+S)?)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fda5c91a66cfe1c08ae9cc86e3418e56:match

```yaml
regex_id: fda5c91a66cfe1c08ae9cc86e3418e56
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/providers/gcp/util/names.py:357:19"
```

### Pattern

`^[a-z][a-z0-9\-]*[a-z0-9]$`

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

## usage_mismatch:fe1446367e29d6ba62a70b5e0b10e834:search

```yaml
regex_id: fe1446367e29d6ba62a70b5e0b10e834
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/providers/snowflake/util/config.py:38:19"
```

### Pattern

`\.snowflakecomputing\.com$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ff1ec574449615ae28655b26b4290186:search

```yaml
regex_id: ff1ec574449615ae28655b26b4290186
schema_version: "1"
kind: usage_mismatch
corpus: forge-cli
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/forge-cli/rules/fluid_build/cli/schedule_sync.py:507:25"
```

### Pattern

`^(.+?)\s*<([^<>@\s]+@[^<>@\s]+)>$`

### Context

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
corpus: forge-cli
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
corpus: forge-cli
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
corpus: forge-cli
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
corpus: forge-cli
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

---
schema_version: "1"
corpus: bernstein
findings: 242
---

# bernstein batch findings

## usage_mismatch:0009ab816e66eba01834b2a3339326e9:search

```yaml
regex_id: 0009ab816e66eba01834b2a3339326e9
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/evolution/detector.py:577:19"
```

### Pattern

`^#\s+\d+\s+-\s+(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0049f5a14cb1bfab78f61cf358ae27d6:search

```yaml
regex_id: 0049f5a14cb1bfab78f61cf358ae27d6
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/datasources/connection.py:30:9"
```

### Pattern

`^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,63}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:006d36eab0f07b9ec3c9dd13127494f2:search

```yaml
regex_id: 006d36eab0f07b9ec3c9dd13127494f2
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sensitive_file_detector.py:126:5"
```

### Pattern

`(^|/)\.token$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:01dbe4e2c41385e51a139dff1aec1a53:search

```yaml
regex_id: 01dbe4e2c41385e51a139dff1aec1a53
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/readme_reminder.py:55:22"
```

### Pattern

`^\+\+\+ b/(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0250755e9961b11c94000bebd6eaf0a5:search

```yaml
regex_id: 0250755e9961b11c94000bebd6eaf0a5
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/cli/display/changelog_display.py:46:13"
```

### Pattern

`^\s*[-*]\s+(.*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:04284cb6633dd19352759485455f75a6:search

```yaml
regex_id: 04284cb6633dd19352759485455f75a6
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/tokens/template_compress_validate.py:103:49"
```

### Pattern

`^## Done signal \(completion contract [\w./-]+\)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:042d918278c61f614fe284e0036d715f:search

```yaml
regex_id: 042d918278c61f614fe284e0036d715f
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/tasks/param_contract.py:80:22"
```

### Pattern

`^[a-z][a-z0-9_]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:048156e2fc017434a05f69837ca994be:search

```yaml
regex_id: 048156e2fc017434a05f69837ca994be
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/tui/log_viewer.py:144:14"
```

### Pattern

`^#{1,6} `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:049ec4cec39b2db3665052b94f0711a7:search

```yaml
regex_id: 049ec4cec39b2db3665052b94f0711a7
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/agents/agent_log_aggregator.py:44:16"
```

### Pattern

`^\[?(?P<ts>\d{4}-\d{2}-\d{2}[ T][^\]\s]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:051266ae5cd5faa6b51d644129bcd7be:search

```yaml
regex_id: 051266ae5cd5faa6b51d644129bcd7be
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/scripts/format_release_notes.py:54:9"
```

### Pattern

`^(?P<type>[a-z]+)(?:\((?P<scope>[^)\n]+)\))?!?: (?P<subject>[^\n]+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:061d4886e4156a71676a5ecca1eb53fb:search

```yaml
regex_id: 061d4886e4156a71676a5ecca1eb53fb
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/config/seed_parser.py:70:13"
```

### Pattern

`^\$(\d+(?:\.\d+)?)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:070e78bb1f3dd118822c4b950a116684:search

```yaml
regex_id: 070e78bb1f3dd118822c4b950a116684
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sensitive_file_detector.py:107:5"
```

### Pattern

`.*\.cer$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:085cf4d133a170866f5051fed726fd84:search

```yaml
regex_id: 085cf4d133a170866f5051fed726fd84
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/observability/promptware_metrics.py:57:36"
```

### Pattern

`^[A-Za-z0-9_.\-]{1,32}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0899bddb9f52f9bc613bc1203fec310a:search

```yaml
regex_id: 0899bddb9f52f9bc613bc1203fec310a
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/skills/catalog/revocation.py:52:19"
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

## usage_mismatch:0a3483f19a356e3c12dbe47a017a6709:search

```yaml
regex_id: 0a3483f19a356e3c12dbe47a017a6709
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/scripts/gen_distribution_manifests.py:47:21"
```

### Pattern

`^date-released:.*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0ac4230b3598273e4faf39aeb7229b45:search

```yaml
regex_id: 0ac4230b3598273e4faf39aeb7229b45
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/orchestration/watchdog.py:77:4"
```

### Pattern

`are you sure\?\s*\[y/n\]\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0b2a1fc1d7877149a6c5570401516376:search

```yaml
regex_id: 0b2a1fc1d7877149a6c5570401516376
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/planning/spec_quality.py:184:27"
```

### Pattern

`^\s{0,3}#{1,6}\s*out[\s-]+of[\s-]+scope\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0b4082a1a9d3eaa2c4666095b1790911:search

```yaml
regex_id: 0b4082a1a9d3eaa2c4666095b1790911
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sensitive_file_detector.py:132:5"
```

### Pattern

`(^|/)kubeconfig$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0bd9f378bdad9cecffa454438142215b:search

```yaml
regex_id: 0bd9f378bdad9cecffa454438142215b
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/gitlab_app/slash_commands.py:18:12"
```

### Pattern

`^[ \t]*/bernstein[ \t]+(\w+)(?:[ \t]+([^\r\n]*))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0be6d9aea0f600a7d070a8859d538730:search

```yaml
regex_id: 0be6d9aea0f600a7d070a8859d538730
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/cli/commands/changelog_cmd.py:20:11"
```

### Pattern

`^(?P<type>feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)(?:\((?P<scope>[^)]+)\))?(?P<breaking>!)?:\s*(?P<desc>.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0c89646b5ab748bfc657135a57307946:search

```yaml
regex_id: 0c89646b5ab748bfc657135a57307946
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/scripts/gen_distribution_manifests.py:46:15"
```

### Pattern

`^version:.*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0d8e928906925697090488327c38b17f:search

```yaml
regex_id: 0d8e928906925697090488327c38b17f
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/git/git_basic.py:825:15"
```

### Pattern

`^new file mode`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0e31dfbe0cbc940b380d470a8463f328:search

```yaml
regex_id: 0e31dfbe0cbc940b380d470a8463f328
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/changelog_generator.py:37:18"
```

### Pattern

`^-\s*def\s+([a-zA-Z]\w*)\s*\(`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0e3b2933abd86c806bde93890c459c7c:search

```yaml
regex_id: 0e3b2933abd86c806bde93890c459c7c
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/streaming_merge.py:83:4"
```

### Pattern

`(?m)^---+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:10b57376da669ab42d18fd485ba9c552:search

```yaml
regex_id: 10b57376da669ab42d18fd485ba9c552
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/dead_code_detector.py:25:16"
```

### Pattern

`^-\s*class\s+(\w+)\s*[:(]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:115ac7f2f1f65dedb4f628835878815f:search

```yaml
regex_id: 115ac7f2f1f65dedb4f628835878815f
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/eval/clean_run.py:97:23"
```

### Pattern

`^sha256:[0-9a-f]{64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:121c88e13a9431fff51e45c755291d75:search

```yaml
regex_id: 121c88e13a9431fff51e45c755291d75
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/eval/calibration.py:64:39"
```

### Pattern

`^\s*(\d+)\s*([smhdw])\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1671d8247aabeea942855ed0efa47899:search

```yaml
regex_id: 1671d8247aabeea942855ed0efa47899
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/observability/log_search.py:36:16"
```

### Pattern

`^\[?(?P<ts>\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}:\d{2}(?:\.\d+)?[Z+-]?(?:\d{2}:\d{2})?)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:17ce7d7aa255116e2dc277ae749dfeed:search

```yaml
regex_id: 17ce7d7aa255116e2dc277ae749dfeed
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/fleet/prometheus_proxy.py:29:11"
```

### Pattern

`^# HELP ([^ ]+) (.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1813bc18b19798272b1034d311e499d7:search

```yaml
regex_id: 1813bc18b19798272b1034d311e499d7
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/tui/log_viewer.py:148:17"
```

### Pattern

`^> `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:184066eda6572c06023fdb765d050d33:search

```yaml
regex_id: 184066eda6572c06023fdb765d050d33
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/license_scanner.py:85:16"
```

### Pattern

`^diff --git a/(.+?) b/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1d2bdc1e12a3a4a177835b8beffbeb3d:search

```yaml
regex_id: 1d2bdc1e12a3a4a177835b8beffbeb3d
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/vuln_disclosure.py:160:24"
```

### Pattern

`^[A-Za-z0-9_.-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1dbcc358487499ac1742dbc30f2e6347:search

```yaml
regex_id: 1dbcc358487499ac1742dbc30f2e6347
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/scripts/text_to_sarif.py:52:15"
```

### Pattern

`^(?P<path>[^:]+):(?P<line>\d+):(?P<col>\d+):\s*(?P<code>[A-Z]\d+):\s*(?P<msg>.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1dea7092738bce26d24c094be85382f6:search

```yaml
regex_id: 1dea7092738bce26d24c094be85382f6
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/git/snapshot.py:76:18"
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

## usage_mismatch:2229291db8327a2ba795a532aef0dcba:search

```yaml
regex_id: 2229291db8327a2ba795a532aef0dcba
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/comment_quality.py:57:20"
```

### Pattern

`^\s*([A-Z][A-Za-z ]+)[ \t]*\n[ \t]*[-=]+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:24e7f8bf17223f42e7fe9a7914fe73f9:search

```yaml
regex_id: 24e7f8bf17223f42e7fe9a7914fe73f9
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sensitive_file_detector.py:104:5"
```

### Pattern

`.*\.jks$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:253d0e7af334ab64b9b9406e364df39e:search

```yaml
regex_id: 253d0e7af334ab64b9b9406e364df39e
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/scripts/format_release_notes.py:50:20"
```

### Pattern

` \((?:audit|rt)-\d+\)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:259bf7652c90ff81a5907b230763a4ba:search

```yaml
regex_id: 259bf7652c90ff81a5907b230763a4ba
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/teams/manifest.py:71:17"
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

## usage_mismatch:25b5453b1c9460f64803791fed9e2ee8:search

```yaml
regex_id: 25b5453b1c9460f64803791fed9e2ee8
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/replay/diagnose_signals.py:73:14"
```

### Pattern

`^[A-Za-z0-9._-]{1,64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:26a26c69bded9406e6d29c7cfffa4d11:search

```yaml
regex_id: 26a26c69bded9406e6d29c7cfffa4d11
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/arch_conformance.py:77:20"
```

### Pattern

`^\+\+\+ b/(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:26cb193f51aa76263bc719fd4fe84780:search

```yaml
regex_id: 26cb193f51aa76263bc719fd4fe84780
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/server/hooks_receiver.py:54:22"
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

## usage_mismatch:28e0710cc88a45be02c7f6157403f31f:search

```yaml
regex_id: 28e0710cc88a45be02c7f6157403f31f
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/evidence/run_artifacts.py:83:10"
```

### Pattern

`^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}\Z`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:28eaa65cbc52db502a07c2d61944ca21:search

```yaml
regex_id: 28eaa65cbc52db502a07c2d61944ca21
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/sandbox/pool_registry.py:34:16"
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

## usage_mismatch:29005b87ab1798d02f48864421436738:search

```yaml
regex_id: 29005b87ab1798d02f48864421436738
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/knowledge/readme_l10n.py:52:12"
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

## usage_mismatch:2a397eb4d0b2f13750c22b3a27d208f6:match

```yaml
regex_id: 2a397eb4d0b2f13750c22b3a27d208f6
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/compliance.py:500:8"
```

### Pattern

`^(\d{4})$`

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

## usage_mismatch:2a3ab86e3eb89b4a756a88cb944d400a:search

```yaml
regex_id: 2a3ab86e3eb89b4a756a88cb944d400a
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/orchestration/run_changelog.py:75:4"
```

### Pattern

`^-\s*@(click\.command|app\.route|router\.(get|post|put|delete|patch))`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2bffebec33cbd0783b9e6addc55e8b31:search

```yaml
regex_id: 2bffebec33cbd0783b9e6addc55e8b31
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/git/merge_queue.py:75:17"
```

### Pattern

`^[ \t]{1,20}(?:base|our|their)[ \t]{1,10}\d+[ \t]{1,10}[0-9a-f]+[ \t]{1,10}(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2cfeda068d90eb610ffcdd62459259c8:search

```yaml
regex_id: 2cfeda068d90eb610ffcdd62459259c8
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/adapters/admission.py:288:19"
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

## usage_mismatch:2e8c61fb0ad4780ecdd15f439ac15cb0:search

```yaml
regex_id: 2e8c61fb0ad4780ecdd15f439ac15cb0
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/plugins_core/plugin_manifest.py:26:18"
```

### Pattern

`^[a-zA-Z0-9][a-zA-Z0-9_-]{0,63}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:32eda0b83a23ab61be6dfe7209ee9966:search

```yaml
regex_id: 32eda0b83a23ab61be6dfe7209ee9966
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sensitive_file_detector.py:102:5"
```

### Pattern

`.*\.p12$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:330c54dd2daf75f3384b2a7a2cbb6774:search

```yaml
regex_id: 330c54dd2daf75f3384b2a7a2cbb6774
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/routes/review_board.py:92:38"
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

## usage_mismatch:337702b68083debc28d8873251d305a6:search

```yaml
regex_id: 337702b68083debc28d8873251d305a6
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/auth_middleware.py:199:31"
```

### Pattern

`^(?:/api/v\d+)?/tasks/(?P<segment>[^/{}]+)(?:/.*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:34dabc649330153f17504898acdf35c2:search

```yaml
regex_id: 34dabc649330153f17504898acdf35c2
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/tasks/backlog_parser.py:315:19"
```

### Pattern

`^[-*]\s+\[[ xX]\]\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:359f1250fb9faf67c55397c465451acc:search

```yaml
regex_id: 359f1250fb9faf67c55397c465451acc
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/agents/agent_log_aggregator.py:60:26"
```

### Pattern

`^(?:Modified|Created|Wrote|Updated):\s+\S+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:36ad537ff3be7e3133aff757806535c6:match

```yaml
regex_id: 36ad537ff3be7e3133aff757806535c6
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/sdk/python/src/bernstein_sdk/adapters/jira.py:150:15"
```

### Pattern

`^[A-Z][A-Z0-9_]+-\d+$`

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

## usage_mismatch:36f838e5a72faf7844d1e144e8731bd6:search

```yaml
regex_id: 36f838e5a72faf7844d1e144e8731bd6
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/git/git_basic.py:826:13"
```

### Pattern

`^rename from`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:39cb6ed78d2cafb1fcaa2f7bc9df4872:search

```yaml
regex_id: 39cb6ed78d2cafb1fcaa2f7bc9df4872
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/fleet/prometheus_proxy.py:30:11"
```

### Pattern

`^# TYPE ([^ ]+) (.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3b003140844da526f132f0b51d28a29f:search

```yaml
regex_id: 3b003140844da526f132f0b51d28a29f
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/scripts/build_copr_srpm.py:31:18"
```

### Pattern

`(?m)^Version:(?P<pad>[ \t]+)\S+[ \t]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3b3b533eb695ad440ee81dbf867924da:search

```yaml
regex_id: 3b3b533eb695ad440ee81dbf867924da
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/tokens/template_compression.py:93:41"
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

## usage_mismatch:3dd4de58f4227858d9dafbbd8959b19b:search

```yaml
regex_id: 3dd4de58f4227858d9dafbbd8959b19b
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/scripts/build_copr_srpm.py:36:23"
```

### Pattern

`(?m)^%global(?P<pad>[ \t]+)pypi_version[ \t]+\S+[ \t]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3ec811086784313947709ebfe665a693:search

```yaml
regex_id: 3ec811086784313947709ebfe665a693
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/scripts/check_context_staleness.py:99:20"
```

### Pattern

`^[0-9a-f]{40}\t`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4206df1c1444719a7d2c22c230ff51ac:search

```yaml
regex_id: 4206df1c1444719a7d2c22c230ff51ac
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/verifier_ladder.py:70:11"
```

### Pattern

`^sha256:[0-9a-f]{64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:421780e925c7a8ae09c485694c80c23e:search

```yaml
regex_id: 421780e925c7a8ae09c485694c80c23e
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/janitor.py:1825:4"
```

### Pattern

`^\s*git\s+rev-parse\s+--verify\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4335b5ee38a76c5e00c791da64c2e1f5:search

```yaml
regex_id: 4335b5ee38a76c5e00c791da64c2e1f5
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/workflows/workflow_spec.py:60:19"
```

### Pattern

`^\d+\.\d+(?:\.\d+)?(?:-[A-Za-z0-9.-]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:45378eb8c40e2b3e3fb0522d2f4d8140:search

```yaml
regex_id: 45378eb8c40e2b3e3fb0522d2f4d8140
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/streaming_merge.py:84:4"
```

### Pattern

`(?m)^```(?:python|javascript|typescript|yaml|json)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4549d6dc3156fc928457ad9ad90fdbea:search

```yaml
regex_id: 4549d6dc3156fc928457ad9ad90fdbea
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/replay/diagnose_signals.py:72:19"
```

### Pattern

`^sha256:[0-9a-f]{64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:45ff2694d0515fde2d9e409d0b845a8d:search

```yaml
regex_id: 45ff2694d0515fde2d9e409d0b845a8d
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/routes/agents.py:30:17"
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

## usage_mismatch:46147b09d5e22059fb0bcad9059f6f60:search

```yaml
regex_id: 46147b09d5e22059fb0bcad9059f6f60
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sensitive_file_detector.py:124:5"
```

### Pattern

`(^|/)id_(rsa|dsa|ecdsa|ed25519)\.pub$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:469b03ac56fb2c7e8e05511f423c5ec0:search

```yaml
regex_id: 469b03ac56fb2c7e8e05511f423c5ec0
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/arch_conformance.py:80:21"
```

### Pattern

`^\+(?!\+\+)\s*(?:from\s+([\w.]+)|import\s+([\w.,\s]+))`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4934b7abde9db41920f457d5468c0f31:search

```yaml
regex_id: 4934b7abde9db41920f457d5468c0f31
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/dead_code_detector.py:26:17"
```

### Pattern

`^\+\s*(?:async\s+)?def\s+(\w+)\s*\(`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4bbf1db1aca106535ae1151ac1f44cac:search

```yaml
regex_id: 4bbf1db1aca106535ae1151ac1f44cac
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/tui/log_viewer.py:23:22"
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

## usage_mismatch:4c77083932a9cf9cc90afc2c31c7a48c:search

```yaml
regex_id: 4c77083932a9cf9cc90afc2c31c7a48c
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/tui/diff_folding.py:60:11"
```

### Pattern

`^@@ -(\d+),?(\d*) \+(\d+),?(\d*) @@(.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4d3bc4f3f6818e742d6dee479ba40087:search

```yaml
regex_id: 4d3bc4f3f6818e742d6dee479ba40087
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sensitive_file_detector.py:108:5"
```

### Pattern

`.*\.der$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4e35f9d9a61358a05674d77d5cfb0348:search

```yaml
regex_id: 4e35f9d9a61358a05674d77d5cfb0348
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/replay/diagnosis_receipt.py:83:13"
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

## usage_mismatch:4f4dd9e984512c4d193a94cd54be4c5d:search

```yaml
regex_id: 4f4dd9e984512c4d193a94cd54be4c5d
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/routes/review_board.py:87:37"
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

## usage_mismatch:51994c4c58ee296e0bd14eea12b7062f:search

```yaml
regex_id: 51994c4c58ee296e0bd14eea12b7062f
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/comment_quality.py:211:20"
```

### Pattern

`^\s*Returns?:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5208bc28ef4dfabe68b07e0b15d8a600:search

```yaml
regex_id: 5208bc28ef4dfabe68b07e0b15d8a600
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/run_closure.py:24:13"
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

## usage_mismatch:53b822edf1bf1fe61b6501ae5b08b413:search

```yaml
regex_id: 53b822edf1bf1fe61b6501ae5b08b413
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/orchestration/watchdog.py:76:4"
```

### Pattern

`proceed\?\s*\[y/n\]\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:53ecf1511e6a8e380d236307689d8d1a:search

```yaml
regex_id: 53ecf1511e6a8e380d236307689d8d1a
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/scripts/check_routes_broad_except.py:36:16"
```

### Pattern

`^\s*except\s+Exception\s*(?:as\s+\w+)?\s*:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:555111af1c522b9d2908e69adf98a53b:search

```yaml
regex_id: 555111af1c522b9d2908e69adf98a53b
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/orchestration/browser_check.py:77:10"
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

## usage_mismatch:5555af2924276fe14697b39e9dc4247d:search

```yaml
regex_id: 5555af2924276fe14697b39e9dc4247d
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/cli/display/changelog_display.py:42:15"
```

### Pattern

`^\s*[-*]\s*(?:BREAKING:\s*|⚠\s*)(.*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:55974520d6469ec68d2e56724b39353c:search

```yaml
regex_id: 55974520d6469ec68d2e56724b39353c
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sandbox_eval.py:103:20"
```

### Pattern

`^https://github\.com/[A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+/?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:55d7eb50a2f6364c625505437638a614:search

```yaml
regex_id: 55d7eb50a2f6364c625505437638a614
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/git/snapshot.py:79:14"
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

## usage_mismatch:55dcf8efacdef2d2da798574b0042d0a:search

```yaml
regex_id: 55dcf8efacdef2d2da798574b0042d0a
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/comment_quality.py:220:20"
```

### Pattern

`^\s*Raises?:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:581ffa164126010f07daa996e37293a3:search

```yaml
regex_id: 581ffa164126010f07daa996e37293a3
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/skills/manifest.py:36:33"
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

## usage_mismatch:588656492a3e3c5500b9fa31204f8acc:search

```yaml
regex_id: 588656492a3e3c5500b9fa31204f8acc
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/planning/workflow_importer.py:31:15"
```

### Pattern

`^[ \t]{0,20}[-*][ \t]{1,5}\[[ \t]+\][ \t]{1,5}(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:59cb05cbd569675bae720b53f5dd23df:search

```yaml
regex_id: 59cb05cbd569675bae720b53f5dd23df
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/compliance/ai_bom.py:64:13"
```

### Pattern

`^sha256:[0-9a-f]{64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5a2331ada251ca2560c6d043e771636a:search

```yaml
regex_id: 5a2331ada251ca2560c6d043e771636a
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/tasks/auto_spawn_guard.py:53:18"
```

### Pattern

`[\[(][0-9a-f-]{6,}[\])]\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5a9c945289b7beac56079bd14a5cf0f2:search

```yaml
regex_id: 5a9c945289b7beac56079bd14a5cf0f2
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/orchestration/run_changelog.py:74:4"
```

### Pattern

`^-\s*(def |class )[A-Za-z]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5b27c46c86eef9f627b4ff753d184d21:search

```yaml
regex_id: 5b27c46c86eef9f627b4ff753d184d21
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sensitive_file_detector.py:121:5"
```

### Pattern

`(^|/)\.netrc$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5cc53602f824b3abcdde723ee93b8105:search

```yaml
regex_id: 5cc53602f824b3abcdde723ee93b8105
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sensitive_file_detector.py:131:5"
```

### Pattern

`(^|/)\.azure/.*\.json$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5f593a99c71edbc24f411ad2ee0e0bdd:search

```yaml
regex_id: 5f593a99c71edbc24f411ad2ee0e0bdd
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/git/git_basic.py:827:13"
```

### Pattern

`^deleted file mode`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5fa8b7cc6455631859be488437e1ecde:search

```yaml
regex_id: 5fa8b7cc6455631859be488437e1ecde
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/server/webhook_signatures.py:9:17"
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

## usage_mismatch:5fbf79b22feffd426d7bab09b05d0f92:search

```yaml
regex_id: 5fbf79b22feffd426d7bab09b05d0f92
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/sandbox/pool_placement.py:49:21"
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

## usage_mismatch:61e88101bdc68708dbf6b4730b7b15a0:search

```yaml
regex_id: 61e88101bdc68708dbf6b4730b7b15a0
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/planning/lifecycle.py:87:41"
```

### Pattern

`^(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>[a-z0-9][a-z0-9-]*?)(?:-(?P<hash>[0-9a-f]{6}))?\.yaml$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:644dd476b5abf35bffbd9d88d66ae566:search

```yaml
regex_id: 644dd476b5abf35bffbd9d88d66ae566
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/knowledge/readme_l10n.py:51:14"
```

### Pattern

`^###\s+(.+?)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:65895fe39f1febaecf1e3e0e7613bc4e:search

```yaml
regex_id: 65895fe39f1febaecf1e3e0e7613bc4e
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/comment_quality.py:36:19"
```

### Pattern

`^[ \t]{4,20}(\w+)[ \t]{0,10}(?:\([^)]{0,100}\))?[ \t]{0,10}:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:66a873ca45675f12fdf63dc6a385d5e6:search

```yaml
regex_id: 66a873ca45675f12fdf63dc6a385d5e6
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/orchestration/activity_modalities.py:111:14"
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

## usage_mismatch:678a647b3f645cf4bbf55588137d8d22:search

```yaml
regex_id: 678a647b3f645cf4bbf55588137d8d22
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/scripts/bump_version.py:41:13"
```

### Pattern

`^\d+\.\d+\.\d+(?:[-+.][0-9A-Za-z.-]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:678f66f4e9fc621abc06ba2cca4f9aa1:search

```yaml
regex_id: 678f66f4e9fc621abc06ba2cca4f9aa1
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/github_app/slash_commands.py:25:12"
```

### Pattern

`^[ \t]*/bernstein[ \t]+(\w+)(?:[ \t]+([^\r\n]*))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:67a4f9516a8de0c1a2cfd0202c13009e:search

```yaml
regex_id: 67a4f9516a8de0c1a2cfd0202c13009e
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/observability/log_search.py:80:12"
```

### Pattern

`^last\s+(?P<n>\d+(?:\.\d+)?)\s*(?P<unit>s|sec|second|seconds|m|min|minute|minutes|h|hour|hours|d|day|days)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6856f2a600a4e7c24f783312306a537f:search

```yaml
regex_id: 6856f2a600a4e7c24f783312306a537f
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/scripts/check_docs_drift.py:44:10"
```

### Pattern

`^\|\s*`([^`|]+?)`\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*`([a-z-]+)`\s*\|\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6cdeed9bdaae63a60ba771b906864a43:search

```yaml
regex_id: 6cdeed9bdaae63a60ba771b906864a43
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/plugins_core/team_hub_manifest.py:41:33"
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

## usage_mismatch:6f609ee321af90d34c4c4cb24639c7f9:search

```yaml
regex_id: 6f609ee321af90d34c4c4cb24639c7f9
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sensitive_file_detector.py:129:5"
```

### Pattern

`(^|/)\.aws/credentials$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6f9daeec1e873356af10cd92d4316c5d:search

```yaml
regex_id: 6f9daeec1e873356af10cd92d4316c5d
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/git/merge_queue.py:71:21"
```

### Pattern

`^(changed in both|added in both|both added|both removed|removed in both)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:70f737a4b8347866aa304d2c961dc429:search

```yaml
regex_id: 70f737a4b8347866aa304d2c961dc429
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/teams/manifest.py:69:19"
```

### Pattern

`^(?P<name>[A-Za-z0-9][A-Za-z0-9._-]*)(?:@(?P<digest>[0-9a-fA-F]{64}))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:73172b1393fecb2fa6bec57d2eedd7e6:search

```yaml
regex_id: 73172b1393fecb2fa6bec57d2eedd7e6
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/planning/spec_assertions.py:73:15"
```

### Pattern

`^\s*contains\s+(?P<path>\S+?)\s+/(?P<pattern>.+)/\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7566cc28cab0843786b0b8b03cd3fa2f:search

```yaml
regex_id: 7566cc28cab0843786b0b8b03cd3fa2f
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/datasources/engine.py:502:24"
```

### Pattern

`^select\s+(?P<cols>.+?)\s+from\s+(?P<table>[a-z_][a-z0-9_]*)(?:\s+order\s+by\s+(?P<order>[a-z_][a-z0-9_]*)(?:\s+(?P<dir>asc|desc))?)?(?:\s+limit\s+(?P<limit>\d+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:757411bb12f60d96f755916fbcd5a4d1:search

```yaml
regex_id: 757411bb12f60d96f755916fbcd5a4d1
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sensitive_file_detector.py:110:5"
```

### Pattern

`(^|/)\.env(\..+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7594faa93c3499fbc8948c15416627b6:search

```yaml
regex_id: 7594faa93c3499fbc8948c15416627b6
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sensitive_file_detector.py:130:5"
```

### Pattern

`(^|/)\.gcp/.*\.json$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7613330f3c316e1f9164d0a643eb3e6d:search

```yaml
regex_id: 7613330f3c316e1f9164d0a643eb3e6d
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/orchestration/browser_check.py:74:16"
```

### Pattern

`^sha256:[0-9a-f]{64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:765aca5db4b095013e99dc87bc36b8dd:search

```yaml
regex_id: 765aca5db4b095013e99dc87bc36b8dd
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/knowledge/memory_integrity.py:134:8"
```

### Pattern

`^\s*#+\s*(system|human|assistant|user)\s*:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:770b4ebe34530129cc224c7a145c62c7:search

```yaml
regex_id: 770b4ebe34530129cc224c7a145c62c7
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/quality_gates.py:612:20"
```

### Pattern

`test_(\w+)\.py$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:77427dedb92a17d2c05cddd9fa8e15ec:search

```yaml
regex_id: 77427dedb92a17d2c05cddd9fa8e15ec
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sensitive_file_detector.py:112:5"
```

### Pattern

`(^|/)\.env\.production$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:775020b62e1c61daf5c4dfe967aa3c83:search

```yaml
regex_id: 775020b62e1c61daf5c4dfe967aa3c83
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/routes/sandbox.py:23:22"
```

### Pattern

`^[A-Za-z0-9_-]{1,64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7829a203e62b0f2ba6c062b33aca4847:search

```yaml
regex_id: 7829a203e62b0f2ba6c062b33aca4847
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sensitive_file_detector.py:111:5"
```

### Pattern

`(^|/)\.env\.local$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:78a7648ce3113ad023dfb1bdecac5ace:search

```yaml
regex_id: 78a7648ce3113ad023dfb1bdecac5ace
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/eval/scenario_generator.py:84:32"
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

## usage_mismatch:7a22b671dcefddaebe00d6eb28420b52:search

```yaml
regex_id: 7a22b671dcefddaebe00d6eb28420b52
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/cli/display/changelog_display.py:38:13"
```

### Pattern

`^##\s+\[(?P<version>[^\]]+)\]\s*-\s*(?P<date>\S+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7a662ff4458b9f5c2095100592793446:search

```yaml
regex_id: 7a662ff4458b9f5c2095100592793446
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/ci_monitor.py:37:17"
```

### Pattern

`^((?:[\w.]*\w)?(?:Error|Exception|Failure)[^\n]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7ab4b463f1d95022ed8726d73e0a1cc5:search

```yaml
regex_id: 7ab4b463f1d95022ed8726d73e0a1cc5
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/tasks/backlog_parser.py:321:18"
```

### Pattern

`(?:->|→)\s*([\w,\s-]+?)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7b37385878f5ed563e021be4017e9815:search

```yaml
regex_id: 7b37385878f5ed563e021be4017e9815
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/intent_capsule.py:508:13"
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

## usage_mismatch:7c3970e18a45db83d0771b8af879ed13:search

```yaml
regex_id: 7c3970e18a45db83d0771b8af879ed13
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sensitive_file_detector.py:106:5"
```

### Pattern

`.*\.crt$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7c3dd6aca0c9b53610d24525206109b9:match

```yaml
regex_id: 7c3dd6aca0c9b53610d24525206109b9
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/compliance.py:490:8"
```

### Pattern

`^(\d{4})-(\d{2})$`

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

## usage_mismatch:7d0504b86eac213a270534714367e533:search

```yaml
regex_id: 7d0504b86eac213a270534714367e533
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/adapters/security_floor.py:121:19"
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

## usage_mismatch:7d68d46a173d937915b2f014cb230d9e:search

```yaml
regex_id: 7d68d46a173d937915b2f014cb230d9e
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/payments/_canonical.py:57:15"
```

### Pattern

`^[A-Z]{3}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7e9ea32f03cbf5f2fbc91a1d4853d4bd:search

```yaml
regex_id: 7e9ea32f03cbf5f2fbc91a1d4853d4bd
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/scripts/auto_heal_apply_typos.py:22:34"
```

### Pattern

`^([A-Za-z_][A-Za-z0-9_]*)\s*=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8420d50610f21282daf6327d5df71332:search

```yaml
regex_id: 8420d50610f21282daf6327d5df71332
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/workflows/workflow_spec.py:57:14"
```

### Pattern

`^[a-z0-9][a-z0-9_\-]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:85a69d89d0122ca5c65fd14329227f0a:search

```yaml
regex_id: 85a69d89d0122ca5c65fd14329227f0a
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/adapters/openai_agents_runner.py:734:35"
```

### Pattern

`^[A-Z][A-Z0-9_]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:85d5c568c988239f6fe365ac85da5b28:search

```yaml
regex_id: 85d5c568c988239f6fe365ac85da5b28
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/identity/spiffe/spiffe_id.py:61:19"
```

### Pattern

`^[a-zA-Z0-9._-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:85f4ed65500f758a9caa350b9714b5f4:match

```yaml
regex_id: 85f4ed65500f758a9caa350b9714b5f4
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/compliance.py:481:8"
```

### Pattern

`^Q([1-4])-(\d{4})$`

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

## usage_mismatch:8b1da97af2284843b5bccf65b55cae2c:search

```yaml
regex_id: 8b1da97af2284843b5bccf65b55cae2c
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/tasks/backlog_parser.py:323:12"
```

### Pattern

`^US\d+[\w-]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8bf52532084d95dfe4800b04009d072a:search

```yaml
regex_id: 8bf52532084d95dfe4800b04009d072a
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/config/seed_parser.py:71:14"
```

### Pattern

`^\$\{([A-Z0-9_]+)\}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8cab82afdc61cb15b6007c06d1710ea3:search

```yaml
regex_id: 8cab82afdc61cb15b6007c06d1710ea3
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/routes/approvals.py:77:14"
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

## usage_mismatch:8fcfcc1a10626afd8f8239b4ef8f96a5:search

```yaml
regex_id: 8fcfcc1a10626afd8f8239b4ef8f96a5
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/replay/journal.py:86:13"
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

## usage_mismatch:90bcbb2107ea4770ebae0942ac058dec:search

```yaml
regex_id: 90bcbb2107ea4770ebae0942ac058dec
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/memory/session_memory.py:88:9"
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

## usage_mismatch:916bdee46f485838caf304e530866dea:search

```yaml
regex_id: 916bdee46f485838caf304e530866dea
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/cost/scheduling/receipt.py:50:20"
```

### Pattern

`^sha256:[0-9a-f]{64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9476ff81bcc5d86726f8644729e66dc0:search

```yaml
regex_id: 9476ff81bcc5d86726f8644729e66dc0
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/cli/run_names.py:207:10"
```

### Pattern

`^[a-z]+-[a-z]+-\d{2}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:947fe9afcb856b6880f729e6a6962f8a:search

```yaml
regex_id: 947fe9afcb856b6880f729e6a6962f8a
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/scripts/format_release_notes.py:45:16"
```

### Pattern

` \(#\d+\)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:973452630662d4f883d96dce00e1d099:search

```yaml
regex_id: 973452630662d4f883d96dce00e1d099
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/run_service/paths.py:19:13"
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

## usage_mismatch:9766d215c0d1435ab700d107b2eb83c5:search

```yaml
regex_id: 9766d215c0d1435ab700d107b2eb83c5
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/quality_gates.py:611:21"
```

### Pattern

`^\+\+\+ b/(tests?/\S{0,200}test_\w+\.py|\w+/tests?/test_\w+\.py)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9b826fb2efb6467fb9d63a4347930e01:search

```yaml
regex_id: 9b826fb2efb6467fb9d63a4347930e01
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/plugins_core/plugin_manifest.py:122:16"
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

## usage_mismatch:9c0df375b4c5a59ca12277fc9c8c85fd:search

```yaml
regex_id: 9c0df375b4c5a59ca12277fc9c8c85fd
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/scripts/auto_heal_typos.py:41:36"
```

### Pattern

`^error: `([^`]+)` should be `([^`]+)``

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9eb077ac9738495f59b5dd598e4ff526:search

```yaml
regex_id: 9eb077ac9738495f59b5dd598e4ff526
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/memory/jsonl_log.py:49:10"
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

## usage_mismatch:a006fb721842783f3551c766996ba029:search

```yaml
regex_id: a006fb721842783f3551c766996ba029
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/orchestration/run_changelog.py:288:19"
```

### Pattern

`^(?P<type>feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)(?:\((?P<scope>[^)]+)\))?(?P<breaking>!)?:\s*(?P<desc>.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a0f1e74f440c79359aa6fba7be15d58b:search

```yaml
regex_id: a0f1e74f440c79359aa6fba7be15d58b
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sensitive_file_detector.py:103:5"
```

### Pattern

`.*\.pfx$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a191f499bc0b5fe6385e0d7233b5b08f:search

```yaml
regex_id: a191f499bc0b5fe6385e0d7233b5b08f
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/flaky_detector.py:17:20"
```

### Pattern

`^(?P<test_id>[^\s:]+(?:::[^\s:]+)+)\s+(?P<status>PASSED|FAILED|ERROR|SKIPPED|XFAIL|XPASS)\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a2ba9c02ecaae50f5e6a39a1541f2e8e:search

```yaml
regex_id: a2ba9c02ecaae50f5e6a39a1541f2e8e
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/eval/promotion.py:55:19"
```

### Pattern

`^sha256:[0-9a-f]{64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a401e574a458f8c0ba889366eaea0dc9:search

```yaml
regex_id: a401e574a458f8c0ba889366eaea0dc9
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sensitive_file_detector.py:123:5"
```

### Pattern

`(^|/)id_(rsa|dsa|ecdsa|ed25519)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a4ce55278f0597925553a0e6efcc4f7f:search

```yaml
regex_id: a4ce55278f0597925553a0e6efcc4f7f
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/scripts/bump_version.py:40:14"
```

### Pattern

`^version = "[^"]*"$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a5b30b21c3c6cb8f85d2cd1ee25697e5:search

```yaml
regex_id: a5b30b21c3c6cb8f85d2cd1ee25697e5
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/adapters/canary.py:124:19"
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

## usage_mismatch:a5ffe2f8fbde1aa69c6e48ce3eeea4a7:search

```yaml
regex_id: a5ffe2f8fbde1aa69c6e48ce3eeea4a7
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/integrations/tickets/__init__.py:53:17"
```

### Pattern

`^linear://(?P<key>[A-Z0-9]+-\d+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a6a4879cd5751784f968ebec0d79faf1:search

```yaml
regex_id: a6a4879cd5751784f968ebec0d79faf1
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/orchestration/consensus_relay.py:108:39"
```

### Pattern

`^[A-Za-z0-9._-]{1,128}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a83ff2d37b662b6b9732d2590c6fa04e:search

```yaml
regex_id: a83ff2d37b662b6b9732d2590c6fa04e
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/protocols/mcp_catalog/manifest.py:37:31"
```

### Pattern

`^[a-z0-9][a-z0-9._-]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a864c646d80f82b0eaee89c724d5133e:search

```yaml
regex_id: a864c646d80f82b0eaee89c724d5133e
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/skills/catalog/manifest.py:67:31"
```

### Pattern

`^[a-z0-9][a-z0-9._-]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a8a3037c7b9b75173637a8d25036c3cd:search

```yaml
regex_id: a8a3037c7b9b75173637a8d25036c3cd
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/tasks/backlog_parser.py:319:16"
```

### Pattern

`^\[([^\[\]]+)\]\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a8d9f54d3bf19cbe17bea723d2df7ade:search

```yaml
regex_id: a8d9f54d3bf19cbe17bea723d2df7ade
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/tokens/context_fallback.py:144:19"
```

### Pattern

`^[\s]*(?:[./]|[|`\\]|[a-zA-Z]:[\\/]).*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a9798483036f644195850e07e52137f1:search

```yaml
regex_id: a9798483036f644195850e07e52137f1
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/eval/trajectory_receipt.py:91:19"
```

### Pattern

`^sha256:[0-9a-f]{64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:aac5ce3eb5400df4983f4ff77b31e7dc:search

```yaml
regex_id: aac5ce3eb5400df4983f4ff77b31e7dc
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/config/seed_parser.py:364:21"
```

### Pattern

`^[a-zA-Z][a-zA-Z0-9+\-.]*://[^/\s*]+:\*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:aadfcaa7ceeb1c477ab9c3e769cb0b96:search

```yaml
regex_id: aadfcaa7ceeb1c477ab9c3e769cb0b96
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/tui/log_viewer.py:147:11"
```

### Pattern

`^(\s*[-*+]|\s*\d+\.) `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:aaef3240035568bde303ded4fcf6d293:search

```yaml
regex_id: aaef3240035568bde303ded4fcf6d293
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/comment_quality.py:62:18"
```

### Pattern

`^\s*(\w+)\s*:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:aebd4053f788875c11f36a72781c117c:search

```yaml
regex_id: aebd4053f788875c11f36a72781c117c
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/orchestration/worker.py:38:17"
```

### Pattern

`^[a-zA-Z0-9_.-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b0f32528608e969fdba6485202548930:search

```yaml
regex_id: b0f32528608e969fdba6485202548930
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/skills/lint.py:115:35"
```

### Pattern

`^(?:[-*+]\s|\d+[.)]\s|#{1,6}\s|>|\|)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b2faed3ca5223feaca699faafc69f892:search

```yaml
regex_id: b2faed3ca5223feaca699faafc69f892
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/adapters/ci/github_actions.py:25:16"
```

### Pattern

`^\d{4}-\d{2}-\d{2}T[\d:.]+Z\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b36e8f2bbbb26bb5d45cf1ca5e48b034:search

```yaml
regex_id: b36e8f2bbbb26bb5d45cf1ca5e48b034
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/policy_engine.py:137:19"
```

### Pattern

`^(?P<field>[a-z_]+)[ \t]{0,10}(?P<operator>==|!=|>=|<=|>|<)[ \t]{0,10}(?P<value>.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b409d432911ceffbbc356180a8746e66:search

```yaml
regex_id: b409d432911ceffbbc356180a8746e66
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/scripts/auto_heal_typos.py:48:36"
```

### Pattern

`^[a-z][a-z0-9_]{2,39}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b5b86cbfea70d3404c29313490109660:search

```yaml
regex_id: b5b86cbfea70d3404c29313490109660
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/adapters/ci/gitlab_ci.py:30:19"
```

### Pattern

`^(?:ERROR|FATAL|FAILED|WARNING|Traceback|#<\w+Error)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b6a1726ab83602f19f985703086ce629:search

```yaml
regex_id: b6a1726ab83602f19f985703086ce629
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/tasks/backlog_parser.py:322:11"
```

### Pattern

`^T\d+[\w-]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b6da79e7bf0a498426207822bd1fcd04:search

```yaml
regex_id: b6da79e7bf0a498426207822bd1fcd04
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sensitive_file_detector.py:127:5"
```

### Pattern

`(^|/)token\.json$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b7cfa0cffa1af662ca1995d050a6e832:search

```yaml
regex_id: b7cfa0cffa1af662ca1995d050a6e832
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/integrations/tickets/github_issues.py:29:12"
```

### Pattern

`^https?://github\.com/(?P<owner>[^/]+)/(?P<repo>[^/]+)/issues/(?P<num>\d+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b8236fc6ea266275ea0c0043893c6524:search

```yaml
regex_id: b8236fc6ea266275ea0c0043893c6524
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/identity/spiffe/spiffe_id.py:57:19"
```

### Pattern

`^[a-z0-9._-]{1,255}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b9547cffa24d1161911dafedd03b5438:search

```yaml
regex_id: b9547cffa24d1161911dafedd03b5438
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/workflows/recipe_spec.py:70:22"
```

### Pattern

`^[a-z][a-z0-9_]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bcfe4604dcdf13227de51ff6b629adbd:search

```yaml
regex_id: bcfe4604dcdf13227de51ff6b629adbd
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/observability/traces.py:185:11"
```

### Pattern

`^\[(?P<tool>[A-Za-z]+)\][ \t]{0,10}(?P<args>[^\n]{0,500})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bd7d0ffc5f25c5fc20c194ea3982c9e3:search

```yaml
regex_id: bd7d0ffc5f25c5fc20c194ea3982c9e3
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/routes/missions.py:61:38"
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

## usage_mismatch:be5820a3e59f3dd25780d245e5b25362:search

```yaml
regex_id: be5820a3e59f3dd25780d245e5b25362
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/scripts/text_to_sarif.py:46:13"
```

### Pattern

`^(?P<path>[^:]+):(?P<line>\d+):(?P<col>\d+)\s*(?:\[(?P<code>FURB\d+)\])?\s*:?\s*(?P<msg>.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bf241b730a7e0c778bd943ab2ca1c223:search

```yaml
regex_id: bf241b730a7e0c778bd943ab2ca1c223
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sensitive_file_detector.py:116:8"
```

### Pattern

`(^|/)service[-_]?account.*\.json$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bf4f4d5dc211a32f4b013b506b0d441b:search

```yaml
regex_id: bf4f4d5dc211a32f4b013b506b0d441b
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/cli/release_notes.py:22:19"
```

### Pattern

`^v(\d+)\.(\d+)\.(\d+)\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bfaf35e2315c61092b64ae50f2976287:search

```yaml
regex_id: bfaf35e2315c61092b64ae50f2976287
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/dead_code_detector.py:27:18"
```

### Pattern

`^\+\s*class\s+(\w+)\s*[:(]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bfe10d824dab458ee8c04010701dd8f2:search

```yaml
regex_id: bfe10d824dab458ee8c04010701dd8f2
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/persistence/work_ledger.py:133:11"
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

## usage_mismatch:c0d55375b2a1eacd115d49e7ad5d14ba:search

```yaml
regex_id: c0d55375b2a1eacd115d49e7ad5d14ba
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/integrations/tickets/__init__.py:54:16"
```

### Pattern

`^https?://github\.com/(?P<owner>[^/]+)/(?P<repo>[^/]+)/issues/(?P<num>\d+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c0d9020cc0478e8379255f97df6cc3ca:search

```yaml
regex_id: c0d9020cc0478e8379255f97df6cc3ca
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/tasks/figures.py:252:15"
```

### Pattern

`(USD|EUR|GBP|JPY|CHF|CAD|AUD)\s?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c450cfde81fc80391e3370f61098ddae:search

```yaml
regex_id: c450cfde81fc80391e3370f61098ddae
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/skills/manifest.py:41:34"
```

### Pattern

`^---[ \t]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c7262e7adc7dbbe119325415102b9fc4:search

```yaml
regex_id: c7262e7adc7dbbe119325415102b9fc4
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/plugins/security_review.py:206:24"
```

### Pattern

`^\+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c7424408df26bca6d7f0701e7c72e1e8:search

```yaml
regex_id: c7424408df26bca6d7f0701e7c72e1e8
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/planning/spec_quality.py:183:25"
```

### Pattern

`^\s{0,3}#{1,6}\s*acceptance\s+criteria\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c746bbd2ad6b6eb485df5b6977ca8316:search

```yaml
regex_id: c746bbd2ad6b6eb485df5b6977ca8316
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/orchestration/watchdog.py:75:4"
```

### Pattern

`continue\?\s*\[y/n\]\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c78b30da8c89f12fd4ba33dedd0847be:search

```yaml
regex_id: c78b30da8c89f12fd4ba33dedd0847be
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/scripts/text_to_sarif.py:43:14"
```

### Pattern

`^(?P<path>[^:]+):(?P<line>\d+):\s*(?P<msg>.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c7a811e900df4229b58ba3eaeee7f8cd:search

```yaml
regex_id: c7a811e900df4229b58ba3eaeee7f8cd
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/persistence/work_ledger.py:137:14"
```

### Pattern

`^[A-Za-z0-9_.-]{0,64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cc2fb8a418f0a4b8f0c3096dbddd43c3:search

```yaml
regex_id: cc2fb8a418f0a4b8f0c3096dbddd43c3
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/comment_quality.py:230:17"
```

### Pattern

`^(get|set|init|initialise|initialize|create|make|build|return|returns?|return\s+the|gets?\s+the|sets?\s+the)\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cd539be5e0a6264197b399b97eff8c09:search

```yaml
regex_id: cd539be5e0a6264197b399b97eff8c09
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/admission/models.py:36:11"
```

### Pattern

`^[a-z0-9][a-z0-9_.-]{0,63}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ced9e67a11908a7716d8c90fe54a22b5:search

```yaml
regex_id: ced9e67a11908a7716d8c90fe54a22b5
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/git/git_basic.py:14:26"
```

### Pattern

`^(feat|fix|chore|docs|test|refactor)(\([a-z0-9._/-]+\))?: .+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d0a8bc4f9cacb788ab893628bd294613:search

```yaml
regex_id: d0a8bc4f9cacb788ab893628bd294613
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/eval/gate_receipt.py:65:19"
```

### Pattern

`^sha256:[0-9a-f]{64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d0cc8a8ca0ade9a16f0484d2f738d95e:search

```yaml
regex_id: d0cc8a8ca0ade9a16f0484d2f738d95e
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/tokens/compaction_validate.py:107:41"
```

### Pattern

`^( {0,3})(`{3,}|~{3,})[ \t]*([^\n`]*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d25cc849d98019c40d03385034d09b93:search

```yaml
regex_id: d25cc849d98019c40d03385034d09b93
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/changelog_generator.py:43:16"
```

### Pattern

`^\+\s*def\s+([a-zA-Z]\w*)\s*\((.+)\)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d27d5a5f0bbcc61f30122a590cfbe263:search

```yaml
regex_id: d27d5a5f0bbcc61f30122a590cfbe263
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/planning/spec_quality.py:185:25"
```

### Pattern

`^\s{0,3}#{1,6}\s*tested[\s-]+via\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d33ded412ad7e7e18875cab0f9a4dd90:search

```yaml
regex_id: d33ded412ad7e7e18875cab0f9a4dd90
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sensitive_file_detector.py:133:5"
```

### Pattern

`(^|/)\.kube/config$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d43d1ca39d1536ac5ae5212c568b22f7:search

```yaml
regex_id: d43d1ca39d1536ac5ae5212c568b22f7
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/tui/log_viewer.py:149:9"
```

### Pattern

`^(-{3,}|\*{3,}|_{3,})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d464749e08f4440ae72975106e038c4f:search

```yaml
regex_id: d464749e08f4440ae72975106e038c4f
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/evidence/run_artifacts.py:86:14"
```

### Pattern

`^[A-Za-z0-9_.:-]{1,256}\Z`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d55abbd286d4318354c1124cb733be33:search

```yaml
regex_id: d55abbd286d4318354c1124cb733be33
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/orchestration/missions.py:128:9"
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

## usage_mismatch:d6bdd2aa173b87a0b656e1d9f72b9079:search

```yaml
regex_id: d6bdd2aa173b87a0b656e1d9f72b9079
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/plugins/security_review.py:204:20"
```

### Pattern

`^\+\+\+ b/(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d6f39bdef9d2890af7ae4810dcaf6830:search

```yaml
regex_id: d6f39bdef9d2890af7ae4810dcaf6830
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/fleet/bulk.py:30:13"
```

### Pattern

`^\s*(?P<field>cost|agents|approvals)\s*(?P<op><=|>=|==|!=|<|>)\s*(?P<value>-?\d+(?:\.\d+)?)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d76cefe0d5c991c16b0a313a42b48b1b:search

```yaml
regex_id: d76cefe0d5c991c16b0a313a42b48b1b
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/scripts/text_to_sarif.py:58:14"
```

### Pattern

`^(?P<path>[^:]+):(?P<line>\d+)(?::(?P<col>\d+))?:\s*(?P<msg>.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d958ae2ee79a536af59e3f03a22e423e:search

```yaml
regex_id: d958ae2ee79a536af59e3f03a22e423e
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/changelog_generator.py:38:20"
```

### Pattern

`^-\s*class\s+([a-zA-Z]\w*)\s*[\(:]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dac2ba77e40b6b6c34746024c47f2454:search

```yaml
regex_id: dac2ba77e40b6b6c34746024c47f2454
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/tokens/template_compress_validate.py:124:38"
```

### Pattern

`^ {0,3}#{1,6} \S`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dce89fa586aa0f3c07e97992e0a42f44:search

```yaml
regex_id: dce89fa586aa0f3c07e97992e0a42f44
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/auth_middleware.py:116:19"
```

### Pattern

`^(?:/api/v\d+)?/tasks/(?P<task_id>[^/]+)(?:/.*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dd946f359e0b76bed4da10b2db1c264b:search

```yaml
regex_id: dd946f359e0b76bed4da10b2db1c264b
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/path_containment.py:49:18"
```

### Pattern

`^[A-Za-z0-9_.-]+\Z`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:de448a625ad43b0c2b9664b44d5fa4fb:search

```yaml
regex_id: de448a625ad43b0c2b9664b44d5fa4fb
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sensitive_file_detector.py:120:5"
```

### Pattern

`(^|/)\.htpasswd$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e194e1d7a450b5d4ae79a38fc1607af7:search

```yaml
regex_id: e194e1d7a450b5d4ae79a38fc1607af7
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/comment_quality.py:31:21"
```

### Pattern

`^\s*(Args|Returns?|Raises?|Yields?|Attributes?|Examples?|Note|Notes|Todo)\s*:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e1fa5496085cd7ed7fb9f44c99a115dc:search

```yaml
regex_id: e1fa5496085cd7ed7fb9f44c99a115dc
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/persistence/ledger_git.py:90:13"
```

### Pattern

`^[A-Za-z0-9_][A-Za-z0-9_.-]{0,63}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e21d3f0c8e5bacd3eff13b718211f0eb:search

```yaml
regex_id: e21d3f0c8e5bacd3eff13b718211f0eb
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/scripts/format_release_notes.py:53:19"
```

### Pattern

`^(?:audit|rt)-\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e33f5c92c4363a158e0c6ed30c153c46:match

```yaml
regex_id: e33f5c92c4363a158e0c6ed30c153c46
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/orchestration/run_changelog.py:220:15"
```

### Pattern

`^\d{4}-\d{2}-\d{2}\.jsonl$`

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

## usage_mismatch:e353733488c903c7fa7766783821e5ed:search

```yaml
regex_id: e353733488c903c7fa7766783821e5ed
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/policy_engine.py:136:17"
```

### Pattern

`^(?P<field>[a-z_]+)[ \t]*(?P<operator>!~|=~)[ \t]*/(?P<pattern>.+)/$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e48ad2dc51364a14c83b2295d7cdab59:search

```yaml
regex_id: e48ad2dc51364a14c83b2295d7cdab59
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/path_containment.py:62:19"
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

## usage_mismatch:e6718789adb07338539a4e37f0018d44:search

```yaml
regex_id: e6718789adb07338539a4e37f0018d44
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/janitor.py:1826:4"
```

### Pattern

`^\s*git\s+log\s+-1\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e72b391c1f54a90586e3d0965df59b9e:search

```yaml
regex_id: e72b391c1f54a90586e3d0965df59b9e
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/routes/session_peek.py:66:41"
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

## usage_mismatch:e91db889a107af3979d677a94015d1a9:search

```yaml
regex_id: e91db889a107af3979d677a94015d1a9
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/promptware_detector.py:218:14"
```

### Pattern

`(?im)^\s*(?:please\s+)?(?:do|run|execute|send|fetch|download|post|upload|delete|stop)\b[^\n]{0,80}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e91eb7eb048f7d4e1f9abcf5642e19f7:match

```yaml
regex_id: e91eb7eb048f7d4e1f9abcf5642e19f7
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/protocols/mcp/mcp_version_compat.py:74:21"
```

### Pattern

`^(\d{4})-(\d{2})-(\d{2})$`

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

## usage_mismatch:e9293b75d06554f8ca57b4caf9fe25cf:search

```yaml
regex_id: e9293b75d06554f8ca57b4caf9fe25cf
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/routes/missions.py:58:41"
```

### Pattern

`^[A-Za-z0-9_.\-]{1,64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:eace2f7b7cdf0afa75225edf1eb2767e:search

```yaml
regex_id: eace2f7b7cdf0afa75225edf1eb2767e
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/planning/spec_assertions.py:68:13"
```

### Pattern

`^\s*(?:file\s+)?exists\s+(?P<path>\S.+?)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:eca5488366ea442c5306d09ec0447337:search

```yaml
regex_id: eca5488366ea442c5306d09ec0447337
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/plugins/security_review.py:205:20"
```

### Pattern

`^@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ed13701a4cb739daa5db11c36ae10a73:search

```yaml
regex_id: ed13701a4cb739daa5db11c36ae10a73
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/planning/sla_store.py:74:9"
```

### Pattern

`^[A-Za-z0-9_.:@/-]{1,256}\Z`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ed4c4e3e962e951eac7e985e09fed0c3:search

```yaml
regex_id: ed4c4e3e962e951eac7e985e09fed0c3
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/persistence/migrations/runner.py:49:13"
```

### Pattern

`^v(\d+)_[a-z0-9_]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ed909e800e38c29e07f0885df32f216e:search

```yaml
regex_id: ed909e800e38c29e07f0885df32f216e
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/changelog_generator.py:44:25"
```

### Pattern

`^-\s*def\s+([a-zA-Z]\w*)\s*\((.+)\)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ee7784796c00813f4d45c6a900ec045e:search

```yaml
regex_id: ee7784796c00813f4d45c6a900ec045e
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/scripts/check_context_staleness.py:100:14"
```

### Pattern

`^(\d+|-)\t(\d+|-)\t(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ef04f4503155a5d6546e3a2b8f9e15ea:search

```yaml
regex_id: ef04f4503155a5d6546e3a2b8f9e15ea
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/dead_code_detector.py:24:15"
```

### Pattern

`^-\s*(?:async\s+)?def\s+(\w+)\s*\(`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:efdb82b6325561f035cc027ef8127b08:search

```yaml
regex_id: efdb82b6325561f035cc027ef8127b08
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/observability/log_search.py:37:12"
```

### Pattern

`^(?P<y>\d{4})-(?P<mo>\d{2})-(?P<d>\d{2})[T ](?P<h>\d{2}):(?P<mi>\d{2}):(?P<s>\d{2})`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f45cf21dd73d4cf992b438189b24e0f6:search

```yaml
regex_id: f45cf21dd73d4cf992b438189b24e0f6
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sensitive_file_detector.py:100:5"
```

### Pattern

`.*\.pem$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f558662f3705f7a3b368fefd781be995:search

```yaml
regex_id: f558662f3705f7a3b368fefd781be995
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/adapters/ci/github_actions.py:34:12"
```

### Pattern

`##\[error\](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f5bd0d4a50fef2ef9a4c185c0f5e17ad:search

```yaml
regex_id: f5bd0d4a50fef2ef9a4c185c0f5e17ad
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/replay/review_board.py:415:15"
```

### Pattern

`^diff --git a/(?P<a>.+?) b/(?P<b>.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f6462cb244dd7ba94decef055d13204b:search

```yaml
regex_id: f6462cb244dd7ba94decef055d13204b
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/fleet/prometheus_proxy.py:31:13"
```

### Pattern

`^([a-zA-Z_:][a-zA-Z0-9_:]*)(\{[^}]*\})?\s+(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f7563af148f37f8da323089a7d4cfce6:search

```yaml
regex_id: f7563af148f37f8da323089a7d4cfce6
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/sandbox/ssh_backend.py:61:24"
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

## usage_mismatch:f82230f3c71d0cea53c1143c3da8fd14:search

```yaml
regex_id: f82230f3c71d0cea53c1143c3da8fd14
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/sdd/validator.py:142:14"
```

### Pattern

`^v\d+(?:\.\d+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f8c02aa123c323a4b218e34fd69dc3eb:search

```yaml
regex_id: f8c02aa123c323a4b218e34fd69dc3eb
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/integrations/tickets/__init__.py:49:14"
```

### Pattern

`^https?://linear\.app/(?P<workspace>[^/]+)/issue/(?P<key>[A-Z0-9]+-\d+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f9e2331d19cec95cbc199087f070c67e:search

```yaml
regex_id: f9e2331d19cec95cbc199087f070c67e
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sensitive_file_detector.py:114:5"
```

### Pattern

`(^|/)credentials\.json$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fb15cf1f5f1db2d2f27752225e3bfeeb:search

```yaml
regex_id: fb15cf1f5f1db2d2f27752225e3bfeeb
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/collaboration_miner.py:42:12"
```

### Pattern

`^\[RETRY\s+\d+\]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fb231b85a09fe4c0419952aa7df3155a:search

```yaml
regex_id: fb231b85a09fe4c0419952aa7df3155a
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/routes/task_detail.py:345:11"
```

### Pattern

`^@@ -(?P<os>\d+)(?:,(?P<ol>\d+))? \+(?P<ns>\d+)(?:,(?P<nl>\d+))? @@`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fb5ce3a1946070ec5f1b69c1f97a3b87:search

```yaml
regex_id: fb5ce3a1946070ec5f1b69c1f97a3b87
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/quality/readme_reminder.py:43:21"
```

### Pattern

`^\+(?!\+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fc286249a614e038987bc295346ae961:search

```yaml
regex_id: fc286249a614e038987bc295346ae961
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/core/security/sensitive_file_detector.py:101:5"
```

### Pattern

`.*\.key$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fdcd7583374108d8412f78726858bee3:search

```yaml
regex_id: fdcd7583374108d8412f78726858bee3
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/sdd/spec_pipeline/draft.py:51:13"
```

### Pattern

`^\s*(?:[-*+]\s+)?(?:\[[ xX]\]\s+)?(?:\d+[.)]\s+)?`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ff5564e77b443bce426c3a9beb058d8a:search

```yaml
regex_id: ff5564e77b443bce426c3a9beb058d8a
schema_version: "1"
kind: usage_mismatch
corpus: bernstein
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/bernstein/rules/src/bernstein/adapters/ci/github_actions.py:99:8"
```

### Pattern

`##\[group\]Run\s+(.+)$`

### Context

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
corpus: bernstein
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
corpus: bernstein
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
corpus: bernstein
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
corpus: bernstein
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

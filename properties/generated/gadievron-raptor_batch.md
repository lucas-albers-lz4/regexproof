---
schema_version: "1"
corpus: gadievron-raptor
findings: 428
---

# gadievron-raptor batch findings

## usage_mismatch:02b95d93827508d74b449a580f61d418:search

```yaml
regex_id: 02b95d93827508d74b449a580f61d418
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:619:5"
```

### Pattern

`^(register)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:037fb4e26f37609ffa69838a6e4740ae:search

```yaml
regex_id: 037fb4e26f37609ffa69838a6e4740ae
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/source_intel/analyze.py:1127:12"
```

### Pattern

`^-?\d+[uUlL]*$|^0[xX][0-9a-fA-F]+[uUlL]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:04029edfba622953a8b77fb4cf659a3b:search

```yaml
regex_id: 04029edfba622953a8b77fb4cf659a3b
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:619:44"
```

### Pattern

`^(unregister)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:04711c43962a3170c9059c4d0b30e653:search

```yaml
regex_id: 04711c43962a3170c9059c4d0b30e653
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/inline_installs/__init__.py:544:14"
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

## usage_mismatch:05236ebf5c00e8b33e0092554c2c5f5b:search

```yaml
regex_id: 05236ebf5c00e8b33e0092554c2c5f5b
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/trajectories/types.py:30:16"
```

### Pattern

`^[A-Za-z0-9_\-.]{1,128}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0525b22403036ceef6c3e7c564d3ed40:search

```yaml
regex_id: 0525b22403036ceef6c3e7c564d3ed40
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/typestate.py:115:34"
```

### Pattern

`^(\w+?)_unref$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0691877a55bf14b6779e033de93cc8a0:search

```yaml
regex_id: 0691877a55bf14b6779e033de93cc8a0
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/source_intel/analyze.py:1129:12"
```

### Pattern

`^[A-Za-z_][A-Za-z_0-9]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0850d0f27d53847c7524acda2f6c1d48:search

```yaml
regex_id: 0850d0f27d53847c7524acda2f6c1d48
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/llm/providers.py:1081:21"
```

### Pattern

`^o\d`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:086c1121caadd3ee7a227d5e70793ce4:search

```yaml
regex_id: 086c1121caadd3ee7a227d5e70793ce4
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/sibling_analysis.py:406:5"
```

### Pattern

`^(?:encode|encrypt|serialize|marshal|pack|compress)_(\w+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:087e9679c0c498955bf9df2580769102:search

```yaml
regex_id: 087e9679c0c498955bf9df2580769102
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/translation_view.py:212:18"
```

### Pattern

`^[ \t]*#[ \t]*define[ \t]+(\w+)[ \t]*\(([^)]*)\)(.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:089d8bfceb5c68d77419afe5bd846ba7:search

```yaml
regex_id: 089d8bfceb5c68d77419afe5bd846ba7
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:1482:15"
```

### Pattern

`\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:090fd9f864c51e77c02fca3747be1c2c:search

```yaml
regex_id: 090fd9f864c51e77c02fca3747be1c2c
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:614:5"
```

### Pattern

`^(get)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:092f5521ac5bf171e4968243463d2e3d:search

```yaml
regex_id: 092f5521ac5bf171e4968243463d2e3d
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/typestate.py:114:5"
```

### Pattern

`^(\w+?)_begin$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:095bcc4b57a8cbcadfe5ecdb0493500c:search

```yaml
regex_id: 095bcc4b57a8cbcadfe5ecdb0493500c
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/translation_view.py:65:19"
```

### Pattern

`^(!\s*)?defined\s+(\w+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0baecf02a71e6246f962bba49cdd3030:search

```yaml
regex_id: 0baecf02a71e6246f962bba49cdd3030
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/spec_inference.py:50:5"
```

### Pattern

`^encode_|^serialize_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0c8fc5c75741dc0e277b5e0a4d7d29b0:search

```yaml
regex_id: 0c8fc5c75741dc0e277b5e0a4d7d29b0
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:633:11"
```

### Pattern

`return\s+\d+\s*;?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0c9b30b69f4ec4d0d6e3acd13ecd9a89:search

```yaml
regex_id: 0c9b30b69f4ec4d0d6e3acd13ecd9a89
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/inline_installs/_managers.py:297:17"
```

### Pattern

`^(@[A-Za-z0-9][A-Za-z0-9._\-]*/[A-Za-z0-9][A-Za-z0-9._\-]*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0ce90167647b6d518a573daeb4b9ed91:search

```yaml
regex_id: 0ce90167647b6d518a573daeb4b9ed91
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/smt_solver/path_feasibility.py:259:10"
```

### Pattern

`^0x[0-9a-f]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0d8a1e5b2acf9ae008f72533e7760b60:search

```yaml
regex_id: 0d8a1e5b2acf9ae008f72533e7760b60
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/typestate.py:109:5"
```

### Pattern

`^(\w+?)_new$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0dd99d1b6693448cf7baeeedf2418478:search

```yaml
regex_id: 0dd99d1b6693448cf7baeeedf2418478
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:623:42"
```

### Pattern

`^(disable)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0e1663b47bbf52cda3ce6aa16aa347b0:search

```yaml
regex_id: 0e1663b47bbf52cda3ce6aa16aa347b0
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/oci/blob.py:99:21"
```

### Pattern

`^(?:\.?/)+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0e703b879ab55b914566b98e6b709b3e:search

```yaml
regex_id: 0e703b879ab55b914566b98e6b709b3e
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/reachability/gomod.py:36:17"
```

### Pattern

`^\s*(?:[A-Za-z_][A-Za-z0-9_]*\s+)?"([^"]+)"`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0f8147887162e0a87ef687e198170b31:search

```yaml
regex_id: 0f8147887162e0a87ef687e198170b31
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/callsite_consistency.py:269:18"
```

### Pattern

`^\s*(?:return|yield)\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0feb95e0ddcb9dabd14cef7070a34feb:search

```yaml
regex_id: 0feb95e0ddcb9dabd14cef7070a34feb
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/cve_diff/cve_diff/diffing/extract_via_gitlab_api.py:80:18"
```

### Pattern

`^(https?://([\w.-]+))/([^?#]+?)/?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:105d8f3cfbc462430da2c64256a9dd76:search

```yaml
regex_id: 105d8f3cfbc462430da2c64256a9dd76
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:612:40"
```

### Pattern

`^(unlock)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:11223425f075f3f682e75d19bd8cc79d:search

```yaml
regex_id: 11223425f075f3f682e75d19bd8cc79d
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/exploit_feasibility/analyzer.py:3921:28"
```

### Pattern

`^([0-9a-f]+)\s+[0-9a-f]+\s+\S+\s+[0-9a-f]+\s+(\w+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1157516aee21981bc6494d6cc1e9cb92:search

```yaml
regex_id: 1157516aee21981bc6494d6cc1e9cb92
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/binary_oracle_edges.py:464:18"
```

### Pattern

`^\s*0x[0-9a-fA-F]+\s*:\s*(\S+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:11a3471796ab6761e8157b023752d016:search

```yaml
regex_id: 11a3471796ab6761e8157b023752d016
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/_util.py:17:27"
```

### Pattern

`^[A-Za-z_][A-Za-z0-9_]*(\.[A-Za-z_][A-Za-z0-9_]*)*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:11ba7230128cb4d5492dafd061038cae:search

```yaml
regex_id: 11ba7230128cb4d5492dafd061038cae
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/condition_smt.py:1228:21"
```

### Pattern

`^\s*return\s+(0|nil|None|True|true|EXIT_SUCCESS)\s*;?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:12dbe21710b8701485b5ac4ec15c9b35:search

```yaml
regex_id: 12dbe21710b8701485b5ac4ec15c9b35
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/source_intel/conditional.py:41:16"
```

### Pattern

`^\s*#\s*(if|ifdef|ifndef|elif|else|endif)\b\s*(.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:13013f8fd46a00a016099cc3d96e82a1:search

```yaml
regex_id: 13013f8fd46a00a016099cc3d96e82a1
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:602:11"
```

### Pattern

`\bself\.\w+\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:13409dea8ed1fcf9e8c98df4cef0e58b:search

```yaml
regex_id: 13409dea8ed1fcf9e8c98df4cef0e58b
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/typestate.py:113:38"
```

### Pattern

`^(\w+?)_disconnect$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:136354c31185a412d75cc62283611577:search

```yaml
regex_id: 136354c31185a412d75cc62283611577
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/module_load_abort.py:500:10"
```

### Pattern

`^end\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:13d6b93d2928d1d58c041df44078560f:search

```yaml
regex_id: 13d6b93d2928d1d58c041df44078560f
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/supply_chain/orphan_commit_dep.py:112:12"
```

### Pattern

`^[a-f0-9]{40}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:14ff7f11b084eb040e3b49743c8fe5ac:search

```yaml
regex_id: 14ff7f11b084eb040e3b49743c8fe5ac
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/reachability/composer.py:42:14"
```

### Pattern

`^\s*use\s+(?:function\s+|const\s+)?([A-Z][A-Za-z0-9_]*(?:\\[A-Za-z_][A-Za-z0-9_]*)*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:155f9199bff9539dac6d248b744d7059:search

```yaml
regex_id: 155f9199bff9539dac6d248b744d7059
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/hash_pin.py:48:11"
```

### Pattern

`^(?P<prefix>[ \t]*(?:-[ \t]+)?uses:[ \t]*)
        (?P<owner>[A-Za-z0-9_.\-]+)/
        (?P<repo>[A-Za-z0-9_.\-]+)
        (?P<sub>(?:/[A-Za-z0-9_./\-]+)?)
        @(?P<ref>[A-Za-z0-9_./\-]+)
        (?P<trailing>[ \t]*(?:\#.*)?)?$
    `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:158b857284d9a1b450bd638f624a9b59:search

```yaml
regex_id: 158b857284d9a1b450bd638f624a9b59
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:611:11"
```

### Pattern

`return\s+\$this->\w+\s*;$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:15c2aa1ffb728847f4284c38f641d1e6:search

```yaml
regex_id: 15c2aa1ffb728847f4284c38f641d1e6
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/lifecycle_collector.py:17:19"
```

### Pattern

`^(?:If|While|ElIf)\s*\((.+)\)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:16f36d7163b0731110b29931c44db662:search

```yaml
regex_id: 16f36d7163b0731110b29931c44db662
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/constant_resolution.py:33:9"
```

### Pattern

`^\s*#\s*(?:if|ifdef|ifndef)\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:17ff17d7804920ec9b9652bc1cfafc91:search

```yaml
regex_id: 17ff17d7804920ec9b9652bc1cfafc91
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/source_intel/discovery.py:301:16"
```

### Pattern

`^\s*#\s*define\s+([A-Za-z_][A-Za-z0-9_]*)\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:17ff6a6b66bf8b4f45733e1d69feafb3:search

```yaml
regex_id: 17ff6a6b66bf8b4f45733e1d69feafb3
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/constant_resolution.py:35:18"
```

### Pattern

`^\s*#\s*define\s+(\w+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1a6724bc74101f5fce86ef21821d81e4:search

```yaml
regex_id: 1a6724bc74101f5fce86ef21821d81e4
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/binary_oracle_corpora/zstd_holdout.py:193:14"
```

### Pattern

`^Function '([^']+)'`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1ae3e417c4d8dc14369bc4f5dd5f2fe7:search

```yaml
regex_id: 1ae3e417c4d8dc14369bc4f5dd5f2fe7
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/annotations/storage.py:72:21"
```

### Pattern

`^<!--\s*annotations-version:\s*(\d+)\s*-->\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1b7033bac556c996a61ca5043c92783f:search

```yaml
regex_id: 1b7033bac556c996a61ca5043c92783f
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/source_intel/analyze.py:2448:19"
```

### Pattern

`^\s*#`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1bbe53f2679ce32203293da7a738af6d:search

```yaml
regex_id: 1bbe53f2679ce32203293da7a738af6d
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/engine/coccinelle/vocab_renderer.py:25:13"
```

### Pattern

`^//\s*@vocab:\s*(\w+)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1bf9106915c1848af4d854cace79827d:search

```yaml
regex_id: 1bf9106915c1848af4d854cace79827d
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:608:43"
```

### Pattern

`^(unmarshal)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1cb607b752fe00afea6584cb2eb0ea72:search

```yaml
regex_id: 1cb607b752fe00afea6584cb2eb0ea72
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:1519:11"
```

### Pattern

`\b(?:file_get_contents|file_put_contents|fopen|readfile|unlink|rename)\s*\(\s*\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1d12e9029dbbc6c4b2662569ee43328d:search

```yaml
regex_id: 1d12e9029dbbc6c4b2662569ee43328d
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/spec_inference.py:58:5"
```

### Pattern

`^set_|^update_|^write_|^store_|^save_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:1d3eedfd78dea2d5a887946a6750bd4b:url

```yaml
regex_id: 1d3eedfd78dea2d5a887946a6750bd4b
schema_version: "1"
kind: intent_mismatch
corpus: gadievron-raptor
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/transform_sequence.py:289:19"
```

### Pattern

`url.*encode|urllib.*quote|percent.*encode|encodeURI|url\.QueryEscape|url\.PathEscape|(?:percent|url|uri|path).*quote|quote_plus`

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

## usage_mismatch:1dab4f665f3448a9c59f784a9fca32f1:search

```yaml
regex_id: 1dab4f665f3448a9c59f784a9fca32f1
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/versions/composer.py:65:11"
```

### Pattern

`^(?P<base>v?\d[\d.]*)(?:[-.]?(?P<stab>alpha|beta|rc|pre|stable|release|dev|a|b)\.?(?P<idx>\d*))?`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1eb5a4a85f2245ba83478c60c15f37bb:search

```yaml
regex_id: 1eb5a4a85f2245ba83478c60c15f37bb
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/bump/orchestrator.py:1208:23"
```

### Pattern

`^\s*(?:-\s+)?uses:\s*(?P<repo>[\w.-]+/[\w.-]+)(?P<subpath>(?:/[\w./-]+)?)@(?P<sha>[a-f0-9]{40})\s+#\s*was\s+(?P<tag>[^\s#]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1eedc56ab411678347e4589685dc9a5e:search

```yaml
regex_id: 1eedc56ab411678347e4589685dc9a5e
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/typestate.py:111:35"
```

### Pattern

`^(\w+?)_unlock$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:201ddb51c401585ef8f1dad1160a5ab9:search

```yaml
regex_id: 201ddb51c401585ef8f1dad1160a5ab9
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/labeled_attempts/types.py:29:19"
```

### Pattern

`^[0-9a-fA-F]{8,64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:20d834149730afb0e7e5e935dfe0be7e:search

```yaml
regex_id: 20d834149730afb0e7e5e935dfe0be7e
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/suppressions.py:268:15"
```

### Pattern

`^\d{4}-\d{2}-\d{2}`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:22256709112018befd16cb80da0c66d2:search

```yaml
regex_id: 22256709112018befd16cb80da0c66d2
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/annotations/storage.py:96:11"
```

### Pattern

`^<!--\s*meta:\s*(.*?)\s*-->\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:223808896339376e8c462a564740d59e:search

```yaml
regex_id: 223808896339376e8c462a564740d59e
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/pnpm_lock.py:139:10"
```

### Pattern

`^/(?P<name>(?:@[^/]+/)?[^/@]+)@(?P<version>.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2266d14d4f3ddae4a42f12d64b4f2666:search

```yaml
regex_id: 2266d14d4f3ddae4a42f12d64b4f2666
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/fail_open_detector.py:149:21"
```

### Pattern

`^\s*return\s+(?P<value>\{[^}]*\}|\[[^\]]*\]|None|True|False|\"\"|''|0)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:22925acd1caadf979a5b57503ce4fa6d:search

```yaml
regex_id: 22925acd1caadf979a5b57503ce4fa6d
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/typestate.py:108:5"
```

### Pattern

`^(\w+?)_alloc$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:22ab4164ba8128b5c7d6e01430db7d62:search

```yaml
regex_id: 22ab4164ba8128b5c7d6e01430db7d62
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/package_json.py:88:16"
```

### Pattern

`^v?\d+(?:\.\d+){0,2}(?:[-+].+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:22ab7ccb74dfab645243bb624980878e:search

```yaml
regex_id: 22ab7ccb74dfab645243bb624980878e
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/binary/glibc_versions.py:23:14"
```

### Pattern

`^\s*(\d+)(?:\.(\d+))?(?:\.\d+)?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:22af176ddf341c775d8a7b6917ef213f:search

```yaml
regex_id: 22af176ddf341c775d8a7b6917ef213f
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/exploit_feasibility/analyzer.py:3951:24"
```

### Pattern

`^Seccomp:\s*(\d+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:22f89b8ddb89f1615411a678558735a5:search

```yaml
regex_id: 22f89b8ddb89f1615411a678558735a5
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/constant_resolution.py:34:12"
```

### Pattern

`^\s*#\s*endif\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:235c10a7ec3de9deb3cddf40f71cf017:search

```yaml
regex_id: 235c10a7ec3de9deb3cddf40f71cf017
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:613:41"
```

### Pattern

`^(free)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:23d735beef66d028db5b75972a102bfc:search

```yaml
regex_id: 23d735beef66d028db5b75972a102bfc
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/sibling_analysis.py:247:4"
```

### Pattern

`^(validate|check|verify)_(\w+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:24e8a4717b1375049dbba81ac0416bd7:search

```yaml
regex_id: 24e8a4717b1375049dbba81ac0416bd7
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/reachability/gomod.py:32:19"
```

### Pattern

`^\s*import\s*\(\s*([^)]*)\)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:26c263f879b9b002f5e3613aa2ae762a:search

```yaml
regex_id: 26c263f879b9b002f5e3613aa2ae762a
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/typestate.py:112:5"
```

### Pattern

`^(\w+?)_start$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:26c7f97b2e8561388a8f958cef166527:search

```yaml
regex_id: 26c7f97b2e8561388a8f958cef166527
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/binary_oracle_edges.py:105:15"
```

### Pattern

`^[0-9a-f]{8,128}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2711d5b1766d739638811fb2b74bfaae:search

```yaml
regex_id: 2711d5b1766d739638811fb2b74bfaae
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/condition_smt.py:1904:19"
```

### Pattern

`^\s*return\s+(-\w+|NULL|ERR_PTR\s*\(|err|ret|rc|status)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:275b9e14b472164a695b5cc57f7b274b:search

```yaml
regex_id: 275b9e14b472164a695b5cc57f7b274b
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/inline_installs/__init__.py:692:25"
```

### Pattern

`^(\s*)(?:-\s+)?run:\s*[|>][+-]?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:276d450d5259c6d6bb1ce34d8d02c70f:search

```yaml
regex_id: 276d450d5259c6d6bb1ce34d8d02c70f
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/spec_inference.py:59:5"
```

### Pattern

`^delete_|^remove_|^drop_|^unlink_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2779978ae149bc3dbc4a65c8508ce970:search

```yaml
regex_id: 2779978ae149bc3dbc4a65c8508ce970
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/sweep.py:67:35"
```

### Pattern

`^[A-Za-z_][A-Za-z0-9_]*(\.[A-Za-z_][A-Za-z0-9_]*)*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:28944743d31b0da20aaf5c27cbfd7d95:search

```yaml
regex_id: 28944743d31b0da20aaf5c27cbfd7d95
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/spec_inference.py:55:5"
```

### Pattern

`^hash_|^hmac_|^sign_|^encrypt_|^decrypt_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:297d03f44600cdbe02458ac27a83fe62:search

```yaml
regex_id: 297d03f44600cdbe02458ac27a83fe62
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:620:45"
```

### Pattern

`^(unsubscribe)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:29a375988633380ef16f2734933cce15:search

```yaml
regex_id: 29a375988633380ef16f2734933cce15
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/binary_oracle_corpora/zlib.py:156:17"
```

### Pattern

`^Lines executed:([\d.]+)% of \d+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:29becc482c2f1b7503073fb758da9530:search

```yaml
regex_id: 29becc482c2f1b7503073fb758da9530
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/sibling_analysis.py:407:5"
```

### Pattern

`^(?:decode|decrypt|deserialize|unmarshal|unpack|decompress)_(\w+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:29d88fd2f901ca1c1c8952e826459d63:search

```yaml
regex_id: 29d88fd2f901ca1c1c8952e826459d63
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/source_intel/discovery.py:91:13"
```

### Pattern

`^\s*#\s*define\s+([A-Za-z_][A-Za-z0-9_]*)\s*(?:\([^)]*\))?\s+(.+?)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2ab13aaa849bacf32b601d9c0e78f438:search

```yaml
regex_id: 2ab13aaa849bacf32b601d9c0e78f438
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/exploit_feasibility/smt_verbs.py:85:18"
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

## usage_mismatch:2af472762e15b9fd32429a71794b6205:search

```yaml
regex_id: 2af472762e15b9fd32429a71794b6205
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/source_intel/adapter.py:1560:20"
```

### Pattern

`^\s*(?:-?\d+[uUlL]*|0[xX][0-9a-fA-F]+[uUlL]*|NULL|nullptr|\(void\s*\*\s*\)\s*0)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2b80ec11c7e63d20513eb96cf93c932e:search

```yaml
regex_id: 2b80ec11c7e63d20513eb96cf93c932e
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/platform_matrix/matrix.py:453:17"
```

### Pattern

`^\s*runs-on:\s*([^\n#]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2bb5743f8e4c7addb415d2c6d3b27564:search

```yaml
regex_id: 2bb5743f8e4c7addb415d2c6d3b27564
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/update.py:1619:16"
```

### Pattern

`^([ \t]*)("?)([A-Za-z0-9_\-.]+)\2\s*=\s*"([^"]*)"`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2c1a9ded54e16ad9250450805493e3b1:search

```yaml
regex_id: 2c1a9ded54e16ad9250450805493e3b1
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/spec_inference.py:49:5"
```

### Pattern

`^parse_|^decode_|^deserialize_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2ca4086741a99edb72c61ef1fa8ac81d:search

```yaml
regex_id: 2ca4086741a99edb72c61ef1fa8ac81d
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/dark_verify/_execute.py:49:16"
```

### Pattern

`^[a-zA-Z_][a-zA-Z0-9_.:/]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2e664d28742f3dbabb257102d1256642:search

```yaml
regex_id: 2e664d28742f3dbabb257102d1256642
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/block_sibling_analysis.py:313:14"
```

### Pattern

`^(\s*)(if|elif|else\s+if|else)\s*[\s(:]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2ef108027288196d9afe41d9a7550a5c:search

```yaml
regex_id: 2ef108027288196d9afe41d9a7550a5c
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:625:5"
```

### Pattern

`^(open)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2f0588a933b21a17aa6bbf59de000248:search

```yaml
regex_id: 2f0588a933b21a17aa6bbf59de000248
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:628:5"
```

### Pattern

`^(setup)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2f87d695ddd01aec1e859ecc1e1717cc:search

```yaml
regex_id: 2f87d695ddd01aec1e859ecc1e1717cc
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/translation_view.py:66:12"
```

### Pattern

`^(\w+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:31d342e7d2d78852c690f059991ea88a:search

```yaml
regex_id: 31d342e7d2d78852c690f059991ea88a
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/typestate.py:108:36"
```

### Pattern

`^(\w+?)_free$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3200013f9231e6893402bce0432bd67a:search

```yaml
regex_id: 3200013f9231e6893402bce0432bd67a
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/cve_diff/cve_diff/cli/main.py:200:20"
```

### Pattern

`^DiscoveryError:.*?\bagent surrendered \((budget_cost_usd|budget_iterations|budget_tokens|budget_s)\)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:321056def305e47c4257e90a924175b2:search

```yaml
regex_id: 321056def305e47c4257e90a924175b2
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:608:11"
```

### Pattern

`^\s*\d+\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:321df4b3015cbf3e5ffe0940f9c576bb:search

```yaml
regex_id: 321df4b3015cbf3e5ffe0940f9c576bb
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:608:5"
```

### Pattern

`^(marshal)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3225e3249305b688abfae25335d0cc1b:search

```yaml
regex_id: 3225e3249305b688abfae25335d0cc1b
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:614:39"
```

### Pattern

`^(put)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:32fd74c029581783655f9ff35422c7a3:search

```yaml
regex_id: 32fd74c029581783655f9ff35422c7a3
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:599:11"
```

### Pattern

`return\s+\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:33c2a35e0a9cf02d7da076b329e6ff9d:search

```yaml
regex_id: 33c2a35e0a9cf02d7da076b329e6ff9d
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/gemfile.py:51:15"
```

### Pattern

`^\s*gem\s+
        (?P<quote>['"])(?P<name>[A-Za-z0-9_.\-]+)(?P=quote)
        (?P<rest>[^\n#]*)
    `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:33cbbbfef009c502f1820e0ed3763c56:search

```yaml
regex_id: 33cbbbfef009c502f1820e0ed3763c56
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/reachability/maven.py:70:13"
```

### Pattern

`^\s*import\s+(?:static\s+)?([A-Za-z_][A-Za-z0-9_.]*)\s*(?:\.\*)?\s*;`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:340b65f45b98e6bea4c82b0efb74165e:search

```yaml
regex_id: 340b65f45b98e6bea4c82b0efb74165e
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:615:11"
```

### Pattern

`return\s+\d+\s*;$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:35300f5b66b856e3412abe578d8765f5:search

```yaml
regex_id: 35300f5b66b856e3412abe578d8765f5
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:595:11"
```

### Pattern

`return\s+\w+\.\w+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3540938d8354c8747348d7a8ecf90e89:search

```yaml
regex_id: 3540938d8354c8747348d7a8ecf90e89
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/_test_paths.py:52:16"
```

### Pattern

`^(test_.*\.py|.*_test\.py|.*\.test\.(?:py|js|ts|jsx|tsx|mjs|cjs)|.*\.spec\.(?:py|js|ts|jsx|tsx|mjs|cjs)|.*_test\.go|.*_test\.rb|.*_spec\.rb|.*Test\.(?:java|kt)|.*Tests\.(?:java|kt)|.*IT\.(?:java|kt)|.*_test\.rs|.*Test\.cs|.*Tests\.cs|.*Test\.php)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:356448c3f699984988149a0923dd25c3:search

```yaml
regex_id: 356448c3f699984988149a0923dd25c3
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/sibling_analysis.py:409:5"
```

### Pattern

`^(\w+?)_(?:sanitize|sanitise|escape|clean)_output$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:36d49a9554d251603b1cbed877d92827:search

```yaml
regex_id: 36d49a9554d251603b1cbed877d92827
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/hash_pin.py:59:10"
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

## usage_mismatch:36d8fd5922993e771290b0239123057e:search

```yaml
regex_id: 36d8fd5922993e771290b0239123057e
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/gitmodules.py:69:14"
```

### Pattern

`^\[submodule\s+"(.+?)"\s*\]\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:375a8da0ab772991b579bba070916e56:search

```yaml
regex_id: 375a8da0ab772991b579bba070916e56
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:615:39"
```

### Pattern

`^(set)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:37b65c068dbf8fb5845d33b249adf015:search

```yaml
regex_id: 37b65c068dbf8fb5845d33b249adf015
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/supply_chain/orphan_commit_dep.py:105:21"
```

### Pattern

`^(?P<owner>[\w.\-]+)/(?P<repo>[\w.\-]+)(?:#(?P<ref>[\w./\-]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:39499030185a9a3f22b1a0923ac60d86:search

```yaml
regex_id: 39499030185a9a3f22b1a0923ac60d86
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/sbom_import.py:194:11"
```

### Pattern

`^pkg:(?P<type>[A-Za-z0-9.+-]+)/(?P<path_and_version>[^?#]+)(?:[?#].*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3a0f5fd803dde1614c72db8a09bbd437:search

```yaml
regex_id: 3a0f5fd803dde1614c72db8a09bbd437
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:606:11"
```

### Pattern

`return\s+self\.\w+\s*;?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3a580c18b385a6e20cd2a0f9c6cfa0a8:search

```yaml
regex_id: 3a580c18b385a6e20cd2a0f9c6cfa0a8
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/fuzzing/afl_runner.py:26:14"
```

### Pattern

`^-?\d+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3ab8b305bdf198cd6ee39262cad1ed6c:search

```yaml
regex_id: 3ab8b305bdf198cd6ee39262cad1ed6c
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:617:11"
```

### Pattern

`return\s+(true|false|null)\s*;$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3b35d15e9093e76c9e038b45d4c9a519:search

```yaml
regex_id: 3b35d15e9093e76c9e038b45d4c9a519
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/platform_matrix/matrix.py:505:22"
```

### Pattern

`^\s*platforms:\s*([^\n#]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3ba71ce9beba97862d71540be769dce1:search

```yaml
regex_id: 3ba71ce9beba97862d71540be769dce1
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/smt_solver/path_feasibility.py:261:12"
```

### Pattern

`^[a-z_][a-z0-9_]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3bcb9680b31a413e4aa0994ffb1df615:search

```yaml
regex_id: 3bcb9680b31a413e4aa0994ffb1df615
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/transitive_drop/detector.py:260:13"
```

### Pattern

`^v?(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:\.(\d+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3bf494d25dc98503e5b43554bbf83dde:search

```yaml
regex_id: 3bf494d25dc98503e5b43554bbf83dde
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/inline_installs/__init__.py:623:21"
```

### Pattern

`^\s*RUN\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3d3c4304fe3209103b757067692fd6dd:search

```yaml
regex_id: 3d3c4304fe3209103b757067692fd6dd
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:631:11"
```

### Pattern

`return\s+this\._\w+\s*;?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3e000f6b0be879b786cfd807cf07004f:search

```yaml
regex_id: 3e000f6b0be879b786cfd807cf07004f
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/orchestrator.py:7440:15"
```

### Pattern

`^\s*(\w+)\s*=\s*(.+?)(?:\s*//.*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3e1197ac044ba0ef7043c3997643c967:search

```yaml
regex_id: 3e1197ac044ba0ef7043c3997643c967
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/translation_view.py:59:16"
```

### Pattern

`^\s*#\s*(if|ifdef|ifndef|elif|else|endif)\b(.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3e5159ce86832b1381f6dfe0e7c1d314:search

```yaml
regex_id: 3e5159ce86832b1381f6dfe0e7c1d314
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/orchestration/trace_widening.py:21:20"
```

### Pattern

`^(.+?):(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3e5d3b58aba3f19415fb3aed12e8cf97:search

```yaml
regex_id: 3e5d3b58aba3f19415fb3aed12e8cf97
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/cargo.py:281:22"
```

### Pattern

`^\s*(=|\^|~|>=?|<=?)\s*(\d[^\s,]*)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3eecaa37f33b9ecec8326b6ce637e20f:search

```yaml
regex_id: 3eecaa37f33b9ecec8326b6ce637e20f
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/pom_inheritance.py:105:18"
```

### Pattern

`^[A-Za-z0-9._+\-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3ef519a69376cebaaf684878eb0adab8:search

```yaml
regex_id: 3ef519a69376cebaaf684878eb0adab8
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/supply_chain/commit_provenance.py:133:26"
```

### Pattern

`^\d+\+(?:dependabot|renovate|github-actions|snyk-bot|mend-bot|imgbot|allcontributors)\[bot\]@users\.noreply\.github\.com$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3f8d631db587250fea1d1790c400aa12:search

```yaml
regex_id: 3f8d631db587250fea1d1790c400aa12
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/dockerfile/parser.py:59:14"
```

### Pattern

`\s+AS\s+(?P<name>[A-Za-z0-9_-]+)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:417120714e494ab29c7ea396f4b1a120:search

```yaml
regex_id: 417120714e494ab29c7ea396f4b1a120
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/exploit_feasibility/analyzer.py:3376:24"
```

### Pattern

`^([0-9a-f]+)\s+\w+\s+system(?:@@|\s|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:460a7ab3848d64e9d0eb87c7cbe910f1:search

```yaml
regex_id: 460a7ab3848d64e9d0eb87c7cbe910f1
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/wheel_compat/wheel_tags.py:85:23"
```

### Pattern

`^(manylinux1|manylinux2010|manylinux2014)_(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:46111d55a9aa6460c55094b58ba7663c:match

```yaml
regex_id: 46111d55a9aa6460c55094b58ba7663c
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/versions/semver.py:215:12"
```

### Pattern

`^(>=|<=|>|<|=|\^|~)?\s*(.*)$`

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

## usage_mismatch:46fa84081f21d3e4f4dc9da48b12df42:search

```yaml
regex_id: 46fa84081f21d3e4f4dc9da48b12df42
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:636:11"
```

### Pattern

`return\s+self\.\w+\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:47be341c96bb623b99ccfaa63568e281:search

```yaml
regex_id: 47be341c96bb623b99ccfaa63568e281
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/upstream_latest/_version_filter.py:41:14"
```

### Pattern

`^v?(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:\.(\d+))?-([a-z][a-z0-9-]*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:48a27bfa26aef501d39d43b4cb89d860:search

```yaml
regex_id: 48a27bfa26aef501d39d43b4cb89d860
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/autonomous/exploit_validator.py:358:24"
```

### Pattern

`: fatal error: (.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:48f2e65bc477fb504f98d79e5b678333:search

```yaml
regex_id: 48f2e65bc477fb504f98d79e5b678333
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/zkpox/bundle.py:46:14"
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

## usage_mismatch:49b06d4d989ca2e5d651f9cff612f765:search

```yaml
regex_id: 49b06d4d989ca2e5d651f9cff612f765
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/spec_inference.py:54:5"
```

### Pattern

`^auth(?:enticate)?_|^login_|^verify_(?:password|token|cred)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4a5fb7241c46a2e0a4663b59c34f8e03:search

```yaml
regex_id: 4a5fb7241c46a2e0a4663b59c34f8e03
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:641:11"
```

### Pattern

`return\s+\$self->\{\s*\w+\s*\}\s*;$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4ab3393ec82051128dc9a84c9a4c5aad:search

```yaml
regex_id: 4ab3393ec82051128dc9a84c9a4c5aad
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/module_load_abort.py:505:12"
```

### Pattern

`^(raise\s+\S|abort\b|exit\b|exit!|fail\s+\S|Kernel\.(abort|exit))`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4b7948fe729866d9d127792c31e6bf74:search

```yaml
regex_id: 4b7948fe729866d9d127792c31e6bf74
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/spec_inference.py:61:5"
```

### Pattern

`^compare_|^cmp_|^diff_|^eq_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4bce507f47fe06185f0ce77170d5c753:search

```yaml
regex_id: 4bce507f47fe06185f0ce77170d5c753
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:611:52"
```

### Pattern

`^(sanitize_output)_?(.+)?`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4bdfd7971e38443ca011427997fbc376:search

```yaml
regex_id: 4bdfd7971e38443ca011427997fbc376
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/license/spdx.py:40:16"
```

### Pattern

`^[A-Za-z0-9.+\-]+(?:\s+(?:AND|OR|WITH)\s+[A-Za-z0-9.+\-]+)+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4dc35fe1caa116adfbc47eea5fdd2742:search

```yaml
regex_id: 4dc35fe1caa116adfbc47eea5fdd2742
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/requirements.py:92:19"
```

### Pattern

`^\s*#`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4e1103a9313c1a4db862ef684f3224a8:search

```yaml
regex_id: 4e1103a9313c1a4db862ef684f3224a8
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/binary/glibc_versions.py:70:21"
```

### Pattern

`^\s*(\d+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4e6f679c776319b18388f476e9a396b4:search

```yaml
regex_id: 4e6f679c776319b18388f476e9a396b4
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/header_functions.py:25:15"
```

### Pattern

`^[ \t]*(?:__attribute__\s*\(\([^()]*(?:\([^()]*\)[^()]*)*\)\)\s+)*(?:\w+\s+)*?(\w+)\s*\([^)]*\)\s*\{`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4ee474d0777a3135e15a6ccff0e38640:search

```yaml
regex_id: 4ee474d0777a3135e15a6ccff0e38640
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:617:5"
```

### Pattern

`^(ref)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4fb776d1cca51a8d7f5bf8678a676cd8:search

```yaml
regex_id: 4fb776d1cca51a8d7f5bf8678a676cd8
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:623:5"
```

### Pattern

`^(enable)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5040e76992e8285aa5fe3eaf92489f78:match

```yaml
regex_id: 5040e76992e8285aa5fe3eaf92489f78
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/oci/registry_hosts.py:146:12"
```

### Pattern

`^\d+\.dkr\.ecr\.([a-z0-9-]+)\.amazonaws\.com$`

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

## usage_mismatch:509496cb573f9d8b75be8a006589079a:search

```yaml
regex_id: 509496cb573f9d8b75be8a006589079a
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/platform_matrix/matrix.py:148:11"
```

### Pattern

`^\s*FROM\s+(?:--platform=(\S+)\s+)?(\S+)(?:\s+AS\s+\S+)?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:522fa714ec658d9b12124c52ca889fcb:search

```yaml
regex_id: 522fa714ec658d9b12124c52ca889fcb
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:1538:11"
```

### Pattern

`\bheader\s*\(\s*["\']Location.*\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:526fb9e91b7b87cd3d44eac036bb5684:search

```yaml
regex_id: 526fb9e91b7b87cd3d44eac036bb5684
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/reachability/cargo.py:42:13"
```

### Pattern

`^[ \t]*(?:pub\s+)?extern\s+crate\s+([A-Za-z_][A-Za-z0-9_]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5276d352a134bd2273c8fde514e0d06b:search

```yaml
regex_id: 5276d352a134bd2273c8fde514e0d06b
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/reachability/nuget.py:45:17"
```

### Pattern

`^\s*Imports\s+(?:[A-Za-z_][A-Za-z0-9_]*\s*=\s*)?([A-Za-z_][A-Za-z0-9_.]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:53155a098e44b0c4afde2ec06716d501:search

```yaml
regex_id: 53155a098e44b0c4afde2ec06716d501
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:606:5"
```

### Pattern

`^(encrypt)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:535c0c713efe62b614770c4220b61c0e:search

```yaml
regex_id: 535c0c713efe62b614770c4220b61c0e
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:616:5"
```

### Pattern

`^(acquire)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5450731e3369a24f86290ade00c642cc:match

```yaml
regex_id: 5450731e3369a24f86290ade00c642cc
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/exploit_feasibility/analyzer.py:3438:39"
```

### Pattern

`^(0x[0-9a-f]+)\s+(.+)$`

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

## usage_mismatch:547174f0130fc5159c7f9f76f6bf5440:search

```yaml
regex_id: 547174f0130fc5159c7f9f76f6bf5440
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:627:40"
```

### Pattern

`^(cleanup)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:54786d36e577af94b298fbf2a21c335f:search

```yaml
regex_id: 54786d36e577af94b298fbf2a21c335f
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/sibling_analysis.py:249:4"
```

### Pattern

`^(parse|decode|deserialize|unmarshal)_(\w+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:564067598a078890b635839a9a4c4cb7:search

```yaml
regex_id: 564067598a078890b635839a9a4c4cb7
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/context.py:2544:22"
```

### Pattern

`^## \d+\.\s+(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:59277cfa7ee1b36c41cf7cfc8ea4ca10:search

```yaml
regex_id: 59277cfa7ee1b36c41cf7cfc8ea4ca10
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/fail_open_detector.py:293:15"
```

### Pattern

`^\s*return\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:595e6d227b392d08f75dc834cde537e3:search

```yaml
regex_id: 595e6d227b392d08f75dc834cde537e3
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/reachability/nuget.py:34:15"
```

### Pattern

`^\s*(?:global\s+)?using\s+(?:[A-Za-z_][A-Za-z0-9_]*\s*=\s*)?([A-Za-z_][A-Za-z0-9_.]*)\s*;`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5970bae68a14121eb37a1a63cd8f09b2:search

```yaml
regex_id: 5970bae68a14121eb37a1a63cd8f09b2
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/dead_scope.py:381:21"
```

### Pattern

`\b(\w+)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:59bc1aaff27afce260c4f595b58b9750:search

```yaml
regex_id: 59bc1aaff27afce260c4f595b58b9750
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:606:43"
```

### Pattern

`^(decrypt)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5b3ac63d48d8e47a4f5856f5de799701:match

```yaml
regex_id: 5b3ac63d48d8e47a4f5856f5de799701
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/reachability_gates.py:182:11"
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

## usage_mismatch:5b45c60740255067026336442a32a99e:search

```yaml
regex_id: 5b45c60740255067026336442a32a99e
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/typestate.py:111:5"
```

### Pattern

`^(\w+?)_lock$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5bb7297a07007d0281783584b46a2db9:search

```yaml
regex_id: 5bb7297a07007d0281783584b46a2db9
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/yarn_lock.py:153:11"
```

### Pattern

`^([A-Za-z_][\w-]*)\s+(?:"([^"]*)"|([^\s].*))$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5d49e6391c8d0bb0bc793f91e95e75b5:search

```yaml
regex_id: 5d49e6391c8d0bb0bc793f91e95e75b5
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:625:40"
```

### Pattern

`^(close)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5dfb4cb51b3d9da99d11c9f793a72d11:search

```yaml
regex_id: 5dfb4cb51b3d9da99d11c9f793a72d11
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/_util.py:21:21"
```

### Pattern

`^[A-Za-z0-9_][A-Za-z0-9_\-.]*\.cocci$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5e29ed74d12b1c6774a689cccb72cb95:match

```yaml
regex_id: 5e29ed74d12b1c6774a689cccb72cb95
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/optimise.py:665:12"
```

### Pattern

`^(['"])([A-Za-z0-9_\-.]+)\s*(['"])\s*,?\s*$`

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

## usage_mismatch:5e3004d4b0b8d02c93f94dd7eaa37d89:match

```yaml
regex_id: 5e3004d4b0b8d02c93f94dd7eaa37d89
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/reachability_gates.py:322:11"
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

## usage_mismatch:5e919119e62441d9a5b69d5a00ff2772:search

```yaml
regex_id: 5e919119e62441d9a5b69d5a00ff2772
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/joern/runner.py:37:27"
```

### Pattern

`^[A-Za-z_][A-Za-z0-9_]*(\.[A-Za-z_][A-Za-z0-9_]*)*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5fc358ae4ae0cb9245a6f8c411e29a32:search

```yaml
regex_id: 5fc358ae4ae0cb9245a6f8c411e29a32
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/translation_view.py:64:14"
```

### Pattern

`^(!\s*)?defined\s*\(\s*(\w+)\s*\)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5fe531bf45903f10be00ff977e1b35f2:match

```yaml
regex_id: 5fe531bf45903f10be00ff977e1b35f2
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/exploit_feasibility/analyzer.py:3674:24"
```

### Pattern

`^(0x[0-9a-f]+)\s+:\s+(.+)$`

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

## usage_mismatch:6033d00ec70f3833beef64f1a39de764:search

```yaml
regex_id: 6033d00ec70f3833beef64f1a39de764
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/engine/coccinelle/vocab_renderer.py:26:11"
```

### Pattern

`^//\s*@vocab-tmpl:\s*(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:60997b5128c6c2b9d4efe98a677e571a:search

```yaml
regex_id: 60997b5128c6c2b9d4efe98a677e571a
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/spec_inference.py:56:5"
```

### Pattern

`^is_|^has_|^can_|^should_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:60d165ddd3c9026311e3b1fd6b0db4f9:search

```yaml
regex_id: 60d165ddd3c9026311e3b1fd6b0db4f9
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/module_load_abort.py:498:13"
```

### Pattern

`^(class|module|def|begin|if|unless|while|until|case|for)\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6117b197b409763797459b9b201b025f:search

```yaml
regex_id: 6117b197b409763797459b9b201b025f
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:605:5"
```

### Pattern

`^(encode)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6350946b14e306f44d1501be00bc6de1:search

```yaml
regex_id: 6350946b14e306f44d1501be00bc6de1
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/sandbox/observe_profile.py:129:19"
```

### Pattern

`^(?P<ip>[^\s]+):(?P<port>\d+)\s+\((?P<family>AF_INET6?)\)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:64377c0ff292c00e75cc619980c61e06:search

```yaml
regex_id: 64377c0ff292c00e75cc619980c61e06
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/spec_inference.py:60:5"
```

### Pattern

`^copy_|^clone_|^dup(?:licate)?_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:645ce8512936ea92c7891c4575a9a43b:search

```yaml
regex_id: 645ce8512936ea92c7891c4575a9a43b
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/dynamic_sweep.py:384:12"
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

## usage_mismatch:646102c6754a3f41aa512a05ddc8becf:search

```yaml
regex_id: 646102c6754a3f41aa512a05ddc8becf
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/binary_oracle_corpora/libsodium.py:168:14"
```

### Pattern

`^Function '([^']+)'`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:65cdcb912bd95491fd2edfc3fcac71be:search

```yaml
regex_id: 65cdcb912bd95491fd2edfc3fcac71be
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/gitmodules.py:70:13"
```

### Pattern

`^\s*([A-Za-z0-9_\-]+)\s*=\s*(.+?)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:65fbf7a2827eb45b209bbacbb3cdb37b:search

```yaml
regex_id: 65fbf7a2827eb45b209bbacbb3cdb37b
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/constant_resolution.py:38:17"
```

### Pattern

`^[-()\s0-9a-fA-FxX+*/%|&^~<>]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6792778af02fefbf616268b7ea657f5a:search

```yaml
regex_id: 6792778af02fefbf616268b7ea657f5a
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/platform_matrix/matrix.py:630:23"
```

### Pattern

`^(Dockerfile|.*\.dockerfile)$|^Containerfile$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:682c76c5232152f626cc8fb97cb24d33:search

```yaml
regex_id: 682c76c5232152f626cc8fb97cb24d33
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/source_intel/analyze.py:1128:13"
```

### Pattern

`^\s*sizeof\s*\(`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6929ac7cf19898e8942d63a03b8b6b3a:search

```yaml
regex_id: 6929ac7cf19898e8942d63a03b8b6b3a
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/codeql_validation.py:52:16"
```

### Pattern

`^~?[A-Za-z_][A-Za-z0-9_]*(?:::[A-Za-z_~][A-Za-z0-9_]*)*(?:<[A-Za-z0-9_:,\s*&]*>)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:69962e7cadbab093a3cee905bca03794:search

```yaml
regex_id: 69962e7cadbab093a3cee905bca03794
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:578:11"
```

### Pattern

`return\s+\w+->\w+\s*;$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:69cf935db7f8f604ce60faa3706fa805:search

```yaml
regex_id: 69cf935db7f8f604ce60faa3706fa805
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:597:11"
```

### Pattern

`return\s+\w+\.\w+\s*,\s*nil$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:6ad4806f2fafb09f981bb047522835ac:url

```yaml
regex_id: 6ad4806f2fafb09f981bb047522835ac
schema_version: "1"
kind: intent_mismatch
corpus: gadievron-raptor
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/security/prompt_envelope.py:158:23"
```

### Pattern

`!\[[^\]]{0,8192}\]\([^)]{1,8192}\)|\[[^\]]{0,8192}\]\((?:https?|ht%74ps?|data|javascript|vbscript|file|ftp)?:[^)]{1,8192}\)|\[[^\]]{0,8192}\]\(//[^)]{1,8192}\)|<(?:img|iframe|object|embed|video|audio|source|link|script|base|form|use)\b[^>]{0,8192}>|<a\s[^>]{0,8192}>|<svg\b[^>]{0,8192}>|<meta\b[^>]{0,8192}>|<style\b[^>]*>.*?</style>|<style\b[^>]*>|@import\s+url\([^)]*\)|\[[^\]]+\]:\s*(?:https?|data|javascript|vbscript|file|ftp):[^\s]+|data:[a-zA-Z0-9+./;-]{1,256},[^\s)]{0,65536}`

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

## usage_mismatch:6b6882bc1eb55b494c2ed15254e07731:search

```yaml
regex_id: 6b6882bc1eb55b494c2ed15254e07731
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/spec_inference.py:63:5"
```

### Pattern

`^send_|^emit_|^publish_|^notify_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6bb73f5254bdc056def08ff820a44183:match

```yaml
regex_id: 6bb73f5254bdc056def08ff820a44183
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/gomod.py:283:35"
```

### Pattern

`^v\d+(\.\d+){0,2}$`

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

## usage_mismatch:6c2f9692df4f562daec37d5a8cb6c1c7:search

```yaml
regex_id: 6c2f9692df4f562daec37d5a8cb6c1c7
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/pnpm_lock.py:140:10"
```

### Pattern

`^/(?P<name>(?:@[^/]+/)?[^/]+)/(?P<version>.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6e60957ab429557af1976f46e2e7f8a7:search

```yaml
regex_id: 6e60957ab429557af1976f46e2e7f8a7
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/cfg_conditions.py:90:22"
```

### Pattern

`^(?:If|While|ElIf|For)\s*\((.+)\)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6e840562512a58ce5da328cebed51758:search

```yaml
regex_id: 6e840562512a58ce5da328cebed51758
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/cve_diff/cve_diff/diffing/extract_via_patch_url.py:183:11"
```

### Pattern

`^@@ `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6f3c6a74390b2bd486703e204e9ee928:search

```yaml
regex_id: 6f3c6a74390b2bd486703e204e9ee928
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/module_load_abort.py:396:22"
```

### Pattern

`^[ \t]*compile_error\s*!\s*\(`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6f499d38ff02ebb402743caa5a6ede75:search

```yaml
regex_id: 6f499d38ff02ebb402743caa5a6ede75
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/dataflow/label.py:122:15"
```

### Pattern

`^\d{4}-\d{2}-\d{2}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6f6dd4f23f150f5151a6d5e34ca76eb8:search

```yaml
regex_id: 6f6dd4f23f150f5151a6d5e34ca76eb8
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:621:43"
```

### Pattern

`^(disconnect)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6feecf33535201f146bb7aded51aff56:search

```yaml
regex_id: 6feecf33535201f146bb7aded51aff56
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/condition_smt.py:1469:12"
```

### Pattern

`^(\w+)\s*:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:70b80cc6fe5e0e35082a6649613b5dd9:search

```yaml
regex_id: 70b80cc6fe5e0e35082a6649613b5dd9
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:580:11"
```

### Pattern

`return\s+\w+\.\w+\s*;$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:70fbe5a9abb3c7e37a8aeb5517d610a3:search

```yaml
regex_id: 70fbe5a9abb3c7e37a8aeb5517d610a3
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/sibling_analysis.py:246:4"
```

### Pattern

`^(render|format|emit|display)_(\w+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:710166c09de8c8111a3ff705605ab283:search

```yaml
regex_id: 710166c09de8c8111a3ff705605ab283
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/api_compat.py:137:13"
```

### Pattern

`^(\d+)\.(\d+)(?:\.(\d+))?`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:722135ba8283ecdfe264deee29fbafa1:search

```yaml
regex_id: 722135ba8283ecdfe264deee29fbafa1
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/orchestrator.py:7449:24"
```

### Pattern

`^\s*(//|loc_|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:730c1d1e769628174acd86905d8e3058:search

```yaml
regex_id: 730c1d1e769628174acd86905d8e3058
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/upstream_latest/_version_filter.py:26:13"
```

### Pattern

`^v?(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:\.(\d+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:731e8512d6979e3256ca609fdbe0a6cd:search

```yaml
regex_id: 731e8512d6979e3256ca609fdbe0a6cd
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/dataflow/cvefix_bridge.py:113:16"
```

### Pattern

`(?:^|/)(?:tests?|specs?|__tests?__)/|(?:^|/)test_[^/]+\.py$|_test\.(?:go|py|rb|js|ts|jsx|tsx|java)$|_spec\.(?:rb|py|js|ts|jsx|tsx)$|\.test\.[jt]sx?$|\.spec\.[jt]sx?$|(?:^|/)Test[A-Z][^/]*\.java$|(?:^|/)[^/]+Tests?\.java$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:73a939fe750ab2ecc97d2e3ac543a90b:search

```yaml
regex_id: 73a939fe750ab2ecc97d2e3ac543a90b
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:626:41"
```

### Pattern

`^(stop)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:73fcfe465076bc40e97ac1591e47dfaf:search

```yaml
regex_id: 73fcfe465076bc40e97ac1591e47dfaf
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/inline_installs/_managers.py:528:14"
```

### Pattern

`^[A-Za-z0-9][A-Za-z0-9._\-]*(?:/[A-Za-z0-9._\-]+)*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:758017830161f631cf052dbed4ddddc3:search

```yaml
regex_id: 758017830161f631cf052dbed4ddddc3
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:627:5"
```

### Pattern

`^(init)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:75a76f91573ef35f96433b88bae7817d:search

```yaml
regex_id: 75a76f91573ef35f96433b88bae7817d
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/supply_chain/orphan_commit_dep.py:95:14"
```

### Pattern

`^git(?:\+(?:https?|ssh))?://(?:[^@/]+@)?[\w.\-]+(?:/|:)(?P<owner>[\w.\-]+)/(?P<repo>[\w.\-]+?)(?:\.git)?(?:#(?P<ref>[\w./\-]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:75b8b5e67479275387a048135a72f4b2:match

```yaml
regex_id: 75b8b5e67479275387a048135a72f4b2
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/build_id_cache.py:94:15"
```

### Pattern

`^[0-9a-fA-F]+$`

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

## intent_mismatch:76526fbaebf322b37602d48da8c1ae6b:url

```yaml
regex_id: 76526fbaebf322b37602d48da8c1ae6b
schema_version: "1"
kind: intent_mismatch
corpus: gadievron-raptor
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/cross_function_verify.py:56:9"
```

### Pattern

`unsaniti[sz]ed\s+(?:input|data|header|value|filename)|(?:user|attacker|external)[\w\s-]*(?:control|suppli|provid)\w*\s+(?:data|input|value).*(?:sink|output|render|inject|interpolat)|(?:host|header|query|path|url)\s+(?:value\s+)?(?:directly|without)|taint(?:ed)?\s+.*(?:sink|output|render)|unsaniti[sz]ed\s+\w+\s+.*(?:path|directory|travers)|(?:\.\./|path\s+travers|directory\s+travers)`

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

## usage_mismatch:768878882932c508bee370924dfb625e:search

```yaml
regex_id: 768878882932c508bee370924dfb625e
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/spec_inference.py:48:5"
```

### Pattern

`^sanitize_|^clean_|^escape_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:76f175177ebab212ebc4e76fd064212e:search

```yaml
regex_id: 76f175177ebab212ebc4e76fd064212e
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:621:5"
```

### Pattern

`^(connect)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:79b15f6522250085b91fd74918e616a2:search

```yaml
regex_id: 79b15f6522250085b91fd74918e616a2
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/spec_inference.py:53:5"
```

### Pattern

`^alloc(?:ate)?_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7a903e7385bf6f9d05cfc633458b6383:search

```yaml
regex_id: 7a903e7385bf6f9d05cfc633458b6383
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/dark_verify/_execute.py:48:17"
```

### Pattern

`^[a-zA-Z_][a-zA-Z0-9_]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7b1b76a7f882732074fc7ae6b1186d13:search

```yaml
regex_id: 7b1b76a7f882732074fc7ae6b1186d13
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/cve/cwe.py:27:10"
```

### Pattern

`^\s*cwe[-_\s]?(\d+)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7bc66d415f8118170da478667acda03e:search

```yaml
regex_id: 7bc66d415f8118170da478667acda03e
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/exploit_feasibility/analyzer.py:3381:24"
```

### Pattern

`^([0-9a-f]+)\s+\w+\s+execve(?:@@|\s|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7cb93d6395e69f233543353a87cdcfae:search

```yaml
regex_id: 7cb93d6395e69f233543353a87cdcfae
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/web/fuzzer.py:307:24"
```

### Pattern

`^root:[^:]*:\d+:\d+:|/bin/(?:ba)?sh\b|uid=\d+\(`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7d01b77ed5b1820de6b3a471159fdee7:search

```yaml
regex_id: 7d01b77ed5b1820de6b3a471159fdee7
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/build_membership.py:93:14"
```

### Pattern

`^\s*package\s+\w+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7d1bab0904a76aa9e8222baba022c345:search

```yaml
regex_id: 7d1bab0904a76aa9e8222baba022c345
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/evidence/__init__.py:153:17"
```

### Pattern

`^[A-Za-z_][A-Za-z0-9_]*((?:\.|::|/)[A-Za-z_][A-Za-z0-9_]*)*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7d8273c934e6c3d88cc8ec2c814b72b7:search

```yaml
regex_id: 7d8273c934e6c3d88cc8ec2c814b72b7
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/source_intel/analyze.py:1688:22"
```

### Pattern

`^\s*(?:[A-Za-z_][A-Za-z0-9_]*[\s*&]+)+[A-Za-z_][A-Za-z0-9_]*\s*\(`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7dd9b835e9402e155b6ab0575735b274:search

```yaml
regex_id: 7dd9b835e9402e155b6ab0575735b274
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:410:18"
```

### Pattern

`^(handle|process|parse|render|validate|check|verify|do|on|emit|send|recv|read|write|get|set|create|delete|update|insert|remove|add|init|setup|teardown|cleanup|reset|start|stop|open|close|encode|decode|encrypt|decrypt|compress|decompress|serialize|deserialize|marshal|unmarshal|pack|unpack|load|save|store|fetch|put|push|pull|pop|register|unregister|subscribe|unsubscribe|connect|disconnect|bind|unbind|attach|detach|enable|disable|show|hide|lock|unlock|alloc|free|enter|exit|begin|end|run|exec|dispatch|route)_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7e501ed6287fcd0bb90cb6eba0d69070:search

```yaml
regex_id: 7e501ed6287fcd0bb90cb6eba0d69070
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/fail_open_detector.py:119:24"
```

### Pattern

`^\s*return\s+\w+\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7ec5cd66578a12c0dbf2868e4111b761:search

```yaml
regex_id: 7ec5cd66578a12c0dbf2868e4111b761
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/semgrep/nosemgrep.py:35:16"
```

### Pattern

`(?://|[#]|/\*)       # comment opener
        \s*nosemgrep         # keyword
        (?::[ \t]*           # optional colon + rule list
          ([\w.:,/-]+)       # group 1: comma-separated rule IDs
        )?
        (?:[ \t]+(.+?))?     # group 2: justification text
        (?:\s*\*/)?          # optional block-comment closer
        \s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7ef0f24927d48f40b06e8985245dbddf:search

```yaml
regex_id: 7ef0f24927d48f40b06e8985245dbddf
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/supply_chain/gha_drift.py:53:10"
```

### Pattern

`^[a-f0-9]{40}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7f1525a21f4b3bbf37d987754996844c:search

```yaml
regex_id: 7f1525a21f4b3bbf37d987754996844c
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/orchestration/flow_trace_ast_view.py:87:17"
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

## usage_mismatch:7f9c5a6a6db2a4724e8eb1aac7c924c8:search

```yaml
regex_id: 7f9c5a6a6db2a4724e8eb1aac7c924c8
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/gomod.py:54:21"
```

### Pattern

`^v\d+\.\d+\.\d+(?:-[\w.]+)?-\d{14}-[0-9a-f]{12}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:805236b864b545fa5ec0f27b0f83c98d:search

```yaml
regex_id: 805236b864b545fa5ec0f27b0f83c98d
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/typestate.py:110:38"
```

### Pattern

`^(\w+?)_release$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:80b7016d58dd066bcedfcca8346ce54a:search

```yaml
regex_id: 80b7016d58dd066bcedfcca8346ce54a
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/annotations/storage.py:91:22"
```

### Pattern

`^##[ \t]+(.+?)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8123b07721f8dc840d0f5877babca756:search

```yaml
regex_id: 8123b07721f8dc840d0f5877babca756
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/typestate.py:112:36"
```

### Pattern

`^(\w+?)_stop$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:81ea3547594deb290a22314f7d1da987:search

```yaml
regex_id: 81ea3547594deb290a22314f7d1da987
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/dead_scope.py:548:16"
```

### Pattern

`^(\s*)(?:else|elsif)\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:838a3e15007d4379e9d55bb5073927a8:search

```yaml
regex_id: 838a3e15007d4379e9d55bb5073927a8
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/binary_oracle_corpora/zlib.py:155:14"
```

### Pattern

`^Function '([^']+)'`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:839c63e45e1c883e4855939f3b2ab41d:search

```yaml
regex_id: 839c63e45e1c883e4855939f3b2ab41d
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:613:11"
```

### Pattern

`return\s+self::\$?\w+\s*;$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:83a501bbdb1e9ae72fb36c44d1800c56:search

```yaml
regex_id: 83a501bbdb1e9ae72fb36c44d1800c56
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/dark_verify/_execute.py:73:11"
```

### Pattern

`^[a-zA-Z_][a-zA-Z0-9_*&\[\]<>, .:]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:84043808de4becba087803d15fcf33c4:match

```yaml
regex_id: 84043808de4becba087803d15fcf33c4
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/inline_installs/_managers.py:179:8"
```

### Pattern

`^(==|>=|<=|~=|>|<|!=)\s*(\S+)$`

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

## usage_mismatch:8497ed3434f674711dbf50cd34520516:search

```yaml
regex_id: 8497ed3434f674711dbf50cd34520516
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/wheel_compat/wheel_tags.py:81:16"
```

### Pattern

`^musllinux_(\d+)_(\d+)_(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:84b5ff4b3b56167053b8da6c82b3f9b4:match

```yaml
regex_id: 84b5ff4b3b56167053b8da6c82b3f9b4
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/exploit_feasibility/analyzer.py:3580:24"
```

### Pattern

`^(0x[0-9a-f]+)\s*:\s*(.+)$`

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

## usage_mismatch:84d56c4326cc65d3bdc9cefacb6710b4:search

```yaml
regex_id: 84d56c4326cc65d3bdc9cefacb6710b4
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/checker_synthesis/synthesise.py:99:19"
```

### Pattern

`^\s*when\s*!=\s*(?:if|assert|while|for|switch)\s*\(.*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:85fd85c2420ab35985d844f0f9361338:search

```yaml
regex_id: 85fd85c2420ab35985d844f0f9361338
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/cmake_fetchcontent.py:71:13"
```

### Pattern

`https?://github\.com/(?P<owner>[A-Za-z0-9._-]+)/(?P<repo>[A-Za-z0-9._-]+?)(?:\.git)?/?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:869e5c3fb853d9bf8482aab419a4d9fd:search

```yaml
regex_id: 869e5c3fb853d9bf8482aab419a4d9fd
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/llm_analysis/dataflow_query_builder.py:117:24"
```

### Pattern

`^codeql/([A-Za-z0-9-]+)-queries$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:874d3001f87b2d4f5d4665227760875b:search

```yaml
regex_id: 874d3001f87b2d4f5d4665227760875b
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/extractors.py:993:17"
```

### Pattern

`^(?P<local>local\s+)?function\s+(?P<name>[\w.]+(?::[\w]+)?)\s*\((?P<params>[^)]*)\)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:88402aa7485526b83a1ad1d42f25da40:search

```yaml
regex_id: 88402aa7485526b83a1ad1d42f25da40
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/bump/orchestrator.py:1197:11"
```

### Pattern

`^\s*(?:-\s+)?uses:\s*(?P<repo>[\w.-]+/[\w.-]+)(?P<subpath>(?:/[\w./-]+)?)@(?P<ref>[^\s#]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8a0c387a6d880a08d6906dc0d3808f04:search

```yaml
regex_id: 8a0c387a6d880a08d6906dc0d3808f04
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/sibling_analysis.py:251:4"
```

### Pattern

`^(scan|detect|identify)_(\w+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8a2d4e9ee38ef5066658d9ac55c88f41:search

```yaml
regex_id: 8a2d4e9ee38ef5066658d9ac55c88f41
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:616:43"
```

### Pattern

`^(release)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8a44c605e5a1e6785f51660445b9e03c:search

```yaml
regex_id: 8a44c605e5a1e6785f51660445b9e03c
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/_util.py:15:16"
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

## usage_mismatch:8bce1b6a8533701659ab9f1c4efa889d:search

```yaml
regex_id: 8bce1b6a8533701659ab9f1c4efa889d
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/inline_installs/_managers.py:487:15"
```

### Pattern

`^[A-Za-z0-9][A-Za-z0-9._\-]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8bdbf5a0f4bd1e5612fe67f934674b4f:search

```yaml
regex_id: 8bdbf5a0f4bd1e5612fe67f934674b4f
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/sibling_analysis.py:408:5"
```

### Pattern

`^(\w+?)_(?:sanitize|sanitise|escape|clean)_input$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8cdcd12a580f58c7cec800dbc685bef0:search

```yaml
regex_id: 8cdcd12a580f58c7cec800dbc685bef0
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:1420:11"
```

### Pattern

`\b(?:eval|assert)\s*\(\s*\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8d0a7aa18c90acfa5bb9f0107e2c1891:search

```yaml
regex_id: 8d0a7aa18c90acfa5bb9f0107e2c1891
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/oci/image_ref.py:37:13"
```

### Pattern

`^(?P<algo>[A-Za-z][A-Za-z0-9]*(?:[-_+.][A-Za-z0-9]+)*):(?P<hex>[A-Fa-f0-9]{32,})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8e6ffcc9983693ab121b2179817d2940:search

```yaml
regex_id: 8e6ffcc9983693ab121b2179817d2940
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/wheel_compat/wheel_tags.py:82:13"
```

### Pattern

`^macosx_(\d+)_(\d+)_(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8f5ee56d7a4fd58ba64c4f6017bb4b4c:search

```yaml
regex_id: 8f5ee56d7a4fd58ba64c4f6017bb4b4c
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/autonomous/exploit_validator.py:353:24"
```

### Pattern

`: error: (.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:90a6f2fa3658203b8555f91c5bead9e9:search

```yaml
regex_id: 90a6f2fa3658203b8555f91c5bead9e9
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/inline_installs/_managers.py:300:16"
```

### Pattern

`^([A-Za-z0-9][A-Za-z0-9._\-]*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:90e2d00fc19e0f1e0a011d9d465f5ff1:search

```yaml
regex_id: 90e2d00fc19e0f1e0a011d9d465f5ff1
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:582:11"
```

### Pattern

`return\s+\d+\s*;$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:91042355360b7e52a639499f97be9792:search

```yaml
regex_id: 91042355360b7e52a639499f97be9792
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/spec_inference.py:47:5"
```

### Pattern

`^(?:validate|verify|check)_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:91635fd943d8c51d880b2e7994d7f333:search

```yaml
regex_id: 91635fd943d8c51d880b2e7994d7f333
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/build_membership.py:92:24"
```

### Pattern

`^//\s*\+build\s+(.+?)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:9196c3a8739e9f27e8e24ebbcafa619a:url

```yaml
regex_id: 9196c3a8739e9f27e8e24ebbcafa619a
schema_version: "1"
kind: intent_mismatch
corpus: gadievron-raptor
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/transform_sequence.py:275:19"
```

### Pattern

`url.*decode|unquote|percent.*decode|decodeURI|urllib.*unquote|url\.QueryUnescape|url\.PathUnescape`

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

## usage_mismatch:922552d5d4f9bd49a1a13a17e41aaff6:search

```yaml
regex_id: 922552d5d4f9bd49a1a13a17e41aaff6
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:617:39"
```

### Pattern

`^(unref)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9284229da9ebdf536db248a9025b2a7e:search

```yaml
regex_id: 9284229da9ebdf536db248a9025b2a7e
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/exploit_feasibility/smt_onegadget.py:224:8"
```

### Pattern

`\s+is\s+writable\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:92bd20543389de534c4531fa93a518ff:search

```yaml
regex_id: 92bd20543389de534c4531fa93a518ff
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/platform_matrix/matrix.py:498:22"
```

### Pattern

`^\s*-?\s*uses:\s*docker/build-push-action@[^\s\n]+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:93fd2cce158f2c3982279d8b2d8db8e3:search

```yaml
regex_id: 93fd2cce158f2c3982279d8b2d8db8e3
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/sibling_analysis.py:250:4"
```

### Pattern

`^(handle|process|dispatch)_(\w+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:94a13f97c07a5ec8a9fc13cf16292dd4:search

```yaml
regex_id: 94a13f97c07a5ec8a9fc13cf16292dd4
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/wheel_compat/wheel_tags.py:84:17"
```

### Pattern

`^linux_(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:94c9a0685c7db15e576ae093318199ee:search

```yaml
regex_id: 94c9a0685c7db15e576ae093318199ee
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/inline_installs/_arg_version_pins.py:200:14"
```

### Pattern

`^v?\d+(?:\.\d+){0,3}(?:[-+.]?[A-Za-z][\w.]*)?(?:[-+][\w.]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:95ba7db00c30b1a3c2e92f836709982a:search

```yaml
regex_id: 95ba7db00c30b1a3c2e92f836709982a
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/cve_diff/cve_diff/diffing/extract_via_patch_url.py:181:15"
```

### Pattern

`^diff --git a/\S+? b/(\S+)\r?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:95e793ba94383d71377f6ebe70c20403:search

```yaml
regex_id: 95e793ba94383d71377f6ebe70c20403
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/reachability.py:128:21"
```

### Pattern

`(^|/)(tests?/.*|test_[^/]+\.py|[^/]+_test\.py|conftest\.py)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:97ce23046f92750710fdfe52c611df16:search

```yaml
regex_id: 97ce23046f92750710fdfe52c611df16
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:119:18"
```

### Pattern

`^JOERN_PEERS:([^|]+)\|([^|]*)\|(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:983515794c7979bd83a1e61fc425f927:search

```yaml
regex_id: 983515794c7979bd83a1e61fc425f927
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:613:5"
```

### Pattern

`^(alloc)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9bae78f115f04c64685656379c0948d7:match

```yaml
regex_id: 9bae78f115f04c64685656379c0948d7
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/gomod.py:161:12"
```

### Pattern

`^require\s+(\S+)\s+(\S+)\s*(//.*)?$`

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

## usage_mismatch:9e13daefd708b3c4889a176a1e39e3b6:search

```yaml
regex_id: 9e13daefd708b3c4889a176a1e39e3b6
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/reachability/nodejs.py:60:16"
```

### Pattern

`.*\.(test|spec)\.[mc]?[jt]sx?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9e6985d442ab316d26b26f9423aaa9b6:search

```yaml
regex_id: 9e6985d442ab316d26b26f9423aaa9b6
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/typestate.py:109:34"
```

### Pattern

`^(\w+?)_(?:free|del|delete)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9ef56ca29f0cb6ccec39eafbf846a00a:search

```yaml
regex_id: 9ef56ca29f0cb6ccec39eafbf846a00a
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/macro_resolve.py:21:16"
```

### Pattern

`^\s*#\s*define\s+(\w+)(\([^)]*\))?\s+(.+?)(?:\s*\\)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9f9453f0f8b8f3707b0793f21b2ae8cc:search

```yaml
regex_id: 9f9453f0f8b8f3707b0793f21b2ae8cc
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/platform_matrix/matrix.py:502:25"
```

### Pattern

`^\s*-\s*(?:uses|run|name):`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9fe12b4252a59abc8b0354478bcd1321:search

```yaml
regex_id: 9fe12b4252a59abc8b0354478bcd1321
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/lifecycle_field_discovery.py:39:21"
```

### Pattern

`^\s+self\.(\w+)\s*=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a01c9b67ddba7e8485e2bc6131c4541c:search

```yaml
regex_id: a01c9b67ddba7e8485e2bc6131c4541c
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/dataflow/structural_validator.py:279:19"
```

### Pattern

`^\s*(?:if|elif|else\s+if|while|for)\s*[\(]?\s*(.+?)\s*[\)]?\s*[:{]?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a0aac2c2b241ca15a7bb85645c845fbb:search

```yaml
regex_id: a0aac2c2b241ca15a7bb85645c845fbb
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/spec_inference.py:64:5"
```

### Pattern

`^recv_|^receive_|^consume_|^subscribe_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a0ae6fc2e7f88400316431102f548998:search

```yaml
regex_id: a0ae6fc2e7f88400316431102f548998
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:1442:11"
```

### Pattern

`\b(?:include|include_once|require|require_once)\s*\(\s*\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a12d57c9500e291eca8cf4a6107a0074:search

```yaml
regex_id: a12d57c9500e291eca8cf4a6107a0074
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:626:5"
```

### Pattern

`^(start)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a15379fb5b5f23b922f1ffcd6fa7536d:search

```yaml
regex_id: a15379fb5b5f23b922f1ffcd6fa7536d
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:610:44"
```

### Pattern

`^(decompress)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a15d4d754bf1b77d7b52e8047b9ebde2:match

```yaml
regex_id: a15d4d754bf1b77d7b52e8047b9ebde2
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/reachability_gates.py:320:11"
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

## usage_mismatch:a16e2e97410b6b239237640a9108568f:match

```yaml
regex_id: a16e2e97410b6b239237640a9108568f
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/gomod.py:205:12"
```

### Pattern

`^replace\s+(\S+)(?:\s+\S+)?\s*=>\s*(\S+)(?:\s+(\S+))?\s*$`

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

## usage_mismatch:a1b96667d3b0de23f057f52a5c10efa1:search

```yaml
regex_id: a1b96667d3b0de23f057f52a5c10efa1
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/extractors.py:998:18"
```

### Pattern

`^(?P<local>local\s+)?(?P<name>[\w.]+)\s*=\s*function\s*\((?P<params>[^)]*)\)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a303e0441596b07b913dd385d40d0062:search

```yaml
regex_id: a303e0441596b07b913dd385d40d0062
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:622:42"
```

### Pattern

`^(detach)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a3a16c7f097f563ff34990bdf26f129e:search

```yaml
regex_id: a3a16c7f097f563ff34990bdf26f129e
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/typestate.py:116:34"
```

### Pattern

`^(\w+?)_put$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a507e83dd8da2f7197245cf1cedcd84b:search

```yaml
regex_id: a507e83dd8da2f7197245cf1cedcd84b
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/supply_chain/git_drift.py:37:15"
```

### Pattern

`^(?:v?\d+(?:\.\d+)*(?:[-+][\w.]+)?|release-?\d|\d{8})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a58385d5ceebab95bc6f1e30f863c708:search

```yaml
regex_id: a58385d5ceebab95bc6f1e30f863c708
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:610:5"
```

### Pattern

`^(compress)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a636ee6a80ac4085e5f59e9ef5250dff:search

```yaml
regex_id: a636ee6a80ac4085e5f59e9ef5250dff
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/source_intel/adapter.py:1645:18"
```

### Pattern

`^\s*(?:[A-Za-z_][A-Za-z_0-9*\s]*?\s+\*?\s*)?(?P<name>[A-Za-z_][A-Za-z_0-9]*)\s*\(`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a64b41080f4cc2e2383919308d0a2b37:search

```yaml
regex_id: a64b41080f4cc2e2383919308d0a2b37
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/exploit_feasibility/cache.py:428:23"
```

### Pattern

`^\s*([0-9a-f]+)\s+/bin/sh\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a6e00e7041d4aecfcd60a592d06f3acc:search

```yaml
regex_id: a6e00e7041d4aecfcd60a592d06f3acc
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/typestate.py:106:37"
```

### Pattern

`^(\w+?)_(?:delete|destroy|free)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a72698782e1acaebec56ff7283a9c504:search

```yaml
regex_id: a72698782e1acaebec56ff7283a9c504
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/uninit_detector.py:162:15"
```

### Pattern

`^\s*(?:struct|union)\s+(\w+)\s+(\w+)\s*;`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a728155ba0783d39c30f56a3d6e960eb:search

```yaml
regex_id: a728155ba0783d39c30f56a3d6e960eb
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/__init__.py:70:20"
```

### Pattern

`sca\.parsers\.[\w_]+:\s+(?P<kind>\w+(?:\s\w+)?)\s+parse failed for\s+(?P<path>.+?):\s+(?P<reason>.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a73e61eeb6f283a2b97f80b183751257:search

```yaml
regex_id: a73e61eeb6f283a2b97f80b183751257
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/dead_scope.py:549:13"
```

### Pattern

`^(\s*)end\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a75d670b4cc74f3a894c6e3db800d4a3:search

```yaml
regex_id: a75d670b4cc74f3a894c6e3db800d4a3
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/smt_solver/path_feasibility.py:260:10"
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

## usage_mismatch:a77d0f3a4491d772828c628665e3cb10:match

```yaml
regex_id: a77d0f3a4491d772828c628665e3cb10
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/gemfile.py:157:12"
```

### Pattern

`^    (\S+)\s+\(([^)]+)\)\s*$`

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

## usage_mismatch:aa0da7ff4bc534b85094210280b0b547:search

```yaml
regex_id: aa0da7ff4bc534b85094210280b0b547
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/rewriters/gha_uses.py:158:10"
```

### Pattern

`^[a-f0-9]{40}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:aacd80656ab11c96333aa7959d701ace:search

```yaml
regex_id: aacd80656ab11c96333aa7959d701ace
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/binary_oracle.py:514:13"
```

### Pattern

`^\s*<(\d+)><([0-9a-fA-F]+)>:\s+Abbrev Number:\s*\d+\s*\((\w+)\)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ab426a44fa35169853065a3aea992259:search

```yaml
regex_id: ab426a44fa35169853065a3aea992259
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/typestate.py:107:35"
```

### Pattern

`^(\w+?)_close$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:abf611e4f4a66284d3c76f53e851ec62:match

```yaml
regex_id: abf611e4f4a66284d3c76f53e851ec62
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/reachability_gates.py:247:11"
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

## usage_mismatch:acf9f7bf399dedca831ec1525a337696:search

```yaml
regex_id: acf9f7bf399dedca831ec1525a337696
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/binary_oracle.py:417:17"
```

### Pattern

`^<([\w:]+)>::(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ada33afedb1181e2ece5db8f60d6aeda:search

```yaml
regex_id: ada33afedb1181e2ece5db8f60d6aeda
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:607:5"
```

### Pattern

`^(serialize)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ae4244c1d38258777ef41a0286858e73:search

```yaml
regex_id: ae4244c1d38258777ef41a0286858e73
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/value_space_checker.py:81:17"
```

### Pattern

`^(?:ecosystem|status|state|kind|category|type|mode|level|severity|phase|stage|role|action|signal|crash_type|final_status|result|verdict|classification|method|event_type|protocol|encoding|operation|platform|direction|priority|strategy|transport|scheme|backend)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ae585af06820a21d219c1a96b76d5801:search

```yaml
regex_id: ae585af06820a21d219c1a96b76d5801
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/orchestrator.py:7446:12"
```

### Pattern

`^\s*sym(?:\.imp)?\.(?:[\w.]+\.dll_|_)?(\w+)\s*\(.*?\)\s*(?://.*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:aead0e0e370e0cc7d01daad43952e1b1:search

```yaml
regex_id: aead0e0e370e0cc7d01daad43952e1b1
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/sandbox/seatbelt_audit.py:105:15"
```

### Pattern

`Sandbox:\s+(\S+)\((\d+)\)\s+(allow|deny)\s+(\S+)\s+(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:afbaa009db75890a0479c7a07c94ea7b:search

```yaml
regex_id: afbaa009db75890a0479c7a07c94ea7b
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:607:45"
```

### Pattern

`^(deserialize)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b0560a459298d7938c9cb60c28334ca7:match

```yaml
regex_id: b0560a459298d7938c9cb60c28334ca7
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/gomod.py:285:7"
```

### Pattern

`^v\d+(\.\d+){0,2}(?:-[\w.]+)?$`

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

## usage_mismatch:b0c78f2e7523c0950d4bca200fb9e288:match

```yaml
regex_id: b0c78f2e7523c0950d4bca200fb9e288
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/nuget.py:653:7"
```

### Pattern

`^\d[\w.\-+]*$`

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

## usage_mismatch:b14121469bb2e72fc91f27f4a712802a:search

```yaml
regex_id: b14121469bb2e72fc91f27f4a712802a
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:2010:11"
```

### Pattern

`\bDBI\b.*\bdo\s*\(|\bprepare\s*\(.*\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b1e61247446141169527ccd4cd437128:match

```yaml
regex_id: b1e61247446141169527ccd4cd437128
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/dark_verify/_execute.py:115:18"
```

### Pattern

`^[a-zA-Z0-9_./-]+$`

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

## usage_mismatch:b22842d3f34bbf7d2563a364b32d2510:search

```yaml
regex_id: b22842d3f34bbf7d2563a364b32d2510
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:611:5"
```

### Pattern

`^(sanitize_input)_?(.+)?`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b30338ccd95ac7eafe555982712103f7:search

```yaml
regex_id: b30338ccd95ac7eafe555982712103f7
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/exploit_feasibility/analyzer.py:3391:24"
```

### Pattern

`^([0-9a-f]+)\s+\w+\s+__free_hook(?:@@|\s|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b35e7569efa92def6925e08bf83e11f7:match

```yaml
regex_id: b35e7569efa92def6925e08bf83e11f7
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/gomod.py:180:21"
```

### Pattern

`^(\S+)\s+(\S+)\s*(//.*)?$`

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

## usage_mismatch:b442135bf145cc11ef384063ba10f6e3:search

```yaml
regex_id: b442135bf145cc11ef384063ba10f6e3
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/typestate.py:113:5"
```

### Pattern

`^(\w+?)_connect$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b4ea23c843e0cce6cdccb6245646a887:search

```yaml
regex_id: b4ea23c843e0cce6cdccb6245646a887
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/reachability/nuget.py:40:14"
```

### Pattern

`^\s*open\s+([A-Za-z_][A-Za-z0-9_.]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b5019c0a4eaf2c77c50fa92399326bd7:match

```yaml
regex_id: b5019c0a4eaf2c77c50fa92399326bd7
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/reachability_gates.py:283:11"
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

## usage_mismatch:b5f0bf299241e4bcb48c6d22f339b32f:search

```yaml
regex_id: b5f0bf299241e4bcb48c6d22f339b32f
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/build_membership.py:91:17"
```

### Pattern

`^//go:build\s+(.+?)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b75421cc0398310d41e40ff058ca979b:search

```yaml
regex_id: b75421cc0398310d41e40ff058ca979b
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/block_sibling_analysis.py:308:18"
```

### Pattern

`^(\s*)(?:case\s+(.+?):|when\s+(.+?)\s|default\s*:)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b7a99c0d1454d118be6dabf8da1a7fba:search

```yaml
regex_id: b7a99c0d1454d118be6dabf8da1a7fba
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/dead_scope.py:545:14"
```

### Pattern

`^(\s*)(?:if\s+(?:false|nil)|unless\s+true|while\s+false|until\s+true)\s*(?:then\b.*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b7c9a5547a7c469d6f4ecb27e9de8388:search

```yaml
regex_id: b7c9a5547a7c469d6f4ecb27e9de8388
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/autonomous/poc_source_scan.py:80:5"
```

### Pattern

`^[ \t]*#[ \t]*pragma[ \t]+GCC[ \t]+dependency[ \t]+"([^"]+)"`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b7e583d31240e95ddff25d083c4e47a0:search

```yaml
regex_id: b7e583d31240e95ddff25d083c4e47a0
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/exploit_feasibility/context.py:1004:28"
```

### Pattern

`^\s*([0-9a-f]+)\s+/bin/sh$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b807493d17ba0a4682750770b6c08a82:search

```yaml
regex_id: b807493d17ba0a4682750770b6c08a82
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/sibling_analysis.py:405:5"
```

### Pattern

`^(\w+?)_(?:decode|decrypt|deserialize|unmarshal|unpack|decompress)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b8559b0650a037605600809a31e5e6d9:search

```yaml
regex_id: b8559b0650a037605600809a31e5e6d9
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/sln.py:49:19"
```

### Pattern

`^Project\("\{[^}]+\}"\)\s*=\s*"[^"]*"\s*,\s*"(?P<path>[^"]+)"\s*,\s*"\{[^}]+\}"\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b8e2dfc0a8a39c95e2ecac2ec8c5c54a:search

```yaml
regex_id: b8e2dfc0a8a39c95e2ecac2ec8c5c54a
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/binary_oracle_corpora/zstd_holdout.py:194:17"
```

### Pattern

`^Lines executed:([\d.]+)% of \d+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b944ee5a57d353864a52f838564e9353:search

```yaml
regex_id: b944ee5a57d353864a52f838564e9353
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:584:11"
```

### Pattern

`return\s+NULL\s*;$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bbf62a8a0c57553c6fc0396aff330e1f:search

```yaml
regex_id: bbf62a8a0c57553c6fc0396aff330e1f
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/json/tolerant.py:117:17"
```

### Pattern

`^\s*(?:```|~~~)\s*(?P<lang>[a-zA-Z0-9_+-]*)\s*\n(?P<body>[\s\S]*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bcfd834122274c2d3a234d448baea0a1:search

```yaml
regex_id: bcfd834122274c2d3a234d448baea0a1
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/calibration/_apply_refit.py:44:20"
```

### Pattern

`^(?P<indent>\s*)(?P<name>_[A-Z][A-Z0-9_]*)\s*=\s*(?P<value>[+-]?\d+(?:\.\d+)?)(?P<rest>.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bd41c3c22b5634495e28f91b96c7a29a:search

```yaml
regex_id: bd41c3c22b5634495e28f91b96c7a29a
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/source_intel/adapter.py:1218:25"
```

### Pattern

`//.*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bdebe7b9175890daf6fb4866111720d0:search

```yaml
regex_id: bdebe7b9175890daf6fb4866111720d0
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:2052:11"
```

### Pattern

`\bchmod\s*\(?\s*0?777|\bchmod\b.*\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:be221dc119b4a5c4935ee84ff1fde3a1:search

```yaml
regex_id: be221dc119b4a5c4935ee84ff1fde3a1
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:589:12"
```

### Pattern

`return\s+(\w+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bebe93ad2afc91435ad06d044294943c:search

```yaml
regex_id: bebe93ad2afc91435ad06d044294943c
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/transform_sequence.py:541:18"
```

### Pattern

`^\s*(?:(?:static|inline|void|int|char|unsigned|const|auto|func|function|export|async|public|private|protected|internal|override|virtual|abstract|final|synchronized|fn|def)\s+)*(?:\([^)]*\)\s+)?(?:\w+\s+)*(\w+)\s*\(`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bec4a19b3d6f1776ebef73e34e1f4d6a:search

```yaml
regex_id: bec4a19b3d6f1776ebef73e34e1f4d6a
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/supply_chain/git_drift.py:35:10"
```

### Pattern

`^[a-f0-9]{40}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bee9ba84ffcaacdb17727df16931672d:search

```yaml
regex_id: bee9ba84ffcaacdb17727df16931672d
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/autonomous/poc_source_scan.py:76:5"
```

### Pattern

`^[ \t]*#[ \t]*include[ \t]*[<"]([^>"]+)[>"]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bf97e828d35d93a2257dacba31067b70:search

```yaml
regex_id: bf97e828d35d93a2257dacba31067b70
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/supply_chain/orphan_commit_dep.py:91:19"
```

### Pattern

`^github:(?P<owner>[\w.\-]+)/(?P<repo>[\w.\-]+)(?:#(?P<ref>[\w./\-]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c0aacba6500ae828e5646d9f547a0073:search

```yaml
regex_id: c0aacba6500ae828e5646d9f547a0073
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:618:39"
```

### Pattern

`^(dec)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c1fffd2134bc07336760e4abaa7f5715:search

```yaml
regex_id: c1fffd2134bc07336760e4abaa7f5715
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/sibling_analysis.py:404:5"
```

### Pattern

`^(\w+?)_(?:encode|encrypt|serialize|marshal|pack|compress)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c27cdfd53b8984a886b67a3d116525c3:match

```yaml
regex_id: c27cdfd53b8984a886b67a3d116525c3
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/conan.py:276:30"
```

### Pattern

`^[A-Za-z0-9._\-+]+$`

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

## usage_mismatch:c2cb407292f93dc2eb7adc6a53cd3ecd:search

```yaml
regex_id: c2cb407292f93dc2eb7adc6a53cd3ecd
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:612:5"
```

### Pattern

`^(lock)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c35e9b6a29c5f72404208ecbbfd69f12:search

```yaml
regex_id: c35e9b6a29c5f72404208ecbbfd69f12
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/binary_oracle_corpora/libsodium.py:169:17"
```

### Pattern

`^Lines executed:([\d.]+)% of \d+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c36839f6775d82cdafae61bf3aa9c41d:search

```yaml
regex_id: c36839f6775d82cdafae61bf3aa9c41d
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/exploit_feasibility/analyzer.py:3386:24"
```

### Pattern

`^([0-9a-f]+)\s+\w+\s+__malloc_hook(?:@@|\s|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c535143ebd30d69fc01266b979589894:search

```yaml
regex_id: c535143ebd30d69fc01266b979589894
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/fail_open_detector.py:338:15"
```

### Pattern

`^\s*return\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c577de58cd141ace2fad45fd1413118b:search

```yaml
regex_id: c577de58cd141ace2fad45fd1413118b
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/spec_inference.py:52:5"
```

### Pattern

`^free_|^destroy_|^cleanup_|^close_|^release_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c62d3d606fe930dab8213eecb67f04c9:search

```yaml
regex_id: c62d3d606fe930dab8213eecb67f04c9
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/wheel_compat/wheel_tags.py:83:10"
```

### Pattern

`^(win_amd64|win32)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c689411c0dc945a4519835dea1c1b7ad:search

```yaml
regex_id: c689411c0dc945a4519835dea1c1b7ad
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/llm_analysis/agent.py:1894:21"
```

### Pattern

`^```(?P<lang>[a-zA-Z0-9_+-]*)\s*\n(?P<body>.*?)^```\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c6cba545e0dca678d04f40b297aafa7c:search

```yaml
regex_id: c6cba545e0dca678d04f40b297aafa7c
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/reachability/gomod.py:27:20"
```

### Pattern

`^\s*import\s+(?:[A-Za-z_][A-Za-z0-9_]*\s+)?"([^"]+)"`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c7aa2c0692ac1415fb34f2d6094ed20f:search

```yaml
regex_id: c7aa2c0692ac1415fb34f2d6094ed20f
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:623:16"
```

### Pattern

`return\s+(\w+)\s*;$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c81b4bc1ad1401db007ae7f65b6b256a:search

```yaml
regex_id: c81b4bc1ad1401db007ae7f65b6b256a
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/platform_matrix/matrix.py:454:19"
```

### Pattern

`^\s*(?:os|platform):\s*\[\s*([^\]]+)\s*\]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c8a84ed0a16747e3a6363d76bb2edcd4:search

```yaml
regex_id: c8a84ed0a16747e3a6363d76bb2edcd4
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/binary_oracle.py:534:23"
```

### Pattern

`\(in(?:direct|dexed) string[^)]*\):\s*(.+?)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c8c1f35ed33125e55239429adc4ddc75:search

```yaml
regex_id: c8c1f35ed33125e55239429adc4ddc75
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/typestate.py:107:5"
```

### Pattern

`^(\w+?)_open$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c91a5b1566508ea6d7df95e53d69399a:search

```yaml
regex_id: c91a5b1566508ea6d7df95e53d69399a
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:629:11"
```

### Pattern

`return\s+this\.\w+\s*;?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c9c9c74154b63b2276257bf75911d015:match

```yaml
regex_id: c9c9c74154b63b2276257bf75911d015
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/gomod.py:168:11"
```

### Pattern

`^require\s*\(\s*$`

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

## usage_mismatch:caa95d2220ff4c0f3a7257eda4cadcd1:search

```yaml
regex_id: caa95d2220ff4c0f3a7257eda4cadcd1
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/condition_smt.py:3946:24"
```

### Pattern

`^\s+(?:struct\s+\w+\s+\*|[\w]+\s+\*?)\w+\s*=\s*(\w+)->\w+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cadc374fdb33738d508f17bd56ba99fc:search

```yaml
regex_id: cadc374fdb33738d508f17bd56ba99fc
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:1990:11"
```

### Pattern

``[^`]*\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cb3de186ff9ec4550fc996b08685715d:search

```yaml
regex_id: cb3de186ff9ec4550fc996b08685715d
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/web/fuzzer.py:313:24"
```

### Pattern

`^root:x:\d+:\d+:|\[boot loader\]|\[extensions\].*\[fonts\]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cc31ee8f72637e6095cd7e56c3d57e72:search

```yaml
regex_id: cc31ee8f72637e6095cd7e56c3d57e72
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/source_intel/adapter.py:590:19"
```

### Pattern

`^\s*(?:[A-Za-z_][A-Za-z0-9_*\s]*\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ccc551c24dd69c300c213de04bff03e7:search

```yaml
regex_id: ccc551c24dd69c300c213de04bff03e7
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/test_discovery.py:20:22"
```

### Pattern

`(?:test_\w+|_test)\.\w+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cd95b595b9fda62d3bbf76fffb3234b6:search

```yaml
regex_id: cd95b595b9fda62d3bbf76fffb3234b6
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/sibling_analysis.py:248:4"
```

### Pattern

`^(sanitize|sanitise|escape|clean|scrub)_(\w+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cdebc1a4dff925995fba42deae66df54:search

```yaml
regex_id: cdebc1a4dff925995fba42deae66df54
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/module_load_abort.py:504:15"
```

### Pattern

`\bend\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ce735f2eafa345080bd199f43aca4067:search

```yaml
regex_id: ce735f2eafa345080bd199f43aca4067
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/llm/multi_model/prompt_helpers.py:100:16"
```

### Pattern

`^[A-Z_]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cee4b6b051f9d839a554e1c471c2ddcc:match

```yaml
regex_id: cee4b6b051f9d839a554e1c471c2ddcc
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/gomod.py:216:11"
```

### Pattern

`^replace\s*\(\s*$`

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

## usage_mismatch:ceec32f3c7760d4a30b9741228631ad8:search

```yaml
regex_id: ceec32f3c7760d4a30b9741228631ad8
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:618:5"
```

### Pattern

`^(inc)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d03c91e6ea87494a9a4766440fde13d7:search

```yaml
regex_id: d03c91e6ea87494a9a4766440fde13d7
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/llm/response_validation.py:33:10"
```

### Pattern

`^CWE-\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d05251e02dbdfcb697534cdfc66f6251:search

```yaml
regex_id: d05251e02dbdfcb697534cdfc66f6251
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/spec_inference.py:62:5"
```

### Pattern

`^handle_|^process_|^on_|^dispatch_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d0b96e2d31ad8ec16691ba5e3f29d2f9:search

```yaml
regex_id: d0b96e2d31ad8ec16691ba5e3f29d2f9
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/_reach_cache.py:157:18"
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

## usage_mismatch:d1236498d82d1e2ec3bf03d0d916d8d6:search

```yaml
regex_id: d1236498d82d1e2ec3bf03d0d916d8d6
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:638:11"
```

### Pattern

`return\s+\d+\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d1f0520d9cd525d98da3168831483c6d:search

```yaml
regex_id: d1f0520d9cd525d98da3168831483c6d
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/typestate.py:106:5"
```

### Pattern

`^(\w+?)_create$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d388e0b7c19c5b709be53f33f7f48ccc:search

```yaml
regex_id: d388e0b7c19c5b709be53f33f7f48ccc
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/inline_installs/__init__.py:691:19"
```

### Pattern

`^(\s*)(?:-\s+)?run:\s*(\S.*?)?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d38a807a28652357e70452764639eb39:search

```yaml
regex_id: d38a807a28652357e70452764639eb39
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/llm/response_validation.py:28:11"
```

### Pattern

`^CVSS:3\.[01]/AV:[NALP]/AC:[LH]/PR:[NLH]/UI:[NR]/S:[UC]/C:[NLH]/I:[NLH]/A:[NLH]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d4087e0d821e606af3c800ef59eec698:search

```yaml
regex_id: d4087e0d821e606af3c800ef59eec698
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:609:40"
```

### Pattern

`^(unpack)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d4e4283e15a23667c151e29bf5182546:search

```yaml
regex_id: d4e4283e15a23667c151e29bf5182546
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/spec_inference.py:51:5"
```

### Pattern

`^init(?:ialize)?_|^setup_|^create_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d5591ba5c6b7026f773273da04ce3d48:search

```yaml
regex_id: d5591ba5c6b7026f773273da04ce3d48
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:643:11"
```

### Pattern

`return\s+\$_\[\d+\]\s*;$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d6ffe883d68883f6d69b38c0c5f24091:search

```yaml
regex_id: d6ffe883d68883f6d69b38c0c5f24091
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/propagation.py:50:16"
```

### Pattern

`(?:^|/)(?:test|tests|testing|__tests__|spec|specs)/|_test\.\w+$|test_\w+\.\w+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d90935ce8b1958ef1a25ec7e13433257:search

```yaml
regex_id: d90935ce8b1958ef1a25ec7e13433257
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:604:11"
```

### Pattern

`\bself\.\w+\.clone\(\)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d93bf3b661c15234fa70d536886b0241:search

```yaml
regex_id: d93bf3b661c15234fa70d536886b0241
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/llm/providers.py:1080:25"
```

### Pattern

`^gpt-(\d+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d992e2e93a1ae407c23eb0014a5e6958:search

```yaml
regex_id: d992e2e93a1ae407c23eb0014a5e6958
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/binary_oracle_autodetect.py:234:19"
```

### Pattern

`^lib[A-Za-z0-9_.+\-]+\.(?:so(?:\.\d+)*|a)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d9f961e82edab0e3ade277b63ffdbd86:search

```yaml
regex_id: d9f961e82edab0e3ade277b63ffdbd86
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/exploit_feasibility/smt_verbs.py:83:12"
```

### Pattern

`^[a-z_][a-z0-9_]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:da8e60782aee8436be79ec80c45b232c:match

```yaml
regex_id: da8e60782aee8436be79ec80c45b232c
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/joern/runner.py:817:39"
```

### Pattern

`^[A-Za-z_][A-Za-z0-9_]*$`

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

## usage_mismatch:dac38ab967c878089280133e8561fa11:search

```yaml
regex_id: dac38ab967c878089280133e8561fa11
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/cve_diff/cve_diff/core/path_classifier.py:31:16"
```

### Pattern

`(?:^|/)(?:tests?|__tests__|specs?|testing|fixtures?)(?:/|$)|(?:^|/)test_[^/]{1,255}(?:\.[^/]{1,255})?$|(?:^|/)[^/]{1,255}_test\.[^/]{1,255}$|(?:^|/)[^/]{1,255}\.(?:test|spec)\.[^/]{1,255}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:db4501cb0d2d74e7b2579ee1a51edc94:search

```yaml
regex_id: db4501cb0d2d74e7b2579ee1a51edc94
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/condition_smt.py:2943:17"
```

### Pattern

`^\s*(?:return\b|goto\s+\w+\s*;)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:db78cbeb8bdda9f5b1987845d56e8fe4:search

```yaml
regex_id: db78cbeb8bdda9f5b1987845d56e8fe4
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:615:5"
```

### Pattern

`^(get)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dc2cd5eca236ad6b169462022deeba5e:search

```yaml
regex_id: dc2cd5eca236ad6b169462022deeba5e
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/callsite_consistency.py:275:21"
```

### Pattern

`^\s*(\w+(?:\.\w+)*)\s*\(`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dc72c15d1ad874dd1ef165ec051538e5:search

```yaml
regex_id: dc72c15d1ad874dd1ef165ec051538e5
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/nvd/client.py:41:14"
```

### Pattern

`^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dc8147900b3b0ffba8195119ddfd34ae:match

```yaml
regex_id: dc8147900b3b0ffba8195119ddfd34ae
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/optimise.py:616:12"
```

### Pattern

`^([A-Za-z0-9_\-.]+)\s*$`

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

## usage_mismatch:dd63a68b54950c16b1acf3e96e3b5188:search

```yaml
regex_id: dd63a68b54950c16b1acf3e96e3b5188
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/binary_oracle.py:191:23"
```

### Pattern

`\.(?:constprop|isra|part|cold|local|lto_priv|clone|_omp_fn|resolver|cfi)(?:\.\d+)?$|\.llvm\.\w+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dda0df39e985c3278d8ebd8d8ea7d49e:search

```yaml
regex_id: dda0df39e985c3278d8ebd8d8ea7d49e
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/binary_oracle.py:517:14"
```

### Pattern

`DW_AT_(\w+)\s*:?\s*(.*?)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:de08d4a99c0dd122e9538a5f7d3dc4f7:search

```yaml
regex_id: de08d4a99c0dd122e9538a5f7d3dc4f7
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/reachability/gemfile.py:34:14"
```

### Pattern

`^\s*(?:require|require_relative)\s+
        (['"])([^'"]+)\1`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:de4e8df41b5f40218bbefcc01b0866db:search

```yaml
regex_id: de4e8df41b5f40218bbefcc01b0866db
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/_util.py:222:15"
```

### Pattern

`^(?P<indent>[ \t]*)(?:async\s+)?def\s+(?P<name>[A-Za-z_]\w*)\s*\(`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:decf606d247f5e13f622c4d872ffc2e5:match

```yaml
regex_id: decf606d247f5e13f622c4d872ffc2e5
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/cargo.py:312:7"
```

### Pattern

`^\d[\w.\-+]*$`

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

## usage_mismatch:defadbd76a84caa57732ab49b36a468a:search

```yaml
regex_id: defadbd76a84caa57732ab49b36a468a
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/exploit_feasibility/smt_onegadget.py:232:8"
```

### Pattern

`\s+is\s+null\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:df3370b2cf6b4e726e89f5a8a0471710:search

```yaml
regex_id: df3370b2cf6b4e726e89f5a8a0471710
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/callsite_consistency.py:271:16"
```

### Pattern

`^\s*(?:if|while|elif|else\s+if|assert)\s*[\s(]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:df7a1046717d256e4e9a9d4ad3b2de62:search

```yaml
regex_id: df7a1046717d256e4e9a9d4ad3b2de62
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/lifecycle_field_discovery.py:35:15"
```

### Pattern

`^class\s+(\w+).*?:\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:df832598c026c7684f6902e1bcd87855:match

```yaml
regex_id: df832598c026c7684f6902e1bcd87855
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/gomod.py:227:21"
```

### Pattern

`^(\S+)(?:\s+\S+)?\s*=>\s*(\S+)(?:\s+(\S+))?\s*$`

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

## usage_mismatch:e11d97de1352dc772ba9310e92c47ce6:search

```yaml
regex_id: e11d97de1352dc772ba9310e92c47ce6
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/platform_matrix/matrix.py:570:19"
```

### Pattern

`^macos-(\d+)(?:\.(\d+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e1909e2a93d0be0894f99b6dff0bc56e:search

```yaml
regex_id: e1909e2a93d0be0894f99b6dff0bc56e
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:624:5"
```

### Pattern

`^(bind)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e26bcccf09576c17763d8c245a0eb06f:search

```yaml
regex_id: e26bcccf09576c17763d8c245a0eb06f
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:620:5"
```

### Pattern

`^(subscribe)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e2ad21b675aeac41e9248fee9f5aaa3e:search

```yaml
regex_id: e2ad21b675aeac41e9248fee9f5aaa3e
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/conan.py:55:10"
```

### Pattern

`^(?P<name>[A-Za-z0-9._\-+]+)/(?P<version>\[[^\]]+\]|[A-Za-z0-9._\-+]+)(?:@(?P<userchannel>[A-Za-z0-9._\-+]+/[A-Za-z0-9._\-+]+))?(?:#[A-Fa-f0-9]+(?:%[0-9.]+)?)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e4036afd6a43b4f2e3d1bbe570f201d3:search

```yaml
regex_id: e4036afd6a43b4f2e3d1bbe570f201d3
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/typestate.py:116:5"
```

### Pattern

`^(\w+?)_get$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e4945294e5369630569d70e49b335aed:search

```yaml
regex_id: e4945294e5369630569d70e49b335aed
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/typestate.py:105:35"
```

### Pattern

`^(\w+?)_(?:destroy|fini|cleanup|deinit)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e4a2209a44df413cd2ec9cf59873cf79:search

```yaml
regex_id: e4a2209a44df413cd2ec9cf59873cf79
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/typestate.py:115:5"
```

### Pattern

`^(\w+?)_ref$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e5b40a86a631da8ad411ea9bf627ed04:search

```yaml
regex_id: e5b40a86a631da8ad411ea9bf627ed04
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/condition_smt.py:1465:13"
```

### Pattern

`^\s*return\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e6775d3ceba49a78b2adabed2ad87edf:search

```yaml
regex_id: e6775d3ceba49a78b2adabed2ad87edf
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/callsite_consistency.py:263:18"
```

### Pattern

`^\s*(?:(?:const|let|var|auto|int|char|void|bool|string|float|double|long|unsigned|size_t|ssize_t|[\w:*&]+)\s+)?\w+\s*(?::=|=[^=])`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e6e084eed870299ad1ad2246d747a49c:match

```yaml
regex_id: e6e084eed870299ad1ad2246d747a49c
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/oci/registry_hosts.py:46:20"
```

### Pattern

`^\d+\.dkr\.ecr\.[a-z0-9-]+\.amazonaws\.com$`

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

## usage_mismatch:e6f6fa1b5ae7dd7bc1d33b1bb932e685:search

```yaml
regex_id: e6f6fa1b5ae7dd7bc1d33b1bb932e685
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/fail_open_detector.py:222:13"
```

### Pattern

`^[ \t]*(?:(?:static|inline|void|int|char|unsigned|const|auto|public|private|protected|func|function|export|async|fn|override|virtual|abstract|final|synchronized)\s+)*(?:\([^)]*\)\s+)?(?:\w+[*&]*\s+)*(\w+)\s*\([^)]*\)\s*\{`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e6f715f6e89483157f8dd36662fbd392:search

```yaml
regex_id: e6f715f6e89483157f8dd36662fbd392
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/exploit_feasibility/strategies.py:239:24"
```

### Pattern

`^ldd\b.*\)\s*(\d+\.\d+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e8884dc16b310241b61bf92d6a0398d1:search

```yaml
regex_id: e8884dc16b310241b61bf92d6a0398d1
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:620:11"
```

### Pattern

`return\s+this\.\w+\s*;$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e907a67500ae4b4d60084b6eac5be763:search

```yaml
regex_id: e907a67500ae4b4d60084b6eac5be763
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/typestate.py:105:5"
```

### Pattern

`^(\w+?)_init$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e959b5d01fab49e59dcd3ea4e83c46a3:search

```yaml
regex_id: e959b5d01fab49e59dcd3ea4e83c46a3
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/extractors.py:2781:17"
```

### Pattern

`^\s*#\s*define\s+(\w+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:eb9b25a5a118bbe7eff575121d2dd090:search

```yaml
regex_id: eb9b25a5a118bbe7eff575121d2dd090
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:628:41"
```

### Pattern

`^(teardown)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ec9ea4cf44f561548990e374875b7f4b:search

```yaml
regex_id: ec9ea4cf44f561548990e374875b7f4b
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/autonomous/poc_source_scan.py:78:5"
```

### Pattern

`^[ \t]*#[ \t]*embed[ \t]*[<"]([^>"]+)[>"]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ecb76bfa5a3b7ff8461a08b420e9ac77:search

```yaml
regex_id: ecb76bfa5a3b7ff8461a08b420e9ac77
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:624:40"
```

### Pattern

`^(unbind)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ecd9fb8cf01f52d42c3c004f8275f038:search

```yaml
regex_id: ecd9fb8cf01f52d42c3c004f8275f038
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/typestate.py:110:5"
```

### Pattern

`^(\w+?)_acquire$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ecdb304fdc70980f23dbe812cd8eaaaa:search

```yaml
regex_id: ecdb304fdc70980f23dbe812cd8eaaaa
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/update.py:1309:18"
```

### Pattern

`^\s*(===|==|>=|<=|~=|!=|>|<)\s*(.+?)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ed073a6b44e45ae5d2f8b48b00a0f63a:search

```yaml
regex_id: ed073a6b44e45ae5d2f8b48b00a0f63a
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/composer.py:203:18"
```

### Pattern

`^v?\d+(\.\d+)*[\w.\-+]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ed9c0fbe2c76d1549375645373602471:search

```yaml
regex_id: ed9c0fbe2c76d1549375645373602471
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/ops_struct.py:15:19"
```

### Pattern

`\.\s*(\w+)\s*=\s*(\w+)\s*,?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:eda4b0e31ed40d4c73de05d267992ec4:search

```yaml
regex_id: eda4b0e31ed40d4c73de05d267992ec4
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/package_json.py:87:11"
```

### Pattern

`^[0-9a-f]{7,40}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:eda9d6afce84b4c24182ff23750b8987:search

```yaml
regex_id: eda9d6afce84b4c24182ff23750b8987
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/test_discovery.py:21:18"
```

### Pattern

`^\s*(?:assert(?:Equal|True|False|Raises|In|NotIn|Is|IsNot|Greater|Less|Regex|Almost|Count|Contains|Not)?|self\.assert\w+|expect\(|assert )(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:eeb6ba8922536f8f47d06c9777dd0ed6:search

```yaml
regex_id: eeb6ba8922536f8f47d06c9777dd0ed6
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/supply_chain/branch_protection.py:67:13"
```

### Pattern

`^(?:ssh://)?git@github\.com[:/](?P<owner>[\w.\-]+)/(?P<repo>[\w.\-]+?)(?:\.git)?/?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ef389e25ea212aef677a303258371bea:search

```yaml
regex_id: ef389e25ea212aef677a303258371bea
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/fail_open_detector.py:144:20"
```

### Pattern

`^\s*except(?:\s+\w[\w.,\s]*)?\s*(?:as\s+\w+)?\s*:\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ef423560d3477b5650d914a3150d796c:search

```yaml
regex_id: ef423560d3477b5650d914a3150d796c
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/inline_installs/_arg_version_pins.py:59:10"
```

### Pattern

`^\s*ARG\s+(\w+_VERSION)\s*=\s*(\S+?)\s*(?:#\s*(.+?)\s*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ef59fe3984e9a89f14c2a81062f5606f:search

```yaml
regex_id: ef59fe3984e9a89f14c2a81062f5606f
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:609:5"
```

### Pattern

`^(pack)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f09a27e406f79c7cfbba05f514ff8232:search

```yaml
regex_id: f09a27e406f79c7cfbba05f514ff8232
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:622:5"
```

### Pattern

`^(attach)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f1c7eace6f37c73626ee76dfb91b9899:match

```yaml
regex_id: f1c7eace6f37c73626ee76dfb91b9899
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/composer.py:198:7"
```

### Pattern

`^v?\d[\w.\-+]*$`

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

## usage_mismatch:f1e65eec589a49606494d1ece88332b2:search

```yaml
regex_id: f1e65eec589a49606494d1ece88332b2
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/spec_inference.py:57:5"
```

### Pattern

`^get_|^fetch_|^read_|^load_|^find_|^lookup_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f22507bbd6083bb5bd76dd8636be182d:search

```yaml
regex_id: f22507bbd6083bb5bd76dd8636be182d
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/wheel_compat/wheel_tags.py:80:20"
```

### Pattern

`^manylinux_(\d+)_(\d+)_(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f282a29386051a2c3f7aecac02c590d5:search

```yaml
regex_id: f282a29386051a2c3f7aecac02c590d5
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/smt_solver/path_feasibility.py:262:11"
```

### Pattern

`^NULL$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f4160bace1c08484cd9cb338c8d8b409:search

```yaml
regex_id: f4160bace1c08484cd9cb338c8d8b409
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/reachability/cargo.py:37:10"
```

### Pattern

`^[ \t]*(?:pub\s+)?use\s+([A-Za-z_][A-Za-z0-9_]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f535400bbc4c0ae8c13e28ad54cc1f21:search

```yaml
regex_id: f535400bbc4c0ae8c13e28ad54cc1f21
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/json/tolerant.py:108:12"
```

### Pattern

`^\s*(?P<delim>```|~~~)\s*(?P<lang>[a-zA-Z0-9_+-]*)\s*\n(?P<body>[\s\S]*?)\n\s*(?P=delim)[^\n]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f54b0b49194bfea485c4f6c41c6bd995:search

```yaml
regex_id: f54b0b49194bfea485c4f6c41c6bd995
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/exploit_feasibility/analyzer.py:3402:24"
```

### Pattern

`^\s*([0-9a-f]+)\s+/bin/sh$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f59dc96dab9757e418e740378b795fb1:search

```yaml
regex_id: f59dc96dab9757e418e740378b795fb1
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/typestate.py:114:36"
```

### Pattern

`^(\w+?)_end$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f60399ef5b4e001ed61f050e0cc70e95:search

```yaml
regex_id: f60399ef5b4e001ed61f050e0cc70e95
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/supply_chain/gha_freshness.py:63:12"
```

### Pattern

`^[A-Za-z\-]*v?(?P<major>\d+)(?:[.\-].*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f7a1b23cb38af73cad36d0934de98358:search

```yaml
regex_id: f7a1b23cb38af73cad36d0934de98358
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:622:11"
```

### Pattern

`return\s+\w+\s*;$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f7cd50641b91fae6168bc64583215fc0:search

```yaml
regex_id: f7cd50641b91fae6168bc64583215fc0
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/audit/prefilter.py:587:11"
```

### Pattern

`return\s+self\.\w+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f80b49954ca20a41da6e103b15961d72:match

```yaml
regex_id: f80b49954ca20a41da6e103b15961d72
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/update.py:1103:24"
```

### Pattern

`^(\s*#+\s*)(.*)$`

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

## usage_mismatch:f85951369ed29772f53b59729a6563cf:search

```yaml
regex_id: f85951369ed29772f53b59729a6563cf
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/supply_chain/git_drift.py:53:16"
```

### Pattern

`^v\d+\.\d+\.\d+(?:-(?:[\w]+\.)?0\.|-)\d{14}-[0-9a-f]{12}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f99725e9b6c08601719088abb2e4ca92:search

```yaml
regex_id: f99725e9b6c08601719088abb2e4ca92
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/source_intel/analyze.py:1669:15"
```

### Pattern

`^\s*(?:[A-Za-z_][A-Za-z0-9_]*[\s*&]+)*([A-Za-z_][A-Za-z0-9_]*)\s*\([^;{]*?\)\s*\{?`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fb5886b64ea0ad95705bbdc67cd891cf:search

```yaml
regex_id: fb5886b64ea0ad95705bbdc67cd891cf
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/inventory/extractors.py:500:21"
```

### Pattern

`(?a)^\s*[A-Za-z_][A-Za-z_0-9]*[A-Za-z_0-9*&\s]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fc33252b7e8196d34daad27ec68f8b65:search

```yaml
regex_id: fc33252b7e8196d34daad27ec68f8b65
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/exploit_feasibility/smt_verbs.py:84:18"
```

### Pattern

`^0x[0-9a-f]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fc8f9498e94ee7c9d42ea81d981b9e95:search

```yaml
regex_id: fc8f9498e94ee7c9d42ea81d981b9e95
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/supply_chain/branch_protection.py:62:15"
```

### Pattern

`^https?://(?:[^@/]+@)?github\.com/(?P<owner>[\w.\-]+)/(?P<repo>[\w.\-]+?)(?:\.git)?/?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fce1cf74a14400a2e25958b910673412:search

```yaml
regex_id: fce1cf74a14400a2e25958b910673412
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/core/analysis/peer_groups.py:605:42"
```

### Pattern

`^(decode)_(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ff710dba70ee9856c390c6b9033f0ca7:search

```yaml
regex_id: ff710dba70ee9856c390c6b9033f0ca7
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/parsers/nuget.py:605:14"
```

### Pattern

`^\s*([\[\(])\s*([^,\[\]\(\)]*?)\s*(?:,\s*([^,\[\]\(\)]*?)\s*)?([\]\)])\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ffd3206f4ac31611502b6de9c3a0b863:match

```yaml
regex_id: ffd3206f4ac31611502b6de9c3a0b863
schema_version: "1"
kind: usage_mismatch
corpus: gadievron-raptor
call_kind: match
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/gadievron-raptor/rules/packages/sca/registry_metadata_walk.py:421:12"
```

### Pattern

`^\s*([A-Za-z0-9._-]+)\s*(.*?)\s*$`

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

## property:inventory:rc-shape1-injection-alphabet:rc-shape1-injection-alphabet

```yaml
regex_id: "inventory:rc-shape1-injection-alphabet"
schema_version: "1"
kind: property
corpus: gadievron-raptor
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
corpus: gadievron-raptor
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
corpus: gadievron-raptor
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
corpus: gadievron-raptor
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

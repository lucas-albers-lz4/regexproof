---
schema_version: "1"
corpus: stateset-icommerce
findings: 104
---

# stateset-icommerce batch findings

## usage_mismatch:0999d73898ac2c0355b09fb670b056ea:search

```yaml
regex_id: 0999d73898ac2c0355b09fb670b056ea
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/skills/parser.js:65:17"
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

## usage_mismatch:0c070ad8c1358fc251096a352ec6600a:search

```yaml
regex_id: 0c070ad8c1358fc251096a352ec6600a
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/chains/validation.js:363:29"
```

### Pattern

`^bc1[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{39,59}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0fcc9861aea84b23498420322cd0be81:search

```yaml
regex_id: 0fcc9861aea84b23498420322cd0be81
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/slack/gateway.js:299:13"
```

### Pattern

`^track[_:\s](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:10938da9ae1e5563f1efc33118c26b71:search

```yaml
regex_id: 10938da9ae1e5563f1efc33118c26b71
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/skills/marketplace.js:773:21"
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

## usage_mismatch:113d20fcb3b8e72375959edb91a82459:search

```yaml
regex_id: 113d20fcb3b8e72375959edb91a82459
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/skills/parser.js:31:23"
```

### Pattern

`^---\s*\n([\s\S]*?)\n---\s*\n?([\s\S]*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:15e665847637d36915604cd1b65d1e8e:search

```yaml
regex_id: 15e665847637d36915604cd1b65d1e8e
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/tools/agent-receipt.js:724:15"
```

### Pattern

`^0x[0-9a-fA-F]{40}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1626ccec07a2434f9dcb60244fdaf0cc:search

```yaml
regex_id: 1626ccec07a2434f9dcb60244fdaf0cc
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/channels/http-gateway.js:79:4"
```

### Pattern

`^::ffff:172\.(1[6-9]|2\d|3[0-1])\.`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:176c3062b93255144f17f6fbe92cf429:search

```yaml
regex_id: 176c3062b93255144f17f6fbe92cf429
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/signal/gateway.js:99:49"
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

## usage_mismatch:18e77ac22e0a600d7204cd6e7c4f4f37:search

```yaml
regex_id: 18e77ac22e0a600d7204cd6e7c4f4f37
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/slack/gateway.js:298:13"
```

### Pattern

`^view_cart[_:\s](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:190e7d68d51e3ddf544c78407b7dd551:search

```yaml
regex_id: 190e7d68d51e3ddf544c78407b7dd551
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/admin/tailwind.config.ts:86:8"
```

### Pattern

`^(border-(?:slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose)-(?:50|100|200|300|400|500|600|700|800|900|950))$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1cb43af24ab432277a8a7cd2de6c334e:search

```yaml
regex_id: 1cb43af24ab432277a8a7cd2de6c334e
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/coverage/mcp-api-coverage.js:678:44"
```

### Pattern

`^\s+([A-Za-z0-9]+)\(`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1d30b716108b85488ebae7f3687d8443:search

```yaml
regex_id: 1d30b716108b85488ebae7f3687d8443
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/tools/agent-receipt.js:399:15"
```

### Pattern

`^[A-Z]{2,8}\/[A-Za-z]{2,8}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:243cdd3274d5f849407f05ef24f641e5:search

```yaml
regex_id: 243cdd3274d5f849407f05ef24f641e5
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/a2a/index.js:116:9"
```

### Pattern

`^[a-fA-F0-9]{64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:281f74ce72f78c9d535e889ba9051b22:search

```yaml
regex_id: 281f74ce72f78c9d535e889ba9051b22
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/chains/config.js:687:25"
```

### Pattern

`^[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2902299a44363c3e7b83e1b4aea9d113:search

```yaml
regex_id: 2902299a44363c3e7b83e1b4aea9d113
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/tools/agent-receipt.js:196:11"
```

### Pattern

`^0x[0-9a-fA-F]{40}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2a67d85dd0ba694ea4310eca90aeb947:search

```yaml
regex_id: 2a67d85dd0ba694ea4310eca90aeb947
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/telegram/gateway.js:215:13"
```

### Pattern

`^inventory[:\s](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2d0e554569d437aeccf92d3a39604842:search

```yaml
regex_id: 2d0e554569d437aeccf92d3a39604842
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/mcp-schema-validator.js:378:13"
```

### Pattern

`^\+?[\d\s-()]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2e9755858b4a18c6bc3fbb2a5773a41a:search

```yaml
regex_id: 2e9755858b4a18c6bc3fbb2a5773a41a
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/channels/browser-evaluate-policy.js:12:2"
```

### Pattern

`^[\d+\-*/%().\s]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:30dda935761ee7ef0804a97a277f8c83:search

```yaml
regex_id: 30dda935761ee7ef0804a97a277f8c83
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/chains/zcash.js:128:9"
```

### Pattern

`^(?:t1|t3|tm|t2)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3154b1de3a749142ec30300d493c439b:search

```yaml
regex_id: 3154b1de3a749142ec30300d493c439b
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/mcp-schema-validator.js:377:12"
```

### Pattern

`^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:32731cea6c85ed73774d370f2084da8e:search

```yaml
regex_id: 32731cea6c85ed73774d370f2084da8e
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/telegram/gateway.js:213:13"
```

### Pattern

`^view_cart[:\s](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:352bf2df48c9772d9fbcc9e24ce5e408:search

```yaml
regex_id: 352bf2df48c9772d9fbcc9e24ce5e408
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/channels/browser-evaluate-policy.js:10:2"
```

### Pattern

`^document\.(title|readyState|URL|baseURI|referrer)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:359fcb5ca4cede384fdb9d60e6fbcf24:search

```yaml
regex_id: 359fcb5ca4cede384fdb9d60e6fbcf24
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/admin/tailwind.config.ts:95:8"
```

### Pattern

`^(stroke-(?:slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose)-(?:50|100|200|300|400|500|600|700|800|900|950))$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:35f6ac5420f2a97a3cd5ce7130541db4:search

```yaml
regex_id: 35f6ac5420f2a97a3cd5ce7130541db4
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/mcp-schema-validator.js:376:11"
```

### Pattern

`^https?:\/\/.+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4022c0b250ecbbe7751b0a501eac0d8d:search

```yaml
regex_id: 4022c0b250ecbbe7751b0a501eac0d8d
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/channels/browser-evaluate-policy.js:17:2"
```

### Pattern

`^document\.getElementById\(\s*(["'])(?:\\.|(?!\1)[^\\\r\n]){1,512}\1\s*\)\.(textContent|innerText|innerHTML|value|href|src|id|className)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:40c4069def15f51816edabd7c0dab6ce:search

```yaml
regex_id: 40c4069def15f51816edabd7c0dab6ce
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/chains/validation.js:314:24"
```

### Pattern

`^zs1[a-z0-9]{75}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:437ac4c6c8d999e3547a33df293620ed:search

```yaml
regex_id: 437ac4c6c8d999e3547a33df293620ed
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/policies/engine.js:74:34"
```

### Pattern

`^(\w+)\[(\d+)\]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4913201c7796c926207507795b1f356a:search

```yaml
regex_id: 4913201c7796c926207507795b1f356a
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/discord/gateway.js:240:13"
```

### Pattern

`^view_cart[:\s](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:496eadb20ff6b96d5a24eaf498d5ba97:search

```yaml
regex_id: 496eadb20ff6b96d5a24eaf498d5ba97
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/chains/validation.js:283:22"
```

### Pattern

`^[1-9A-HJ-NP-Za-km-z]{32,44}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4f52c59662ca8efd8cb42ad2652461b5:search

```yaml
regex_id: 4f52c59662ca8efd8cb42ad2652461b5
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/mcp-schema-validator.js:379:15"
```

### Pattern

`^\d{5}(-\d{4})?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4f818e81614fd95d71bddfd5f29f736a:search

```yaml
regex_id: 4f818e81614fd95d71bddfd5f29f736a
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/slack/gateway.js:300:13"
```

### Pattern

`^inventory[_:\s](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5202b74261402cf0aef2c15960ae192f:search

```yaml
regex_id: 5202b74261402cf0aef2c15960ae192f
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/mcp-schema-validator.js:492:13"
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

## usage_mismatch:55891dde8d73bd2ad931a854d60079fb:search

```yaml
regex_id: 55891dde8d73bd2ad931a854d60079fb
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/mcp-schema-validator.js:461:13"
```

### Pattern

`^\+?[\d\s-()]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:59e03eff015d4bc84d5f95e379585136:search

```yaml
regex_id: 59e03eff015d4bc84d5f95e379585136
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/coverage/binding-accessor-parity.js:54:18"
```

### Pattern

`^pub use ([a-z0-9_]+)::([A-Za-z0-9]+);$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5a4b8cdd3cc0fc34a76dd7dd54e4bce2:search

```yaml
regex_id: 5a4b8cdd3cc0fc34a76dd7dd54e4bce2
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/channels/browser-evaluate-policy.js:11:2"
```

### Pattern

`^window\.(innerWidth|innerHeight|outerWidth|outerHeight|devicePixelRatio|scrollX|scrollY)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5baddaff960342614027b0f05e89bd3a:search

```yaml
regex_id: 5baddaff960342614027b0f05e89bd3a
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/skills/marketplace.js:605:41"
```

### Pattern

`^version:\s*(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5c6e45d8234f627c76e8282cb4186682:search

```yaml
regex_id: 5c6e45d8234f627c76e8282cb4186682
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/chains/validation.js:353:28"
```

### Pattern

`^1[1-9A-HJ-NP-Za-km-z]{25,34}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5faa30af4c8729fa2720b025eab92a83:search

```yaml
regex_id: 5faa30af4c8729fa2720b025eab92a83
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/connectors/wasm-marketplace.js:17:33"
```

### Pattern

`^[a-zA-Z][a-zA-Z0-9_:-]{1,63}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:60170fea1189190c487e98ef151fd3f8:search

```yaml
regex_id: 60170fea1189190c487e98ef151fd3f8
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/skills/parser.js:93:6"
```

### Pattern

`^(list|get|create|update|delete|set|adjust|reserve|confirm|release|approve|reject|send|record|calculate|convert|format|enable|validate|apply|complete|cancel|abandon|pause|resume|skip|activate|deactivate|archive|deliver|ship|start|add|remove|vector|sync)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:67bec9f7c66fa26dbd2795bf4ad559ca:search

```yaml
regex_id: 67bec9f7c66fa26dbd2795bf4ad559ca
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/signal/gateway.js:114:49"
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

## usage_mismatch:68edb354d3885ae96f94b1e03d5d5c5a:search

```yaml
regex_id: 68edb354d3885ae96f94b1e03d5d5c5a
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/slack/gateway.js:297:13"
```

### Pattern

`^view_order[_:\s](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:763c8ae50e42640ebc2acd87ff034a71:email

```yaml
regex_id: 763c8ae50e42640ebc2acd87ff034a71
schema_version: "1"
kind: intent_mismatch
corpus: stateset-icommerce
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/agent-debugger.js:59:15"
```

### Pattern

`email.*already exists|duplicate.*email`

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

## usage_mismatch:77f89110f2eed7be215294f5844b4842:search

```yaml
regex_id: 77f89110f2eed7be215294f5844b4842
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/x402/exact-evm.js:324:7"
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

## usage_mismatch:7834317e60d7ff42c4fe64d9e6769d12:search

```yaml
regex_id: 7834317e60d7ff42c4fe64d9e6769d12
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/chains/validation.js:354:28"
```

### Pattern

`^[mn][1-9A-HJ-NP-Za-km-z]{25,34}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7aaa3c00606defa2280a9e54bf1b5eff:search

```yaml
regex_id: 7aaa3c00606defa2280a9e54bf1b5eff
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/skills/parser.js:66:19"
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

## usage_mismatch:7b37182e2816263d31b0cd27b5af2306:search

```yaml
regex_id: 7b37182e2816263d31b0cd27b5af2306
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/chains/validation.js:315:28"
```

### Pattern

`^ztestsapling1[a-z0-9]{65,}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7bf01d56a17e76b7884b3bdb00e58be5:search

```yaml
regex_id: 7bf01d56a17e76b7884b3bdb00e58be5
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/x402/exact-evm.js:144:9"
```

### Pattern

`^0x[a-fA-F0-9]{40}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7cd1a9d499a630ba701bc46ce715d1f3:search

```yaml
regex_id: 7cd1a9d499a630ba701bc46ce715d1f3
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/admin/tailwind.config.ts:81:8"
```

### Pattern

`^(text-(?:slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose)-(?:50|100|200|300|400|500|600|700|800|900|950))$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7dc2fb181548e41030c8a57a8da9c07b:search

```yaml
regex_id: 7dc2fb181548e41030c8a57a8da9c07b
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/chains/validation.js:320:27"
```

### Pattern

`^utest1[a-z0-9]{50,200}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7f8fae44efc7da696309146c9e72cb3b:search

```yaml
regex_id: 7f8fae44efc7da696309146c9e72cb3b
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/workflows/scheduler.js:80:9"
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

## usage_mismatch:7fe1f51c60ca43c465a40b575b478d78:search

```yaml
regex_id: 7fe1f51c60ca43c465a40b575b478d78
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/discord/gateway.js:239:13"
```

### Pattern

`^view_order[:\s](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:83e4d246f75a9d8215f1a6f8a30bd2b3:search

```yaml
regex_id: 83e4d246f75a9d8215f1a6f8a30bd2b3
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/admin/tailwind.config.ts:91:8"
```

### Pattern

`^(ring-(?:slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose)-(?:50|100|200|300|400|500|600|700|800|900|950))$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8b53a1106d3b9c59fc908e274e6cbde6:search

```yaml
regex_id: 8b53a1106d3b9c59fc908e274e6cbde6
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/tools/agent-receipt.js:718:15"
```

### Pattern

`^0x[0-9a-fA-F]{40}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8c3c7c2751a29d4905f9ed9543503012:search

```yaml
regex_id: 8c3c7c2751a29d4905f9ed9543503012
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/admin/tailwind.config.ts:99:8"
```

### Pattern

`^(fill-(?:slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose)-(?:50|100|200|300|400|500|600|700|800|900|950))$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8cb839e23d99e939480d12fcd2228f9d:search

```yaml
regex_id: 8cb839e23d99e939480d12fcd2228f9d
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/bin/stateset-daemon.js:1474:7"
```

### Pattern

`^[a-zA-Z0-9._@:[\]-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8d6a8fefdaacdf0c071cd82d7b94aea8:search

```yaml
regex_id: 8d6a8fefdaacdf0c071cd82d7b94aea8
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/connectors/wasm-marketplace.js:15:29"
```

### Pattern

`^[a-z0-9][a-z0-9._-]{1,63}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8de74f1cb93c3b04619e916a838b3a56:search

```yaml
regex_id: 8de74f1cb93c3b04619e916a838b3a56
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/bin/stateset-config.js:26:29"
```

### Pattern

`^[A-Za-z0-9._-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8fa59530e4f8aadd675f547ac45b2ae5:search

```yaml
regex_id: 8fa59530e4f8aadd675f547ac45b2ae5
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/discord/gateway.js:241:13"
```

### Pattern

`^track[:\s](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:908535ac3b6709d53d51720ef4dbb655:search

```yaml
regex_id: 908535ac3b6709d53d51720ef4dbb655
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/tools/agent-receipt.js:463:15"
```

### Pattern

`^0x[0-9a-fA-F]{40}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9215a8dc0acc04669b606a16dffe8d78:search

```yaml
regex_id: 9215a8dc0acc04669b606a16dffe8d78
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/workflows/scheduler.js:108:7"
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

## usage_mismatch:94946b97d5b37b366eef225dc0bc6dda:search

```yaml
regex_id: 94946b97d5b37b366eef225dc0bc6dda
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/session.js:15:27"
```

### Pattern

`^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:94ed8441050eb4774e3b49178e495ecc:search

```yaml
regex_id: 94ed8441050eb4774e3b49178e495ecc
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/telegram/gateway.js:214:13"
```

### Pattern

`^track[:\s](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:966704c9eaccefd476177369a9e48d71:search

```yaml
regex_id: 966704c9eaccefd476177369a9e48d71
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/bin/stateset-direct.js:505:8"
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

## usage_mismatch:9b3fa8106b03bccbcd75bedb5bd3b3c3:search

```yaml
regex_id: 9b3fa8106b03bccbcd75bedb5bd3b3c3
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/skills/marketplace.js:729:4"
```

### Pattern

`^[a-zA-Z]:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a0b74244faef9986de557cd78b441664:search

```yaml
regex_id: a0b74244faef9986de557cd78b441664
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/chains/validation.js:310:24"
```

### Pattern

`^t[13m2][1-9A-HJ-NP-Za-km-z]{33}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a358841dcacecbab645c23a56842f512:search

```yaml
regex_id: a358841dcacecbab645c23a56842f512
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/coverage/binding-accessor-parity.js:68:41"
```

### Pattern

`^\s*get ([A-Za-z0-9]+)\(\)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a3670346f29ad7c436c74bedb5d1bd2d:search

```yaml
regex_id: a3670346f29ad7c436c74bedb5d1bd2d
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/chains/zcash.js:132:9"
```

### Pattern

`^(?:u1|utest1|zs1|ztestsapling1)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a3c191d09a267db32cfc34c8507fb2a0:search

```yaml
regex_id: a3c191d09a267db32cfc34c8507fb2a0
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/admin/tailwind.config.ts:76:8"
```

### Pattern

`^(bg-(?:slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose)-(?:50|100|200|300|400|500|600|700|800|900|950))$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a791c94cd1f44f132113dade906bc0f9:search

```yaml
regex_id: a791c94cd1f44f132113dade906bc0f9
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/memory/markdown-store.js:80:41"
```

### Pattern

`^\*\*(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\*\*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a7a0602949949156e020e157c7d78d7c:search

```yaml
regex_id: a7a0602949949156e020e157c7d78d7c
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/memory/markdown-store.js:71:33"
```

### Pattern

`^---$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ac032ad0ab602e05b315d31f7a865381:search

```yaml
regex_id: ac032ad0ab602e05b315d31f7a865381
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/mcp-schema-validator.js:375:13"
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

## usage_mismatch:ad7c615cddfa6f747bb7477c0cf68fa3:search

```yaml
regex_id: ad7c615cddfa6f747bb7477c0cf68fa3
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/chains/validation.js:358:27"
```

### Pattern

`^2[1-9A-HJ-NP-Za-km-z]{25,34}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:aeb2a43da5d8379ddd04a983c10fa049:search

```yaml
regex_id: aeb2a43da5d8379ddd04a983c10fa049
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/chains/validation.js:319:30"
```

### Pattern

`^u1[a-z0-9]{50,200}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b1c83c26bce8bf569f2cae0dd4a96110:search

```yaml
regex_id: b1c83c26bce8bf569f2cae0dd4a96110
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/discord/gateway.js:242:13"
```

### Pattern

`^inventory[:\s](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b4378ce23e234e70d99ae97d4a8daecb:search

```yaml
regex_id: b4378ce23e234e70d99ae97d4a8daecb
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/tools/agent-receipt.js:470:15"
```

### Pattern

`^0x[0-9a-fA-F]{40}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b9e5632a6ab76ef1fb661af9a2571fe7:search

```yaml
regex_id: b9e5632a6ab76ef1fb661af9a2571fe7
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/chains/validation.js:254:7"
```

### Pattern

`^0x[0-9a-fA-F]{40}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bfd21997929bf8798cf597f835db58cc:search

```yaml
regex_id: bfd21997929bf8798cf597f835db58cc
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/admin/src/lib/finance/format.ts:10:23"
```

### Pattern

`^-?\d+(\.\d+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c770cdc81b570345275a0c7d41ec52e3:search

```yaml
regex_id: c770cdc81b570345275a0c7d41ec52e3
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/x402/exact-evm.js:719:9"
```

### Pattern

`^0x[a-fA-F0-9]{64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c80a775763c77df4c1aa47b8d61a9834:search

```yaml
regex_id: c80a775763c77df4c1aa47b8d61a9834
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/skills/marketplace.js:774:7"
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

## usage_mismatch:cacd12bba08909ca9e4e7512b9b3811d:search

```yaml
regex_id: cacd12bba08909ca9e4e7512b9b3811d
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/admin/src/lib/shared/schemas.ts:160:9"
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

## usage_mismatch:ce0a18b72996989f47fc7689a699c612:search

```yaml
regex_id: ce0a18b72996989f47fc7689a699c612
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/policies/engine.js:113:28"
```

### Pattern

`^\$\{([^}]+)\}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d02076d93c41effae48e2cb3bf7e60cb:search

```yaml
regex_id: d02076d93c41effae48e2cb3bf7e60cb
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/workflows/scheduler.js:80:38"
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

## usage_mismatch:d43d2e87af60c1b22b3e2d02cbca26d4:search

```yaml
regex_id: d43d2e87af60c1b22b3e2d02cbca26d4
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/teams/gateway.js:737:13"
```

### Pattern

`^view_order[_:\s](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d572eb2ef40bbf4bf7db0e157507ebf5:search

```yaml
regex_id: d572eb2ef40bbf4bf7db0e157507ebf5
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/x402/exact-evm.js:152:9"
```

### Pattern

`^0x[a-fA-F0-9]{64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:db3282224ba17d8341b307199a840422:search

```yaml
regex_id: db3282224ba17d8341b307199a840422
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/tools/agent-receipt.js:215:11"
```

### Pattern

`^0x[0-9a-fA-F]{64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:db647bbe79f2844af6e1a8a21c1c1375:search

```yaml
regex_id: db647bbe79f2844af6e1a8a21c1c1375
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/bin/stateset-daemon.js:249:39"
```

### Pattern

`^ANTHROPIC_API_KEY=\S+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dbcb53b09fa34d66aeb1e0250aaa298d:search

```yaml
regex_id: dbcb53b09fa34d66aeb1e0250aaa298d
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/plugins/loader.js:35:11"
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

## usage_mismatch:dc3912dc31612db77c814c5a1ab61751:search

```yaml
regex_id: dc3912dc31612db77c814c5a1ab61751
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/channels/http-gateway.js:122:29"
```

### Pattern

`^\[([^\]]+)\]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e0267d1d5d23ae20adb49f3b8b3726eb:search

```yaml
regex_id: e0267d1d5d23ae20adb49f3b8b3726eb
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/chains/validation.js:357:27"
```

### Pattern

`^3[1-9A-HJ-NP-Za-km-z]{25,34}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e205b0ade31fe0f0adb9e83bebe1f342:search

```yaml
regex_id: e205b0ade31fe0f0adb9e83bebe1f342
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/teams/gateway.js:739:13"
```

### Pattern

`^track[_:\s](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e3fb40bc0ee2b7cf2f4ce97f76bdad43:search

```yaml
regex_id: e3fb40bc0ee2b7cf2f4ce97f76bdad43
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/chains/validation.js:364:29"
```

### Pattern

`^tb1[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{39,59}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e58750e4a537401a667fda967cf452c0:search

```yaml
regex_id: e58750e4a537401a667fda967cf452c0
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/channels/browser-evaluate-policy.js:16:2"
```

### Pattern

`^document\.querySelector\(\s*(["'])(?:\\.|(?!\1)[^\\\r\n]){1,512}\1\s*\)\.(textContent|innerText|innerHTML|value|href|src|id|className)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e6f592cd9dbc4e4ab3c0ba1f79bf816b:search

```yaml
regex_id: e6f592cd9dbc4e4ab3c0ba1f79bf816b
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/teams/gateway.js:740:13"
```

### Pattern

`^inventory[_:\s](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e7b3ae76ffcf823da5124e5ce222bcdf:search

```yaml
regex_id: e7b3ae76ffcf823da5124e5ce222bcdf
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/teams/gateway.js:738:13"
```

### Pattern

`^view_cart[_:\s](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:efb9fc1fb0f955f6577235b64a47846d:search

```yaml
regex_id: efb9fc1fb0f955f6577235b64a47846d
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/tools/agent-receipt.js:540:15"
```

### Pattern

`^\d{4}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f26828d4ac3c5aa0a32fb3eef3c95905:search

```yaml
regex_id: f26828d4ac3c5aa0a32fb3eef3c95905
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/connectors/wasm-marketplace.js:16:34"
```

### Pattern

`^[0-9A-Za-z][0-9A-Za-z._+-]{0,63}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f44409ac66527b80872c886d4457d71b:search

```yaml
regex_id: f44409ac66527b80872c886d4457d71b
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/channels/browser-evaluate-policy.js:18:2"
```

### Pattern

`^document\.querySelectorAll\(\s*(["'])(?:\\.|(?!\1)[^\\\r\n]){1,512}\1\s*\)\.length$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f5bb49e4a3ed79c3d18566e8b6b7c054:search

```yaml
regex_id: f5bb49e4a3ed79c3d18566e8b6b7c054
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/workflows/scheduler.js:56:9"
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

## usage_mismatch:f92c63adde65e3bd2e939a00b154d381:search

```yaml
regex_id: f92c63adde65e3bd2e939a00b154d381
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/src/telegram/gateway.js:212:13"
```

### Pattern

`^view_order[:\s](.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:feaadc0acec1a2fd36ea9762a2edf8de:search

```yaml
regex_id: feaadc0acec1a2fd36ea9762a2edf8de
schema_version: "1"
kind: usage_mismatch
corpus: stateset-icommerce
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/stateset-icommerce/rules/cli/test/helpers/sqlite-mock.js:109:34"
```

### Pattern

`^(\w+)\s*=\s*(.+)$`

### Context

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
corpus: stateset-icommerce
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
corpus: stateset-icommerce
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
corpus: stateset-icommerce
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
corpus: stateset-icommerce
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

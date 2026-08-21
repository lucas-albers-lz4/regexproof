---
schema_version: "1"
corpus: SveltyCMS-SveltyCMS
findings: 242
---

# SveltyCMS-SveltyCMS batch findings

## usage_mismatch:0425914f192b7e4684083dbc5260a751:search

```yaml
regex_id: 0425914f192b7e4684083dbc5260a751
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/mongodb/normalize-id.ts:22:38"
```

### Pattern

`^[0-9a-fA-F]{24}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:04912eb91acd24c1f3ae716adb9e8e80:search

```yaml
regex_id: 04912eb91acd24c1f3ae716adb9e8e80
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/json-path-filter.ts:27:18"
```

### Pattern

`^\s*([A-Za-z0-9_.[\]]+)\s*(==|!=|>=|<=|~|\*=|=|>|<)\s*(.+?)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:06a0a069350fb2de2de6c48dbbd4568f:search

```yaml
regex_id: 06a0a069350fb2de2de6c48dbbd4568f
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/slop-scanner.ts:655:46"
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

## usage_mismatch:075c5aa007349980109c200a7371f3b3:search

```yaml
regex_id: 075c5aa007349980109c200a7371f3b3
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/run-integration.ts:358:29"
```

### Pattern

`^\s*\((pass|fail)\)\s+(.+?)\s*\[([\d.]+)ms\]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:09302f3a73823d2c2968b60c6395f9b9:search

```yaml
regex_id: 09302f3a73823d2c2968b60c6395f9b9
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/media/signed-urls.ts:51:34"
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

## usage_mismatch:099350a6d4cb22834636200b210ec82e:search

```yaml
regex_id: 099350a6d4cb22834636200b210ec82e
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/scan-security-risk.ts:466:16"
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

## usage_mismatch:0aa2ca6d8ff41e75dbcfc28477e203ed:search

```yaml
regex_id: 0aa2ca6d8ff41e75dbcfc28477e203ed
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:65:2"
```

### Pattern

`[/\\]populate-resolver\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0aa4faa7982cf27eb7faae202b92b0f2:search

```yaml
regex_id: 0aa4faa7982cf27eb7faae202b92b0f2
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/routes/api/[...path]/handlers/utility.ts:258:7"
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

## usage_mismatch:0c330c4864062705d267e1fffd6deba8:search

```yaml
regex_id: 0c330c4864062705d267e1fffd6deba8
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:42:2"
```

### Pattern

`[/\\]boot-engine\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0c7dd0995d883c3a77b6aa75f853e57f:search

```yaml
regex_id: 0c7dd0995d883c3a77b6aa75f853e57f
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/postgresql/connection.ts:66:18"
```

### Pattern

`^\d+(kB|MB|GB)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0fbad2825c756e918b2408f72ca9103e:search

```yaml
regex_id: 0fbad2825c756e918b2408f72ca9103e
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:45:2"
```

### Pattern

`[/\\]migrated-media\.server\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:11919173016ab247fedec5c8fcd7aa74:search

```yaml
regex_id: 11919173016ab247fedec5c8fcd7aa74
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/egress-guard.ts:26:2"
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

## usage_mismatch:11ebfe6f2d91cab720153ded078c3b76:search

```yaml
regex_id: 11ebfe6f2d91cab720153ded078c3b76
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/config-state.ts:540:4"
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

## usage_mismatch:11f7b1b25669e64cab440a6b1cb83d17:search

```yaml
regex_id: 11f7b1b25669e64cab440a6b1cb83d17
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/smart-importer/performance.ts:47:24"
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

## usage_mismatch:12a2adce60ceb20c5ebd370da6e6c49d:search

```yaml
regex_id: 12a2adce60ceb20c5ebd370da6e6c49d
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/scan-security-risk.ts:514:19"
```

### Pattern

`^['"`]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:153392863ce7726f275f38d583d433c8:search

```yaml
regex_id: 153392863ce7726f275f38d583d433c8
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/unified-data-hub/server/ssrf.ts:22:2"
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

## usage_mismatch:16456b9db1b520c46fc255c30dc35b9a:search

```yaml
regex_id: 16456b9db1b520c46fc255c30dc35b9a
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/routes/(app)/config/redirects/redirects-utils.ts:22:21"
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

## usage_mismatch:1671f0a39124225657cd846cf729d6c8:search

```yaml
regex_id: 1671f0a39124225657cd846cf729d6c8
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/services/core/content-sync-service.ts:167:22"
```

### Pattern

`(^|_)name$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:171810b2c952cfbfbde052156239e535:search

```yaml
regex_id: 171810b2c952cfbfbde052156239e535
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/scan-security-risk.ts:534:12"
```

### Pattern

`^[A-Za-z_][A-Za-z0-9_.]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:181ed1c75ce8cf895b2eb4bbfc527f9e:search

```yaml
regex_id: 181ed1c75ce8cf895b2eb4bbfc527f9e
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/widgets/custom/seo/index.ts:65:39"
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

## usage_mismatch:1824b9ad24d95b43c39c2c44a338b744:search

```yaml
regex_id: 1824b9ad24d95b43c39c2c44a338b744
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/sqlite/adapter-core.ts:1479:16"
```

### Pattern

`^\s*(insert|update|delete|create|drop|alter|replace|begin|commit|rollback|savepoint)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:184f59bb2e9ae36049ff8d94cdd949a8:search

```yaml
regex_id: 184f59bb2e9ae36049ff8d94cdd949a8
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/test-bypass.server.ts:206:22"
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

## usage_mismatch:18afdb6c12b8501dc9c86b5898e0071e:search

```yaml
regex_id: 18afdb6c12b8501dc9c86b5898e0071e
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/hooks/handle-content-initialization.ts:63:6"
```

### Pattern

`^\/[a-z]{2,5}(?:-[a-zA-Z]+)?\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1d20ea590817884f50d1073864228624:search

```yaml
regex_id: 1d20ea590817884f50d1073864228624
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/media/storage-adapters.ts:22:2"
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

## usage_mismatch:1ed998dee08fee47daad9e6a27f81194:search

```yaml
regex_id: 1ed998dee08fee47daad9e6a27f81194
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/routes/(app)/config/system-settings/settings-utils.ts:93:23"
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

## usage_mismatch:1f409fa2f35b4dc73c12207dcaa1f98a:search

```yaml
regex_id: 1f409fa2f35b4dc73c12207dcaa1f98a
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/services/sdk/namespaces/auth-namespace.ts:200:21"
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

## usage_mismatch:200286dbcbf65bf357b6ae7f7e9a6878:search

```yaml
regex_id: 200286dbcbf65bf357b6ae7f7e9a6878
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/widgets/core/slug/index.ts:58:6"
```

### Pattern

`^[a-z0-9-_]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2028b3b36e17dc16d588f3b6d6d4bdf2:search

```yaml
regex_id: 2028b3b36e17dc16d588f3b6d6d4bdf2
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/content/sync-content-state.server.ts:627:41"
```

### Pattern

`\.(ts|js)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:23ea0a43f5b633a5809c2fb37922f53d:search

```yaml
regex_id: 23ea0a43f5b633a5809c2fb37922f53d
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/mariadb/connection.ts:57:26"
```

### Pattern

`^[a-zA-Z0-9_\s=;'-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:25f81a5ad2fade8d424af71e1d6f2e29:search

```yaml
regex_id: 25f81a5ad2fade8d424af71e1d6f2e29
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/date.ts:206:36"
```

### Pattern

`^PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:267266004be6db7dad12e8b9ee5f5c15:search

```yaml
regex_id: 267266004be6db7dad12e8b9ee5f5c15
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/unified-data-hub/server/ssrf.ts:17:2"
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

## usage_mismatch:292a3affb92b322db8aee8545c37dbee:search

```yaml
regex_id: 292a3affb92b322db8aee8545c37dbee
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/unified-data-hub/server/ssrf.ts:14:2"
```

### Pattern

`^localhost$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:29b2c96790c52684b3cb9b5651209ded:search

```yaml
regex_id: 29b2c96790c52684b3cb9b5651209ded
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/hook-utils.ts:71:2"
```

### Pattern

`^\/(?!api(?:\/|$))[a-z]{2,5}(?:-[a-zA-Z]+)?\/(?:setup|login|register|forgot-password)(?:\/|$|\?)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2bce069c6832153b6a2566c71fc0899e:search

```yaml
regex_id: 2bce069c6832153b6a2566c71fc0899e
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/hook-utils.ts:69:2"
```

### Pattern

`^\/(?!api(?:\/|$))[a-z]{2,5}(?:-[a-zA-Z]+)?\/(?:setup|login|register)(?:\/|$|\?)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2bde88fc1f1a717469eb59bad58e71fb:search

```yaml
regex_id: 2bde88fc1f1a717469eb59bad58e71fb
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/settings-crypto.ts:78:8"
```

### Pattern

`^[0-9a-fA-F]{64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2d5f1635641568a7f20cb9dd0e2023fb:search

```yaml
regex_id: 2d5f1635641568a7f20cb9dd0e2023fb
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/media/storage-adapters.ts:27:2"
```

### Pattern

`^fc00:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2d69fe0232c46885c266c5f384c996a2:search

```yaml
regex_id: 2d69fe0232c46885c266c5f384c996a2
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/media/media-reference-index.ts:144:67"
```

### Pattern

`^[a-f0-9]{32,}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2f5e059c3cfe3cf7cb5d4d5e989f03a8:search

```yaml
regex_id: 2f5e059c3cfe3cf7cb5d4d5e989f03a8
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/smart-importer/parsers/universal.ts:461:34"
```

### Pattern

`^\s+-\s+(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2ff5c95f76c0c3aca2fed92e80c8be9c:search

```yaml
regex_id: 2ff5c95f76c0c3aca2fed92e80c8be9c
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/scan-secret-misuse.ts:412:27"
```

### Pattern

`^[a-z][-a-z0-9/]+ `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:306b353f38046d5927fe09aedb75acb8:search

```yaml
regex_id: 306b353f38046d5927fe09aedb75acb8
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:41:2"
```

### Pattern

`[/\\]db-init\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:308888c686053ebc339e5e94aa5f0908:search

```yaml
regex_id: 308888c686053ebc339e5e94aa5f0908
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:57:2"
```

### Pattern

`[/\\]handlers[/\\]setup\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:32e179f358edd635256210a1353569b2:search

```yaml
regex_id: 32e179f358edd635256210a1353569b2
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/log-export.ts:43:56"
```

### Pattern

`\.(\d+)\.gz$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:32ee5e05bd900378c3d45bc2f213e3ec:email

```yaml
regex_id: 32ee5e05bd900378c3d45bc2f213e3ec
schema_version: "1"
kind: intent_mismatch
corpus: SveltyCMS-SveltyCMS
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/routes/login/oauth/+page.server.ts:310:38"
```

### Pattern

`(.{2}).*@(.*)`

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

## usage_mismatch:3326ebf4c0497424903429da04aac862:search

```yaml
regex_id: 3326ebf4c0497424903429da04aac862
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/check-widget-naming.mjs:38:20"
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

## usage_mismatch:358fa57dda174de97f01642c079c74a6:search

```yaml
regex_id: 358fa57dda174de97f01642c079c74a6
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/media/storage-adapters.ts:28:2"
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

## usage_mismatch:36a360fb832df67c60f891ec28d2345a:search

```yaml
regex_id: 36a360fb832df67c60f891ec28d2345a
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/scan-security-risk.ts:109:9"
```

### Pattern

`[\\/]routes[\\/].*[\\/]\+page\.server\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:36cc939ccb54b746ddfec6b44d3917a4:search

```yaml
regex_id: 36cc939ccb54b746ddfec6b44d3917a4
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/widgets/custom/phone-number/index.ts:29:25"
```

### Pattern

`^\+?[1-9]\d{1,14}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3723625693c70b05bb786f9734c22de7:search

```yaml
regex_id: 3723625693c70b05bb786f9734c22de7
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/auth/totp.ts:432:22"
```

### Pattern

`^[A-Z2-7]+=*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:374e118018f7ed07fea1eb2c6e86f528:search

```yaml
regex_id: 374e118018f7ed07fea1eb2c6e86f528
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/egress-guard.ts:31:2"
```

### Pattern

`^fe80:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:379876cd5713b26c598b46a5cbdff0fe:search

```yaml
regex_id: 379876cd5713b26c598b46a5cbdff0fe
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:44:2"
```

### Pattern

`[/\\]demo-cleanup\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:390debf2cbd1575cfc685e7de13fe720:search

```yaml
regex_id: 390debf2cbd1575cfc685e7de13fe720
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/media/storage-adapters.ts:26:2"
```

### Pattern

`^fe80:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3910a49aae8f2f642c4f2aa033ed4e83:search

```yaml
regex_id: 3910a49aae8f2f642c4f2aa033ed4e83
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/unified-data-hub/server/ssrf.ts:21:2"
```

### Pattern

`^\[::1\]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3914b00aee716bd021206b1749c7b4ed:search

```yaml
regex_id: 3914b00aee716bd021206b1749c7b4ed
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/media/signed-urls.ts:28:15"
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

## usage_mismatch:3956634670e15775378ab6e452c29f67:search

```yaml
regex_id: 3956634670e15775378ab6e452c29f67
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/hooks/wasm-waf-guard.ts:43:2"
```

### Pattern

`--\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3ab57724f355818beca858c8ce725300:search

```yaml
regex_id: 3ab57724f355818beca858c8ce725300
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/hooks/handle-turbo-pipeline.server.ts:423:43"
```

### Pattern

`^\/[a-z]{2,5}(-[a-zA-Z]+)?\/setup`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3be67ae66e30fee142691af974282f81:search

```yaml
regex_id: 3be67ae66e30fee142691af974282f81
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/collection-query-filters.ts:197:7"
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

## usage_mismatch:3e63baddd6a7857542c06aa74d936a83:search

```yaml
regex_id: 3e63baddd6a7857542c06aa74d936a83
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/widgets/custom/remote-video/index.ts:48:2"
```

### Pattern

`^https?:\/\/(www\.)?(youtube\.com\/watch\?v=|youtu\.be\/)([a-zA-Z0-9_-]{11})`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3e65083a19333a47fa4badc783d3ffa5:search

```yaml
regex_id: 3e65083a19333a47fa4badc783d3ffa5
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:50:2"
```

### Pattern

`[/\\]tenant-adapter\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3e97adb6492521b9cd683cde325b5645:search

```yaml
regex_id: 3e97adb6492521b9cd683cde325b5645
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/smart-importer/parsers/universal.ts:412:34"
```

### Pattern

`^\{[\s\S]*?\}\r?\n([\s\S]*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3f472d77847afdc38a316ca7d96531a4:search

```yaml
regex_id: 3f472d77847afdc38a316ca7d96531a4
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/media/streaming-upload.ts:68:2"
```

### Pattern

`^(image\/(jpeg|png|gif|webp|svg\+xml|bmp|tiff|avif)|video\/(mp4|webm|ogg|quicktime|x-msvideo)|audio\/(mpeg|ogg|wav|webm|aac|flac)|application\/(pdf|json|zip|gzip|x-tar|x-7z-compressed))$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:40858135c4bdc07eeb95aac66ac9cf69:search

```yaml
regex_id: 40858135c4bdc07eeb95aac66ac9cf69
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/sqlite/adapter-core.ts:998:10"
```

### Pattern

`^\s*(create|drop|alter|insert|update|delete|replace|pragma|begin|commit|rollback|savepoint)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:40c5617c7b9028fd15ced034bff39a21:search

```yaml
regex_id: 40c5617c7b9028fd15ced034bff39a21
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/hooks/handle-test-isolation.ts:70:9"
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

## usage_mismatch:440dc05c6ff0cfa26c09a6ac633661ef:search

```yaml
regex_id: 440dc05c6ff0cfa26c09a6ac633661ef
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/unified-data-hub/server/ssrf.ts:15:2"
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

## usage_mismatch:44c384cd352f3e066dcc7487e4b209e5:search

```yaml
regex_id: 44c384cd352f3e066dcc7487e4b209e5
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/scan-security-risk.ts:221:10"
```

### Pattern

`Url$|URL$|Href$|Endpoint$|Uri$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4555a65ea4f342a383d87bb91ba554b0:search

```yaml
regex_id: 4555a65ea4f342a383d87bb91ba554b0
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/core/relational-utils.ts:357:4"
```

### Pattern

`^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}(\.\d+)?[+-]\d{2}(:\d{2})?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:463db853b21333cb51e1f8bad8df99ab:search

```yaml
regex_id: 463db853b21333cb51e1f8bad8df99ab
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/core/relational-utils.ts:709:35"
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

## usage_mismatch:475890e3a40be21e31b47547192da6ae:search

```yaml
regex_id: 475890e3a40be21e31b47547192da6ae
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:61:2"
```

### Pattern

`[/\\]telemetry-service\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:487229014791c72088fe2bdef08a00a5:search

```yaml
regex_id: 487229014791c72088fe2bdef08a00a5
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/unified-data-hub/server/rest-fixture.ts:104:45"
```

### Pattern

`^\/wp-json\/wp\/v2\/posts\/([^/]+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:49815c0e5125af9316d87dd26f36d868:search

```yaml
regex_id: 49815c0e5125af9316d87dd26f36d868
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/scan-secret-misuse.ts:540:23"
```

### Pattern

`\.(ts|svelte|js)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4a030dd0e5e7c2df9368a1ee875bc9f2:search

```yaml
regex_id: 4a030dd0e5e7c2df9368a1ee875bc9f2
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/compilation/transformers.ts:37:20"
```

### Pattern

`\.(js|mjs|cjs|json|ts|svelte|svelte\.ts|css|svg|png|jpe?g|webp|wasm)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4aa16051351d9777ef2b697991713d9e:search

```yaml
regex_id: 4aa16051351d9777ef2b697991713d9e
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/test-smart.ts:610:21"
```

### Pattern

`^[A-Z_][A-Z0-9_]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4ccf13915a7685319d2abeb032eb9ed4:search

```yaml
regex_id: 4ccf13915a7685319d2abeb032eb9ed4
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/mongodb/media-methods.ts:364:67"
```

### Pattern

`^global\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:50841babcc35ac729be5869b9bcd76ae:search

```yaml
regex_id: 50841babcc35ac729be5869b9bcd76ae
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:51:2"
```

### Pattern

`[/\\]mongo-db-adapter\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:525751228e297c931a8c03b71c4b877b:search

```yaml
regex_id: 525751228e297c931a8c03b71c4b877b
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/unified-data-hub/server/rest-write-utils.ts:10:27"
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

## usage_mismatch:52618b193f1156732d2e34180f0919a0:search

```yaml
regex_id: 52618b193f1156732d2e34180f0919a0
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/vite.config.ts:264:8"
```

### Pattern

`(?:^|\/)\+?(?:page|layout|server|error)(?:\.[^/]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5273a30744b62185d2a9d2bdf38a38f3:search

```yaml
regex_id: 5273a30744b62185d2a9d2bdf38a38f3
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/id-generator.ts:54:6"
```

### Pattern

`^[0-9-]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:544502076b6391aec0015a3abbced13e:email

```yaml
regex_id: 544502076b6391aec0015a3abbced13e
schema_version: "1"
kind: intent_mismatch
corpus: SveltyCMS-SveltyCMS
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/routes/login/oauth/+page.server.ts:261:38"
```

### Pattern

`(.{2}).*@(.*)`

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

## usage_mismatch:54f2794ebdb291af25d53bac5f4fe32c:search

```yaml
regex_id: 54f2794ebdb291af25d53bac5f4fe32c
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/schemas.ts:52:8"
```

### Pattern

`^[a-zA-Z0-9@$!%*#._-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:55fa67c4c99ce3bbee742fc4f7cb967f:search

```yaml
regex_id: 55fa67c4c99ce3bbee742fc4f7cb967f
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/scan-security-risk.ts:494:24"
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

## usage_mismatch:56804d70dc55d02f2894556464f97ae2:search

```yaml
regex_id: 56804d70dc55d02f2894556464f97ae2
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/slop-scanner.ts:562:4"
```

### Pattern

`\.(?:server|remote|ws)\.(?:ts|js)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:57049c699f2eda6290f308539b7c58e3:search

```yaml
regex_id: 57049c699f2eda6290f308539b7c58e3
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/media/storage-adapters.ts:24:2"
```

### Pattern

`^0\.0\.0\.0$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5759685adba859f7379a873ad197ddcf:search

```yaml
regex_id: 5759685adba859f7379a873ad197ddcf
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/schemas.ts:74:4"
```

### Pattern

`^(?=.*[A-Za-z])(?=.*[0-9])(?=.*[!@#$%^&*()_+\-=[\]{};':"\\|,.<>?]).+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:59492267ca91ce525f86e7562c6b3a1a:search

```yaml
regex_id: 59492267ca91ce525f86e7562c6b3a1a
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/scan-secret-misuse.ts:437:8"
```

### Pattern

`^<[a-z]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5b1b0eef579438732320c0817b42aac1:search

```yaml
regex_id: 5b1b0eef579438732320c0817b42aac1
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/core/drizzle-sql-helpers.ts:678:9"
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

## usage_mismatch:5c6f0352855eea085b75eedaa8427496:search

```yaml
regex_id: 5c6f0352855eea085b75eedaa8427496
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/postgresql/postgres-adapter.ts:154:50"
```

### Pattern

`^[A-Za-z0-9_"]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5ca437a02d0bc3a44017c0ece7cb375b:search

```yaml
regex_id: 5ca437a02d0bc3a44017c0ece7cb375b
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/upgrade.ts:61:23"
```

### Pattern

`^[a-zA-Z0-9._/-]{1,100}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5d02f400d0f6d162448f49c51123c173:search

```yaml
regex_id: 5d02f400d0f6d162448f49c51123c173
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:49:2"
```

### Pattern

`[/\\]relational-system\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5d6f3ac51c41240599457133c00de9e3:search

```yaml
regex_id: 5d6f3ac51c41240599457133c00de9e3
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/egress-guard.ts:27:2"
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

## usage_mismatch:5dbef8ea561fdfd42a0fc906eab0535c:search

```yaml
regex_id: 5dbef8ea561fdfd42a0fc906eab0535c
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/egress-guard.ts:28:2"
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

## usage_mismatch:5ee261350f30d316422cb01157943bee:search

```yaml
regex_id: 5ee261350f30d316422cb01157943bee
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/smart-importer/parsers/wordpress.ts:425:6"
```

### Pattern

`^i:\d+;$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5f050b40c1e2be8ba3c6f9adc5e3f0de:search

```yaml
regex_id: 5f050b40c1e2be8ba3c6f9adc5e3f0de
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/check-widget-naming.mjs:37:22"
```

### Pattern

`^[a-z][a-z0-9]*(-[a-z0-9]+)*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:604f2b47c8f7da0478af329539b1b461:search

```yaml
regex_id: 604f2b47c8f7da0478af329539b1b461
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/schemas.ts:343:8"
```

### Pattern

`^[a-z]{2}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:60b5b3d7592afd823e8b9a65fac09a74:search

```yaml
regex_id: 60b5b3d7592afd823e8b9a65fac09a74
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/egress-guard.ts:25:2"
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

## usage_mismatch:6160dd6b673f8c6da06a0b4138bff027:search

```yaml
regex_id: 6160dd6b673f8c6da06a0b4138bff027
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/hook-utils.ts:54:2"
```

### Pattern

`^\/(?:@vite\/client|@fs\/|src\/|node_modules\/|vite\/|_app|static|\.svelte-kit\/generated\/client\/nodes)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:61ce061b66f78b80afeba898cdeb8a84:search

```yaml
regex_id: 61ce061b66f78b80afeba898cdeb8a84
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/slop-scanner.ts:180:10"
```

### Pattern

`^[A-Z]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:63bb8d968ee2db8509b5ce60ddb4f0de:search

```yaml
regex_id: 63bb8d968ee2db8509b5ce60ddb4f0de
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/sqlite/adapter-core.ts:1542:43"
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

## usage_mismatch:65f70acf45364ebba7fe5cd2c925c370:search

```yaml
regex_id: 65f70acf45364ebba7fe5cd2c925c370
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/core/relational-utils.ts:29:20"
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

## usage_mismatch:691341f46a686d0fbbc5a01e19ae58ef:search

```yaml
regex_id: 691341f46a686d0fbbc5a01e19ae58ef
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/content/sync-content-state.server.ts:379:10"
```

### Pattern

`\.(ts|js)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:69ffd1cce29bb3c28ae47897224c31ea:search

```yaml
regex_id: 69ffd1cce29bb3c28ae47897224c31ea
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/services/core/content-sync-service.ts:178:22"
```

### Pattern

`ip$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6a18450b9f44badab1ec432d719c1505:search

```yaml
regex_id: 6a18450b9f44badab1ec432d719c1505
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:52:2"
```

### Pattern

`[/\\]website-token-methods\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6bf49a866447b4af80f7b2a7ff9d8cdf:search

```yaml
regex_id: 6bf49a866447b4af80f7b2a7ff9d8cdf
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/widgets/custom/remote-video/index.ts:51:2"
```

### Pattern

`^https?:\/\/(www\.)?tiktok\.com\/@[\w.-]+\/video\/\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6de48722f657bf6e956332f521b28cd9:search

```yaml
regex_id: 6de48722f657bf6e956332f521b28cd9
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/vite.config.ts:387:56"
```

### Pattern

`\.(ts|js)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:707c509936c55301c4b882a96680f428:search

```yaml
regex_id: 707c509936c55301c4b882a96680f428
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/check-dashboard-widget-packages.mjs:80:7"
```

### Pattern

`^[a-z0-9]+(?:-[a-z0-9]+)*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:71231f469566b6587f75281eaf2173b8:search

```yaml
regex_id: 71231f469566b6587f75281eaf2173b8
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/widgets/custom/remote-video/index.ts:50:2"
```

### Pattern

`^https?:\/\/(www\.)?twitch\.tv\/videos\/\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7229f6fc5dd75debda9f6b1e45e19fa7:search

```yaml
regex_id: 7229f6fc5dd75debda9f6b1e45e19fa7
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:43:2"
```

### Pattern

`[/\\]engine\.server\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:72672ed0fb523c11596e908cf9b99192:search

```yaml
regex_id: 72672ed0fb523c11596e908cf9b99192
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/hook-utils.ts:63:2"
```

### Pattern

`^\/(?:@vite\/client|@fs\/|src\/|node_modules\/|vite\/|_app|static|files\/|favicon\.ico|\.svelte-kit\/generated\/client\/nodes|.*\.(svg|png|jpg|jpeg|gif|css|js|woff|woff2|ttf|eot|map|json))`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:72b073c900122394995a096db4ac3c27:search

```yaml
regex_id: 72b073c900122394995a096db4ac3c27
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:56:2"
```

### Pattern

`[/\\]handlers[/\\]auth\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:72b64b3b523bccec3a9fa55cf6cb76cf:search

```yaml
regex_id: 72b64b3b523bccec3a9fa55cf6cb76cf
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/unified-data-hub/server/ssrf.ts:18:2"
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

## usage_mismatch:749c678a40c2a98cea5481aa879033eb:search

```yaml
regex_id: 749c678a40c2a98cea5481aa879033eb
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:40:2"
```

### Pattern

`[/\\]setup-check\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:772c0028cef203afba4219b5335e89e3:search

```yaml
regex_id: 772c0028cef203afba4219b5335e89e3
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/check-lockfile-sync.ts:71:27"
```

### Pattern

`^(http|file:|git|link:|workspace:)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:77ad5f131d5fe895d2d4d127712ac01e:search

```yaml
regex_id: 77ad5f131d5fe895d2d4d127712ac01e
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/services/sdk/namespaces/auth-namespace.ts:824:19"
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

## usage_mismatch:78b2bad564bb4dfa6d1ebce155872679:search

```yaml
regex_id: 78b2bad564bb4dfa6d1ebce155872679
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/core/page-utils.ts:140:8"
```

### Pattern

`^[a-zA-Z0-9_-]{6,128}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7b2079c188e4ddeac764ee61e7f68a57:search

```yaml
regex_id: 7b2079c188e4ddeac764ee61e7f68a57
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/smart-importer/parsers/wordpress.ts:426:6"
```

### Pattern

`^d:[\d.]+;$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7c6a7a99948f90cdc9d7f930bf7e9442:search

```yaml
regex_id: 7c6a7a99948f90cdc9d7f930bf7e9442
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/widgets/core/rich-text/extensions/image-resize.ts:184:49"
```

### Pattern

`^\d+(%|px)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7e09d71fe872f22e3fa0919735f14da6:search

```yaml
regex_id: 7e09d71fe872f22e3fa0919735f14da6
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/smart-importer/parsers/wordpress.ts:418:6"
```

### Pattern

`^O:\d+:".*":`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7fd3edae64c817e41d1d6169737d5a59:search

```yaml
regex_id: 7fd3edae64c817e41d1d6169737d5a59
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/widgets/widget-factory.ts:210:42"
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

## usage_mismatch:813abea6f727753da2a3f86a6a26b30e:search

```yaml
regex_id: 813abea6f727753da2a3f86a6a26b30e
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/unified-data-hub/server/ssrf.ts:16:2"
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

## usage_mismatch:81918c4e50135444826c0082a9e80f26:search

```yaml
regex_id: 81918c4e50135444826c0082a9e80f26
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/widgets/widget-naming.ts:98:4"
```

### Pattern

`\.(ts|js|mts|cts|svelte)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:832a23f747cafd813005a1ac434aa271:search

```yaml
regex_id: 832a23f747cafd813005a1ac434aa271
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/json-path-filter.ts:94:32"
```

### Pattern

`^([A-Za-z0-9_]+)\[(\d+)\]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:871fb887c215e91e68f22fe242908bbc:search

```yaml
regex_id: 871fb887c215e91e68f22fe242908bbc
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/egress-guard.ts:32:2"
```

### Pattern

`^fc00:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:874023e7af0d3fdd86abbf37a339e0c9:search

```yaml
regex_id: 874023e7af0d3fdd86abbf37a339e0c9
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/schema/field-utils.ts:75:6"
```

### Pattern

`^[0-9]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:882b97bff690b228857acfb9637f596b:search

```yaml
regex_id: 882b97bff690b228857acfb9637f596b
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/core/media-json-path.ts:33:7"
```

### Pattern

`^[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8cf0a0209d4e062eea3e5d80f4314ef1:search

```yaml
regex_id: 8cf0a0209d4e062eea3e5d80f4314ef1
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:60:2"
```

### Pattern

`[/\\]tenant-service\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8d3a07d6e06c3b46f3ef5d53ab43bad3:search

```yaml
regex_id: 8d3a07d6e06c3b46f3ef5d53ab43bad3
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/media/storage-adapters.ts:19:2"
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

## usage_mismatch:8d465a0403d4e6a683c3076f20ddd887:search

```yaml
regex_id: 8d465a0403d4e6a683c3076f20ddd887
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/media/media-utils.ts:29:25"
```

### Pattern

`^(con|prn|aux|nul|com[1-9]|lpt[1-9])(\..*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8f873784b91b7a2ee6cf48e6f35cd26e:search

```yaml
regex_id: 8f873784b91b7a2ee6cf48e6f35cd26e
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:62:2"
```

### Pattern

`[/\\]scheduled-jobs\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8fea822e526d41b5fef676dd6238c4ee:search

```yaml
regex_id: 8fea822e526d41b5fef676dd6238c4ee
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/core/collection-module.ts:256:8"
```

### Pattern

`^collection_workflow_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9066e3fc767628c2552e9d66af4f5a05:search

```yaml
regex_id: 9066e3fc767628c2552e9d66af4f5a05
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/media/storage-adapters.ts:30:2"
```

### Pattern

`^2001:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:963f9fdc0a1d4edfbf22619fe5f08aa5:search

```yaml
regex_id: 963f9fdc0a1d4edfbf22619fe5f08aa5
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/media/storage-adapters.ts:23:2"
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

## usage_mismatch:971cef30e6ee7274f67b71837877afd8:search

```yaml
regex_id: 971cef30e6ee7274f67b71837877afd8
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/mongodb/mongodb-utils.ts:17:2"
```

### Pattern

`^([0-9a-f]{32}|[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:98aee6d13c2ee4b34076f6813bad1ab7:search

```yaml
regex_id: 98aee6d13c2ee4b34076f6813bad1ab7
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:46:2"
```

### Pattern

`[/\\]magic-link\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:998231742fdede4cbf6473ee513374f6:search

```yaml
regex_id: 998231742fdede4cbf6473ee513374f6
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/stores/floating-nav-store.svelte.ts:206:6"
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

## usage_mismatch:99f5a839ddaf33f5bbfe639aca5a5bd6:search

```yaml
regex_id: 99f5a839ddaf33f5bbfe639aca5a5bd6
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/media/storage-adapters.ts:25:2"
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

## usage_mismatch:9b8ca922bbe698ce38cd52d34771eb14:search

```yaml
regex_id: 9b8ca922bbe698ce38cd52d34771eb14
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/stores/floating-nav-store.svelte.ts:207:31"
```

### Pattern

`\/+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9df6845c2e06017c31def1010759953d:search

```yaml
regex_id: 9df6845c2e06017c31def1010759953d
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/log-export.ts:42:56"
```

### Pattern

`\.(\d+)\.gz$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a22e5e57050b6cd891a487b2aef3d48b:search

```yaml
regex_id: a22e5e57050b6cd891a487b2aef3d48b
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/log-export.ts:105:36"
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

## usage_mismatch:a2f5cb15eba7be4e60c1c9ebf89a15e1:search

```yaml
regex_id: a2f5cb15eba7be4e60c1c9ebf89a15e1
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/hooks/handle-redirects.ts:302:23"
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

## usage_mismatch:a37633a5ba8d53929913bb4047a9e90f:search

```yaml
regex_id: a37633a5ba8d53929913bb4047a9e90f
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/run-all-db-matrix.ts:94:25"
```

### Pattern

`^\s*\((fail)\)\s+(.+?)\s*\[([\d.]+)ms\]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a3df5b4590039c281214f6903a3c672a:search

```yaml
regex_id: a3df5b4590039c281214f6903a3c672a
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/security/auth-utils.ts:38:38"
```

### Pattern

`^(\d+)(ms|s|m|h|d|w)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a46cdf59683264d16339d862ce8266b4:search

```yaml
regex_id: a46cdf59683264d16339d862ce8266b4
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/services/token/engine.ts:336:35"
```

### Pattern

`^(\w+)(?:\((.*)\))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a4a5df3803f090c70cf5a41bdea3cb58:search

```yaml
regex_id: a4a5df3803f090c70cf5a41bdea3cb58
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/run-integration.ts:378:25"
```

### Pattern

`^\s*(\d+)\s+pass\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a5b5bc12cf4eaa37fb62b804fc24c88c:search

```yaml
regex_id: a5b5bc12cf4eaa37fb62b804fc24c88c
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/egress-guard.ts:33:2"
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

## usage_mismatch:a6c8286139b8089aec3aa7bd1e192797:search

```yaml
regex_id: a6c8286139b8089aec3aa7bd1e192797
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/services/background/jobs/scheduled-jobs.ts:62:24"
```

### Pattern

`^[0-9a-fA-F]{24}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a7130abbf5f41d38a93b3e1f8104d7a2:search

```yaml
regex_id: a7130abbf5f41d38a93b3e1f8104d7a2
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/routes/api/[...path]/handlers/testing.ts:1596:11"
```

### Pattern

`^[a-zA-Z0-9][a-zA-Z0-9._-]{0,127}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a7e559ec8bd99538af65bf046134f0a9:search

```yaml
regex_id: a7e559ec8bd99538af65bf046134f0a9
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/widgets/custom/remote-video/index.ts:49:2"
```

### Pattern

`^https?:\/\/(www\.)?vimeo\.com\/\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a8855b5a64ae4334a8723bbc9c17e231:search

```yaml
regex_id: a8855b5a64ae4334a8723bbc9c17e231
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/unified-data-hub/server/sql-dialect.ts:15:19"
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

## usage_mismatch:ab3ba85694d342fdda4e673f6aebd1eb:search

```yaml
regex_id: ab3ba85694d342fdda4e673f6aebd1eb
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/widgets/widget-naming.ts:100:24"
```

### Pattern

`\.(ts|js|mts|cts|svelte)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:accc6ca706a677c133648e656047b1d8:search

```yaml
regex_id: accc6ca706a677c133648e656047b1d8
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:64:2"
```

### Pattern

`[/\\]media-namespace\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:acd0a83cc1323cf66439eeffbb9f014a:search

```yaml
regex_id: acd0a83cc1323cf66439eeffbb9f014a
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/security/scanner.ts:113:34"
```

### Pattern

`^([^=]+)=([^;]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b0a86260aa4e16cc2051f68d6f50efbb:search

```yaml
regex_id: b0a86260aa4e16cc2051f68d6f50efbb
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/core/collection-module.ts:255:8"
```

### Pattern

`^collection_plugin_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b0ee0cc22126f964b5332087b252dabb:search

```yaml
regex_id: b0ee0cc22126f964b5332087b252dabb
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/widgets/widget-naming.ts:23:16"
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

## usage_mismatch:b278aab61f4d24b6fc4976d4869ba56e:search

```yaml
regex_id: b278aab61f4d24b6fc4976d4869ba56e
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/check-dashboard-widget-packages.mjs:143:7"
```

### Pattern

`^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b2e176843daf4b6847d93e1fe03357fe:search

```yaml
regex_id: b2e176843daf4b6847d93e1fe03357fe
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/scan-security-risk.ts:495:24"
```

### Pattern

`^[A-Za-z_][A-Za-z0-9_]*\.[A-Za-z_][A-Za-z0-9_]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b386fcbf97c013fbf9b87436d55b7636:search

```yaml
regex_id: b386fcbf97c013fbf9b87436d55b7636
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/config-state.ts:554:4"
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

## usage_mismatch:b409eae0b147ee9b56b33d5c4968b6ba:search

```yaml
regex_id: b409eae0b147ee9b56b33d5c4968b6ba
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/unified-data-hub/server/ssrf.ts:20:2"
```

### Pattern

`^0\.0\.0\.0$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b499bfd6c72a0137067825d3cdec69de:search

```yaml
regex_id: b499bfd6c72a0137067825d3cdec69de
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/benchmark-matrix/generate-ci-markdown.ts:27:28"
```

### Pattern

`ms$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b4a8bd6a88f1fc1c80429d8d4d3de9a3:search

```yaml
regex_id: b4a8bd6a88f1fc1c80429d8d4d3de9a3
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/email.server.ts:117:20"
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

## usage_mismatch:b5388f0f2cf72c5b9f7236f4916df016:search

```yaml
regex_id: b5388f0f2cf72c5b9f7236f4916df016
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/scan-security-risk.ts:218:10"
```

### Pattern

`^(url|uri|href|endpoint|target|host|remoteUrl|remoteUrls|assetUrl|imageUrl|mediaUrl|src|link|callback|redirect|webhook|webhookUrl|externalUrl)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b738d2c6fc78ca035fae50ecd0e32730:search

```yaml
regex_id: b738d2c6fc78ca035fae50ecd0e32730
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:47:2"
```

### Pattern

`[/\\]handle-authorization\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b7b273822150385c3ce54f11e15b1dfb:search

```yaml
regex_id: b7b273822150385c3ce54f11e15b1dfb
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/tenant.ts:79:6"
```

### Pattern

`^(localhost|127\.0\.0\.1|192\.168\.)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b812e85ee88b9832faa0420c49051509:search

```yaml
regex_id: b812e85ee88b9832faa0420c49051509
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/scan-secret-misuse.ts:246:58"
```

### Pattern

`^x{8,}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b89ad79d72ea6400bedee9d5cf02172a:search

```yaml
regex_id: b89ad79d72ea6400bedee9d5cf02172a
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/smart-importer/enterprise.ts:276:42"
```

### Pattern

`^[a-z]{2}(-[A-Z]{2})?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b9dd952b79f18e7b62643e1aa87bd989:search

```yaml
regex_id: b9dd952b79f18e7b62643e1aa87bd989
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/media/media-service.server.ts:42:19"
```

### Pattern

`^#[0-9a-fA-F]{3,8}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ba5ebe301609efb9f07795ca0c3dc447:search

```yaml
regex_id: ba5ebe301609efb9f07795ca0c3dc447
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/mongodb/crud-methods.ts:849:28"
```

### Pattern

`_DELETED_\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bb0270656d93f24c57762f8d9a0b6f64:search

```yaml
regex_id: bb0270656d93f24c57762f8d9a0b6f64
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/widgets/custom/color-picker/index.ts:30:10"
```

### Pattern

`^#[0-9a-f]{6}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bba30b492ac87b2234c87de4195324a1:search

```yaml
regex_id: bba30b492ac87b2234c87de4195324a1
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:66:2"
```

### Pattern

`[/\\]\+layout\.server\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bd3db9518293e85c34c9af1ddebbc31c:search

```yaml
regex_id: bd3db9518293e85c34c9af1ddebbc31c
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/benchmark-matrix/generate-ci-markdown.ts:28:6"
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

## intent_mismatch:bdc8f4ce2cb5a438d25f92351d9c83e9:email

```yaml
regex_id: bdc8f4ce2cb5a438d25f92351d9c83e9
schema_version: "1"
kind: intent_mismatch
corpus: SveltyCMS-SveltyCMS
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/smart-importer/utils/token-mapper.ts:96:12"
```

### Pattern

`\[bloginfo\s+admin_email\]`

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

## usage_mismatch:bdce53a73627b1079919a7c17ca37824:search

```yaml
regex_id: bdce53a73627b1079919a7c17ca37824
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/media/storage-adapters.ts:20:2"
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

## usage_mismatch:bdd223b3e27bcc3d581042886fc781bd:search

```yaml
regex_id: bdd223b3e27bcc3d581042886fc781bd
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/egress-guard.ts:29:2"
```

### Pattern

`^0\.0\.0\.0`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bf54161378f438f0f075772db594beab:search

```yaml
regex_id: bf54161378f438f0f075772db594beab
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/scan-security-risk.ts:595:15"
```

### Pattern

`\.(ts|js|svelte)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bf9deecee367f28493b4dd1e98d984d1:search

```yaml
regex_id: bf9deecee367f28493b4dd1e98d984d1
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/smart-importer/parsers/universal.ts:449:15"
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

## usage_mismatch:c0002b60b6545d2c9866426d4474f078:search

```yaml
regex_id: c0002b60b6545d2c9866426d4474f078
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/egress-guard.ts:30:2"
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

## usage_mismatch:c1266a5c7661f77cad5d7b487fc016a3:search

```yaml
regex_id: c1266a5c7661f77cad5d7b487fc016a3
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/media/storage-adapters.ts:29:2"
```

### Pattern

`^2002:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c265e146b6643e0b994811e1490cb3ee:search

```yaml
regex_id: c265e146b6643e0b994811e1490cb3ee
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/widgets/custom/price/index.ts:28:35"
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

## usage_mismatch:c332f22b1f8d65581d6446946711bcca:search

```yaml
regex_id: c332f22b1f8d65581d6446946711bcca
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/services/core/collection-filter-engine.ts:181:7"
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

## usage_mismatch:c40a399a2300e43530fab7c216cf9a26:search

```yaml
regex_id: c40a399a2300e43530fab7c216cf9a26
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/unified-data-hub/server/ssrf.ts:19:2"
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

## usage_mismatch:c499ab4fc951418862a836aef5f8308b:search

```yaml
regex_id: c499ab4fc951418862a836aef5f8308b
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/media/media-service.server.ts:45:20"
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

## usage_mismatch:c4d4e30f668b2542b793d292baad299f:search

```yaml
regex_id: c4d4e30f668b2542b793d292baad299f
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/file-uploading.ts:74:25"
```

### Pattern

`^\.+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c660a38bdc03854bf919e42585c530f3:search

```yaml
regex_id: c660a38bdc03854bf919e42585c530f3
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/slop-scanner.ts:159:10"
```

### Pattern

`<style\b[^>]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c69678d69afa65504c976b2b040d37ec:search

```yaml
regex_id: c69678d69afa65504c976b2b040d37ec
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/upgrade.ts:440:27"
```

### Pattern

`^(stash@\{\d+\})`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c810556060c8a0fc7479a039b6c1f52c:search

```yaml
regex_id: c810556060c8a0fc7479a039b6c1f52c
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/vite.config.ts:648:18"
```

### Pattern

`^\/ai\/wasm\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c9c2bdf0adf4d6dd2259531da8e786a6:search

```yaml
regex_id: c9c2bdf0adf4d6dd2259531da8e786a6
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/core/relational-system.ts:39:4"
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

## usage_mismatch:cba94584e76df076975fc9d41899559f:search

```yaml
regex_id: cba94584e76df076975fc9d41899559f
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/slop-scanner.ts:140:8"
```

### Pattern

`^\s*````

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ce1036ededff5085bc632da5a798b958:search

```yaml
regex_id: ce1036ededff5085bc632da5a798b958
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/hook-utils.ts:58:2"
```

### Pattern

`\.(?:svg|png|jpg|jpeg|gif|css|js|mjs|cjs|woff|woff2|ttf|eot|map|json|ico|pdf|txt|xml|webmanifest)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cf2d753854de0d977f87fec2a40734b5:search

```yaml
regex_id: cf2d753854de0d977f87fec2a40734b5
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/email.server.ts:181:6"
```

### Pattern

`dummy|example|\.invalid$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cfd1ba5870efc2fb43a5d47e69b6320f:search

```yaml
regex_id: cfd1ba5870efc2fb43a5d47e69b6320f
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/services/media/image-variant-storage.ts:60:34"
```

### Pattern

`variants\/(.+)-(\d+)\.([a-z0-9]+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d0b5f10db52d875e7ab7330eae15797e:search

```yaml
regex_id: d0b5f10db52d875e7ab7330eae15797e
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/schemas.ts:213:4"
```

### Pattern

`^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d269ffaec9273a3ac388ddb5383d34f0:search

```yaml
regex_id: d269ffaec9273a3ac388ddb5383d34f0
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/widgets/core/rich-text/extensions/image-resize.ts:180:61"
```

### Pattern

`^\d+(%|px)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d314a858581eb4009c079eade6ebd669:search

```yaml
regex_id: d314a858581eb4009c079eade6ebd669
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/services/token/modifiers.ts:130:29"
```

### Pattern

`\.([^.]+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d48af29ba4933c08560f686983271a94:search

```yaml
regex_id: d48af29ba4933c08560f686983271a94
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/routes/(app)/[language]/[...collection]/+page.server.ts:95:19"
```

### Pattern

`^[a-f0-9]{32}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d48eb2fb614b9c54347657ebb9e41774:search

```yaml
regex_id: d48eb2fb614b9c54347657ebb9e41774
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:63:2"
```

### Pattern

`[/\\]auth-namespace\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d7871f3d931a7413eae8f8cd77267137:search

```yaml
regex_id: d7871f3d931a7413eae8f8cd77267137
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/slop-scanner.ts:156:10"
```

### Pattern

`<script\b[^>]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d861ec4df04496e5741429fa6dc3bd40:search

```yaml
regex_id: d861ec4df04496e5741429fa6dc3bd40
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/postgresql/postgres-adapter.ts:153:58"
```

### Pattern

`^[A-Za-z0-9_"]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d86ba1543d99de39d04bc25e65934de9:search

```yaml
regex_id: d86ba1543d99de39d04bc25e65934de9
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/sqlite/adapter-core.ts:1539:38"
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

## usage_mismatch:d8bac0fe204da99a43f8063a91254543:search

```yaml
regex_id: d8bac0fe204da99a43f8063a91254543
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/stores/user-store.svelte.ts:16:6"
```

### Pattern

`^\/?Default_User\.svg$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d924133089a67c091ed3d8007b9b8f89:search

```yaml
regex_id: d924133089a67c091ed3d8007b9b8f89
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/core/schema-proxy.ts:44:31"
```

### Pattern

`^[a-z][a-zA-Z0-9_]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dcb799f32c90617e32914ce28cf0edb8:search

```yaml
regex_id: dcb799f32c90617e32914ce28cf0edb8
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:58:2"
```

### Pattern

`[/\\]handlers[/\\]testing\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dde89f4376ce004723442a8a6bb433c6:search

```yaml
regex_id: dde89f4376ce004723442a8a6bb433c6
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/test-smart.ts:531:22"
```

### Pattern

`^\+\s+.*?\b([a-zA-Z_][a-zA-Z0-9_]{3,})\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:de8c4102b067f7801cf0023b2d09669d:search

```yaml
regex_id: de8c4102b067f7801cf0023b2d09669d
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/run-integration.ts:380:25"
```

### Pattern

`^\s*(\d+)\s+fail\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:de97d3d9d98f13cc4c7796b5eff50339:search

```yaml
regex_id: de97d3d9d98f13cc4c7796b5eff50339
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/tenant.ts:67:9"
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

## usage_mismatch:e09351b1faba65e9c0611e6de4c80e4a:search

```yaml
regex_id: e09351b1faba65e9c0611e6de4c80e4a
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/core/sql-adapter-core.ts:607:12"
```

### Pattern

`^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e10158a2a37435a687d88a8c1ea53840:search

```yaml
regex_id: e10158a2a37435a687d88a8c1ea53840
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/smart-importer/parsers/universal.ts:406:34"
```

### Pattern

`^\+\+\+\r?\n([\s\S]*?)\r?\n\+\+\+\r?\n([\s\S]*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e1b4df6e624367217a54aa8ddff81cb6:search

```yaml
regex_id: e1b4df6e624367217a54aa8ddff81cb6
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/services/core/content-sync-service.ts:174:22"
```

### Pattern

`(^|_)phone$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e279feeff1d68685eafc9f6d44c992d4:search

```yaml
regex_id: e279feeff1d68685eafc9f6d44c992d4
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/media/media-utils.ts:129:39"
```

### Pattern

`\.[a-z0-9]{2,8}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e41ccc5b2a5a3f1995d18826f47762fc:search

```yaml
regex_id: e41ccc5b2a5a3f1995d18826f47762fc
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/smart-importer/parsers/universal.ts:176:28"
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

## usage_mismatch:e4b743fdd42007957260323435ed71d4:search

```yaml
regex_id: e4b743fdd42007957260323435ed71d4
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/services/site/site-config.server.ts:26:29"
```

### Pattern

`^\/[a-z]{2}(?:-[a-zA-Z]+)?(?:\/|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e519b41605e4dc11605456024f7ed157:search

```yaml
regex_id: e519b41605e4dc11605456024f7ed157
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/hook-utils.ts:290:38"
```

### Pattern

`^\/api\/token\/([^/]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e565f3ec03292b06780d04f4e9b2e3e6:search

```yaml
regex_id: e565f3ec03292b06780d04f4e9b2e3e6
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/theme-preset-mapper.ts:227:18"
```

### Pattern

`^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e6223e826b8efb51dd3b6c275c36d41b:search

```yaml
regex_id: e6223e826b8efb51dd3b6c275c36d41b
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/vitest.config.ts:92:10"
```

### Pattern

`^graphql$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e66787c3913b82a771cb19fb41b1bf50:search

```yaml
regex_id: e66787c3913b82a771cb19fb41b1bf50
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:48:2"
```

### Pattern

`[/\\]handle-authentication\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:e8d2c41600d98ceb53a5ea21bf6dff0f:email

```yaml
regex_id: e8d2c41600d98ceb53a5ea21bf6dff0f
schema_version: "1"
kind: intent_mismatch
corpus: SveltyCMS-SveltyCMS
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/smart-importer/utils/token-mapper.ts:264:12"
```

### Pattern

`\{\{\s*shop\.email\s*\}\}`

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

## usage_mismatch:e94c654db79ac4e753371e1a5a3e98bd:search

```yaml
regex_id: e94c654db79ac4e753371e1a5a3e98bd
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/smart-importer/parsers/wordpress.ts:409:6"
```

### Pattern

`^a:\d+:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e9caea0177da7dde65741097f8120cde:search

```yaml
regex_id: e9caea0177da7dde65741097f8120cde
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/widgets/widget-naming.ts:20:18"
```

### Pattern

`^[a-z][a-z0-9]*(-[a-z0-9]+)*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:eac2ac418a25e9cccfc61d8a76d3f38a:search

```yaml
regex_id: eac2ac418a25e9cccfc61d8a76d3f38a
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/schemas.ts:288:4"
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

## usage_mismatch:ed2a86bba4e27f597e3b4ec25fd66f3a:search

```yaml
regex_id: ed2a86bba4e27f597e3b4ec25fd66f3a
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/scan-secret-misuse.ts:246:34"
```

### Pattern

`^0{32,}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ee11bb640a8f98b9e0df3ba216e62ba3:search

```yaml
regex_id: ee11bb640a8f98b9e0df3ba216e62ba3
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/smart-importer/parsers/universal.ts:469:32"
```

### Pattern

`^(\w[\w\s]*):\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ee40e9bffe85c06d97de7bc8cf0b9ff8:search

```yaml
regex_id: ee40e9bffe85c06d97de7bc8cf0b9ff8
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/schemas.ts:335:8"
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

## usage_mismatch:f0ae818b68118077f7447e91a0dfd2df:search

```yaml
regex_id: f0ae818b68118077f7447e91a0dfd2df
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:54:2"
```

### Pattern

`[/\\]plugins[/\\]registry\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f3f80699ad5ae49306800fb9d935338c:search

```yaml
regex_id: f3f80699ad5ae49306800fb9d935338c
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/scan-security-risk.ts:84:20"
```

### Pattern

`^[A-Za-z0-9_.[\]'" ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f54d8b92a5c43786bc833f4998b4a379:search

```yaml
regex_id: f54d8b92a5c43786bc833f4998b4a379
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/security/scanner.ts:122:38"
```

### Pattern

`^([^=]+)=([^;]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f59ec1bfeaf75fa76b342d96c23be80e:search

```yaml
regex_id: f59ec1bfeaf75fa76b342d96c23be80e
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/media/storage-adapters.ts:65:35"
```

### Pattern

`^(\d+)\.(\d+)\.(\d+)\.(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f5c621622e44f2f86e5c4c529dd80d27:search

```yaml
regex_id: f5c621622e44f2f86e5c4c529dd80d27
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/benchmark-matrix/generate-ci-markdown.ts:45:42"
```

### Pattern

`^\d+(\.\d+)?(ms)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f6ce4cc6bd647d50e2c4c106a1b45331:search

```yaml
regex_id: f6ce4cc6bd647d50e2c4c106a1b45331
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/egress-guard.ts:24:2"
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

## usage_mismatch:f7e4cbc2c3db60e0851ab1a3d57f7694:search

```yaml
regex_id: f7e4cbc2c3db60e0851ab1a3d57f7694
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/routes/api/graphql/resolvers/collections.ts:73:6"
```

### Pattern

`^[0-9]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f84c85542aa7d9f26ea0d4cb72462305:search

```yaml
regex_id: f84c85542aa7d9f26ea0d4cb72462305
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/auth/totp.ts:73:8"
```

### Pattern

`^[0-9a-fA-F]{64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f90fb7e4d1452093f922eb5b9647ea46:search

```yaml
regex_id: f90fb7e4d1452093f922eb5b9647ea46
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/hooks/handle-content-initialization.ts:24:2"
```

### Pattern

`^(?:\/[a-z]{2,5}(?:-[a-zA-Z]+)?)?\/(api|config|user|dashboard|mediagallery|login|email-previews|admin|setup)(?:\/|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fa3f9db448941e29447894ae35a0ac6b:search

```yaml
regex_id: fa3f9db448941e29447894ae35a0ac6b
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:55:2"
```

### Pattern

`[/\\]plugins[/\\]settings\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fa5dae93198ac78584712cca257d1d6d:search

```yaml
regex_id: fa5dae93198ac78584712cca257d1d6d
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/databases/core/collection-module.ts:257:8"
```

### Pattern

`^collection_redirects_mv$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fa98ce0901d93f41bf44145fccffb541:search

```yaml
regex_id: fa98ce0901d93f41bf44145fccffb541
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/hooks/handle-turbo-pipeline.server.ts:468:41"
```

### Pattern

`^\/[a-z]{2,5}(-[a-zA-Z]+)?\/setup`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:faad89300b669b38ef724978eb0b712b:search

```yaml
regex_id: faad89300b669b38ef724978eb0b712b
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/hooks/handle-turbo-pipeline.server.ts:482:39"
```

### Pattern

`^\/[a-z]{2,5}(-[a-zA-Z]+)?\/setup`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fb230fecccb775d41906ac14d986f823:search

```yaml
regex_id: fb230fecccb775d41906ac14d986f823
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/smart-importer/parsers/universal.ts:451:15"
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

## usage_mismatch:fb28bcb018800355a74a0df85978e51a:search

```yaml
regex_id: fb28bcb018800355a74a0df85978e51a
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/utils/media/storage-adapters.ts:21:2"
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

## usage_mismatch:fb6a9e49291c529f02699a264d7219e7:search

```yaml
regex_id: fb6a9e49291c529f02699a264d7219e7
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/services/core/collection-filter-engine.ts:257:46"
```

### Pattern

`^\d{4}(-\d{2})?(-\d{2})?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fc524e7d365f4c9b7964c4b17cca776d:search

```yaml
regex_id: fc524e7d365f4c9b7964c4b17cca776d
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/benchmark-matrix/reporting.ts:1445:53"
```

### Pattern

`\.json$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fce965a837ec8b6620df236542894be0:search

```yaml
regex_id: fce965a837ec8b6620df236542894be0
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/unified-data-hub/server/postgres-fixture.ts:27:19"
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

## usage_mismatch:fdecf28fd6b19b50b8380b2e3be714c7:search

```yaml
regex_id: fdecf28fd6b19b50b8380b2e3be714c7
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/scripts/lint-tenant-api.ts:53:2"
```

### Pattern

`[/\\]pagespeed[/\\]migrations\.ts$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:feea2611c8e60b46e3c17620bd23bb9e:search

```yaml
regex_id: feea2611c8e60b46e3c17620bd23bb9e
schema_version: "1"
kind: usage_mismatch
corpus: SveltyCMS-SveltyCMS
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/SveltyCMS-SveltyCMS/rules/src/plugins/smart-importer/parsers/universal.ts:395:30"
```

### Pattern

`^---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]*)$`

### Context

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
corpus: SveltyCMS-SveltyCMS
shape: 1
result: planned
ground_truth_status: planned
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

planned

## property:inventory:rc-shape2-missing-keyword:rc-shape2-missing-keyword

```yaml
regex_id: "inventory:rc-shape2-missing-keyword"
schema_version: "1"
kind: property
corpus: SveltyCMS-SveltyCMS
shape: 2
result: planned
ground_truth_status: planned
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

planned

## property:inventory:rc-shape3-capture-truncation:rc-shape3-capture-truncation

```yaml
regex_id: "inventory:rc-shape3-capture-truncation"
schema_version: "1"
kind: property
corpus: SveltyCMS-SveltyCMS
shape: 3
result: planned
ground_truth_status: planned
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

planned

## property:inventory:rc-shape4-escape-image:rc-shape4-escape-image

```yaml
regex_id: "inventory:rc-shape4-escape-image"
schema_version: "1"
kind: property
corpus: SveltyCMS-SveltyCMS
shape: 4
result: planned
ground_truth_status: planned
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

planned

---
schema_version: "1"
corpus: globussoft-crm
findings: 252
---

# globussoft-crm batch findings

## usage_mismatch:0014a21f9fc226c75c798d966c408b5b:search

```yaml
regex_id: 0014a21f9fc226c75c798d966c408b5b
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/travel/BrochureEngine.jsx:583:41"
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

## usage_mismatch:00f537856e99905588856713f5fdc33b:search

```yaml
regex_id: 00f537856e99905588856713f5fdc33b
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/mrzParser.js:295:7"
```

### Pattern

`^[MF<X]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:02244713af0f2c3c64155137e3969668:search

```yaml
regex_id: 02244713af0f2c3c64155137e3969668
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/sanitizeJson.js:113:48"
```

### Pattern

`^[a-z-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:02b3b033b60213637317b74160aaa46a:search

```yaml
regex_id: 02b3b033b60213637317b74160aaa46a
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/scripts/cleanup-seed-pollution-2026-04-27.js:347:8"
```

### Pattern

`^Phone Validation Test`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0473fd4cb00223eb1ae1b6706f3c9961:search

```yaml
regex_id: 0473fd4cb00223eb1ae1b6706f3c9961
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:6215:8"
```

### Pattern

`^_teardown_|^_test_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0490cc7989e47650e5a6bf8caf903402:search

```yaml
regex_id: 0490cc7989e47650e5a6bf8caf903402
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/agentic-orchcrm/packages/tools/src/brochure/render-core.ts:712:22"
```

### Pattern

`^([A-Z][A-Za-z'&./ ]{1,28}):\s*(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:05db712fb560d057ee7f562830bf734e:search

```yaml
regex_id: 05db712fb560d057ee7f562830bf734e
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/wellness/patients/PatientCreateModal.jsx:25:37"
```

### Pattern

`^\+91[6-9]\d{9}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:06c4c7907ded16742c16043dec3ff849:search

```yaml
regex_id: 06c4c7907ded16742c16043dec3ff849
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/scripts/cleanup-seed-pollution-2026-04-27.js:478:27"
```

### Pattern

`\s\d{13}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:06daf010cc2c21e613b8cc3edf64d85a:search

```yaml
regex_id: 06daf010cc2c21e613b8cc3edf64d85a
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/inboundLeadVerification.js:595:8"
```

### Pattern

`^(SENDER_|QUERY_)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:078207768c309665896171d2fa1acce0:search

```yaml
regex_id: 078207768c309665896171d2fa1acce0
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:13015:15"
```

### Pattern

`^image\/(png|jpe?g|gif|webp|svg\+xml)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0799355fabe2bf4e3163feb0279f7c90:search

```yaml
regex_id: 0799355fabe2bf4e3163feb0279f7c90
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/leadJunkFilter.js:56:6"
```

### Pattern

`^[bcdfghjklmnpqrstvwxyz]{5,}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0844c0600a750e7616bbf4984d0cee48:search

```yaml
regex_id: 0844c0600a750e7616bbf4984d0cee48
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:7274:9"
```

### Pattern

`^\d{6}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0b2529c1af4498120eea17938b3f3362:search

```yaml
regex_id: 0b2529c1af4498120eea17938b3f3362
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/travel/TripDetail.jsx:650:36"
```

### Pattern

`^[6-9]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0c680fb4a4f4074832b5609af8d0e4a9:search

```yaml
regex_id: 0c680fb4a4f4074832b5609af8d0e4a9
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/visaLetterService.js:266:8"
```

### Pattern

`^date:\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0eba53e468f0062297b6bcfd7752b259:search

```yaml
regex_id: 0eba53e468f0062297b6bcfd7752b259
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/travel/BrochureEngine.jsx:773:27"
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

## usage_mismatch:0f4f7edd97abe55dbf557037fd3a3dff:search

```yaml
regex_id: 0f4f7edd97abe55dbf557037fd3a3dff
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:12136:9"
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

## usage_mismatch:0f74c116e53c9373a46ae11848b126fd:search

```yaml
regex_id: 0f74c116e53c9373a46ae11848b126fd
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/landing_pages.js:5819:7"
```

### Pattern

`^172\.(1[6-9]|2[0-9]|3[01])\.`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:112d720d8cad08a8900eec7859f8dbc0:search

```yaml
regex_id: 112d720d8cad08a8900eec7859f8dbc0
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_diagnostics.js:1377:25"
```

### Pattern

`^\d{4}-Q[1-4]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:11dd46ad4bf97edd3aa8e198f191accb:search

```yaml
regex_id: 11dd46ad4bf97edd3aa8e198f191accb
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/inboundLeadVerification.js:1000:8"
```

### Pattern

`^(sender_|query_)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:141f37855d46c5805bca27fee8a199a6:search

```yaml
regex_id: 141f37855d46c5805bca27fee8a199a6
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/validators.js:15:17"
```

### Pattern

`^[^\s@,;]+@[^\s@,;]+\.[^\s@,;]{2,}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:15f9561376891baca0d9ac26aa91b2d7:search

```yaml
regex_id: 15f9561376891baca0d9ac26aa91b2d7
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/superadmin/SuperAdminCronMaintenance.jsx:131:27"
```

### Pattern

`^\*\/\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:17ceaadc988b23a8a3fcdfee987b7039:search

```yaml
regex_id: 17ceaadc988b23a8a3fcdfee987b7039
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/wellness/patients/PatientCreateModal.jsx:26:8"
```

### Pattern

`^91[6-9]\d{9}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:19a061ab7312b60797355b678c299d94:search

```yaml
regex_id: 19a061ab7312b60797355b678c299d94
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_diagnostics.js:2686:23"
```

### Pattern

`^(\d+)(?:-|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1a7c09fdc156b8647b8b57aed9cc0e71:search

```yaml
regex_id: 1a7c09fdc156b8647b8b57aed9cc0e71
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:10727:11"
```

### Pattern

`^\d{6}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1a9e9a9e71860c8430b566248ac6b360:search

```yaml
regex_id: 1a9e9a9e71860c8430b566248ac6b360
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/agentic-orchcrm/packages/providers/src/openai-compatible.ts:179:9"
```

### Pattern

`^(gpt-5|o[1-9])`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1bea3d69b0428108c404149f690aa823:search

```yaml
regex_id: 1bea3d69b0428108c404149f690aa823
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/LandingPageWanderluxEditor.jsx:129:9"
```

### Pattern

`^image\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1c13144c736f80382386bfcb87b16707:search

```yaml
regex_id: 1c13144c736f80382386bfcb87b16707
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/landing_pages.js:5823:7"
```

### Pattern

`^fc[0-9a-f]{2}:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1daa3c49b16b77c50cceccb707ead7f7:search

```yaml
regex_id: 1daa3c49b16b77c50cceccb707ead7f7
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/sanitizeJson.js:114:51"
```

### Pattern

`^rgb\(`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2028a69584cc1356b69cbbf8e774091a:search

```yaml
regex_id: 2028a69584cc1356b69cbbf8e774091a
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/passportVizParser.js:73:6"
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

## usage_mismatch:20fe34a128ee57042920e3d2b25be46f:search

```yaml
regex_id: 20fe34a128ee57042920e3d2b25be46f
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/services/pdfRenderer.js:1441:38"
```

### Pattern

`^zylu`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:21eafe21b2a479215789a93c08706abb:search

```yaml
regex_id: 21eafe21b2a479215789a93c08706abb
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/leadJunkFilter.js:42:35"
```

### Pattern

`^[6-9]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:228cb4127da51c7058a22c7579ccd448:search

```yaml
regex_id: 228cb4127da51c7058a22c7579ccd448
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/services/travelExperienceEngine.js:428:20"
```

### Pattern

`^\d{4}-(\d{2})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:22bf55328cf6dcd58771bdaba6ea83d0:search

```yaml
regex_id: 22bf55328cf6dcd58771bdaba6ea83d0
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/scripts/check-migration-safety.js:333:18"
```

### Pattern

`^model\s+(\w+)\s*\{([^}]*)\}`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:237ff7d240dd42f56cdd5c1f158c4e39:search

```yaml
regex_id: 237ff7d240dd42f56cdd5c1f158c4e39
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/services/whatsappWebClient.js:323:10"
```

### Pattern

`^(0|false|no)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:24aabdc7874803e43e67479cc890c694:search

```yaml
regex_id: 24aabdc7874803e43e67479cc890c694
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/leadJunkFilter.js:57:6"
```

### Pattern

`^(test|asdf|qwer|abcd|xxx+|aaa+|fake|none|na|ttt+|fff+|ggg+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:24bd4f20fc252683db36098383b7b650:search

```yaml
regex_id: 24bd4f20fc252683db36098383b7b650
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/services/templates/wanderlux/support.js:190:18"
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

## usage_mismatch:24fa745d86c74e90e3f1d44d75aedacc:search

```yaml
regex_id: 24fa745d86c74e90e3f1d44d75aedacc
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/scripts/cleanup-seed-pollution-2026-04-27.js:348:8"
```

### Pattern

`^Validation Test`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:255eecbfa18e738dea7815bd55fb72cb:search

```yaml
regex_id: 255eecbfa18e738dea7815bd55fb72cb
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_diagnostics.js:1587:22"
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

## usage_mismatch:25ae5ade3e69e0eb6b7fdb917163fc51:search

```yaml
regex_id: 25ae5ade3e69e0eb6b7fdb917163fc51
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/scripts/check-migration-safety.js:316:40"
```

### Pattern

`^([a-z]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:27943f736ed7dd2c22b1e61f2326936a:search

```yaml
regex_id: 27943f736ed7dd2c22b1e61f2326936a
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/whatsapp.js:736:6"
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

## usage_mismatch:2a9c9b56facaf72eaf244aeb73578afd:search

```yaml
regex_id: 2a9c9b56facaf72eaf244aeb73578afd
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/sanitizeJson.js:113:16"
```

### Pattern

`^#(0x)?[0-9a-f]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2b0b78ef85f92e36c50795d59114ded6:search

```yaml
regex_id: 2b0b78ef85f92e36c50795d59114ded6
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/agentic-orchcrm/packages/tools/src/brochure/render-core.ts:538:29"
```

### Pattern

`^(map|route ?map|the route|logo|logo ?placement|design|design ?style)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2b72e52ee89dbe76eedac175973c2374:search

```yaml
regex_id: 2b72e52ee89dbe76eedac175973c2374
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/sanitizeJson.js:115:56"
```

### Pattern

`^justify$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2d4b27af6d6533b2d3b9cfdff57acc12:search

```yaml
regex_id: 2d4b27af6d6533b2d3b9cfdff57acc12
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_invoices.js:2017:7"
```

### Pattern

`^[A-Z]{5}[0-9]{4}[A-Z]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2ddc6f2b5f49bd1d18bf29796e08307c:search

```yaml
regex_id: 2ddc6f2b5f49bd1d18bf29796e08307c
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/agentic-orchcrm/packages/tools/src/brochure/render-core.ts:993:34"
```

### Pattern

`^contact`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2e5bf3f9c811c22d44a009d1da6d874a:search

```yaml
regex_id: 2e5bf3f9c811c22d44a009d1da6d874a
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/whatsapp.js:1719:9"
```

### Pattern

`^[a-z0-9_]{1,512}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2e85204ff72a2b4c714cdb356dd12d44:search

```yaml
regex_id: 2e85204ff72a2b4c714cdb356dd12d44
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/cron/leadScoringEngine.js:177:23"
```

### Pattern

`^(gmail|yahoo|hotmail|outlook|icloud|aol|protonmail|live|msn|me|mail|ymail)\.`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2eb2a3d652718fd6f0d53972d882d57e:search

```yaml
regex_id: 2eb2a3d652718fd6f0d53972d882d57e
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/agentic-orchcrm/packages/tools/src/brochure/render-core.ts:680:22"
```

### Pattern

`^Day\s+\d+\s*[—–-]?\s*([^:]*?):\s*(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2ee2f213c64501f3147b4ba12f63365b:search

```yaml
regex_id: 2ee2f213c64501f3147b4ba12f63365b
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/mrzParser.js:292:7"
```

### Pattern

`^\d{8}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3044b6ba29fba35f13840691b14ea551:search

```yaml
regex_id: 3044b6ba29fba35f13840691b14ea551
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/scripts/check-migration-safety.js:343:27"
```

### Pattern

`^(\w+)\s+([\w()]+)(\??)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:310a2373efd47eaf67082c1140f9d0f3:search

```yaml
regex_id: 310a2373efd47eaf67082c1140f9d0f3
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/superadmin/SuperAdminCronMaintenance.jsx:146:6"
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

## usage_mismatch:31ffaf17531724e231fce306be05b3f5:search

```yaml
regex_id: 31ffaf17531724e231fce306be05b3f5
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/landing_pages.js:3577:21"
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

## usage_mismatch:329b53b38017ad4cb0e2e535ebc0223b:search

```yaml
regex_id: 329b53b38017ad4cb0e2e535ebc0223b
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/csvEntities.js:1108:18"
```

### Pattern

`^[^@\s]+@[^@\s]+\.[^@\s]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:353b9a363d5d4393cc3d1d13f29a28e4:search

```yaml
regex_id: 353b9a363d5d4393cc3d1d13f29a28e4
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_commission_profiles.js:639:23"
```

### Pattern

`^\d{4}-(0[1-9]|1[0-2])$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3774a52d267b77f2c962eed16d6d2509:search

```yaml
regex_id: 3774a52d267b77f2c962eed16d6d2509
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/services/whatsappWebClient.js:1486:35"
```

### Pattern

`^\d{6,15}@c\.us$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3812f6fdb9c2a1bf1dabc6128bb676b3:search

```yaml
regex_id: 3812f6fdb9c2a1bf1dabc6128bb676b3
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/services/landingPageRenderer.js:63:34"
```

### Pattern

`^([a-z][a-z0-9+.-]*):`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:381b6ae9e8c8523d865fd6ec8d1d9a88:search

```yaml
regex_id: 381b6ae9e8c8523d865fd6ec8d1d9a88
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/services/pdfRenderer.js:1290:37"
```

### Pattern

`^data:image\/(png|jpeg|jpg);base64,(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:38cc7d78686b2b5980e2bb6b79fd4af0:search

```yaml
regex_id: 38cc7d78686b2b5980e2bb6b79fd4af0
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/services/landingPageRenderer.js:73:29"
```

### Pattern

`^data:image\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3943af24ca0346bc030733508c7b950f:search

```yaml
regex_id: 3943af24ca0346bc030733508c7b950f
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_diagnostics.js:1167:23"
```

### Pattern

`^\d{4}-(0[1-9]|1[0-2])$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3a42c40e760c51c44e1c562d1bc2c06e:search

```yaml
regex_id: 3a42c40e760c51c44e1c562d1bc2c06e
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/validators.js:239:27"
```

### Pattern

`^(tenantId|id)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3a8128d289361a49233970266ed6b477:search

```yaml
regex_id: 3a8128d289361a49233970266ed6b477
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/Contacts.jsx:417:20"
```

### Pattern

`\.xlsx?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3bf09691ba3b050d3ed9c7bab397ee1f:search

```yaml
regex_id: 3bf09691ba3b050d3ed9c7bab397ee1f
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/validators.js:247:27"
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

## usage_mismatch:3dbb03aa2fa09a26beaaadf886e2684d:search

```yaml
regex_id: 3dbb03aa2fa09a26beaaadf886e2684d
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/services/templates/wanderlux/support.js:189:17"
```

### Pattern

`^[A-Za-z_$][A-Za-z0-9_$]*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3edb1d60b5c3b6e0be2bdd245308cf86:search

```yaml
regex_id: 3edb1d60b5c3b6e0be2bdd245308cf86
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:7379:9"
```

### Pattern

`^\d{6}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:40c1af869a6a40c0024a0addeefa4b60:email

```yaml
regex_id: 40c1af869a6a40c0024a0addeefa4b60
schema_version: "1"
kind: intent_mismatch
corpus: globussoft-crm
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/Reports.jsx:367:47"
```

### Pattern

`th><th style={thStyle}>Email<`

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

## usage_mismatch:41c2ca6d8d65f34990df4f525d43be45:search

```yaml
regex_id: 41c2ca6d8d65f34990df4f525d43be45
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_commission_profiles.js:2819:23"
```

### Pattern

`^\d{4}-(0[1-9]|1[0-2])$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:441a3517d3a9c3effe56fd876ced1581:search

```yaml
regex_id: 441a3517d3a9c3effe56fd876ced1581
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/LandingPageBuilder.jsx:2916:49"
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

## usage_mismatch:44309b07e98f724d9409b104f456756a:search

```yaml
regex_id: 44309b07e98f724d9409b104f456756a
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_microsites.js:169:22"
```

### Pattern

`^\.(png|jpe?g|webp)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:449de65aa906083ac445064ca6202b46:search

```yaml
regex_id: 449de65aa906083ac445064ca6202b46
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/superadmin/SuperAdminCronMaintenance.jsx:150:6"
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

## usage_mismatch:44f73df5679b683a74f1105bb32c996e:search

```yaml
regex_id: 44f73df5679b683a74f1105bb32c996e
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/LandingPageWanderluxEditor.jsx:194:9"
```

### Pattern

`^video\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:47ba382161366ca929bf6b535efd1b8b:search

```yaml
regex_id: 47ba382161366ca929bf6b535efd1b8b
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/agentic-orchcrm/packages/tools/src/brochure/render-core.ts:895:2"
```

### Pattern

`^(create a premium.*|overview|agency|contact|website|address|social|trip|category|target audience|tagline|group size|duration|accent ?colou?r?|accent|route|map|logo placement|design style|about the experience|day[ -]?by[ -]?day itinerary|itinerary|pricing|price)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4a1672ff850049e840db124ace7ed963:search

```yaml
regex_id: 4a1672ff850049e840db124ace7ed963
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/landing_pages.js:5817:7"
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

## usage_mismatch:4a84fe155aa7d066ddf8729d4a40ae5c:search

```yaml
regex_id: 4a84fe155aa7d066ddf8729d4a40ae5c
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/agentic-orchcrm/packages/tools/src/brochure/render-core.ts:863:22"
```

### Pattern

`^([A-Z][A-Z0-9 &',./()\-]{2,48}):\s*(.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4c8e87d1d61a1b59135185af10a283e0:search

```yaml
regex_id: 4c8e87d1d61a1b59135185af10a283e0
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/guardTeeContent.js:217:23"
```

### Pattern

`^([^.]+)\.(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4cc094cdaac03a129f49c26f05245863:search

```yaml
regex_id: 4cc094cdaac03a129f49c26f05245863
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/landing_pages.js:5825:7"
```

### Pattern

`^fd[0-9a-f]{2}:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4cd133d8ff466e3728fbb0f5eaf90e69:search

```yaml
regex_id: 4cd133d8ff466e3728fbb0f5eaf90e69
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:14398:10"
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

## usage_mismatch:4dfc810e9aa9fe9d270dc3ed4228dfb8:search

```yaml
regex_id: 4dfc810e9aa9fe9d270dc3ed4228dfb8
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_quotes.js:1921:22"
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

## usage_mismatch:52b1b507c7412a2205785535123bb458:search

```yaml
regex_id: 52b1b507c7412a2205785535123bb458
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:3895:9"
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

## usage_mismatch:52c6b96172e585c3917707153c9419be:search

```yaml
regex_id: 52c6b96172e585c3917707153c9419be
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_invoices.js:2545:23"
```

### Pattern

`^\d{4}-Q[1-4]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:540d5c724367777da6418ecbc2311d90:search

```yaml
regex_id: 540d5c724367777da6418ecbc2311d90
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/landing_pages.js:439:21"
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

## usage_mismatch:547874f8e560a10dad60aafdb3c1a2b5:search

```yaml
regex_id: 547874f8e560a10dad60aafdb3c1a2b5
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/services/pdfRenderer.js:346:25"
```

### Pattern

`^\s*\[ZYLU-#?(\d+)\]\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:55797ff8d0011ada1c2b54b5681d4664:search

```yaml
regex_id: 55797ff8d0011ada1c2b54b5681d4664
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/landing_pages.js:5821:7"
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

## usage_mismatch:55f5bb297d5b36e8aae8c34f9c6a88a1:search

```yaml
regex_id: 55f5bb297d5b36e8aae8c34f9c6a88a1
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/GmailInbox.jsx:293:35"
```

### Pattern

`^re:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:561d7648853e457f3cdf184173d62fe9:search

```yaml
regex_id: 561d7648853e457f3cdf184173d62fe9
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/travel/MarketingFlyerStudio.jsx:693:27"
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

## usage_mismatch:56edd303f971171dd78f75c5cac077cd:search

```yaml
regex_id: 56edd303f971171dd78f75c5cac077cd
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_quotes.js:1633:25"
```

### Pattern

`^\d{4}-Q[1-4]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:578f327b86501aed8d53d3f0afb2ec02:search

```yaml
regex_id: 578f327b86501aed8d53d3f0afb2ec02
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/mrzParser.js:263:7"
```

### Pattern

`^\d{8}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:57f5f289fafa963a44f51b6ca48b2975:email

```yaml
regex_id: 57f5f289fafa963a44f51b6ca48b2975
schema_version: "1"
kind: intent_mismatch
corpus: globussoft-crm
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/visaLetterService.js:361:51"
```

### Pattern

`\s*\/\s*`

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

## usage_mismatch:58672a4f1f277068c8628f9c5fc32ebe:search

```yaml
regex_id: 58672a4f1f277068c8628f9c5fc32ebe
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/mrzParser.js:116:22"
```

### Pattern

`^P[A-Z<]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:59c4878bf37f0143b83c6af7c6c368e8:search

```yaml
regex_id: 59c4878bf37f0143b83c6af7c6c368e8
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/developer.js:229:4"
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

## usage_mismatch:5afc4f820b9dbd376ab4374cd31b122a:search

```yaml
regex_id: 5afc4f820b9dbd376ab4374cd31b122a
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:8146:18"
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

## usage_mismatch:5ea75340eea64cf03084d08715f07874:search

```yaml
regex_id: 5ea75340eea64cf03084d08715f07874
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/travel/BrochureEngine.jsx:589:31"
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

## usage_mismatch:5f4f3d57f4972adf57cdeba262b405df:search

```yaml
regex_id: 5f4f3d57f4972adf57cdeba262b405df
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/travel/PublicTripMicrosite.jsx:439:20"
```

### Pattern

`^H[1-3]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:60a0121006412117f3d91d9d5db74940:search

```yaml
regex_id: 60a0121006412117f3d91d9d5db74940
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:9954:9"
```

### Pattern

`^[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6392ac748c1bd4ac1b639285d07eeb5e:search

```yaml
regex_id: 6392ac748c1bd4ac1b639285d07eeb5e
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/agentic-orchcrm/packages/tools/src/brochure/render-core.ts:843:42"
```

### Pattern

`^[•\-*]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:663f7a9bea6155e46b6dd905cf37cb77:search

```yaml
regex_id: 663f7a9bea6155e46b6dd905cf37cb77
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/sanitizeJson.js:123:17"
```

### Pattern

`^\d+(\.\d+)?(px|pt|em|rem|%)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:669135fe6817542deaf9636ccbbdd942:search

```yaml
regex_id: 669135fe6817542deaf9636ccbbdd942
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/Channels.jsx:68:16"
```

### Pattern

`^[A-Za-z0-9 \r\n@£$¥èéùìòÇØøÅåΔ_ΦΓΛΩΠΨΣΘΞ^{}\\[\]~|€!"#%&'()*+,\-./:;<=>?¡ÄÖÑÜ§¿äöñüà]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:66bb82720fca592a50748a1cab7af6df:search

```yaml
regex_id: 66bb82720fca592a50748a1cab7af6df
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/landing_pages.js:5811:7"
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

## usage_mismatch:6865fafd25a5bfe98c690101f66cd081:search

```yaml
regex_id: 6865fafd25a5bfe98c690101f66cd081
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:10051:6"
```

### Pattern

`^(smoke-test|e2e[-_ ]|test[-_ ]|qa[-_ ]|dev[-_ ])`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:68c6fdc4637e54326ae07143e611f2ba:search

```yaml
regex_id: 68c6fdc4637e54326ae07143e611f2ba
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/sanitizeJson.js:115:33"
```

### Pattern

`^right$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6ab1ea2928c7b1bf72f6d168a0fbc3ce:search

```yaml
regex_id: 6ab1ea2928c7b1bf72f6d168a0fbc3ce
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_microsites.js:1387:9"
```

### Pattern

`^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6abe752fd78ed209628d873b9810ed86:search

```yaml
regex_id: 6abe752fd78ed209628d873b9810ed86
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/visaLetterService.js:271:8"
```

### Pattern

`^to,?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6bf3d2399feb3c82dbee624c872f2b59:search

```yaml
regex_id: 6bf3d2399feb3c82dbee624c872f2b59
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/GmailInbox.jsx:19:29"
```

### Pattern

`[.,!?;:)\]}'"]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6c57564c0454b4c080049eb34ff1983c:search

```yaml
regex_id: 6c57564c0454b4c080049eb34ff1983c
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_invoices.js:1075:8"
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

## usage_mismatch:6ca6f967529af6f49b5099b55dfa67d9:search

```yaml
regex_id: 6ca6f967529af6f49b5099b55dfa67d9
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/utils/landingPageUtils.js:34:29"
```

### Pattern

`^data:image\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6eb199ac93a2c0127da1ec9777a2998a:search

```yaml
regex_id: 6eb199ac93a2c0127da1ec9777a2998a
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/sanitizeJson.js:118:23"
```

### Pattern

`^(italic|normal)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6ffd71f3a3a6aea7cd94a535e48df578:search

```yaml
regex_id: 6ffd71f3a3a6aea7cd94a535e48df578
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/services/pdfRenderer.js:348:25"
```

### Pattern

`^\s*(chief complaint|diagnosis|investigations?|advice|advice\/referrals?|status|notes?)\s*:\s*(.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:70deea2411438d9cb3d4814a4f875398:search

```yaml
regex_id: 70deea2411438d9cb3d4814a4f875398
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/sanitizeJson.js:117:24"
```

### Pattern

`^(bold|bolder|lighter|normal|\d{3})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:70fa3b2aaee468aa515d246bf95782e2:search

```yaml
regex_id: 70fa3b2aaee468aa515d246bf95782e2
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:13031:8"
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

## usage_mismatch:71eaf0494b9bc6318ed74085d130cd67:search

```yaml
regex_id: 71eaf0494b9bc6318ed74085d130cd67
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/services/templates/wanderlux/support.js:354:28"
```

### Pattern

`^\s*\{\{([\s\S]+?)\}\}\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:72dcb5f19391a71a2e13c3bfb0c20f21:search

```yaml
regex_id: 72dcb5f19391a71a2e13c3bfb0c20f21
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/travel/BrochureEngine.jsx:510:11"
```

### Pattern

`^image\/(png|jpe?g|webp|gif)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:731a63b5f12c73cec6af4faf02839c87:search

```yaml
regex_id: 731a63b5f12c73cec6af4faf02839c87
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/sanitizeJson.js:120:17"
```

### Pattern

`^\d+(\.\d+)?(px|pt|em|rem|%)?(\s+\d+(\.\d+)?(px|pt|em|rem|%)?){0,3}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:757f796512c9f21328abe42f22d5f8e2:search

```yaml
regex_id: 757f796512c9f21328abe42f22d5f8e2
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/Contacts.jsx:77:29"
```

### Pattern

`^[=+\-@\t\r]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7729c524e90c2c8af7bb7be1cac0ab91:search

```yaml
regex_id: 7729c524e90c2c8af7bb7be1cac0ab91
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/sanitizeJson.js:113:38"
```

### Pattern

`^rgb\(`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:825516bdf627d8b30ac392aba2b3ce05:search

```yaml
regex_id: 825516bdf627d8b30ac392aba2b3ce05
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_microsites.js:892:25"
```

### Pattern

`^\d{4}-Q[1-4]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:827823e91818ff43a6d4034fe0acd56e:search

```yaml
regex_id: 827823e91818ff43a6d4034fe0acd56e
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_microsites.js:1054:22"
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

## usage_mismatch:832dfc20c52a39da0ea48574373b40e6:search

```yaml
regex_id: 832dfc20c52a39da0ea48574373b40e6
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/landingPageGuard.js:107:18"
```

### Pattern

`^https?:\/\/|^\/uploads\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:83dd26fd3817346b0a4867bbdf9752b4:search

```yaml
regex_id: 83dd26fd3817346b0a4867bbdf9752b4
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:8064:19"
```

### Pattern

`^\d{2}:\d{2}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:847db6ea27ba697d83b391be4d841d09:search

```yaml
regex_id: 847db6ea27ba697d83b391be4d841d09
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/sanitizeJson.js:124:69"
```

### Pattern

`^none$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:854a4f74b672b2d91e650439e3f9865f:search

```yaml
regex_id: 854a4f74b672b2d91e650439e3f9865f
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/mrzParser.js:123:6"
```

### Pattern

`^P[A-Z<]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:860418827083b1e3916867c8ce6bb167:search

```yaml
regex_id: 860418827083b1e3916867c8ce6bb167
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/scripts/cleanup-seed-pollution-2026-04-27.js:252:13"
```

### Pattern

`^Lifecycle\s+\d`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:863ca7e5123e7d76ffc47d2f3d5cfb21:search

```yaml
regex_id: 863ca7e5123e7d76ffc47d2f3d5cfb21
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/CustomerRegister.jsx:138:24"
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

## usage_mismatch:8670d7829dcc140a48ec6f0df767ebf5:search

```yaml
regex_id: 8670d7829dcc140a48ec6f0df767ebf5
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/landing_pages.js:5815:7"
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

## usage_mismatch:878f879b2d75c093278177d6cf45d9d2:search

```yaml
regex_id: 878f879b2d75c093278177d6cf45d9d2
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/developer.js:223:4"
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

## usage_mismatch:87be804eb405904785c555c88189e410:search

```yaml
regex_id: 87be804eb405904785c555c88189e410
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/visaLetterService.js:267:40"
```

### Pattern

`^date:\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:888a520b43eff6d95858cba12aed5548:search

```yaml
regex_id: 888a520b43eff6d95858cba12aed5548
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_diagnostics.js:2733:9"
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

## usage_mismatch:89486662b0b4f1f8e775a89903948d73:search

```yaml
regex_id: 89486662b0b4f1f8e775a89903948d73
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_invoices.js:2846:20"
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

## usage_mismatch:89e8775efbe935fef980b1c20f68476b:search

```yaml
regex_id: 89e8775efbe935fef980b1c20f68476b
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/sanitizeJson.js:119:28"
```

### Pattern

`^(underline|none|line-through)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8ad91acd7cd7d17ac71bad49df724e41:search

```yaml
regex_id: 8ad91acd7cd7d17ac71bad49df724e41
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/sanitizeJson.js:116:22"
```

### Pattern

`^\d+(\.\d+)?(px|pt|em|rem|%)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8c9c94e056dd6cd9535c3668308a18ca:search

```yaml
regex_id: 8c9c94e056dd6cd9535c3668308a18ca
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/leadJunkFilter.js:58:6"
```

### Pattern

`^[a-z]\.?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8dc0d50ededa53a987cdbd68d78ba511:search

```yaml
regex_id: 8dc0d50ededa53a987cdbd68d78ba511
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/sanitizeJson.js:122:16"
```

### Pattern

`^\d+(\.\d+)?(px|pt|em|rem|%)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8dd9a4c2318dbc4805bf947c762f3e4c:search

```yaml
regex_id: 8dd9a4c2318dbc4805bf947c762f3e4c
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/leadJunkFilter.js:54:6"
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

## usage_mismatch:8decdd743df8970513cd9cb3822dc090:search

```yaml
regex_id: 8decdd743df8970513cd9cb3822dc090
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_itineraries.js:3466:38"
```

### Pattern

`^[A-Z0-9]{2}`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8edf6976187f013181636c3ad21b8a16:search

```yaml
regex_id: 8edf6976187f013181636c3ad21b8a16
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_microsites.js:1544:9"
```

### Pattern

`^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9076c03fd86f0dc31269c1e9071f71a0:search

```yaml
regex_id: 9076c03fd86f0dc31269c1e9071f71a0
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:1035:2"
```

### Pattern

`^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:90a04171340074eb160d2cb8f1481c78:search

```yaml
regex_id: 90a04171340074eb160d2cb8f1481c78
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:15258:10"
```

### Pattern

`^_teardown_|^_test_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:90f143ab17309d940172da5dc8448e5b:search

```yaml
regex_id: 90f143ab17309d940172da5dc8448e5b
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:1910:10"
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

## usage_mismatch:93ee83de210fc9db432ba6a651b05e62:search

```yaml
regex_id: 93ee83de210fc9db432ba6a651b05e62
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/server.js:1074:4"
```

### Pattern

`^\/travel\/quotes\/public\/quote\/[^/]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:94be2c0ad28979eebf85da84b327676f:search

```yaml
regex_id: 94be2c0ad28979eebf85da84b327676f
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:10313:11"
```

### Pattern

`^\d{6}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9508c34c6f82d0e722be4b01a575c913:search

```yaml
regex_id: 9508c34c6f82d0e722be4b01a575c913
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_itineraries.js:1220:23"
```

### Pattern

`^\d{4}-Q[1-4]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:9742dc76390b5862d06831a7daf16048:email

```yaml
regex_id: 9742dc76390b5862d06831a7daf16048
schema_version: "1"
kind: intent_mismatch
corpus: globussoft-crm
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/Reports.jsx:367:171"
```

### Pattern

`th><th style={thStyle}>Assigned To<`

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

## usage_mismatch:9965f00dbde3fe73c28ab55111fcdfda:search

```yaml
regex_id: 9965f00dbde3fe73c28ab55111fcdfda
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/inboundLeadVerification.js:115:9"
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

## usage_mismatch:9a5cb14dbf1bebce6e1fba082e682a27:search

```yaml
regex_id: 9a5cb14dbf1bebce6e1fba082e682a27
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/whatsapp.js:82:6"
```

### Pattern

`^[0-9]{10,15}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9a7e0316307b89202eb8b206856054f2:search

```yaml
regex_id: 9a7e0316307b89202eb8b206856054f2
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/agentic-orchcrm/packages/tools/src/brochure/render-core.ts:1004:34"
```

### Pattern

`call ?to ?action|^cta$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9af56ba51eaa0571185f0325b16ba619:search

```yaml
regex_id: 9af56ba51eaa0571185f0325b16ba619
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/sanitizeJson.js:114:61"
```

### Pattern

`^[a-z-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9cdeda51b66e2dbe682cc1c95f1ed134:search

```yaml
regex_id: 9cdeda51b66e2dbe682cc1c95f1ed134
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/services/passportOcrClient.js:337:26"
```

### Pattern

`^[A-Z0-9<]{1,9}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9da06faeb27ca191126f3d4898e667bb:search

```yaml
regex_id: 9da06faeb27ca191126f3d4898e667bb
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/server.js:1095:4"
```

### Pattern

`^\/brand-kits\/by-subbrand\/[^/]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9e80fde8e30438be38f56467d288e456:search

```yaml
regex_id: 9e80fde8e30438be38f56467d288e456
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:11283:18"
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

## usage_mismatch:a053b661b46434be707204c2652f33b3:search

```yaml
regex_id: a053b661b46434be707204c2652f33b3
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:10673:18"
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

## usage_mismatch:a1233a5a1b603087c9803469be57e6dd:search

```yaml
regex_id: a1233a5a1b603087c9803469be57e6dd
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/server.js:1654:8"
```

### Pattern

`^glbs_[A-Za-z0-9_-]{8,}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a1eae55d79f2a5cc2acc07fb75b0560f:search

```yaml
regex_id: a1eae55d79f2a5cc2acc07fb75b0560f
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_microsites.js:176:8"
```

### Pattern

`^image\/(png|jpe?g|webp)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a39906095f8c6d646ac0bf6df1d704ee:search

```yaml
regex_id: a39906095f8c6d646ac0bf6df1d704ee
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/mrzParser.js:66:7"
```

### Pattern

`^\d{6}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a41bda5e71a535305f1b0993b54da208:search

```yaml
regex_id: a41bda5e71a535305f1b0993b54da208
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_itineraries.js:946:21"
```

### Pattern

`^\d{4}-(0[1-9]|1[0-2])$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a450b4e0d5bc519e4cee50d8b3202f37:search

```yaml
regex_id: a450b4e0d5bc519e4cee50d8b3202f37
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/developer.js:224:4"
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

## usage_mismatch:a6cd26d9fb7fd49341b535dc296cb2fb:search

```yaml
regex_id: a6cd26d9fb7fd49341b535dc296cb2fb
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:11572:37"
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

## usage_mismatch:a9233e0ed7d37b2407fbb9d9d32b375a:search

```yaml
regex_id: a9233e0ed7d37b2407fbb9d9d32b375a
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/sanitizeJson.js:124:17"
```

### Pattern

`^\d+px\s+(solid|dashed|dotted)\s+#?[0-9a-fA-F]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a95cacad5ea7a06cb97b17b78561b931:search

```yaml
regex_id: a95cacad5ea7a06cb97b17b78561b931
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:13191:7"
```

### Pattern

`^#[0-9a-fA-F]{6}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:aa2da71fc9a219748cef970bd69e25a0:search

```yaml
regex_id: aa2da71fc9a219748cef970bd69e25a0
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/landing_pages.js:5813:7"
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

## usage_mismatch:ab02ce5da5230b3fb2f67d8c53709373:search

```yaml
regex_id: ab02ce5da5230b3fb2f67d8c53709373
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/developer.js:231:4"
```

### Pattern

`^fd[0-9a-f]{2}:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ac0e608c9b7f8dda407fa9dd983bf3ac:search

```yaml
regex_id: ac0e608c9b7f8dda407fa9dd983bf3ac
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/superadmin/SuperAdminCronMaintenance.jsx:122:6"
```

### Pattern

`^\*\/\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ad1753faa8c6e9283a9de6f98aa74bc6:search

```yaml
regex_id: ad1753faa8c6e9283a9de6f98aa74bc6
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:10665:9"
```

### Pattern

`^(\+?91)?[6-9]\d{9}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ad7dd80986121c77b070c2dd2048999e:search

```yaml
regex_id: ad7dd80986121c77b070c2dd2048999e
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/leadJunkFilter.js:43:62"
```

### Pattern

`^[6-9]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:afcd0757cbf97a2f9694bf214a6046ec:search

```yaml
regex_id: afcd0757cbf97a2f9694bf214a6046ec
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/LandingPageBuilder.jsx:1768:49"
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

## usage_mismatch:afdf478f4b8f10338a30efdcc345963f:search

```yaml
regex_id: afdf478f4b8f10338a30efdcc345963f
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/validators.js:179:15"
```

### Pattern

`^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][0-9][Z][0-9A-Z]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b1e131e9df0192cdfedb0484c9701b82:search

```yaml
regex_id: b1e131e9df0192cdfedb0484c9701b82
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/wellness/patients/PatientCreateModal.jsx:20:27"
```

### Pattern

`^(\+91)?[6-9]\d{9}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b2121b004a46ecc87dcb3b9e280728bc:search

```yaml
regex_id: b2121b004a46ecc87dcb3b9e280728bc
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:13037:33"
```

### Pattern

`\/(?:api\/)?uploads\/(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b27b30f83c54382210d6a3b2cff26f90:search

```yaml
regex_id: b27b30f83c54382210d6a3b2cff26f90
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_microsites.js:1180:9"
```

### Pattern

`^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b35b3a11187eb63e91d7be45ebb19071:search

```yaml
regex_id: b35b3a11187eb63e91d7be45ebb19071
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/LandingPageBuilder.jsx:2492:20"
```

### Pattern

`^https?:\/\/(?:www\.)?youtube\.com\/embed\/([A-Za-z0-9_-]{6,})`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b4efdf8c3afea8d7783d3976a209feb6:search

```yaml
regex_id: b4efdf8c3afea8d7783d3976a209feb6
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/superadmin/SuperAdminCronMaintenance.jsx:131:6"
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

## usage_mismatch:b6b2310eab757a65addd134dc69ce3ed:search

```yaml
regex_id: b6b2310eab757a65addd134dc69ce3ed
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_invoices.js:2246:21"
```

### Pattern

`^\d{4}-(0[1-9]|1[0-2])$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b7950a47fafb76acae75d43f89c70f5d:search

```yaml
regex_id: b7950a47fafb76acae75d43f89c70f5d
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/server.js:1079:4"
```

### Pattern

`^\/travel\/quotes\/public\/quote\/[^/]+\/(accept|reject|counter)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ba3f288c5892d91949c2504e6fd685e3:search

```yaml
regex_id: ba3f288c5892d91949c2504e6fd685e3
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/utils/landingPageUtils.js:28:34"
```

### Pattern

`^([a-z][a-z0-9+.-]*):`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bb71db8823d915f94af0f18793690625:search

```yaml
regex_id: bb71db8823d915f94af0f18793690625
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/sanitizeJson.js:114:29"
```

### Pattern

`^#(0x)?[0-9a-f]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bb77440fd61701a468bd77419d8313dc:search

```yaml
regex_id: bb77440fd61701a468bd77419d8313dc
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/mrzParser.js:291:7"
```

### Pattern

`^[A-Z]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bb9c9c194467e28dc2cc8eef9bd7edf5:search

```yaml
regex_id: bb9c9c194467e28dc2cc8eef9bd7edf5
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/LandingPageBuilder.jsx:602:37"
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

## usage_mismatch:bbc10f54dfd6c8b040b8ab03e15bd0fc:search

```yaml
regex_id: bbc10f54dfd6c8b040b8ab03e15bd0fc
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/services/travelExperienceEngine.js:634:10"
```

### Pattern

`^stub-`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bca6363d3e2aa6fbb05317df17fe4d38:search

```yaml
regex_id: bca6363d3e2aa6fbb05317df17fe4d38
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/travel/TripDetail.jsx:651:63"
```

### Pattern

`^[6-9]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bcc0cd556be606afa5f6f24659cde705:search

```yaml
regex_id: bcc0cd556be606afa5f6f24659cde705
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/server.js:1721:11"
```

### Pattern

`^glbs_[A-Za-z0-9_-]{8,}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bef495856954efb6c6acdaf2679602f1:search

```yaml
regex_id: bef495856954efb6c6acdaf2679602f1
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/LandingPageBuilder.jsx:2494:20"
```

### Pattern

`^https?:\/\/(?:www\.)?vimeo\.com\/(\d+)(?:\/([A-Za-z0-9]+))?`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bf0d1f6a69ab92b5cbf3fef5a0316de2:search

```yaml
regex_id: bf0d1f6a69ab92b5cbf3fef5a0316de2
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/scripts/cleanup-seed-pollution-2026-04-27.js:459:13"
```

### Pattern

`^spam-\d`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bf517ab6d38d97535c6ee133f3a128b3:search

```yaml
regex_id: bf517ab6d38d97535c6ee133f3a128b3
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/Contacts.jsx:75:17"
```

### Pattern

`^[^\s@,;]+@[^\s@,;]+\.[^\s@,;]{2,}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bf84ed1759487ca7285f86a27d55304b:search

```yaml
regex_id: bf84ed1759487ca7285f86a27d55304b
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/agentic-orchcrm/packages/tools/src/brochure/render-core.ts:45:7"
```

### Pattern

`^[0-9a-fA-F]{6}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c10a801a5fcb2990ea784656e2d92c9f:search

```yaml
regex_id: c10a801a5fcb2990ea784656e2d92c9f
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/LandingPageBuilder.jsx:2490:20"
```

### Pattern

`^https?:\/\/(?:www\.|m\.)?youtube\.com\/watch\?.*?\bv=([A-Za-z0-9_-]{6,})`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c17c076b4ff8a386554448eddb36fb07:search

```yaml
regex_id: c17c076b4ff8a386554448eddb36fb07
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/csvEntities.js:85:7"
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

## usage_mismatch:c27d5529bd9c3b4e79443f8e78ce39e5:search

```yaml
regex_id: c27d5529bd9c3b4e79443f8e78ce39e5
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/agentic-orchcrm/packages/tools/src/brochure/render-core.ts:698:22"
```

### Pattern

`^([A-Z][A-Za-z'&./ ]{1,28}):\s*(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c342bc583eebfdd7213941a85008922b:search

```yaml
regex_id: c342bc583eebfdd7213941a85008922b
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/superadmin/SuperAdminCronMaintenance.jsx:140:6"
```

### Pattern

`^\d+(,\d+)+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c4c0bf4a99523631422b2236024b4df9:search

```yaml
regex_id: c4c0bf4a99523631422b2236024b4df9
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/LandingPageBuilder.jsx:401:56"
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

## usage_mismatch:c6eeb7d9655ba6b8f8e38c441237f21c:search

```yaml
regex_id: c6eeb7d9655ba6b8f8e38c441237f21c
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:14035:9"
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

## usage_mismatch:c748d89e6b38b3628ee2f0793e0cca58:search

```yaml
regex_id: c748d89e6b38b3628ee2f0793e0cca58
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_itineraries.js:1490:20"
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

## usage_mismatch:c85821365a5a4f2804be9e3fadb32c09:search

```yaml
regex_id: c85821365a5a4f2804be9e3fadb32c09
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/whatsapp.js:91:22"
```

### Pattern

`^\s*(STOP|UNSUBSCRIBE|UNSUB|OPT[\s-]?OUT|STOP ALL)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c8d79a2f6e64b5f1865eca573d3bc7e7:search

```yaml
regex_id: c8d79a2f6e64b5f1865eca573d3bc7e7
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/server.js:1067:30"
```

### Pattern

`^\/landing-pages\/\d+\/preview$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:cc22732a3ad2b45e987d9dac7038046a:email

```yaml
regex_id: cc22732a3ad2b45e987d9dac7038046a
schema_version: "1"
kind: intent_mismatch
corpus: globussoft-crm
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/Reports.jsx:367:109"
```

### Pattern

`th><th style={thStyle}>Status<`

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

## usage_mismatch:ceae2921685720c20e61ffc6106efce3:search

```yaml
regex_id: ceae2921685720c20e61ffc6106efce3
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_commission_profiles.js:944:25"
```

### Pattern

`^\d{4}-Q[1-4]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cec5f9be8e8e388daeb1dfe8db870b92:search

```yaml
regex_id: cec5f9be8e8e388daeb1dfe8db870b92
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/GmailInbox.jsx:99:23"
```

### Pattern

`^\s*"?([^"<]*?)"?\s*<[^>]+>\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cf6e7cdfb71d48c28a8ddca1a948207d:search

```yaml
regex_id: cf6e7cdfb71d48c28a8ddca1a948207d
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/WebForms.jsx:4239:6"
```

### Pattern

`^[0-9a-fA-F]{6}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cfc96797d02823a0810de3adce15d83d:search

```yaml
regex_id: cfc96797d02823a0810de3adce15d83d
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/developer.js:228:4"
```

### Pattern

`^172\.(1[6-9]|2[0-9]|3[01])\.`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cfec32357224f7d0261304151b979d17:search

```yaml
regex_id: cfec32357224f7d0261304151b979d17
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/Reports.jsx:108:19"
```

### Pattern

`^[^\s@,;]+@[^\s@,;]+\.[^\s@,;]{2,}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d0ef5caac8a49e9e6ad2f4913ef6af4b:search

```yaml
regex_id: d0ef5caac8a49e9e6ad2f4913ef6af4b
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/developer.js:226:4"
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

## usage_mismatch:d1171fa5c0746c4e041768cdb41cccb0:search

```yaml
regex_id: d1171fa5c0746c4e041768cdb41cccb0
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/developer.js:230:4"
```

### Pattern

`^fc[0-9a-f]{2}:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d1652a56446b8e2044284561d3a6b546:search

```yaml
regex_id: d1652a56446b8e2044284561d3a6b546
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/mrzParser.js:293:7"
```

### Pattern

`^\d{8}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d2815b7ab9a8e3080af745d43b47d592:search

```yaml
regex_id: d2815b7ab9a8e3080af745d43b47d592
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/superadmin/SuperAdminCronMaintenance.jsx:136:6"
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

## usage_mismatch:d336fd0b4d481b9f1bc0655f31295d3d:search

```yaml
regex_id: d336fd0b4d481b9f1bc0655f31295d3d
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/server.js:1041:4"
```

### Pattern

`^\/travel\/brochures\/runs\/[^/]+\/stream$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d3ca8e115447d879490b37e6259f7612:search

```yaml
regex_id: d3ca8e115447d879490b37e6259f7612
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_microsites.js:733:23"
```

### Pattern

`^\d{4}-(0[1-9]|1[0-2])$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d3ff3fb3368da1b755b168b24a73f9fe:search

```yaml
regex_id: d3ff3fb3368da1b755b168b24a73f9fe
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:2327:7"
```

### Pattern

`^[0-9+\-\s()]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d40c708ec9dd2fd9ed6fc09dc3c33f52:search

```yaml
regex_id: d40c708ec9dd2fd9ed6fc09dc3c33f52
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:13168:7"
```

### Pattern

`^#[0-9a-fA-F]{6}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d44443e7cdfee197d8588975a6edaf13:search

```yaml
regex_id: d44443e7cdfee197d8588975a6edaf13
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/wellness/patients/PatientCreateModal.jsx:21:19"
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

## usage_mismatch:d46f90921323361067fc3db6e600723d:search

```yaml
regex_id: d46f90921323361067fc3db6e600723d
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/LandingPageBuilder.jsx:2488:20"
```

### Pattern

`^https?:\/\/(?:www\.|m\.)?youtube\.com\/shorts\/([A-Za-z0-9_-]{6,})`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d5cd0a2431757b82ec951ac51bde1681:search

```yaml
regex_id: d5cd0a2431757b82ec951ac51bde1681
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/WebForms.jsx:4223:6"
```

### Pattern

`^#[0-9a-fA-F]{6}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d801540f4ffa17d27bd180f91d8a4f3a:search

```yaml
regex_id: d801540f4ffa17d27bd180f91d8a4f3a
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/services/whatsappWebClient.js:492:6"
```

### Pattern

`^(1|true|yes)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d8d87889a471e61f780b7cf1d2714fb1:search

```yaml
regex_id: d8d87889a471e61f780b7cf1d2714fb1
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_microsites.js:1243:9"
```

### Pattern

`^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:da44b113aba627f14a1f1e3492e4e446:search

```yaml
regex_id: da44b113aba627f14a1f1e3492e4e446
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:10247:9"
```

### Pattern

`^(\+?91)?[6-9]\d{9}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:da697d163162dde24e88a79ff2fac7f0:search

```yaml
regex_id: da697d163162dde24e88a79ff2fac7f0
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/superadmin/SuperAdminCronMaintenance.jsx:150:27"
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

## usage_mismatch:db73ef7c456caa44f67f3eb7086e8147:search

```yaml
regex_id: db73ef7c456caa44f67f3eb7086e8147
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/Contacts.jsx:76:17"
```

### Pattern

`^\+?[\d\s\-().]{7,15}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dcdfe64e183de62bf49f33ad3a69c23e:search

```yaml
regex_id: dcdfe64e183de62bf49f33ad3a69c23e
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/services/whatsappWebClient.js:76:25"
```

### Pattern

`^(0|false|no|disabled)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:deea0357383787d2be01470c4af352de:search

```yaml
regex_id: deea0357383787d2be01470c4af352de
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_commission_profiles.js:1234:22"
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

## usage_mismatch:e15446b2b855cdf0690cca0aec70bd02:search

```yaml
regex_id: e15446b2b855cdf0690cca0aec70bd02
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/superadmin/SuperAdminCronMaintenance.jsx:146:27"
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

## usage_mismatch:e35f7503b8b13feca1c799d45e0d1202:search

```yaml
regex_id: e35f7503b8b13feca1c799d45e0d1202
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/visaLetterService.js:281:8"
```

### Pattern

`^subject:\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e3b726f5d67209914a99b0611c584364:search

```yaml
regex_id: e3b726f5d67209914a99b0611c584364
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_microsites.js:1905:7"
```

### Pattern

`^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e43ea62693f528b2d276ee5f68d6e4d8:search

```yaml
regex_id: e43ea62693f528b2d276ee5f68d6e4d8
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/sanitizeJson.js:121:18"
```

### Pattern

`^\d+(\.\d+)?(px|pt|em|rem|%)?(\s+\d+(\.\d+)?(px|pt|em|rem|%)?){0,3}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e43ec6e08d3b65efe1180b98de135486:search

```yaml
regex_id: e43ec6e08d3b65efe1180b98de135486
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:11280:18"
```

### Pattern

`^(?:\+?91)?[6-9]\d{9}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e48501aceb62f5ca05a3ecc4765eb2b6:search

```yaml
regex_id: e48501aceb62f5ca05a3ecc4765eb2b6
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_quotes.js:1345:23"
```

### Pattern

`^\d{4}-(0[1-9]|1[0-2])$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e494b5c29b40e0baec742cb6b04a1559:search

```yaml
regex_id: e494b5c29b40e0baec742cb6b04a1559
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/services/templates/wanderlux/support.js:256:79"
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

## usage_mismatch:e4e4ac3e85fde5419b9af3a1850e05a7:search

```yaml
regex_id: e4e4ac3e85fde5419b9af3a1850e05a7
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_commission_profiles.js:3269:22"
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

## usage_mismatch:e50cc05cccde822337caed3828f620ac:search

```yaml
regex_id: e50cc05cccde822337caed3828f620ac
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/scripts/cleanup-seed-pollution-2026-04-27.js:159:8"
```

### Pattern

`^Targeted \/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e70202ba870d250fe744018a0e512ff4:search

```yaml
regex_id: e70202ba870d250fe744018a0e512ff4
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/services/templates/wanderlux/support.js:132:9"
```

### Pattern

`\.dc\.html?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e90aa707edd2a8e0ce94cb7d83cf470f:search

```yaml
regex_id: e90aa707edd2a8e0ce94cb7d83cf470f
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:11694:13"
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

## usage_mismatch:ea8ecd0ce1b5caeef628e58c1264fc6d:search

```yaml
regex_id: ea8ecd0ce1b5caeef628e58c1264fc6d
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/server.js:1054:4"
```

### Pattern

`^\/travel\/diagnostics\/\d+\/readiness-report\.pdf$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:eb2f0923b8dd5bb5288bde9efcb5b4b4:search

```yaml
regex_id: eb2f0923b8dd5bb5288bde9efcb5b4b4
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/server.js:1025:4"
```

### Pattern

`^\/travel\/itineraries\/\d+\/pdf$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ecbb03c84ab2cfd7fe4500065de127b0:search

```yaml
regex_id: ecbb03c84ab2cfd7fe4500065de127b0
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_commission_profiles.js:3067:25"
```

### Pattern

`^\d{4}-Q[1-4]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ecf76d77c0607e1fb5fbb40e95f1bd0e:search

```yaml
regex_id: ecf76d77c0607e1fb5fbb40e95f1bd0e
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/leadJunkFilter.js:44:63"
```

### Pattern

`^[6-9]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ed65abfd55d7217e454a34b574499031:search

```yaml
regex_id: ed65abfd55d7217e454a34b574499031
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/scripts/cleanup-seed-pollution-2026-04-27.js:160:8"
```

### Pattern

`^Test\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f1a0638b5893382e03fbe316a9751c35:search

```yaml
regex_id: f1a0638b5893382e03fbe316a9751c35
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:5889:29"
```

### Pattern

`^_teardown_|^_test_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f2ad579a9e826e5f168c58be8b0c1489:search

```yaml
regex_id: f2ad579a9e826e5f168c58be8b0c1489
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/scripts/cleanup-seed-pollution-2026-04-27.js:161:8"
```

### Pattern

`^Test\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f2e4bb1c647809007784a9c96fd6355e:search

```yaml
regex_id: f2e4bb1c647809007784a9c96fd6355e
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:10254:18"
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

## usage_mismatch:f3b5d278cc4ff081c1ba78ec2974ed5f:search

```yaml
regex_id: f3b5d278cc4ff081c1ba78ec2974ed5f
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/wellness.js:1538:8"
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

## usage_mismatch:f49a6398d61f46cb4c621566a256f9dc:search

```yaml
regex_id: f49a6398d61f46cb4c621566a256f9dc
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_invoices.js:3810:17"
```

### Pattern

`^(\d{4})-(\d{2})-(\d{2})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f50bedf6d75771e88fd411b2faaf26ad:search

```yaml
regex_id: f50bedf6d75771e88fd411b2faaf26ad
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_microsites.js:213:8"
```

### Pattern

`^(image\/(png|jpe?g)|application\/pdf)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f569ce1c373339fc076937e38aa07cf5:search

```yaml
regex_id: f569ce1c373339fc076937e38aa07cf5
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/visaLetterService.js:282:43"
```

### Pattern

`^subject:\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f68b04ce454cd83cf83383320cc189a0:search

```yaml
regex_id: f68b04ce454cd83cf83383320cc189a0
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/sanitizeJson.js:115:23"
```

### Pattern

`^left$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f9ec97212d414612a92d385e2aa04b68:search

```yaml
regex_id: f9ec97212d414612a92d385e2aa04b68
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/landing_pages.js:3775:21"
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

## usage_mismatch:fb04d634db8e4d08b25e31a2ff7bd8f4:search

```yaml
regex_id: fb04d634db8e4d08b25e31a2ff7bd8f4
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/superadmin/SuperAdminCronMaintenance.jsx:150:81"
```

### Pattern

`^\d$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fb65884aef3b793275591fd7dec9a565:search

```yaml
regex_id: fb65884aef3b793275591fd7dec9a565
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/validators.js:251:25"
```

### Pattern

`^(tenantId|id)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fc559d241d8c4799428619983e79489e:search

```yaml
regex_id: fc559d241d8c4799428619983e79489e
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/csvEntities.js:1101:16"
```

### Pattern

`^[0-9+\-\s()]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fcf5cfa6edb19f4eaaa8aa4115c0addb:search

```yaml
regex_id: fcf5cfa6edb19f4eaaa8aa4115c0addb
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/travel_microsites.js:1746:9"
```

### Pattern

`^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fd3cee6a75aca51daec9a8486a88e6a7:search

```yaml
regex_id: fd3cee6a75aca51daec9a8486a88e6a7
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/agentic-orchcrm/packages/tools/src/brochure/render-core.ts:865:8"
```

### Pattern

`^[A-Z][A-Z &]{4,48}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fd48dafad0300d80ef420d5fe4489f1f:search

```yaml
regex_id: fd48dafad0300d80ef420d5fe4489f1f
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/lib/sanitizeJson.js:115:44"
```

### Pattern

`^center$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fd813e35691433b92cb7f2cd6c406004:search

```yaml
regex_id: fd813e35691433b92cb7f2cd6c406004
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/LandingPageBuilder.jsx:2486:24"
```

### Pattern

`^https?:\/\/(?:www\.)?youtu\.be\/([A-Za-z0-9_-]{6,})`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fd850cba74de6c6974008e1509fe2c69:search

```yaml
regex_id: fd850cba74de6c6974008e1509fe2c69
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/frontend/src/pages/wellness/patients/PatientCreateModal.jsx:27:8"
```

### Pattern

`^[6-9]\d{9}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fe0dacf7160f033a4c06c934e00b2ef0:search

```yaml
regex_id: fe0dacf7160f033a4c06c934e00b2ef0
schema_version: "1"
kind: usage_mismatch
corpus: globussoft-crm
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/globussoft-crm/rules/backend/routes/developer.js:225:4"
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

## property:inventory:rc-shape1-injection-alphabet:rc-shape1-injection-alphabet

```yaml
regex_id: "inventory:rc-shape1-injection-alphabet"
schema_version: "1"
kind: property
corpus: globussoft-crm
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
corpus: globussoft-crm
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
corpus: globussoft-crm
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
corpus: globussoft-crm
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

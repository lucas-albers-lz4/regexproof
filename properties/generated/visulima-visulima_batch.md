---
schema_version: "1"
corpus: visulima-visulima
findings: 576
---

# visulima-visulima batch findings

## intent_mismatch:001b0b1801a8fd6f243ad915e7dce261:email

```yaml
regex_id: 001b0b1801a8fd6f243ad915e7dce261
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/crypto/dkim-signer.ts:63:47"
```

### Pattern

`\s+`

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

## usage_mismatch:001b8f748148c7b5877d8b520aea079f:search

```yaml
regex_id: 001b8f748148c7b5877d8b520aea079f
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/analyze/handler.ts:10:29"
```

### Pattern

`^[\^~>=<]+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:00f470166139c49024bde8e0ef51bb51:search

```yaml
regex_id: 00f470166139c49024bde8e0ef51bb51
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/config/workspace.ts:293:81"
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

## usage_mismatch:01b1bf8e7397c84cdb534853e79d7857:search

```yaml
regex_id: 01b1bf8e7397c84cdb534853e79d7857
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/util/catalog.ts:26:29"
```

### Pattern

`^(@[^:]+):registry$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:02acda08f45647f08bab1c1ff70b6100:search

```yaml
regex_id: 02acda08f45647f08bab1c1ff70b6100
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/tui/src/ink/color-matrix.ts:108:17"
```

### Pattern

`^#?(?<r>[\da-f])(?<g>[\da-f])(?<b>[\da-f])$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:03393d9f947ff6aaaf0a148cf91fcf65:search

```yaml
regex_id: 03393d9f947ff6aaaf0a148cf91fcf65
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/update/ecosystems/applier.ts:114:36"
```

### Pattern

`^\s*#\s*v?\d[\w.+-]*\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:03577f396b8b5fb6402f6df6288665ba:search

```yaml
regex_id: 03577f396b8b5fb6402f6df6288665ba
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/task-runner/src/lockfile-hasher.ts:125:28"
```

### Pattern

`^\s{4,}(\S+):\n\s+specifier:.*\n\s+version:\s*'?([^'\n(]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:03f1616d88631d47645a3fa5da062ec3:search

```yaml
regex_id: 03f1616d88631d47645a3fa5da062ec3
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/apps/web/scripts/copy-package-docs.js:306:20"
```

### Pattern

`^(\/|#|[a-z][a-z0-9+.-]*:)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0410393bd6f0ca7e1f32e3bf2c187a27:search

```yaml
regex_id: 0410393bd6f0ca7e1f32e3bf2c187a27
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/parser/dumper.ts:50:28"
```

### Pattern

`^\s|\s$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:04106ec1cd7bc8cf66be59cef8f42304:search

```yaml
regex_id: 04106ec1cd7bc8cf66be59cef8f42304
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/secret-scanner/scripts/kingfisher-converter.mjs:18:35"
```

### Pattern

`^\{\d+(?:,\d*)?\}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:04bbf1649cd3fe82f8898a932e3f54fd:search

```yaml
regex_id: 04bbf1649cd3fe82f8898a932e3f54fd
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/multi-eco-lockfiles.ts:233:26"
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

## usage_mismatch:04dc12e2632f0c273f61569e53697807:search

```yaml
regex_id: 04dc12e2632f0c273f61569e53697807
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/secret-scanner/scripts/kingfisher-converter.mjs:14:29"
```

### Pattern

`^\s*\(\?[a-z]+\)\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0550e52b878bcf16bbb34a68816e0778:search

```yaml
regex_id: 0550e52b878bcf16bbb34a68816e0778
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/util/catalog.ts:25:31"
```

### Pattern

`^catalogs:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:0592f4d790fdb520ed81fcaac9faa2e7:url

```yaml
regex_id: 0592f4d790fdb520ed81fcaac9faa2e7
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/remote/gitlab.ts:248:22"
```

### Pattern

`gitlab\.[\w.-]+[/:]([^/].*?)(?:\.git)?$`

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

## intent_mismatch:05a3852631c8540f4cf7757d18766f43:email

```yaml
regex_id: 05a3852631c8540f4cf7757d18766f43
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/free-email-domains/scripts/free-email-sync-manager.js:12:24"
```

### Pattern

`^(?:0\.0\.0\.0\s+|127\.0\.0\.1\s+|localhost\s+)`

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

## usage_mismatch:05a3852631c8540f4cf7757d18766f43:search

```yaml
regex_id: 05a3852631c8540f4cf7757d18766f43
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/free-email-domains/scripts/free-email-sync-manager.js:12:24"
```

### Pattern

`^(?:0\.0\.0\.0\s+|127\.0\.0\.1\s+|localhost\s+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:06403f10b8057713c64f829850ef5ab6:search

```yaml
regex_id: 06403f10b8057713c64f829850ef5ab6
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/packem.config.ts:44:16"
```

### Pattern

`^@visulima\/tui-kit(\/|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0744cc2dc0afc177016775c43c6a4e30:search

```yaml
regex_id: 0744cc2dc0afc177016775c43c6a4e30
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/cache/cache-directory.ts:117:33"
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

## usage_mismatch:07ccc04bf6f95720d2432d7247b649ff:search

```yaml
regex_id: 07ccc04bf6f95720d2432d7247b649ff
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/release/doctor/handler.ts:1277:27"
```

### Pattern

`(?:^|@)\d+\.\d+\.\d+(?:[-+].+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:07f5792da100d204754eeb635dec8f21:search

```yaml
regex_id: 07f5792da100d204754eeb635dec8f21
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/hook/migrate.ts:16:28"
```

### Pattern

`^\. "\$\(dirname "\$0"\)\/common\.sh"\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0848bf6818cfdc3adbb41f6148d62e26:search

```yaml
regex_id: 0848bf6818cfdc3adbb41f6148d62e26
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/string/src/constants.ts:84:43"
```

### Pattern

`(?:\r\n|\r|\n)[ \t]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0861a10624544ba072ccc962a643f4f2:search

```yaml
regex_id: 0861a10624544ba072ccc962a643f4f2
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/utils/parse-eml.ts:11:30"
```

### Pattern

`^\r?\n`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:08c87f8cfcfb770683a90628bfd830e6:search

```yaml
regex_id: 08c87f8cfcfb770683a90628bfd830e6
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/deps/missing-package-json.ts:28:35"
```

### Pattern

`\/\*\*$|\/\*\/\*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:08fb780bb6874ad3d34c97ec8388fc99:search

```yaml
regex_id: 08fb780bb6874ad3d34c97ec8388fc99
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/webhooks/ses-sns.ts:53:34"
```

### Pattern

`^sns\.[a-z0-9-]+\.amazonaws\.com(?:\.cn)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0955aadf57c9a384a3e5c2010b09719e:search

```yaml
regex_id: 0955aadf57c9a384a3e5c2010b09719e
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/util/patched-dependencies.ts:30:21"
```

### Pattern

`^(@[\w./-]+\/[\w./-]+|[\w.-]+)@(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0aba7965351dfbac813ae68b12f0443a:search

```yaml
regex_id: 0aba7965351dfbac813ae68b12f0443a
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/iso-locale/src/locale.ts:13:22"
```

### Pattern

`^[a-z]{3}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0b7081118be2961eff6283665f24bed8:search

```yaml
regex_id: 0b7081118be2961eff6283665f24bed8
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/replay.ts:24:19"
```

### Pattern

`^(.+)@(\d+\.\d+\.\d+(?:[-+].*)?)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0b867679d900d0016324a100fbe8a138:search

```yaml
regex_id: 0b867679d900d0016324a100fbe8a138
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/util/format-package-json-fields.ts:12:25"
```

### Pattern

`^git\+ssh:\/\/git@github\.com\/([^/]+)\/([^/.]+(?:\.git)?)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:0c2ddcffca4ad3fc481b511f798af47f:email

```yaml
regex_id: 0c2ddcffca4ad3fc481b511f798af47f
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/free-email-domains/scripts/sync-domains.js:12:26"
```

### Pattern

`github\.com\/([^/]+\/[^/]+)`

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

## usage_mismatch:0c406d8729def3927411bacd5cea6b18:search

```yaml
regex_id: 0c406d8729def3927411bacd5cea6b18
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/lint-fmt/adapters/ruff.ts:32:31"
```

### Pattern

`^Would reformat:?\s+(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0cca4e450fdbdd3d1ea912bed77c9eaf:search

```yaml
regex_id: 0cca4e450fdbdd3d1ea912bed77c9eaf
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/iso-locale/src/locale.ts:6:21"
```

### Pattern

`^[A-Z]{2}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0d75f34de3a132e05038f24f0ea7aad1:search

```yaml
regex_id: 0d75f34de3a132e05038f24f0ea7aad1
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/hook/list.ts:26:23"
```

### Pattern

`^# ([^:\s]\S*)(?::\s+(.+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0dca129474dad89b9fa5802edcf81c39:search

```yaml
regex_id: 0dca129474dad89b9fa5802edcf81c39
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/filesystem/fs/src/utils/parse-json.ts:26:28"
```

### Pattern

`in JSON at position (\d+)(?: \(line (\d+) column (\d+)\))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0de3e466d458124a27884e474a2f0f85:search

```yaml
regex_id: 0de3e466d458124a27884e474a2f0f85
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/api/jsdoc-open-api/src/util/yaml-loc.ts:3:31"
```

### Pattern

`^\s*(#\s*(?:\S.*)?)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0e1f4f541336199187ffed104d6c24d3:search

```yaml
regex_id: 0e1f4f541336199187ffed104d6c24d3
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/filesystem/path/src/path.ts:31:19"
```

### Pattern

`[^/](\.[^./]+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0ebf40f0b6cbaae80befe68bc84185de:search

```yaml
regex_id: 0ebf40f0b6cbaae80befe68bc84185de
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/vite-overlay/src/overlay/client/runtime.js:18:25"
```

### Pattern

`^\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0f26a96db5e88a0a2bb6e8595ef8bb79:search

```yaml
regex_id: 0f26a96db5e88a0a2bb6e8595ef8bb79
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/changelog/keep-a-changelog.ts:92:47"
```

### Pattern

`^\s*[a-z]+(?:\([^)]+\))?!\s*:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0f430a2773ed833eb6a258d1a480640d:search

```yaml
regex_id: 0f430a2773ed833eb6a258d1a480640d
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/is-ansi-color-supported/src/is-color-supported.server.ts:15:31"
```

### Pattern

`^-{1,2}(color|colors|color=true|color=always)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0f64932155d5ba0da4f784e95cf60b6a:search

```yaml
regex_id: 0f64932155d5ba0da4f784e95cf60b6a
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/task-runner/src/file-access-tracker.ts:491:12"
```

### Pattern

`\.so(\.\d+)*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0fba896ac54e3bf0ab313c0bfcc8fd8e:search

```yaml
regex_id: 0fba896ac54e3bf0ab313c0bfcc8fd8e
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/lint-fmt/adapters/shellcheck.ts:43:72"
```

### Pattern

`^[a-z]:[\\/]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:107500af33a2556869c7356565b70420:email

```yaml
regex_id: 107500af33a2556869c7356565b70420
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/render/dark-mode.ts:2:18"
```

### Pattern

`<head[^<>]*>`

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

## usage_mismatch:10a76c38cfcef1c2fd2d991e9e192743:search

```yaml
regex_id: 10a76c38cfcef1c2fd2d991e9e192743
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/dev-toolbar/src/apps/tailwind/tailwind-app.tsx:15:27"
```

### Pattern

`-\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:10cca03eba0ba8f68364a489f0df7bf1:search

```yaml
regex_id: 10cca03eba0ba8f68364a489f0df7bf1
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/transitive-fix.ts:178:8"
```

### Pattern

`^overrides\s*:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:120fe31803efde5719e0e6c0b094bf3d:search

```yaml
regex_id: 120fe31803efde5719e0e6c0b094bf3d
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/dev-toolbar/src/apps/inspector/element-utils.ts:333:8"
```

### Pattern

`^h[1-6]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:135faf6a17bc7271a3924cf0e9ed8733:search

```yaml
regex_id: 135faf6a17bc7271a3924cf0e9ed8733
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/update/ecosystems/gitlab/scanner.ts:107:24"
```

### Pattern

`^\s*-?\s*[a-z_][\w-]*:\s*(?:#.*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1360d0aed571012f63e92f14d8afbad6:search

```yaml
regex_id: 1360d0aed571012f63e92f14d8afbad6
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/schema/schemas.ts:39:26"
```

### Pattern

`^[-+]?0[0-7_]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:13ca607b8a163aa075b0d6bd6b30bfe8:search

```yaml
regex_id: 13ca607b8a163aa075b0d6bd6b30bfe8
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/apps/web/src/pages/home/sections/hero.tsx:126:38"
```

### Pattern

`^[{}()[\];,=>:]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1440ddefaf5b25be9a6d18f882d12ce6:search

```yaml
regex_id: 1440ddefaf5b25be9a6d18f882d12ce6
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/channels.ts:108:20"
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

## intent_mismatch:1453fc474dc70a047e5cd4f68b53e8a9:email

```yaml
regex_id: 1453fc474dc70a047e5cd4f68b53e8a9
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/disposable-email-domains/scripts/sync-domains.js:12:26"
```

### Pattern

`github\.com\/([^/]+\/[^/]+)`

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

## usage_mismatch:15cf59accefc56c0fefe17b40097ecab:search

```yaml
regex_id: 15cf59accefc56c0fefe17b40097ecab
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/migrate/kingfisher.ts:74:54"
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

## usage_mismatch:1694f0d5fc3d25d0f7848ac62cc35d41:search

```yaml
regex_id: 1694f0d5fc3d25d0f7848ac62cc35d41
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/ci-ignore-helpers.ts:55:19"
```

### Pattern

`^[\w./~^@{}][\w.\-/~^@{}]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:16c50c019785a94b61bac5b0a40e2593:email

```yaml
regex_id: 16c50c019785a94b61bac5b0a40e2593
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/crypto/smime-encrypter.ts:34:20"
```

### Pattern

`\s`

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

## usage_mismatch:16f753a2c1247fd8a814cb0952b9e131:search

```yaml
regex_id: 16f753a2c1247fd8a814cb0952b9e131
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/task-runner/src/lockfile-hasher.ts:130:53"
```

### Pattern

`^['"]|['"]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:17353bf4b1256fa84da6fe8221d83f61:search

```yaml
regex_id: 17353bf4b1256fa84da6fe8221d83f61
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/deps/missing-package-json.ts:24:26"
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

## usage_mismatch:177a9651377267502a92f79117043ded:search

```yaml
regex_id: 177a9651377267502a92f79117043ded
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/pail/src/reporter/http/utils/retry.ts:42:28"
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

## usage_mismatch:1783aa8958343f65868dafd0e3f23da0:search

```yaml
regex_id: 1783aa8958343f65868dafd0e3f23da0
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/task-runner/src/file-access-tracker.ts:394:29"
```

### Pattern

`^(?:\d+\s+)?open\("([^"]+)"`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:17ff3eb457dd86aab6c93c9f2e5bccad:email

```yaml
regex_id: 17ff3eb457dd86aab6c93c9f2e5bccad
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/disposable-email-domains/scripts/disposable-email-sync-manager.js:14:31"
```

### Pattern

`\s\S*$`

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

## usage_mismatch:17ff3eb457dd86aab6c93c9f2e5bccad:search

```yaml
regex_id: 17ff3eb457dd86aab6c93c9f2e5bccad
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/disposable-email-domains/scripts/disposable-email-sync-manager.js:14:31"
```

### Pattern

`\s\S*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:183317adf547cd03e9b507350173a766:search

```yaml
regex_id: 183317adf547cd03e9b507350173a766
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/change-file.ts:98:17"
```

### Pattern

`^ {0,3}(?:```|~~~)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1851b0e9c9e5478ea35ab468e6024892:search

```yaml
regex_id: 1851b0e9c9e5478ea35ab468e6024892
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/error/src/stacktrace/parse-stacktrace.ts:66:6"
```

### Pattern

`^.*?\s*at\s(?:(.+?\)(?:\s\[.+\])?|\(?.*?)\s?\((?:address\sat\s)?)?(?:async\s)?((?:<anonymous>|[-a-z]+:|.*bundle|\/)?.*?)(?::(\d+))?(?::(\d+))?\)?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:193e5b42c2093c54621f93b05f0efcd4:search

```yaml
regex_id: 193e5b42c2093c54621f93b05f0efcd4
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/error/src/stacktrace/parse-stacktrace.ts:118:25"
```

### Pattern

`^.*?\s*@.*|\[native code\]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1963faa1ae22a9127b279a1e98c7e6fe:search

```yaml
regex_id: 1963faa1ae22a9127b279a1e98c7e6fe
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/release/doctor/handler.ts:808:38"
```

### Pattern

`^v\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:19e8e5ed282fed5e26b3bb71c4b725e9:search

```yaml
regex_id: 19e8e5ed282fed5e26b3bb71c4b725e9
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/pm/overrides.ts:193:10"
```

### Pattern

`^overrides:\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:19f43954c9a67936002499db29f27cb4:search

```yaml
regex_id: 19f43954c9a67936002499db29f27cb4
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/find-ai-runner/src/process-tree.ts:22:32"
```

### Pattern

`\.(?:bat|cmd|exe)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1a13ae78a5c37231a9ec87af2be3b5fa:search

```yaml
regex_id: 1a13ae78a5c37231a9ec87af2be3b5fa
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/string/src/case/identify-case.ts:10:21"
```

### Pattern

`^[A-Z][A-Z0-9]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1a5ede1380b1d3fedd69fa8ad864b4d3:search

```yaml
regex_id: 1a5ede1380b1d3fedd69fa8ad864b4d3
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/tui-kit/scripts/build-registry.mjs:81:31"
```

### Pattern

`\.(tsx|ts)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1b6fb3096afc8fae0ce73701ffdccc40:search

```yaml
regex_id: 1b6fb3096afc8fae0ce73701ffdccc40
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/min-release-age.ts:176:35"
```

### Pattern

`^npmPreapprovedPackages:[ \t]*\n(?:[ \t]{2}[^\n]*\n)*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1bd2fb852f9353186e0f5f074b677339:search

```yaml
regex_id: 1bd2fb852f9353186e0f5f074b677339
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/secret-scanner/src/heuristics.ts:131:21"
```

### Pattern

`^[\da-f]{8}-[\da-f]{4}-[\da-f]{4}-[\da-f]{4}-[\da-f]{12}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1c14a7a3e0b488d15254291852b3d3f5:search

```yaml
regex_id: 1c14a7a3e0b488d15254291852b3d3f5
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/util/catalog.ts:32:32"
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

## usage_mismatch:1cbbc21a499b0747d82d2e805f7b23a0:search

```yaml
regex_id: 1cbbc21a499b0747d82d2e805f7b23a0
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis-mcp/src/tools/list-runs.ts:10:28"
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

## usage_mismatch:1cc75160c7a15b95d841acd182362913:search

```yaml
regex_id: 1cc75160c7a15b95d841acd182362913
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/parser/stream.ts:30:24"
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

## usage_mismatch:1d0619883f9cd8e24fe796c2e05ddc23:search

```yaml
regex_id: 1d0619883f9cd8e24fe796c2e05ddc23
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/iso-locale/src/locale.ts:9:21"
```

### Pattern

`^\d{3}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1d3e96590ffd1750f042008154496ddb:search

```yaml
regex_id: 1d3e96590ffd1750f042008154496ddb
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/schema/schemas.ts:47:34"
```

### Pattern

`^[-+]?[1-9][\d_]*(?::[0-5]?\d)+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1e1943874d6750a944dcfc9bea7ce607:search

```yaml
regex_id: 1e1943874d6750a944dcfc9bea7ce607
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/update/ecosystems/gitlab/scanner.ts:97:24"
```

### Pattern

`^(\s*-\s*)(['"]?)([^'"\s#:]+:[^'"\s#]+)\2(\s*#.*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1efb992603437b580b0f4b16ee044504:search

```yaml
regex_id: 1efb992603437b580b0f4b16ee044504
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/typosquats.ts:376:17"
```

### Pattern

`^(?:npm|pnpm|yarn):(.+?)(?:@.*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1f8d4fd42a790c5973aa738c5b170e56:search

```yaml
regex_id: 1f8d4fd42a790c5973aa738c5b170e56
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/string/src/constants.ts:81:42"
```

### Pattern

`^[ \t]*(?:\r\n|\r|\n)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1f9f1ecfe1c6e37a98b6073317ba6b97:search

```yaml
regex_id: 1f9f1ecfe1c6e37a98b6073317ba6b97
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/dev-toolbar/src/vite-plugin.ts:27:19"
```

### Pattern

`\.[jt]sx$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1fa857bba2452a0dcb002476e149bc0c:search

```yaml
regex_id: 1fa857bba2452a0dcb002476e149bc0c
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/enforcement.ts:93:20"
```

### Pattern

`^\s*enableScripts\s*:\s*false\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2007bf6a504f2b350e0cafb2cac752a8:search

```yaml
regex_id: 2007bf6a504f2b350e0cafb2cac752a8
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/replay.ts:23:27"
```

### Pattern

`^exit[\s-]prerelease\s*:\s*(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:205845a9886e69f12302552b83332d50:search

```yaml
regex_id: 205845a9886e69f12302552b83332d50
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/apps/web/src/pages/home/sections/hero.tsx:127:33"
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

## usage_mismatch:20e0687e2731f98865bc7130925076d5:search

```yaml
regex_id: 20e0687e2731f98865bc7130925076d5
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/string/src/word-wrap.ts:8:27"
```

### Pattern

`^\s+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:210698d45b2422cad5d3b4320e70c50b:search

```yaml
regex_id: 210698d45b2422cad5d3b4320e70c50b
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/generate/moon-adapter/tera-subset.ts:345:8"
```

### Pattern

`^-?\d+(?:\.\d+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:21f9cb852dd368be9da9c19602a01681:search

```yaml
regex_id: 21f9cb852dd368be9da9c19602a01681
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/hook/install.ts:12:26"
```

### Pattern

`\/$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:22851f0a0aa7979fba1ceaa38115714f:search

```yaml
regex_id: 22851f0a0aa7979fba1ceaa38115714f
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/filesystem/path/src/utils.ts:147:23"
```

### Pattern

`^(?:msys|cygwin)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:229d1747ace67454d23cf6f286828f7c:email

```yaml
regex_id: 229d1747ace67454d23cf6f286828f7c
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/utils/decode-mime-header.ts:73:39"
```

### Pattern

`(\?=)\s+(=\?)`

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

## usage_mismatch:22aa91f94a4de86dfcc15bf18557370f:search

```yaml
regex_id: 22aa91f94a4de86dfcc15bf18557370f
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/runtime/toolchain.ts:198:38"
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

## usage_mismatch:22c3b987d7e42b695bbffe7f71b9df6a:search

```yaml
regex_id: 22c3b987d7e42b695bbffe7f71b9df6a
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/storage/storage/src/handler/base/base-handler-core.ts:186:16"
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

## usage_mismatch:22c8aefe883951d6500ef36ccc09d6c3:search

```yaml
regex_id: 22c8aefe883951d6500ef36ccc09d6c3
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/deps/custom-types.ts:117:30"
```

### Pattern

`^([@\w./-]+?)@([^+]+)(\+.+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:22f0c0ec622b45d61fcacdd3cf863fb8:search

```yaml
regex_id: 22f0c0ec622b45d61fcacdd3cf863fb8
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/apply-release-plan.ts:227:24"
```

### Pattern

`^# .+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:2447db59bd735dff80895405b8b5f45a:url

```yaml
regex_id: 2447db59bd735dff80895405b8b5f45a
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/vite-overlay/src/utils/enhance-vite-ssr-error.ts:13:28"
```

### Pattern

`Failed to load url\s+(.*?)\s+\(resolved id:`

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

## usage_mismatch:245fe3abf5d1dc2f178694333a2ec60c:search

```yaml
regex_id: 245fe3abf5d1dc2f178694333a2ec60c
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/is-ansi-color-supported/src/is-color-supported.server.ts:21:22"
```

### Pattern

`^screen|^tmux|^xterm|^vt[1-5]\d\d|^ansi|color|mintty|rxvt|cygwin|linux`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:24f01483826444fc5d8f1567358a7b68:search

```yaml
regex_id: 24f01483826444fc5d8f1567358a7b68
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/storage/storage/src/utils/http.ts:246:33"
```

### Pattern

`^[\da-z]{4,}(?:-[\da-z]{4,}){2,}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:26275ca3a07a9f4681f31e4ac88f1c44:search

```yaml
regex_id: 26275ca3a07a9f4681f31e4ac88f1c44
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/filesystem/fs/src/utils/ini-preserve.ts:11:20"
```

### Pattern

`^[^=]+=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:268bb89ddbc5dc8601ffed8accc40378:search

```yaml
regex_id: 268bb89ddbc5dc8601ffed8accc40378
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/task-runner/src/command-parser/strip-quotes.ts:10:8"
```

### Pattern

`^".+?"$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2693261634b7181db7b3d7048e383028:search

```yaml
regex_id: 2693261634b7181db7b3d7048e383028
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/utils/parse-eml.ts:16:31"
```

### Pattern

`\r?\n$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:26ba4758d333a1ab2121d71f84a7af23:search

```yaml
regex_id: 26ba4758d333a1ab2121d71f84a7af23
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/task/arguments.ts:181:31"
```

### Pattern

`^[a-zA-Z][\w-]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:276ea0c8596adc942093d73b33e03ff5:search

```yaml
regex_id: 276ea0c8596adc942093d73b33e03ff5
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/task-runner/src/command-parser/expand-shortcut.ts:3:23"
```

### Pattern

`^(npm|yarn|pnpm|bun|node|deno):(\S+)(.*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2829ef9dade1a478855c6a625850e598:search

```yaml
regex_id: 2829ef9dade1a478855c6a625850e598
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/tui/src/ink/styled-line-factory.ts:445:28"
```

### Pattern

`^[\u0020-\u007E]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:285ff7ad2971d817695200f74f854b37:search

```yaml
regex_id: 285ff7ad2971d817695200f74f854b37
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/schema/resolve-scalar.ts:28:21"
```

### Pattern

`^\.(?:nan|NaN|NAN)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:286bbce56df7df6cc889210bd2a1abbe:search

```yaml
regex_id: 286bbce56df7df6cc889210bd2a1abbe
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/disposable-email-domains/scripts/disposable-email-sync-manager.js:17:32"
```

### Pattern

`^[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?(?:\.[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:28b16fc12a7f1e2e293986de50748c4b:search

```yaml
regex_id: 28b16fc12a7f1e2e293986de50748c4b
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/dev-toolbar/src/apps/seo/seo-app.tsx:96:19"
```

### Pattern

`^\d{4}-\d{2}-\d{2}(?:T\d{2}:\d{2}(?::\d{2})?(?:[+-]\d{2}:\d{2}|Z)?)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2a978fb729810f33faabf0b4d4908dc2:search

```yaml
regex_id: 2a978fb729810f33faabf0b4d4908dc2
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/ai/audit-explain.ts:44:8"
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

## usage_mismatch:2ba366ab940328f901777b0419aee8e7:search

```yaml
regex_id: 2ba366ab940328f901777b0419aee8e7
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/filesystem/path/src/utils.ts:145:23"
```

### Pattern

`^(?:\.?\.[/\\]|\.\.\B)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2bf81d0b18b20bfad5daf6afb28a630c:search

```yaml
regex_id: 2bf81d0b18b20bfad5daf6afb28a630c
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/exotic-subdeps.ts:72:8"
```

### Pattern

`^[\w.-]+\/[\w.-]+(?:#.+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:2c7c0a17ce58b629fa5a70e71ffd50b3:email

```yaml
regex_id: 2c7c0a17ce58b629fa5a70e71ffd50b3
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/crypto/smime-signer.ts:45:20"
```

### Pattern

`-----END[^-]+-----`

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

## usage_mismatch:2cd4ba9c99b3480ed73d56456d3258bd:search

```yaml
regex_id: 2cd4ba9c99b3480ed73d56456d3258bd
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/vite-overlay/src/utils/normalize-id-candidates.ts:2:21"
```

### Pattern

`^\/@fs\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:2d4fade76505d0e03e4c369953361fbb:email

```yaml
regex_id: 2d4fade76505d0e03e4c369953361fbb
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/providers/azure/provider.ts:355:65"
```

### Pattern

`endpoint=([^;]+);accesskey=([^;]+)`

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

## usage_mismatch:2ec2c0e3aafe805aacc01963addeaa63:search

```yaml
regex_id: 2ec2c0e3aafe805aacc01963addeaa63
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/.lintstagedrc.js:40:76"
```

### Pattern

`[/\\]CHANGELOG\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2f5f65264018746f02fd900a6177cc28:search

```yaml
regex_id: 2f5f65264018746f02fd900a6177cc28
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/error-handler/src/error-handler/jsonp-error-handler.ts:13:25"
```

### Pattern

`^[A-Za-z_$][\w$.]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:314e50f5d62509d8e08bcae377afe591:email

```yaml
regex_id: 314e50f5d62509d8e08bcae377afe591
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/providers/aws-ses/provider.ts:270:50"
```

### Pattern

`<Message>(.*?)<\/Message>`

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

## intent_mismatch:32e6bb21e276cde49c0790b3efc5e053:email

```yaml
regex_id: 32e6bb21e276cde49c0790b3efc5e053
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/utils/parse-address.ts:134:44"
```

### Pattern

`^<([^>]+)>$`

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

## usage_mismatch:32e6bb21e276cde49c0790b3efc5e053:search

```yaml
regex_id: 32e6bb21e276cde49c0790b3efc5e053
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/utils/parse-address.ts:134:44"
```

### Pattern

`^<([^>]+)>$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3315e1ff4ee729c2b1386b83a8fdcf20:search

```yaml
regex_id: 3315e1ff4ee729c2b1386b83a8fdcf20
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/find-ai-runner/src/index.ts:18:27"
```

### Pattern

`\.(?:bat|cmd)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:340a0db2f92fe5e85bf4e423e240ea40:search

```yaml
regex_id: 340a0db2f92fe5e85bf4e423e240ea40
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/schema/resolve-scalar.ts:20:19"
```

### Pattern

`^0x[0-9a-fA-F]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:3430e10b92ac3c81263e1561b50c8d54:email

```yaml
regex_id: 3430e10b92ac3c81263e1561b50c8d54
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/disposable-email-domains/scripts/disposable-email-sync-manager.js:15:33"
```

### Pattern

`[,;][^,;]*$`

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

## usage_mismatch:3430e10b92ac3c81263e1561b50c8d54:search

```yaml
regex_id: 3430e10b92ac3c81263e1561b50c8d54
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/disposable-email-domains/scripts/disposable-email-sync-manager.js:15:33"
```

### Pattern

`[,;][^,;]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:344524dc98de7a8f8a8bac19647452b6:search

```yaml
regex_id: 344524dc98de7a8f8a8bac19647452b6
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis-mcp/src/validation.ts:11:23"
```

### Pattern

`^[\w.-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:34832fac40d0bbd1fe2cf3d1915cf2db:search

```yaml
regex_id: 34832fac40d0bbd1fe2cf3d1915cf2db
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/humanizer/src/load-duration-language.ts:3:26"
```

### Pattern

`^[a-z]{2,3}(?:_[a-z]+)*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:349f47a6d1819be0d445af3c33d179d9:search

```yaml
regex_id: 349f47a6d1819be0d445af3c33d179d9
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/lint-fmt/ignore.ts:35:25"
```

### Pattern

`^\s*(?:#.*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:352eb28321786b350fc43ad7b419115d:search

```yaml
regex_id: 352eb28321786b350fc43ad7b419115d
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/filesystem/path/src/path.ts:33:26"
```

### Pattern

`\/$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:353d57c5a782f3b62e6f5a3f7131c7c8:search

```yaml
regex_id: 353d57c5a782f3b62e6f5a3f7131c7c8
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/lint-fmt/adapters/biome.ts:167:31"
```

### Pattern

`^[a-z]:[\\/]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3574003467d417217d1ce739d285158e:search

```yaml
regex_id: 3574003467d417217d1ce739d285158e
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/packem.config.ts:36:16"
```

### Pattern

`^react-reconciler(\/|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:35e334376e5d7bfb82e28ad1b1ce7c0f:search

```yaml
regex_id: 35e334376e5d7bfb82e28ad1b1ce7c0f
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/free-email-domains/scripts/free-email-sync-manager.js:11:25"
```

### Pattern

`^refs\/heads\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:373422b27186860fffe422b6d6875cfe:search

```yaml
regex_id: 373422b27186860fffe422b6d6875cfe
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/manifests.ts:35:30"
```

### Pattern

`^([^<(]+?)?(?:<([^>]+)>)?\s*(?:\(([^)]+)\))?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:37470c1552059a00a5764cd324714738:search

```yaml
regex_id: 37470c1552059a00a5764cd324714738
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/api/health-check/src/utils/normalize-host.ts:14:8"
```

### Pattern

`^[a-z][\w+.-]*:\/\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3765d9ee5ed5e87a16733327ef3590a4:search

```yaml
regex_id: 3765d9ee5ed5e87a16733327ef3590a4
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/tui-kit/src/time-picker.tsx:70:22"
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

## usage_mismatch:37d6b5e1480760b5fa0af5c877526430:search

```yaml
regex_id: 37d6b5e1480760b5fa0af5c877526430
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/deps/custom-types.ts:118:33"
```

### Pattern

`^([@\w./-]+)~(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:390020fcf682382fbff1fb3cb76b376d:search

```yaml
regex_id: 390020fcf682382fbff1fb3cb76b376d
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/change-file.ts:73:24"
```

### Pattern

`^(?:@[a-z0-9-]+\/)?[\w.-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:39779af05e9a329fddd934b90c06ba63:email

```yaml
regex_id: 39779af05e9a329fddd934b90c06ba63
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/crypto/dkim-signer.ts:22:72"
```

### Pattern

`\s+`

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

## usage_mismatch:39a326569dcf90b128baedadf73c8b6d:search

```yaml
regex_id: 39a326569dcf90b128baedadf73c8b6d
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/update/ecosystems/gitlab/scanner.ts:66:15"
```

### Pattern

`^\s*ref:\s*(['"]?)([^'"\s#]+)\1(\s*#.*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3a599058937b5a609687605841eb5644:search

```yaml
regex_id: 3a599058937b5a609687605841eb5644
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/config/workspace.ts:36:18"
```

### Pattern

`^['"]|['"]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3aafb955801247cbe8ded0ba1eae328d:search

```yaml
regex_id: 3aafb955801247cbe8ded0ba1eae328d
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/utils/quoted-printable.ts:4:23"
```

### Pattern

`^[\da-f]{2}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3b44239ea4781ba845e992b2a65247b6:search

```yaml
regex_id: 3b44239ea4781ba845e992b2a65247b6
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/tui/src/ink/sanitize-ansi.ts:3:27"
```

### Pattern

`^[\d:;]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3b574a02c08ac807e2a273046fba517f:search

```yaml
regex_id: 3b574a02c08ac807e2a273046fba517f
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/cerebro/src/util/process-env-variables.ts:63:34"
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

## usage_mismatch:3bb297db31c18a58a5d461a3c8082ba5:search

```yaml
regex_id: 3bb297db31c18a58a5d461a3c8082ba5
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/apps/web/src/pages/home/sections/hero.tsx:124:34"
```

### Pattern

`^(import|from|const|await|export|async|function|type)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3c1ae435eea3ccdc3c723fba14246ed0:search

```yaml
regex_id: 3c1ae435eea3ccdc3c723fba14246ed0
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/io/gitignore.ts:47:15"
```

### Pattern

`^\*{0,2}\/?\.vis(?:\/\*{0,2})?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3c47d7b341eded1c2f8bda533f26a63b:search

```yaml
regex_id: 3c47d7b341eded1c2f8bda533f26a63b
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/string/src/case/identify-case.ts:12:19"
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

## intent_mismatch:3c690dbf11e06ca1cc185152bc19e4d9:email

```yaml
regex_id: 3c690dbf11e06ca1cc185152bc19e4d9
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/crypto/dkim-signer.ts:171:48"
```

### Pattern

`\s+`

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

## usage_mismatch:3d81a2599158bea0b359bece61c77367:search

```yaml
regex_id: 3d81a2599158bea0b359bece61c77367
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/disposable-email-domains/scripts/disposable-email-sync-manager.js:16:27"
```

### Pattern

`@([^\s@]+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:3dbff37064ab5fb740ec03a0df11b3b5:email

```yaml
regex_id: 3dbff37064ab5fb740ec03a0df11b3b5
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/deliverability/list-unsubscribe.ts:106:33"
```

### Pattern

`<[^<>]+>`

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

## intent_mismatch:3e90aeadef43943a56f3a26b1c35dfb8:email

```yaml
regex_id: 3e90aeadef43943a56f3a26b1c35dfb8
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/utils/encode-mime-header.ts:8:24"
```

### Pattern

`[^\u0000-\u007F]`

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

## usage_mismatch:3ebd20678d8b00ea15cfe9395a42265d:search

```yaml
regex_id: 3ebd20678d8b00ea15cfe9395a42265d
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/inspector/src/utils/inspect-property.ts:4:24"
```

### Pattern

`^"|"$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3ee1668d16819080c81600754b0bcd00:search

```yaml
regex_id: 3ee1668d16819080c81600754b0bcd00
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/reply-parser.ts:17:4"
```

### Pattern

`^.+\btarihinde\b.+yazdı:$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3f613be12e4facfd1ffb0e64e969a0d3:search

```yaml
regex_id: 3f613be12e4facfd1ffb0e64e969a0d3
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/package/src/lockfile.ts:120:23"
```

### Pattern

`^\s+integrity[\s:]+"?([^"\s]+)"?`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3fa03f888b2dafde3b51f9a7ae3316a7:search

```yaml
regex_id: 3fa03f888b2dafde3b51f9a7ae3316a7
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/tui/src/ink/parse-keypress.ts:7:22"
```

### Pattern

`^\u001B([a-z0-9])$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3fbec96fbbe9791a2fdb164e7ddd20aa:search

```yaml
regex_id: 3fbec96fbbe9791a2fdb164e7ddd20aa
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/workflow/workflow/src/store/sql-store.ts:7:27"
```

### Pattern

`^[A-Z_]\w*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3fcd7c7f7cdb9d321209b534bba885ce:search

```yaml
regex_id: 3fcd7c7f7cdb9d321209b534bba885ce
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email-verifier/src/internal/address.ts:5:27"
```

### Pattern

`\.$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:40593facd0915266d111bce9f15b7ad3:search

```yaml
regex_id: 40593facd0915266d111bce9f15b7ad3
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/print-config.ts:39:29"
```

### Pattern

`\.(?:pem|gpg|key|asc|p12|pfx)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:412fda6bc0f68fc164999f194e31e8ce:email

```yaml
regex_id: 412fda6bc0f68fc164999f194e31e8ce
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/reply-parser.ts:10:4"
```

### Pattern

`^Am .*schrieb.*:$`

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

## usage_mismatch:412fda6bc0f68fc164999f194e31e8ce:search

```yaml
regex_id: 412fda6bc0f68fc164999f194e31e8ce
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/reply-parser.ts:10:4"
```

### Pattern

`^Am .*schrieb.*:$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:413f68a31eb9dda3d5d883118ac3269b:search

```yaml
regex_id: 413f68a31eb9dda3d5d883118ac3269b
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/error/src/stacktrace/parse-stacktrace.ts:82:19"
```

### Pattern

`^\s*in\s(?:([^\\/]+(?:\s\[as\s\S+\])?)\s\(?)?\(at?\s?(.*?):(\d+)(?::(\d+))?\)?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:439b23d22c2c37eb7c794f6feb562e20:email

```yaml
regex_id: 439b23d22c2c37eb7c794f6feb562e20
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/reply-parser.ts:24:4"
```

### Pattern

`^-{2,}\s*Original Message\s*-{2,}`

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

## usage_mismatch:439b23d22c2c37eb7c794f6feb562e20:search

```yaml
regex_id: 439b23d22c2c37eb7c794f6feb562e20
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/reply-parser.ts:24:4"
```

### Pattern

`^-{2,}\s*Original Message\s*-{2,}`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4478d04aaf41da0f5a1b4620107a2a9d:search

```yaml
regex_id: 4478d04aaf41da0f5a1b4620107a2a9d
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/lint-fmt/adapters/markdownlint.ts:26:24"
```

### Pattern

`^([^:]+):(\d+)(?::(\d+))?\s+([\w/-]+)\s+(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:44fc9e60992364ff422d318d8888c0b6:search

```yaml
regex_id: 44fc9e60992364ff422d318d8888c0b6
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/runtime/toolchain.ts:447:22"
```

### Pattern

`^([a-z][\w-]*)\s*=\s*"?([^"\n#]+?)"?\s*(?:#.*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:458a8cf9ddc5c38cf8c327b8a5d4a5ae:search

```yaml
regex_id: 458a8cf9ddc5c38cf8c327b8a5d4a5ae
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/changelog/default.ts:69:26"
```

### Pattern

`^(?<type>[a-z]+)(?:\([^)]+\))?!?:\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:47abc9e111e5be14892b852cdaff58d8:search

```yaml
regex_id: 47abc9e111e5be14892b852cdaff58d8
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/parser/dumper.ts:54:19"
```

### Pattern

`^\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:48489f8a72f7b8338ea1389dae6961f6:search

```yaml
regex_id: 48489f8a72f7b8338ea1389dae6961f6
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/tui-kit/src/tabs.tsx:23:27"
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

## usage_mismatch:4850d80cdd7132b087f7906b9c646d76:search

```yaml
regex_id: 4850d80cdd7132b087f7906b9c646d76
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/free-email-domains/scripts/free-email-sync-manager.js:17:32"
```

### Pattern

`^[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?(?:\.[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4899fe235ffdb6118682812ddf1c8326:search

```yaml
regex_id: 4899fe235ffdb6118682812ddf1c8326
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/storage/storage/src/storage/bunny/bunny-storage.ts:98:8"
```

### Pattern

`^file not found`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:48cd426dba7047d3e9687072d8bea457:search

```yaml
regex_id: 48cd426dba7047d3e9687072d8bea457
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/providers/autosend/provider.ts:35:28"
```

### Pattern

`^[A-Z0-9-]{1,76}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4a19608a773bdd966cbb6f312fa5cb66:search

```yaml
regex_id: 4a19608a773bdd966cbb6f312fa5cb66
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/tui/src/ink/parse-keypress.ts:9:22"
```

### Pattern

`^\u001B+([ON[]|\[\[)(?:(\d+)(?:;(\d+))?([~^$])|(?:1;)?(\d+)?([a-zA-Z]))`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4a299bf35f49c026c9a80e67b760346e:search

```yaml
regex_id: 4a299bf35f49c026c9a80e67b760346e
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/runtime/ts-loader.ts:28:14"
```

### Pattern

`\.[cm]?tsx?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4a68de948727eb00fd24707c1faf4c2f:search

```yaml
regex_id: 4a68de948727eb00fd24707c1faf4c2f
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/cerebro/src/cli.ts:42:34"
```

### Pattern

`^--(\S+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4a9d619bbd8cddab7ec94f9127709da6:search

```yaml
regex_id: 4a9d619bbd8cddab7ec94f9127709da6
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/packem.config.ts:32:16"
```

### Pattern

`^@visulima\/tabular(\/|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:4c05c509656ebf09f267b59c0ab2db3d:email

```yaml
regex_id: 4c05c509656ebf09f267b59c0ab2db3d
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/utils.ts:5:27"
```

### Pattern

`\s+`

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

## usage_mismatch:4c1f3edd28f64be0c0e62c252bab26b8:search

```yaml
regex_id: 4c1f3edd28f64be0c0e62c252bab26b8
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/reply-parser.ts:26:4"
```

### Pattern

`^_{5,}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4c4e7227d61a3bb81795158b857bd0de:search

```yaml
regex_id: 4c4e7227d61a3bb81795158b857bd0de
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/parser/properties.ts:21:27"
```

### Pattern

`^(?:!|!!|![a-z-]+!)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4c935f119445ccc8a123c5727096a00a:search

```yaml
regex_id: 4c935f119445ccc8a123c5727096a00a
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/task-runner/src/import-boundaries.ts:97:23"
```

### Pattern

`^\s*type\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4cf1fcc4dea5fdf1bb797cbb4676ec90:search

```yaml
regex_id: 4cf1fcc4dea5fdf1bb797cbb4676ec90
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/storage/storage/src/handler/multipart/multipart.ts:16:16"
```

### Pattern

`^multipart\/.+|application\/x-www-form-urlencoded$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4d174915eab70b13a3d7d714e88e3a9b:search

```yaml
regex_id: 4d174915eab70b13a3d7d714e88e3a9b
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/tui-kit/src/number-input.tsx:104:22"
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

## usage_mismatch:4da3511fdeb9d0a46d04ea2e41a70a9f:search

```yaml
regex_id: 4da3511fdeb9d0a46d04ea2e41a70a9f
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/api/jsdoc-open-api/src/jsdoc/comments-to-open-api.ts:8:27"
```

### Pattern

`\[\]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4dc5d76975153b68fd337a58c92c7655:search

```yaml
regex_id: 4dc5d76975153b68fd337a58c92c7655
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/error/src/stacktrace/parse-stacktrace.ts:116:28"
```

### Pattern

`^.*?\s*at\s.*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4e6827849218a620fe263275e88745f7:search

```yaml
regex_id: 4e6827849218a620fe263275e88745f7
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/release/doctor/handler.ts:725:51"
```

### Pattern

`\.(?:pem|gpg|key|asc|p12|pfx)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:50780fe98456ceba6f8c4c6aca31bbed:search

```yaml
regex_id: 50780fe98456ceba6f8c4c6aca31bbed
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/task-runner/src/file-access-tracker.ts:492:12"
```

### Pattern

`node_modules\/.package-lock\.json$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:521b979677a9e70dc2f3b20774328af2:search

```yaml
regex_id: 521b979677a9e70dc2f3b20774328af2
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/free-email-domains/src/index.ts:31:27"
```

### Pattern

`\.$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5299fa9b35da7528739029b98d5de430:search

```yaml
regex_id: 5299fa9b35da7528739029b98d5de430
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/dev-toolbar/src/apps/inspector/element-utils.ts:433:23"
```

### Pattern

`[_-][a-f0-9]{5,}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5313faa61b4239c6751ba771f3aa4ffa:search

```yaml
regex_id: 5313faa61b4239c6751ba771f3aa4ffa
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/string/src/case/identify-case.ts:13:27"
```

### Pattern

`^[a-z][a-z0-9]*(?:[A-Z][a-z0-9]*)+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:531ddae422e6b290dff29870ea57c428:search

```yaml
regex_id: 531ddae422e6b290dff29870ea57c428
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/util/gitignore-matcher.ts:15:26"
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

## usage_mismatch:53837f4509c6753c638f0546065d789f:search

```yaml
regex_id: 53837f4509c6753c638f0546065d789f
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/schema/schemas.ts:55:22"
```

### Pattern

`^[-+]?0b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:557ffbddd51b07e2b5bf158d916c43ee:search

```yaml
regex_id: 557ffbddd51b07e2b5bf158d916c43ee
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/native-config-sync.ts:165:20"
```

### Pattern

`^\s*ignore-scripts\s*=\s*true\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:55ba297b74f4726afeaa82c599929fd1:search

```yaml
regex_id: 55ba297b74f4726afeaa82c599929fd1
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/exotic-subdeps.ts:76:11"
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

## usage_mismatch:55d021ce4ab8bfb6941cc8a62a17d4d9:search

```yaml
regex_id: 55d021ce4ab8bfb6941cc8a62a17d4d9
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/min-release-age.ts:101:81"
```

### Pattern

`^\s*min-release-age\s*=.*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:560c6d7c66c725afa5b7178dea4e06bb:search

```yaml
regex_id: 560c6d7c66c725afa5b7178dea4e06bb
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/is-ansi-color-supported/src/is-color-supported.server.ts:18:20"
```

### Pattern

`^(9\.(0*[1-9]\d*)\.|\d{2,}\.)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5644400287976f2aabf88b7a1d299407:search

```yaml
regex_id: 5644400287976f2aabf88b7a1d299407
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/dev-toolbar/src/apps/tailwind/tailwind-app.tsx:17:26"
```

### Pattern

`^--`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:566ce6c08ebe52c429b44a80c32627d8:search

```yaml
regex_id: 566ce6c08ebe52c429b44a80c32627d8
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/cerebro/src/util/command-line-commands.ts:12:30"
```

### Pattern

`^-([^\d-]{2,})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:574684c33be8de2d804b7b8f29ddf586:email

```yaml
regex_id: 574684c33be8de2d804b7b8f29ddf586
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/render/cid.ts:2:22"
```

### Pattern

`\b(src|href)\s*=\s*(["'])cid:([^"']+)\2`

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

## usage_mismatch:577c62e636703ed64bdc0637a98cd957:search

```yaml
regex_id: 577c62e636703ed64bdc0637a98cd957
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/error/src/stacktrace/parse-stacktrace.ts:86:35"
```

### Pattern

`^(?:.*@)?(.*):(\d+):(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:578461d593869e4f3dfdd9c2fb7ee706:search

```yaml
regex_id: 578461d593869e4f3dfdd9c2fb7ee706
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/storage/storage/src/storage/cloudinary/cloudinary-storage.ts:52:28"
```

### Pattern

`^cloudinary:\/\/([^:]+):([^@]+)@(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:57f9550905f7eb5b2e712c7fc89a7ce0:search

```yaml
regex_id: 57f9550905f7eb5b2e712c7fc89a7ce0
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/string/src/case/identify-case.ts:6:28"
```

### Pattern

`^[A-Z0-9_]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:580d378dde3b6b66b8553d0bb7f6e506:email

```yaml
regex_id: 580d378dde3b6b66b8553d0bb7f6e506
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/render/dark-mode.ts:3:18"
```

### Pattern

`<html[^<>]*>`

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

## usage_mismatch:583443f4a7d8e5a47f237d38e4f463a0:search

```yaml
regex_id: 583443f4a7d8e5a47f237d38e4f463a0
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/string/src/case/identify-case.ts:14:27"
```

### Pattern

`^[a-z]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:58834eadcc53fa522a9f0eb93bc0106d:search

```yaml
regex_id: 58834eadcc53fa522a9f0eb93bc0106d
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/package/src/lockfile.ts:106:23"
```

### Pattern

`^[A-Z0-9+/]+={0,2}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5912fddc9115540a7a3cd607a03103d6:search

```yaml
regex_id: 5912fddc9115540a7a3cd607a03103d6
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/filesystem/fs/src/sanitize.ts:23:29"
```

### Pattern

`^(?:\.+[/\\]+)+|^\.+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:59cbf68a9c3efe75e3d71a38c679ec73:search

```yaml
regex_id: 59cbf68a9c3efe75e3d71a38c679ec73
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/disposable-email-domains/scripts/disposable-email-sync-manager.js:13:23"
```

### Pattern

`^\*\.`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5a3ba97906428602b8b3f6d0a069af12:search

```yaml
regex_id: 5a3ba97906428602b8b3f6d0a069af12
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/runtime/toolchain.ts:1774:58"
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

## usage_mismatch:5aba18c3eefd0e8973376181e4b66a02:search

```yaml
regex_id: 5aba18c3eefd0e8973376181e4b66a02
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/tui/src/ink/color-utils.ts:37:17"
```

### Pattern

`^rgb\(\s?(\d+),\s?(\d+),\s?(\d+)\s?\)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5ac45e2ecf9e23a04036830367aef170:search

```yaml
regex_id: 5ac45e2ecf9e23a04036830367aef170
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/package/src/lockfile.ts:118:21"
```

### Pattern

`^\s+version:?\s+"?([^"\n]+)"?`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5af947386493ae79ad281726e0f83a9e:search

```yaml
regex_id: 5af947386493ae79ad281726e0f83a9e
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/free-email-domains/scripts/free-email-sync-manager.js:13:23"
```

### Pattern

`^\*\.`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5c71c0dcff69c1c7ba62183b3d3c1a99:search

```yaml
regex_id: 5c71c0dcff69c1c7ba62183b3d3c1a99
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/fmt/src/inspect-colors.ts:188:6"
```

### Pattern

`^hsla?\(\s*([+-]?(?:\d+(?:\.\d+)?|\.\d+))\s*,\s*([+-]?(?:\d+(?:\.\d+)?|\.\d+))%\s*,\s*([+-]?(?:\d+(?:\.\d+)?|\.\d+))%\s*(,\s*([+-]?(?:\d+(?:\.\d+)?|\.\d+))\s*)?\)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5cd8317473bfc8097673a807a4c470e7:search

```yaml
regex_id: 5cd8317473bfc8097673a807a4c470e7
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/source-map/src/load-source-map.ts:14:23"
```

### Pattern

`^data:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5d037a00fcad3ed341783a742b2f7d00:search

```yaml
regex_id: 5d037a00fcad3ed341783a742b2f7d00
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/min-release-age.ts:72:84"
```

### Pattern

`^[ \t]*minimumReleaseAge[ \t]*=.*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5d0de5895cd87a204351ed98a623952f:search

```yaml
regex_id: 5d0de5895cd87a204351ed98a623952f
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/parser/dumper.ts:55:27"
```

### Pattern

`[ \t]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5d58381de1203a9f0fd4ff406ae587f9:search

```yaml
regex_id: 5d58381de1203a9f0fd4ff406ae587f9
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/is-ansi-color-supported/src/is-color-supported.server.ts:11:27"
```

### Pattern

`^-{1,2}(color=256)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5ee239defa84a41d83f2ac1dad3a0fb9:search

```yaml
regex_id: 5ee239defa84a41d83f2ac1dad3a0fb9
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/multi-eco-lockfiles.ts:219:20"
```

### Pattern

`^ {4}([^ ()]+) \(([^()]+)\)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:5f389573d1d8a1c9c54da97169226c4e:email

```yaml
regex_id: 5f389573d1d8a1c9c54da97169226c4e
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/providers/aws-ses/provider.ts:258:56"
```

### Pattern

`<Max24HourSend>(.*?)<\/Max24HourSend>`

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

## usage_mismatch:5fa77aa3009ccb13e9e887d319327d9f:search

```yaml
regex_id: 5fa77aa3009ccb13e9e887d319327d9f
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/task-runner/src/lockfile-hasher.ts:148:30"
```

### Pattern

`^\s{2}[/'"]?(?:@([^/@']+)\/)?([^@']+)@(\d[^:'"\s]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:5fbd0b6727bc64e499f7fd3a002fe485:email

```yaml
regex_id: 5fbd0b6727bc64e499f7fd3a002fe485
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/crypto/smime-encrypter.ts:33:20"
```

### Pattern

`-----END[^-]+-----`

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

## usage_mismatch:6015f010e67f947708a70c9b2e486cd7:search

```yaml
regex_id: 6015f010e67f947708a70c9b2e486cd7
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/schema/schemas.ts:51:22"
```

### Pattern

`^([-+])?\.(?:inf|Inf|INF)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:60daa456cafc04f825ba2b6ba771de52:search

```yaml
regex_id: 60daa456cafc04f825ba2b6ba771de52
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/ono/src/error-inspector/components/stack-trace-viewer/index.ts:16:32"
```

### Pattern

`^file:\/\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:617eafd2fef2669346f90475c5b879f5:search

```yaml
regex_id: 617eafd2fef2669346f90475c5b879f5
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/task-runner/src/task-hasher.ts:255:13"
```

### Pattern

`^[A-Z_]\w*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:61be04749804378c4bef3f39fb1fb036:search

```yaml
regex_id: 61be04749804378c4bef3f39fb1fb036
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/preflight/vite-client-override.ts:255:13"
```

### Pattern

`^y(?:es)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6229bb14b73debd0ee78bc9578eaa70e:search

```yaml
regex_id: 6229bb14b73debd0ee78bc9578eaa70e
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/humanizer/src/parse-duration.ts:115:21"
```

### Pattern

`^(?:(\d+):)?(?:(\d+):)?(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6232c415a2823544747e7118d3affd80:search

```yaml
regex_id: 6232c415a2823544747e7118d3affd80
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/update/ecosystems/prompt.ts:96:8"
```

### Pattern

`^[\d ,]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:624809cbc86e27d52839da09796ca0cc:search

```yaml
regex_id: 624809cbc86e27d52839da09796ca0cc
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/min-release-age.ts:130:22"
```

### Pattern

`^minimumReleaseAge[ \t]*:.*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6274ad6d81db1db6a552326820406319:search

```yaml
regex_id: 6274ad6d81db1db6a552326820406319
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/task-runner/src/affected.ts:20:9"
```

### Pattern

`^[\w./~^@{}][\w.\-/~^@{}]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6338099329a2f5d4b5db2ee7588fb590:search

```yaml
regex_id: 6338099329a2f5d4b5db2ee7588fb590
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/update/ecosystems/gitlab/scanner.ts:351:16"
```

### Pattern

`^(?:\.git|node_modules|\.pnpm-store|\.turbo|\.nx|dist|build|\.cache)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:63438e2c983a23cc764a6674369532ef:search

```yaml
regex_id: 63438e2c983a23cc764a6674369532ef
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/tui/failure-render.ts:28:27"
```

### Pattern

`^(?<name>(?:[A-Z][\w$]*)?(?:Error|Exception))(?::[ \t](?<message>.*))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6440465d6ca99838efc77b321b5e4e7b:search

```yaml
regex_id: 6440465d6ca99838efc77b321b5e4e7b
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/update/ecosystems/gitlab/scanner.ts:68:21"
```

### Pattern

`^\s*-?\s*component:\s*(['"]?)([^'"\s#]+)\1(\s*#.*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6445bc73bb075618b20d225c8934be4d:search

```yaml
regex_id: 6445bc73bb075618b20d225c8934be4d
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/utils/parse-eml.ts:15:32"
```

### Pattern

`[\r\n]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:648fde21c037e0e05fd8926e44ad6ef7:email

```yaml
regex_id: 648fde21c037e0e05fd8926e44ad6ef7
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/crypto/smime-signer.ts:46:20"
```

### Pattern

`\s`

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

## usage_mismatch:64bc5a537f56c2a68515a375d2035977:search

```yaml
regex_id: 64bc5a537f56c2a68515a375d2035977
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/webhooks/ses-sns.ts:54:29"
```

### Pattern

`\.$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:64f08ddcf81ce25ce51370aef33ba52b:search

```yaml
regex_id: 64f08ddcf81ce25ce51370aef33ba52b
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/migrate/constants.ts:53:4"
```

### Pattern

`^((?:[A-Z_][A-Z0-9_]*(?:=\S*)?\s+)*)(pnpm|pnpm exec|npx|yarn|yarn run|npm exec|npm run|bunx|bun run|bun x)\s+nano-staged\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:65992252b9760b319262b8e8651e82ad:search

```yaml
regex_id: 65992252b9760b319262b8e8651e82ad
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/cerebro/src/util/arg-processing/get-parameter-option.ts:3:27"
```

### Pattern

`^-{1,2}(\w+)(=(.+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:65cdb8266e83f29df15667d14067828b:search

```yaml
regex_id: 65cdb8266e83f29df15667d14067828b
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/change-file.ts:508:48"
```

### Pattern

`^[a-z0-9-]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:66716f718f9205538e095509a75609cb:search

```yaml
regex_id: 66716f718f9205538e095509a75609cb
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/transitive-fix.ts:166:12"
```

### Pattern

`^overrides\s*:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6695948456c90da6492b012e3d053a89:search

```yaml
regex_id: 6695948456c90da6492b012e3d053a89
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/filesystem/fs/src/utils/ini-preserve.ts:8:29"
```

### Pattern

`^\s*\[([^\]]+)\]\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6764fc2fb1dca50f1cb6b7258aad0fa5:search

```yaml
regex_id: 6764fc2fb1dca50f1cb6b7258aad0fa5
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/replay.ts:88:65"
```

### Pattern

`^\d+\.\d+\.\d+-`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:689f773403ade5d4288c5947d18ce88f:search

```yaml
regex_id: 689f773403ade5d4288c5947d18ce88f
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/secret-scanner/scripts/kingfisher-converter.mjs:21:34"
```

### Pattern

`^[0-9_-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6906f0fc07660351d34f99f269ef115a:search

```yaml
regex_id: 6906f0fc07660351d34f99f269ef115a
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/runtime/runtime-check.ts:102:19"
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

## usage_mismatch:69c2477dbdad132296bede98c3f439be:search

```yaml
regex_id: 69c2477dbdad132296bede98c3f439be
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/storage/storage/src/handler/tus/tus.ts:292:23"
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

## usage_mismatch:69dda4ceaacc099b6321cea448761adc:search

```yaml
regex_id: 69dda4ceaacc099b6321cea448761adc
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/change-file.ts:252:50"
```

### Pattern

`^\d+\.\d+\.\d+(?:[-+].*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6a77c6405a69e267f1bc6339b3cc21bb:search

```yaml
regex_id: 6a77c6405a69e267f1bc6339b3cc21bb
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/filesystem/path/src/path.ts:28:24"
```

### Pattern

`^[A-Z]:$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6ac6fb74c7c83558ed952d6ec0632d73:search

```yaml
regex_id: 6ac6fb74c7c83558ed952d6ec0632d73
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/transitive-fix.ts:179:42"
```

### Pattern

`^overrides\s*:[^\n]*\n(?:[ \t][^\n]*\n)*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6b39a55e839a31255ebe92d3c1ab3359:search

```yaml
regex_id: 6b39a55e839a31255ebe92d3c1ab3359
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/cerebro/src/cli.ts:40:35"
```

### Pattern

`^-([^\d-])$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6b6c2cc9a6f71d03f849782c5f73a341:search

```yaml
regex_id: 6b6c2cc9a6f71d03f849782c5f73a341
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/update/ecosystems/gitlab/scanner.ts:95:24"
```

### Pattern

`^(\s*-\s*name:\s*)(['"]?)([^'"\s#]+)\2(\s*#.*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6b955b8bd09978bef6efb5fc9d55c51d:search

```yaml
regex_id: 6b955b8bd09978bef6efb5fc9d55c51d
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/schema/schemas.ts:57:22"
```

### Pattern

`^[-+]?0x`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6c226ac97410aefe03e64fa9dc6551e8:search

```yaml
regex_id: 6c226ac97410aefe03e64fa9dc6551e8
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/version-actions/jsr.ts:87:23"
```

### Pattern

`^@[a-z0-9-]+\/[a-z0-9-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:6c5a30f10a0cbd3cf048c4800b4d9663:email

```yaml
regex_id: 6c5a30f10a0cbd3cf048c4800b4d9663
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/disposable-email-domains/scripts/disposable-email-sync-manager.js:10:25"
```

### Pattern

`github\.com\/([^/]+)\/([^/]+)`

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

## usage_mismatch:6c78c1f60ad2d0df0a70ea48175cbc6e:search

```yaml
regex_id: 6c78c1f60ad2d0df0a70ea48175cbc6e
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/tui/src/ink/parse-keypress.ts:532:28"
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

## usage_mismatch:6db411df1a4c2106ce46d9b635deae90:search

```yaml
regex_id: 6db411df1a4c2106ce46d9b635deae90
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/runtime/runtime-diagnostics.ts:424:70"
```

### Pattern

`^"|"$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6e3bc7a910659fc1a59b52255a033db0:search

```yaml
regex_id: 6e3bc7a910659fc1a59b52255a033db0
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/filesystem/fs/src/ensure/ensure-symlink-sync.ts:15:50"
```

### Pattern

`^(?:msys|cygwin)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6ea2db6ba8677d659d1146932d64a535:search

```yaml
regex_id: 6ea2db6ba8677d659d1146932d64a535
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/changelog/default.ts:107:66"
```

### Pattern

`^[a-z]+(?:\([^)]+\))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6f436be3260b9c4006e98d1f29e5d825:search

```yaml
regex_id: 6f436be3260b9c4006e98d1f29e5d825
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/apps/web/scripts/copy-package-docs.js:337:20"
```

### Pattern

`^\.\.?\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6f47e7f4cfc8d9630d8917f1b2da5f43:search

```yaml
regex_id: 6f47e7f4cfc8d9630d8917f1b2da5f43
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/schema/schemas.ts:33:20"
```

### Pattern

`^-?(?:0|[1-9]\d*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6f89daab51b4307b46f8d18e3897b10a:search

```yaml
regex_id: 6f89daab51b4307b46f8d18e3897b10a
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/update/ecosystems/actions/scanner.ts:51:21"
```

### Pattern

`^\s*-?\s*uses:\s*(['"]?)([^'"\s#]+)\1(?:\s*#\s*(.+))?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6fb18897d47fdc63c469bb7546a36127:search

```yaml
regex_id: 6fb18897d47fdc63c469bb7546a36127
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/schema/schemas.ts:45:24"
```

### Pattern

`^[-+]?(?:\d[\d_]*)?\.[\d_]*(?:e[-+]?\d+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:700df623e57a7892206c30f7de30068b:search

```yaml
regex_id: 700df623e57a7892206c30f7de30068b
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/humanizer/src/parse-duration.ts:116:29"
```

### Pattern

`^[+-]?\d+(?:\.\d+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:704d58fb2d80dc27e177ee607976dfca:search

```yaml
regex_id: 704d58fb2d80dc27e177ee607976dfca
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/exotic-subdeps.ts:67:8"
```

### Pattern

`^(?:github|gitlab|bitbucket|gist):`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:707b69e4af1d4b908d84322b183050f5:search

```yaml
regex_id: 707b69e4af1d4b908d84322b183050f5
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/schema/schemas.ts:49:36"
```

### Pattern

`^[-+]?[1-9][\d_]*(?::[0-5]?\d)+\.[\d_]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:7089802e8fb9b12858f8e883081fff16:email

```yaml
regex_id: 7089802e8fb9b12858f8e883081fff16
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/utils/parse-eml.ts:9:26"
```

### Pattern

`^[ \t]`

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

## usage_mismatch:7089802e8fb9b12858f8e883081fff16:search

```yaml
regex_id: 7089802e8fb9b12858f8e883081fff16
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/utils/parse-eml.ts:9:26"
```

### Pattern

`^[ \t]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:710e688fba69e12082f86a402df181f8:email

```yaml
regex_id: 710e688fba69e12082f86a402df181f8
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/crypto/arc-signer.ts:13:23"
```

### Pattern

` $`

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

## usage_mismatch:710e688fba69e12082f86a402df181f8:search

```yaml
regex_id: 710e688fba69e12082f86a402df181f8
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/crypto/arc-signer.ts:13:23"
```

### Pattern

` $`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:717d462eefbd1ff3123690c70db9be48:search

```yaml
regex_id: 717d462eefbd1ff3123690c70db9be48
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/schema/resolve-scalar.ts:24:17"
```

### Pattern

`^[-+]?(?:\.\d+|\d+(?:\.\d*)?)(?:e[-+]?\d+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:71e0cb567b822f9dae6408be62921093:search

```yaml
regex_id: 71e0cb567b822f9dae6408be62921093
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/apply-release-plan.ts:228:24"
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

## usage_mismatch:725e3efb58fdf9604dc6c320ff43b415:search

```yaml
regex_id: 725e3efb58fdf9604dc6c320ff43b415
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/runtime/toolchain.ts:1794:58"
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

## usage_mismatch:72a8a6129ae645ad8e5e23c017012763:search

```yaml
regex_id: 72a8a6129ae645ad8e5e23c017012763
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/packem.config.ts:34:16"
```

### Pattern

`^react\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:740909ee62ae38b1db0d8127e6651de0:search

```yaml
regex_id: 740909ee62ae38b1db0d8127e6651de0
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/task-runner/src/archive.ts:98:67"
```

### Pattern

`^[a-z]:[\\/]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7474e92b3de56e40265c19fa89126b68:search

```yaml
regex_id: 7474e92b3de56e40265c19fa89126b68
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/source-map/src/load-source-map.ts:16:35"
```

### Pattern

`^[ \t]*\/\*[@#][ \t]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:74f1796dfdc0e8a9de3b8e0d06fa68dd:search

```yaml
regex_id: 74f1796dfdc0e8a9de3b8e0d06fa68dd
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/update/ecosystems/docker/scanner.ts:224:25"
```

### Pattern

`^\s*image:\s*(['"]?)([^'"\s#]+)\1(\s*#.*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:75f5aa7bb93543197a7ab6f4e975d7ef:search

```yaml
regex_id: 75f5aa7bb93543197a7ab6f4e975d7ef
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/migrate/kingfisher.ts:63:12"
```

### Pattern

`^\s*-\s*filepath\s*:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:76d5185033fa1168057e954de02466a8:search

```yaml
regex_id: 76d5185033fa1168057e954de02466a8
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/error/src/stacktrace/parse-stacktrace.ts:114:24"
```

### Pattern

`^\s*in\s.*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:76db5366b61893e576f2419d2333e21b:search

```yaml
regex_id: 76db5366b61893e576f2419d2333e21b
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/task/selectors.ts:230:47"
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

## usage_mismatch:76e80ae97d8a8854cb3071a0e741adb1:search

```yaml
regex_id: 76e80ae97d8a8854cb3071a0e741adb1
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/iso-locale/src/locale.ts:11:24"
```

### Pattern

`^[\da-z]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:76e981e609c3f2b69184da5c1f21c20c:search

```yaml
regex_id: 76e981e609c3f2b69184da5c1f21c20c
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/min-release-age.ts:131:34"
```

### Pattern

`^minimumReleaseAge[ \t]*:.*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:77f3a6e86a019ef96b6b7ed063d98f46:search

```yaml
regex_id: 77f3a6e86a019ef96b6b7ed063d98f46
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/utils/decode-mime-header.ts:40:27"
```

### Pattern

`^utf-?8$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:7867275ea3bcb3fe864d00da98494f04:email

```yaml
regex_id: 7867275ea3bcb3fe864d00da98494f04
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/crypto/arc-signer.ts:12:23"
```

### Pattern

`\s+`

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

## usage_mismatch:78a5a9a2557735fda20966356d1355e7:search

```yaml
regex_id: 78a5a9a2557735fda20966356d1355e7
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/schema/resolve-scalar.ts:26:21"
```

### Pattern

`^([-+]?)\.(?:inf|Inf|INF)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:7960524a0344aec92d2719afef260671:email

```yaml
regex_id: 7960524a0344aec92d2719afef260671
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/reply-parser.ts:12:4"
```

### Pattern

`^Le .*a écrit ?:$`

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

## usage_mismatch:7960524a0344aec92d2719afef260671:search

```yaml
regex_id: 7960524a0344aec92d2719afef260671
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/reply-parser.ts:12:4"
```

### Pattern

`^Le .*a écrit ?:$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7a6ea908d81a8f38d4fa769ac373e3fd:search

```yaml
regex_id: 7a6ea908d81a8f38d4fa769ac373e3fd
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/migrate/kingfisher.ts:82:60"
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

## usage_mismatch:7ad75011b2a8030b09aa0075cb462936:search

```yaml
regex_id: 7ad75011b2a8030b09aa0075cb462936
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/vite-overlay/src/utils/find-module-for-path.ts:5:27"
```

### Pattern

`^[./]*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7b0494c424abdf377b1470bf8256e96f:search

```yaml
regex_id: 7b0494c424abdf377b1470bf8256e96f
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/vite-overlay/src/overlay/client/runtime.js:20:21"
```

### Pattern

`^\/@fs\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7bd4e822bcd7223ef619410143185b72:search

```yaml
regex_id: 7bd4e822bcd7223ef619410143185b72
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/fmt/src/inspect-colors.ts:185:6"
```

### Pattern

`^rgba?\(\s*([+-]?(?:\d+(?:\.\d+)?|\.\d+))\s*,\s*([+-]?(?:\d+(?:\.\d+)?|\.\d+))\s*,\s*([+-]?(?:\d+(?:\.\d+)?|\.\d+))\s*(,\s*([+-]?(?:\d+(?:\.\d+)?|\.\d+))\s*)?\)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7bdba61d739a40b20b3f230a3290773a:search

```yaml
regex_id: 7bdba61d739a40b20b3f230a3290773a
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/create/discovery.ts:73:37"
```

### Pattern

`^[^/#@][^/#]*\/[^/#]+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7c416ae66efb11539660b75652e60f00:search

```yaml
regex_id: 7c416ae66efb11539660b75652e60f00
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/utils.ts:6:35"
```

### Pattern

`^"|"$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7c615669670c6821045ecedf5659088c:search

```yaml
regex_id: 7c615669670c6821045ecedf5659088c
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/fmt/src/inspect-colors.ts:180:21"
```

### Pattern

`^#([\dA-F]{2})([\dA-F]{2})([\dA-F]{2})([\dA-F]{2})?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7d72c5ff2aec143c796af2fc046e0455:search

```yaml
regex_id: 7d72c5ff2aec143c796af2fc046e0455
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/lint-fmt/adapters/deno.ts:39:72"
```

### Pattern

`^[a-z]:[\\/]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7d72f4dc3d97133063ec19a4c1eee354:search

```yaml
regex_id: 7d72f4dc3d97133063ec19a4c1eee354
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/filesystem/fs/src/utils/ini-preserve.ts:10:27"
```

### Pattern

`\r?\n$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:7e324cb52da62048fd83c6c54b249acb:email

```yaml
regex_id: 7e324cb52da62048fd83c6c54b249acb
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/utils/decode-mime-header.ts:55:27"
```

### Pattern

`=\?([^?]+)\?([bq])\?([^?]*)\?=`

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

## usage_mismatch:7e61a9b98860e045f12ce92134db48b7:search

```yaml
regex_id: 7e61a9b98860e045f12ce92134db48b7
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/dev-toolbar/src/vite-plugin.ts:292:39"
```

### Pattern

`router\.tsx$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7fb5356b42e3a00872d5e6c683fb5f27:search

```yaml
regex_id: 7fb5356b42e3a00872d5e6c683fb5f27
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/package/src/lockfile.ts:464:23"
```

### Pattern

`^ {2}(['"]?[^\s:][^:\n]*?['"]?):\s*\n((?: {4}[^\n]*\n?)+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8067cd9a2cbf19a5a1eb3ee111013fa0:search

```yaml
regex_id: 8067cd9a2cbf19a5a1eb3ee111013fa0
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/iso-locale/src/locale.ts:7:19"
```

### Pattern

`^[a-z]{2,3}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8121af7f57792e7c63c02784eab03053:search

```yaml
regex_id: 8121af7f57792e7c63c02784eab03053
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/vite-overlay/src/overlay/client/runtime.js:19:21"
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

## usage_mismatch:81d2c9c37def8babaaecc63ddfbc1dc3:search

```yaml
regex_id: 81d2c9c37def8babaaecc63ddfbc1dc3
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/storage/storage/src/storage/bunny/bunny-storage.ts:102:8"
```

### Pattern

`^unauthorized access`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:8395b1b9015122b76b6478412eb4100c:email

```yaml
regex_id: 8395b1b9015122b76b6478412eb4100c
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/providers/smtp/provider.ts:166:53"
```

### Pattern

`^(\d{3})[\s-]`

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

## usage_mismatch:8395b1b9015122b76b6478412eb4100c:search

```yaml
regex_id: 8395b1b9015122b76b6478412eb4100c
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/providers/smtp/provider.ts:166:53"
```

### Pattern

`^(\d{3})[\s-]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:83a861ac23998dc2e9058f0cf49fbb7b:search

```yaml
regex_id: 83a861ac23998dc2e9058f0cf49fbb7b
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/update/ecosystems/actions/scanner.ts:53:15"
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

## intent_mismatch:84e8fbc84dee8f7925337af4d2846154:email

```yaml
regex_id: 84e8fbc84dee8f7925337af4d2846154
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/providers/azure/provider.ts:163:65"
```

### Pattern

`endpoint=([^;]+);accesskey=([^;]+)`

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

## usage_mismatch:852aee288a37e66b92d17596d204d11e:search

```yaml
regex_id: 852aee288a37e66b92d17596d204d11e
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/cerebro/src/cli.ts:44:38"
```

### Pattern

`^-([^\d-]{2,})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:86aefebe258358003f1da14ba376c366:search

```yaml
regex_id: 86aefebe258358003f1da14ba376c366
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/min-release-age.ts:72:23"
```

### Pattern

`^[ \t]*minimumReleaseAge[ \t]*=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:86f5d63f1d3f24e2685c5e7098233181:search

```yaml
regex_id: 86f5d63f1d3f24e2685c5e7098233181
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/apps/web/src/routes/r/$name.ts:16:20"
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

## usage_mismatch:8700b40b420ee3a2a6428b3e3fe842dd:search

```yaml
regex_id: 8700b40b420ee3a2a6428b3e3fe842dd
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/string/src/case/identify-case.ts:8:22"
```

### Pattern

`^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:885d6f6dc26effbf609111d590312b58:email

```yaml
regex_id: 885d6f6dc26effbf609111d590312b58
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/crypto/dkim-signer.ts:67:38"
```

### Pattern

`[ \t]+$`

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

## intent_mismatch:88769f33bb06a684fcbfa647a5332392:email

```yaml
regex_id: 88769f33bb06a684fcbfa647a5332392
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/crypto/smime-signer.ts:44:20"
```

### Pattern

`-----BEGIN[^-]+-----`

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

## usage_mismatch:88f886cc236032c0db82ecd10b37361d:search

```yaml
regex_id: 88f886cc236032c0db82ecd10b37361d
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/task-runner/src/task-hasher.ts:251:53"
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

## intent_mismatch:89903f11a9cc89338800b8058e80f26b:email

```yaml
regex_id: 89903f11a9cc89338800b8058e80f26b
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/crypto/format-address.ts:36:39"
```

### Pattern

`\s+`

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

## intent_mismatch:89c1b56894e1b9dbd07eb9a7ffef4073:email

```yaml
regex_id: 89c1b56894e1b9dbd07eb9a7ffef4073
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/reply-parser.ts:8:4"
```

### Pattern

`^On .*wrote:$`

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

## usage_mismatch:89c1b56894e1b9dbd07eb9a7ffef4073:search

```yaml
regex_id: 89c1b56894e1b9dbd07eb9a7ffef4073
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/reply-parser.ts:8:4"
```

### Pattern

`^On .*wrote:$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8b2d8960caafd53d4137329d2b0aecb5:search

```yaml
regex_id: 8b2d8960caafd53d4137329d2b0aecb5
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/error/src/stacktrace/parse-stacktrace.ts:113:33"
```

### Pattern

`^Anonymous function$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8ba7068f76b9f4d3ad88bbf727e23e41:search

```yaml
regex_id: 8ba7068f76b9f4d3ad88bbf727e23e41
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/iso-locale/src/currencies.ts:6:26"
```

### Pattern

`^\d{1,3}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8bad3d024bb4c741b032436c6f081c9c:search

```yaml
regex_id: 8bad3d024bb4c741b032436c6f081c9c
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/native-config-sync.ts:106:46"
```

### Pattern

`^onlyBuiltDependencies:[ \t]*\n(?:[ \t]{2}[^\n]*\n)*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8bb42133a8a024c602faccba704f45e6:search

```yaml
regex_id: 8bb42133a8a024c602faccba704f45e6
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/dev-toolbar/packem.config.ts:11:56"
```

### Pattern

`^virtual:visulima-dev-toolbar-path:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8d134c202b0ec6d2827a38c229710843:search

```yaml
regex_id: 8d134c202b0ec6d2827a38c229710843
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/runtime/toolchain.ts:500:28"
```

### Pattern

`^\[tools\]\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8d8124ef9e32a1a82e8e97d30616c1f1:search

```yaml
regex_id: 8d8124ef9e32a1a82e8e97d30616c1f1
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/update/ecosystems/gitlab/scanner.ts:70:17"
```

### Pattern

`^\s*image:\s*(['"]?)([^'"\s#]+)\1(\s*#.*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8df5b8892b51db194c98116559ff8980:search

```yaml
regex_id: 8df5b8892b51db194c98116559ff8980
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/util/hadolint/fixers.ts:41:23"
```

### Pattern

`^\s*ADD\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8e218ec1cee984bb86d0f97fe3a24fb8:search

```yaml
regex_id: 8e218ec1cee984bb86d0f97fe3a24fb8
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/string/src/case/identify-case.ts:9:32"
```

### Pattern

`^[a-z ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8e960187f6ff8aafcd1a75c7464b5638:search

```yaml
regex_id: 8e960187f6ff8aafcd1a75c7464b5638
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/util/catalog.ts:27:25"
```

### Pattern

`^\/\/(.+)\/:_authToken$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8fd1847ec62585154714ff011df4eca5:search

```yaml
regex_id: 8fd1847ec62585154714ff011df4eca5
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/packem.config.ts:14:16"
```

### Pattern

`^@visulima\/vis(\/|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8ff16f26b4af24e5dd171cf96bea2155:search

```yaml
regex_id: 8ff16f26b4af24e5dd171cf96bea2155
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/util/format-package-json-fields.ts:11:27"
```

### Pattern

`^git\+https:\/\/github\.com\/([^/]+)\/([^/.]+(?:\.git)?)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:902a44f36827b4b7bfac35f56b6f8a8e:search

```yaml
regex_id: 902a44f36827b4b7bfac35f56b6f8a8e
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/cerebro/src/util/command-line-commands.ts:8:27"
```

### Pattern

`^-([^\d-])$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:90be81820849e16d93d1edb0118efdd8:search

```yaml
regex_id: 90be81820849e16d93d1edb0118efdd8
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/storage/storage/src/storage/bunny/bunny-storage.ts:106:8"
```

### Pattern

`^unable to upload file`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:90ceaf1553368f8482939cbddc8c3922:search

```yaml
regex_id: 90ceaf1553368f8482939cbddc8c3922
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/migrate/nx.ts:236:29"
```

### Pattern

`node_modules\/nx\/schemas\/project-schema\.json$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:912953dfff2e0fc359b065dc476ed348:search

```yaml
regex_id: 912953dfff2e0fc359b065dc476ed348
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/native-config-sync.ts:98:43"
```

### Pattern

`^allowBuilds:[ \t]*\n(?:[ \t]{2}[^\n]*\n)*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:91ff5cd2a920f4f4ac04ac441d4710b9:search

```yaml
regex_id: 91ff5cd2a920f4f4ac04ac441d4710b9
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/util/catalog.ts:201:11"
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

## usage_mismatch:9213270b4c8d9b57b47fbeb2c68e367c:search

```yaml
regex_id: 9213270b4c8d9b57b47fbeb2c68e367c
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/update/ecosystems/docker/scanner.ts:142:21"
```

### Pattern

`^\s*FROM\s+(?:--\S+\s+)*([^\s#]+)(?:\s[^#]*)?(#.*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:92cf8b8a2f81281f565034020a150b35:search

```yaml
regex_id: 92cf8b8a2f81281f565034020a150b35
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/is-ansi-color-supported/src/is-color-supported.server.ts:9:26"
```

### Pattern

`^-{1,2}(no-color|no-colors|color=false|color=never)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:935704eecfcdf414594dddd7f090e643:search

```yaml
regex_id: 935704eecfcdf414594dddd7f090e643
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/task/selectors.ts:32:25"
```

### Pattern

`^([@\w\-/]+):(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:941b1e619e9b22d0aa0cfa55fc49ca34:search

```yaml
regex_id: 941b1e619e9b22d0aa0cfa55fc49ca34
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/tui/src/ink/hooks/use-text-buffer.ts:57:26"
```

### Pattern

`\S+\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:94490bf124edae658bb4fd0846c7f01e:email

```yaml
regex_id: 94490bf124edae658bb4fd0846c7f01e
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/providers/smtp/dkim.ts:24:39"
```

### Pattern

`[ \t]+`

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

## usage_mismatch:9486c8c1fcf1e656f6a128f92ed5c7be:search

```yaml
regex_id: 9486c8c1fcf1e656f6a128f92ed5c7be
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/tui-kit/src/select-input.tsx:151:27"
```

### Pattern

`^[1-9]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:953246afea041a7e53d2bf5aa259f68c:email

```yaml
regex_id: 953246afea041a7e53d2bf5aa259f68c
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/thread.ts:97:28"
```

### Pattern

`\s+`

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

## usage_mismatch:9598f844fabf648889f500ba687adec1:search

```yaml
regex_id: 9598f844fabf648889f500ba687adec1
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/string/src/case/identify-case.ts:4:23"
```

### Pattern

`^([A-Z][a-z]*)+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:960113ba4d54f7e3f6bf6b7d8c80cefe:search

```yaml
regex_id: 960113ba4d54f7e3f6bf6b7d8c80cefe
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/multi-eco-lockfiles.ts:68:21"
```

### Pattern

`^\s*name\s*=\s*"([^"]+)"\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9648ce03f37ef1a0a0612b190930b3a1:search

```yaml
regex_id: 9648ce03f37ef1a0a0612b190930b3a1
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/util/catalog.ts:24:30"
```

### Pattern

`^catalog:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:9651a5285e77bb40d470f3bdc39e8002:email

```yaml
regex_id: 9651a5285e77bb40d470f3bdc39e8002
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/free-email-domains/scripts/free-email-sync-manager.js:10:25"
```

### Pattern

`github\.com\/([^/]+)\/([^/]+)`

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

## intent_mismatch:96772498689dc330ff119cc33df4df4f:email

```yaml
regex_id: 96772498689dc330ff119cc33df4df4f
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/crypto/arc-signer.ts:14:21"
```

### Pattern

`^\s*i=(\d+)\s*;`

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

## usage_mismatch:96772498689dc330ff119cc33df4df4f:search

```yaml
regex_id: 96772498689dc330ff119cc33df4df4f
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/crypto/arc-signer.ts:14:21"
```

### Pattern

`^\s*i=(\d+)\s*;`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:969764ffce420dd7e093eaa7a5dfa644:search

```yaml
regex_id: 969764ffce420dd7e093eaa7a5dfa644
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/iso-locale/src/countries.ts:6:26"
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

## usage_mismatch:96b86bb2aa0837a77b68b5a14c1b95e7:search

```yaml
regex_id: 96b86bb2aa0837a77b68b5a14c1b95e7
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/colorize/src/util/convert-hex-to-rgb.ts:33:24"
```

### Pattern

`^#?([a-f\d]{3}|[a-f\d]{6})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:973d1092d12e837ab7097fe01368b65e:search

```yaml
regex_id: 973d1092d12e837ab7097fe01368b65e
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/task/selectors.ts:31:23"
```

### Pattern

`^#([\w\-/]+):(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:97468eb74c81446b07801bd3f029bde7:search

```yaml
regex_id: 97468eb74c81446b07801bd3f029bde7
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/migrate/kingfisher.ts:63:49"
```

### Pattern

`^\s*-\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:97bb49e1378954523d1aa9fe34104bf6:search

```yaml
regex_id: 97bb49e1378954523d1aa9fe34104bf6
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/migrate/constants.ts:28:4"
```

### Pattern

`^((?:[A-Z_][A-Z0-9_]*(?:=\S*)?\s+)*)(pnpm|pnpm exec|npx|yarn|yarn run|npm exec|npm run|bunx|bun run|bun x)\s+lint-staged\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:98094adc12ed08a0b92108d6281e99b2:search

```yaml
regex_id: 98094adc12ed08a0b92108d6281e99b2
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/string/src/constants.ts:87:58"
```

### Pattern

`^(?:[\r\n]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:993fea7385fa9788a018568be095b2d0:search

```yaml
regex_id: 993fea7385fa9788a018568be095b2d0
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/release/add/handler.ts:163:20"
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

## usage_mismatch:998576972a421047b445f5e0a9234f73:search

```yaml
regex_id: 998576972a421047b445f5e0a9234f73
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/ono/src/error-inspector/utils/sanitize.ts:21:26"
```

### Pattern

`^[\w+/-]+={0,2}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9a2c1d37e430a8c5bf72cf74756774c3:search

```yaml
regex_id: 9a2c1d37e430a8c5bf72cf74756774c3
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/update/ecosystems/actions/index.ts:17:37"
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

## usage_mismatch:9d6681a6261b6ce7b867a6c98e98d607:search

```yaml
regex_id: 9d6681a6261b6ce7b867a6c98e98d607
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/dev-toolbar/src/apps/seo/seo-app.tsx:463:25"
```

### Pattern

`\]\]>$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9dccab36cba22cff0bdd3e2f94022ff0:search

```yaml
regex_id: 9dccab36cba22cff0bdd3e2f94022ff0
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/util/catalog.ts:31:26"
```

### Pattern

`^['"]|['"]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9dd5ced768a028b03adacf86f57fc1f0:search

```yaml
regex_id: 9dd5ced768a028b03adacf86f57fc1f0
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/min-release-age.ts:136:35"
```

### Pattern

`^minimumReleaseAgeExclude:[ \t]*\n(?:[ \t]{2}[^\n]*\n)*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9e511ea6221ea81ec36091dc0fb0967b:search

```yaml
regex_id: 9e511ea6221ea81ec36091dc0fb0967b
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/schema/schemas.ts:37:26"
```

### Pattern

`^[-+]?(?:0|[1-9][\d_]*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9e798843f55a85db1549f65814b7a666:search

```yaml
regex_id: 9e798843f55a85db1549f65814b7a666
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/dev-toolbar/src/vite-plugin.ts:25:21"
```

### Pattern

`\?.+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9ec415c184a5495dcdeffad7292a7edb:search

```yaml
regex_id: 9ec415c184a5495dcdeffad7292a7edb
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/vite-overlay/src/utils/render-safe-markdown.ts:24:20"
```

### Pattern

`^(?:https?:|mailto:|tel:|#|\.{0,2}\/)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9ede8bac6b48cdd8e9e9f60a8ec54c22:search

```yaml
regex_id: 9ede8bac6b48cdd8e9e9f60a8ec54c22
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/config/workspace.ts:34:30"
```

### Pattern

`\/\*\*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9ef12f8114a77248bb3fc76039fc9bea:search

```yaml
regex_id: 9ef12f8114a77248bb3fc76039fc9bea
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/lint-fmt/paths.ts:14:79"
```

### Pattern

`^[a-z]:[\\/]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9f06adacd79cba368c1661f271be14bb:search

```yaml
regex_id: 9f06adacd79cba368c1661f271be14bb
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/command-line-args/src/resolve-args.ts:10:24"
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

## usage_mismatch:a0a9c5fd3b401f0bcf28e4d7c5ec6fa7:search

```yaml
regex_id: a0a9c5fd3b401f0bcf28e4d7c5ec6fa7
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/tui/src/ink/parse-keypress.ts:136:26"
```

### Pattern

`^\u001B\[(\d+);(\d+):(\d+)([A-Z~])$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a12a74424b2008ab183277593db40c5e:search

```yaml
regex_id: a12a74424b2008ab183277593db40c5e
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/util/catalog.ts:23:25"
```

### Pattern

`^(?:'([^']+)'|"([^"]+)"|([^:\s]+)):\s*(?:'([^']+)'|"([^"]+)"|(\S+))`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a132f7dbe43f2a01946c6cbf8daee9a5:search

```yaml
regex_id: a132f7dbe43f2a01946c6cbf8daee9a5
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/config/workspace.ts:35:30"
```

### Pattern

`\/\*\/\*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a2d1b5f962e5db6a312feed6760b7be1:search

```yaml
regex_id: a2d1b5f962e5db6a312feed6760b7be1
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/tui/src/ink/parse-keypress.ts:131:19"
```

### Pattern

`^\u001B\[(\d+)(?:;(\d+)(?::(\d+))?(?:;([\d:]+))?)?u$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a3c387b661469d88e3ff880d6cd73efc:search

```yaml
regex_id: a3c387b661469d88e3ff880d6cd73efc
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/free-email-domains/scripts/free-email-sync-manager.js:16:27"
```

### Pattern

`@([^\s@]+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:a41fb1f0b0036ad3978d6767dd0dba04:email

```yaml
regex_id: a41fb1f0b0036ad3978d6767dd0dba04
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/attachment-helpers.ts:22:20"
```

### Pattern

`[^a-z0-9]`

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

## intent_mismatch:a48ac8539e4f54725bd1f79a1c2e45d5:email

```yaml
regex_id: a48ac8539e4f54725bd1f79a1c2e45d5
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/reply-parser.ts:33:27"
```

### Pattern

`^(?:from|von):\s`

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

## usage_mismatch:a48ac8539e4f54725bd1f79a1c2e45d5:search

```yaml
regex_id: a48ac8539e4f54725bd1f79a1c2e45d5
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/reply-parser.ts:33:27"
```

### Pattern

`^(?:from|von):\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a63b8526fae855c4a55400be51b08f53:search

```yaml
regex_id: a63b8526fae855c4a55400be51b08f53
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/release/doctor/handler.ts:196:52"
```

### Pattern

`^['"]|['"]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a69696dbd8508aebf6a7cf91ee4375b1:search

```yaml
regex_id: a69696dbd8508aebf6a7cf91ee4375b1
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/changelog/default.ts:80:29"
```

### Pattern

`^(?:[\p{Emoji_Presentation}\p{Extended_Pictographic}]|:\w+:)\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a6975b7ab607775c0292a52e3617f558:search

```yaml
regex_id: a6975b7ab607775c0292a52e3617f558
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/tui/failure-render.ts:29:26"
```

### Pattern

`^\s*at\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:a73a28867dabd25b91a127973d588720:email

```yaml
regex_id: a73a28867dabd25b91a127973d588720
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email-verifier/src/checks/smtp.ts:97:25"
```

### Pattern

`^(\d{3})(?: |$)`

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

## usage_mismatch:a73a28867dabd25b91a127973d588720:search

```yaml
regex_id: a73a28867dabd25b91a127973d588720
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email-verifier/src/checks/smtp.ts:97:25"
```

### Pattern

`^(\d{3})(?: |$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a7c40d3c616b376d55da8af0476a578e:search

```yaml
regex_id: a7c40d3c616b376d55da8af0476a578e
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/dev-toolbar/src/apps/seo/seo-app.tsx:462:27"
```

### Pattern

`^<!\[CDATA\[`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a7d8362cf481e16ddd58e96212d1d206:search

```yaml
regex_id: a7d8362cf481e16ddd58e96212d1d206
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/drift.ts:36:8"
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

## usage_mismatch:a86c855b2d89f21894469d3c3a72fdbc:search

```yaml
regex_id: a86c855b2d89f21894469d3c3a72fdbc
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/package/src/lockfile.ts:111:28"
```

### Pattern

`^[a-z][a-zA-Z0-9]*:\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:a8fc4c847c53f582bb0f17c9d53ed111:email

```yaml
regex_id: a8fc4c847c53f582bb0f17c9d53ed111
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/free-email-domains/scripts/free-email-sync-manager.js:15:33"
```

### Pattern

`[,;][^,;]*$`

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

## usage_mismatch:a8fc4c847c53f582bb0f17c9d53ed111:search

```yaml
regex_id: a8fc4c847c53f582bb0f17c9d53ed111
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/free-email-domains/scripts/free-email-sync-manager.js:15:33"
```

### Pattern

`[,;][^,;]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a97ca60feeafd3d4adb3cac3718ac00c:search

```yaml
regex_id: a97ca60feeafd3d4adb3cac3718ac00c
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/filesystem/path/src/path.ts:29:23"
```

### Pattern

`^\/([A-Z]:)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a9ca9a84eb1b5a7a4ec212fa919c92e3:search

```yaml
regex_id: a9ca9a84eb1b5a7a4ec212fa919c92e3
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/humanizer/src/parse-duration.ts:71:30"
```

### Pattern

`^(?:\s*,)?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:aa349cfac6cbf62ad3bcd48ec4f93c06:search

```yaml
regex_id: aa349cfac6cbf62ad3bcd48ec4f93c06
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/migrate/constants.ts:54:4"
```

### Pattern

`^((?:[A-Z_][A-Z0-9_]*(?:=\S*)?\s+)*)nano-staged\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ab4e27d6c27dd50db8ed33aad7572797:search

```yaml
regex_id: ab4e27d6c27dd50db8ed33aad7572797
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/pm/overrides.ts:194:30"
```

### Pattern

`^overrides:\s*\n(?:(?:[ \t].*)?\n)*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ab71dc072fe2c384ed2fcf39e793bad5:search

```yaml
regex_id: ab71dc072fe2c384ed2fcf39e793bad5
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/util/workspace-register.ts:38:27"
```

### Pattern

`^\s*packages\s*:\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ab7fe1ce01bf64a5c9c3eb2c736cdb30:search

```yaml
regex_id: ab7fe1ce01bf64a5c9c3eb2c736cdb30
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/lint-fmt/adapters/ruff.ts:71:72"
```

### Pattern

`^[a-z]:[\\/]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ab8db82fcd98b443b1e94ff6ac053125:search

```yaml
regex_id: ab8db82fcd98b443b1e94ff6ac053125
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/lint-fmt/adapters/ruff.ts:31:31"
```

### Pattern

`^\[tool\.ruff(?:\.[\w-]+)*\]\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:abe9a9944da26d14486244eaedf88e52:search

```yaml
regex_id: abe9a9944da26d14486244eaedf88e52
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/tui/src/ink/mouse/constants.ts:75:34"
```

### Pattern

`\[<(\d+);(\d+);(\d+)(M)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:aca2d304d607fcfd21df35e0386cca1f:email

```yaml
regex_id: aca2d304d607fcfd21df35e0386cca1f
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/utils/parse-eml.ts:17:32"
```

### Pattern

`\s`

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

## usage_mismatch:acd087c5bf6a2ea53de8e7095110e8ec:search

```yaml
regex_id: acd087c5bf6a2ea53de8e7095110e8ec
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/bytes/src/index.ts:52:15"
```

### Pattern

`^[0-9a-f]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:acd92d2eace95f5569ee1f6ce4e64d6c:search

```yaml
regex_id: acd92d2eace95f5569ee1f6ce4e64d6c
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/utils/validation/validate-email.ts:9:23"
```

### Pattern

`^[^\s@]+@[^\s@][^\s.@]*\.[^\s@]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:acdf718b863d2509cb53f01e1af01ea5:search

```yaml
regex_id: acdf718b863d2509cb53f01e1af01ea5
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/schema/schemas.ts:344:23"
```

### Pattern

`^[-+]?(?:0B[01]+|0O[0-7]+|0X[\dA-F]+|\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:acfdd6c34c12a36dea3178c085c834d8:search

```yaml
regex_id: acfdd6c34c12a36dea3178c085c834d8
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/api/jsdoc-open-api/src/jsdoc/comments-to-open-api.ts:10:27"
```

### Pattern

`Param$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ad0dcf4b3fffb60b9a54704f3035033e:search

```yaml
regex_id: ad0dcf4b3fffb60b9a54704f3035033e
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/schema/schemas.ts:41:26"
```

### Pattern

`^[-+]?0x[\dA-Fa-f_]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:ad4231343d7c9d5ba89be327a9bfe5a4:email

```yaml
regex_id: ad4231343d7c9d5ba89be327a9bfe5a4
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/crypto/smime-encrypter.ts:32:20"
```

### Pattern

`-----BEGIN[^-]+-----`

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

## usage_mismatch:af87e055199849a8dae9572caeb7a0b9:search

```yaml
regex_id: af87e055199849a8dae9572caeb7a0b9
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/multi-eco-lockfiles.ts:69:24"
```

### Pattern

`^\s*version\s*=\s*"([^"]+)"\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:af9ccc9e3ba5afd3885ae21815cecc89:search

```yaml
regex_id: af9ccc9e3ba5afd3885ae21815cecc89
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/change-file.ts:149:21"
```

### Pattern

`^\s*(pr|commit|author)\s*:\s*(.+?)\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b070f630fcb8b78a26daf0c14d2c29cc:search

```yaml
regex_id: b070f630fcb8b78a26daf0c14d2c29cc
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email-verifier/src/enrich/name.ts:20:30"
```

### Pattern

`\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b0bab895961dd3d7be70c2c5aeff9ca7:search

```yaml
regex_id: b0bab895961dd3d7be70c2c5aeff9ca7
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/changelog/keep-a-changelog.ts:58:28"
```

### Pattern

`^\s*\[(added|changed|deprecated|removed|fixed|security)\]\s*:?\s*(.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b14e1e9e61fbf99d234090852811a5d1:search

```yaml
regex_id: b14e1e9e61fbf99d234090852811a5d1
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/api/jsdoc-open-api/src/jsdoc/comments-to-open-api.ts:9:31"
```

### Pattern

`^- `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b17d66488a56c22a2d47aec72564254c:search

```yaml
regex_id: b17d66488a56c22a2d47aec72564254c
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/ono/src/error-inspector/components/copy-dropdown.ts:10:28"
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

## usage_mismatch:b19ad7d4a64bff67f859d55b91555a85:search

```yaml
regex_id: b19ad7d4a64bff67f859d55b91555a85
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/release/doctor/handler.ts:1278:71"
```

### Pattern

`^v?\d+\.\d+\.\d+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b2966c2099e0a557547cfc584b58f2b3:search

```yaml
regex_id: b2966c2099e0a557547cfc584b58f2b3
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/attachment-helpers.ts:25:20"
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

## usage_mismatch:b468815b7805c954c2216acb4fd1ed76:search

```yaml
regex_id: b468815b7805c954c2216acb4fd1ed76
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/min-release-age.ts:101:22"
```

### Pattern

`^\s*min-release-age\s*=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b494f622fdb2194fd63f26f1bc9f3593:search

```yaml
regex_id: b494f622fdb2194fd63f26f1bc9f3593
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/package/src/lockfile.ts:652:23"
```

### Pattern

`^ {4}(['"]?[^\s:'"]+['"]?)\s*(?::\s*)?['"]([^'"\n]+)['"]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b4d6830b663603605048a804194d497f:search

```yaml
regex_id: b4d6830b663603605048a804194d497f
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/schema/resolve-scalar.ts:22:19"
```

### Pattern

`^0o[0-7]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:b4ee4f14c1a52e1b8e76d014b512d818:email

```yaml
regex_id: b4ee4f14c1a52e1b8e76d014b512d818
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/reply-parser.ts:34:28"
```

### Pattern

`^(?:to|an|cc|sent|gesendet|date|datum|subject|betreff|reply-to):\s`

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

## usage_mismatch:b4ee4f14c1a52e1b8e76d014b512d818:search

```yaml
regex_id: b4ee4f14c1a52e1b8e76d014b512d818
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/reply-parser.ts:34:28"
```

### Pattern

`^(?:to|an|cc|sent|gesendet|date|datum|subject|betreff|reply-to):\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b502acb717fbb4fe1f816da1d5b86724:search

```yaml
regex_id: b502acb717fbb4fe1f816da1d5b86724
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/is-ansi-color-supported/src/is-color-supported.server.ts:13:33"
```

### Pattern

`^-{1,2}(color=16m|color=full|color=truecolor)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b7b4ccf3f6c93fdafac25938bb63ffce:search

```yaml
regex_id: b7b4ccf3f6c93fdafac25938bb63ffce
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/packem.config.ts:38:16"
```

### Pattern

`^@visulima\/tui(\/|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b7c74b6cef77a80388db2315b74ac453:search

```yaml
regex_id: b7c74b6cef77a80388db2315b74ac453
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/source-map/src/load-source-map.ts:15:34"
```

### Pattern

`^[ \t]*\/\/[@#][ \t]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b7e7326c0fe231afd257b656add486bd:search

```yaml
regex_id: b7e7326c0fe231afd257b656add486bd
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/schema/schemas.ts:53:22"
```

### Pattern

`^\.(?:nan|NaN|NAN)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b86b9c79be1b3f6002ebc844e6039629:search

```yaml
regex_id: b86b9c79be1b3f6002ebc844e6039629
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/package/src/lockfile.ts:109:21"
```

### Pattern

`^['"]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b8978c0c7e16236bbafa9b20115d448f:search

```yaml
regex_id: b8978c0c7e16236bbafa9b20115d448f
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/task-runner/src/parse-input-uri.ts:24:22"
```

### Pattern

`^([a-z][a-z0-9+.-]*):\/\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b8bbbb72892085a4f2e4a7aa628f9d80:search

```yaml
regex_id: b8bbbb72892085a4f2e4a7aa628f9d80
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/migrate/gitleaks.ts:227:28"
```

### Pattern

`^([^:#][^:]*):([^:]+):(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b93f595ef4314c41f1af4c12ba10ab26:search

```yaml
regex_id: b93f595ef4314c41f1af4c12ba10ab26
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/filesystem/path/src/path.ts:32:21"
```

### Pattern

`^[/\\]|^[a-z]:[/\\]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b96e2717dfd281ee9f273092768af62c:search

```yaml
regex_id: b96e2717dfd281ee9f273092768af62c
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/error/src/stacktrace/parse-stacktrace.ts:92:20"
```

### Pattern

`^\s*(.*?)(?:\((.*?)\))?(?:^|@)?((?:[-a-z]+)?:\/.*?|\[native code\]|[^@]*(?:bundle|\d+\.js)|\/[\w\-. \/=]+)(?::(\d+))?(?::(\d+))?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b9b91caba0abfb9d4060003611f83f53:search

```yaml
regex_id: b9b91caba0abfb9d4060003611f83f53
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/is-ansi-color-supported/src/is-color-supported.server.ts:20:20"
```

### Pattern

`-256(color)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ba3e5ed974859a2e74fcd35c6afbbc7d:search

```yaml
regex_id: ba3e5ed974859a2e74fcd35c6afbbc7d
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/deps/catalog-proposals.ts:263:56"
```

### Pattern

`^catalog\s*:\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ba8090b7d507a86a19c5984e14abc31e:search

```yaml
regex_id: ba8090b7d507a86a19c5984e14abc31e
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/exotic-subdeps.ts:63:8"
```

### Pattern

`^(?:git\+|git:\/\/|git@|ssh:\/\/)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bb57a123a7f7fc9ef3943fc6ab150794:search

```yaml
regex_id: bb57a123a7f7fc9ef3943fc6ab150794
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/apply-release-plan.ts:63:18"
```

### Pattern

`^([\^~=]|>=?|<=?)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bb8016b444eefbb5c953be7d2eb6e845:search

```yaml
regex_id: bb8016b444eefbb5c953be7d2eb6e845
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/min-release-age.ts:170:22"
```

### Pattern

`^npmMinimalAgeGate[ \t]*:.*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bb958d2c6fa765c0e8d1b00fd93170a0:search

```yaml
regex_id: bb958d2c6fa765c0e8d1b00fd93170a0
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/reachability.ts:30:66"
```

### Pattern

`^[a-z][a-z0-9+.-]*:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bc62e2685be3a607cb47e1d420cc5d40:search

```yaml
regex_id: bc62e2685be3a607cb47e1d420cc5d40
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/util/catalog.ts:33:29"
```

### Pattern

`\/$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bd02fbf70fcce1183f9008c0f034f870:search

```yaml
regex_id: bd02fbf70fcce1183f9008c0f034f870
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/vite-overlay/src/utils/error-processing/remap-stack-to-original.ts:9:24"
```

### Pattern

`^(Error:.*?)at `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bdf438aedb6a6d59e0033cb5012e7772:search

```yaml
regex_id: bdf438aedb6a6d59e0033cb5012e7772
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/generate/conventional-commits.ts:103:29"
```

### Pattern

`^(?:[\p{Emoji_Presentation}\p{Extended_Pictographic}]|:\w+:)\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bdf77c85c9e9a5de7139ba7ed555cb48:search

```yaml
regex_id: bdf77c85c9e9a5de7139ba7ed555cb48
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/providers/resend/provider.ts:36:25"
```

### Pattern

`^[\w-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:be6e3389800962527427ad8efecc0324:search

```yaml
regex_id: be6e3389800962527427ad8efecc0324
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/schema/resolve-scalar.ts:18:19"
```

### Pattern

`^[-+]?\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:be7b8b9d61a202c4239182d59bb6c2d0:search

```yaml
regex_id: be7b8b9d61a202c4239182d59bb6c2d0
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/runtime/ts-loader.ts:38:20"
```

### Pattern

`\.(?:ya?ml|toml|jsonc|json5|txt)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bec7f12e79079cdc1e10648d8b6b2da0:search

```yaml
regex_id: bec7f12e79079cdc1e10648d8b6b2da0
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/humanizer/src/parse-duration.ts:117:26"
```

### Pattern

`^[-+]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bf27c264e99b5d09deb6a837a16f722c:search

```yaml
regex_id: bf27c264e99b5d09deb6a837a16f722c
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/vite-overlay/src/utils/error-processing/index.ts:25:23"
```

### Pattern

`^https?:\/\/[^/]+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bf4e742d0b90fc8d8e67e710f9192025:search

```yaml
regex_id: bf4e742d0b90fc8d8e67e710f9192025
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/update/handler.ts:130:8"
```

### Pattern

`^\d+(?:\.\d+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bf841b5992d39c71db8cf93b6d029890:search

```yaml
regex_id: bf841b5992d39c71db8cf93b6d029890
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/iso-locale/src/currencies.ts:7:22"
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

## usage_mismatch:c004a98d56f336e4138a6467ab63764a:search

```yaml
regex_id: c004a98d56f336e4138a6467ab63764a
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/find-ai-runner/src/process-tree.ts:31:29"
```

### Pattern

`"$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c05876e44bf26a0bd6df91ed87b92ad0:search

```yaml
regex_id: c05876e44bf26a0bd6df91ed87b92ad0
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/filesystem/path/src/path.ts:30:22"
```

### Pattern

`^([A-Z]:)\/$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c0806272a122cf27122d97fe7c7a05c4:search

```yaml
regex_id: c0806272a122cf27122d97fe7c7a05c4
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/filesystem/path/src/path.ts:26:18"
```

### Pattern

`^[/\\]{2}`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c10e1dc269fa5eaabf23de2cf10212f0:search

```yaml
regex_id: c10e1dc269fa5eaabf23de2cf10212f0
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/update/ecosystems/gitlab/scanner.ts:83:21"
```

### Pattern

`^\s*(?:-\s*)?(?:include:\s*)?\{([^}]*)\}\s*(?:#.*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c123fa8a4c45aaad11390fcee9dbe863:search

```yaml
regex_id: c123fa8a4c45aaad11390fcee9dbe863
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/error/src/stacktrace/parse-stacktrace.ts:108:34"
```

### Pattern

`^(\S+):(\d+):(\d+)$|^(\S+):(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c189ade2fd41873187507961015d8b86:search

```yaml
regex_id: c189ade2fd41873187507961015d8b86
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/tui/components/devcontainer/vis-devcontainer-app.tsx:263:25"
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

## usage_mismatch:c204dc76fefdf0afe3d76b806198542a:search

```yaml
regex_id: c204dc76fefdf0afe3d76b806198542a
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/scripts/update-cyclonedx-schemas.ts:41:20"
```

### Pattern

`^(\d+)\.(\d+)(?:\.\d+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c21cab8a8c709b479113eb9b53fceeb9:search

```yaml
regex_id: c21cab8a8c709b479113eb9b53fceeb9
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/providers/smtp/provider.ts:28:26"
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

## usage_mismatch:c2dea4a8528a686ae0789d6b96030e11:search

```yaml
regex_id: c2dea4a8528a686ae0789d6b96030e11
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/package/src/lockfile.ts:531:23"
```

### Pattern

`^ {6}([^\s:]+):\s*([^\n]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c352672cb273cf8d28c41907d7a93622:search

```yaml
regex_id: c352672cb273cf8d28c41907d7a93622
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/vite-overlay/src/utils/enhance-vite-ssr-error.ts:8:25"
```

### Pattern

`\.mdx$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c364299bba28813963e2aad548a51881:search

```yaml
regex_id: c364299bba28813963e2aad548a51881
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/pretrust.ts:239:45"
```

### Pattern

`\.ya?ml$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c37e37e6c529280a116a42db776a8b97:search

```yaml
regex_id: c37e37e6c529280a116a42db776a8b97
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/find-ai-runner/src/process-tree.ts:28:28"
```

### Pattern

`^"`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c3bda513ff85bc1b991b4c823794bb22:search

```yaml
regex_id: c3bda513ff85bc1b991b4c823794bb22
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/colorize/src/template/make-template.ts:19:21"
```

### Pattern

`^(['"])((?:\\.|(?!\1)[^\\])*)\1$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c487f54fa96354247fced76b39038114:search

```yaml
regex_id: c487f54fa96354247fced76b39038114
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/bytes/src/index.ts:63:18"
```

### Pattern

`^[a-z0-9+/]*={0,2}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c5086b6a767d3bfe480ff83097a06f20:search

```yaml
regex_id: c5086b6a767d3bfe480ff83097a06f20
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/secret-scanner/src/transformers/yaml.ts:35:28"
```

### Pattern

`^(?<indent>[\t ]*)(?<key>[^\s#:]+)[\t ]*:[\t ]*[|>][+-]?\d*[\t ]*(?:#.*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c716d1394fc295cd567aaa48ac311145:search

```yaml
regex_id: c716d1394fc295cd567aaa48ac311145
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/schema/schemas.ts:59:22"
```

### Pattern

`^[-+]?0`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c79641f1bf9d8e4334e7e9e87959b289:search

```yaml
regex_id: c79641f1bf9d8e4334e7e9e87959b289
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/update/ecosystems/gitlab/scanner.ts:64:19"
```

### Pattern

`^\s*-?\s*project:\s*(['"]?)([^'"\s#]+)\1(?:\s*#.*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c910bb83f9e2e3e44f9c08ab96598eb0:search

```yaml
regex_id: c910bb83f9e2e3e44f9c08ab96598eb0
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/util/utils.ts:67:27"
```

### Pattern

`^(.+?)(?:@(.+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c919946de59847e4dee6a2ce061fc8b5:search

```yaml
regex_id: c919946de59847e4dee6a2ce061fc8b5
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/filesystem/fs/src/sanitize.ts:24:36"
```

### Pattern

`^(?:con|prn|aux|nul|com\d|lpt\d)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:c9d3265b9b9bcbd38b12187652147c16:email

```yaml
regex_id: c9d3265b9b9bcbd38b12187652147c16
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/providers/azure/provider.ts:87:65"
```

### Pattern

`endpoint=([^;]+);accesskey=([^;]+)`

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

## usage_mismatch:ca21b4a1588f2f2fd2f9e9e7b449fc96:search

```yaml
regex_id: ca21b4a1588f2f2fd2f9e9e7b449fc96
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/native-config-sync.ts:40:16"
```

### Pattern

`^\s*ignore-scripts\s*=\s*true\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ca2390d6c6009a5645e3903d00d82dc1:search

```yaml
regex_id: ca2390d6c6009a5645e3903d00d82dc1
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/vite-overlay/src/utils/stack-trace.ts:19:24"
```

### Pattern

`:(\d+)(?::(\d+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ca839473535f4ec8e786f253b35f65b1:search

```yaml
regex_id: ca839473535f4ec8e786f253b35f65b1
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/humanizer/src/bytes.ts:8:26"
```

### Pattern

`^(?<value>-?\d+(?:[\p{Zs}'’.,]\d+)*)\p{Zs}*(?<type>[a-z]+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:caa93b6d470bd3899e4d6888a6631747:email

```yaml
regex_id: caa93b6d470bd3899e4d6888a6631747
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/utils.ts:4:27"
```

### Pattern

`<[^<>]+>`

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

## usage_mismatch:cb00841c519bfdf5b38eba08eed14f09:search

```yaml
regex_id: cb00841c519bfdf5b38eba08eed14f09
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/package/src/lockfile.ts:110:21"
```

### Pattern

`['"]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cb351adf885103212b675ea72bc1b860:search

```yaml
regex_id: cb351adf885103212b675ea72bc1b860
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email-verifier/src/enrich/name.ts:18:25"
```

### Pattern

`^[a-z]+(?:[A-Z][a-z]+)+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cd5f9ad263d7baf3a02c16ccd99f5a4b:search

```yaml
regex_id: cd5f9ad263d7baf3a02c16ccd99f5a4b
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/deps/dead-workspace-pattern.ts:122:62"
```

### Pattern

`^['"]|['"]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cd8fea2446c1286bbf4a4317886b6415:search

```yaml
regex_id: cd8fea2446c1286bbf4a4317886b6415
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/release/add/handler.ts:105:28"
```

### Pattern

`^(?:[a-z]+(?:\([^)]+\))?:\s+)?[Bb]ump\s+(?<dep>\S+)\s+from\s+(?<fromVersion>\S+)\s+to\s+(?<toVersion>\S+)(?:\s+in\s+\S+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cd9094a432f734d062ac25be6a7a59da:search

```yaml
regex_id: cd9094a432f734d062ac25be6a7a59da
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/dlx/changelog.ts:142:46"
```

### Pattern

`^\[.*\]:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cda7238594f6595a4e12ebe54baa8764:search

```yaml
regex_id: cda7238594f6595a4e12ebe54baa8764
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/tui/src/ink/colorize.ts:7:17"
```

### Pattern

`^rgb\(\s?(\d+),\s?(\d+),\s?(\d+)\s?\)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cdb03ff445529dfc4ba283b1ddfb1a49:search

```yaml
regex_id: cdb03ff445529dfc4ba283b1ddfb1a49
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/inspector/src/utils/add-numeric-separator.ts:4:32"
```

### Pattern

`_$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cdec02bb69158abca2469c107d5c094b:search

```yaml
regex_id: cdec02bb69158abca2469c107d5c094b
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/task/selectors.ts:184:24"
```

### Pattern

`^(\w+)\s*(!?=)\s*(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ceaddbcbe722b9658d17eaf359cd86fb:search

```yaml
regex_id: ceaddbcbe722b9658d17eaf359cd86fb
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/native-config-sync.ts:147:31"
```

### Pattern

`^\s*enableScripts\s*:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cef0d83685ada10d29253b7b996dd7e8:search

```yaml
regex_id: cef0d83685ada10d29253b7b996dd7e8
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/secret-scanner/src/checksum.ts:20:29"
```

### Pattern

`^\s*\(\?([a-z]+)\)\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cf0306ee59e6a7e96cfebb234becac24:search

```yaml
regex_id: cf0306ee59e6a7e96cfebb234becac24
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/migrate/constants.ts:29:4"
```

### Pattern

`^((?:[A-Z_][A-Z0-9_]*(?:=\S*)?\s+)*)lint-staged\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cf4e5fc85b255206326781bbe3d5b3ef:search

```yaml
regex_id: cf4e5fc85b255206326781bbe3d5b3ef
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/iso-locale/src/locale.ts:10:22"
```

### Pattern

`^(?:[\da-z]{5,8}|\d[\da-z]{3})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cfae1a2bdb55651c8d6d5f36edd5a98c:search

```yaml
regex_id: cfae1a2bdb55651c8d6d5f36edd5a98c
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/task-runner/src/flow-controllers/input-handler.ts:41:27"
```

### Pattern

`^(\S+?):(.+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d039fb29b9383b4f7419438418aa5df2:search

```yaml
regex_id: d039fb29b9383b4f7419438418aa5df2
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/sort-package-json/handler.ts:118:8"
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

## usage_mismatch:d0575189aee93a420633e9af98870433:search

```yaml
regex_id: d0575189aee93a420633e9af98870433
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/tui-kit/src/path-input.tsx:14:23"
```

### Pattern

`\/$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d05f5b11174a0b97a523c7697024bdb2:search

```yaml
regex_id: d05f5b11174a0b97a523c7697024bdb2
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/min-release-age.ts:171:34"
```

### Pattern

`^npmMinimalAgeGate[ \t]*:.*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d07d9df9f329d94311916c1a172a0758:search

```yaml
regex_id: d07d9df9f329d94311916c1a172a0758
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/shared/utils/get-file-source.ts:105:8"
```

### Pattern

`^(?:https?|data):`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d0ec590214c342301c0aa496b771df48:search

```yaml
regex_id: d0ec590214c342301c0aa496b771df48
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/prompts.ts:33:15"
```

### Pattern

`^y(?:es)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d10aea95d2586a44c342a69485dfffcc:search

```yaml
regex_id: d10aea95d2586a44c342a69485dfffcc
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/tui/src/ink/color-utils.ts:36:21"
```

### Pattern

`^ansi256\(\s?(\d+)\s?\)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d1d4b648d675f57cbdabefb777ef228d:search

```yaml
regex_id: d1d4b648d675f57cbdabefb777ef228d
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/string/src/slice.ts:11:22"
```

### Pattern

`^[\u0000-\u007F]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d1ea4740f7f99d3971c1b213cb33a49e:search

```yaml
regex_id: d1ea4740f7f99d3971c1b213cb33a49e
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/update/ecosystems/docker/scanner.ts:300:11"
```

### Pattern

`^(?:docker-)?compose(?:\..+)?\.ya?ml$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d1f124ae6ea2a7e04237aa9c896e2583:search

```yaml
regex_id: d1f124ae6ea2a7e04237aa9c896e2583
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/enforcement.ts:55:68"
```

### Pattern

`^\s*ignore-scripts\s*=\s*true\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d33fbe8ef10502bb0fc5826ccdc477a6:search

```yaml
regex_id: d33fbe8ef10502bb0fc5826ccdc477a6
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/error-handler/src/error-handler/utils/render-html-error-inspector.ts:43:31"
```

### Pattern

`^\s*#+\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d402a6c05f23d5bcf858c5e4218e2f68:search

```yaml
regex_id: d402a6c05f23d5bcf858c5e4218e2f68
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/apps/web/src/pages/home/sections/hero.tsx:125:33"
```

### Pattern

`^["'`]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d4918373cd032243d862b4fe77055e4e:search

```yaml
regex_id: d4918373cd032243d862b4fe77055e4e
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/migrate/nx.ts:1076:25"
```

### Pattern

`^nx\s+(?:run-many|run|affected|reset|repair)\b|^nx\s+exec\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d4ae655de937dcd86370c8891a8a4bda:search

```yaml
regex_id: d4ae655de937dcd86370c8891a8a4bda
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/dev-toolbar/src/apps/tailwind/tailwind-app.tsx:16:35"
```

### Pattern

`-(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d4c82f82769de35e7124b5648a9e81ee:search

```yaml
regex_id: d4c82f82769de35e7124b5648a9e81ee
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/generate/conventional-commits.ts:93:25"
```

### Pattern

`^Revert\s+"(.+)"\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d4c84202a9589e8606a1e3b48c17c6a6:search

```yaml
regex_id: d4c84202a9589e8606a1e3b48c17c6a6
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/change-file.ts:53:23"
```

### Pattern

`^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d61d9760eb66e06fee3a64300b9364be:search

```yaml
regex_id: d61d9760eb66e06fee3a64300b9364be
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/source-map/src/load-source-map.ts:13:25"
```

### Pattern

`^[a-z][a-z0-9+.-]*:\/\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d6260976006cf60532c941e4b85dafb3:search

```yaml
regex_id: d6260976006cf60532c941e4b85dafb3
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/vite-overlay/src/utils/resolve-original-location.ts:11:25"
```

### Pattern

`^\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d6b3369af99bb150983aaa171bdec66f:search

```yaml
regex_id: d6b3369af99bb150983aaa171bdec66f
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/release/add/handler.ts:96:11"
```

### Pattern

`^[\d.+\-a-z]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:d7b57ffeb2257ecb844d95ac162677c6:email

```yaml
regex_id: d7b57ffeb2257ecb844d95ac162677c6
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email-verifier/src/internal/address.ts:13:25"
```

### Pattern

`\s`

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

## usage_mismatch:d7e6e4bab80af76cfc8d1dcb19e1178d:search

```yaml
regex_id: d7e6e4bab80af76cfc8d1dcb19e1178d
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/apps/web/src/pages/home/sections/hero.tsx:128:34"
```

### Pattern

`^(true|false|null|undefined)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d852f6c54b04fcc3fa533537027adae6:search

```yaml
regex_id: d852f6c54b04fcc3fa533537027adae6
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/ono/src/server/open-in-editor.ts:10:31"
```

### Pattern

`^[\w.+-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d89d378195ba340b4fb2d986c409b6bb:search

```yaml
regex_id: d89d378195ba340b4fb2d986c409b6bb
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/staged/git/diff.ts:43:54"
```

### Pattern

`^0+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d9bc1d7a6078654cd3be04a129ddac35:search

```yaml
regex_id: d9bc1d7a6078654cd3be04a129ddac35
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/vite-overlay/src/utils/normalize-id-candidates.ts:1:23"
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

## intent_mismatch:daf6296fef53e85f9e604a5cf6614937:email

```yaml
regex_id: daf6296fef53e85f9e604a5cf6614937
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/providers/smtp/dkim.ts:50:53"
```

### Pattern

`\s+`

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

## usage_mismatch:db2f7fb5d35633f2a9fab26d4a746dfa:search

```yaml
regex_id: db2f7fb5d35633f2a9fab26d4a746dfa
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email-verifier/src/checks/syntax.ts:8:26"
```

### Pattern

`^[^\s@]+@[^\s@][^\s.@]*\.[^\s@]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:db54766b13a43617923861db840045ed:search

```yaml
regex_id: db54766b13a43617923861db840045ed
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/vite-overlay/src/utils/error-processing/index.ts:26:25"
```

### Pattern

`^\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dbe8e058b81d4f3cbe09a4015248bad4:search

```yaml
regex_id: dbe8e058b81d4f3cbe09a4015248bad4
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/min-release-age.ts:75:27"
```

### Pattern

`^[ \t]*minimumReleaseAgeExcludes[ \t]*=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dc229c5ca35028f6c48dc12e22fff31c:search

```yaml
regex_id: dc229c5ca35028f6c48dc12e22fff31c
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/api/jsdoc-open-api/src/jsdoc/comments-to-open-api.ts:12:23"
```

### Pattern

`^(GET|PUT|POST|DELETE|OPTIONS|HEAD|PATCH|TRACE) \/.*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dd418e64152dfabec8ae21917080e256:search

```yaml
regex_id: dd418e64152dfabec8ae21917080e256
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/cerebro/src/util/command-processing/option-processor.ts:7:24"
```

### Pattern

`^no-`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:de0f86e5945473c755015b7b2a272bf0:search

```yaml
regex_id: de0f86e5945473c755015b7b2a272bf0
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/runtime/toolchain.ts:501:21"
```

### Pattern

`^([a-z][\w-]*)\s*=\s*"?([^"\n#]+?)"?\s*(?:#.*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dee2c11b1d5f26858929ea49d638d6f5:search

```yaml
regex_id: dee2c11b1d5f26858929ea49d638d6f5
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/config/workspace.ts:33:26"
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

## usage_mismatch:df2bc33ecec6c61345304e3a36f3fba8:search

```yaml
regex_id: df2bc33ecec6c61345304e3a36f3fba8
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/cerebro/src/util/command-line-commands.ts:10:26"
```

### Pattern

`^--(\S+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:df2e77a167c97c54bc53ba9073f34ae4:search

```yaml
regex_id: df2e77a167c97c54bc53ba9073f34ae4
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/tui/src/ink/colorize.ts:8:18"
```

### Pattern

`^ansi256\(\s?(\d+)\s?\)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:df7c39691dfdc043b4ef41a64eade10a:search

```yaml
regex_id: df7c39691dfdc043b4ef41a64eade10a
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/inspector/src/utils/inspect-property.ts:3:23"
```

### Pattern

`^[a-z_]\w*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:df7d8f1f1ced8b87e8e3ef268401feb2:search

```yaml
regex_id: df7d8f1f1ced8b87e8e3ef268401feb2
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/tui-kit/src/text-input.tsx:59:26"
```

### Pattern

`\S+\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:dfd7ff305d166be903388d29a500b22a:email

```yaml
regex_id: dfd7ff305d166be903388d29a500b22a
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/providers/smtp/dkim.ts:24:63"
```

### Pattern

` +$`

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

## usage_mismatch:dfececd845c36d7444ca2b6aa4a603c8:search

```yaml
regex_id: dfececd845c36d7444ca2b6aa4a603c8
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/util/catalog.ts:20:21"
```

### Pattern

`^([\^~]|>=|<=|[><=])`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e025730016f36dde42d6887d3256e856:search

```yaml
regex_id: e025730016f36dde42d6887d3256e856
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/change-file.ts:95:19"
```

### Pattern

`^ {0,3}(#{1,3})\s+\S`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:e0495c3190b275ba14f3ff2e8f0abfc0:email

```yaml
regex_id: e0495c3190b275ba14f3ff2e8f0abfc0
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/free-email-domains/scripts/free-email-sync-manager.js:14:31"
```

### Pattern

`\s\S*$`

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

## usage_mismatch:e0495c3190b275ba14f3ff2e8f0abfc0:search

```yaml
regex_id: e0495c3190b275ba14f3ff2e8f0abfc0
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/free-email-domains/scripts/free-email-sync-manager.js:14:31"
```

### Pattern

`\s\S*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:e09e45afec0b47f8f556d15f3beda84c:email

```yaml
regex_id: e09e45afec0b47f8f556d15f3beda84c
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/reply-parser.ts:14:4"
```

### Pattern

`^El .*escribió:$`

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

## usage_mismatch:e09e45afec0b47f8f556d15f3beda84c:search

```yaml
regex_id: e09e45afec0b47f8f556d15f3beda84c
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/reply-parser.ts:14:4"
```

### Pattern

`^El .*escribió:$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e25058a8dd0673d8e98925600474973c:search

```yaml
regex_id: e25058a8dd0673d8e98925600474973c
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/release/add/handler.ts:131:26"
```

### Pattern

`^(?:[a-z]+(?:\([^)]+\))?:\s+)?[Uu]pdate\s+(?:dependency|module)\s+(?<dep>\S+)\s+to\s+(?<toVersion>\S+)(?:\s+\S.*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e26a3b66e7201a29a7aa046bd9624336:search

```yaml
regex_id: e26a3b66e7201a29a7aa046bd9624336
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/task-runner/src/file-access-tracker.ts:914:33"
```

### Pattern

`^(?:[a-z]:)?[/\\]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e390a85184bdf3a15433297ea7a6bcd4:search

```yaml
regex_id: e390a85184bdf3a15433297ea7a6bcd4
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/min-release-age.ts:76:39"
```

### Pattern

`^[ \t]*minimumReleaseAgeExcludes[ \t]*=.*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e3d40834bc5d39b864814d03db72a3bf:search

```yaml
regex_id: e3d40834bc5d39b864814d03db72a3bf
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/dev-toolbar/src/apps/vite-config/vite-config-app.tsx:170:24"
```

### Pattern

`^\/|^[A-Z]:\\`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e4189f43a7b9104df7dc1fa55725f64a:search

```yaml
regex_id: e4189f43a7b9104df7dc1fa55725f64a
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/filesystem/path/src/normalize-windows-path.ts:7:30"
```

### Pattern

`^[A-Z]:\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e473ab91c007ef2caad3bc0b20f0f0f1:search

```yaml
regex_id: e473ab91c007ef2caad3bc0b20f0f0f1
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/storage/storage/src/handler/multipart/multipart-fetch.ts:15:16"
```

### Pattern

`^multipart\/.+|application\/x-www-form-urlencoded$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e4b6e0b4a39aa02443081822857f2e66:search

```yaml
regex_id: e4b6e0b4a39aa02443081822857f2e66
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/filesystem/fs/src/ensure/ensure-symlink.ts:15:50"
```

### Pattern

`^(?:msys|cygwin)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e51173bf4e0fb3348b5d81a55d9a9e28:search

```yaml
regex_id: e51173bf4e0fb3348b5d81a55d9a9e28
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/task/arguments.ts:79:75"
```

### Pattern

`^-(?:\d|\.\d)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e5fb1c1cc424c007ed801b13a5573444:search

```yaml
regex_id: e5fb1c1cc424c007ed801b13a5573444
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/storage/storage/src/storage/supabase/supabase-storage.ts:26:25"
```

### Pattern

`^attachment(\s*;|\s*$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e6af6bbd6f3a9e6fafddb423ab920d14:search

```yaml
regex_id: e6af6bbd6f3a9e6fafddb423ab920d14
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/filesystem/fs/src/utils/ini-preserve.ts:7:31"
```

### Pattern

`^\s*(?:[;#].*)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e6ccea48a629deb0608ded3358ba3664:search

```yaml
regex_id: e6ccea48a629deb0608ded3358ba3664
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/dev-toolbar/src/apps/seo/seo-app.tsx:461:24"
```

### Pattern

`\/\/\]\]>$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e7e16bb0f05d34fc152f9173563acf12:search

```yaml
regex_id: e7e16bb0f05d34fc152f9173563acf12
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/apps/web/src/pages/home/sections/hero.tsx:116:20"
```

### Pattern

`^\s+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e82359756dc40b904abb1ecb760d3f6e:search

```yaml
regex_id: e82359756dc40b904abb1ecb760d3f6e
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/source-map/src/load-source-map.ts:12:31"
```

### Pattern

`^data:application\/json[^,]+base64,`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e837d529c0e36ba174182d86451c2b3a:search

```yaml
regex_id: e837d529c0e36ba174182d86451c2b3a
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/pm/overrides.ts:193:46"
```

### Pattern

`^overrides:\s*\n`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e87eec8bffaa50a3ad110826dd55c6ec:search

```yaml
regex_id: e87eec8bffaa50a3ad110826dd55c6ec
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/release/doctor/handler.ts:1308:20"
```

### Pattern

`^#{1,2}\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e992fae45a0498ae4d8ab18d4a0f08fc:search

```yaml
regex_id: e992fae45a0498ae4d8ab18d4a0f08fc
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/secret-scanner/src/heuristics.ts:97:31"
```

### Pattern

`^(.)\1+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e996c48862f303f84d46b42e6b358fe4:search

```yaml
regex_id: e996c48862f303f84d46b42e6b358fe4
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/tsconfig/src/version-defaults/index.ts:29:22"
```

### Pattern

`^v?(\d+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e9dcd104e338fbb68e2ac95d584fb697:search

```yaml
regex_id: e9dcd104e338fbb68e2ac95d584fb697
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/package/src/lockfile.ts:116:6"
```

### Pattern

`^["']?((?:@[^/@"']+\/)?[^@"'\n]+)@[^\n]+\n((?:[\t ][^\n]*(?:\n|$))+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:e9dea23cf5e19f54c726813f838d1a7b:email

```yaml
regex_id: e9dea23cf5e19f54c726813f838d1a7b
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/utils/parse-address.ts:71:41"
```

### Pattern

`^"((?:[^"\\]|\\.)+)"@(.+)$`

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

## usage_mismatch:e9dea23cf5e19f54c726813f838d1a7b:search

```yaml
regex_id: e9dea23cf5e19f54c726813f838d1a7b
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/utils/parse-address.ts:71:41"
```

### Pattern

`^"((?:[^"\\]|\\.)+)"@(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ea1be89b284123c99a5d0de7a0d4a7ec:search

```yaml
regex_id: ea1be89b284123c99a5d0de7a0d4a7ec
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email-verifier/src/checks/syntax.ts:15:27"
```

### Pattern

`^[\p{L}\p{N}-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ea1c4092c6bbb1e64bd59b17a7cdfeb3:search

```yaml
regex_id: ea1c4092c6bbb1e64bd59b17a7cdfeb3
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/hook/builtins/trailing-whitespace.ts:9:20"
```

### Pattern

`\.(?:md|markdown|mdown|mdx)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ea55bc3efa5248ebadcde737653c0f36:search

```yaml
regex_id: ea55bc3efa5248ebadcde737653c0f36
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/colorize/src/gradient/gradient-builder.ts:10:23"
```

### Pattern

`^[a-f\d]{3}$|^[a-f\d]{6}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ea5b78f0b5b66fef0c6c742abe87183b:search

```yaml
regex_id: ea5b78f0b5b66fef0c6c742abe87183b
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/package/src/package-json.ts:22:29"
```

### Pattern

`, ([^,]*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:eaea587f0ea8e79b2a223005d8c80b85:search

```yaml
regex_id: eaea587f0ea8e79b2a223005d8c80b85
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/commands/release/add/handler.ts:89:9"
```

### Pattern

`^[\dv]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:eba8ee0d52fb6eb58b2a3143e465e0db:search

```yaml
regex_id: eba8ee0d52fb6eb58b2a3143e465e0db
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/task-runner/src/command-parser/strip-quotes.ts:10:35"
```

### Pattern

`^'.+?'$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ec9545657d183e3043a6bd1fa9a93fde:search

```yaml
regex_id: ec9545657d183e3043a6bd1fa9a93fde
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/task-runner/src/lockfile-hasher.ts:182:10"
```

### Pattern

`^["']?(?:@([^/@"']+)\/)?([^@"']+)@[^"'\n]+["']?:?[\t\v\f\r \u00A0\u1680\u2000-\u200A\u2028\u2029\u202F\u205F\u3000\uFEFF]*\n\s+version:?\s+"?([^"\n]+)"?`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ed2dc761cf2145ea42feb013afb27a6c:search

```yaml
regex_id: ed2dc761cf2145ea42feb013afb27a6c
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/tui/src/ink/color-matrix.ts:107:17"
```

### Pattern

`^#?(?<r>[\da-f]{2})(?<g>[\da-f]{2})(?<b>[\da-f]{2})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ed73e7437743d840fdb4baff40bcf0f8:search

```yaml
regex_id: ed73e7437743d840fdb4baff40bcf0f8
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/secret-scanner/src/transports/jdbc.ts:7:25"
```

### Pattern

`^jdbc:([a-zA-Z][a-zA-Z0-9+.-]*):(\/\/.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:edb4f12cb54bc16269d8658633977b34:search

```yaml
regex_id: edb4f12cb54bc16269d8658633977b34
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/util/workspace-register.ts:39:21"
```

### Pattern

`^(\s*)-\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ee11737d132283c1de46298d542ec77d:search

```yaml
regex_id: ee11737d132283c1de46298d542ec77d
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/deps/root-package-manager.ts:33:30"
```

### Pattern

`^[a-z][\w-]*@\S+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ee2619d80743bed2a95b69ed96bab214:search

```yaml
regex_id: ee2619d80743bed2a95b69ed96bab214
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/tui/src/ink/input-utils.ts:5:24"
```

### Pattern

`^[a-z]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ee82c44059ec3766a272618b2d448af2:search

```yaml
regex_id: ee82c44059ec3766a272618b2d448af2
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/storage/storage/src/storage/utils/file/metadata.ts:3:29"
```

### Pattern

`^[\d+/A-Z]*={0,2}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:eec4dbe4712ec186a0b82ceeea8a5c15:email

```yaml
regex_id: eec4dbe4712ec186a0b82ceeea8a5c15
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/render/preheader.ts:2:18"
```

### Pattern

`<body[^<>]*>`

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

## intent_mismatch:eff4676dc87077e756e9316556d84a6a:email

```yaml
regex_id: eff4676dc87077e756e9316556d84a6a
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/reply-parser.ts:29:28"
```

### Pattern

`^--\s?$`

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

## usage_mismatch:eff4676dc87077e756e9316556d84a6a:search

```yaml
regex_id: eff4676dc87077e756e9316556d84a6a
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/reply-parser.ts:29:28"
```

### Pattern

`^--\s?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f02fd7122bc36ef0eb33c29b591d9303:search

```yaml
regex_id: f02fd7122bc36ef0eb33c29b591d9303
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/filesystem/path/src/path.ts:27:23"
```

### Pattern

`^[/\\](?![/\\])|^[/\\]{2}(?!\.)|^[A-Z]:[/\\]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f04b07bbdc4b32d28aaae91c6fe3f728:search

```yaml
regex_id: f04b07bbdc4b32d28aaae91c6fe3f728
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/error/src/stacktrace/parse-stacktrace.ts:40:33"
```

### Pattern

`^(?:node:internal\/|node:|internal\/)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f079f42f7581f60d6a530a8943d7fdc5:search

```yaml
regex_id: f079f42f7581f60d6a530a8943d7fdc5
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/reachability.ts:55:75"
```

### Pattern

`(^|[^:])\/\/.*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f080bed2edc7ef00a3e786676a2a2ad4:search

```yaml
regex_id: f080bed2edc7ef00a3e786676a2a2ad4
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/lint-fmt/adapters/markdownlint.ts:54:72"
```

### Pattern

`^[a-z]:[\\/]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f18b69a30adb4122376d467fe76796dd:search

```yaml
regex_id: f18b69a30adb4122376d467fe76796dd
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/disposable-email-domains/src/index.ts:31:27"
```

### Pattern

`\.$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f1a728d7a50088d8b88af46c2fda9884:search

```yaml
regex_id: f1a728d7a50088d8b88af46c2fda9884
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/release/core/security.ts:25:27"
```

### Pattern

`^(?:@[a-z0-9-]{1,39}\/)?[a-z0-9._-]{1,214}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f1d1264933953307da3565c87d8837c5:search

```yaml
regex_id: f1d1264933953307da3565c87d8837c5
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/dev-toolbar/src/apps/tailwind/tailwind-app.tsx:14:25"
```

### Pattern

`^\w+-\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:f22b0f15c8cf36820fae0113f6ea69af:email

```yaml
regex_id: f22b0f15c8cf36820fae0113f6ea69af
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/disposable-email-domains/scripts/disposable-email-sync-manager.js:12:24"
```

### Pattern

`^(?:0\.0\.0\.0\s+|127\.0\.0\.1\s+|localhost\s+)`

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

## usage_mismatch:f22b0f15c8cf36820fae0113f6ea69af:search

```yaml
regex_id: f22b0f15c8cf36820fae0113f6ea69af
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/disposable-email-domains/scripts/disposable-email-sync-manager.js:12:24"
```

### Pattern

`^(?:0\.0\.0\.0\s+|127\.0\.0\.1\s+|localhost\s+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f2b6a0272ba1d2c57010ac8c40dcae8a:search

```yaml
regex_id: f2b6a0272ba1d2c57010ac8c40dcae8a
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/parser/dumper.ts:77:20"
```

### Pattern

`^\S+(?: \S+)*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f39f079464848f24940b9d134f82ad36:search

```yaml
regex_id: f39f079464848f24940b9d134f82ad36
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/task-runner/src/command-parser/shell-quote.ts:18:29"
```

### Pattern

`^[\w./:@+,=-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f4b23c260cb8c6b7264f8b44997dcd0b:search

```yaml
regex_id: f4b23c260cb8c6b7264f8b44997dcd0b
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/cerebro/src/util/general/validate-input.ts:8:21"
```

### Pattern

`^[a-z][\w-]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f577c5dffed508e7fdbf27fb2c748bc5:search

```yaml
regex_id: f577c5dffed508e7fdbf27fb2c748bc5
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/iso-locale/src/locale.ts:12:31"
```

### Pattern

`^[\da-z]{1,8}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f704bcc73bbbf6d12e2cca672b492b04:search

```yaml
regex_id: f704bcc73bbbf6d12e2cca672b492b04
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/native-config-sync.ts:148:33"
```

### Pattern

`^\s*enableScripts\s*:\s*false\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f7cf0f2ba262a1d7038100509f69f52e:search

```yaml
regex_id: f7cf0f2ba262a1d7038100509f69f52e
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/disposable-email-domains/scripts/disposable-email-sync-manager.js:11:25"
```

### Pattern

`^refs\/heads\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f88bca4c6730073521d14c2e83291863:search

```yaml
regex_id: f88bca4c6730073521d14c2e83291863
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/iso-locale/src/locale.ts:8:21"
```

### Pattern

`^[A-Z]{4}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f89f8afbe0ff51c2c84c8f06536bf8ff:search

```yaml
regex_id: f89f8afbe0ff51c2c84c8f06536bf8ff
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/runtime/toolchain.ts:814:8"
```

### Pattern

`^\d[\d.]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f8a1a49e0c197b0763c925066cbab994:search

```yaml
regex_id: f8a1a49e0c197b0763c925066cbab994
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/storage/storage/src/storage/storage.ts:506:12"
```

### Pattern

`^[A-Z]:[/\\]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f8f6f2396e494e6ccc61c6672f69adbe:search

```yaml
regex_id: f8f6f2396e494e6ccc61c6672f69adbe
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/package/src/lockfile.ts:396:23"
```

### Pattern

`^ {2}(['"]?[^\s:][^:\n]*?['"]?):\s*\n((?: {4}[^\n]*\n?)+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:f940ff2ea524a0d83166b1719b9d8620:email

```yaml
regex_id: f940ff2ea524a0d83166b1719b9d8620
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/providers/postmark.ts:51:56"
```

### Pattern

`<[^<>]+>`

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

## intent_mismatch:f9abdc7bec2e8e870044bdaaa7476d2a:email

```yaml
regex_id: f9abdc7bec2e8e870044bdaaa7476d2a
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/providers/aws-ses/provider.ts:248:62"
```

### Pattern

`<MessageId>(.*?)<\/MessageId>`

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

## usage_mismatch:fa2d3b14d6059212117063e485fa904e:search

```yaml
regex_id: fa2d3b14d6059212117063e485fa904e
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/string/src/case/identify-case.ts:7:28"
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

## usage_mismatch:fbb5542df259d6f261b8085a6ccbe87a:search

```yaml
regex_id: fbb5542df259d6f261b8085a6ccbe87a
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/ansi/src/helpers.ts:11:21"
```

### Pattern

`^(?:msys|cygwin)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:fc26465661a4f3e779e26d14ea23b090:email

```yaml
regex_id: fc26465661a4f3e779e26d14ea23b090
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/utils/parse-eml.ts:10:23"
```

### Pattern

`boundary=(?:"([^"]+)"|([^";]+))`

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

## usage_mismatch:fc63e32e745bb4400ab3869fd1a5b0e4:search

```yaml
regex_id: fc63e32e745bb4400ab3869fd1a5b0e4
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/dlx/changelog.ts:99:22"
```

### Pattern

`^(#{1,4})\s+(.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fcb87fd71899899d4bb7736c7434778f:search

```yaml
regex_id: fcb87fd71899899d4bb7736c7434778f
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/terminal/fmt/src/inspect-colors.ts:182:27"
```

### Pattern

`^#([\dA-F])([\dA-F])([\dA-F])([\dA-F])?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:fd26c7504f3ad63ab133650cc4d19061:email

```yaml
regex_id: fd26c7504f3ad63ab133650cc4d19061
schema_version: "1"
kind: intent_mismatch
corpus: visulima-visulima
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/reply-parser.ts:25:4"
```

### Pattern

`^-{2,}\s*Forwarded message\s*-{2,}`

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

## usage_mismatch:fd26c7504f3ad63ab133650cc4d19061:search

```yaml
regex_id: fd26c7504f3ad63ab133650cc4d19061
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email/src/inbound/reply-parser.ts:25:4"
```

### Pattern

`^-{2,}\s*Forwarded message\s*-{2,}`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fd5a3f59c14e925c8dc368f90c0e89e6:search

```yaml
regex_id: fd5a3f59c14e925c8dc368f90c0e89e6
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/util/hadolint/fixers.ts:41:62"
```

### Pattern

`^(\s*)ADD\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fd77c0e3309df916a5d6f0b233f6bad9:search

```yaml
regex_id: fd77c0e3309df916a5d6f0b233f6bad9
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/schema/schemas.ts:35:22"
```

### Pattern

`^-?(?:0|[1-9]\d*)(?:\.\d+)?(?:e[-+]?\d+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fd7c66e8e6bace8c950519ebe94a06cb:search

```yaml
regex_id: fd7c66e8e6bace8c950519ebe94a06cb
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/dev-toolbar/src/apps/seo/seo-app.tsx:460:26"
```

### Pattern

`^\/\/<!\[CDATA\[`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fd92f866c91f081cd3bff3987722fba1:search

```yaml
regex_id: fd92f866c91f081cd3bff3987722fba1
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/email/email-provider-mx/src/index.ts:53:27"
```

### Pattern

`\.$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fdb676e3e7713af005321d35007a0e96:search

```yaml
regex_id: fdb676e3e7713af005321d35007a0e96
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/security/apply-direct.ts:218:28"
```

### Pattern

`^(?:workspace|file|link|portal|patch|git\+|git:|github:|npm:|catalog|jsr|http|https):`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fe313394beb91e662cf112d1aa72d0c2:search

```yaml
regex_id: fe313394beb91e662cf112d1aa72d0c2
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/string/src/constants.ts:93:68"
```

### Pattern

`^[ \t]*[\r\n][ \t\r\n]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fec147c15ebc191d9d4143ee4c585f7d:search

```yaml
regex_id: fec147c15ebc191d9d4143ee4c585f7d
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/util/codeowners-sources.ts:146:28"
```

### Pattern

`^(?:https?:\/\/)?(?:www\.)?github\.com\/([^/?#]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ff4bc2d7d6eae4a94acfb902bd9e94e0:search

```yaml
regex_id: ff4bc2d7d6eae4a94acfb902bd9e94e0
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/data-manipulation/yaml/src/schema/schemas.ts:43:26"
```

### Pattern

`^[-+]?0b[01_]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ffb5c4567b04ecd776e2ba72594c2349:search

```yaml
regex_id: ffb5c4567b04ecd776e2ba72594c2349
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/error-debugging/vite-overlay/src/utils/find-module-for-path.ts:4:26"
```

### Pattern

`^\/@fs\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ffe1f791caeb723db7bfc17dec55ecd9:search

```yaml
regex_id: ffe1f791caeb723db7bfc17dec55ecd9
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/deps/catalog-proposals.ts:175:56"
```

### Pattern

`^catalog\s*:\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fff8cc8bec0756a7d93625842ee8a301:search

```yaml
regex_id: fff8cc8bec0756a7d93625842ee8a301
schema_version: "1"
kind: usage_mismatch
corpus: visulima-visulima
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/visulima-visulima/rules/packages/tooling/vis/src/report/audit/html.ts:152:37"
```

### Pattern

`^([^:]{2,40}):\s*(.+)$`

### Context

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
corpus: visulima-visulima
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
corpus: visulima-visulima
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
corpus: visulima-visulima
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
corpus: visulima-visulima
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

---
schema_version: "1"
corpus: three-ui
findings: 260
---

# three-ui batch findings

## usage_mismatch:02a28e4f3f83c3e28f82468cf0a84bf3:search

```yaml
regex_id: 02a28e4f3f83c3e28f82468cf0a84bf3
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:44055:11"
```

### Pattern

`^(ipfs)://(.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:06f6de013223edad1541a53e9785c90d:search

```yaml
regex_id: 06f6de013223edad1541a53e9785c90d
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:34606:45"
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

## usage_mismatch:084de26efa732c4ffecc61f4b102002d:search

```yaml
regex_id: 084de26efa732c4ffecc61f4b102002d
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/editor/manifest-builder.js:1118:7"
```

### Pattern

`\.(glb|gltf)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0954c8f99b12b6425976d51ced4f090b:search

```yaml
regex_id: 0954c8f99b12b6425976d51ced4f090b
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:264:19"
```

### Pattern

`^(`+)([^`]|[^`][\s\S]*?[^`])\1(?!`)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0a45b46fcd91e508ec832e156b8bd6bd:search

```yaml
regex_id: 0a45b46fcd91e508ec832e156b8bd6bd
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/app.js:80:27"
```

### Pattern

`^eip155:(\d+):(0x[a-fA-F0-9]{40})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0ac0e9df84cb96223f204e8f885f30c0:search

```yaml
regex_id: 0ac0e9df84cb96223f204e8f885f30c0
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/widgets/passport.js:114:7"
```

### Pattern

`^https:\/\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0d85212107b96f5c5722ceb2e50dd637:search

```yaml
regex_id: 0d85212107b96f5c5722ceb2e50dd637
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/erc8004/resolver.js:57:13"
```

### Pattern

`^eip155:(\d+)\/erc721:(0x[0-9a-fA-F]{40})\/(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0d8705c236235c99b8739106ec1b503a:search

```yaml
regex_id: 0d8705c236235c99b8739106ec1b503a
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:77:22"
```

### Pattern

`^ *:-+: *$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0e47a338298f489a7d796e2e6a2cf9a3:search

```yaml
regex_id: 0e47a338298f489a7d796e2e6a2cf9a3
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:49204:73"
```

### Pattern

`^ktx`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0f9c19d6c09db9f6419b494d5b3f04ba:search

```yaml
regex_id: 0f9c19d6c09db9f6419b494d5b3f04ba
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:47542:85"
```

### Pattern

`^eip155:(\d+)\/erc721:(0x[0-9a-fA-F]{40})\/(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:130019932404125180b23f298bd4894b:search

```yaml
regex_id: 130019932404125180b23f298bd4894b
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/artifact.js:22:1"
```

### Pattern

`^https:\/\/[^/]+\.vercel\.app$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:146f0a3b460e53aeb6bfe52c3cc21b14:search

```yaml
regex_id: 146f0a3b460e53aeb6bfe52c3cc21b14
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:137:18"
```

### Pattern

`^[^\n]+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1715335b399ec50f66f16a876fc81144:search

```yaml
regex_id: 1715335b399ec50f66f16a876fc81144
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/erc8004/resolve-avatar.js:49:5"
```

### Pattern

`^[a-z0-9][a-z0-9-]*(\.[a-z0-9-]+)+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1794aec02b053dcc650d23b31a48b008:search

```yaml
regex_id: 1794aec02b053dcc650d23b31a48b008
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/agent-oembed.js:95:37"
```

### Pattern

`^\/agent\/([A-Za-z0-9_-]+)\/?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:18f674589bb591a4ca3a63a6d33d6716:search

```yaml
regex_id: 18f674589bb591a4ca3a63a6d33d6716
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:37397:19"
```

### Pattern

`^0x[0-9a-f]{40}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1a7797f30820831a9b1ac0ec9ec33a5a:search

```yaml
regex_id: 1a7797f30820831a9b1ac0ec9ec33a5a
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:41207:58"
```

### Pattern

`^(u?int)([0-9]*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1b2459a12b90eaddf4f9b505e9d0c4b1:search

```yaml
regex_id: 1b2459a12b90eaddf4f9b505e9d0c4b1
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/widgets/oembed.js:125:41"
```

### Pattern

`^\/w\/([A-Za-z0-9_-]+)\/?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1b43fb5d757e9be03a252c14449dce55:search

```yaml
regex_id: 1b43fb5d757e9be03a252c14449dce55
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:47295:24"
```

### Pattern

`^data:application\/json(?:;base64)?,(.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1c0a50c7434e6d58bbf01e186b8f839f:search

```yaml
regex_id: 1c0a50c7434e6d58bbf01e186b8f839f
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:64:21"
```

### Pattern

`^ {0,3}>`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1f0e0b070d566af491822448cdbd1efb:search

```yaml
regex_id: 1f0e0b070d566af491822448cdbd1efb
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:266:19"
```

### Pattern

`^(`+|[^`])(?:(?= {2,}\n)|[\s\S]*?(?:(?=[\\<!\[`*_]|\b_|$)|[^ ](?= {2,}\n)))`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1f836b15ff0722dc0ef157f66f4faa03:search

```yaml
regex_id: 1f836b15ff0722dc0ef157f66f4faa03
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:39941:22"
```

### Pattern

`^(u?)int(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1fb2028dd52945c74fb2b9ea31428f6f:search

```yaml
regex_id: 1fb2028dd52945c74fb2b9ea31428f6f
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/artifact.js:18:1"
```

### Pattern

`^https:\/\/[^/]+\.cloudfront\.net$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2070d8370cbdc3f7b29fe52c35069d14:search

```yaml
regex_id: 2070d8370cbdc3f7b29fe52c35069d14
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/artifact.js:20:1"
```

### Pattern

`^https:\/\/[^/]+\.blob\.core\.windows\.net$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:20a192bcc1089dcc9e468c943618d56a:search

```yaml
regex_id: 20a192bcc1089dcc9e468c943618d56a
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:33545:12"
```

### Pattern

`^([a-z]+:|\/)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2140f0c7e52eac5d52e37e9cbab9396f:search

```yaml
regex_id: 2140f0c7e52eac5d52e37e9cbab9396f
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:25913:26"
```

### Pattern

`^#([A-F0-9])([A-F0-9])([A-F0-9])$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:217241ea98e608153dd0cdf9ea6d8ecd:search

```yaml
regex_id: 217241ea98e608153dd0cdf9ea6d8ecd
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:80:13"
```

### Pattern

`^<\/a>`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:23869c19de19a95cbdcfd39f413734c3:search

```yaml
regex_id: 23869c19de19a95cbdcfd39f413734c3
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:263:17"
```

### Pattern

`^\\([!"#$%&'()*+,\-./:;<=>?@\[\]\\^_`{|}~])`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2402a21173da3445dd40b5d991c04208:search

```yaml
regex_id: 2402a21173da3445dd40b5d991c04208
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/_lib/validate.js:80:39"
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

## usage_mismatch:2414edcb2b7ae7c724efeb987d8d7807:search

```yaml
regex_id: 2414edcb2b7ae7c724efeb987d8d7807
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:33871:60"
```

### Pattern

`^0x[0-9a-f]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2522f6de8d0e4b1a237c6fd3611a08c3:search

```yaml
regex_id: 2522f6de8d0e4b1a237c6fd3611a08c3
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:32923:20"
```

### Pattern

`^ar:\/\/(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2562bc74d70ace6e3628d551b5b48916:search

```yaml
regex_id: 2562bc74d70ace6e3628d551b5b48916
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:28820:39"
```

### Pattern

`[,:;]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2a1bf2e1c96acb4e25c965d80a2c957f:search

```yaml
regex_id: 2a1bf2e1c96acb4e25c965d80a2c957f
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/widgets/oembed.js:121:2"
```

### Pattern

`^https?:\/\/localhost(:\d+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2af059c919b50c3b194270242cf13860:search

```yaml
regex_id: 2af059c919b50c3b194270242cf13860
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:40259:66"
```

### Pattern

`^([a-zA-Z$_][a-zA-Z0-9$_]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2b323910b7e385c220aab057eafbab96:search

```yaml
regex_id: 2b323910b7e385c220aab057eafbab96
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:24486:226"
```

### Pattern

`^data\:image\/ktx2`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2b82be6f1c045d9e4d2e8f794aa0a577:search

```yaml
regex_id: 2b82be6f1c045d9e4d2e8f794aa0a577
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:72:18"
```

### Pattern

`^<(.*)>$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2bf54e4c2679d74d0ef46a12b8612b3d:search

```yaml
regex_id: 2bf54e4c2679d74d0ef46a12b8612b3d
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/app.js:91:35"
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

## usage_mismatch:2e9d33f62334dd2c5dfc8e3887f7160a:search

```yaml
regex_id: 2e9d33f62334dd2c5dfc8e3887f7160a
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/editor/manifest-builder.js:1554:6"
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

## usage_mismatch:30e56be6e77c3df52df3fe6a4bedb94d:search

```yaml
regex_id: 30e56be6e77c3df52df3fe6a4bedb94d
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/vite.config.js:156:27"
```

### Pattern

`^\/a\/[^/]+(?:\/[^/]+){1,2}\/?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:314364f7c33b6e1b491b4723e1bc22e1:search

```yaml
regex_id: 314364f7c33b6e1b491b4723e1bc22e1
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/erc8004/resolve-avatar.js:45:5"
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

## usage_mismatch:339b65668d44777cf1652fcf5e5468e0:search

```yaml
regex_id: 339b65668d44777cf1652fcf5e5468e0
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:136:19"
```

### Pattern

`^([^\n]+(?:\n(?!hr|heading|lheading|blockquote|fences|list|html|table| +\n)[^\n]+)*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:347640b3634305dae30c5d9bc7ccd8db:search

```yaml
regex_id: 347640b3634305dae30c5d9bc7ccd8db
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:48567:20"
```

### Pattern

`^---\n[\s\S]*?\n---\n?([\s\S]*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:34c2d24d2f4135bd3f476e71309abe30:search

```yaml
regex_id: 34c2d24d2f4135bd3f476e71309abe30
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:12535:203"
```

### Pattern

`^blob:.*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:35c3c13eb78193090ca3e495bb5aa21d:search

```yaml
regex_id: 35c3c13eb78193090ca3e495bb5aa21d
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/erc8004/resolver.js:61:13"
```

### Pattern

`^onchain:(\d+):(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:37bae7c19bd20ff5c128ddf15b277735:search

```yaml
regex_id: 37bae7c19bd20ff5c128ddf15b277735
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:29919:54"
```

### Pattern

`[ \t\n\f\r]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3812a1fb2d79b259ede082fe98021d73:search

```yaml
regex_id: 3812a1fb2d79b259ede082fe98021d73
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:41207:22"
```

### Pattern

`^bytes([0-9]*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3992628324709963aca7b5541b67708a:search

```yaml
regex_id: 3992628324709963aca7b5541b67708a
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/erc8004/resolver.js:69:13"
```

### Pattern

`^\/?a\/(\d+)\/(\d+)(?:\/(embed))?\/?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3abdb1791212a5667e024ae5adc3555e:search

```yaml
regex_id: 3abdb1791212a5667e024ae5adc3555e
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:34254:68"
```

### Pattern

`^ipfs://(ipfs/)?(.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3cf84d7713e6c60d0f83ae479a228286:search

```yaml
regex_id: 3cf84d7713e6c60d0f83ae479a228286
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/widgets/passport.js:240:6"
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

## usage_mismatch:3e42e42785d06dab345c0666b79db430:search

```yaml
regex_id: 3e42e42785d06dab345c0666b79db430
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/app.js:1205:23"
```

### Pattern

`\.(gltf|glb)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3f37667a23b2539d0b9250ca47863476:search

```yaml
regex_id: 3f37667a23b2539d0b9250ca47863476
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/auth/siwe/[action].js:126:18"
```

### Pattern

`^https?:\/\/localhost(:\d+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3f3b797caf47f64344e79b52aae57612:search

```yaml
regex_id: 3f3b797caf47f64344e79b52aae57612
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:83:23"
```

### Pattern

`^<`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:404dfeab56b3e9902588d7b35d6d29b3:search

```yaml
regex_id: 404dfeab56b3e9902588d7b35d6d29b3
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/widgets/passport.js:240:6"
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

## usage_mismatch:40b8a00900136ca80bed01706086e9df:search

```yaml
regex_id: 40b8a00900136ca80bed01706086e9df
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/app.js:77:22"
```

### Pattern

`^\/a\/([^/]+)(?:\/([^/]+))?(?:\/([^/]+))?\/?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:41f07c04ca4e9b83912c5243a2f96da6:search

```yaml
regex_id: 41f07c04ca4e9b83912c5243a2f96da6
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:44020:17"
```

### Pattern

`^ipfs:\/\/ipfs\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4238127e2f47c1d9a953d47637d7ad5b:search

```yaml
regex_id: 4238127e2f47c1d9a953d47637d7ad5b
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/marked-katex-extension/index.js:4:18"
```

### Pattern

`^(\${1,2})\n((?:\\[^]|[^\\])+?)\n\1(?:\n|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:455cb153cda57b997b29fe8881697974:search

```yaml
regex_id: 455cb153cda57b997b29fe8881697974
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/erc8004/resolver.js:61:13"
```

### Pattern

`^onchain:(\d+):(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:46341b27fcf3d9109f6fdc7b51d844a1:search

```yaml
regex_id: 46341b27fcf3d9109f6fdc7b51d844a1
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/widgets/oembed.js:122:2"
```

### Pattern

`^https?:\/\/3d\.irish$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:46b2092e93d6a86bb877f9145eb24899:search

```yaml
regex_id: 46b2092e93d6a86bb877f9145eb24899
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:47542:301"
```

### Pattern

`^agent:\/\/(\d+)\/(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:492b7a015c338ff3db21fa018c2a8677:search

```yaml
regex_id: 492b7a015c338ff3db21fa018c2a8677
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/erc8004/resolver.js:69:13"
```

### Pattern

`^\/?a\/(\d+)\/(\d+)(?:\/(embed))?\/?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4a826331468376931c6f69f7be021169:search

```yaml
regex_id: 4a826331468376931c6f69f7be021169
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/erc8004/resolver.js:71:13"
```

### Pattern

`^\/?a\/(\d+)\/(0x[0-9a-fA-F]{40})\/(\d+)\/?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4ab81e0f9db4ee2a17dbeca02e6a7af0:search

```yaml
regex_id: 4ab81e0f9db4ee2a17dbeca02e6a7af0
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/tts/edge.js:40:17"
```

### Pattern

`^[+-]\d+Hz$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4b062c187e634e5738c856fa3bea1c75:search

```yaml
regex_id: 4b062c187e634e5738c856fa3bea1c75
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:40233:20"
```

### Pattern

`^u?int`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4ccf6643fcc02956add2277af75f341b:search

```yaml
regex_id: 4ccf6643fcc02956add2277af75f341b
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/editor/publish.js:219:15"
```

### Pattern

`^[a-z0-9]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4d7c41e056e016dee9ce4c8532ecab71:search

```yaml
regex_id: 4d7c41e056e016dee9ce4c8532ecab71
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/app.js:88:67"
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

## usage_mismatch:4e223865f93ed293d1e76b91ea4b551d:search

```yaml
regex_id: 4e223865f93ed293d1e76b91ea4b551d
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:68:24"
```

### Pattern

`^ {1,4}(?=( {4})*[^ ])`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4e649bc96b2f30169d405beea2fe122e:search

```yaml
regex_id: 4e649bc96b2f30169d405beea2fe122e
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:28687:9"
```

### Pattern

`^\p{M}+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4edc9b2ec8faae9dc45eee06b856205a:search

```yaml
regex_id: 4edc9b2ec8faae9dc45eee06b856205a
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:37465:29"
```

### Pattern

`^u?int[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4ee6a2da2d68b58a18868f5937e1d4c4:search

```yaml
regex_id: 4ee6a2da2d68b58a18868f5937e1d4c4
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/erc8004/resolver.js:57:13"
```

### Pattern

`^eip155:(\d+)\/erc721:(0x[0-9a-fA-F]{40})\/(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4f8c2e5712c4fe758c46b9057d71e765:search

```yaml
regex_id: 4f8c2e5712c4fe758c46b9057d71e765
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/erc8004/resolver.js:65:13"
```

### Pattern

`^agent:\/\/(\d+)\/(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:526abb0b25f0f6d5d069581d7781a99e:search

```yaml
regex_id: 526abb0b25f0f6d5d069581d7781a99e
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/contracts/lib/openzeppelin-contracts/scripts/release/workflow/github-release.js:28:18"
```

### Pattern

`^ {0,3}(?<lead>#{1,6})(?: [ \t\v\f]*(?<text>.*?)[ \t\v\f]*)?(?:[\n\r]+|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:53d3d535734664c34f88db9b5d9d04f4:search

```yaml
regex_id: 53d3d535734664c34f88db9b5d9d04f4
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/erc8004/resolve-avatar.js:353:29"
```

### Pattern

`^agent:\/\/([^/]+)\/(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:53f4ac0c368583bb8268b41403b857e8:search

```yaml
regex_id: 53f4ac0c368583bb8268b41403b857e8
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/element.js:1523:22"
```

### Pattern

`^---\n[\s\S]*?\n---\n?([\s\S]*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5424232d10732eb90c26e65091137eee:search

```yaml
regex_id: 5424232d10732eb90c26e65091137eee
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:81:23"
```

### Pattern

`^<(pre|code|kbd|script)(\s|>)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:545c40598ae6825e56fb852eae15a122:search

```yaml
regex_id: 545c40598ae6825e56fb852eae15a122
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:24495:10"
```

### Pattern

`^((?!chrome|android).)*safari`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:56183c1e0c8e39feae51ec5db0bd3525:search

```yaml
regex_id: 56183c1e0c8e39feae51ec5db0bd3525
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:33887:44"
```

### Pattern

`^0x[0-9A-Fa-f]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:571cba5fe607aa53c2b5f7e5f5725d64:search

```yaml
regex_id: 571cba5fe607aa53c2b5f7e5f5725d64
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:40259:8"
```

### Pattern

`^(\s*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:573310f95f46c963a43f6638df164773:search

```yaml
regex_id: 573310f95f46c963a43f6638df164773
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/a-og.js:62:20"
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

## usage_mismatch:58094eee508a3b60b842f19edd9132ed:search

```yaml
regex_id: 58094eee508a3b60b842f19edd9132ed
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/app.js:72:35"
```

### Pattern

`^(\/a\/.+?)\/embed\/?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5995f98bfc0ff09c021b4aaa8fee4542:search

```yaml
regex_id: 5995f98bfc0ff09c021b4aaa8fee4542
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/contracts/lib/openzeppelin-contracts/scripts/release/format-changelog.js:15:28"
```

### Pattern

`^## (\d+\.\d+\.\d+(-rc\.\d+)?)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5b1f02d280e290ca8f7a317db2ccc7ac:search

```yaml
regex_id: 5b1f02d280e290ca8f7a317db2ccc7ac
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:99:19"
```

### Pattern

`^\S*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5e44d28da965fac4a20de8e2052e001f:search

```yaml
regex_id: 5e44d28da965fac4a20de8e2052e001f
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/app.js:108:31"
```

### Pattern

`^(\d+):(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:608aa5fd6bce420134b0ad33f6c9db07:search

```yaml
regex_id: 608aa5fd6bce420134b0ad33f6c9db07
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:55:16"
```

### Pattern

`#$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:61f720d7aef695efbff6f705ef6bb20a:search

```yaml
regex_id: 61f720d7aef695efbff6f705ef6bb20a
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:25945:26"
```

### Pattern

`^rgba\(\s*(\S+)\s*,\s*(\S+)\s*,\s*(\S+)\s*,\s*(\S+)\s*\)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:63b5d78f646fffe46ce79d1f94f41416:search

```yaml
regex_id: 63b5d78f646fffe46ce79d1f94f41416
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:40259:36"
```

### Pattern

`^([0-9]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6458ce41dfc8ce524551c761461c3127:search

```yaml
regex_id: 6458ce41dfc8ce524551c761461c3127
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/permissions/[action].js:81:10"
```

### Pattern

`^(0x[0-9a-fA-F]+|\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:649ae86418e43b8216c463e2a5b6a4de:search

```yaml
regex_id: 649ae86418e43b8216c463e2a5b6a4de
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:44056:2"
```

### Pattern

`^(https)://(.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:65da7368385e7e1190c010237f82764f:search

```yaml
regex_id: 65da7368385e7e1190c010237f82764f
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:56:23"
```

### Pattern

`^ `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:680c959ec1e1794d36729bd8e911f756:search

```yaml
regex_id: 680c959ec1e1794d36729bd8e911f756
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:34643:75"
```

### Pattern

`^https?:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:68b2a138c418c389799758d2161769c3:search

```yaml
regex_id: 68b2a138c418c389799758d2161769c3
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/editor/manifest-builder.js:1542:6"
```

### Pattern

`^### `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:68ba4d1a5af301a2c61da2968e4b0305:search

```yaml
regex_id: 68ba4d1a5af301a2c61da2968e4b0305
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/marked-katex-extension/index.js:7:29"
```

### Pattern

`^\\\[(\s*)((?:\\[^]|[^\\])+?)(\s*)\\](?:\n|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:68dbd4726b5d3d22f3d1d7ea55ce9dcb:search

```yaml
regex_id: 68dbd4726b5d3d22f3d1d7ea55ce9dcb
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:85:23"
```

### Pattern

`^([^'"]*[^\s])\s+(['"])(.*)\2`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:68f3d2664af5aa73c87a9227987c4125:search

```yaml
regex_id: 68f3d2664af5aa73c87a9227987c4125
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:69:16"
```

### Pattern

`^\[[ xX]\] `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:69b2be6f1f11d1e14da665fbcdaf0243:search

```yaml
regex_id: 69b2be6f1f11d1e14da665fbcdaf0243
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/editor/manifest-builder.js:1477:6"
```

### Pattern

`^### `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6c0ff65446f6d1364ec98227c061b80f:search

```yaml
regex_id: 6c0ff65446f6d1364ec98227c061b80f
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:44020:70"
```

### Pattern

`^ipfs:\/\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6c44ba2659def0f346323024207bec49:search

```yaml
regex_id: 6c44ba2659def0f346323024207bec49
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:40259:114"
```

### Pattern

`^([a-zA-Z$_][a-zA-Z0-9$_]*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6d09c94fe93410f6c9a4a804d61c28dc:search

```yaml
regex_id: 6d09c94fe93410f6c9a4a804d61c28dc
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/vite.config.js:141:22"
```

### Pattern

`^\/marketplace\/agents\/[^/]+\/?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6e05a1b55d68deb988896cd32d0ff682:search

```yaml
regex_id: 6e05a1b55d68deb988896cd32d0ff682
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/element.js:2489:22"
```

### Pattern

`^---\n[\s\S]*?\n---\n?([\s\S]*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6fd93854d2a6759ac73d0ba13db1109f:search

```yaml
regex_id: 6fd93854d2a6759ac73d0ba13db1109f
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/permissions/[action].js:64:34"
```

### Pattern

`^0x([0-9a-fA-F]{2})*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:70934c6b2bc119314fb821bc67b2bd01:search

```yaml
regex_id: 70934c6b2bc119314fb821bc67b2bd01
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:12535:52"
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

## usage_mismatch:70ec4a03c9ba0aba4af0d85959ce0024:search

```yaml
regex_id: 70ec4a03c9ba0aba4af0d85959ce0024
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/artifact.js:16:1"
```

### Pattern

`^https:\/\/[^/]+\.r2\.cloudflarestorage\.com$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:71d9dca246eeeb49ef3b8e5e1d982e84:search

```yaml
regex_id: 71d9dca246eeeb49ef3b8e5e1d982e84
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:100:19"
```

### Pattern

`\n$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:73e5fe9388e0483e9a3077517d186b58:search

```yaml
regex_id: 73e5fe9388e0483e9a3077517d186b58
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/_lib/validate.js:84:39"
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

## usage_mismatch:753e563efa6c086644a853684719e510:search

```yaml
regex_id: 753e563efa6c086644a853684719e510
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/erc8004/resolve-avatar.js:49:5"
```

### Pattern

`^[a-z0-9][a-z0-9-]*(\.[a-z0-9-]+)+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:759e69a7e9192ae7b93a9fe88b6e2342:search

```yaml
regex_id: 759e69a7e9192ae7b93a9fe88b6e2342
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/erc8004/resolve-avatar.js:45:5"
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

## usage_mismatch:75fe289d18c0efceb68ce77e33ded1f8:search

```yaml
regex_id: 75fe289d18c0efceb68ce77e33ded1f8
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:47542:390"
```

### Pattern

`^\/?a\/(\d+)\/(\d+)(?:\/(embed))?\/?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7610d045c29e075a408ce70916f07147:search

```yaml
regex_id: 7610d045c29e075a408ce70916f07147
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/vite.config.js:145:27"
```

### Pattern

`^\/agent\/[^/]+\/embed$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7620a56d5c377ce4d3e85877bf9c11fd:search

```yaml
regex_id: 7620a56d5c377ce4d3e85877bf9c11fd
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/marked-katex-extension/index.js:6:1"
```

### Pattern

`^\\\((?!\$)((?:\\.|[^\\\n])*?(?:\\.|[^\\\n$]))\\\)(?=[\s?!.,:？！。，：]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:76f789ce84a97218f6f16c2d0d460503:search

```yaml
regex_id: 76f789ce84a97218f6f16c2d0d460503
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/widgets/passport.js:139:6"
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

## usage_mismatch:7b3e1a54a17e501806bcd3bd2bc2b8d7:search

```yaml
regex_id: 7b3e1a54a17e501806bcd3bd2bc2b8d7
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/erc8004/resolver.js:53:17"
```

### Pattern

`^eip155:(\d+):(0x[0-9a-fA-F]{40}):(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7bd8d30f9fe867aae3e14d7c887bf137:search

```yaml
regex_id: 7bd8d30f9fe867aae3e14d7c887bf137
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/element.js:1207:11"
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

## usage_mismatch:7c1ac441ea2afcb009b54788363f590c:search

```yaml
regex_id: 7c1ac441ea2afcb009b54788363f590c
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:78:20"
```

### Pattern

`^ *:-+ *$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7cc62c5eb30009888765a50e935005c2:search

```yaml
regex_id: 7cc62c5eb30009888765a50e935005c2
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/editor/manifest-builder.js:1489:6"
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

## usage_mismatch:7ceab63853c357e996ef0f109d2dc53b:search

```yaml
regex_id: 7ceab63853c357e996ef0f109d2dc53b
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:57:21"
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

## usage_mismatch:7e61a426b35a25b9f26c64cb4059d811:search

```yaml
regex_id: 7e61a426b35a25b9f26c64cb4059d811
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/erc8004/resolve-avatar.js:46:5"
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

## usage_mismatch:7ecbc7ace27c777b8c5088026d2c1345:search

```yaml
regex_id: 7ecbc7ace27c777b8c5088026d2c1345
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:32920:20"
```

### Pattern

`^ipfs:\/\/(.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7f4784f61590bf0c1b2bf7c55c57c4d0:search

```yaml
regex_id: 7f4784f61590bf0c1b2bf7c55c57c4d0
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/vite.config.js:150:27"
```

### Pattern

`^\/a\/[^/]+(?:\/[^/]+){1,2}\/edit\/?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7f54c742d514558a9b7c05a42fc56dd7:search

```yaml
regex_id: 7f54c742d514558a9b7c05a42fc56dd7
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/permissions/[action].js:65:36"
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

## usage_mismatch:8015275a9c3463604d62b599f4bd260c:search

```yaml
regex_id: 8015275a9c3463604d62b599f4bd260c
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/app.js:93:35"
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

## usage_mismatch:8117a1e54f0b6669cd8bf08474b64855:search

```yaml
regex_id: 8117a1e54f0b6669cd8bf08474b64855
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:265:11"
```

### Pattern

`^( {2,}|\\)\n(?!\s*$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:82f28cef6174bed17e4415d4d72530fb:search

```yaml
regex_id: 82f28cef6174bed17e4415d4d72530fb
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/_lib/validate.js:62:9"
```

### Pattern

`^[a-f0-9]{64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:83845181ad4535c4d320a141c003ca9d:search

```yaml
regex_id: 83845181ad4535c4d320a141c003ca9d
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:40259:163"
```

### Pattern

`^(address|bool|bytes([0-9]*)|string|u?int([0-9]*))$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:83c9e402e1b5b0316c0636dadddd998d:search

```yaml
regex_id: 83c9e402e1b5b0316c0636dadddd998d
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:37374:14"
```

### Pattern

`^XE[0-9]{2}[0-9A-Za-z]{30,31}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:83f26ae6c1d26a991eced1cdd414f66a:search

```yaml
regex_id: 83f26ae6c1d26a991eced1cdd414f66a
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/app.js:75:22"
```

### Pattern

`^\/a\/([^/]+)(?:\/([^/]+))?(?:\/([^/]+))?\/?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:85b29d7ac0acb78114797bde201e51bb:search

```yaml
regex_id: 85b29d7ac0acb78114797bde201e51bb
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/app.js:88:34"
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

## usage_mismatch:86a9d711f9e5be77c54b9f56ae306a03:search

```yaml
regex_id: 86a9d711f9e5be77c54b9f56ae306a03
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:98:15"
```

### Pattern

`^ +$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:86afbaf0a6d76e1eacdfba95e8759d1d:url

```yaml
regex_id: 86afbaf0a6d76e1eacdfba95e8759d1d
schema_version: "1"
kind: intent_mismatch
corpus: three-ui
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/vite.config.js:269:18"
```

### Pattern

`^https:\/\/fonts\.gstatic\.com\/.*`

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

## usage_mismatch:86afbaf0a6d76e1eacdfba95e8759d1d:search

```yaml
regex_id: 86afbaf0a6d76e1eacdfba95e8759d1d
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/vite.config.js:269:18"
```

### Pattern

`^https:\/\/fonts\.gstatic\.com\/.*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:873781b2f43c41c2da9f6dc4e0726ada:search

```yaml
regex_id: 873781b2f43c41c2da9f6dc4e0726ada
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/widgets/[id]/[action].js:249:6"
```

### Pattern

`^https:\/\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:874913faf44ecddd5335885cca6b01aa:search

```yaml
regex_id: 874913faf44ecddd5335885cca6b01aa
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/permissions/[action].js:63:33"
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

## usage_mismatch:87f6bd173a6b3c804aa21cd1b47db84e:search

```yaml
regex_id: 87f6bd173a6b3c804aa21cd1b47db84e
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/extensions/container.ts:58:23"
```

### Pattern

`^:::[^:\n\s]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8824eb1870719f50ee757276fc7687b6:search

```yaml
regex_id: 8824eb1870719f50ee757276fc7687b6
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/auth/siwe/[action].js:286:6"
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

## usage_mismatch:88be59a3bb0c8071e343797fb98c2ee8:search

```yaml
regex_id: 88be59a3bb0c8071e343797fb98c2ee8
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/vite.config.js:143:27"
```

### Pattern

`^\/agent\/[^/]+\/edit$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:88c7274f83ff7174a74ada0ddfbacf24:search

```yaml
regex_id: 88c7274f83ff7174a74ada0ddfbacf24
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/artifact.js:12:20"
```

### Pattern

`^[a-z0-9_-]{3,64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8981deeba70bdcafbf728c6c37e3e062:search

```yaml
regex_id: 8981deeba70bdcafbf728c6c37e3e062
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:29919:32"
```

### Pattern

`^[ \t\n\f\r]+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8aedabef64bf5e7ef2c6450bf4bddee9:search

```yaml
regex_id: 8aedabef64bf5e7ef2c6450bf4bddee9
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/widgets/passport.js:114:7"
```

### Pattern

`^https:\/\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8cfda12c574c43fdad966791e4fe84e4:search

```yaml
regex_id: 8cfda12c574c43fdad966791e4fe84e4
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/app.js:1266:23"
```

### Pattern

`\.(gltf|glb)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8d5648639c55411684ad995d93e1fe4d:search

```yaml
regex_id: 8d5648639c55411684ad995d93e1fe4d
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:244:9"
```

### Pattern

`^ *\[([^\]]+)\]: *<?([^\s>]+)>?(?: +(["(][^\n]+[")]))? *(?:\n+|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8fdce002e927bc049c3814e9bbced13c:search

```yaml
regex_id: 8fdce002e927bc049c3814e9bbced13c
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:11517:22"
```

### Pattern

`^([\w-]*?)([\d]+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:90b610a984567e9cb97a6233c35c9b4c:search

```yaml
regex_id: 90b610a984567e9cb97a6233c35c9b4c
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:12535:79"
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

## usage_mismatch:93752e653e80260d2260b64b6c57ad07:search

```yaml
regex_id: 93752e653e80260d2260b64b6c57ad07
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/vite.config.js:153:27"
```

### Pattern

`^\/a\/[^/]+(?:\/[^/]+){1,2}\/embed\/?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:943b87f046ea05c7c695ccc71bd927be:search

```yaml
regex_id: 943b87f046ea05c7c695ccc71bd927be
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/permissions/[action].js:1074:16"
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

## usage_mismatch:95b23342d02225d4f41155761656e5fa:search

```yaml
regex_id: 95b23342d02225d4f41155761656e5fa
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:67:21"
```

### Pattern

`^\t+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9702636920a22fb44e29c67b72fcebbc:search

```yaml
regex_id: 9702636920a22fb44e29c67b72fcebbc
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/oauth/[action].js:195:33"
```

### Pattern

`^localhost$|^127\.0\.0\.1$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:974421962050498ffaeb5df4d33fbc89:search

```yaml
regex_id: 974421962050498ffaeb5df4d33fbc89
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:397:9"
```

### Pattern

`^(~~?)(?=[^\s~])((?:\\.|[^\\])*?(?:\\.|[^\s~\\]))\1(?=[^~]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9811935d1e5912c19d4176360f4f3965:search

```yaml
regex_id: 9811935d1e5912c19d4176360f4f3965
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:24486:139"
```

### Pattern

`^data\:image\/webp`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9a17b6bee9b7afeea2420be0b81fe853:search

```yaml
regex_id: 9a17b6bee9b7afeea2420be0b81fe853
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:115:16"
```

### Pattern

`^ {0,3}(#{1,6})(?=\s|$)(.*)(?:\n+|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9afb453caf51abd840f65f5deacf6423:search

```yaml
regex_id: 9afb453caf51abd840f65f5deacf6423
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:12535:146"
```

### Pattern

`^(https?:)?\/\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9db8fce9404f25d0030b84f1a42b58f2:search

```yaml
regex_id: 9db8fce9404f25d0030b84f1a42b58f2
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:117:21"
```

### Pattern

`^(?!bull |blockCode|fences|blockquote|heading|html|table)((?:.|\n(?!\s*?\n|bull |blockCode|fences|blockquote|heading|html|table))+?)\n {0,3}(=+|-+) *(?:\n+|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9dcdef783d0bcf1af1017cce6760218e:search

```yaml
regex_id: 9dcdef783d0bcf1af1017cce6760218e
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:37369:72"
```

### Pattern

`^(0x)?[0-9a-fA-F]{40}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9eef0e268ee34df3274e544a7ff1352c:search

```yaml
regex_id: 9eef0e268ee34df3274e544a7ff1352c
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:63:21"
```

### Pattern

`\n[ \t]*\n[ \t]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a01a7e32273370747c239560242dad52:search

```yaml
regex_id: a01a7e32273370747c239560242dad52
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:62:15"
```

### Pattern

`^[ \t]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a1efdcf05215488fec4873098549b56b:search

```yaml
regex_id: a1efdcf05215488fec4873098549b56b
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:28820:9"
```

### Pattern

`^[A-Za-z0-9_]+[,:;]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a24467e8b9df74af1aeb28ba5958a2fb:search

```yaml
regex_id: a24467e8b9df74af1aeb28ba5958a2fb
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/agent-oembed.js:109:34"
```

### Pattern

`^https?:\/\/localhost(:\d+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a2f25e9e6c5574a0264eb60a5cd8d9bb:search

```yaml
regex_id: a2f25e9e6c5574a0264eb60a5cd8d9bb
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/app.js:83:23"
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

## usage_mismatch:a414a892c70019e5e0142d41ff4f79f1:search

```yaml
regex_id: a414a892c70019e5e0142d41ff4f79f1
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/element.js:820:11"
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

## usage_mismatch:a62faa0abc9dcf8839d05c7ce72d8d0e:search

```yaml
regex_id: a62faa0abc9dcf8839d05c7ce72d8d0e
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:44183:22"
```

### Pattern

`^0xe40101fa011b20([0-9a-f]*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a6d7070922b90ce09730b32688b41f66:search

```yaml
regex_id: a6d7070922b90ce09730b32688b41f66
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:34254:11"
```

### Pattern

`^data:([^;:]*)?(;base64)?,(.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a7b7422ddcea7104e974629ec6ab5ae6:search

```yaml
regex_id: a7b7422ddcea7104e974629ec6ab5ae6
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:42034:172"
```

### Pattern

`^u?int`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a886feb3da286d2c54990f5ce3c7a757:search

```yaml
regex_id: a886feb3da286d2c54990f5ce3c7a757
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/app.js:91:16"
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

## usage_mismatch:a93f5393fba1dbc0dae36bc30348a40f:search

```yaml
regex_id: a93f5393fba1dbc0dae36bc30348a40f
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:44283:25"
```

### Pattern

`^(https:\/\/|data:)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:aa6df24aae863ddc50da4f350c60ee31:search

```yaml
regex_id: aa6df24aae863ddc50da4f350c60ee31
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/app.js:82:27"
```

### Pattern

`^eip155:(\d+):(0x[a-fA-F0-9]{40})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ac136e7b4ebc9775f0d42d7d3020dd61:search

```yaml
regex_id: ac136e7b4ebc9775f0d42d7d3020dd61
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/erc8004/resolve-avatar.js:47:5"
```

### Pattern

`^\d{1,10}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:af2e90a45690972379d19b6014772e97:search

```yaml
regex_id: af2e90a45690972379d19b6014772e97
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/permissions/[action].js:580:34"
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

## usage_mismatch:af699dc193fc3e68c34bc22cf87d0b99:search

```yaml
regex_id: af699dc193fc3e68c34bc22cf87d0b99
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/artifact.js:17:1"
```

### Pattern

`^https:\/\/[^/]+\.amazonaws\.com$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b08a050ac710e465c590745675505e9b:search

```yaml
regex_id: b08a050ac710e465c590745675505e9b
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:44059:2"
```

### Pattern

`^eip155:[0-9]+/(erc[0-9]+):(.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b297566450d8c8397371f738cdbf1278:search

```yaml
regex_id: b297566450d8c8397371f738cdbf1278
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/app.js:81:23"
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

## usage_mismatch:b2d1ec4865bf43f90b8e6b2668371414:search

```yaml
regex_id: b2d1ec4865bf43f90b8e6b2668371414
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:39953:22"
```

### Pattern

`^bytes(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b2f7bfbd676f12ca7e8dd29a7c06612b:search

```yaml
regex_id: b2f7bfbd676f12ca7e8dd29a7c06612b
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/agent-oembed.js:92:34"
```

### Pattern

`^https?:\/\/localhost(:\d+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b40df2d0ac5b2fe8ea3e9f0a7e946b01:search

```yaml
regex_id: b40df2d0ac5b2fe8ea3e9f0a7e946b01
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/editor/manifest-builder.js:1546:6"
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

## usage_mismatch:b4e8167fe742b89347116f63fd697e95:search

```yaml
regex_id: b4e8167fe742b89347116f63fd697e95
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:25933:26"
```

### Pattern

`^rgb\(\s*(\S+)\s*,\s*(\S+)\s*,\s*(\S+)\s*\)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b555e32fc2107e763fccaa887044077c:search

```yaml
regex_id: b555e32fc2107e763fccaa887044077c
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:113:15"
```

### Pattern

`^ {0,3}(`{3,}(?=[^`\n]*(?:\n|$))|~{3,})([^\n]*)(?:\n|$)(?:|([\s\S]*?)(?:\n|$))(?: {0,3}\1[~`]* *(?=\n|$)|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b5fc3c3337c88dfb2153ccef0ccf2a8e:search

```yaml
regex_id: b5fc3c3337c88dfb2153ccef0ccf2a8e
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/tts/edge.js:38:17"
```

### Pattern

`^[a-zA-Z]{2,8}-[a-zA-Z]{2,8}-[a-zA-Z]{5,50}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b8c3d4ab6ccd1d1ac241809d4c350f83:search

```yaml
regex_id: b8c3d4ab6ccd1d1ac241809d4c350f83
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:66:30"
```

### Pattern

`^ {0,3}>[ \t]?`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b97efeedb5af1283dd05c8eea4e1a7e9:search

```yaml
regex_id: b97efeedb5af1283dd05c8eea4e1a7e9
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/erc8004/resolver.js:71:13"
```

### Pattern

`^\/?a\/(\d+)\/(0x[0-9a-fA-F]{40})\/(\d+)\/?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bb4e3d2dfd68b1b2d94c331890135b9e:search

```yaml
regex_id: bb4e3d2dfd68b1b2d94c331890135b9e
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:398:10"
```

### Pattern

`^([`~]+|[^`~])(?:(?= {2,}\n)|(?=[a-zA-Z0-9.!#$%&'*+\/=?_`{\|}~-]+@)|[\s\S]*?(?:(?=[\\<!\[`*~_]|\b_|https?:\/\/|ftp:\/\/|www\.|$)|[^ ](?= {2,}\n)|[^a-zA-Z0-9.!#$%&'*+\/=?_`{\|}~-](?=[a-zA-Z0-9.!#$%&'*+\/=?_`{\|}~-]+@)))`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:be25dea1b95fb4674edad7c536f7d014:search

```yaml
regex_id: be25dea1b95fb4674edad7c536f7d014
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:1496:8"
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

## usage_mismatch:be98f72204aad2da0b6a493440b49a71:search

```yaml
regex_id: be98f72204aad2da0b6a493440b49a71
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:24486:52"
```

### Pattern

`^data\:image\/jpeg`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bed2b67fa78f2f622cf88c5a68331d57:search

```yaml
regex_id: bed2b67fa78f2f622cf88c5a68331d57
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:33465:9"
```

### Pattern

`^([a-z]+:|\/)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bf1b15b95c77babb60a740effbbe194f:search

```yaml
regex_id: bf1b15b95c77babb60a740effbbe194f
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:47542:492"
```

### Pattern

`^\/?a\/(\d+)\/(0x[0-9a-fA-F]{40})\/(\d+)\/?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bff27397d6610cb702babe77706c25c0:search

```yaml
regex_id: bff27397d6610cb702babe77706c25c0
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:20225:11"
```

### Pattern

`^[ \t]*#include +<([\w\d./]+)>`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c02bd6960f1a087ca78dd675656861c8:search

```yaml
regex_id: c02bd6960f1a087ca78dd675656861c8
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:47337:20"
```

### Pattern

`^agent:\/\/([^/]+)\/(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c098e802865a4a8408770dbd4594f7d6:search

```yaml
regex_id: c098e802865a4a8408770dbd4594f7d6
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/app.js:74:35"
```

### Pattern

`^(\/a\/.+?)\/embed\/?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c102cc4ca5cd2b374af029419ce55274:search

```yaml
regex_id: c102cc4ca5cd2b374af029419ce55274
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/editor/manifest-builder.js:1183:7"
```

### Pattern

`\.(glb|gltf)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c105a3b5b3ace8de858b93eabebdfdd2:search

```yaml
regex_id: c105a3b5b3ace8de858b93eabebdfdd2
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/permissions/[action].js:579:33"
```

### Pattern

`^0x[0-9a-fA-F]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c189170e031bdbcd7368ff9d8a64d96f:search

```yaml
regex_id: c189170e031bdbcd7368ff9d8a64d96f
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:114:11"
```

### Pattern

`^ {0,3}((?:-[\t ]*){3,}|(?:_[ \t]*){3,}|(?:\*[ \t]*){3,})(?:\n+|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c26121a92e9a8f474a1458054af15f79:search

```yaml
regex_id: c26121a92e9a8f474a1458054af15f79
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:53:28"
```

### Pattern

`^(\s+)(?:```)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c2b095a2fd8230512de04bc2726741ab:search

```yaml
regex_id: c2b095a2fd8230512de04bc2726741ab
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:39986:20"
```

### Pattern

`^([^\x5b]*)((\x5b\d*\x5d)*)(\x5b(\d*)\x5d)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c3062242d5b7e742eaea4a417eb5bf06:search

```yaml
regex_id: c3062242d5b7e742eaea4a417eb5bf06
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:35036:22"
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

## usage_mismatch:c344ec9914881548d4e8a596c62b7413:search

```yaml
regex_id: c344ec9914881548d4e8a596c62b7413
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/_lib/validate.js:75:9"
```

### Pattern

`^[a-f0-9]{64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c35a2b05d4e8c49af46aa76a980dbdeb:search

```yaml
regex_id: c35a2b05d4e8c49af46aa76a980dbdeb
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/extensions/container.ts:99:17"
```

### Pattern

`^:::(\n|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c3d3b6b41f20eeeffd4019932df1ea8d:search

```yaml
regex_id: c3d3b6b41f20eeeffd4019932df1ea8d
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:70:21"
```

### Pattern

`^\[[ xX]\] +`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c3ea870c61127b536b13e05c95670dc8:search

```yaml
regex_id: c3ea870c61127b536b13e05c95670dc8
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/artifact.js:21:1"
```

### Pattern

`^https:\/\/three\.ws$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c4739ac7d69908bb1d02c88f38fd68c5:search

```yaml
regex_id: c4739ac7d69908bb1d02c88f38fd68c5
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/editor/manifest-builder.js:1485:6"
```

### Pattern

`^# `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c7070099e8f1638abe262d1caff6a359:search

```yaml
regex_id: c7070099e8f1638abe262d1caff6a359
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/character-studio/public/ktx2/libktx.js:7849:25"
```

### Pattern

`^WebGL GLSL ES ([0-9]\.[0-9][0-9]?)(?:$| .*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c78536071f787e4dc9f2960f061abb54:search

```yaml
regex_id: c78536071f787e4dc9f2960f061abb54
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:47542:215"
```

### Pattern

`^onchain:(\d+):(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c80a5635c17dc68a36210695b4ce1ac5:search

```yaml
regex_id: c80a5635c17dc68a36210695b4ce1ac5
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/editor/manifest-builder.js:1550:6"
```

### Pattern

`^# `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c88ba31aa28e97bbe094c7c2bff86c14:search

```yaml
regex_id: c88ba31aa28e97bbe094c7c2bff86c14
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:48241:17"
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

## usage_mismatch:c9dedcc95a24f216dee158764ed0aef8:search

```yaml
regex_id: c9dedcc95a24f216dee158764ed0aef8
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:25923:26"
```

### Pattern

`^#([A-F0-9]{6})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ca35733e80cdfb31f022b8e3ce18a35b:search

```yaml
regex_id: ca35733e80cdfb31f022b8e3ce18a35b
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:54:20"
```

### Pattern

`^\s+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ca3e5ed026330bfcf0303406da2cdb2f:search

```yaml
regex_id: ca3e5ed026330bfcf0303406da2cdb2f
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/widgets/passport.js:139:6"
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

## usage_mismatch:cae407978a2a2e3c2ecd9228a541d19a:search

```yaml
regex_id: cae407978a2a2e3c2ecd9228a541d19a
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:112:18"
```

### Pattern

`^((?: {4}| {0,3}\t)[^\n]+(?:\n(?:[ \t]*(?:\n|$))*)?)+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cd03a77824379e9046e1b589a1cde917:search

```yaml
regex_id: cd03a77824379e9046e1b589a1cde917
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:279:27"
```

### Pattern

`^(?:\*+(?:((?!\*)punct)|[^\s*]))|^_+(?:((?!_)punct)|([^\s_]))`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cdf4747ffad6802e203218978451a063:search

```yaml
regex_id: cdf4747ffad6802e203218978451a063
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/app.js:110:31"
```

### Pattern

`^(\d+):(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cf259267dc115b265d8288db7b76bf5c:search

```yaml
regex_id: cf259267dc115b265d8288db7b76bf5c
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:33585:11"
```

### Pattern

`^---\n([\s\S]*?)\n---\n?([\s\S]*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d06627d1b99331351518a0fd592e0474:search

```yaml
regex_id: d06627d1b99331351518a0fd592e0474
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/app.js:86:34"
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

## usage_mismatch:d2483161e119c148b843455a474382fb:search

```yaml
regex_id: d2483161e119c148b843455a474382fb
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/tts/edge.js:39:16"
```

### Pattern

`^[+-]\d+%$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d2bcd06d975a1d5acc5e4ff23d8487c2:search

```yaml
regex_id: d2bcd06d975a1d5acc5e4ff23d8487c2
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/_lib/validate.js:27:8"
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

## usage_mismatch:d2cbe110becb3fadfded917cf9af8ca3:search

```yaml
regex_id: d2cbe110becb3fadfded917cf9af8ca3
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/erc8004/resolve-avatar.js:44:5"
```

### Pattern

`^agent:\/\/[^/]+\/\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d313d8f7067d4a48b5d25969fb6d276d:search

```yaml
regex_id: d313d8f7067d4a48b5d25969fb6d276d
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/app.js:88:15"
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

## usage_mismatch:d428e4132e2409bf35112d9ebc245680:search

```yaml
regex_id: d428e4132e2409bf35112d9ebc245680
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:247:14"
```

### Pattern

`^(.+?)\n {0,3}(=+|-+) *(?:\n+|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d5c995f8371b5501925023b8dcc664cc:search

```yaml
regex_id: d5c995f8371b5501925023b8dcc664cc
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/erc8004/resolve-avatar.js:300:6"
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

## usage_mismatch:d6825b61d8e2106fc267fdf32ca75b9d:search

```yaml
regex_id: d6825b61d8e2106fc267fdf32ca75b9d
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/contracts/lib/openzeppelin-contracts/scripts/release/format-changelog.js:12:27"
```

### Pattern

`^- (\[#.*?\]\(.*?\))?.*?! - (.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d7348bfeb48ccb1d7046adc7ef127456:search

```yaml
regex_id: d7348bfeb48ccb1d7046adc7ef127456
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/app.js:86:67"
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

## usage_mismatch:d769e019c04ba31d23559839b5061b00:search

```yaml
regex_id: d769e019c04ba31d23559839b5061b00
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:76:21"
```

### Pattern

`^ *-+: *$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d8480898272871ce649da954f4da0d22:search

```yaml
regex_id: d8480898272871ce649da954f4da0d22
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:79:15"
```

### Pattern

`^<a `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:da6f737a47f481ea786555a227aa991a:search

```yaml
regex_id: da6f737a47f481ea786555a227aa991a
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/erc8004/resolve-avatar.js:353:29"
```

### Pattern

`^agent:\/\/([^/]+)\/(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:daea3028f3c33ce2c5977925ee7db303:search

```yaml
regex_id: daea3028f3c33ce2c5977925ee7db303
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/erc8004/resolver.js:53:17"
```

### Pattern

`^eip155:(\d+):(0x[0-9a-fA-F]{40}):(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:db2c94fcba2fbd5e078270cf926c428d:search

```yaml
regex_id: db2c94fcba2fbd5e078270cf926c428d
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/erc8004/resolver.js:65:13"
```

### Pattern

`^agent:\/\/(\d+)\/(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dc95ecc7d5e8e6669e0771ea37f53bf3:search

```yaml
regex_id: dc95ecc7d5e8e6669e0771ea37f53bf3
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:44815:15"
```

### Pattern

`^[0-9.]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:df5d9978b8d2691d634a233d3835075a:search

```yaml
regex_id: df5d9978b8d2691d634a233d3835075a
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:44177:22"
```

### Pattern

`^0x(e3010170|e5010172)(([0-9a-f][0-9a-f])([0-9a-f][0-9a-f])([0-9a-f]*))$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e05bfdc53ceb38034e68aeeef1d17c19:search

```yaml
regex_id: e05bfdc53ceb38034e68aeeef1d17c19
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/erc8004/resolve-avatar.js:47:5"
```

### Pattern

`^\d{1,10}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e23791f29abb84898559d52e2c44def4:search

```yaml
regex_id: e23791f29abb84898559d52e2c44def4
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:82:21"
```

### Pattern

`^<\/(pre|code|kbd|script)(\s|>)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e2fb87d84e833716a590e935039b33bf:search

```yaml
regex_id: e2fb87d84e833716a590e935039b33bf
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/auth/siwe/[action].js:21:29"
```

### Pattern

`^0x[a-fA-F0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e30673218f5ef58dec2485f30ce52590:search

```yaml
regex_id: e30673218f5ef58dec2485f30ce52590
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:44824:28"
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

## usage_mismatch:e349e8833203f13814f7624c31fd17f7:search

```yaml
regex_id: e349e8833203f13814f7624c31fd17f7
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/agent-oembed.js:112:37"
```

### Pattern

`^\/a\/(\d+)\/(\d+)\/?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e5355e4b94e410c5a9323eda1d7e8527:search

```yaml
regex_id: e5355e4b94e410c5a9323eda1d7e8527
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:12535:176"
```

### Pattern

`^data:.*,.*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e57fc75757b388a52dbb5a9dcfa58f27:search

```yaml
regex_id: e57fc75757b388a52dbb5a9dcfa58f27
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:40231:20"
```

### Pattern

`^bytes(\d*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:e6143ac75228d679a4f8d71a6d01759b:url

```yaml
regex_id: e6143ac75228d679a4f8d71a6d01759b
schema_version: "1"
kind: intent_mismatch
corpus: three-ui
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/vite.config.js:260:18"
```

### Pattern

`^https:\/\/fonts\.googleapis\.com\/.*`

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

## usage_mismatch:e6143ac75228d679a4f8d71a6d01759b:search

```yaml
regex_id: e6143ac75228d679a4f8d71a6d01759b
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/vite.config.js:260:18"
```

### Pattern

`^https:\/\/fonts\.googleapis\.com\/.*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e6e7eb18b275e201b937a4652fcb5392:search

```yaml
regex_id: e6e7eb18b275e201b937a4652fcb5392
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/marked-katex-extension/index.js:3:19"
```

### Pattern

`^(\${1,2})(?!\$)((?:\\.|[^\\\n])*?(?:\\.|[^\\\n$]))\1(?=[\s?!.,:？！。，：]|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e872bb1c7a3413424f5e9ace143b1248:search

```yaml
regex_id: e872bb1c7a3413424f5e9ace143b1248
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/editor/publish.js:219:15"
```

### Pattern

`^[a-z0-9]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e89c89ed9f4d6a3ed63d6c4668b44926:search

```yaml
regex_id: e89c89ed9f4d6a3ed63d6c4668b44926
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:40451:22"
```

### Pattern

`^(.*)\[([0-9]*)\]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ea2220e4e7744fe14380424ec1eece81:search

```yaml
regex_id: ea2220e4e7744fe14380424ec1eece81
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/widgets/[id]/[action].js:276:5"
```

### Pattern

`^(hi|hello|hey|sup|yo)\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ebe9c0057b0d6981f480bda764523dca:search

```yaml
regex_id: ebe9c0057b0d6981f480bda764523dca
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:28420:33"
```

### Pattern

`[\t\n\r\f]| {2,}|^ | $`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ec2a409a0c48d58c107e77f0f3690551:search

```yaml
regex_id: ec2a409a0c48d58c107e77f0f3690551
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:44057:2"
```

### Pattern

`^(data):(.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ec6869639d82e0dedb7e1775dda0341b:search

```yaml
regex_id: ec6869639d82e0dedb7e1775dda0341b
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:74:21"
```

### Pattern

`^\||\| *$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ed038beaf600efb2c445617294df33e0:search

```yaml
regex_id: ed038beaf600efb2c445617294df33e0
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/vite.config.js:147:27"
```

### Pattern

`^\/agent\/[^/]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ed502e9d4b7aef555ecc2e4179642a5c:search

```yaml
regex_id: ed502e9d4b7aef555ecc2e4179642a5c
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/artifact.js:19:1"
```

### Pattern

`^https:\/\/storage\.googleapis\.com$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ee0b5de88fa4800186f4dfad55a273c3:search

```yaml
regex_id: ee0b5de88fa4800186f4dfad55a273c3
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:245:13"
```

### Pattern

`^(#{1,6})(.*)(?:\n+|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:eecb465739ee46131a1aff467c0fe6ce:search

```yaml
regex_id: eecb465739ee46131a1aff467c0fe6ce
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/erc8004/resolve-avatar.js:44:5"
```

### Pattern

`^agent:\/\/[^/]+\/\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ef0cea34f8c000764a97c1c6f7126111:search

```yaml
regex_id: ef0cea34f8c000764a97c1c6f7126111
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:84:21"
```

### Pattern

`>$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f0def32a61c4336886b92ddc63d2930c:search

```yaml
regex_id: f0def32a61c4336886b92ddc63d2930c
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/permissions/[action].js:918:26"
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

## usage_mismatch:f3e9c45f681317f884c70f0f6bee7ea5:search

```yaml
regex_id: f3e9c45f681317f884c70f0f6bee7ea5
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/app.js:93:16"
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

## usage_mismatch:f4df452e36f079ea94e90b1a1ee332db:search

```yaml
regex_id: f4df452e36f079ea94e90b1a1ee332db
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/src/erc8004/resolve-avatar.js:300:6"
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

## usage_mismatch:f92ca073a026e50e1f0b7cad225fe58a:search

```yaml
regex_id: f92ca073a026e50e1f0b7cad225fe58a
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/app.js:86:15"
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

## usage_mismatch:f9452b943d52872a3cbf7afa9d29fe4b:search

```yaml
regex_id: f9452b943d52872a3cbf7afa9d29fe4b
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:111:16"
```

### Pattern

`^(?:[ \t]*(?:\n|$))+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f94760aeb15893880e0c3356c1e1b0d9:search

```yaml
regex_id: f94760aeb15893880e0c3356c1e1b0d9
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:28751:11"
```

### Pattern

`^[A-Za-z][A-Za-z0-9+.-]*:$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fa62108bfc3c50bef548dd5389b172c5:search

```yaml
regex_id: fa62108bfc3c50bef548dd5389b172c5
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/rider/webpack.config.js:93:14"
```

### Pattern

`\.css$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fb83789a6142c5d6c41fa9c46eb019bb:search

```yaml
regex_id: fb83789a6142c5d6c41fa9c46eb019bb
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:51:22"
```

### Pattern

`^(?: {1,4}| {0,3}\t)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fbd91af16f54a8c40c822fcf13a99935:search

```yaml
regex_id: fbd91af16f54a8c40c822fcf13a99935
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/_lib/validate.js:13:8"
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

## usage_mismatch:fc0723fa135d53db22168f41fe0a4ac4:search

```yaml
regex_id: fc0723fa135d53db22168f41fe0a4ac4
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:47541:18"
```

### Pattern

`^eip155:(\d+):(0x[0-9a-fA-F]{40}):(\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fd0dfa4a0357ca49a683a3173c4dcc3a:search

```yaml
regex_id: fd0dfa4a0357ca49a683a3173c4dcc3a
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/editor/manifest-builder.js:1481:6"
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

## usage_mismatch:fd9e102792a8ffcf6e238edf378e05cf:search

```yaml
regex_id: fd9e102792a8ffcf6e238edf378e05cf
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/chat/src/svelte-marked/markdown/marked.esm.js:75:23"
```

### Pattern

`\n[ \t]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fdb944d7a80f09a61722a1d37b0c3310:search

```yaml
regex_id: fdb944d7a80f09a61722a1d37b0c3310
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/api/auth/siwe/[action].js:115:52"
```

### Pattern

`^localhost(:\d+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fe114b5073f1de4b83c42cf9e22c7b15:search

```yaml
regex_id: fe114b5073f1de4b83c42cf9e22c7b15
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/src/erc8004/resolve-avatar.js:46:5"
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

## usage_mismatch:fed9beeab7d7a443c82d41bd30d507de:search

```yaml
regex_id: fed9beeab7d7a443c82d41bd30d507de
schema_version: "1"
kind: usage_mismatch
corpus: three-ui
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/three-ui/rules/publish/agent-3d.js:42034:209"
```

### Pattern

`^bytes`

### Context

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
corpus: three-ui
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
corpus: three-ui
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
corpus: three-ui
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
corpus: three-ui
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

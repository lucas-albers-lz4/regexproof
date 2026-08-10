---
schema_version: "1"
corpus: lonkero
findings: 69
---

# lonkero batch findings

## usage_mismatch:030ac90357116da1f180772e3fbbe73b:search

```yaml
regex_id: 030ac90357116da1f180772e3fbbe73b
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1944:8"
```

### Pattern

`\.legacy\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0c55ab2325782a3fe5e10bb13cc3a113:search

```yaml
regex_id: 0c55ab2325782a3fe5e10bb13cc3a113
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/cms-scanner.js:80:17"
```

### Pattern

`^[A-Z_]+=.+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0c85d50ffaac62d945d256e170e1204f:search

```yaml
regex_id: 0c85d50ffaac62d945d256e170e1204f
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:864:73"
```

### Pattern

`^\/webpack|^\/node_modules`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0e4c2300f8b78cdc41e471d8c312e357:search

```yaml
regex_id: 0e4c2300f8b78cdc41e471d8c312e357
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/xss-scanner.js:452:8"
```

### Pattern

`on\w+\s*=\s*["']?[^"']*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1147434cdfa0e237d0a0bad30972de1f:search

```yaml
regex_id: 1147434cdfa0e237d0a0bad30972de1f
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1928:28"
```

### Pattern

`\.(js|mjs|cjs|css|scss|less|png|jpg|jpeg|gif|svg|ico|webp|avif|woff|woff2|ttf|eot|otf|mp4|webm|mp3|wav|ogg|pdf|map|json|xml|txt|md|yml|yaml|toml)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:13f23f31dbca1d0c8633e8dfd6024598:search

```yaml
regex_id: 13f23f31dbca1d0c8633e8dfd6024598
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1836:26"
```

### Pattern

`^_ga`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:149510b2bae00e9578d5d02c4d523e28:search

```yaml
regex_id: 149510b2bae00e9578d5d02c4d523e28
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:670:12"
```

### Pattern

`^(src|href|class|style|id|type|rel|charset|lang|xmlns|content|name|alt|title|action|method|encoding|target|value|placeholder|pattern|icon|image|img|logo|font|css|svg|data|d|viewBox|fill|stroke)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1a76f729bd7ef880b29e9457092c971d:search

```yaml
regex_id: 1a76f729bd7ef880b29e9457092c971d
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/background.js:254:121"
```

### Pattern

`^[A-Z0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1d40670e73f4cfd8cda9b635e8372a27:search

```yaml
regex_id: 1d40670e73f4cfd8cda9b635e8372a27
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1870:32"
```

### Pattern

`^(auth|jwt|access|refresh|api|bearer)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:219f6d66f8d2434bbdb6ffd0032bd214:search

```yaml
regex_id: 219f6d66f8d2434bbdb6ffd0032bd214
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1836:35"
```

### Pattern

`^_gid`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:27e6048a22139cd5fe19cf10f653952e:search

```yaml
regex_id: 27e6048a22139cd5fe19cf10f653952e
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:3167:13"
```

### Pattern

`^[A-Z_]+=|DB_|API_KEY|SECRET|PASSWORD`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2935ac9909baf8add734754dc8e1ebd5:search

```yaml
regex_id: 2935ac9909baf8add734754dc8e1ebd5
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1538:40"
```

### Pattern

`^\$ACTION_ID_([a-f0-9]{32,40})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2c49ed9a76755cc13aa426fd1cf93c0b:search

```yaml
regex_id: 2c49ed9a76755cc13aa426fd1cf93c0b
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1401:33"
```

### Pattern

`^\d+:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:31649b0bd99f9a700a0ad45fb8242346:search

```yaml
regex_id: 31649b0bd99f9a700a0ad45fb8242346
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/graphql-fuzzer.js:196:12"
```

### Pattern

`^172\.(1[6-9]|2\d|3[01])\.\d+\.\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:37db74a517d5e5a7070f450794a9a2e7:search

```yaml
regex_id: 37db74a517d5e5a7070f450794a9a2e7
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/cms-scanner.js:1434:10"
```

### Pattern

`^[^\x00-\x08\x0e-\x1f]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3b0bd1e96daa347af8bdb083b484c1ca:search

```yaml
regex_id: 3b0bd1e96daa347af8bdb083b484c1ca
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1837:25"
```

### Pattern

`^_fbp`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3fcbc05c6204eee5bb9b982ce7414558:search

```yaml
regex_id: 3fcbc05c6204eee5bb9b982ce7414558
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/cms-scanner.js:84:17"
```

### Pattern

`^<\?xml|<[\w-]+\s*xmlns`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:412577b3d97536019ca87ee1e24ecda7:search

```yaml
regex_id: 412577b3d97536019ca87ee1e24ecda7
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:3168:19"
```

### Pattern

`^[A-Z_]+=|DB_|API_KEY|SECRET|PASSWORD`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:418ebdcc002b23e8a71d7d0134c73d9c:search

```yaml
regex_id: 418ebdcc002b23e8a71d7d0134c73d9c
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1828:14"
```

### Pattern

`^sp_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:41a27cbc5d07d1ce20dc53d0de299b12:search

```yaml
regex_id: 41a27cbc5d07d1ce20dc53d0de299b12
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1772:30"
```

### Pattern

`^\d+:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:45df2cad12f27a7efb078a6dccd02425:search

```yaml
regex_id: 45df2cad12f27a7efb078a6dccd02425
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:967:18"
```

### Pattern

`^\/_next\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:47f8682fbe5fe97c7a3461caf50116ca:search

```yaml
regex_id: 47f8682fbe5fe97c7a3461caf50116ca
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/graphql-fuzzer.js:376:17"
```

### Pattern

`^\s*subscription\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4bab3d7c652f25de44874147259c8648:search

```yaml
regex_id: 4bab3d7c652f25de44874147259c8648
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/dom-hooks.js:120:9"
```

### Pattern

`^DYO\.|^Kameleoon|^VWO\.|^Optimizely|^AB\.|^_vwo_|^convert\.|^Qubit`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4d7d7882633956ec4e44d48e58f0939b:search

```yaml
regex_id: 4d7d7882633956ec4e44d48e58f0939b
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1844:46"
```

### Pattern

`^experiment`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:507debfd331411533f225bdc732ff2d0:search

```yaml
regex_id: 507debfd331411533f225bdc732ff2d0
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/background.js:623:45"
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

## usage_mismatch:56a9c4d9dffa4098edfac7ae912c0c03:search

```yaml
regex_id: 56a9c4d9dffa4098edfac7ae912c0c03
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/dom-hooks.js:115:26"
```

### Pattern

`^\(function\(\)\{return\s*(window\.\w+\?|Math\.|"|\d|sessionStorage|localStorage|typeof\s)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5784174d9fd71eb8bb926b5180b6f55b:search

```yaml
regex_id: 5784174d9fd71eb8bb926b5180b6f55b
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:828:32"
```

### Pattern

`\.(js|css|png|svg)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5be4a6e839bd940fb535410dc72840a5:search

```yaml
regex_id: 5be4a6e839bd940fb535410dc72840a5
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1200:58"
```

### Pattern

`^\s*[\[{]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5e5a3f42a9181b3d6f2e9c82ed832a26:search

```yaml
regex_id: 5e5a3f42a9181b3d6f2e9c82ed832a26
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:3507:12"
```

### Pattern

`^\/\/[\w.-]+\.(com|net|org|io|fi|de|uk|se|no|eu|co)\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5fdb1b96a3ead482f33e1300cb9adbb9:search

```yaml
regex_id: 5fdb1b96a3ead482f33e1300cb9adbb9
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1842:4"
```

### Pattern

`^_gcl`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6354d749028d104449477680842e3099:search

```yaml
regex_id: 6354d749028d104449477680842e3099
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:673:12"
```

### Pattern

`^\/webpack|^\/node_modules`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:67cfab6d3c48f7984e21b3d2bce5f925:search

```yaml
regex_id: 67cfab6d3c48f7984e21b3d2bce5f925
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/xss-scanner.js:1187:32"
```

### Pattern

`^\s*alert`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6e850f9705b0e077f1ce39b27d9a798e:search

```yaml
regex_id: 6e850f9705b0e077f1ce39b27d9a798e
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/popup.js:77:123"
```

### Pattern

`^[A-Z0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:71f7bb159dcb08843bb0b8640c661e65:search

```yaml
regex_id: 71f7bb159dcb08843bb0b8640c661e65
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/cms-scanner.js:2061:10"
```

### Pattern

`^(source|gem|package)\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:72301b3f2c8966792e7d44c3233a19e8:search

```yaml
regex_id: 72301b3f2c8966792e7d44c3233a19e8
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:807:34"
```

### Pattern

`\.(js|css|png|svg)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:78621e480bfe5b145b1a31ab29cafefc:search

```yaml
regex_id: 78621e480bfe5b145b1a31ab29cafefc
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1542:42"
```

### Pattern

`^\$ACTION_[:_](\d+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7a6891645093ffd9511fea3c35912f00:search

```yaml
regex_id: 7a6891645093ffd9511fea3c35912f00
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:3509:12"
```

### Pattern

`^\/\/[a-z][\w.-]*\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7f802fb11bb005dc7b2f4ba38d2ecace:search

```yaml
regex_id: 7f802fb11bb005dc7b2f4ba38d2ecace
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:215:37"
```

### Pattern

`^[a-z_]+=(?:yes|no|true|false);?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:80e504e767f471e17f48e3ce849d0a5f:search

```yaml
regex_id: 80e504e767f471e17f48e3ce849d0a5f
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:3481:10"
```

### Pattern

`^\[if |^google|^gtm|^fb-|^ko |public folder|PUBLIC_URL|manifest\.json|favicon`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8251b7d341f9e06eaabebdf723940a09:search

```yaml
regex_id: 8251b7d341f9e06eaabebdf723940a09
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1871:31"
```

### Pattern

`(_token|_jwt|_auth|_key)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:89b76f783a81abd33442f8d21e54695b:search

```yaml
regex_id: 89b76f783a81abd33442f8d21e54695b
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/dom-hooks.js:117:9"
```

### Pattern

`^\(function\(\)\{(var\s+\w+=)?.*Math\.(random|floor|ceil|round|abs)\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8b8eb3f8c0bca9299522ce10f48af37f:search

```yaml
regex_id: 8b8eb3f8c0bca9299522ce10f48af37f
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/graphql-fuzzer.js:194:12"
```

### Pattern

`^192\.168\.\d+\.\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8bc7b55b807f00545cab7082800f2239:search

```yaml
regex_id: 8bc7b55b807f00545cab7082800f2239
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:864:13"
```

### Pattern

`\.(js|css|png|jpg|svg|woff|ico|map|json)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:99f82e5b04b710c4d2fd4861dfc0278e:search

```yaml
regex_id: 99f82e5b04b710c4d2fd4861dfc0278e
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/dom-hooks.js:116:9"
```

### Pattern

`^\(function\(\)\{return\s*typeof\s+window\.\w+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a231e48a02a5c8b98ac7680d1178dd57:search

```yaml
regex_id: a231e48a02a5c8b98ac7680d1178dd57
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:966:15"
```

### Pattern

`\.(js|css|png|jpg|svg|woff|ico|map|json)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a23b99c28d11a33abeab3b6a92bbd31f:search

```yaml
regex_id: a23b99c28d11a33abeab3b6a92bbd31f
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:2048:31"
```

### Pattern

`\.[a-z]{2,5}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a3a741487e82a1d6e0a40c4d645110c6:search

```yaml
regex_id: a3a741487e82a1d6e0a40c4d645110c6
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:671:12"
```

### Pattern

`\.(js|css|png|jpg|jpeg|gif|svg|woff|woff2|ttf|eot|ico|map|json|xml|txt|html|htm)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a3d7fc49dfae41db710d2a658b2399d9:search

```yaml
regex_id: a3d7fc49dfae41db710d2a658b2399d9
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1941:8"
```

### Pattern

`^\/(static|assets|public|dist|build|vendor|lib|fonts|images|img|media|node_modules)\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b01cebfad6f2d8b0ae5dce1a501b93d6:search

```yaml
regex_id: b01cebfad6f2d8b0ae5dce1a501b93d6
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1321:97"
```

### Pattern

`^\s*[\[{]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b4e424fa481c0935a68fd268aaa2a1d7:search

```yaml
regex_id: b4e424fa481c0935a68fd268aaa2a1d7
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1828:4"
```

### Pattern

`^_sp_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b7a055cdcf826d77b540817cd6da3ddb:search

```yaml
regex_id: b7a055cdcf826d77b540817cd6da3ddb
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1611:38"
```

### Pattern

`^\d+:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b82eef59007ae98205d81dfc13b1cf9e:search

```yaml
regex_id: b82eef59007ae98205d81dfc13b1cf9e
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/graphql-fuzzer.js:374:10"
```

### Pattern

`^\s*mutation\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b9b6934dede3857a9bba78d338eb5bff:search

```yaml
regex_id: b9b6934dede3857a9bba78d338eb5bff
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:675:12"
```

### Pattern

`^\/_next\/static`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b9c9da1a6d44248442a0faa690db9c7c:search

```yaml
regex_id: b9c9da1a6d44248442a0faa690db9c7c
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1896:29"
```

### Pattern

`^eyJ`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bda6bef2c22de20a11c9e7b453216f7a:search

```yaml
regex_id: bda6bef2c22de20a11c9e7b453216f7a
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1943:8"
```

### Pattern

`polyfill.*\.js$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c131c3e5ca5052a0bc18229fab917c97:search

```yaml
regex_id: c131c3e5ca5052a0bc18229fab917c97
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/cms-scanner.js:2152:38"
```

### Pattern

`^\s*#?\d+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c5f11218979a6980d618880345afef38:search

```yaml
regex_id: c5f11218979a6980d618880345afef38
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1897:28"
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

## usage_mismatch:c9ef98ef2b0d6f0c7a769028f5e132ba:search

```yaml
regex_id: c9ef98ef2b0d6f0c7a769028f5e132ba
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:691:35"
```

### Pattern

`\.(js|css|png|jpg|svg|woff|ico|map)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d2102f54739d3786e5385c1b734c2dfc:search

```yaml
regex_id: d2102f54739d3786e5385c1b734c2dfc
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:2047:25"
```

### Pattern

`\.(html?|php|aspx?|jsp)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ded2eac729b9a399aca4cf4ca14c2fd8:search

```yaml
regex_id: ded2eac729b9a399aca4cf4ca14c2fd8
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1840:20"
```

### Pattern

`^fp_`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e09c8f4cd3e12f27741c9752d300b3cb:search

```yaml
regex_id: e09c8f4cd3e12f27741c9752d300b3cb
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/background.js:112:31"
```

### Pattern

`^[A-Z0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e2d1d70a119087a5f688924e7d4b0e23:search

```yaml
regex_id: e2d1d70a119087a5f688924e7d4b0e23
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/cms-scanner.js:192:22"
```

### Pattern

`\.(html?|php|asp|aspx|jsp)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e72fdf53df97a2c9bdedbfca38976705:search

```yaml
regex_id: e72fdf53df97a2c9bdedbfca38976705
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1540:41"
```

### Pattern

`^\$ACTION_REF_([a-f0-9]{32,40})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f9fa68e491c069dbd9f6fc268047db7e:search

```yaml
regex_id: f9fa68e491c069dbd9f6fc268047db7e
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/content.js:1898:28"
```

### Pattern

`^[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fcabd371eca50ada00f34e870d9fc286:search

```yaml
regex_id: fcabd371eca50ada00f34e870d9fc286
schema_version: "1"
kind: usage_mismatch
corpus: lonkero
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lonkero/rules/browser-assist-extension/graphql-fuzzer.js:195:12"
```

### Pattern

`^10\.\d+\.\d+\.\d+$`

### Context

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
corpus: lonkero
shape: 1
result: planned
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

None

## property:inventory:rc-shape2-missing-keyword:rc-shape2-missing-keyword

```yaml
regex_id: "inventory:rc-shape2-missing-keyword"
schema_version: "1"
kind: property
corpus: lonkero
shape: 2
result: planned
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

None

## property:inventory:rc-shape3-capture-truncation:rc-shape3-capture-truncation

```yaml
regex_id: "inventory:rc-shape3-capture-truncation"
schema_version: "1"
kind: property
corpus: lonkero
shape: 3
result: planned
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

None

## property:inventory:rc-shape4-escape-image:rc-shape4-escape-image

```yaml
regex_id: "inventory:rc-shape4-escape-image"
schema_version: "1"
kind: property
corpus: lonkero
shape: 4
result: planned
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

None

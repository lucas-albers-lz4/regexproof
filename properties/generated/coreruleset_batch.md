---
schema_version: "1"
corpus: coreruleset
findings: 106
---

# coreruleset batch findings

## usage_mismatch:074291341618248dc4e9ba8d9df0ac29:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:610:0`
- ground_truth_status: `None`
- disclosure: `private_first`

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

## usage_mismatch:0b4ddc24d5845c4243fbb3ab26c5411d:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:1418:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^bytes=(?:(?:\d+)?-(?:\d+)?\s*,?\s*){6}`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:156e25364871ae04cca15ffa9c8f035a:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:93:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^_pk_ref`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1e7fd3f5f4b927645e93c2b113f91040:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-931-APPLICATION-ATTACK-RFI.conf:94:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^(?i:file|ftps?|https?).*?\?+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1fb7be6eba1a0b8ba8cf4a8ce9ca3df3:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-932-APPLICATION-ATTACK-RCE.conf:737:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^\(\s*\)\s+\{`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:272e3d0c0531d68d9d0023670e490ab2:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:1155:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`\.[^.~]+~(?:/.*|)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:29990488e209777c49eb3a4ec2c25cc5:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:96:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^_pk_ref`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2dcd558f9ae33898812ae717efc88e88:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-942-APPLICATION-ATTACK-SQLI.conf:235:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^(?:json\.)?(?:429496729[56]|2(?:14748364[78]|.22507385850720(?:07|11)e-308)|-(?:214748364[89]|0000023456)|00000(?:12345|23456)|1e309)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2e237551a994a7d096f61f3d65997cd0:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-932-APPLICATION-ATTACK-RCE.conf:1240:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^[^\.]*?(?:['\*\?\x5c`][^\n/]+/|/[^/]+?['\*\?\x5c`]|\$[!#\$\(\*\-0-9\?-\[_a-\{])`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:32e8c2a4d1def98567057f221c978666:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:1461:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^bytes=(?:(?:\d+)?-(?:\d+)?\s*,?\s*){63}`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:352b96d4af29025b3decd1f809865c49:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:78:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^pbjs-\w+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:371b9c6243d6964f97523bd662ddb83c:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-931-APPLICATION-ATTACK-RFI.conf:47:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^(f(?:ile|tps?)|https?|ssh)://(?:\[?[0-9a-f]+:[0-:a-f]+\]?|[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:38fe8f38d021147a9c2d3030be326204:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-921-PROTOCOL-ATTACK.conf:415:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^[^\s\x0b,;]+[\s\x0b,;].*?\b(?:((?:tex|multipar)t|application)|((?:audi|vide)o|image|cs[sv]|(?:vn|relate)d|p(?:df|lain)|json|(?:soa|cs)p|x(?:ml|-www-form-urlencoded)|form-data|x-amf|(?:octe|repor)t|stream)|([\+/]))\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3b3f2dfac21262f17fec91a9cba8ec8f:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-943-APPLICATION-ATTACK-SESSION-FIXATION.conf:96:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^(?:json\.)?(?:j(?:se(?:ssionid|rvsession)|wsession)|(?:asp(?:\.net_)?session|session[\-_]?)id|phpsessi(?:on|d)|(?:weblogic|laravel_)session|_(?:session_id|flask_session)|c(?:f(?:s?id|token)|onnect\.sid))$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3c7136019bbc675652ef5b97689b41e4:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:1876:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^bytes=(?:(?:\d+)?-(?:\d+)?\s*,?\s*){6}`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3daf1e92d7dec9c51c5f9ed8b5af6a68:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-942-APPLICATION-ATTACK-SQLI.conf:1544:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^(?:and|or)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3e364adc16a1379c1fdcab6e29d66cad:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/RESPONSE-955-WEB-SHELLS.conf:314:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^<title>PHP Web Shell</title>\r\n<html>\r\n<body>\r\n    <!-- Replaces command with Base64-encoded Data -->`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3ed0416bdb65ab61bcfe47ab20a83e36:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:77:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^pbjs-\w+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4432eb00f69f1e82b3063bc2cbb873fa:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:79:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^pbjs-\w+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4482183add03a5824ab8273b6c55e2b4:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:27:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^_ga(?:_\w+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:46c17ea8663b4e26812900481da326bf:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:100:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^_pk_ref`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:472b2cd1f873b822accaef3c06f1b3b0:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:569:0`
- ground_truth_status: `None`
- disclosure: `private_first`

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

## usage_mismatch:4de1c7f6e650cd742926d3c4997fd473:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/RESPONSE-955-WEB-SHELLS.conf:74:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^<html><head><meta http-equiv='Content-Type' content='text/html; charset=(?:Windows-1251|UTF-8)?'><title>.*?(?: -)? W[Ss][Oo] [0-9.]+</title>`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:522cb71c6f5fbf27d194d26ebcdddd8c:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:80:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^pbjs-\w+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:588671500ad6d4745b5c2a98f74543dc:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-922-MULTIPART-ATTACK.conf:73:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^content-type\s*:\s*(.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5913ee2ec8898c4839b7aafa90fca050:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:29:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^_ga(?:_\w+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:599bd7c963b4557f29cc1b2c6bcc89d1:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:30:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^_ga(?:_\w+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:59cce351d2b6fe714b6aa1d63828abe4:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:101:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^_pk_ref`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5a2ac3b738e63465f30515a8dbb85038:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:83:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^pbjs-\w+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5a626fa3c127ed861d7a6dca33b1f5cd:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-932-APPLICATION-ATTACK-RCE.conf:2143:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`(?:^(?:json\.)?|b[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?u[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?s[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?y[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?b[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?o[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?x|(?:c[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?o[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?m[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?m[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?a[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?n[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?d|e[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?(?:n[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?v|v[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?a[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?l)|w[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?a[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?t[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?c[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?h)[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?[\s\x0b&\),<>\|].*|[ls][\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?t[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?r[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?a[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?c[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?e|n[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?o[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?h[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?u[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?p|t[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?i[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?m[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?e[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?(?:[\s\x0b&\),<>\|].*|o[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?u[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?t)|[\n\r;=`\{]|\|\|?|&&?|\$(?:\(\(?|[\[\{])|<(?:\(|<<)|>\(|\([\s\x0b]*\))[\s\x0b]*(?:[!\$\(\{][\s\x0b]*|(?:[0-9A-Z_a-z]+=[^\s\x0b]+|\$[0-9A-Z_a-z]+)[\s\x0b]+)*[\s\x0b]*[\"']*(?:[\"'-\+\--9\?A-\]_a-z\|]+/)?[\"'\x5c]*(?:(?:aptitud|unam)e|d(?:f|ir|mesg)|env|h(?:istory|ostname|top)|i(?:d|ostat)|l(?:ast|s)|mysql(?:[^\s\x0b]{1,10}\b)?|p(?:s(?:ql)?|wd)|(?:reboo|vmsta)t|s(?:(?:cree|hutdow)n|et|u)|top|w(?:ho(?:ami|is)?)?)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5aa81cbca1e622016961312a3ce455c9:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:84:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^pbjs-\w+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5b86db5b80a8e56c84ca546312648232:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:95:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^_pk_ref`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5bdd4eaf48ddce540a6c4b655a6f0be6:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:108:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^(?:&(?:(?:[acegilnorsuz]acut|[aeiou]grav|[aino]tild)e|[c-elnr-tz]caron|(?:[cgklnr-t]cedi|[aeiouy]um)l|[aceg-josuwy]circ|[au]ring|a(?:mp|pos)|nbsp|oslash);|[^\"';=\x5c])*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5ca0e9cbd91d0cbe225ed903cea98573:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:199:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^(?:GET|HEAD)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5e8543a242e0243b44ef4c6fa4142636:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:670:0`
- ground_truth_status: `None`
- disclosure: `private_first`

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

## usage_mismatch:5ee4b6e28a0a16e3a24b523ee6adb1f4:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-943-APPLICATION-ATTACK-SESSION-FIXATION.conf:83:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^(?:ht|f)tps?://(.*?)/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5ff6ec1d690eda40066530ff5f8a3f18:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-905-COMMON-EXCEPTIONS.conf:54:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^(?:GET /|OPTIONS \*) HTTP/[12]\.[01]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6401b41867911932193681c5eef262e5:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/RESPONSE-955-WEB-SHELLS.conf:416:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^ <html>\n\n<head>\n\n<title>g00nshell v[0-9.]+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:66332d85a6b49adfc35876412ac95ce3:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-921-PROTOCOL-ATTACK.conf:258:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^[^!&\(\):<>\|~]*\)[\s\x0b]*(?:\((?:[^!&\(\),<->\|~]+[<>~]?=|[\s\x0b]*[!&\|][\s\x0b]*[\(\)]?[\s\x0b]*)|\)[\s\x0b]*\([\s\x0b]*[!&\|][\s\x0b]*|[!&\|][\s\x0b]*\([^!&\(\),<->\|~]+[<>~]?=[^!&\(\):<>\|~]*)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6b30c72210e0276d6fe893f9ba0cc89b:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/RESPONSE-950-DATA-LEAKAGES.conf:87:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^#\!\s?/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6c05e57cae2b6c06cb1f0e9bc280cd02:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-932-APPLICATION-ATTACK-RCE.conf:1197:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^[^#]+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6ccd15fbab1c08949249b9a11a8d2ab8:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:961:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^[\w/.+*-]+(?:\s?;\s*(?:action|boundary|charset|component|start(?:-info)?|type|version)\s?=\s?['\"\w.()+,/:=?<>@#*-]+)*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6db1b37191130cebb0613babf1703ebb:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-933-APPLICATION-ATTACK-PHP.conf:860:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`.*\.ph(?:p\d*|tml|ar|ps|t|pt)\..*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6f200650ea1b61930f51c2b7097276d9:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-942-APPLICATION-ATTACK-SQLI.conf:1395:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^(?:ey[\-0-9A-Z_a-z]+\.ey[\-0-9A-Z_a-z]+\.)?[\-0-9A-Z_a-z]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7015710b5f31a3d7b3684dbd39025a25:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-932-APPLICATION-ATTACK-RCE.conf:1217:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^[^\.]+\.[^;\?]+[;\?](.*(['\*\?\x5c`][^\n/]+/|/[^/]+?['\*\?\x5c`]|\$[!#\$\(\*\-0-9\?-\[_a-\{]))`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:72f84da5e7db436c11a71a0f5c5b868c:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-943-APPLICATION-ATTACK-SESSION-FIXATION.conf:63:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^(?:json\.)?(?:j(?:se(?:ssionid|rvsession)|wsession)|(?:asp(?:\.net_)?session|zend_session_)id|p(?:hpsessi(?:on|d)|lay_session)|(?:(?:w(?:eblogic|l)|rack\.|laravel_)sessio|(?:next-auth\.session-|meteor_login_)toke)n|s(?:(?:ession[\-_]?|ails\.s)id|hiny-token)|_(?:session_id|(?:(?:flask|rails)_sessio|_(?:secure|host)-next-auth\.session-toke)n)|c(?:f(?:s?id|token)|onnect\.sid|akephp|i_session)|koa[\.:]sess)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:73a0ba3547234fa983dce48e9cf0badf:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:92:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^_pk_ref`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7488d97763be19df9356e0237d9660f6:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/RESPONSE-954-DATA-LEAKAGES-IIS.conf:101:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^404$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7784d941baae3e1bf5ba4c336fc8ad5b:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:1816:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^(?:(?:max-age=[0-9]+|min-fresh=[0-9]+|no-cache|no-store|no-transform|only-if-cached|max-stale(?:=[0-9]+)?)(?:\s*\,\s*|$)){1,7}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7913ee6bfbce541a2d9ce9cdd9091756:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:85:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^pbjs-\w+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7e9b5dc488d03abf301a91a2147b6814:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:173:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^(?:GET|HEAD)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7f6b313656fbba41949609754d6c1406:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:97:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^_pk_ref`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:81b5a19497c6405ab0d230345c051055:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:653:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^OPTIONS$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:84eaf964b1a64fe4c0611d5d6a2c59c9:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-933-APPLICATION-ATTACK-PHP.conf:95:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`.*\.ph(?:p\d*|tml|ar|ps|t|pt)\.*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:86714c09aad06493636518e024bb7d6a:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:26:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^_ga(?:_\w+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:86b1aa955c1ffdc4de869bee54474822:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/RESPONSE-955-WEB-SHELLS.conf:194:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^<html>\r\n<head>\r\n<title>GRP WebShell [0-9.]+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8b4ae10edef03424d50bb4aacd28b270:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-932-APPLICATION-ATTACK-RCE.conf:629:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`(?:b[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?u[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?s[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?y[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?b[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?o[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?x|(?:c[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?o[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?m[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?m[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?a[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?n[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?d|e[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?(?:n[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?v|v[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?a[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?l)|w[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?a[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?t[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?c[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?h)[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?[\s\x0b&\),<>\|].*|[ls][\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?t[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?r[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?a[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?c[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?e|n[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?o[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?h[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?u[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?p|t[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?i[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?m[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?e[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?(?:[\s\x0b&\),<>\|].*|o[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?u[\"'\)\[\x5c]*(?:(?:(?:\|\||&&)[\s\x0b]*)?\$[!#\(\*\-0-9\?@_a-\{]*)?\x5c?t)|[\n\r;=`\{]|\|\|?|&&?|\$(?:\(\(?|[\[\{])|<(?:\(|<<)|>\(|\([\s\x0b]*\))[\s\x0b]*(?:[!\$\(\{][\s\x0b]*|(?:[0-9A-Z_a-z]+=[^\s\x0b]+|\$[0-9A-Z_a-z]+)[\s\x0b]+)*[\s\x0b]*[\"']*(?:[\"'-\+\--9\?A-\]_a-z\|]+/)?[\"'\x5c]*(?:aptitude|d(?:f|mesg)|env|h(?:ostname|top)|(?:(?:io|vm)sta|reboo)t|l(?:ast|s)|mysql(?:[^\s\x0b]{1,10}\b)?|ps(?:ql)?|s(?:et|hutdown|u)|w(?:ho(?:ami|is)?)?)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8c3e6585ec248c0e24a5f6c218548922:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:636:0`
- ground_truth_status: `None`
- disclosure: `private_first`

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

## usage_mismatch:928ff0cf6e703ed3e5601a5ef8f5c1dd:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-934-APPLICATION-ATTACK-GENERIC.conf:255:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^(?:json\.)?data:(?:(?:\*|[^!\"\(\),/:-\?\[-\]\{\}]+)/(?:\*|[^!\"\(\),/:-\?\[-\]\{\}]+)|\*)(?:[\s\x0b]*;[\s\x0b]*(?:charset[\s\x0b]*=[\s\x0b]*\"?(?:iso-8859-15?|utf-8|windows-1252)\b\"?|(?:[^\s\x0b-\"\(\),/:-\?\[-\]c\{\}]|c(?:[^!\"\(\),/:-\?\[-\]h\{\}]|h(?:[^!\"\(\),/:-\?\[-\]a\{\}]|a(?:[^!\"\(\),/:-\?\[-\]r\{\}]|r(?:[^!\"\(\),/:-\?\[-\]s\{\}]|s(?:[^!\"\(\),/:-\?\[-\]e\{\}]|e[^!\"\(\),/:-\?\[-\]t\{\}]))))))[^!\"\(\),/:-\?\[-\]\{\}]*[\s\x0b]*=[\s\x0b]*[^!\(\),/:-\?\[-\]\{\}]+);?)*(?:[\s\x0b]*,[\s\x0b]*(?:(?:\*|[^!\"\(\),/:-\?\[-\]\{\}]+)/(?:\*|[^!\"\(\),/:-\?\[-\]\{\}]+)|\*)(?:[\s\x0b]*;[\s\x0b]*(?:charset[\s\x0b]*=[\s\x0b]*\"?(?:iso-8859-15?|utf-8|windows-1252)\b\"?|(?:[^\s\x0b-\"\(\),/:-\?\[-\]c\{\}]|c(?:[^!\"\(\),/:-\?\[-\]h\{\}]|h(?:[^!\"\(\),/:-\?\[-\]a\{\}]|a(?:[^!\"\(\),/:-\?\[-\]r\{\}]|r(?:[^!\"\(\),/:-\?\[-\]s\{\}]|s(?:[^!\"\(\),/:-\?\[-\]e\{\}]|e[^!\"\(\),/:-\?\[-\]t\{\}]))))))[^!\"\(\),/:-\?\[-\]\{\}]*[\s\x0b]*=[\s\x0b]*[^!\(\),/:-\?\[-\]\{\}]+);?)*)*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:92ffce467df2f12ef8473083a715f6cb:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:1127:0`
- ground_truth_status: `None`
- disclosure: `private_first`

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

## usage_mismatch:9394eddfe5597576273e02ac05793314:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:88:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^_pk_ref`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:939c7c59cb5bb09e7a24a63f455fbe8d:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/RESPONSE-955-WEB-SHELLS.conf:294:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^ *<html>\n[ ]+<head>\n[ ]+<title>lostDC -`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:969fb33a2496abcc51d55c5a401b7e67:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-942-APPLICATION-ATTACK-SQLI.conf:558:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^(?:[^']*'|[^\"]*\"|[^`]*`)[\s\x0b]*;`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9a96f8945a7f9a55125da17f2ad204cb:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-942-APPLICATION-ATTACK-SQLI.conf:1524:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^(?:[^']*?(?:'[^']*?'[^']*?)*?'|[^\"]*?(?:\"[^\"]*?\"[^\"]*?)*?\"|[^`]*?(?:`[^`]*?`[^`]*?)*?`)[\s\x0b]*([0-9A-Z_a-z]+)\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9b26b580f284730a151c8b41cdc3f8e5:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/RESPONSE-955-WEB-SHELLS.conf:254:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^<!DOCTYPE html>\n<html>\n<!-- By Artyum [^<]*<title>Web Shell</title>`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9faf39132ee278a6d62809a6fe27d7bb:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:94:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^_pk_ref`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a3548258564c4e31da2c5e51f8522713:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/RESPONSE-955-WEB-SHELLS.conf:334:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^<html>\n<head>\n<div align=\"left\"><font size=\"1\">Input command :</font></div>\n<form name=\"cmd\" method=\"POST\" enctype=\"multipart/form-data\">`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a3ca8401ae6109781cfffe0624de8827:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:1278:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^(?:(?:\*|[^!\"\(\),/:-\?\[-\]\{\}]+)/(?:\*|[^!\"\(\),/:-\?\[-\]\{\}]+)|\*)(?:[\s\x0b]*;[\s\x0b]*(?:charset[\s\x0b]*=[\s\x0b]*\"?(?:iso-8859-15?|utf-8|windows-1252)\b\"?|(?:[^\s\x0b-\"\(\),/:-\?\[-\]c\{\}]|c(?:[^!\"\(\),/:-\?\[-\]h\{\}]|h(?:[^!\"\(\),/:-\?\[-\]a\{\}]|a(?:[^!\"\(\),/:-\?\[-\]r\{\}]|r(?:[^!\"\(\),/:-\?\[-\]s\{\}]|s(?:[^!\"\(\),/:-\?\[-\]e\{\}]|e[^!\"\(\),/:-\?\[-\]t\{\}]))))))[^!\"\(\),/:-\?\[-\]\{\}]*[\s\x0b]*=[\s\x0b]*[^!\(\),/:-\?\[-\]\{\}]+);?)*(?:[\s\x0b]*,[\s\x0b]*(?:(?:\*|[^!\"\(\),/:-\?\[-\]\{\}]+)/(?:\*|[^!\"\(\),/:-\?\[-\]\{\}]+)|\*)(?:[\s\x0b]*;[\s\x0b]*(?:charset[\s\x0b]*=[\s\x0b]*\"?(?:iso-8859-15?|utf-8|windows-1252)\b\"?|(?:[^\s\x0b-\"\(\),/:-\?\[-\]c\{\}]|c(?:[^!\"\(\),/:-\?\[-\]h\{\}]|h(?:[^!\"\(\),/:-\?\[-\]a\{\}]|a(?:[^!\"\(\),/:-\?\[-\]r\{\}]|r(?:[^!\"\(\),/:-\?\[-\]s\{\}]|s(?:[^!\"\(\),/:-\?\[-\]e\{\}]|e[^!\"\(\),/:-\?\[-\]t\{\}]))))))[^!\"\(\),/:-\?\[-\]\{\}]*[\s\x0b]*=[\s\x0b]*[^!\(\),/:-\?\[-\]\{\}]+);?)*)*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a5c1068bb77961bdf945514945cf2a32:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:90:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^_pk_ref`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a762d54741f39f85ba0b00c434505579:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:1762:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^(?i)up`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b25b8de1d8a3a6e5e9344d3b88bc420a:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:191:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^0?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bc084211f7333dd238953d0894968b2a:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:1209:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^.*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c356f899c2691a0ad83ee4b65035da7d:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:98:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^_pk_ref`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c4960a57704315e93cc0caa49ea866bb:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/RESPONSE-955-WEB-SHELLS.conf:458:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^<html>\n      <head>\n             <title>azrail [0-9.]+ by C-W-M</title>`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c632a1bc72497ad7b1145388b3ef3646:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:52:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^(?:connect (?:(?:[0-9]{1,3}\.){3}[0-9]{1,3}\.?(?::[0-9]+)?|[\--9A-Z_a-z]+:[0-9]+)|options \*|[a-z]{3,10}[\s\x0b]+(?:[0-9A-Z_a-z]{3,7}?://[\--9A-Z_a-z]*(?::[0-9]+)?)?/[^#\?]*(?:\?[^\s\x0b#]*)?(?:#[^\s\x0b]*)?)[\s\x0b]+[\.-9A-Z_a-z]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ca3e0bcb968304db4ddd317cd1b264ba:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-901-INITIALIZATION.conf:439:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^[a-f]*([0-9])[a-f]*([0-9])`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cbe9a27a4c5bf94d3bdd7cb058af632e:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/RESPONSE-955-WEB-SHELLS.conf:356:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^<html>\n<head>\n<title>Ru24PostWebShell`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ce5517710f00f341c911978b04bb0da5:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:28:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^_ga(?:_\w+)?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ce7e22cd3b364285ff19c3fbd44bb390:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-944-APPLICATION-ATTACK-JAVA.conf:166:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`.*\.(?:jsp|jspx)\.*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d026be832868257cac527f6e1c4e9181:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:983:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^[^;\s]+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d13e85d652e239261d63314d2912c203:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:89:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^_pk_ref`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d5ded5db67b3b565ab59dc278927215f:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-933-APPLICATION-ATTACK-PHP.conf:615:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`(?:^|[/\x5c])sess_[,\-0-9a-z]{20,256}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d7181c945239e83382c74ee00ba9d277:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:138:0`
- ground_truth_status: `None`
- disclosure: `private_first`

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

## usage_mismatch:d886fbc18feec00ea19fa48eedcaaeaa:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:99:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^_pk_ref`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d9aaa81e780529bf1d1857e503b38b3d:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:1728:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^(?:OPTIONS|CONNECT)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dc6daa0f32b6e575ba34ad3e402a971c:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-932-APPLICATION-ATTACK-RCE.conf:758:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^\(\s*\)\s+\{`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dda2d2c6a0dd71046f28b6f75d5134f6:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/RESPONSE-955-WEB-SHELLS.conf:396:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^<html>\r\n<head>\r\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=gb2312\">\r\n<title>PhpSpy Ver [0-9]+</title>`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e1c9e77ce8d7e4116bae920d23d5d5d3:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/RESPONSE-950-DATA-LEAKAGES.conf:140:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^5\d{2}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e2a16d69a603f3d4e25ac1da92ccce57:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:81:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^pbjs-\w+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e2b746ec01472853b554f8727f32545d:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:627:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^OPTIONS$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e33c26fd7b1d3beea6e631e89cdcd2d9:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:1560:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^.*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e43e61809a678007812510d63b541cac:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:82:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^pbjs-\w+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e463622ba2b3b4d8e515ac8f8d94d9ab:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-921-PROTOCOL-ATTACK.conf:290:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^[^\s\x0b,;]+[\s\x0b,;].*?(?:application/(?:.+\+)?json|(?:application/(?:soap\+)?|text/)xml)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e66d0252572894c81626300adeaa9f94:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:1660:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^[a-z]{3,10}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e699c6dcbcd7f6c6487d5b18637a273d:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/RESPONSE-955-WEB-SHELLS.conf:518:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^ <html><head><title>:: b374k m1n1 [0-9.]+ ::</title>`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e6f02e50bedb12f9bb6804fb5537c1f4:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/RESPONSE-955-WEB-SHELLS.conf:498:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^<html>\n<title>[^~]*~ Shell I</title>\n<head>\n<style>`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ebdea81dac3e81a6bb4be8e273ff72c2:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-999-COMMON-EXCEPTIONS-AFTER.conf:91:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^_pk_ref`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ee187649406f39c3a50b20f10a8a45e6:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:1935:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^(?:\?[01])?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f1fb7e9eaddc9a797ff86f50982f5dd4:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf:712:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^0$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f7338275e2811560db645f92b23b9dcb:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/RESPONSE-955-WEB-SHELLS.conf:214:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`<small>NGHshell [0-9.]+ by Cr4sh</body></html>\n$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fd4b8aa0ce21a10b2ac3509eb0f3705c:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-922-MULTIPART-ATTACK.conf:91:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^(?:(?:\*|[^!\"\(\),/:-\?\[-\]\{\}]+)/(?:\*|[^!\"\(\),/:-\?\[-\]\{\}]+)|\*)(?:[\s\x0b]*;[\s\x0b]*(?:charset[\s\x0b]*=[\s\x0b]*\"?(?:iso-8859-15?|utf-8|windows-1252)\b\"?|(?:[^\s\x0b-\"\(\),/:-\?\[-\]c\{\}]|c(?:[^!\"\(\),/:-\?\[-\]h\{\}]|h(?:[^!\"\(\),/:-\?\[-\]a\{\}]|a(?:[^!\"\(\),/:-\?\[-\]r\{\}]|r(?:[^!\"\(\),/:-\?\[-\]s\{\}]|s(?:[^!\"\(\),/:-\?\[-\]e\{\}]|e[^!\"\(\),/:-\?\[-\]t\{\}]))))))[^!\"\(\),/:-\?\[-\]\{\}]*[\s\x0b]*=[\s\x0b]*[^!\(\),/:-\?\[-\]\{\}]+);?)*(?:[\s\x0b]*,[\s\x0b]*(?:(?:\*|[^!\"\(\),/:-\?\[-\]\{\}]+)/(?:\*|[^!\"\(\),/:-\?\[-\]\{\}]+)|\*)(?:[\s\x0b]*;[\s\x0b]*(?:charset[\s\x0b]*=[\s\x0b]*\"?(?:iso-8859-15?|utf-8|windows-1252)\b\"?|(?:[^\s\x0b-\"\(\),/:-\?\[-\]c\{\}]|c(?:[^!\"\(\),/:-\?\[-\]h\{\}]|h(?:[^!\"\(\),/:-\?\[-\]a\{\}]|a(?:[^!\"\(\),/:-\?\[-\]r\{\}]|r(?:[^!\"\(\),/:-\?\[-\]s\{\}]|s(?:[^!\"\(\),/:-\?\[-\]e\{\}]|e[^!\"\(\),/:-\?\[-\]t\{\}]))))))[^!\"\(\),/:-\?\[-\]\{\}]*[\s\x0b]*=[\s\x0b]*[^!\(\),/:-\?\[-\]\{\}]+);?)*)*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fd627700a2e362f4522eca14894898ad:search

- result: `finding`
- site: `batch/corpora/coreruleset/rules/REQUEST-942-APPLICATION-ATTACK-SQLI.conf:863:0`
- ground_truth_status: `None`
- disclosure: `private_first`

### Pattern

`^[,\-0-9=A-Z_a-z]+$`

### Context

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

- result: `planned`
- site: `inventory:rc-shape1-injection-alphabet`
- ground_truth_status: `None`
- disclosure: `private_first`

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

- result: `planned`
- site: `inventory:rc-shape2-missing-keyword`
- ground_truth_status: `None`
- disclosure: `private_first`

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

- result: `planned`
- site: `inventory:rc-shape3-capture-truncation`
- ground_truth_status: `None`
- disclosure: `private_first`

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

- result: `planned`
- site: `inventory:rc-shape4-escape-image`
- ground_truth_status: `None`
- disclosure: `private_first`

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

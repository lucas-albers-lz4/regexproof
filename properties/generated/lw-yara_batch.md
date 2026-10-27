---
schema_version: "1"
corpus: lw-yara
findings: 11
---

# lw-yara batch findings

## usage_mismatch:20cbdd5a7ff2b9a36de283f9a2b7c0ea:search

```yaml
regex_id: 20cbdd5a7ff2b9a36de283f9a2b7c0ea
schema_version: "1"
kind: usage_mismatch
corpus: lw-yara
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lw-yara/rules/includes/pop_up_cache_082618.yar:19:6"
```

### Pattern

`\$zzrrzrz___=base64_decode\(\\"bjF6Ym1hNXZ0MGkyOC1weHVxeTZscmtkZzlfZWhjc3dvNGYzN2o=\\"\);\$z__zr_zzrr=\$zzrrzrz___\{30\}\.\$zzrrzrz___\{8\}\.\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:571547262e5129d9a0b2afdd885af7b2:hostname

```yaml
regex_id: 571547262e5129d9a0b2afdd885af7b2
schema_version: "1"
kind: intent_mismatch
corpus: lw-yara
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lw-yara/rules/includes/Navy-shells-072320.yar:56:6"
```

### Pattern

`if\(empty\(\$hostname\)\)\ return;\$exec='nslookup\ \-type=MX\ '\.escapeshellarg\(\$hostname\);@exec\(\$exec,\$output\);if\(empty\(\$output\)\)\ return;`

### Context

```json
{"admitted_char": "'@'", "keyword": "hostname", "reason": "name/comment claims validation but pattern admits excluded char"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:5ae9ae344ee333c6fb5e3a0f572f33aa:hostname

```yaml
regex_id: 5ae9ae344ee333c6fb5e3a0f572f33aa
schema_version: "1"
kind: intent_mismatch
corpus: lw-yara
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lw-yara/rules/includes/Navy-shells-072320.yar:55:6"
```

### Pattern

`if\(empty\(\$hostname\)\)\ return;\$exec='nslookup\ \-type=MX\ '\.escapeshellarg\(\$hostname\);@exec\(\$exec,\$output\);if\(empty\(\$output\)\)\ return;`

### Context

```json
{"admitted_char": "'@'", "keyword": "hostname", "reason": "name/comment claims validation but pattern admits excluded char"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:771dbd1dea3b7e29ef9d53b4b226c378:search

```yaml
regex_id: 771dbd1dea3b7e29ef9d53b4b226c378
schema_version: "1"
kind: usage_mismatch
corpus: lw-yara
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lw-yara/rules/includes/BabaYaga.yar:96:1"
```

### Pattern

`^0\.5\.2\.2\s*?0\.83\.4\.1\s+?1\.0\.145\.2\s+?1\.0\.145\.210\s+?1\.0\.177\.126`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:918cdf81e06c7c237bd513c400581ccc:search

```yaml
regex_id: 918cdf81e06c7c237bd513c400581ccc
schema_version: "1"
kind: usage_mismatch
corpus: lw-yara
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lw-yara/rules/includes/BabaYaga.yar:28:1"
```

### Pattern

`^x\%(?:01|25|9C|DA|5E)[\%A-Za-z\d\.\-\+\_]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:be775e90ce6ea0a562013d04fb173a47:search

```yaml
regex_id: be775e90ce6ea0a562013d04fb173a47
schema_version: "1"
kind: usage_mismatch
corpus: lw-yara
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lw-yara/rules/includes/index-malware-092518.yar:38:6"
```

### Pattern

`\$Id:\ index\.php\ 14401\ 2010\-01\-26\ 14:10:00Z\ louis\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fceb025c27d20d8a87440a947de1e297:search

```yaml
regex_id: fceb025c27d20d8a87440a947de1e297
schema_version: "1"
kind: usage_mismatch
corpus: lw-yara
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/lw-yara/rules/includes/newsletter.yar:62:6"
```

### Pattern

`\$mime\[\]\ =\ sprintf\('Content\-Type:\ %s;\ name=\\"%s\\"%s',\ \$type,\ \$this\->encodeHeader\(\$this\->secureHeader\(\$name\)\),\ \$`

### Context

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
corpus: lw-yara
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
corpus: lw-yara
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
corpus: lw-yara
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
corpus: lw-yara
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

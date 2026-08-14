---
schema_version: "1"
corpus: openmed
findings: 21
---

# openmed batch findings

## usage_mismatch:0c2de1f0a56ef4604846923ec82c7979:search

```yaml
regex_id: 0c2de1f0a56ef4604846923ec82c7979
schema_version: "1"
kind: usage_mismatch
corpus: openmed
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openmed/rules/openmed/core/anonymizer/providers/clinical_ids.py:3323:13"
```

### Pattern

`^(?:9\d{9}|9\d{3}(?P<bc_sep>[ -])\d{3}(?P=bc_sep)\d{3})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0c35f6988bd6ef41322d4a70f9c9ef32:search

```yaml
regex_id: 0c35f6988bd6ef41322d4a70f9c9ef32
schema_version: "1"
kind: usage_mismatch
corpus: openmed
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openmed/rules/openmed/core/anonymizer/format_preserve.py:151:21"
```

### Pattern

`^(?:X{4}|\*{4})[ -]?(?:X{4}|\*{4})[ -]?(?P<last_four>[0-9]{4})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1b18bf249b4ee29afac624922e785e26:search

```yaml
regex_id: 1b18bf249b4ee29afac624922e785e26
schema_version: "1"
kind: usage_mismatch
corpus: openmed
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openmed/rules/openmed/core/clinical_protect.py:44:4"
```

### Pattern

`^\d{3}-\d{2}-\d{4}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:200384b1d2f5c5b3a9c60d189c5d2b1d:match

```yaml
regex_id: 200384b1d2f5c5b3a9c60d189c5d2b1d
schema_version: "1"
kind: usage_mismatch
corpus: openmed
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/openmed/rules/openmed/core/pii_i18n.py:1130:12"
```

### Pattern

`^(\d{8})([A-Z])$`

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

## usage_mismatch:3c9576ad035818b1a772ad9d0f1eb5b1:search

```yaml
regex_id: 3c9576ad035818b1a772ad9d0f1eb5b1
schema_version: "1"
kind: usage_mismatch
corpus: openmed
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openmed/rules/openmed/core/anonymizer/providers/clinical_ids.py:3320:19"
```

### Pattern

`^(?:\d{9}|\d{3}(?P<sin_sep>[ -])\d{3}(?P=sin_sep)\d{3})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3e0ce90ff2e31adc447078160c1ed56d:search

```yaml
regex_id: 3e0ce90ff2e31adc447078160c1ed56d
schema_version: "1"
kind: usage_mismatch
corpus: openmed
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openmed/rules/openmed/core/anonymizer/registry.py:218:24"
```

### Pattern

`^(श्रीमती|श्री\.|सौ\.|कु\.)\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:43058437cef2c564813936539d18f7c9:search

```yaml
regex_id: 43058437cef2c564813936539d18f7c9
schema_version: "1"
kind: usage_mismatch
corpus: openmed
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openmed/rules/openmed/core/anonymizer/providers/clinical_ids.py:3524:26"
```

### Pattern

`^(?P<card>[2-6]\d{9}|[2-6]\d{3} \d{5} \d)(?:(?:[ ]*/[ ]*|[ -]?)(?P<irn>[1-9]))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4901d9e821f21949df03a0885dfc4e15:search

```yaml
regex_id: 4901d9e821f21949df03a0885dfc4e15
schema_version: "1"
kind: usage_mismatch
corpus: openmed
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openmed/rules/openmed/core/clinical_protect.py:45:4"
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

## usage_mismatch:57c33609a2d5b1b2cd2d3a15dd5f97c5:search

```yaml
regex_id: 57c33609a2d5b1b2cd2d3a15dd5f97c5
schema_version: "1"
kind: usage_mismatch
corpus: openmed
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openmed/rules/openmed/core/anonymizer/format_preserve.py:155:14"
```

### Pattern

`^(?:[2-9][0-9]{11}|[2-9][0-9]{3} [0-9]{4} [0-9]{4})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6558b495f6b1345fc7b317085fb895a2:search

```yaml
regex_id: 6558b495f6b1345fc7b317085fb895a2
schema_version: "1"
kind: usage_mismatch
corpus: openmed
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openmed/rules/openmed/core/anonymizer/providers/clinical_ids.py:728:19"
```

### Pattern

`^[a-z][a-z0-9]*(?:\.[a-z0-9]+)*@[a-z][a-z0-9-]{1,31}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6b50799679aac7f17502b7ca953ea06a:match

```yaml
regex_id: 6b50799679aac7f17502b7ca953ea06a
schema_version: "1"
kind: usage_mismatch
corpus: openmed
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/openmed/rules/openmed/core/pii_i18n.py:1156:12"
```

### Pattern

`^([XYZ])(\d{7})([A-Z])$`

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

## usage_mismatch:947cb6e2a1329fc8d07583e89ee4bbf2:search

```yaml
regex_id: 947cb6e2a1329fc8d07583e89ee4bbf2
schema_version: "1"
kind: usage_mismatch
corpus: openmed
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openmed/rules/openmed/core/clinical_protect.py:47:4"
```

### Pattern

`^(?:mrn|medical record|patient id|id)[:#\s-]*[a-z0-9][a-z0-9-]{3,}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:99194ac96819c7b14c6ff44d090e48be:search

```yaml
regex_id: 99194ac96819c7b14c6ff44d090e48be
schema_version: "1"
kind: usage_mismatch
corpus: openmed
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openmed/rules/openmed/core/anonymizer/providers/clinical_ids.py:3528:21"
```

### Pattern

`^(?:\d{9}|\d{3} \d{3} \d{3})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9c2427d0ef418bf3a02968fa378ed357:search

```yaml
regex_id: 9c2427d0ef418bf3a02968fa378ed357
schema_version: "1"
kind: usage_mismatch
corpus: openmed
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openmed/rules/openmed/core/anonymizer/registry.py:424:31"
```

### Pattern

`^[\u3400-\u4dbf\u4e00-\u9fff]{1,12}?省[\u3400-\u4dbf\u4e00-\u9fff]{1,12}?市`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a7e7a2a810152a166627f0a8f6493297:search

```yaml
regex_id: a7e7a2a810152a166627f0a8f6493297
schema_version: "1"
kind: usage_mismatch
corpus: openmed
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openmed/rules/openmed/core/clinical_protect.py:50:4"
```

### Pattern

`^[a-z]{0,4}\d[a-z0-9-]{5,}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bb1cbea4a2bcfc4dc17a3f8b393d3320:search

```yaml
regex_id: bb1cbea4a2bcfc4dc17a3f8b393d3320
schema_version: "1"
kind: usage_mismatch
corpus: openmed
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openmed/rules/openmed/core/pii_i18n.py:2450:19"
```

### Pattern

`^(\d{2})(\d{2})(\d{2})([-+YXWVUABCDEF])(\d{3})([0-9ABCDEFHJKLMNPRSTUVWXY])$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d528acc815324dae6c1da7a45e9c7e81:search

```yaml
regex_id: d528acc815324dae6c1da7a45e9c7e81
schema_version: "1"
kind: usage_mismatch
corpus: openmed
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openmed/rules/openmed/core/clinical_protect.py:46:4"
```

### Pattern

`^\d{1,2}[/-]\d{1,2}[/-]\d{2,4}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d6b45f7ec8fe595c19bf1267219c77fe:search

```yaml
regex_id: d6b45f7ec8fe595c19bf1267219c77fe
schema_version: "1"
kind: usage_mismatch
corpus: openmed
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openmed/rules/openmed/core/anonymizer/providers/clinical_ids.py:732:23"
```

### Pattern

`^(?:HPR|HFR)-[A-Z0-9][A-Z0-9-]{5,31}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e80cf6dcd9923b2314ec97d21db2e7d9:search

```yaml
regex_id: e80cf6dcd9923b2314ec97d21db2e7d9
schema_version: "1"
kind: usage_mismatch
corpus: openmed
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openmed/rules/openmed/core/anonymizer/providers/clinical_ids.py:1396:24"
```

### Pattern

`^(?P<source>.*)\|(?P<attempt>[0-9]+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ed07996dc3e886475104bdd8f66ed5b0:search

```yaml
regex_id: ed07996dc3e886475104bdd8f66ed5b0
schema_version: "1"
kind: usage_mismatch
corpus: openmed
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openmed/rules/openmed/core/anonymizer/providers/clinical_ids.py:3328:26"
```

### Pattern

`^(?P<number>[1-9]\d{3}(?P<ontario_sep>[ -]?)\d{3}(?P=ontario_sep)\d{3})(?:[ -]?(?P<version>[A-Za-z]{1,2}))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fe139beeb63d8b20cacf59ec7694458c:match

```yaml
regex_id: fe139beeb63d8b20cacf59ec7694458c
schema_version: "1"
kind: usage_mismatch
corpus: openmed
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/openmed/rules/openmed/core/pii_i18n.py:1001:19"
```

### Pattern

`^[12]\d{4}2[AB]\d{6}$`

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

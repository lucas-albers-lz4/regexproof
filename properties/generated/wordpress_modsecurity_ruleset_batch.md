---
schema_version: "1"
corpus: wordpress_modsecurity_ruleset
findings: 19
---

# wordpress_modsecurity_ruleset batch findings

## usage_mismatch:01a873c095c72b4268891d9381455cf8:search

```yaml
regex_id: 01a873c095c72b4268891d9381455cf8
schema_version: "1"
kind: usage_mismatch
corpus: wordpress_modsecurity_ruleset
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/wordpress_modsecurity_ruleset/rules/04-EVENTS.conf:11:0"
```

### Pattern

`^/wp\-login\.php`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1d2e9ad593471c45ba7439907157d613:search

```yaml
regex_id: 1d2e9ad593471c45ba7439907157d613
schema_version: "1"
kind: usage_mismatch
corpus: wordpress_modsecurity_ruleset
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/wordpress_modsecurity_ruleset/rules/04-EVENTS.conf:10:0"
```

### Pattern

`^POST$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3b1aa93b812f8eeae3c8ba3ac2160347:search

```yaml
regex_id: 3b1aa93b812f8eeae3c8ba3ac2160347
schema_version: "1"
kind: usage_mismatch
corpus: wordpress_modsecurity_ruleset
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/wordpress_modsecurity_ruleset/rules/04-EVENTS.conf:31:0"
```

### Pattern

`^logout$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:5ea35327454917b117bca40d137d8976:url

```yaml
regex_id: 5ea35327454917b117bca40d137d8976
schema_version: "1"
kind: intent_mismatch
corpus: wordpress_modsecurity_ruleset
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/wordpress_modsecurity_ruleset/rules/05-HARDENING.conf:136:0"
```

### Pattern

`^/wp\-admin/(load\-styles|load\-scripts)\.php.*load\[\]\=([^&,]*,){20,}`

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

## usage_mismatch:5ea35327454917b117bca40d137d8976:search

```yaml
regex_id: 5ea35327454917b117bca40d137d8976
schema_version: "1"
kind: usage_mismatch
corpus: wordpress_modsecurity_ruleset
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/wordpress_modsecurity_ruleset/rules/05-HARDENING.conf:136:0"
```

### Pattern

`^/wp\-admin/(load\-styles|load\-scripts)\.php.*load\[\]\=([^&,]*,){20,}`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6409918c5b1f8ac917f6397d871a352b:search

```yaml
regex_id: 6409918c5b1f8ac917f6397d871a352b
schema_version: "1"
kind: usage_mismatch
corpus: wordpress_modsecurity_ruleset
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/wordpress_modsecurity_ruleset/rules/03-BRUTEFORCE.conf:30:0"
```

### Pattern

`^POST$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:658150d8ddb998e7a78a7cc0561d0348:search

```yaml
regex_id: 658150d8ddb998e7a78a7cc0561d0348
schema_version: "1"
kind: usage_mismatch
corpus: wordpress_modsecurity_ruleset
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/wordpress_modsecurity_ruleset/rules/04-EVENTS.conf:45:0"
```

### Pattern

`^POST$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6637dc9aacd2828fcc99b2109a2e3a8c:search

```yaml
regex_id: 6637dc9aacd2828fcc99b2109a2e3a8c
schema_version: "1"
kind: usage_mismatch
corpus: wordpress_modsecurity_ruleset
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/wordpress_modsecurity_ruleset/rules/03-BRUTEFORCE.conf:50:0"
```

### Pattern

`^POST$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7b38758e1a9df8f7c7371852614f7381:search

```yaml
regex_id: 7b38758e1a9df8f7c7371852614f7381
schema_version: "1"
kind: usage_mismatch
corpus: wordpress_modsecurity_ruleset
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/wordpress_modsecurity_ruleset/rules/04-EVENTS.conf:48:0"
```

### Pattern

`^/wp\-login\.php`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7c3f571421ff4315f7ed6207b1466a61:search

```yaml
regex_id: 7c3f571421ff4315f7ed6207b1466a61
schema_version: "1"
kind: usage_mismatch
corpus: wordpress_modsecurity_ruleset
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/wordpress_modsecurity_ruleset/rules/05-HARDENING.conf:17:0"
```

### Pattern

`^/wp\-content(/.*\.txt(|[\/].*)|(|\/))$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:805a4c00e98b626adfa7b34e68bd42d8:search

```yaml
regex_id: 805a4c00e98b626adfa7b34e68bd42d8
schema_version: "1"
kind: usage_mismatch
corpus: wordpress_modsecurity_ruleset
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/wordpress_modsecurity_ruleset/rules/05-HARDENING.conf:152:0"
```

### Pattern

`^/(wp-cron\.php)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8693c8d5476c3c60b117b8cfebdbba65:search

```yaml
regex_id: 8693c8d5476c3c60b117b8cfebdbba65
schema_version: "1"
kind: usage_mismatch
corpus: wordpress_modsecurity_ruleset
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/wordpress_modsecurity_ruleset/rules/05-HARDENING.conf:110:0"
```

### Pattern

`^(/wp\-json/wp/v[0-9]+/users)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a869164d8e4e7a3699ed13e512d42774:search

```yaml
regex_id: a869164d8e4e7a3699ed13e512d42774
schema_version: "1"
kind: usage_mismatch
corpus: wordpress_modsecurity_ruleset
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/wordpress_modsecurity_ruleset/rules/05-HARDENING.conf:70:0"
```

### Pattern

`^/xmlrpc\.php`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:aba7d8e7cc5bc47cf575eb6d83bc4e4f:search

```yaml
regex_id: aba7d8e7cc5bc47cf575eb6d83bc4e4f
schema_version: "1"
kind: usage_mismatch
corpus: wordpress_modsecurity_ruleset
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/wordpress_modsecurity_ruleset/rules/05-HARDENING.conf:46:0"
```

### Pattern

`^/(?:readme|license)\.`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d7a766291a424fda5cf5c71528b3976d:search

```yaml
regex_id: d7a766291a424fda5cf5c71528b3976d
schema_version: "1"
kind: usage_mismatch
corpus: wordpress_modsecurity_ruleset
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/wordpress_modsecurity_ruleset/rules/03-BRUTEFORCE.conf:51:0"
```

### Pattern

`^/wp\-login\.php$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dd981c4a54227bc2e82d921de3baa0b5:search

```yaml
regex_id: dd981c4a54227bc2e82d921de3baa0b5
schema_version: "1"
kind: usage_mismatch
corpus: wordpress_modsecurity_ruleset
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/wordpress_modsecurity_ruleset/rules/04-EVENTS.conf:32:0"
```

### Pattern

`^/wp\-login\.php`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e46d47bf080298e6996147d58b1981a3:search

```yaml
regex_id: e46d47bf080298e6996147d58b1981a3
schema_version: "1"
kind: usage_mismatch
corpus: wordpress_modsecurity_ruleset
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/wordpress_modsecurity_ruleset/rules/05-HARDENING.conf:2:0"
```

### Pattern

`^/wp\-includes(/.*\.php(|[\/].*)|(|\/))$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e6bec4836bf2d92fdd779f90a89b980e:search

```yaml
regex_id: e6bec4836bf2d92fdd779f90a89b980e
schema_version: "1"
kind: usage_mismatch
corpus: wordpress_modsecurity_ruleset
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/wordpress_modsecurity_ruleset/rules/05-HARDENING.conf:32:0"
```

### Pattern

`^/wp-admin/(?:install|includes)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:feeb5af7c2a7131768eef3bb6c39eaf7:search

```yaml
regex_id: feeb5af7c2a7131768eef3bb6c39eaf7
schema_version: "1"
kind: usage_mismatch
corpus: wordpress_modsecurity_ruleset
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/wordpress_modsecurity_ruleset/rules/03-BRUTEFORCE.conf:31:0"
```

### Pattern

`^/wp\-login\.php$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

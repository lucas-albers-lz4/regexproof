---
schema_version: "1"
corpus: remotepower
findings: 56
---

# remotepower batch findings

## usage_mismatch:055df93209fe94f410c79c3061177404:search

```yaml
regex_id: 055df93209fe94f410c79c3061177404
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/client/remotepower-agent-mac.py:1448:20"
```

### Pattern

`^/(?:Users/[^/]+|var/root|private/var/root)/\.ssh/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0a87bb5e26c19324d2f30d6a3055b669:match

```yaml
regex_id: 0a87bb5e26c19324d2f30d6a3055b669
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/client/remotepower-agent.py:5048:15"
```

### Pattern

`^[A-Za-z0-9_.\-]+$`

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

## usage_mismatch:0d6b9c768b9d6375c8e05109d94f6086:search

```yaml
regex_id: 0d6b9c768b9d6375c8e05109d94f6086
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/client/remotepower-agent.py:3249:20"
```

### Pattern

`^(sha256:)?[0-9a-f]{12,64}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0e61f79b77f0876555622987a6ae6749:match

```yaml
regex_id: 0e61f79b77f0876555622987a6ae6749
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/billing.py:267:8"
```

### Pattern

`^(\d{4})-W(\d{2})$`

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

## usage_mismatch:1268e4b4c615b67078261033956600dd:match

```yaml
regex_id: 1268e4b4c615b67078261033956600dd
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/client/remotepower-agent.py:2870:20"
```

### Pattern

`^(.+?)-(\d[^-]*(-r\d+)?)$`

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

## usage_mismatch:1ac58debf0c43cdf1338edf960dd5f73:search

```yaml
regex_id: 1ac58debf0c43cdf1338edf960dd5f73
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/sanitize.py:172:20"
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

## usage_mismatch:233f8b262903c92901b45d20cfd9c87c:search

```yaml
regex_id: 233f8b262903c92901b45d20cfd9c87c
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/dmarc_monitor.py:156:15"
```

### Pattern

`^[A-Za-z0-9._-]{1,128}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:246fad718d14d5047a7b5b895e1ba9b3:match

```yaml
regex_id: 246fad718d14d5047a7b5b895e1ba9b3
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/proxmox_client.py:1179:11"
```

### Pattern

`^[A-Za-z0-9_\-.]{1,64}$`

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

## usage_mismatch:268d856c47efe4dc602a4ebb3e7ddaea:search

```yaml
regex_id: 268d856c47efe4dc602a4ebb3e7ddaea
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/client/remotepower-agent-win.py:3185:19"
```

### Pattern

`^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,127}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2d0d7ce8f519f94cea23f44f4186aab4:search

```yaml
regex_id: 2d0d7ce8f519f94cea23f44f4186aab4
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/sanitize.py:25:10"
```

### Pattern

`^\d{1,4}\.\d{1,4}(?:\.\d{1,4})?(?:[.\-]\w{1,16})?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:31f550e0d613b33a875a7ee5e29cd972:search

```yaml
regex_id: 31f550e0d613b33a875a7ee5e29cd972
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/proxmox_client.py:706:15"
```

### Pattern

`^[a-zA-Z0-9_.\-]+:[a-zA-Z0-9_./\-]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:363abb816b7bb41f7223d36728efd4cf:search

```yaml
regex_id: 363abb816b7bb41f7223d36728efd4cf
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/cloud_import.py:134:13"
```

### Pattern

`^[a-z]{2}(-[a-z]+)+-\d$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:375a70e8e5c2b40b839da5fba6832395:search

```yaml
regex_id: 375a70e8e5c2b40b839da5fba6832395
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/client/remotepower-agent.py:4278:15"
```

### Pattern

`\.\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:39519ee84291cdec4ffedf790a820b61:search

```yaml
regex_id: 39519ee84291cdec4ffedf790a820b61
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/client/remotepower-agent-win.py:898:16"
```

### Pattern

`^[A-Za-z0-9][A-Za-z0-9.+_-]{0,127}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:47397da0b706f3b0320dd6d45756fd28:search

```yaml
regex_id: 47397da0b706f3b0320dd6d45756fd28
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/proxmox_client.py:704:15"
```

### Pattern

`^[a-zA-Z0-9]([a-zA-Z0-9\-.]{0,61}[a-zA-Z0-9])?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:47623f34308025ff354be93668c58493:search

```yaml
regex_id: 47623f34308025ff354be93668c58493
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/proxmox_client.py:705:15"
```

### Pattern

`^[a-zA-Z0-9_.\-]{1,15}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:50c4416b02a8543a23d5bbc1803017f4:search

```yaml
regex_id: 50c4416b02a8543a23d5bbc1803017f4
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/proxmox_client.py:580:22"
```

### Pattern

`^[A-Za-z][^\x00-\x1f\x7f/\\]{0,63}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:53cd9e571843235e983413f667a597b2:search

```yaml
regex_id: 53cd9e571843235e983413f667a597b2
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/tools/gen-wiki.py:35:47"
```

### Pattern

`security-review-.*\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5e32ffa55b060d8e249893068b3d50b3:search

```yaml
regex_id: 5e32ffa55b060d8e249893068b3d50b3
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/hypervisor.py:48:12"
```

### Pattern

`^[a-z0-9][a-z0-9.-]{0,252}[a-z0-9]$|^[a-z0-9]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5f5f3c64c14a99f92a6219ce35090cd9:search

```yaml
regex_id: 5f5f3c64c14a99f92a6219ce35090cd9
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/client/remotepower-agent-mac.py:1584:61"
```

### Pattern

`\.\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5ffe66be81d6bb6b44e75861c8ecb1d1:search

```yaml
regex_id: 5ffe66be81d6bb6b44e75861c8ecb1d1
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/proxmox_client.py:565:20"
```

### Pattern

`^[A-Za-z][A-Za-z0-9_-]{0,39}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6288ec120630527555887e667eea27dd:search

```yaml
regex_id: 6288ec120630527555887e667eea27dd
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/ai_triage_handlers.py:516:16"
```

### Pattern

`^T\d{4}(?:\.\d{3})?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:66c40da6a03f61562a6d045ac1cdd700:match

```yaml
regex_id: 66c40da6a03f61562a6d045ac1cdd700
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/proxmox_client.py:1152:15"
```

### Pattern

`^[A-Za-z][A-Za-z0-9_\-]{0,39}$`

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

## usage_mismatch:70829a0979c014b5b5ef0ee8f912ad6e:search

```yaml
regex_id: 70829a0979c014b5b5ef0ee8f912ad6e
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/tools/gen-wiki.py:35:14"
```

### Pattern

`.*-internal\.md$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7cfb5620cce980239fabbd51654606a4:search

```yaml
regex_id: 7cfb5620cce980239fabbd51654606a4
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/sanitize.py:24:10"
```

### Pattern

`^([0-9A-Fa-f]{2}[:\-]){5}[0-9A-Fa-f]{2}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7d533d0e5c3c4d97d651b0c290e98adf:match

```yaml
regex_id: 7d533d0e5c3c4d97d651b0c290e98adf
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/proxmox_client.py:903:11"
```

### Pattern

`^[a-z0-9]{2,8}$`

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

## usage_mismatch:801ddca47c5df7b2863882604812488b:search

```yaml
regex_id: 801ddca47c5df7b2863882604812488b
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/ip_reputation.py:23:11"
```

### Pattern

`^(?=.{1,253}$)(?!-)[A-Za-z0-9-]{1,63}(\.[A-Za-z0-9-]{1,63})+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8609187a6a2976db76668cb3d297d0ef:search

```yaml
regex_id: 8609187a6a2976db76668cb3d297d0ef
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/client/remotepower-agent.py:9186:19"
```

### Pattern

`^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,127}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:879110c1fb58b0b7674aecb0cc23d0f2:match

```yaml
regex_id: 879110c1fb58b0b7674aecb0cc23d0f2
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/acme_handlers.py:468:11"
```

### Pattern

`^[a-zA-Z0-9_-]{1,64}$`

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

## usage_mismatch:87ad2666c536ef9fa2e4a7b35e2c4a6d:search

```yaml
regex_id: 87ad2666c536ef9fa2e4a7b35e2c4a6d
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/dmarc_monitor.py:155:13"
```

### Pattern

`^(?=.{1,253}$)([A-Za-z0-9_]([A-Za-z0-9_-]{0,61}[A-Za-z0-9])?\.)+[A-Za-z]{2,}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:89ac37dce043bcbee02a31260f95e441:search

```yaml
regex_id: 89ac37dce043bcbee02a31260f95e441
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/client/remotepower-agent.py:1846:16"
```

### Pattern

`sudo(?:\[\d+\])?:\s*(?P<user>[\w.\-]+)\s*:.*?(?:TTY=(?P<tty>[\w/\-]+))?.*?(?:PWD=(?P<pwd>\S+))?.*?USER=(?P<target>[\w.\-]+)\s*;\s*COMMAND=(?P<cmd>.+)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9c6813acdc4aa57924fab14492862665:search

```yaml
regex_id: 9c6813acdc4aa57924fab14492862665
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/wg_access.py:36:12"
```

### Pattern

`^rp-wg(\d{1,3})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a37e0f3bfaac643676b14f9074424d3d:search

```yaml
regex_id: a37e0f3bfaac643676b14f9074424d3d
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/rag_index.py:1573:27"
```

### Pattern

`(?im)^(\s*(?:export\s+)?[A-Za-z0-9_]*(?:password|passwd|secret|token|api[_-]?key|apikey|passphrase|private[_-]?key|access[_-]?key|client[_-]?secret|bearer|credential)[A-Za-z0-9_]*)\s*([:=])\s*\S.*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:aae9d8c7198009bcb02195b45ef6f22d:search

```yaml
regex_id: aae9d8c7198009bcb02195b45ef6f22d
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/apps_compose_handlers.py:32:17"
```

### Pattern

`^[a-z0-9][a-z0-9_-]{0,63}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b5b91d6c5a70ebeff70d038bf5341e97:match

```yaml
regex_id: b5b91d6c5a70ebeff70d038bf5341e97
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/billing.py:255:8"
```

### Pattern

`^(\d{4})-(\d{2})$`

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

## usage_mismatch:bf12c163baef0ea842f49c78ece7f03b:search

```yaml
regex_id: bf12c163baef0ea842f49c78ece7f03b
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/dns_resolve.py:42:15"
```

### Pattern

`^(?=.{1,253}\.?$)(?!-)[A-Za-z0-9_-]{1,63}(?<!-)(\.(?!-)[A-Za-z0-9_-]{1,63}(?<!-))*\.?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c10b79721ea379062b6b92dbe0c1c346:search

```yaml
regex_id: c10b79721ea379062b6b92dbe0c1c346
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/logsig.py:73:17"
```

### Pattern

`^<ts>\s+\S+\s+[\w.@\-]+(?:\[<pid>\])?:\s*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c3294d3cd313ed9206a1a7318b834509:search

```yaml
regex_id: c3294d3cd313ed9206a1a7318b834509
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/wg_access.py:35:13"
```

### Pattern

`^[A-Za-z0-9+/]{43}=$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c42a125bbc0374d2e92cb7519facc733:search

```yaml
regex_id: c42a125bbc0374d2e92cb7519facc733
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/sanitize.py:18:10"
```

### Pattern

`^(?:(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)|(?:[0-9a-fA-F]{1,4}:){1,7}[0-9a-fA-F]{1,4})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c4ad2e7091cb4658598de6945af24758:search

```yaml
regex_id: c4ad2e7091cb4658598de6945af24758
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/wg_access.py:37:11"
```

### Pattern

`^[A-Za-z0-9][A-Za-z0-9 ._\-]{0,63}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cc1e94125c99462b4da057b9b28b6124:search

```yaml
regex_id: cc1e94125c99462b4da057b9b28b6124
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/client/remotepower-agent-mac.py:1191:20"
```

### Pattern

`^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d3517dc6e0a47a3d5bfe3e5f29cad432:match

```yaml
regex_id: d3517dc6e0a47a3d5bfe3e5f29cad432
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/webterm/remotepower-webterm.py:354:11"
```

### Pattern

`^[a-zA-Z0-9._\-]{1,32}$`

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

## usage_mismatch:d88253c7b0c2157da80b157ff5389c85:match

```yaml
regex_id: d88253c7b0c2157da80b157ff5389c85
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/client/remotepower-agent.py:5546:27"
```

### Pattern

`^\d{1,3}(\.\d{1,3}){3}$`

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

## usage_mismatch:daac73e9e64db96281b607cf7e51135c:match

```yaml
regex_id: daac73e9e64db96281b607cf7e51135c
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/acme_handlers.py:543:11"
```

### Pattern

`^[a-zA-Z0-9_-]{1,64}$`

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

## usage_mismatch:daae3b1f3253926252d963c3aa59e067:match

```yaml
regex_id: daae3b1f3253926252d963c3aa59e067
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/client/remotepower-agent.py:8361:37"
```

### Pattern

`^[0-9./]+$`

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

## usage_mismatch:df1acbd39fc2f074493baf4edd051591:search

```yaml
regex_id: df1acbd39fc2f074493baf4edd051591
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/integrations.py:2449:14"
```

### Pattern

`^[A-Za-z0-9_.-]{1,100}/[A-Za-z0-9_.-]{1,100}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:df1c881a79d59ff5ff334b6c296ef19b:match

```yaml
regex_id: df1c881a79d59ff5ff334b6c296ef19b
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/proxmox_client.py:1161:15"
```

### Pattern

`^[A-Za-z][A-Za-z0-9_\-]{0,39}$`

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

## usage_mismatch:ea995710d1654617d79fb2be246b2daa:match

```yaml
regex_id: ea995710d1654617d79fb2be246b2daa
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/acme_handlers.py:165:16"
```

### Pattern

`^(?=.{1,253}$)(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?$`

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

## usage_mismatch:ec3d4f5cd412de99669dea0f12975f2d:search

```yaml
regex_id: ec3d4f5cd412de99669dea0f12975f2d
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/client/remotepower-agent.py:9103:17"
```

### Pattern

`^[a-z0-9][a-z0-9_-]{0,63}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ef1369c9393202a81a6a952db603473f:search

```yaml
regex_id: ef1369c9393202a81a6a952db603473f
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/client/remotepower-agent.py:1258:14"
```

### Pattern

`^[a-z][a-z0-9_]{0,63}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f9c6e6799634e020e3692821bb7f0a9b:search

```yaml
regex_id: f9c6e6799634e020e3692821bb7f0a9b
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/server/cgi-bin/rag_index.py:107:14"
```

### Pattern

`^(#{1,6})\s+(.*)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fb192290ee08f041e3c67187c0663c5e:match

```yaml
regex_id: fb192290ee08f041e3c67187c0663c5e
schema_version: "1"
kind: usage_mismatch
corpus: remotepower
call_kind: match
shape: null
result: finding
disclosure: null
site: "batch/corpora/remotepower/rules/client/remotepower-agent-mac.py:1958:19"
```

### Pattern

`^[A-Za-z0-9@._+-]{1,80}$`

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

## property:inventory:rc-shape1-injection-alphabet:rc-shape1-injection-alphabet

```yaml
regex_id: "inventory:rc-shape1-injection-alphabet"
schema_version: "1"
kind: property
corpus: remotepower
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
corpus: remotepower
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
corpus: remotepower
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
corpus: remotepower
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

---
schema_version: "1"
corpus: openwrt_packages
findings: 139
---

# openwrt_packages batch findings

## usage_mismatch:01156997f4c26638cc50b7f0d7527767:search

```yaml
regex_id: 01156997f4c26638cc50b7f0d7527767
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/p910nd/files/p910nd.hotplug:169:5"
```

### Pattern

`^$DRIVER_HOME_DEFAULT$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:02a1fa58d486b0679e6336c8adfc3c7b:search

```yaml
regex_id: 02a1fa58d486b0679e6336c8adfc3c7b
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/snort3/files/snort-mgr:255:34"
```

### Pattern

`^${gid}:${sid}\b`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:02db9811dc215d0d4fefa05365350dca:search

```yaml
regex_id: 02db9811dc215d0d4fefa05365350dca
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/speedtest-netperf/files/speedtest-netperf.sh:170:2"
```

### Pattern

`^cpu[0-9]*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0310b1ebf19f3c3a0acf44cdca214965:search

```yaml
regex_id: 0310b1ebf19f3c3a0acf44cdca214965
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/libreswan/files/etc/hotplug.d/iface/89-libreswan:7:21"
```

### Pattern

`='$INTERFACE'$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0394ba59cdbd82555d5aa6573187d12b:search

```yaml
regex_id: 0394ba59cdbd82555d5aa6573187d12b
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/wsdd2/files/wsdd2.init:38:13"
```

### Pattern

`^[[:blank:]]*[^[:blank:]#;]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:063e6fb32e576f2393fba35abbbb428b:search

```yaml
regex_id: 063e6fb32e576f2393fba35abbbb428b
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/safe-search/files/safe-search-maintenance:12:14"
```

### Pattern

`^[:0-9a-f]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0a11945cd8a5b5d87aafefd7f827d044:search

```yaml
regex_id: 0a11945cd8a5b5d87aafefd7f827d044
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/lang/ruby/ruby_missingfiles:58:1"
```

### Pattern

`^  - name: `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0c647e67870af31506ae5c71bae58b58:search

```yaml
regex_id: 0c647e67870af31506ae5c71bae58b58
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/hs20/files/hs20-server.defaults:3:37"
```

### Pattern

`^\.php`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0c6f4a92d55771324db29e105326466c:search

```yaml
regex_id: 0c6f4a92d55771324db29e105326466c
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/files/etc/init.d/pbr:353:24"
```

### Pattern

`^[a-zA-Z0-9][a-zA-Z0-9_-]{0,61}[a-zA-Z0-9]$|^[a-zA-Z0-9]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0e14b6244842e571eb912df3b3180ca6:search

```yaml
regex_id: 0e14b6244842e571eb912df3b3180ca6
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/openssh/files/sshd.init:31:15"
```

### Pattern

`^Port `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:10774de7240e725bae4d057f1e62f8ff:search

```yaml
regex_id: 10774de7240e725bae4d057f1e62f8ff
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/lang/ruby/ruby_missingfiles:57:1"
```

### Pattern

`\|$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:12c1433e5ac285ba9f638bdea964d47e:search

```yaml
regex_id: 12c1433e5ac285ba9f638bdea964d47e
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/tests/06_network/01_gateway_discovery:45:67"
```

### Pattern

`^fe80:.*router`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:14f3ccc1c9f8fb5f551d7f5a679bec4d:search

```yaml
regex_id: 14f3ccc1c9f8fb5f551d7f5a679bec4d
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/uacme/files/dnsapi_helper.sh:536:137"
```

### Pattern

`^NIST CURVE:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:18f6f2686481ee4136549859e9100d74:search

```yaml
regex_id: 18f6f2686481ee4136549859e9100d74
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/utils/librespeed-cli-rust/test.sh:21:66"
```

### Pattern

`^7: Example`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1b1209c5ce43b4840d3b8b82a7e8cfc8:search

```yaml
regex_id: 1b1209c5ce43b4840d3b8b82a7e8cfc8
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/tests/08_dns/01_nftset_element:155:1"
```

### Pattern

`^nftset=/other\.com/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1ca016be497e4bd666fd71b92a502262:search

```yaml
regex_id: 1ca016be497e4bd666fd71b92a502262
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/mwan3/files/lib/mwan3/mwan3.sh:275:23"
```

### Pattern

`\-N mwan3_$\{chain}_$\{family}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1cf2bd22f0ee7d3391109f0d1b6583b5:search

```yaml
regex_id: 1cf2bd22f0ee7d3391109f0d1b6583b5
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/utils/hwdata/test.sh:10:2"
```

### Pattern

`^0781`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1d655aac1a05af714a68fc1507893271:search

```yaml
regex_id: 1d655aac1a05af714a68fc1507893271
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/libs/nacl/do-openwrt:106:38"
```

### Pattern

`\.[sS]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1ec1f743883938c52f58f914e69c5cac:search

```yaml
regex_id: 1ec1f743883938c52f58f914e69c5cac
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/nginx-util/src/test-nginx-util-root.sh:133:21"
```

### Pattern

`^\s*ssl_session_timeout\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:21bc7b08816e1c325b2bf5c956318abd:search

```yaml
regex_id: 21bc7b08816e1c325b2bf5c956318abd
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/uacme/files/dnsapi_helper.sh:1081:7"
```

### Pattern

`^#$__opt$__sep`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:246722ce7323dc5e08de57946a7b1d18:search

```yaml
regex_id: 246722ce7323dc5e08de57946a7b1d18
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/files/etc/init.d/pbr:373:31"
```

### Pattern

`^([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:25442b74f6b4503308aa23f2b6367d4b:search

```yaml
regex_id: 25442b74f6b4503308aa23f2b6367d4b
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/lang/golang/golang-build.sh:57:35"
```

### Pattern

`\.(c|cc|cpp|go|h|hh|hpp|proto|s)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:257cc5a3867210e35ccc5da8f205204d:search

```yaml
regex_id: 257cc5a3867210e35ccc5da8f205204d
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/tests/lib/mocks/functions.sh:48:7"
```

### Pattern

`^list[[:space:]]+([^[:space:]]+)[[:space:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:25aac9a1b6b1fafdb2681e9850db4ceb:search

```yaml
regex_id: 25aac9a1b6b1fafdb2681e9850db4ceb
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/frr/files/frrcommon.sh:382:58"
```

### Pattern

`^declare -a`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2896bdbf968b0996b58c56ef8f7eb99d:search

```yaml
regex_id: 2896bdbf968b0996b58c56ef8f7eb99d
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/tests/lib/mocks/functions.sh:42:7"
```

### Pattern

`^option[[:space:]]+([^[:space:]]+)[[:space:]]+([^[:space:]]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2adba19c21bba5b7dc76adf36281e326:search

```yaml
regex_id: 2adba19c21bba5b7dc76adf36281e326
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/ddns-scripts/files/usr/lib/ddns/update_dnspod_cn_v3.sh:110:49"
```

### Pattern

`[^"]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2ca8066c8abbe6fea09b050beef5731c:search

```yaml
regex_id: 2ca8066c8abbe6fea09b050beef5731c
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/mwan3/files/lib/mwan3/mwan3.sh:943:11"
```

### Pattern

`^-A mwan3_rules.*-i $device`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2e635c86496ec6e4259100391d37eff8:search

```yaml
regex_id: 2e635c86496ec6e4259100391d37eff8
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/files/etc/init.d/pbr:355:28"
```

### Pattern

`^([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2f2b18924b895fcdc1a83e2738d38a77:search

```yaml
regex_id: 2f2b18924b895fcdc1a83e2738d38a77
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/mwan3/files/lib/mwan3/mwan3.sh:1157:68"
```

### Pattern

`.*--comment ([^ ]*) .*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2f5111d745018ecffd3582b831858e58:search

```yaml
regex_id: 2f5111d745018ecffd3582b831858e58
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/tayga/files/tayga.sh:5:17"
```

### Pattern

`^ *$if:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2fa3eb0ff3c0c54c17c4fb04ff35eaa4:search

```yaml
regex_id: 2fa3eb0ff3c0c54c17c4fb04ff35eaa4
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/lang/perl/files/perl-run_tests.sh:70:50"
```

### Pattern

`\.t$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3016f641a3857846abb84c7c9344ad2d:search

```yaml
regex_id: 3016f641a3857846abb84c7c9344ad2d
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/adblock-fast/tests/run_tests.sh:370:26"
```

### Pattern

`^#!/bin/sh`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:32d15aca9c0e265a8eb2052b37ecab0d:search

```yaml
regex_id: 32d15aca9c0e265a8eb2052b37ecab0d
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/freeradius3/test.sh:18:1"
```

### Pattern

`^raddbdir = $FR_ETC\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:373e1e95bec111f246e5d2ff7677cdce:search

```yaml
regex_id: 373e1e95bec111f246e5d2ff7677cdce
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/mwan3/files/lib/mwan3/mwan3.sh:1152:32"
```

### Pattern

`.*--comment "out .*" .*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3a65ae314e43dff4d4cb193c7f01a3ab:search

```yaml
regex_id: 3a65ae314e43dff4d4cb193c7f01a3ab
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/utils/shadow/test.sh:72:13"
```

### Pattern

`^GROUP=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3ac06970655b79079ee64083dd445521:search

```yaml
regex_id: 3ac06970655b79079ee64083dd445521
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/files/etc/init.d/pbr:420:39"
```

### Pattern

`$\{ipTablePrefix}_$\{iface}\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:3d1aed459d9d77efe886ed9ae75fcda3:search

```yaml
regex_id: 3d1aed459d9d77efe886ed9ae75fcda3
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/lang/golang/golang-build.sh:59:36"
```

### Pattern

`/go\.(mod|sum|work)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:427027bacdc514b4df6884c7589c7954:search

```yaml
regex_id: 427027bacdc514b4df6884c7589c7954
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/tests/08_dns/01_nftset_element:47:13"
```

### Pattern

`^nftset=/example\.com/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:42bf6108e37dec4564ae33b90112ff39:search

```yaml
regex_id: 42bf6108e37dec4564ae33b90112ff39
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/https-dns-proxy/tests/run_tests.sh:816:26"
```

### Pattern

`^#!/bin/sh`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4420e0b7fa931075a6914371960f11de:search

```yaml
regex_id: 4420e0b7fa931075a6914371960f11de
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/bsbf-openwrt-resources/files/etc/hotplug.d/net/99-bsbf-autoconf-cellular:6:37"
```

### Pattern

`^DRIVER=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:446fb231af786ee82422d11d66ac47c4:search

```yaml
regex_id: 446fb231af786ee82422d11d66ac47c4
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/dcwapd/files/dcwapd.init:101:36"
```

### Pattern

`^br-`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:44889df84c4094b44ac18d2578455d0a:search

```yaml
regex_id: 44889df84c4094b44ac18d2578455d0a
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/files/etc/init.d/pbr:296:66"
```

### Pattern

`^fe80:.*router`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:44d98117c6784a80266de93e93bd70ce:search

```yaml
regex_id: 44d98117c6784a80266de93e93bd70ce
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/frr/files/frrcommon.sh:357:1"
```

### Pattern

`^[[:blank:]]*(#|$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:44ddfd5057787ccd671ab245429f7773:search

```yaml
regex_id: 44ddfd5057787ccd671ab245429f7773
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/tests/08_dns/01_nftset_element:82:8"
```

### Pattern

`^nftset=/example\.com/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:44f879416fcc378a6a359f25eb7eedae:search

```yaml
regex_id: 44f879416fcc378a6a359f25eb7eedae
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/files/etc/init.d/pbr:1147:28"
```

### Pattern

`^nftset=/${escaped_param}/.*#${safe_nftset6}(,| |$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:46a4ead8d7ef767ccda3b0690b4c96b5:search

```yaml
regex_id: 46a4ead8d7ef767ccda3b0690b4c96b5
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/uacme/files/dnsapi_helper.sh:1123:25"
```

### Pattern

`^$_sdkey *=.*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4a325d957adc753010146f33fa656392:search

```yaml
regex_id: 4a325d957adc753010146f33fa656392
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/files/etc/init.d/pbr:364:24"
```

### Pattern

`^((25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})(/(3[0-2]|[12]?[0-9]))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4a60ee00345dc0759ca4ab3008edee63:search

```yaml
regex_id: 4a60ee00345dc0759ca4ab3008edee63
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/ddns-scripts/files/usr/lib/ddns/update_dnspod_cn_v3.sh:319:48"
```

### Pattern

`[^"]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4e84b83839be05466de031087e0dc20d:search

```yaml
regex_id: 4e84b83839be05466de031087e0dc20d
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/tayga/files/tayga.sh:15:17"
```

### Pattern

`^ *$if:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4eb13874c49639c8f1119db3d0318f3a:search

```yaml
regex_id: 4eb13874c49639c8f1119db3d0318f3a
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/utils/catatonit/test.sh:5:33"
```

### Pattern

`^tini version`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:508250abfae54d8ae74cc28140d777da:search

```yaml
regex_id: 508250abfae54d8ae74cc28140d777da
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/radius-mac/files/radius-mac.init:78:23"
```

### Pattern

`^([0-9a-f]{2}[:-]){5}[0-9a-f]{2}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:55a9e990c3d37867c6f32f16600cf779:search

```yaml
regex_id: 55a9e990c3d37867c6f32f16600cf779
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/uacme/files/dnsapi_helper.sh:527:132"
```

### Pattern

`^publicExponent:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:569004cd8d00e09210b41b48fd13c2b2:search

```yaml
regex_id: 569004cd8d00e09210b41b48fd13c2b2
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/nut/files/add_nut_httpd_conf.default:19:0"
```

### Pattern

`^/cgi-bin/nut`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5a62c266dc80351f5f0269674116b900:search

```yaml
regex_id: 5a62c266dc80351f5f0269674116b900
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/ddns-scripts/files/usr/lib/ddns/update_huaweicloud_com.sh:52:22"
```

### Pattern

`/$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5dd447485ecacc6d00a724031678cc84:search

```yaml
regex_id: 5dd447485ecacc6d00a724031678cc84
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/open-iscsi/files/iscsi-gen-initiatorname:27:45"
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

## usage_mismatch:5de8c1da76918660d76feccb968c0918:search

```yaml
regex_id: 5de8c1da76918660d76feccb968c0918
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/mwan3/files/lib/mwan3/mwan3.sh:1148:36"
```

### Pattern

`.*--comment "out .*" .*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5fe2c7a1dc54cfd6fdcab99f583628dc:search

```yaml
regex_id: 5fe2c7a1dc54cfd6fdcab99f583628dc
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/travelmate/files/travelmate.init:152:48"
```

### Pattern

`^wireless.trm_uplink[0-9]+=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:620b26f57679a69779f4f12ac2d0128d:search

```yaml
regex_id: 620b26f57679a69779f4f12ac2d0128d
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/files/etc/init.d/pbr:354:28"
```

### Pattern

`^([a-zA-Z0-9]([a-zA-Z0-9_-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:62d0b6c1487f5e0d1d538e2158cdc6c0:search

```yaml
regex_id: 62d0b6c1487f5e0d1d538e2158cdc6c0
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/lang/perl/files/perl-run_tests.sh:62:31"
```

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

## usage_mismatch:657ad985638f3fc8b923570ff3be7bdb:search

```yaml
regex_id: 657ad985638f3fc8b923570ff3be7bdb
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/utils/shadow/test.sh:82:18"
```

### Pattern

`^root`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:65a2f089b9716d174e0d69aa9891a1c1:search

```yaml
regex_id: 65a2f089b9716d174e0d69aa9891a1c1
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/ddns-scripts/files/usr/lib/ddns/update_dnspod_cn_v3.sh:78:51"
```

### Pattern

`[^"]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:675044caba963819ab1256cb6ea6de4b:search

```yaml
regex_id: 675044caba963819ab1256cb6ea6de4b
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/fwknop/files/fwknopd.init:131:21"
```

### Pattern

`^\s*PCAP_INTF\s\+`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:69961d9e2d8aec0ca65cd36c10b6fd6e:search

```yaml
regex_id: 69961d9e2d8aec0ca65cd36c10b6fd6e
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/nut/files/nut-server-config.sh.functions:163:5"
```

### Pattern

`^MODE=netclient`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6a80c2463a7b4b7932f1f8e67533c8a6:search

```yaml
regex_id: 6a80c2463a7b4b7932f1f8e67533c8a6
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/files/etc/init.d/pbr:3233:33"
```

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

## usage_mismatch:6d95291f5966ff68085087bf6fc687ab:search

```yaml
regex_id: 6d95291f5966ff68085087bf6fc687ab
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/ddns-scripts/files/usr/lib/ddns/dynamic_dns_functions.sh:1072:28"
```

### Pattern

`^Name:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6e387455b7fd46fa626bb55796a9f060:search

```yaml
regex_id: 6e387455b7fd46fa626bb55796a9f060
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/uacme/files/dnsapi_helper.sh:1135:14"
```

### Pattern

`^$_sdkey *=`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6ef467a9fa56cf22bdd33ec0f2c1e3f0:search

```yaml
regex_id: 6ef467a9fa56cf22bdd33ec0f2c1e3f0
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/mwan3/files/lib/mwan3/mwan3.sh:1151:37"
```

### Pattern

`.*--comment "out .*" .*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6f40090424ae5f6c4432232447156345:search

```yaml
regex_id: 6f40090424ae5f6c4432232447156345
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/tests/08_dns/01_nftset_element:65:8"
```

### Pattern

`^nftset=/example\.com/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:759e7ac64bd7e981a255c7d9802909e7:search

```yaml
regex_id: 759e7ac64bd7e981a255c7d9802909e7
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/nginx/files/nginx.init:29:2"
```

### Pattern

`^include module\.d/\*\.module;`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:78f2cb2cddff8573d39b223baebc4f00:search

```yaml
regex_id: 78f2cb2cddff8573d39b223baebc4f00
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/utils/apparmor/files/apparmor.sh:99:21"
```

### Pattern

`^.+\.new-[0-9\.]+_[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7d5e75204267d0074d4c05fb68007eb6:search

```yaml
regex_id: 7d5e75204267d0074d4c05fb68007eb6
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/strongswan/files/etc/uci-defaults/strongswan:18:10"
```

### Pattern

`^[[:space:]]*option ignore_routing_tables`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7d6db4758e59897717a37c7e2ad19d12:search

```yaml
regex_id: 7d6db4758e59897717a37c7e2ad19d12
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/uacme/files/dnsapi_helper.sh:1095:13"
```

### Pattern

`^$__opt$__sep`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7fa218a4742ee608988d47b42ac9afb3:search

```yaml
regex_id: 7fa218a4742ee608988d47b42ac9afb3
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/utils/fatresize/test.sh:5:30"
```

### Pattern

`^Please report bugs to mouse@ya.ru`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:81b27da8ee02cece3fd140b1037fa984:search

```yaml
regex_id: 81b27da8ee02cece3fd140b1037fa984
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/ddns-scripts/files/usr/lib/ddns/update_dnspod_cn_v3.sh:318:50"
```

### Pattern

`[^"]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:838691b478b33ff8b780eddfd96dbcff:search

```yaml
regex_id: 838691b478b33ff8b780eddfd96dbcff
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/ddns-scripts/files/usr/lib/ddns/dynamic_dns_functions.sh:1063:29"
```

### Pattern

`^$lookup_host`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:87ad2852871402689654d22e86f4adab:search

```yaml
regex_id: 87ad2852871402689654d22e86f4adab
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/radius-mac/files/radius-mac.init:38:23"
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

## usage_mismatch:87aebeb2afa60f79faa68b60b50cbdbb:search

```yaml
regex_id: 87aebeb2afa60f79faa68b60b50cbdbb
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/files/etc/init.d/pbr:2420:3"
```

### Pattern

`$\{ipTablePrefix}_$\{table_iface}\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:89889d22e1c2b2c9b1b5ab73b7434ed0:search

```yaml
regex_id: 89889d22e1c2b2c9b1b5ab73b7434ed0
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/utils/clixon/files/clixon.init:12:7"
```

### Pattern

`^   CLICON_XMLDB_DIR `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8c0b2586aa896ce0d0fa6434ca859ea0:search

```yaml
regex_id: 8c0b2586aa896ce0d0fa6434ca859ea0
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/dcwapd/files/dcwapd.init:17:41"
```

### Pattern

`=channel-set$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8c5ac8efa8f883d2e6a4b9b6eeed028d:search

```yaml
regex_id: 8c5ac8efa8f883d2e6a4b9b6eeed028d
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/mini_snmpd/files/mini_snmpd.init:172:97"
```

### Pattern

`with false$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8dce01b6e9fc1b951dc4e8d9329925bd:search

```yaml
regex_id: 8dce01b6e9fc1b951dc4e8d9329925bd
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/mwan3/files/lib/mwan3/mwan3.sh:744:34"
```

### Pattern

`^-A $policy`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8f56ff2f306b61d77c763c41ff64f747:search

```yaml
regex_id: 8f56ff2f306b61d77c763c41ff64f747
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pptpd/files/pptpd.init:65:1"
```

### Pattern

`^\w+\s+pptp-server\s+.+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9198236cff0beb0691ca465855086d76:search

```yaml
regex_id: 9198236cff0beb0691ca465855086d76
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/sound/mpc/files/pls-handler.sh:4:0"
```

### Pattern

`^File[0-9]*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:935bb8f427103e0d3e5f34fbf5bfffe2:search

```yaml
regex_id: 935bb8f427103e0d3e5f34fbf5bfffe2
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/adblock/files/95-adblock-housekeeping:58:34"
```

### Pattern

`^(wildcard/|domains/)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:96ce86b7c4a026168c4dd157a13e942c:search

```yaml
regex_id: 96ce86b7c4a026168c4dd157a13e942c
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/mwan3/files/etc/init.d/mwan3:80:32"
```

### Pattern

`^[1-3][0-9]{3}:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9c401ed1355cb857be70bb4a8e4fdf5f:search

```yaml
regex_id: 9c401ed1355cb857be70bb4a8e4fdf5f
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/uacme/files/dnsapi_helper.sh:1070:5"
```

### Pattern

`^$__opt$__sep`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9d01cccc367749928b4bc1b02381a446:search

```yaml
regex_id: 9d01cccc367749928b4bc1b02381a446
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/uacme/files/hook.sh:71:4"
```

### Pattern

`^$\{acme_server:-$staging}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9d9a2f788386533d7f9ef8ed2534538c:search

```yaml
regex_id: 9d9a2f788386533d7f9ef8ed2534538c
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/utils/parted/test.sh:5:34"
```

### Pattern

`^Copyright`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9e3613fda09a6a6d359ee95bfa772c7a:search

```yaml
regex_id: 9e3613fda09a6a6d359ee95bfa772c7a
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/ddns-scripts/files/usr/lib/ddns/dynamic_dns_functions.sh:824:42"
```

### Pattern

`^[0-9a-eA-E]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9fa95974f0ffa820f6fa8ebf81d23cf4:search

```yaml
regex_id: 9fa95974f0ffa820f6fa8ebf81d23cf4
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/radius-mac/files/radius-mac.init:67:23"
```

### Pattern

`^([0-9]{1,3}\.){3}[0-9]{1,3}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a07d633d031b9525eeb07fc71ef5117a:search

```yaml
regex_id: a07d633d031b9525eeb07fc71ef5117a
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/tests/lib/mocks/functions.sh:38:7"
```

### Pattern

`^option[[:space:]]+([^[:space:]]+)[[:space:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a81d73250cc5e287c7caa1080ebf1eb7:search

```yaml
regex_id: a81d73250cc5e287c7caa1080ebf1eb7
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/files/etc/init.d/pbr:1153:4"
```

### Pattern

`^nftset=/$\{escaped_param}/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a891525154f17b381aa7ebec96d30483:search

```yaml
regex_id: a891525154f17b381aa7ebec96d30483
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/files/etc/init.d/pbr:3269:18"
```

### Pattern

`^$\{tid}[[:space:]]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:aa10bfb0b018e2fd7b7da49e06e0601c:search

```yaml
regex_id: aa10bfb0b018e2fd7b7da49e06e0601c
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/tests/08_dns/01_nftset_element:62:13"
```

### Pattern

`^nftset=/example\.com/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:aa308f3c6af51ae339cf54f1203c027d:search

```yaml
regex_id: aa308f3c6af51ae339cf54f1203c027d
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/utils/sane-backends/files/saned.hotplug:6:0"
```

### Pattern

`^$SANE_GROUP:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ad0a79bf8d15e02085982389808a4168:search

```yaml
regex_id: ad0a79bf8d15e02085982389808a4168
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/aria2/files/aria2.init:313:1"
```

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

## usage_mismatch:baef6606324bcf302a21fd0927e42204:search

```yaml
regex_id: baef6606324bcf302a21fd0927e42204
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/lang/golang/golang-build.sh:65:77"
```

### Pattern

`^[[:space:]]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bbdcb97d95dcc8c735a763ad85c4e299:search

```yaml
regex_id: bbdcb97d95dcc8c735a763ad85c4e299
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/mwan3/files/lib/mwan3/mwan3.sh:655:20"
```

### Pattern

`^-A mwan3_policy_$policy.*--comment .* [0-9]* [0-9]*`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bd18b4b835e5343e762767eb245aad77:search

```yaml
regex_id: bd18b4b835e5343e762767eb245aad77
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/freeradius3/test.sh:20:2"
```

### Pattern

`^raddbdir`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:be411610d1d13f94014db34ac612c9d6:search

```yaml
regex_id: be411610d1d13f94014db34ac612c9d6
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/multimedia/imagemagick/test.sh:32:62"
```

### Pattern

`^255$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bf2ba51b45eb83dfdd39142a9bbb67f6:search

```yaml
regex_id: bf2ba51b45eb83dfdd39142a9bbb67f6
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/tests/08_dns/01_nftset_element:152:1"
```

### Pattern

`^nftset=/example\.com/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c35abf65485cd5a9a6f4bb5a3ab1a1a5:search

```yaml
regex_id: c35abf65485cd5a9a6f4bb5a3ab1a1a5
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/nginx-util/src/test-nginx-util-root.sh:131:21"
```

### Pattern

`^\s*ssl_session_cache\s`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c3bec82e737b988b695614c270232186:search

```yaml
regex_id: c3bec82e737b988b695614c270232186
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/libs/nacl/do-openwrt:105:38"
```

### Pattern

`\.c$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c78612768a6580254847bbd3eb68174a:search

```yaml
regex_id: c78612768a6580254847bbd3eb68174a
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/libs/postgresql/files/postgresql.init:11:1"
```

### Pattern

`localhost$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c7881f408f71b5296f9b10590e7622b4:search

```yaml
regex_id: c7881f408f71b5296f9b10590e7622b4
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/nginx/files/nginx.init:40:7"
```

### Pattern

`^include module\.d/\*\.module;$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c89844aca18196cc2684b920d54737c6:search

```yaml
regex_id: c89844aca18196cc2684b920d54737c6
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/tests/08_dns/01_nftset_element:29:13"
```

### Pattern

`^nftset=/example\.com/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c9af0a54f5e8e5198ecb01888d4ee7a4:search

```yaml
regex_id: c9af0a54f5e8e5198ecb01888d4ee7a4
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/banip/files/banip-functions.sh:2643:38"
```

### Pattern

`^([1-9][0-9]*(ms|s|m|h|d|w))+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ca8c0217e17113e6b8d50918df4d3e71:search

```yaml
regex_id: ca8c0217e17113e6b8d50918df4d3e71
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/tests/lib/mocks/functions.sh:32:5"
```

### Pattern

`^config[[:space:`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cce005d42804aecfa73dd4fd5e5f3cbd:search

```yaml
regex_id: cce005d42804aecfa73dd4fd5e5f3cbd
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/files/etc/init.d/pbr:385:26"
```

### Pattern

`^$\{1:--}`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cd0bb9173cbd41f5451a7e6cc83a42df:search

```yaml
regex_id: cd0bb9173cbd41f5451a7e6cc83a42df
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/files/etc/init.d/pbr:374:44"
```

### Pattern

`^([0-9A-Fa-f]{2}-){5}([0-9A-Fa-f]{2})$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cf7f440a393e52abeea5816e6e09e15d:search

```yaml
regex_id: cf7f440a393e52abeea5816e6e09e15d
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/tests/08_dns/01_nftset_element:135:8"
```

### Pattern

`^nftset=/example\.com/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d02e16f6f50375aa7321cbf1dc55ade7:search

```yaml
regex_id: d02e16f6f50375aa7321cbf1dc55ade7
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/lang/perl/files/perl-run_tests.sh:71:60"
```

### Pattern

`^t/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d2633fba922ff575e6ada67e8968eee1:search

```yaml
regex_id: d2633fba922ff575e6ada67e8968eee1
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/mwan3/files/lib/mwan3/mwan3.sh:1157:31"
```

### Pattern

`.*--comment "out .*" .*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d5fca924077f1f3dc553a493c8e8ed18:search

```yaml
regex_id: d5fca924077f1f3dc553a493c8e8ed18
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/files/etc/init.d/pbr:1145:6"
```

### Pattern

`^nftset=/$\{escaped_param}/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d71a8e47257159fbcb709d7484c50f91:search

```yaml
regex_id: d71a8e47257159fbcb709d7484c50f91
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/tests/lib/mocks/functions.sh:56:7"
```

### Pattern

`^list[[:space:]]+([^[:space:]]+)[[:space:]]+([^[:space:]]+)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d89b4ac865a81036473ebe3d99387cd1:search

```yaml
regex_id: d89b4ac865a81036473ebe3d99387cd1
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/open-iscsi/files/iscsi_offload:206:9"
```

### Pattern

`^$mod`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d98ece739a307a59d5023df8c4bc891d:search

```yaml
regex_id: d98ece739a307a59d5023df8c4bc891d
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/libs/valkey/files/valkey.init:48:2"
```

### Pattern

`^port|^bind|^dir|^logfile|^daemonize|^maxmemory|^save|^appendonly|^appendfilename`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:da810a131b67d111d5480356207d74d5:search

```yaml
regex_id: da810a131b67d111d5480356207d74d5
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/open-iscsi/files/iscsi_offload:201:9"
```

### Pattern

`^$mod`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:de13d16f668b285e91a1612bc1d87985:search

```yaml
regex_id: de13d16f668b285e91a1612bc1d87985
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/keepalived/files/usr/share/keepalived/scripts/rsync.sh:107:6"
```

### Pattern

`^$ssh_pubkey$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e3c9d9a8c0d36423a28b9fbef02dadc4:search

```yaml
regex_id: e3c9d9a8c0d36423a28b9fbef02dadc4
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/uacme/files/dnsapi_helper.sh:881:28"
```

### Pattern

`^[^ ][^ ]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e431bfef624f29c98ab32dec355f301d:search

```yaml
regex_id: e431bfef624f29c98ab32dec355f301d
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/tests/08_dns/01_nftset_element:99:8"
```

### Pattern

`^nftset=/example\.com/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e50bfe6229ea754b2ee5bd7f6e12a866:search

```yaml
regex_id: e50bfe6229ea754b2ee5bd7f6e12a866
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/sstp-client/files/lib/netifd/proto/sstp.sh:69:2"
```

### Pattern

`^$module `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e5719eb1c29689f67e898ccd32e99098:search

```yaml
regex_id: e5719eb1c29689f67e898ccd32e99098
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/dcwapd/files/dcwapd.init:136:27"
```

### Pattern

`^uci: `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e679796fabe624f5edd7175da7b81d4f:search

```yaml
regex_id: e679796fabe624f5edd7175da7b81d4f
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/bsbf-openwrt-resources/files/etc/hotplug.d/net/99-bsbf-autoconf-dhcp:7:25"
```

### Pattern

`^DRIVER=(cdc_ether|r8152|rndis_host|ipheth)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ea6d3b50fafc07b6bed1471db4e6728b:search

```yaml
regex_id: ea6d3b50fafc07b6bed1471db4e6728b
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/nut/files/nut-server-config.sh.functions:154:28"
```

### Pattern

`^MODE=none`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:eae7ae88223eacefa023f0a37fabec22:search

```yaml
regex_id: eae7ae88223eacefa023f0a37fabec22
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/ddns-scripts/files/usr/lib/ddns/update_cloudflare_com_v4.sh:245:50"
```

### Pattern

`[^"]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ebc0bcf83e2beb8681d5dddf4ca554c0:search

```yaml
regex_id: ebc0bcf83e2beb8681d5dddf4ca554c0
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/utils/hwdata/test.sh:6:2"
```

### Pattern

`^8086`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ecdf8537456e9e729759f6219eca26a3:search

```yaml
regex_id: ecdf8537456e9e729759f6219eca26a3
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/ddns-scripts/files/usr/lib/ddns/dynamic_dns_functions.sh:295:22"
```

### Pattern

`^http`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:eeba457d85018256ab4ab5ada6261fc2:search

```yaml
regex_id: eeba457d85018256ab4ab5ada6261fc2
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/nginx-util/src/test-nginx-util-root.sh:93:4"
```

### Pattern

`^\s*#UCI_HTTP_CONFIG\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f782e2e689859f8f4e3783b8eaff7305:search

```yaml
regex_id: f782e2e689859f8f4e3783b8eaff7305
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/files/etc/init.d/pbr:1144:3"
```

### Pattern

`^nftset=/${escaped_param}/.*#${safe_nftset4}(,| |$)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f87c1a06cb9b0d78749b8ce98ff7d1d2:search

```yaml
regex_id: f87c1a06cb9b0d78749b8ce98ff7d1d2
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/utils/librespeed-cli-rust/test.sh:9:30"
```

### Pattern

`^Timestamp,Server Name,Address,Ping,Jitter,Download,Upload,Share,IP$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f95a39521ca68ee730c9d70787f2060e:search

```yaml
regex_id: f95a39521ca68ee730c9d70787f2060e
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/ripe-atlas/test.sh:106:1"
```

### Pattern

`^REG_[0-9]+_HOST=[^[:space:]]`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f99ea0fd72f24a09b39614eeafc7e0ba:search

```yaml
regex_id: f99ea0fd72f24a09b39614eeafc7e0ba
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/pbr/tests/08_dns/01_nftset_element:149:13"
```

### Pattern

`^nftset=/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fb90f87f425d4de06100cac2a3ca9689:search

```yaml
regex_id: fb90f87f425d4de06100cac2a3ca9689
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/admin/rsyslog/files/20_rsyslog:3:0"
```

### Pattern

`^\s*#`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fed89239c21076e52e52b83066fe2f3f:search

```yaml
regex_id: fed89239c21076e52e52b83066fe2f3f
schema_version: "1"
kind: usage_mismatch
corpus: openwrt_packages
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/openwrt_packages/rules/net/netopeer2/files/netopeer2-server-setup.default:85:40"
```

### Pattern

`^$name +\|[^\|]*\| I`

### Context

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
corpus: openwrt_packages
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
corpus: openwrt_packages
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
corpus: openwrt_packages
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
corpus: openwrt_packages
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

---
schema_version: "1"
corpus: AegisMind
findings: 155
---

# AegisMind batch findings

## intent_mismatch:03c3b5e1a219879088665836636e18cb:email

```yaml
regex_id: 03c3b5e1a219879088665836636e18cb
schema_version: "1"
kind: intent_mismatch
corpus: AegisMind
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/Email_PHP_Mailer.yar:54:8"
```

### Pattern

`X-PHP-Filename: (\/[\w]+\/(.*\.php))?`

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

## usage_mismatch:03df311bb66c4d05c7229b49e501219d:search

```yaml
regex_id: 03df311bb66c4d05c7229b49e501219d
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/MALW_Miscelanea.yar:679:2"
```

### Pattern

`niB\.elcyceR\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0498480bfc2bb2dbff0e002a52a38570:search

```yaml
regex_id: 0498480bfc2bb2dbff0e002a52a38570
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/APT_Poseidon_Group.yar:38:8"
```

### Pattern

`\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-This_is_a_boundary\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:07c182eb737309be684884a922a52316:search

```yaml
regex_id: 07c182eb737309be684884a922a52316
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_ua_hermetic_wiper.yar:64:6"
```

### Pattern

`1>\ \\\\\\\\127\.0\.0\.1\\\\ADMIN\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:086405333950f39bf38e299166ef0ee9:search

```yaml
regex_id: 086405333950f39bf38e299166ef0ee9
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_hafnium.yar:114:6"
```

### Pattern

`=\(\[text\.encoding\]::ASCII\)\.GetBytes\(\(iex\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0d3cdd23107c452a07f4bfffe0195675:search

```yaml
regex_id: 0d3cdd23107c452a07f4bfffe0195675
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/gen_metasploit_payloads.yar:209:6"
```

### Pattern

`::VirtualAlloc\(0,\[Math\]::Max\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0f860ae6e213efb6ed3e6e7e3f3fe2ea:search

```yaml
regex_id: 0f860ae6e213efb6ed3e6e7e3f3fe2ea
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/thor-webshells.yar:4263:2"
```

### Pattern

`\ \$fileEditInfo\ =\ \\"\&nbsp;\&nbsp;:::::::\&nbsp;\&nbsp;Owner:\ <font\ color=\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:100486865753c353e4aee69d525be676:email

```yaml
regex_id: 100486865753c353e4aee69d525be676
schema_version: "1"
kind: intent_mismatch
corpus: AegisMind
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/TOOLKIT_FinFisher_.yar:16:8"
```

### Pattern

`(N)AME,EMAIL CLIENT,EMAIL ADDRESS,SERVER NAME,SERVER TYPE,USERNAME,PASSWORD,PROFILE`

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

## usage_mismatch:11fe404f74ce41f7027f860b4d7f762b:search

```yaml
regex_id: 11fe404f74ce41f7027f860b4d7f762b
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/thor-webshells.yar:9800:6"
```

### Pattern

`\)\.substr\(md5\(strrev\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:13bbe6e1e2b74c8e2748d7f745396140:search

```yaml
regex_id: 13bbe6e1e2b74c8e2748d7f745396140
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/RANSOM_Petya_MS17_010.yar:14:6"
```

### Pattern

`\\\\admin\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:15dc223c944b5388c82a766c5f2f8ac1:search

```yaml
regex_id: 15dc223c944b5388c82a766c5f2f8ac1
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/WShell_THOR_Webshells.yar:3813:2"
```

### Pattern

`\ \$fileEditInfo\ =\ \\"\&nbsp;\&nbsp;:::::::\&nbsp;\&nbsp;Owner:\ <font\ color=\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:16d2a66743fef3055a8a1d41d3053b00:search

```yaml
regex_id: 16d2a66743fef3055a8a1d41d3053b00
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/APT_KeyBoy.yar:41:8"
```

### Pattern

`\$shell\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:199debbfc1317c8603d0327972102b4e:email

```yaml
regex_id: 199debbfc1317c8603d0327972102b4e
schema_version: "1"
kind: intent_mismatch
corpus: AegisMind
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/TOOLKIT_FinFisher_.yar:86:8"
```

### Pattern

`(N)AME,EMAIL CLIENT,EMAIL ADDRESS,SERVER NAME,SERVER TYPE,USERNAME,PASSWORD,PROFILE`

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

## usage_mismatch:1c11b3dda19bab6c0f3fa38b07929f66:search

```yaml
regex_id: 1c11b3dda19bab6c0f3fa38b07929f66
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/gen_webshells.yar:887:8"
```

### Pattern

`^<\?php \$[a-z]{3,30} = '`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1d6867ce129a1e584091047de77c270c:search

```yaml
regex_id: 1d6867ce129a1e584091047de77c270c
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/gen_gcti_cobaltstrike.yar:1057:6"
```

### Pattern

`[A-Za-z]{1020}.{4}$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:203e4a424d6043cd39f64dacb75f67bb:search

```yaml
regex_id: 203e4a424d6043cd39f64dacb75f67bb
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/WShell_THOR_Webshells.yar:6872:2"
```

### Pattern

`\$Info:\ This\ file\ is\ packed\ with\ the\ UPX\ executable\ packer\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:21ac807f62a983dea7a3625ff2bf10d0:email

```yaml
regex_id: 21ac807f62a983dea7a3625ff2bf10d0
schema_version: "1"
kind: intent_mismatch
corpus: AegisMind
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/TOOLKIT_FinFisher_.yar:17:8"
```

### Pattern

`\/scomma excel2010\.part`

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

## intent_mismatch:2339dd640add5fceac16f6c0bb749233:email

```yaml
regex_id: 2339dd640add5fceac16f6c0bb749233
schema_version: "1"
kind: intent_mismatch
corpus: AegisMind
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/expl_proxyshell.yar:12:6"
```

### Pattern

`Email=autodiscover\/autodiscover\.json[^\n]{1,400}401 0 0`

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

## usage_mismatch:275a5364f2b51420a502c1900bd6d137:search

```yaml
regex_id: 275a5364f2b51420a502c1900bd6d137
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/APT_KeyBoy.yar:44:8"
```

### Pattern

`\$fileUpload\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:28f8e8142e396f20728aca82dfce5fd9:search

```yaml
regex_id: 28f8e8142e396f20728aca82dfce5fd9
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_cn_pp_zerot.yar:54:6"
```

### Pattern

`\*\ \$l\&\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:2bca7eede839b4259b6a7f7897bf3d44:email

```yaml
regex_id: 2bca7eede839b4259b6a7f7897bf3d44
schema_version: "1"
kind: intent_mismatch
corpus: AegisMind
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/TOOLKIT_FinFisher_.yar:15:8"
```

### Pattern

`\/scomma kbd101\.sys`

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

## intent_mismatch:2ce27a2ff7d6175dca861aa6f52de3b3:email

```yaml
regex_id: 2ce27a2ff7d6175dca861aa6f52de3b3
schema_version: "1"
kind: intent_mismatch
corpus: AegisMind
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/Email_PHP_Mailer.yar:53:8"
```

### Pattern

`X-PHP-Script: ([\w\.\/]+\/(.*\.php))?`

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

## usage_mismatch:2d31f91c30a133e4dc1b7bad1370da3b:search

```yaml
regex_id: 2d31f91c30a133e4dc1b7bad1370da3b
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_ua_hermetic_wiper.yar:84:6"
```

### Pattern

`postgresql\.exe\ 1>\ \\\\\\\\127\.0\.0\.1\\\\ADMIN\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2de54d2d48ffcffd2ccbb66035ac67e3:search

```yaml
regex_id: 2de54d2d48ffcffd2ccbb66035ac67e3
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/thor-webshells.yar:9717:6"
```

### Pattern

`global\$auth;return\ sh_decrypt_phase\(sh_decrypt_phase\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:2ea5f44a18cb47cba9bfe90da6fa495d:email

```yaml
regex_id: 2ea5f44a18cb47cba9bfe90da6fa495d
schema_version: "1"
kind: intent_mismatch
corpus: AegisMind
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/TOOLKIT_FinFisher_.yar:85:8"
```

### Pattern

`\/scomma kbd101\.sys`

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

## usage_mismatch:30de48bb812c0346d12e6dd1479b43a4:search

```yaml
regex_id: 30de48bb812c0346d12e6dd1479b43a4
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/thor-webshells.yar:7227:2"
```

### Pattern

`\$Info:\ This\ file\ is\ packed\ with\ the\ UPX\ executable\ packer\ http://upx\.tsx\.org\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:317fbe779d988bb72bf729626bf61427:search

```yaml
regex_id: 317fbe779d988bb72bf729626bf61427
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/gen_webshells.yar:1269:8"
```

### Pattern

`\]\.\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:321f23cfa7361bc754523dd7e9e76e6d:search

```yaml
regex_id: 321f23cfa7361bc754523dd7e9e76e6d
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/gen_webshells.yar:2611:8"
```

### Pattern

`extract\(\$_REQUEST\)\&\&@\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:35a5d3aa0dfae4d65deee1a435416a77:search

```yaml
regex_id: 35a5d3aa0dfae4d65deee1a435416a77
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/APT_Snowglobe_Babar.yar:32:8"
```

### Pattern

`CONOUT\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:3b112035d8712d61c27f150bfffd4143:email

```yaml
regex_id: 3b112035d8712d61c27f150bfffd4143
schema_version: "1"
kind: intent_mismatch
corpus: AegisMind
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/Email_PHP_Mailer.yar:52:8"
```

### Pattern

`X-PHP-Originating-Script: ([\w\.]+(.*\.php))?`

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

## intent_mismatch:42b220989336ef249e58afe5973b7a23:hostname

```yaml
regex_id: 42b220989336ef249e58afe5973b7a23
schema_version: "1"
kind: intent_mismatch
corpus: AegisMind
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/TOOLKIT_Chinese_Hacktools.yar:1874:2"
```

### Pattern

`@members\.3322\.net/dyndns/update\?system=dyndns\&hostname=`

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

## usage_mismatch:43aa132d94c979d0492186e3f4625666:search

```yaml
regex_id: 43aa132d94c979d0492186e3f4625666
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_hafnium.yar:114:6"
```

### Pattern

`=\(\[text\.encoding\]::ASCII\)\.GetBytes\(\(iex\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:43b0173d2f9c83fc728dd73966b2ce81:search

```yaml
regex_id: 43b0173d2f9c83fc728dd73966b2ce81
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_ua_hermetic_wiper.yar:84:6"
```

### Pattern

`postgresql\.exe\ 1>\ \\\\\\\\127\.0\.0\.1\\\\ADMIN\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4546ebff2723e70e0cea3ff115adfd61:search

```yaml
regex_id: 4546ebff2723e70e0cea3ff115adfd61
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_apt30_backspace.yar:157:2"
```

### Pattern

`\$LDDATA\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:49b6abf0da78f66d3afa34eb52b64b1f:search

```yaml
regex_id: 49b6abf0da78f66d3afa34eb52b64b1f
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/thor-webshells.yar:3680:2"
```

### Pattern

`echo\ \\"Command\ :\ <INPUT\ TYPE=text\ NAME=cmd\ value=\\"\.@stripslashes\(htmlentities\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:49defe21439a61598c9c174efaa1c5fa:search

```yaml
regex_id: 49defe21439a61598c9c174efaa1c5fa
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_ta18_149A.yar:23:6"
```

### Pattern

`cmd\.exe\ /q\ /c\ net\ share\ adnim\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4b6cae37024f5452c3840576e6b4204e:search

```yaml
regex_id: 4b6cae37024f5452c3840576e6b4204e
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/crime_malware_generic.yar:16:2"
```

### Pattern

`CONIN\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4c2c54f7dae5a1dd0e439139852e3576:search

```yaml
regex_id: 4c2c54f7dae5a1dd0e439139852e3576
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/APT_KeyBoy.yar:40:8"
```

### Pattern

`\$sysinfo\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:50798ad76774dfaa8240e1b35ebf7a3b:search

```yaml
regex_id: 50798ad76774dfaa8240e1b35ebf7a3b
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_fin7_backdoor.yar:25:6"
```

### Pattern

`Scripting\.FileSystemObject\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:5646bbc9ee2048bcd7d66cb167335dae:hostname

```yaml
regex_id: 5646bbc9ee2048bcd7d66cb167335dae
schema_version: "1"
kind: intent_mismatch
corpus: AegisMind
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/TOOLKIT_Chinese_Hacktools.yar:1876:2"
```

### Pattern

`@ddns\.oray\.com/ph/update\?hostname=`

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

## intent_mismatch:564a3b65a41296f3da80621ad99ee645:hostname

```yaml
regex_id: 564a3b65a41296f3da80621ad99ee645
schema_version: "1"
kind: intent_mismatch
corpus: AegisMind
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/gen_cn_hacktools.yar:2061:2"
```

### Pattern

`@ddns\.oray\.com/ph/update\?hostname=`

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

## intent_mismatch:57dbba975514cf49972e57acb22c85c1:email

```yaml
regex_id: 57dbba975514cf49972e57acb22c85c1
schema_version: "1"
kind: intent_mismatch
corpus: AegisMind
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/TOOLKIT_FinFisher_.yar:86:8"
```

### Pattern

`(N)AME,EMAIL CLIENT,EMAIL ADDRESS,SERVER NAME,SERVER TYPE,USERNAME,PASSWORD,PROFILE`

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

## usage_mismatch:58fc2a93e3ca49e72d9b16c9396dfa32:search

```yaml
regex_id: 58fc2a93e3ca49e72d9b16c9396dfa32
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_apt30_backspace.yar:672:2"
```

### Pattern

`\\\\driver32\\\\7\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5ba0fb8e4a8956ac4aad117c064ee0a3:search

```yaml
regex_id: 5ba0fb8e4a8956ac4aad117c064ee0a3
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/MALW_Hsdfihdf_banking.yar:28:1"
```

### Pattern

`zv7,'\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5f0ecf026579c7ecf6d33a079840bbc0:search

```yaml
regex_id: 5f0ecf026579c7ecf6d33a079840bbc0
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/RAT_PoisonIvy.yar:39:2"
```

### Pattern

`CONOUT\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:5fa5b16d3373fabf950a73c82917f04a:search

```yaml
regex_id: 5fa5b16d3373fabf950a73c82917f04a
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/APT_APT29_Grizzly_Steppe.yar:92:6"
```

### Pattern

`\(strrev\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:60d9084387c199251f87df3853017fe7:search

```yaml
regex_id: 60d9084387c199251f87df3853017fe7
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/thor-hacktools.yar:2954:6"
```

### Pattern

`WScript\.Echo\ \\"\ \ \ \$\$\\\\\ \ \ \ \ \ \$\$\\\\\ \$\$\\\\\ \ \ \ \ \ \$\$\\\\\ \$\$\$\$\$\$\\\\\ \$\$\$\$\$\$\$\$\\\\\ \$\$\\\\\ \ \ \$\$\\\\\ \$\$\$\$\$\$\$\$\\\\\ \ \$\$\$\$\$\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:62176cff30b707a6aea6d05885492644:search

```yaml
regex_id: 62176cff30b707a6aea6d05885492644
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/RANSOM_Petya_MS17_010.yar:14:6"
```

### Pattern

`\\\\admin\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:689edb00be57c2c3cde8b5c52559b32d:search

```yaml
regex_id: 689edb00be57c2c3cde8b5c52559b32d
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/gen_enigma_protector.yar:19:6"
```

### Pattern

`P\.rel\$oc\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:68c520fe3a446a692c7763d319cf7646:search

```yaml
regex_id: 68c520fe3a446a692c7763d319cf7646
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_pulsesecure.yar:185:8"
```

### Pattern

`syswrite\(\*fd,[\x09\x20]{0,32}[\x22\x27]realm=\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:68d106f66c5945d5a663afd6d2ece164:search

```yaml
regex_id: 68d106f66c5945d5a663afd6d2ece164
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/WShell_THOR_Webshells.yar:7335:2"
```

### Pattern

`\$Info:\ This\ file\ is\ packed\ with\ the\ UPX\ executable\ packer\ http://upx\.tsx\.org\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:68e0b2db0df42c06b046f80bd73f3411:search

```yaml
regex_id: 68e0b2db0df42c06b046f80bd73f3411
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/thor-webshells.yar:9864:6"
```

### Pattern

`\\";@eval\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6982edc06cadabdd8e52ffb2ae239d6d:search

```yaml
regex_id: 6982edc06cadabdd8e52ffb2ae239d6d
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/crime_wannacry.yar:35:6"
```

### Pattern

`\\\\\\\\192\.168\.56\.20\\\\IPC\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:6b9e7e668739df089b75075119a46bf6:email

```yaml
regex_id: 6b9e7e668739df089b75075119a46bf6
schema_version: "1"
kind: intent_mismatch
corpus: AegisMind
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/TOOLKIT_FinFisher_.yar:16:8"
```

### Pattern

`(N)AME,EMAIL CLIENT,EMAIL ADDRESS,SERVER NAME,SERVER TYPE,USERNAME,PASSWORD,PROFILE`

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

## usage_mismatch:6bb08311b71ca0f96c623f9b76e1b52d:search

```yaml
regex_id: 6bb08311b71ca0f96c623f9b76e1b52d
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/APT_Derusbi.yar:263:8"
```

### Pattern

`Wrod\-\-\$\$\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6c4393794c24e7ac8d5577c10340a74f:search

```yaml
regex_id: 6c4393794c24e7ac8d5577c10340a74f
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_apt30_backspace.yar:911:6"
```

### Pattern

`\$LDDATA\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:700e87abf5d6d5b618698e4a65509b12:search

```yaml
regex_id: 700e87abf5d6d5b618698e4a65509b12
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/WShell_THOR_Webshells.yar:621:2"
```

### Pattern

`echo\ \\"\ <font\ color='\#0000FF'>CHMODU\ \\"\.substr\(base_convert\(@fileperms\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:70d654c9c9a626ca10300a41f22815c8:hostname

```yaml
regex_id: 70d654c9c9a626ca10300a41f22815c8
schema_version: "1"
kind: intent_mismatch
corpus: AegisMind
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/gen_cn_hacktools.yar:2059:2"
```

### Pattern

`@members\.3322\.net/dyndns/update\?system=dyndns\&hostname=`

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

## usage_mismatch:74e615ff2085461e8bccdcf1375b1d18:search

```yaml
regex_id: 74e615ff2085461e8bccdcf1375b1d18
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/WShell_PHP_in_images.yar:12:8"
```

### Pattern

`^GIF8[79]a`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:750df4325374c29fb3f00d89573e068e:search

```yaml
regex_id: 750df4325374c29fb3f00d89573e068e
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/APT_ThreatGroup3390.yar:38:8"
```

### Pattern

`@CONOUT\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:76282ec50fd95ef0f500ca8f6b85ae4f:search

```yaml
regex_id: 76282ec50fd95ef0f500ca8f6b85ae4f
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/gen_webshells.yar:2500:8"
```

### Pattern

`echo[\t ]{0,500}\(?`\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7680277ca4f3ea8fb371ee5c9f0ae63e:search

```yaml
regex_id: 7680277ca4f3ea8fb371ee5c9f0ae63e
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/WShell_THOR_Webshells.yar:1880:2"
```

### Pattern

`if\(eregi\('WHERE\|LIMIT',\$_POST\['nsql'\]\)\ \&\&\ eregi\('SELECT\|FROM',\$_POST\['nsql'\]\)\)\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:78a9d426b324f7724f162d55d89bb966:email

```yaml
regex_id: 78a9d426b324f7724f162d55d89bb966
schema_version: "1"
kind: intent_mismatch
corpus: AegisMind
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/expl_proxyshell.yar:29:6"
```

### Pattern

`autodiscover\/autodiscover\.json[^\n]{1,60}&X-Rps-CAT=`

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

## usage_mismatch:79949aca0ac13b551a2b030b7a02b943:search

```yaml
regex_id: 79949aca0ac13b551a2b030b7a02b943
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/thor-webshells.yar:722:2"
```

### Pattern

`echo\ \\"\ <font\ color='\#0000FF'>CHMODU\ \\"\.substr\(base_convert\(@fileperms\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7c25aadaf94850b03774815f0aa07aa7:search

```yaml
regex_id: 7c25aadaf94850b03774815f0aa07aa7
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/APT_Passcv.yar:158:6"
```

### Pattern

`admin\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7c2854f539aa993d0032f793e309c7fb:search

```yaml
regex_id: 7c2854f539aa993d0032f793e309c7fb
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_unc2447_sombrat.yar:115:6"
```

### Pattern

`\[Runtime\.InteropServices\.Marshal\]::Copy\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:7eb5b812544c9001d6998a97f50683a7:email

```yaml
regex_id: 7eb5b812544c9001d6998a97f50683a7
schema_version: "1"
kind: intent_mismatch
corpus: AegisMind
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/expl_proxyshell.yar:11:6"
```

### Pattern

` \/autodiscover\/autodiscover\.json[^\n]{1,300}\/(powershell|mapi\/nspi|EWS\/|X-Rps-CAT)[^\n]{1,400}401 0 0`

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

## usage_mismatch:7f26aa3171edfa7dbb20e964463b82d9:search

```yaml
regex_id: 7f26aa3171edfa7dbb20e964463b82d9
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/WShell_THOR_Webshells.yar:6262:2"
```

### Pattern

`\$_REQUEST\['command'\]\ =\ \$aliases\[\$token\]\ \.\ substr\(\$_REQUEST\['command'\],\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:7fa50282726d28737268d16984e787b6:search

```yaml
regex_id: 7fa50282726d28737268d16984e787b6
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_ua_hermetic_wiper.yar:64:6"
```

### Pattern

`1>\ \\\\\\\\127\.0\.0\.1\\\\ADMIN\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:81157599d3be13ee6fbdc5e61d928846:search

```yaml
regex_id: 81157599d3be13ee6fbdc5e61d928846
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_cn_brickstorm_sep25.yar:140:6"
```

### Pattern

`abcdABCD1234!@\#\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:829e1e9b006e4af108a135df9681a9f1:search

```yaml
regex_id: 829e1e9b006e4af108a135df9681a9f1
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/gen_webshells.yar:2611:8"
```

### Pattern

`extract\(\$_REQUEST\)\&\&@\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8525f70626f9623db4dcf5f880a4f40e:search

```yaml
regex_id: 8525f70626f9623db4dcf5f880a4f40e
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/thor-webshells.yar:8140:2"
```

### Pattern

`\$Info:\ This\ file\ is\ packed\ with\ the\ UPX\ executable\ packer\ http://upx\.tsx\.org\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:877d27eb8660240b6c352c155f4c6779:search

```yaml
regex_id: 877d27eb8660240b6c352c155f4c6779
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/MALW_Miscelanea.yar:137:2"
```

### Pattern

`CONIN\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8811f887e55d1d7c09f60d0a3b7ecf51:search

```yaml
regex_id: 8811f887e55d1d7c09f60d0a3b7ecf51
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_oilrig_rgdoor.yar:31:6"
```

### Pattern

`download\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:897bf1e43f412fc6ddf971f9c804e1b2:search

```yaml
regex_id: 897bf1e43f412fc6ddf971f9c804e1b2
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/APT_Derusbi.yar:318:8"
```

### Pattern

`Wrod\-\-\$\$\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8a76fb83def031213bdfbebc7c0e2006:search

```yaml
regex_id: 8a76fb83def031213bdfbebc7c0e2006
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/WShell_THOR_Webshells.yar:3274:2"
```

### Pattern

`echo\ \\"Command\ :\ <INPUT\ TYPE=text\ NAME=cmd\ value=\\"\.@stripslashes\(htmlentities\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:8d993faca250b0c040469144aaf7407b:email

```yaml
regex_id: 8d993faca250b0c040469144aaf7407b
schema_version: "1"
kind: intent_mismatch
corpus: AegisMind
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/TOOLKIT_FinFisher_.yar:85:8"
```

### Pattern

`\/scomma kbd101\.sys`

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

## usage_mismatch:8dd7029792e3cc04cda9956ffb28940d:search

```yaml
regex_id: 8dd7029792e3cc04cda9956ffb28940d
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/gen_metasploit_payloads.yar:96:6"
```

### Pattern

`\.func\]::CreateThread\(0,0,\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8fed2d48ea0f59a844d13bb68511cf59:search

```yaml
regex_id: 8fed2d48ea0f59a844d13bb68511cf59
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/APT_APT29_Grizzly_Steppe.yar:109:6"
```

### Pattern

`<\?php\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:902d8d9846fc202b79b50412f86c885b:search

```yaml
regex_id: 902d8d9846fc202b79b50412f86c885b
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/gen_metasploit_payloads.yar:212:6"
```

### Pattern

`::memset\(\[IntPtr\]\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9209798e5395acc57801b04f0e7c684d:search

```yaml
regex_id: 9209798e5395acc57801b04f0e7c684d
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_apt29_nobelium_may21.yar:142:6"
```

### Pattern

`\]::FromBase64String\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:92c0dad14923cdc57803878969c5886b:search

```yaml
regex_id: 92c0dad14923cdc57803878969c5886b
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_poisonivy_gen3.yar:18:2"
```

### Pattern

`CONOUT\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9877c73928d1c5f21d06c9cd7ddacdc0:search

```yaml
regex_id: 9877c73928d1c5f21d06c9cd7ddacdc0
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_pulsesecure.yar:24:8"
```

### Pattern

`if[\x09\x20]{0,32}\(CGI::param\([\x22\x27]\w{1,64}[\x22\x27]\)\)\s{0,128}\{[\x09\x20]{0,32}print [\x22\x27]Cache-Control: no-cache\\n[\x22\x27][\x09\x20]{0,32};\s{0,128}print [\x22\x27]Content-type: text\/html\\n\\n[\x22\x27][\x09\x20]{0,32};\s{0,128}my \$\w{1,64}[\x09\x20]{0,32}=[\x09\x20]{0,32}CGI::param\([\x22\x27]\w{1,64}[\x22\x27]\)[\x09\x20]{0,32};\s{0,128}system\([\x22\x27]\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9b4e71096709bb36c0f8b63390c34a50:search

```yaml
regex_id: 9b4e71096709bb36c0f8b63390c34a50
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/gen_transformed_strings.yar:49:2"
```

### Pattern

`niB\.elcyceR\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9bda75d00c37cc0d68924f198336fa94:search

```yaml
regex_id: 9bda75d00c37cc0d68924f198336fa94
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/mal_perfctl_oct24.yar:15:6"
```

### Pattern

`\.EYE\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9d61c5eb29159e5301554e71673600ef:search

```yaml
regex_id: 9d61c5eb29159e5301554e71673600ef
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/thor-webshells.yar:8418:2"
```

### Pattern

`\$Info:\ This\ file\ is\ packed\ with\ the\ UPX\ executable\ packer\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9dd56dd709fecbd681f8b72a67e792af:search

```yaml
regex_id: 9dd56dd709fecbd681f8b72a67e792af
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/thor-webshells.yar:7234:2"
```

### Pattern

`\$Id:\ UPX\ 1\.07\ Copyright\ \(C\)\ 1996\-2001\ the\ UPX\ Team\.\ All\ Rights\ Reserved\.\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a30b60ca74ca7182baa4c63a8de4f5ce:search

```yaml
regex_id: a30b60ca74ca7182baa4c63a8de4f5ce
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_unc2447_sombrat.yar:115:6"
```

### Pattern

`\[Runtime\.InteropServices\.Marshal\]::Copy\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a498e364fcd8631ce820cc851bee06db:search

```yaml
regex_id: a498e364fcd8631ce820cc851bee06db
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_report_ivanti_mandiant_jan24.yar:76:4"
```

### Pattern

`;eval\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a52dd8cbccecb5707763637c17d80073:search

```yaml
regex_id: a52dd8cbccecb5707763637c17d80073
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/cn_pentestset_webshells.yar:20:2"
```

### Pattern

`echo\ sr\(35,in\('hidden','dir',0,\$dir\)\.in\('hidden','cmd',0,'mysql_dump'\)\.\\"<b>\\"\.\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a6016e540279e6c056854f3f84d44491:search

```yaml
regex_id: a6016e540279e6c056854f3f84d44491
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_sandworm_exim_expl.yar:96:6"
```

### Pattern

`GIF89a\ <\?php\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:aa6489434fd6c834a15f3184e1049cfb:search

```yaml
regex_id: aa6489434fd6c834a15f3184e1049cfb
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_op_cleaver.yar:232:2"
```

### Pattern

`LAST_TIME=00/00/0000:00:00PM\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ad6689565fe646acc1bfc949d72a255d:search

```yaml
regex_id: ad6689565fe646acc1bfc949d72a255d
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/gen_webshells.yar:887:8"
```

### Pattern

`^<\?php \$[a-z]{3,30} = '`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ae05bd7226b7264cdfe59681e02de9f5:search

```yaml
regex_id: ae05bd7226b7264cdfe59681e02de9f5
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/thor-webshells.yar:106:2"
```

### Pattern

`if\ \(\$l\)\ echo\ '<a\ href=\\"'\ \.\ \$self\ \.\ '\?action=permission\&amp;file='\ \.\ urlencode\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:aeba7a886149f06269196957b8bb8f7f:search

```yaml
regex_id: aeba7a886149f06269196957b8bb8f7f
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/TOOLKIT_THOR_HackTools.yar:2775:2"
```

### Pattern

`WScript\.Echo\ \\"\ \ \ \$\$\\\\\ \ \ \ \ \ \$\$\\\\\ \$\$\\\\\ \ \ \ \ \ \$\$\\\\\ \$\$\$\$\$\$\\\\\ \$\$\$\$\$\$\$\$\\\\\ \$\$\\\\\ \ \ \$\$\\\\\ \$\$\$\$\$\$\$\$\\\\\ \ \$\$\$\$\$\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:af21cf442719f6c0f20f76ce6846311e:search

```yaml
regex_id: af21cf442719f6c0f20f76ce6846311e
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/WShell_THOR_Webshells.yar:89:2"
```

### Pattern

`if\ \(\$l\)\ echo\ '<a\ href=\\"'\ \.\ \$self\ \.\ '\?action=permission\&amp;file='\ \.\ urlencode\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b4e28471f01c031ae7a00919886044ea:search

```yaml
regex_id: b4e28471f01c031ae7a00919886044ea
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/gen_powershell_toolkit.yar:197:2"
```

### Pattern

`Write\-Warning\ \\"\[!\]\ Access\ to\ service\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b5042429692b83d49a4cf30ab02f99b1:search

```yaml
regex_id: b5042429692b83d49a4cf30ab02f99b1
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_apt30_backspace.yar:831:2"
```

### Pattern

`\\\\\$NtUninstallKB570317\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b53a8fdb454cfa13243b6b414bf4c156:search

```yaml
regex_id: b53a8fdb454cfa13243b6b414bf4c156
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/thor-webshells.yar:7606:2"
```

### Pattern

`\$Info:\ This\ file\ is\ packed\ with\ the\ UPX\ executable\ packer\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b5ff890c5e1bace637986892c61ac8bd:search

```yaml
regex_id: b5ff890c5e1bace637986892c61ac8bd
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/gen_hktl_koh_tokenstealer.yar:14:8"
```

### Pattern

`0x\[0\-9A\-Fa\-f\]\+\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:b71713df50ce601101e477ca28c9faf4:search

```yaml
regex_id: b71713df50ce601101e477ca28c9faf4
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_apt30_backspace.yar:1248:2"
```

### Pattern

`%s\\\\%s\\\\\$NtRecDoc\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bb4239c4fb41308346bb802fd9bf116e:search

```yaml
regex_id: bb4239c4fb41308346bb802fd9bf116e
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/gen_susp_obfuscation.yar:14:6"
```

### Pattern

`Microsoft\ Azure\ Code\ Signp\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bbece3260777ae9792e27714b52cef36:search

```yaml
regex_id: bbece3260777ae9792e27714b52cef36
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/WShell_THOR_Webshells.yar:50:2"
```

### Pattern

`<INPUT\ TYPE=\\"text\\"\ NAME=\\"cmd\\"\ value=\\"<\?php\ echo\ stripslashes\(htmlentities\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bc15e686bbac0a5546dc40b2843c9a30:search

```yaml
regex_id: bc15e686bbac0a5546dc40b2843c9a30
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/gen_webshells.yar:2605:8"
```

### Pattern

`\\neval\(htmlspecialchars_decode\(gzinflate\(base64_decode\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:be0c2231a2d317505e66011ddd082caf:search

```yaml
regex_id: be0c2231a2d317505e66011ddd082caf
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/MALW_AlMashreq.yar:21:1"
```

### Pattern

`^Try Run$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:be98e1aa73fe2f806d78d9ac0ff81311:search

```yaml
regex_id: be98e1aa73fe2f806d78d9ac0ff81311
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/APT_eqgrp_apr17.yar:2120:6"
```

### Pattern

`By\ default,\ the\ shellcode\ will\ attempt\ to\ immediately\ connect\ s\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bef6d5c24486b4653f7c98afdbda4fec:search

```yaml
regex_id: bef6d5c24486b4653f7c98afdbda4fec
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/bkdr_xz_util_cve_2024_3094.yar:71:6"
```

### Pattern

`eval\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bfca4ead1588e78d1ae246bdacab0e09:search

```yaml
regex_id: bfca4ead1588e78d1ae246bdacab0e09
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_threatgroup_3390.yar:33:2"
```

### Pattern

`@CONOUT\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c0b98607c9eb163a64b026a3917203e4:search

```yaml
regex_id: c0b98607c9eb163a64b026a3917203e4
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/APT_Regin.yar:341:8"
```

### Pattern

`%S\\\\ipc\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c1a06d98d76ebe20e9110b3b212598ee:search

```yaml
regex_id: c1a06d98d76ebe20e9110b3b212598ee
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_pulsesecure.yar:278:8"
```

### Pattern

`MIME::Base64::encode\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c337f6aa9f90470ac3ece877cdf9f6a1:search

```yaml
regex_id: c337f6aa9f90470ac3ece877cdf9f6a1
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_apt30_backspace.yar:741:2"
```

### Pattern

`\$NtRND1\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c372953115cc66783ca02ae4d13f7a2a:search

```yaml
regex_id: c372953115cc66783ca02ae4d13f7a2a
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/APT_Industroyer.yar:87:6"
```

### Pattern

`\^\(\.\+\?\.exe\)\.\*\\\\s\+\-ip\\\\s\*=\\\\s\*\(\.\+\)\\\\s\+\-ports\\\\s\*=\\\\s\*\(\.\+\)\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c6d499875944eb15f0e23b1475da42c7:search

```yaml
regex_id: c6d499875944eb15f0e23b1475da42c7
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/RANSOM_MS17-010_Wannacrypt.yar:173:6"
```

### Pattern

`\\\\\\\\172\.16\.99\.5\\\\IPC\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c8ab0521159afe12d24b8c6be57679cd:search

```yaml
regex_id: c8ab0521159afe12d24b8c6be57679cd
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_apt29_nobelium_may21.yar:142:6"
```

### Pattern

`\]::FromBase64String\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:cb626155e4d492b9cf19bb978ed14bc1:email

```yaml
regex_id: cb626155e4d492b9cf19bb978ed14bc1
schema_version: "1"
kind: intent_mismatch
corpus: AegisMind
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/TOOLKIT_FinFisher_.yar:87:8"
```

### Pattern

`\/scomma excel2010\.part`

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

## usage_mismatch:cddcebfaa2d7c290a308789377076014:search

```yaml
regex_id: cddcebfaa2d7c290a308789377076014
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_pulsesecure.yar:187:8"
```

### Pattern

`syswrite\(\*fd,[\x09\x20]{0,32}[\x22\x27]password=\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:ce7f49abc7a517ff5141f723ccb494da:email

```yaml
regex_id: ce7f49abc7a517ff5141f723ccb494da
schema_version: "1"
kind: intent_mismatch
corpus: AegisMind
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/Email_PHP_Mailer.yar:55:11"
```

### Pattern

`X-Source-Args: (\/[\w]+\/(.*\.php))?`

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

## usage_mismatch:ced849872dbe1b0b7fcdee6d81f547f4:search

```yaml
regex_id: ced849872dbe1b0b7fcdee6d81f547f4
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/thor-webshells.yar:9801:6"
```

### Pattern

`\]\)\)%256\);\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:cfd5b9976969d26e74d96bbe6c6ed694:search

```yaml
regex_id: cfd5b9976969d26e74d96bbe6c6ed694
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/APT_Derusbi.yar:281:8"
```

### Pattern

`PS1=RK\#\ \\\\u@\\\\h:\\\\w\ \\\\\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:d0ae1eb0afdf6ecdcd707580829bcd75:email

```yaml
regex_id: d0ae1eb0afdf6ecdcd707580829bcd75
schema_version: "1"
kind: intent_mismatch
corpus: AegisMind
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/TOOLKIT_FinFisher_.yar:15:8"
```

### Pattern

`\/scomma kbd101\.sys`

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

## usage_mismatch:d1060e9add8d430d13c0c53ed4b9b6ca:search

```yaml
regex_id: d1060e9add8d430d13c0c53ed4b9b6ca
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/spy_regin_fiveeyes.yar:335:5"
```

### Pattern

`%S\\\\ipc\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d4d08e211bd9eb046c5673406790c54c:search

```yaml
regex_id: d4d08e211bd9eb046c5673406790c54c
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/APT_APT29_Grizzly_Steppe.yar:89:6"
```

### Pattern

`<\?php\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d68deb56ec2718bfcc876d1c9765f01c:search

```yaml
regex_id: d68deb56ec2718bfcc876d1c9765f01c
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/APT_KeyBoy.yar:43:8"
```

### Pattern

`\$fileDownload\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d6afa940c3c0f83b994e825d8df60a32:search

```yaml
regex_id: d6afa940c3c0f83b994e825d8df60a32
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_apt30_backspace.yar:904:6"
```

### Pattern

`\$\.DATA\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d779b1a73ae0a3c023d31ede9a9deba5:search

```yaml
regex_id: d779b1a73ae0a3c023d31ede9a9deba5
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_hafnium.yar:115:6"
```

### Pattern

`\.GetStream\(\);\[byte\[\]\]\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d7ed9c8d07754407ed46035be469555a:search

```yaml
regex_id: d7ed9c8d07754407ed46035be469555a
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_pulsesecure.yar:186:8"
```

### Pattern

`syswrite\(\*fd,[\x09\x20]{0,32}[\x22\x27]username=\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:dedc0ec540d23f0817a557e7fd03e228:search

```yaml
regex_id: dedc0ec540d23f0817a557e7fd03e228
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/APT_KeyBoy.yar:42:8"
```

### Pattern

`\$fileManager\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:e0a5e7135f3299c39bf381a8dfc493d6:email

```yaml
regex_id: e0a5e7135f3299c39bf381a8dfc493d6
schema_version: "1"
kind: intent_mismatch
corpus: AegisMind
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/TOOLKIT_FinFisher_.yar:87:8"
```

### Pattern

`\/scomma excel2010\.part`

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

## usage_mismatch:e2fc7b2da2d2ceb2e14e72604cea9a5e:search

```yaml
regex_id: e2fc7b2da2d2ceb2e14e72604cea9a5e
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/RANSOM_MS17-010_Wannacrypt.yar:172:6"
```

### Pattern

`\\\\\\\\192\.168\.56\.20\\\\IPC\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e5ef47ea52dcc8f723cf25625407080f:search

```yaml
regex_id: e5ef47ea52dcc8f723cf25625407080f
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/APT_KeyBoy.yar:39:8"
```

### Pattern

`\$login\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e7d53c5f86a46c7c6328603529489057:search

```yaml
regex_id: e7d53c5f86a46c7c6328603529489057
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_hafnium.yar:115:6"
```

### Pattern

`\.GetStream\(\);\[byte\[\]\]\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e899571f61b4e2120929dcdbbf7e2c4c:search

```yaml
regex_id: e899571f61b4e2120929dcdbbf7e2c4c
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/thor-webshells.yar:2139:2"
```

### Pattern

`if\(eregi\('WHERE\|LIMIT',\$_POST\['nsql'\]\)\ \&\&\ eregi\('SELECT\|FROM',\$_POST\['nsql'\]\)\)\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e910190a36830923198dfb8f3031c384:search

```yaml
regex_id: e910190a36830923198dfb8f3031c384
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/gen_webshells.yar:6905:8"
```

### Pattern

`\]\(\$_COOKIE,\ \$_POST\)\ as\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:ea49a3f0d94e18319cbf00f13bb011b3:email

```yaml
regex_id: ea49a3f0d94e18319cbf00f13bb011b3
schema_version: "1"
kind: intent_mismatch
corpus: AegisMind
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/TOOLKIT_FinFisher_.yar:17:8"
```

### Pattern

`\/scomma excel2010\.part`

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

## intent_mismatch:ec2ea3053331d7d0d0d65b716d3f907b:email

```yaml
regex_id: ec2ea3053331d7d0d0d65b716d3f907b
schema_version: "1"
kind: intent_mismatch
corpus: AegisMind
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/expl_proxyshell.yar:30:6"
```

### Pattern

`Email=autodiscover\/autodiscover\.json[^\n]{1,400}200 0 0`

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

## usage_mismatch:ec86a7a9159cefcf7c75138b8d9ff232:search

```yaml
regex_id: ec86a7a9159cefcf7c75138b8d9ff232
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_sandworm_centreon.yar:21:6"
```

### Pattern

`\.substr\(md5\(strrev\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:eeccfc24a250f4a012ad4c8ccb40b367:search

```yaml
regex_id: eeccfc24a250f4a012ad4c8ccb40b367
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/crime_wannacry.yar:36:6"
```

### Pattern

`\\\\\\\\172\.16\.99\.5\\\\IPC\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ef14945295fcd1bc216ecbd0e24f098c:search

```yaml
regex_id: ef14945295fcd1bc216ecbd0e24f098c
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/WShell_THOR_Webshells.yar:6554:2"
```

### Pattern

`\$Id:\ UPX\ 1\.07\ Copyright\ \(C\)\ 1996\-2001\ the\ UPX\ Team\.\ All\ Rights\ Reserved\.\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f17d03620190a326e534d4ce86509b32:search

```yaml
regex_id: f17d03620190a326e534d4ce86509b32
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/WShell_THOR_Webshells.yar:7573:2"
```

### Pattern

`\$Info:\ This\ file\ is\ packed\ with\ the\ UPX\ executable\ packer\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f1862c460046b434dd04b005d8019821:search

```yaml
regex_id: f1862c460046b434dd04b005d8019821
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/APT_OPCleaver.yar:594:8"
```

### Pattern

`LAST_TIME=00/00/0000:00:00PM\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f45f10527dd9a2ad94bc5b43373b4e95:search

```yaml
regex_id: f45f10527dd9a2ad94bc5b43373b4e95
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/gen_webshells.yar:2500:8"
```

### Pattern

`echo[\t ]{0,500}\(?`\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f4b0a6b881bc0ff21f90df530fcca083:search

```yaml
regex_id: f4b0a6b881bc0ff21f90df530fcca083
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/gen_webshells.yar:2605:8"
```

### Pattern

`\\neval\(htmlspecialchars_decode\(gzinflate\(base64_decode\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f50955bf551cc28e3ca9690f68053ae6:search

```yaml
regex_id: f50955bf551cc28e3ca9690f68053ae6
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/thor-webshells.yar:8419:2"
```

### Pattern

`\$License:\ NRV\ for\ UPX\ is\ distributed\ under\ special\ license\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f5a3f9cbc8e78e07751ea759bb08928a:search

```yaml
regex_id: f5a3f9cbc8e78e07751ea759bb08928a
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/APT_OPCleaver.yar:236:4"
```

### Pattern

`LAST_TIME=00/00/0000:00:00PM\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f92b529c3e95d8044bf00a8962c0497c:search

```yaml
regex_id: f92b529c3e95d8044bf00a8962c0497c
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/WShell_THOR_Webshells.yar:7574:2"
```

### Pattern

`\$License:\ NRV\ for\ UPX\ is\ distributed\ under\ special\ license\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fada74f42a21735da5f9d6f18a2b4b26:search

```yaml
regex_id: fada74f42a21735da5f9d6f18a2b4b26
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/WShell_THOR_Webshells.yar:6547:2"
```

### Pattern

`\$Info:\ This\ file\ is\ packed\ with\ the\ UPX\ executable\ packer\ http://upx\.tsx\.org\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fb7a6f34f6d451f90dea6f4c30eda33f:search

```yaml
regex_id: fb7a6f34f6d451f90dea6f4c30eda33f
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_indetectables_rat.yar:27:2"
```

### Pattern

`\[\[__M3_F_U_D_M3__\]\]\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fbbe89453099ae6acae340feb2cdb26b:search

```yaml
regex_id: fbbe89453099ae6acae340feb2cdb26b
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/gen_webshells.yar:1269:8"
```

### Pattern

`\]\.\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fd8b1dc0bbff9ae5ab0e130ff1094f28:search

```yaml
regex_id: fd8b1dc0bbff9ae5ab0e130ff1094f28
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/thor-hacktools.yar:4193:6"
```

### Pattern

`TNtDllHook\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fe547aef038b262e382b8d92f9b0b8c1:search

```yaml
regex_id: fe547aef038b262e382b8d92f9b0b8c1
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/RAT_Indetectables.yar:29:2"
```

### Pattern

`\[\[__M3_F_U_D_M3__\]\]\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:fe6f29a1ad1536e6601272355dbb93ae:search

```yaml
regex_id: fe6f29a1ad1536e6601272355dbb93ae
schema_version: "1"
kind: usage_mismatch
corpus: AegisMind
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/AegisMind/rules/yara_rules/apt_muddywater.yar:42:6"
```

### Pattern

`scripting\.filesystemobject\$`

### Context

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
corpus: AegisMind
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
corpus: AegisMind
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
corpus: AegisMind
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
corpus: AegisMind
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

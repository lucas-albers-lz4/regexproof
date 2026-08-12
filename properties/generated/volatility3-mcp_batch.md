---
schema_version: "1"
corpus: volatility3-mcp
findings: 71
---

# volatility3-mcp batch findings

## usage_mismatch:00ca20c6f1e337e0b8b3679a307ecf48:search

```yaml
regex_id: 00ca20c6f1e337e0b8b3679a307ecf48
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/APT_eqgrp_apr17.yar:2120:6"
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

## intent_mismatch:056fc2500d530eb3cfbed6cd4c83055e:email

```yaml
regex_id: 056fc2500d530eb3cfbed6cd4c83055e
schema_version: "1"
kind: intent_mismatch
corpus: volatility3-mcp
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/TOOLKIT_FinFisher_.yar:16:8"
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

## intent_mismatch:080ca5b28e55375c5575595e7750770a:email

```yaml
regex_id: 080ca5b28e55375c5575595e7750770a
schema_version: "1"
kind: intent_mismatch
corpus: volatility3-mcp
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/email/Email_PHP_Mailer.yar:55:11"
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

## usage_mismatch:0ded64f8d95b0a8e01b459b8000c01ed:search

```yaml
regex_id: 0ded64f8d95b0a8e01b459b8000c01ed
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/RAT_PoisonIvy.yar:39:2"
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

## usage_mismatch:111ec05c329fc15ecb5091e60b303230:search

```yaml
regex_id: 111ec05c329fc15ecb5091e60b303230
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/webshells/WShell_THOR_Webshells.yar:7574:2"
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

## usage_mismatch:14b418fd768799e81aa17108a0da7d54:search

```yaml
regex_id: 14b418fd768799e81aa17108a0da7d54
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/webshells/WShell_THOR_Webshells.yar:6547:2"
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

## usage_mismatch:179c4feb3ddfb1d0afa97fed14d0cc2f:search

```yaml
regex_id: 179c4feb3ddfb1d0afa97fed14d0cc2f
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/webshells/WShell_THOR_Webshells.yar:89:2"
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

## usage_mismatch:17d46327c538a9678d93079830f60997:search

```yaml
regex_id: 17d46327c538a9678d93079830f60997
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/RANSOM_Petya_MS17_010.yar:14:6"
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

## intent_mismatch:1845545066d749de96a3440a99ddefb4:email

```yaml
regex_id: 1845545066d749de96a3440a99ddefb4
schema_version: "1"
kind: intent_mismatch
corpus: volatility3-mcp
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/TOOLKIT_FinFisher_.yar:17:8"
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

## usage_mismatch:1a217067bcb56a8bd43a2655b933fcc8:search

```yaml
regex_id: 1a217067bcb56a8bd43a2655b933fcc8
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/webshells/WShell_THOR_Webshells.yar:7573:2"
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

## intent_mismatch:1e955d23b81466c308027bf7046729ea:email

```yaml
regex_id: 1e955d23b81466c308027bf7046729ea
schema_version: "1"
kind: intent_mismatch
corpus: volatility3-mcp
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/TOOLKIT_FinFisher_.yar:15:8"
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

## intent_mismatch:20835b5786a9bdc594e28558a0bb4830:email

```yaml
regex_id: 20835b5786a9bdc594e28558a0bb4830
schema_version: "1"
kind: intent_mismatch
corpus: volatility3-mcp
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/email/Email_PHP_Mailer.yar:53:8"
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

## usage_mismatch:272facff46522738f46fbcc528e950c0:search

```yaml
regex_id: 272facff46522738f46fbcc528e950c0
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/APT_Derusbi.yar:281:8"
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

## intent_mismatch:2b8c8d9dcad7b4f3507b391a0e90e123:email

```yaml
regex_id: 2b8c8d9dcad7b4f3507b391a0e90e123
schema_version: "1"
kind: intent_mismatch
corpus: volatility3-mcp
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/TOOLKIT_FinFisher_.yar:86:8"
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

## usage_mismatch:2cc1e4f3ad91dc5ac8290ebad5c80d2e:search

```yaml
regex_id: 2cc1e4f3ad91dc5ac8290ebad5c80d2e
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/APT_KeyBoy.yar:44:8"
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

## usage_mismatch:35602f917b6225ac843bbe982916114d:search

```yaml
regex_id: 35602f917b6225ac843bbe982916114d
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/RAT_Indetectables.yar:29:2"
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

## usage_mismatch:3a6b9d47946c94528eeb21bd155e3d0b:search

```yaml
regex_id: 3a6b9d47946c94528eeb21bd155e3d0b
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/webshells/WShell_THOR_Webshells.yar:7335:2"
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

## usage_mismatch:3df251b34b2a0f2dce18a1ede0088585:search

```yaml
regex_id: 3df251b34b2a0f2dce18a1ede0088585
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/MALW_Miscelanea.yar:679:2"
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

## intent_mismatch:43f1eaa94135d3ed85b812747efeae4f:email

```yaml
regex_id: 43f1eaa94135d3ed85b812747efeae4f
schema_version: "1"
kind: intent_mismatch
corpus: volatility3-mcp
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/TOOLKIT_FinFisher_.yar:16:8"
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

## usage_mismatch:4679ec3b430120e852ab448b159c4f63:search

```yaml
regex_id: 4679ec3b430120e852ab448b159c4f63
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/APT_Passcv.yar:158:6"
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

## usage_mismatch:484e00b091ba6af10d56504596f5686b:search

```yaml
regex_id: 484e00b091ba6af10d56504596f5686b
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/webshells/WShell_THOR_Webshells.yar:3813:2"
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

## usage_mismatch:4a53ea3a89d7c3d07489c703dbe827cb:search

```yaml
regex_id: 4a53ea3a89d7c3d07489c703dbe827cb
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/APT_OPCleaver.yar:594:8"
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

## intent_mismatch:4eb27e92eff68882eb0721f78818fb80:email

```yaml
regex_id: 4eb27e92eff68882eb0721f78818fb80
schema_version: "1"
kind: intent_mismatch
corpus: volatility3-mcp
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/email/Email_PHP_Mailer.yar:54:8"
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

## intent_mismatch:4ebc89fae9dbf7b4950ff38591d41dc9:email

```yaml
regex_id: 4ebc89fae9dbf7b4950ff38591d41dc9
schema_version: "1"
kind: intent_mismatch
corpus: volatility3-mcp
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/TOOLKIT_FinFisher_.yar:87:8"
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

## intent_mismatch:4ec4b129f8f866cb73460aa2f7e572f3:email

```yaml
regex_id: 4ec4b129f8f866cb73460aa2f7e572f3
schema_version: "1"
kind: intent_mismatch
corpus: volatility3-mcp
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/TOOLKIT_FinFisher_.yar:85:8"
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

## intent_mismatch:57a55af1547c6eb574743331e13fc65e:email

```yaml
regex_id: 57a55af1547c6eb574743331e13fc65e
schema_version: "1"
kind: intent_mismatch
corpus: volatility3-mcp
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/email/urls.yar:31:2"
```

### Pattern

`https?:\/\/([\w\.-]+)([\/\w \.-]*)`

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

## usage_mismatch:6098acf9e2eba8f0ddf2a8f4fe68a8f9:search

```yaml
regex_id: 6098acf9e2eba8f0ddf2a8f4fe68a8f9
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/webshells/WShell_THOR_Webshells.yar:3274:2"
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

## usage_mismatch:60ade02ceb343325d684001eb2b71828:search

```yaml
regex_id: 60ade02ceb343325d684001eb2b71828
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/APT_Derusbi.yar:263:8"
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

## usage_mismatch:62273b92f3ebba01c08290ebcbc6cf77:search

```yaml
regex_id: 62273b92f3ebba01c08290ebcbc6cf77
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/APT_KeyBoy.yar:39:8"
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

## intent_mismatch:62f27e705f3126eab4d37c02e027db93:email

```yaml
regex_id: 62f27e705f3126eab4d37c02e027db93
schema_version: "1"
kind: intent_mismatch
corpus: volatility3-mcp
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/TOOLKIT_FinFisher_.yar:87:8"
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

## intent_mismatch:6434a8eb583c1cd971dcc3cf659e117c:email

```yaml
regex_id: 6434a8eb583c1cd971dcc3cf659e117c
schema_version: "1"
kind: intent_mismatch
corpus: volatility3-mcp
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/TOOLKIT_FinFisher_.yar:86:8"
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

## intent_mismatch:64f017c29209af38b7384610b85f0e8e:email

```yaml
regex_id: 64f017c29209af38b7384610b85f0e8e
schema_version: "1"
kind: intent_mismatch
corpus: volatility3-mcp
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/TOOLKIT_FinFisher_.yar:15:8"
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

## usage_mismatch:6516943cee80f203bf854b75e2b9d95d:search

```yaml
regex_id: 6516943cee80f203bf854b75e2b9d95d
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/APT_ThreatGroup3390.yar:38:8"
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

## usage_mismatch:6644726731aaa51a67d85954943b19ad:search

```yaml
regex_id: 6644726731aaa51a67d85954943b19ad
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/MALW_Miscelanea.yar:137:2"
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

## usage_mismatch:6e9dc0e7e977f63be1ad74fe80566578:search

```yaml
regex_id: 6e9dc0e7e977f63be1ad74fe80566578
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/APT_Snowglobe_Babar.yar:32:8"
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

## usage_mismatch:72142b58d0acc67c9b3fceb542a12523:search

```yaml
regex_id: 72142b58d0acc67c9b3fceb542a12523
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/webshells/WShell_PHP_in_images.yar:12:8"
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

## usage_mismatch:740415a8e6a6df006bd6e303f742d905:search

```yaml
regex_id: 740415a8e6a6df006bd6e303f742d905
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/APT_APT29_Grizzly_Steppe.yar:109:6"
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

## usage_mismatch:7646b764f5ca030df6f5dfc6243fe0a5:search

```yaml
regex_id: 7646b764f5ca030df6f5dfc6243fe0a5
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/RANSOM_MS17-010_Wannacrypt.yar:173:6"
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

## usage_mismatch:79bd00ee1f5d440b3d41c7c4c6113412:search

```yaml
regex_id: 79bd00ee1f5d440b3d41c7c4c6113412
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/APT_KeyBoy.yar:40:8"
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

## usage_mismatch:810fad2949c3424a4c41623b39bd7b72:search

```yaml
regex_id: 810fad2949c3424a4c41623b39bd7b72
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/APT_KeyBoy.yar:41:8"
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

## intent_mismatch:833971ee30a2162043f0a7f089fc57ea:email

```yaml
regex_id: 833971ee30a2162043f0a7f089fc57ea
schema_version: "1"
kind: intent_mismatch
corpus: volatility3-mcp
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/email/Email_PHP_Mailer.yar:52:8"
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

## usage_mismatch:83aa00dba388b7d12e289f4609bda467:search

```yaml
regex_id: 83aa00dba388b7d12e289f4609bda467
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/Operation_Blockbuster/general.yara:13:2"
```

### Pattern

`BAISEO%\$2fas9vQsfvx%\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:8991a95f8f096b697ef1af28f8a81246:search

```yaml
regex_id: 8991a95f8f096b697ef1af28f8a81246
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/webshells/WShell_THOR_Webshells.yar:50:2"
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

## intent_mismatch:89c1271a4af2b8698ca6b4e1c6b1387a:email

```yaml
regex_id: 89c1271a4af2b8698ca6b4e1c6b1387a
schema_version: "1"
kind: intent_mismatch
corpus: volatility3-mcp
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/email/urls.yar:16:2"
```

### Pattern

`https?:\/\/([\w\.-]+)([\/\w \.-]*)`

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

## usage_mismatch:8b813a223ae4457363832d15ee7fc998:search

```yaml
regex_id: 8b813a223ae4457363832d15ee7fc998
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/APT_APT29_Grizzly_Steppe.yar:89:6"
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

## usage_mismatch:8f3195d8caff0f033eaf04cccd2565c0:search

```yaml
regex_id: 8f3195d8caff0f033eaf04cccd2565c0
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/webshells/WShell_THOR_Webshells.yar:621:2"
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

## usage_mismatch:942bf4f29c0561621272a3af9a0d25a8:search

```yaml
regex_id: 942bf4f29c0561621272a3af9a0d25a8
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/APT_Derusbi.yar:318:8"
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

## usage_mismatch:ae27fc96a12e79d32c746e0cae82a6fb:search

```yaml
regex_id: ae27fc96a12e79d32c746e0cae82a6fb
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/TOOLKIT_THOR_HackTools.yar:2775:2"
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

## intent_mismatch:aed5a0991bf3a198191547d6a776877b:hostname

```yaml
regex_id: aed5a0991bf3a198191547d6a776877b
schema_version: "1"
kind: intent_mismatch
corpus: volatility3-mcp
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/TOOLKIT_Chinese_Hacktools.yar:1874:2"
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

## usage_mismatch:b91f786f45e64b88046873f3a3d1e982:search

```yaml
regex_id: b91f786f45e64b88046873f3a3d1e982
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/webshells/WShell_THOR_Webshells.yar:6554:2"
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

## usage_mismatch:bb6a2fc61abf98306c22b2350795ce60:search

```yaml
regex_id: bb6a2fc61abf98306c22b2350795ce60
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/webshells/WShell_THOR_Webshells.yar:6262:2"
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

## usage_mismatch:bdd125e4f12b04792e530226b7346096:search

```yaml
regex_id: bdd125e4f12b04792e530226b7346096
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/webshells/WShell_THOR_Webshells.yar:1880:2"
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

## intent_mismatch:c0cae6213722550477401bf0b9ed7474:email

```yaml
regex_id: c0cae6213722550477401bf0b9ed7474
schema_version: "1"
kind: intent_mismatch
corpus: volatility3-mcp
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/TOOLKIT_FinFisher_.yar:85:8"
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

## usage_mismatch:c5ace7b967f7795d9368f3e8f0777e9a:search

```yaml
regex_id: c5ace7b967f7795d9368f3e8f0777e9a
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/APT_Poseidon_Group.yar:38:8"
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

## usage_mismatch:c675f2c47daf89b69f66a03c421ada58:search

```yaml
regex_id: c675f2c47daf89b69f66a03c421ada58
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/APT_Industroyer.yar:87:6"
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

## usage_mismatch:cc690846306c49004f83a54330cd69e0:search

```yaml
regex_id: cc690846306c49004f83a54330cd69e0
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/RANSOM_Petya_MS17_010.yar:14:6"
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

## usage_mismatch:ceded91aa695c24fc7134d81dfd84f9e:search

```yaml
regex_id: ceded91aa695c24fc7134d81dfd84f9e
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/APT_OPCleaver.yar:236:4"
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

## intent_mismatch:d180e9c8b0a8e769d3b16bd63a65cf40:email

```yaml
regex_id: d180e9c8b0a8e769d3b16bd63a65cf40
schema_version: "1"
kind: intent_mismatch
corpus: volatility3-mcp
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/TOOLKIT_FinFisher_.yar:17:8"
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

## intent_mismatch:dc8766bd052f6504ca8f3bc9f42604b8:hostname

```yaml
regex_id: dc8766bd052f6504ca8f3bc9f42604b8
schema_version: "1"
kind: intent_mismatch
corpus: volatility3-mcp
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/TOOLKIT_Chinese_Hacktools.yar:1876:2"
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

## usage_mismatch:dca0c6a31f16e0327f466280638753d1:search

```yaml
regex_id: dca0c6a31f16e0327f466280638753d1
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/APT_KeyBoy.yar:43:8"
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

## usage_mismatch:e2a39a1b53ea4fa918f499d01061dae6:search

```yaml
regex_id: e2a39a1b53ea4fa918f499d01061dae6
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/APT_KeyBoy.yar:42:8"
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

## usage_mismatch:e404ce7e1b861ba0e7c3a16d80946605:search

```yaml
regex_id: e404ce7e1b861ba0e7c3a16d80946605
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/webshells/WShell_THOR_Webshells.yar:6872:2"
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

## usage_mismatch:ead82aad852e087dc97061f800f010ba:search

```yaml
regex_id: ead82aad852e087dc97061f800f010ba
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/RANSOM_MS17-010_Wannacrypt.yar:172:6"
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

## usage_mismatch:ebec20fc743bb86a23b3cd1176a1ccc3:search

```yaml
regex_id: ebec20fc743bb86a23b3cd1176a1ccc3
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/MALW_Hsdfihdf_banking.yar:28:1"
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

## usage_mismatch:f096be7b20f8ffe10fe99ff4ab005e33:search

```yaml
regex_id: f096be7b20f8ffe10fe99ff4ab005e33
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/APT_APT29_Grizzly_Steppe.yar:92:6"
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

## usage_mismatch:f1e47cdb68b1936881e4abf432f76d5b:search

```yaml
regex_id: f1e47cdb68b1936881e4abf432f76d5b
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/APT_Regin.yar:341:8"
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

## usage_mismatch:f886182e03d9f92b66c0cf313e315ac2:search

```yaml
regex_id: f886182e03d9f92b66c0cf313e315ac2
schema_version: "1"
kind: usage_mismatch
corpus: volatility3-mcp
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/volatility3-mcp/rules/malware/MALW_AlMashreq.yar:21:1"
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

## property:inventory:rc-shape1-injection-alphabet:rc-shape1-injection-alphabet

```yaml
regex_id: "inventory:rc-shape1-injection-alphabet"
schema_version: "1"
kind: property
corpus: volatility3-mcp
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
corpus: volatility3-mcp
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
corpus: volatility3-mcp
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
corpus: volatility3-mcp
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

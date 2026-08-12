---
schema_version: "1"
corpus: sec_check
findings: 64
---

# sec_check batch findings

## usage_mismatch:013fd4f00f1310571d43c0289fa7d9fa:search

```yaml
regex_id: 013fd4f00f1310571d43c0289fa7d9fa
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/APT_APT29_Grizzly_Steppe.yar:92:6"
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

## usage_mismatch:0d9f789b44d7b2f8c4c8489454066083:search

```yaml
regex_id: 0d9f789b44d7b2f8c4c8489454066083
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/APT_KeyBoy.yar:41:8"
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

## intent_mismatch:0fb467facb6d6b2a14ff07fd5f1d67bb:hostname

```yaml
regex_id: 0fb467facb6d6b2a14ff07fd5f1d67bb
schema_version: "1"
kind: intent_mismatch
corpus: sec_check
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/TOOLKIT_Chinese_Hacktools.yar:1874:2"
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

## usage_mismatch:1834ff62c0cbefbd56e7f86e629c1ad3:search

```yaml
regex_id: 1834ff62c0cbefbd56e7f86e629c1ad3
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/Webshells/WShell_THOR_Webshells.yar:6554:2"
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

## usage_mismatch:18a1fd0570129a87b2cafc4e870cf75c:search

```yaml
regex_id: 18a1fd0570129a87b2cafc4e870cf75c
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/APT_KeyBoy.yar:44:8"
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

## usage_mismatch:1b9aa7bdbd6876328ece786f347cd887:search

```yaml
regex_id: 1b9aa7bdbd6876328ece786f347cd887
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/APT_APT29_Grizzly_Steppe.yar:109:6"
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

## usage_mismatch:1e79e99080e37a51dc76ebfb87d700b7:search

```yaml
regex_id: 1e79e99080e37a51dc76ebfb87d700b7
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/APT_eqgrp_apr17.yar:2120:6"
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

## usage_mismatch:1e898f702043dd2393131b85f077b8de:search

```yaml
regex_id: 1e898f702043dd2393131b85f077b8de
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/Webshells/WShell_THOR_Webshells.yar:50:2"
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

## usage_mismatch:224a3042d8dd90cd1eed60af681a3ef0:search

```yaml
regex_id: 224a3042d8dd90cd1eed60af681a3ef0
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/Webshells/WShell_THOR_Webshells.yar:3813:2"
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

## usage_mismatch:2aa599838748628051188a6aec1e9583:search

```yaml
regex_id: 2aa599838748628051188a6aec1e9583
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/APT_Industroyer.yar:87:6"
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

## usage_mismatch:2b887fc560eb692139104a409330800f:search

```yaml
regex_id: 2b887fc560eb692139104a409330800f
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/APT_Poseidon_Group.yar:38:8"
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

## usage_mismatch:2c20b2fac5bf08ed667761efdc2063a8:search

```yaml
regex_id: 2c20b2fac5bf08ed667761efdc2063a8
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/Webshells/WShell_THOR_Webshells.yar:621:2"
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

## intent_mismatch:2fdb1de3d7810d01ad7d2991fb614caa:hostname

```yaml
regex_id: 2fdb1de3d7810d01ad7d2991fb614caa
schema_version: "1"
kind: intent_mismatch
corpus: sec_check
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/TOOLKIT_Chinese_Hacktools.yar:1876:2"
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

## usage_mismatch:33cf43df778f3cfb377a7d9a8d3eb6cc:search

```yaml
regex_id: 33cf43df778f3cfb377a7d9a8d3eb6cc
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/Webshells/WShell_THOR_Webshells.yar:89:2"
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

## usage_mismatch:36c4d33d994972983cc7c6d99a667494:search

```yaml
regex_id: 36c4d33d994972983cc7c6d99a667494
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/APT_Derusbi.yar:281:8"
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

## usage_mismatch:3f3c8ea558c1bffa2388e9bcd2b3ffcd:search

```yaml
regex_id: 3f3c8ea558c1bffa2388e9bcd2b3ffcd
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/APT_Passcv.yar:158:6"
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

## intent_mismatch:4433f0e034b89730d67548ee6dbc3a2d:email

```yaml
regex_id: 4433f0e034b89730d67548ee6dbc3a2d
schema_version: "1"
kind: intent_mismatch
corpus: sec_check
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/TOOLKIT_FinFisher_.yar:86:8"
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

## usage_mismatch:470d943f8f76d453a9b76f07e60104f6:search

```yaml
regex_id: 470d943f8f76d453a9b76f07e60104f6
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/APT_Derusbi.yar:318:8"
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

## usage_mismatch:5014725083c16e76893c8aa15148d4d2:search

```yaml
regex_id: 5014725083c16e76893c8aa15148d4d2
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/APT_KeyBoy.yar:40:8"
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

## usage_mismatch:550801f52b94c1183babee567ce1207f:search

```yaml
regex_id: 550801f52b94c1183babee567ce1207f
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/Webshells/WShell_PHP_in_images.yar:12:8"
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

## usage_mismatch:5768a0ae627bb204ad368ef05b638463:search

```yaml
regex_id: 5768a0ae627bb204ad368ef05b638463
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/APT_KeyBoy.yar:43:8"
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

## usage_mismatch:58f27171251f3900ac1c7e8bfbd1f53a:search

```yaml
regex_id: 58f27171251f3900ac1c7e8bfbd1f53a
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/APT_APT29_Grizzly_Steppe.yar:89:6"
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

## usage_mismatch:595370ba0cbc80410f873bb7f338ad0b:search

```yaml
regex_id: 595370ba0cbc80410f873bb7f338ad0b
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/APT_KeyBoy.yar:42:8"
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

## usage_mismatch:5fd76028a09c4753262470f13762ab72:search

```yaml
regex_id: 5fd76028a09c4753262470f13762ab72
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/Webshells/WShell_THOR_Webshells.yar:6547:2"
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

## usage_mismatch:6dfb98d8dff7648e81ffb1aded662e32:search

```yaml
regex_id: 6dfb98d8dff7648e81ffb1aded662e32
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/Webshells/WShell_THOR_Webshells.yar:3274:2"
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

## usage_mismatch:715d5f3962a7dc27a0ac607dc528ec77:search

```yaml
regex_id: 715d5f3962a7dc27a0ac607dc528ec77
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/Webshells/WShell_THOR_Webshells.yar:7335:2"
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

## intent_mismatch:79a0df89f556f4e0209ea7f573b1c0df:email

```yaml
regex_id: 79a0df89f556f4e0209ea7f573b1c0df
schema_version: "1"
kind: intent_mismatch
corpus: sec_check
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/email/urls.yar:16:2"
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

## intent_mismatch:7b0a766e7c70eb5f88cdefdb1f04cebe:email

```yaml
regex_id: 7b0a766e7c70eb5f88cdefdb1f04cebe
schema_version: "1"
kind: intent_mismatch
corpus: sec_check
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/TOOLKIT_FinFisher_.yar:87:8"
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

## intent_mismatch:7cb551372c8afc9ac5b0a11d78c1d9b3:email

```yaml
regex_id: 7cb551372c8afc9ac5b0a11d78c1d9b3
schema_version: "1"
kind: intent_mismatch
corpus: sec_check
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/TOOLKIT_FinFisher_.yar:16:8"
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

## intent_mismatch:81b957177673c42f3fdd265df08fe50b:email

```yaml
regex_id: 81b957177673c42f3fdd265df08fe50b
schema_version: "1"
kind: intent_mismatch
corpus: sec_check
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/email/urls.yar:31:2"
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

## intent_mismatch:8ccf285ec691f5d1c60bbff5ef681fd2:email

```yaml
regex_id: 8ccf285ec691f5d1c60bbff5ef681fd2
schema_version: "1"
kind: intent_mismatch
corpus: sec_check
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/TOOLKIT_FinFisher_.yar:16:8"
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

## intent_mismatch:8e0fba3cd95bf4f8b31b79fae90840e0:email

```yaml
regex_id: 8e0fba3cd95bf4f8b31b79fae90840e0
schema_version: "1"
kind: intent_mismatch
corpus: sec_check
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/TOOLKIT_FinFisher_.yar:86:8"
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

## intent_mismatch:8f71e67fc0ca3f130197238845859038:email

```yaml
regex_id: 8f71e67fc0ca3f130197238845859038
schema_version: "1"
kind: intent_mismatch
corpus: sec_check
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/TOOLKIT_FinFisher_.yar:17:8"
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

## intent_mismatch:993c2b8d21892260ead3dc44a77e328b:email

```yaml
regex_id: 993c2b8d21892260ead3dc44a77e328b
schema_version: "1"
kind: intent_mismatch
corpus: sec_check
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/TOOLKIT_FinFisher_.yar:15:8"
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

## usage_mismatch:9a0d6b53dd9a2f63c27445481b39a45a:search

```yaml
regex_id: 9a0d6b53dd9a2f63c27445481b39a45a
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/Operation_Blockbuster/general.yara:13:2"
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

## intent_mismatch:a4e645265e8236d1d8e76db23c012bf5:email

```yaml
regex_id: a4e645265e8236d1d8e76db23c012bf5
schema_version: "1"
kind: intent_mismatch
corpus: sec_check
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/TOOLKIT_FinFisher_.yar:85:8"
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

## usage_mismatch:a5298a7169e7706b9a0dc21f86c00ec1:search

```yaml
regex_id: a5298a7169e7706b9a0dc21f86c00ec1
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/Webshells/WShell_THOR_Webshells.yar:1880:2"
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

## usage_mismatch:a601e96529dddaf854073dcab8cc9afc:search

```yaml
regex_id: a601e96529dddaf854073dcab8cc9afc
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/APT_Derusbi.yar:263:8"
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

## usage_mismatch:a9dfef36d9132404be26b6a3b374da01:search

```yaml
regex_id: a9dfef36d9132404be26b6a3b374da01
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/APT_Snowglobe_Babar.yar:32:8"
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

## usage_mismatch:b284133ec8528c2896a51da6649ef9af:search

```yaml
regex_id: b284133ec8528c2896a51da6649ef9af
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/TOOLKIT_THOR_HackTools.yar:2775:2"
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

## intent_mismatch:bcddfad6ad90a2a3916c18652c1ece6e:email

```yaml
regex_id: bcddfad6ad90a2a3916c18652c1ece6e
schema_version: "1"
kind: intent_mismatch
corpus: sec_check
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/TOOLKIT_FinFisher_.yar:85:8"
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

## usage_mismatch:bced7f626085434e446874f89267a89d:search

```yaml
regex_id: bced7f626085434e446874f89267a89d
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/APT_ThreatGroup3390.yar:38:8"
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

## usage_mismatch:bf9053b918aac0b6c3ff17dd4fffe347:search

```yaml
regex_id: bf9053b918aac0b6c3ff17dd4fffe347
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/Webshells/WShell_THOR_Webshells.yar:6262:2"
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

## usage_mismatch:c44e6e3fe81a452e164df20f2ba40a24:search

```yaml
regex_id: c44e6e3fe81a452e164df20f2ba40a24
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/RAT_Indetectables.yar:29:2"
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

## usage_mismatch:c9955d5449b781f04c2c4018c01a512b:search

```yaml
regex_id: c9955d5449b781f04c2c4018c01a512b
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/RANSOM_MS17-010_Wannacrypt.yar:172:6"
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

## usage_mismatch:cab54b6c7a467a1d15c6f383b19d6af3:search

```yaml
regex_id: cab54b6c7a467a1d15c6f383b19d6af3
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/Webshells/WShell_THOR_Webshells.yar:6872:2"
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

## usage_mismatch:cc6112ef0ea4f114b84adb737039e8fe:search

```yaml
regex_id: cc6112ef0ea4f114b84adb737039e8fe
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/MALW_Miscelanea.yar:137:2"
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

## intent_mismatch:d0da88d8874a10e915b28f2d00e91f2e:email

```yaml
regex_id: d0da88d8874a10e915b28f2d00e91f2e
schema_version: "1"
kind: intent_mismatch
corpus: sec_check
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/TOOLKIT_FinFisher_.yar:87:8"
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

## usage_mismatch:d10efeebb34146b165ee69b5532980f7:search

```yaml
regex_id: d10efeebb34146b165ee69b5532980f7
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/Webshells/WShell_THOR_Webshells.yar:7574:2"
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

## usage_mismatch:d5926514cf1635c0a79eb66484325e7f:search

```yaml
regex_id: d5926514cf1635c0a79eb66484325e7f
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/RANSOM_MS17-010_Wannacrypt.yar:173:6"
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

## usage_mismatch:dc14ed0116a25c5ced518269ce84a5f9:search

```yaml
regex_id: dc14ed0116a25c5ced518269ce84a5f9
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/MALW_Hsdfihdf_banking.yar:28:1"
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

## usage_mismatch:e1a698dd393039dd0cb9a7a709184940:search

```yaml
regex_id: e1a698dd393039dd0cb9a7a709184940
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/MALW_Miscelanea.yar:679:2"
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

## intent_mismatch:e76c6c687a885aa5547d523cd62f56dc:email

```yaml
regex_id: e76c6c687a885aa5547d523cd62f56dc
schema_version: "1"
kind: intent_mismatch
corpus: sec_check
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/TOOLKIT_FinFisher_.yar:17:8"
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

## intent_mismatch:eb0c380dd64800d02a057ac465d7cdd1:email

```yaml
regex_id: eb0c380dd64800d02a057ac465d7cdd1
schema_version: "1"
kind: intent_mismatch
corpus: sec_check
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/TOOLKIT_FinFisher_.yar:15:8"
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

## usage_mismatch:eb16d0cbc865376ff30ccedf67f9e4c0:search

```yaml
regex_id: eb16d0cbc865376ff30ccedf67f9e4c0
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/RAT_PoisonIvy.yar:39:2"
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

## usage_mismatch:f81b1627ec8b7eede0eadfd32512f21d:search

```yaml
regex_id: f81b1627ec8b7eede0eadfd32512f21d
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/Webshells/WShell_THOR_Webshells.yar:7573:2"
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

## usage_mismatch:f84cf7174701d5335422f84495f6678e:search

```yaml
regex_id: f84cf7174701d5335422f84495f6678e
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/APT_KeyBoy.yar:39:8"
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

## usage_mismatch:fabecb748baad07afd35f3c5d5e51be9:search

```yaml
regex_id: fabecb748baad07afd35f3c5d5e51be9
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/APT_OPCleaver.yar:236:4"
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

## usage_mismatch:fc00e0a4a3a19273eddad320f38e48d1:search

```yaml
regex_id: fc00e0a4a3a19273eddad320f38e48d1
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/APT_OPCleaver.yar:594:8"
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

## usage_mismatch:fe17ab1a618c3e579f75c7fb22c3675c:search

```yaml
regex_id: fe17ab1a618c3e579f75c7fb22c3675c
schema_version: "1"
kind: usage_mismatch
corpus: sec_check
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/sec_check/rules/malware/APT_Regin.yar:341:8"
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

## property:inventory:rc-shape1-injection-alphabet:rc-shape1-injection-alphabet

```yaml
regex_id: "inventory:rc-shape1-injection-alphabet"
schema_version: "1"
kind: property
corpus: sec_check
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
corpus: sec_check
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
corpus: sec_check
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
corpus: sec_check
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

---
schema_version: "1"
corpus: SMAT
findings: 52
---

# SMAT batch findings

## usage_mismatch:06d1470ced3c5f1ca197497b65ebfa22:search

```yaml
regex_id: 06d1470ced3c5f1ca197497b65ebfa22
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/KeyBoy.yar:39:8"
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

## intent_mismatch:06d710020bd7a6c62e9b37dab4c07dad:email

```yaml
regex_id: 06d710020bd7a6c62e9b37dab4c07dad
schema_version: "1"
kind: intent_mismatch
corpus: SMAT
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/FinSpy.yar:87:8"
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

## usage_mismatch:0bb4a04e18b55251f9061213dfe2cc47:search

```yaml
regex_id: 0bb4a04e18b55251f9061213dfe2cc47
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/APT_Derusbi.yar:266:8"
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

## usage_mismatch:10309222a6f86e494aea854accb35a25:search

```yaml
regex_id: 10309222a6f86e494aea854accb35a25
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/KeyBoy.yar:42:8"
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

## usage_mismatch:136cb60004f06777212d566d1a3cc3d6:search

```yaml
regex_id: 136cb60004f06777212d566d1a3cc3d6
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/Operation_Blockbuster/general.yara:13:2"
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

## intent_mismatch:1970737c647eebdf04f128d4ce8c7489:email

```yaml
regex_id: 1970737c647eebdf04f128d4ce8c7489
schema_version: "1"
kind: intent_mismatch
corpus: SMAT
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/FinSpy.yar:17:8"
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

## usage_mismatch:1a5bbb3532a31014cd628771d2960e4c:search

```yaml
regex_id: 1a5bbb3532a31014cd628771d2960e4c
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/THOR_Webshells.yar:7540:2"
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

## usage_mismatch:37bf3ac1be5f2b6acc88ceb574daa761:search

```yaml
regex_id: 37bf3ac1be5f2b6acc88ceb574daa761
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/APT_Regin.yar:317:5"
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

## usage_mismatch:39a24309fe6b23bdc6219c8c47beb66a:search

```yaml
regex_id: 39a24309fe6b23bdc6219c8c47beb66a
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/APT_Poseidon_Group.yar:35:2"
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

## usage_mismatch:3bd00f50c701ad588d610f4f43acd85e:search

```yaml
regex_id: 3bd00f50c701ad588d610f4f43acd85e
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/APT_indetectables_RAT.yar:29:2"
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

## intent_mismatch:3c82c2ffe63e037dcc71cd03dd08b46f:email

```yaml
regex_id: 3c82c2ffe63e037dcc71cd03dd08b46f
schema_version: "1"
kind: intent_mismatch
corpus: SMAT
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/FinSpy.yar:17:8"
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

## usage_mismatch:3f8bd0d2daf49d354055b828e84971d3:search

```yaml
regex_id: 3f8bd0d2daf49d354055b828e84971d3
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/PoisonIvy.yar:39:2"
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

## usage_mismatch:42aebc0edc5d06a8249782155c148787:search

```yaml
regex_id: 42aebc0edc5d06a8249782155c148787
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/KeyBoy.yar:37:8"
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

## intent_mismatch:443688d42f342592f08b241558650138:email

```yaml
regex_id: 443688d42f342592f08b241558650138
schema_version: "1"
kind: intent_mismatch
corpus: SMAT
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/FinSpy.yar:16:8"
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

## usage_mismatch:5f4e27ff2edfec888e3130302cb5b186:search

```yaml
regex_id: 5f4e27ff2edfec888e3130302cb5b186
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/KeyBoy.yar:41:8"
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

## intent_mismatch:604948717343a851428d70fae2a943a6:email

```yaml
regex_id: 604948717343a851428d70fae2a943a6
schema_version: "1"
kind: intent_mismatch
corpus: SMAT
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/FinSpy.yar:16:8"
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

## intent_mismatch:646c5c507f6f86cd026e7b2b5f4cfa99:email

```yaml
regex_id: 646c5c507f6f86cd026e7b2b5f4cfa99
schema_version: "1"
kind: intent_mismatch
corpus: SMAT
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/email/urls.yar:23:2"
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

## intent_mismatch:6552230eaac1385d882cc11e24388072:email

```yaml
regex_id: 6552230eaac1385d882cc11e24388072
schema_version: "1"
kind: intent_mismatch
corpus: SMAT
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/FinSpy.yar:15:8"
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

## intent_mismatch:693c7c7463d83e8dd4f464ff95dfd2ef:email

```yaml
regex_id: 693c7c7463d83e8dd4f464ff95dfd2ef
schema_version: "1"
kind: intent_mismatch
corpus: SMAT
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/FinSpy.yar:85:8"
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

## intent_mismatch:71975ad455692ba65d45813aa0ffd17d:email

```yaml
regex_id: 71975ad455692ba65d45813aa0ffd17d
schema_version: "1"
kind: intent_mismatch
corpus: SMAT
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/FinSpy.yar:87:8"
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

## usage_mismatch:72c59eba7a886d38139f55b64c594ff7:search

```yaml
regex_id: 72c59eba7a886d38139f55b64c594ff7
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/Opcleaver.yar:224:2"
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

## intent_mismatch:7625c6903270da7fdf008fa9335e5be9:email

```yaml
regex_id: 7625c6903270da7fdf008fa9335e5be9
schema_version: "1"
kind: intent_mismatch
corpus: SMAT
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/FinSpy.yar:86:8"
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

## usage_mismatch:779179f016bed9631b67726292a55d05:search

```yaml
regex_id: 779179f016bed9631b67726292a55d05
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/THOR_Webshells.yar:6520:2"
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

## usage_mismatch:7cc39a4f9f2d56ad1da664931ba20f5b:search

```yaml
regex_id: 7cc39a4f9f2d56ad1da664931ba20f5b
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/THOR_Webshells.yar:6230:2"
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

## usage_mismatch:7d318f1a5c6268a240e58ef3744a7077:search

```yaml
regex_id: 7d318f1a5c6268a240e58ef3744a7077
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/THOR_Webshells.yar:6838:2"
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

## usage_mismatch:81565069491f81f6a7871a6508223377:search

```yaml
regex_id: 81565069491f81f6a7871a6508223377
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/KeyBoy.yar:40:8"
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

## usage_mismatch:81866a74c0388c05f0ed0eadbd2d940e:search

```yaml
regex_id: 81866a74c0388c05f0ed0eadbd2d940e
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/THOR_Webshells.yar:7301:2"
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

## usage_mismatch:8297b6ad3b6275015f26929e9eb530b5:search

```yaml
regex_id: 8297b6ad3b6275015f26929e9eb530b5
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/THOR_Webshells.yar:89:2"
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

## usage_mismatch:8311216d7eaef1b568861340d5feb95a:search

```yaml
regex_id: 8311216d7eaef1b568861340d5feb95a
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/Babar.yar:31:2"
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

## usage_mismatch:85902e8594a7d1e1c951388335ebb1e6:search

```yaml
regex_id: 85902e8594a7d1e1c951388335ebb1e6
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/THOR_Webshells.yar:1880:2"
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

## usage_mismatch:88ac25d6ec1a38b19cb7301991053e32:search

```yaml
regex_id: 88ac25d6ec1a38b19cb7301991053e32
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/APT_Derusbi.yar:299:6"
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

## usage_mismatch:8d75730291411cc7e1aaf768435588c4:search

```yaml
regex_id: 8d75730291411cc7e1aaf768435588c4
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/THOR_Webshells.yar:3274:2"
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

## usage_mismatch:97395d6187108c1f04c71f9fa18801c7:search

```yaml
regex_id: 97395d6187108c1f04c71f9fa18801c7
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/THOR_Webshells.yar:7539:2"
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

## usage_mismatch:98951ef14289110110bd0bdd60288bb2:search

```yaml
regex_id: 98951ef14289110110bd0bdd60288bb2
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/THOR_Webshells.yar:621:2"
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

## usage_mismatch:9e07e3b8117c6f966044ccb3872927a7:search

```yaml
regex_id: 9e07e3b8117c6f966044ccb3872927a7
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/Miscelanea.yar:137:2"
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

## usage_mismatch:9f8f0fed3ddbae9cdb5117513671a7a7:search

```yaml
regex_id: 9f8f0fed3ddbae9cdb5117513671a7a7
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/Hsdfihdf_banking_malware.yar:28:1"
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

## intent_mismatch:af55f12f59c130a60b4ff1f3f4490a47:email

```yaml
regex_id: af55f12f59c130a60b4ff1f3f4490a47
schema_version: "1"
kind: intent_mismatch
corpus: SMAT
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/FinSpy.yar:86:8"
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

## usage_mismatch:b131aa7513b32a627c490f7dab8c1148:search

```yaml
regex_id: b131aa7513b32a627c490f7dab8c1148
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/KeyBoy.yar:38:8"
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

## intent_mismatch:ba3049fe2a1cf6c520ce86586db0baf2:email

```yaml
regex_id: ba3049fe2a1cf6c520ce86586db0baf2
schema_version: "1"
kind: intent_mismatch
corpus: SMAT
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/FinSpy.yar:15:8"
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

## intent_mismatch:bb5b433460d268be0c074af6aa4bdd6d:email

```yaml
regex_id: bb5b433460d268be0c074af6aa4bdd6d
schema_version: "1"
kind: intent_mismatch
corpus: SMAT
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/FinSpy.yar:85:8"
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

## usage_mismatch:da44280849cf79929259e4c63419cd3e:search

```yaml
regex_id: da44280849cf79929259e4c63419cd3e
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/THOR_Webshells.yar:50:2"
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

## usage_mismatch:de73db733345fcdb1ca5de8ec70e6950:search

```yaml
regex_id: de73db733345fcdb1ca5de8ec70e6950
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/APT_threatgroup_3390.yar:35:2"
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

## intent_mismatch:e604af1e565d47c3484df406b63d0dd8:email

```yaml
regex_id: e604af1e565d47c3484df406b63d0dd8
schema_version: "1"
kind: intent_mismatch
corpus: SMAT
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/email/urls.yar:12:2"
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

## usage_mismatch:eadbfdfafa10fe2b9ac7d36c311e0617:search

```yaml
regex_id: eadbfdfafa10fe2b9ac7d36c311e0617
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/APT_OPCleaver.yar:198:4"
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

## usage_mismatch:f0942aeb7799522b921daa1cdc7245c8:search

```yaml
regex_id: f0942aeb7799522b921daa1cdc7245c8
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/THOR_HackTools.yar:2775:2"
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

## usage_mismatch:f513a37c4b70abb69184a9fd0160f36b:search

```yaml
regex_id: f513a37c4b70abb69184a9fd0160f36b
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/APT_Derusbi.yar:251:8"
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

## usage_mismatch:f6549688b5af39d1c4b663b8462a49e6:search

```yaml
regex_id: f6549688b5af39d1c4b663b8462a49e6
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/THOR_Webshells.yar:6513:2"
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

## usage_mismatch:fc5ac95ccf10adce5a23b0770eda3cfd:search

```yaml
regex_id: fc5ac95ccf10adce5a23b0770eda3cfd
schema_version: "1"
kind: usage_mismatch
corpus: SMAT
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SMAT/rules/malware/THOR_Webshells.yar:3813:2"
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

## property:inventory:rc-shape1-injection-alphabet:rc-shape1-injection-alphabet

```yaml
regex_id: "inventory:rc-shape1-injection-alphabet"
schema_version: "1"
kind: property
corpus: SMAT
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
corpus: SMAT
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
corpus: SMAT
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
corpus: SMAT
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

---
schema_version: "1"
corpus: NetDefender
findings: 98
---

# NetDefender batch findings

## usage_mismatch:00497f3075c566e4a53cd01fd13dc5be:search

```yaml
regex_id: 00497f3075c566e4a53cd01fd13dc5be
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/APT_APT29_Grizzly_Steppe.yar:92:6"
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

## usage_mismatch:02913af8098f650826427dad171ab52c:search

```yaml
regex_id: 02913af8098f650826427dad171ab52c
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/APT_KeyBoy.yar:40:8"
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

## intent_mismatch:04f84e3f8179dc4ab8031f71b6d96a54:email

```yaml
regex_id: 04f84e3f8179dc4ab8031f71b6d96a54
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/TOOLKIT_FinFisher_.yar:85:8"
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

## intent_mismatch:05f377092b13d1e5fc284e437ab013da:email

```yaml
regex_id: 05f377092b13d1e5fc284e437ab013da
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/TOOLKIT_FinFisher_.yar:17:8"
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

## intent_mismatch:0a09bed36ecf1e6a7bb99bf87ae2c729:email

```yaml
regex_id: 0a09bed36ecf1e6a7bb99bf87ae2c729
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/TOOLKIT_FinFisher_.yar:87:8"
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

## intent_mismatch:0a185aa170209a249eec4e1cf21fb8a0:email

```yaml
regex_id: 0a185aa170209a249eec4e1cf21fb8a0
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/TOOLKIT_FinFisher_.yar:86:8"
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

## intent_mismatch:11fa37d165d7859f1ec717ba805ff9e7:email

```yaml
regex_id: 11fa37d165d7859f1ec717ba805ff9e7
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/TOOLKIT_FinFisher_.yar:85:8"
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

## usage_mismatch:141471318bb4d9cb4811e16ae1f80384:search

```yaml
regex_id: 141471318bb4d9cb4811e16ae1f80384
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/APT_KeyBoy.yar:42:8"
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

## intent_mismatch:173e66d69f71d991d4e3c5f8b2b35f6d:email

```yaml
regex_id: 173e66d69f71d991d4e3c5f8b2b35f6d
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/TOOLKIT_FinFisher_.yar:16:8"
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

## intent_mismatch:1a57cd4af7c51c1b983a3f9cadbdbaef:email

```yaml
regex_id: 1a57cd4af7c51c1b983a3f9cadbdbaef
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/TOOLKIT_FinFisher_.yar:87:8"
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

## usage_mismatch:1b6f7a18e6ab668c574587f053252afc:search

```yaml
regex_id: 1b6f7a18e6ab668c574587f053252afc
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/MALW_Miscelanea.yar:679:2"
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

## intent_mismatch:1d394ca6905d4274c226a485faa82792:email

```yaml
regex_id: 1d394ca6905d4274c226a485faa82792
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/TOOLKIT_FinFisher_.yar:86:8"
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

## usage_mismatch:1eeea75e1ff02300e490857c445e6094:search

```yaml
regex_id: 1eeea75e1ff02300e490857c445e6094
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/APT_Passcv.yar:158:6"
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

## usage_mismatch:1f4c4a145b9c2d228b4fa0477cf5dc68:search

```yaml
regex_id: 1f4c4a145b9c2d228b4fa0477cf5dc68
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/RANSOM_MS17-010_Wannacrypt.yar:172:6"
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

## usage_mismatch:21dd24097b129d6ef75192105fcb9128:search

```yaml
regex_id: 21dd24097b129d6ef75192105fcb9128
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/MALW_Miscelanea.yar:137:2"
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

## usage_mismatch:22564a452824dc75e40de0992689f964:search

```yaml
regex_id: 22564a452824dc75e40de0992689f964
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/APT_OPCleaver.yar:594:8"
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

## usage_mismatch:245845136413417af0fbdf9a42bd1705:search

```yaml
regex_id: 245845136413417af0fbdf9a42bd1705
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/RAT_Indetectables.yar:29:2"
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

## usage_mismatch:254f8859080351d497e3ccf77de2f909:search

```yaml
regex_id: 254f8859080351d497e3ccf77de2f909
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/APT_Poseidon_Group.yar:38:8"
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

## usage_mismatch:29d940cf9462f84fdc4f135404bdbb98:search

```yaml
regex_id: 29d940cf9462f84fdc4f135404bdbb98
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/MALW_Miscelanea.yar:679:2"
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

## usage_mismatch:2c924c254d76b58d3f75ba738281c474:search

```yaml
regex_id: 2c924c254d76b58d3f75ba738281c474
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/APT_KeyBoy.yar:43:8"
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

## usage_mismatch:2e6249bdd86f21a36daccda2a2b778b8:search

```yaml
regex_id: 2e6249bdd86f21a36daccda2a2b778b8
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/APT_OPCleaver.yar:594:8"
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

## usage_mismatch:2ebedd99c52540a53dc81a57fa70a1b4:search

```yaml
regex_id: 2ebedd99c52540a53dc81a57fa70a1b4
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/APT_APT29_Grizzly_Steppe.yar:89:6"
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

## usage_mismatch:2f32fff82812c6d91fae9c457466cee0:search

```yaml
regex_id: 2f32fff82812c6d91fae9c457466cee0
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/MALW_AlMashreq.yar:21:1"
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

## usage_mismatch:312db8a39f763395c1b154b0a0548390:search

```yaml
regex_id: 312db8a39f763395c1b154b0a0548390
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/APT_Derusbi.yar:263:8"
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

## usage_mismatch:31a8c9357bf4c8c1afaca84b86e96607:search

```yaml
regex_id: 31a8c9357bf4c8c1afaca84b86e96607
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/APT_OPCleaver.yar:236:4"
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

## usage_mismatch:34179c4cf6755516e135d57d448c9748:search

```yaml
regex_id: 34179c4cf6755516e135d57d448c9748
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/APT_Snowglobe_Babar.yar:32:8"
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

## usage_mismatch:3464646d178eaefa622c33381dc9c33f:search

```yaml
regex_id: 3464646d178eaefa622c33381dc9c33f
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/RANSOM_Petya_MS17_010.yar:14:6"
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

## usage_mismatch:35a86a668c83338612ddaaca33f97b78:search

```yaml
regex_id: 35a86a668c83338612ddaaca33f97b78
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/APT_Derusbi.yar:318:8"
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

## intent_mismatch:42f9beab471767648db2569a20c55cf8:email

```yaml
regex_id: 42f9beab471767648db2569a20c55cf8
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/TOOLKIT_FinFisher_.yar:87:8"
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

## usage_mismatch:498283bea962c84346b3044fa656eca7:search

```yaml
regex_id: 498283bea962c84346b3044fa656eca7
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/APT_KeyBoy.yar:43:8"
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

## intent_mismatch:4a32506852b3290db2630673b64c5ee9:email

```yaml
regex_id: 4a32506852b3290db2630673b64c5ee9
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/TOOLKIT_FinFisher_.yar:86:8"
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

## intent_mismatch:4bb5396ece60e76e646939201a499395:email

```yaml
regex_id: 4bb5396ece60e76e646939201a499395
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/TOOLKIT_FinFisher_.yar:16:8"
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

## usage_mismatch:4d609f794dcb85dec65e33644bf47053:search

```yaml
regex_id: 4d609f794dcb85dec65e33644bf47053
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/APT_eqgrp_apr17.yar:2120:6"
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

## usage_mismatch:53b70266e577fecd042434ac4444b49b:search

```yaml
regex_id: 53b70266e577fecd042434ac4444b49b
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/APT_Industroyer.yar:87:6"
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

## usage_mismatch:53d9cd98fdefa49aff0632daa60aa4d8:search

```yaml
regex_id: 53d9cd98fdefa49aff0632daa60aa4d8
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/MALW_Hsdfihdf_banking.yar:28:1"
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

## usage_mismatch:5711bfbca8bf4441ff2d197738c2161f:search

```yaml
regex_id: 5711bfbca8bf4441ff2d197738c2161f
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/APT_KeyBoy.yar:41:8"
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

## usage_mismatch:5a55077a6be3bc4effd88a3a9ba61b14:search

```yaml
regex_id: 5a55077a6be3bc4effd88a3a9ba61b14
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/APT_KeyBoy.yar:39:8"
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

## intent_mismatch:5f33046541500653aa31759a8e27bf7b:email

```yaml
regex_id: 5f33046541500653aa31759a8e27bf7b
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/TOOLKIT_FinFisher_.yar:16:8"
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

## intent_mismatch:613e4af10cd69dfcc467a65591b248b3:email

```yaml
regex_id: 613e4af10cd69dfcc467a65591b248b3
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/TOOLKIT_FinFisher_.yar:87:8"
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

## usage_mismatch:6315725b9555750132d28626b25d889f:search

```yaml
regex_id: 6315725b9555750132d28626b25d889f
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/APT_KeyBoy.yar:44:8"
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

## usage_mismatch:66e3387ba7a1e1ca9bb5635d9810f9c7:search

```yaml
regex_id: 66e3387ba7a1e1ca9bb5635d9810f9c7
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/APT_KeyBoy.yar:40:8"
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

## usage_mismatch:6708fab8aab22825f89f19b1b96a3a5f:search

```yaml
regex_id: 6708fab8aab22825f89f19b1b96a3a5f
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/APT_Industroyer.yar:87:6"
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

## intent_mismatch:68bd48da4159e2a486e005029587fd09:email

```yaml
regex_id: 68bd48da4159e2a486e005029587fd09
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/TOOLKIT_FinFisher_.yar:85:8"
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

## intent_mismatch:6c08debd572dcfffabb13e248c4275a5:email

```yaml
regex_id: 6c08debd572dcfffabb13e248c4275a5
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/TOOLKIT_FinFisher_.yar:17:8"
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

## usage_mismatch:6dcd7523af6ba344b74656ee1b340ad1:search

```yaml
regex_id: 6dcd7523af6ba344b74656ee1b340ad1
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/APT_Derusbi.yar:318:8"
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

## usage_mismatch:6de5fe2cc22d03dbe98e06a9915b965e:search

```yaml
regex_id: 6de5fe2cc22d03dbe98e06a9915b965e
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/RANSOM_MS17-010_Wannacrypt.yar:172:6"
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

## intent_mismatch:70a1a4421f250a4927e233b06da8cad2:email

```yaml
regex_id: 70a1a4421f250a4927e233b06da8cad2
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/TOOLKIT_FinFisher_.yar:15:8"
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

## usage_mismatch:776a92a0f37c36fc16b9b1248e67d49c:search

```yaml
regex_id: 776a92a0f37c36fc16b9b1248e67d49c
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/APT_Derusbi.yar:281:8"
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

## usage_mismatch:7842defdf77cb6e3b2c0a41c7e4bcd3a:search

```yaml
regex_id: 7842defdf77cb6e3b2c0a41c7e4bcd3a
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/RANSOM_Petya_MS17_010.yar:14:6"
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

## usage_mismatch:7baf27f7e00688c97fec721f5a42308f:search

```yaml
regex_id: 7baf27f7e00688c97fec721f5a42308f
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/RAT_PoisonIvy.yar:39:2"
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

## intent_mismatch:7f2ebd0d841473fe2a7c34875c4e2d09:email

```yaml
regex_id: 7f2ebd0d841473fe2a7c34875c4e2d09
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/TOOLKIT_FinFisher_.yar:17:8"
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

## intent_mismatch:81b3482c54b7bb60d59858c057d9a3ce:hostname

```yaml
regex_id: 81b3482c54b7bb60d59858c057d9a3ce
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/TOOLKIT_Chinese_Hacktools.yar:1876:2"
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

## usage_mismatch:83497b8faa090db2d09dce48dbdabcea:search

```yaml
regex_id: 83497b8faa090db2d09dce48dbdabcea
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/APT_APT29_Grizzly_Steppe.yar:89:6"
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

## intent_mismatch:863343bb095a9a6c1c4cff69a628f128:hostname

```yaml
regex_id: 863343bb095a9a6c1c4cff69a628f128
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/TOOLKIT_Chinese_Hacktools.yar:1876:2"
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

## intent_mismatch:87b020a3baef99e4531bbe5bb6b29b1d:email

```yaml
regex_id: 87b020a3baef99e4531bbe5bb6b29b1d
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/TOOLKIT_FinFisher_.yar:85:8"
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

## usage_mismatch:87d1882509fb16840e07b1ba6e77947f:search

```yaml
regex_id: 87d1882509fb16840e07b1ba6e77947f
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/APT_Regin.yar:341:8"
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

## usage_mismatch:89bab937b8fc47d5482089af36a9300a:search

```yaml
regex_id: 89bab937b8fc47d5482089af36a9300a
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/APT_ThreatGroup3390.yar:38:8"
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

## intent_mismatch:8a4e573c0b0e38384e09397d689d70fb:email

```yaml
regex_id: 8a4e573c0b0e38384e09397d689d70fb
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/TOOLKIT_FinFisher_.yar:16:8"
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

## intent_mismatch:8c23a4455b864b5ee2343d3a86081d6e:email

```yaml
regex_id: 8c23a4455b864b5ee2343d3a86081d6e
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/TOOLKIT_FinFisher_.yar:15:8"
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

## usage_mismatch:8ca419a21ee814f515c766356c0c2611:search

```yaml
regex_id: 8ca419a21ee814f515c766356c0c2611
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/APT_Poseidon_Group.yar:38:8"
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

## usage_mismatch:90d1cd6c2c3dc0dc041dff31de02b496:search

```yaml
regex_id: 90d1cd6c2c3dc0dc041dff31de02b496
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/APT_APT29_Grizzly_Steppe.yar:109:6"
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

## usage_mismatch:939a700a439b5cb199f5dcd21018a183:search

```yaml
regex_id: 939a700a439b5cb199f5dcd21018a183
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/RAT_Indetectables.yar:29:2"
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

## intent_mismatch:94c90feda2e2974b0fdbf5842183ec59:hostname

```yaml
regex_id: 94c90feda2e2974b0fdbf5842183ec59
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/TOOLKIT_Chinese_Hacktools.yar:1874:2"
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

## usage_mismatch:97e4d6805967f63d6f5923609737e17b:search

```yaml
regex_id: 97e4d6805967f63d6f5923609737e17b
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/APT_KeyBoy.yar:41:8"
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

## intent_mismatch:a1829d7d72503cdd51cfb40225276213:email

```yaml
regex_id: a1829d7d72503cdd51cfb40225276213
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/TOOLKIT_FinFisher_.yar:86:8"
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

## usage_mismatch:aa39098a7663810abe649d15dd8160d2:search

```yaml
regex_id: aa39098a7663810abe649d15dd8160d2
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/APT_ThreatGroup3390.yar:38:8"
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

## usage_mismatch:ae9d6ae664fcfc12b4aba90bfaf00e98:search

```yaml
regex_id: ae9d6ae664fcfc12b4aba90bfaf00e98
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/APT_Snowglobe_Babar.yar:32:8"
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

## usage_mismatch:af8ec3ee1d3efd405a07f2fe191c168a:search

```yaml
regex_id: af8ec3ee1d3efd405a07f2fe191c168a
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/APT_Derusbi.yar:263:8"
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

## usage_mismatch:b2b9664bca90b17ca66aa92705d995d0:search

```yaml
regex_id: b2b9664bca90b17ca66aa92705d995d0
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/APT_KeyBoy.yar:42:8"
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

## usage_mismatch:b395c26ec751a18ffd5c8b59c7b94fa2:search

```yaml
regex_id: b395c26ec751a18ffd5c8b59c7b94fa2
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/APT_Regin.yar:341:8"
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

## usage_mismatch:b54fccd1bc67f0d3a5fbda1347eb5089:search

```yaml
regex_id: b54fccd1bc67f0d3a5fbda1347eb5089
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/RAT_PoisonIvy.yar:39:2"
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

## usage_mismatch:b617ede1624ffa1f5b29d8f781d4262e:search

```yaml
regex_id: b617ede1624ffa1f5b29d8f781d4262e
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/APT_eqgrp_apr17.yar:2120:6"
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

## usage_mismatch:c62ab8022c14bd139bbf47c8608c7513:search

```yaml
regex_id: c62ab8022c14bd139bbf47c8608c7513
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/APT_KeyBoy.yar:44:8"
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

## intent_mismatch:c8aa749c51972c4661416bd6dba28b8d:email

```yaml
regex_id: c8aa749c51972c4661416bd6dba28b8d
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/TOOLKIT_FinFisher_.yar:15:8"
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

## intent_mismatch:cac35e28032ab499ebccb7b892d2986b:hostname

```yaml
regex_id: cac35e28032ab499ebccb7b892d2986b
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/TOOLKIT_Chinese_Hacktools.yar:1874:2"
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

## usage_mismatch:caed124a19429f77799fa92f68cf1d63:search

```yaml
regex_id: caed124a19429f77799fa92f68cf1d63
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/RANSOM_MS17-010_Wannacrypt.yar:173:6"
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

## usage_mismatch:cf439a892637cea63a4beb284020400e:search

```yaml
regex_id: cf439a892637cea63a4beb284020400e
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/RANSOM_Petya_MS17_010.yar:14:6"
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

## usage_mismatch:d3073f629bf1a45ebf7cc25fb79ecc0e:search

```yaml
regex_id: d3073f629bf1a45ebf7cc25fb79ecc0e
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/general.yara:13:2"
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

## usage_mismatch:d67a38119cfa078f9fdb8b0579957b1f:search

```yaml
regex_id: d67a38119cfa078f9fdb8b0579957b1f
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/MALW_AlMashreq.yar:21:1"
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

## usage_mismatch:d6b3da7fd99528b394e4d6eaa143f9ed:search

```yaml
regex_id: d6b3da7fd99528b394e4d6eaa143f9ed
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/RANSOM_Petya_MS17_010.yar:14:6"
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

## usage_mismatch:df32e10dfe8f9777e6b5cdbc2f996f61:search

```yaml
regex_id: df32e10dfe8f9777e6b5cdbc2f996f61
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/general.yara:13:2"
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

## intent_mismatch:e05349ddf00c5c13753b6029419cdadb:email

```yaml
regex_id: e05349ddf00c5c13753b6029419cdadb
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/TOOLKIT_FinFisher_.yar:15:8"
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

## usage_mismatch:e1f08d61a07931c6f1a240084c64d11b:search

```yaml
regex_id: e1f08d61a07931c6f1a240084c64d11b
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/APT_Passcv.yar:158:6"
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

## usage_mismatch:e26b91ca8b53ee7988d6fdd446fdda9d:search

```yaml
regex_id: e26b91ca8b53ee7988d6fdd446fdda9d
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/TOOLKIT_THOR_HackTools.yar:2775:2"
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

## usage_mismatch:e61daa55f7852806def632713d47a187:search

```yaml
regex_id: e61daa55f7852806def632713d47a187
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/MALW_Hsdfihdf_banking.yar:28:1"
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

## intent_mismatch:e6c0d25e554785ac55dd31be92d257cb:email

```yaml
regex_id: e6c0d25e554785ac55dd31be92d257cb
schema_version: "1"
kind: intent_mismatch
corpus: NetDefender
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/TOOLKIT_FinFisher_.yar:17:8"
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

## usage_mismatch:e85ee069696f58ed8cd22c6c54e024dd:search

```yaml
regex_id: e85ee069696f58ed8cd22c6c54e024dd
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/APT_APT29_Grizzly_Steppe.yar:92:6"
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

## usage_mismatch:e8bf647464cb785d3bc3dc093da72ed5:search

```yaml
regex_id: e8bf647464cb785d3bc3dc093da72ed5
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/MALW_Miscelanea.yar:137:2"
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

## usage_mismatch:ec722859441ae1bc59ed9e4b85374988:search

```yaml
regex_id: ec722859441ae1bc59ed9e4b85374988
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/RANSOM_MS17-010_Wannacrypt.yar:173:6"
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

## usage_mismatch:f0f5f2b63796cc160b7471fc959ce021:search

```yaml
regex_id: f0f5f2b63796cc160b7471fc959ce021
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/APT_KeyBoy.yar:39:8"
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

## usage_mismatch:f47bb35abfbeb4b1630ad2a56684cbaf:search

```yaml
regex_id: f47bb35abfbeb4b1630ad2a56684cbaf
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/APT_APT29_Grizzly_Steppe.yar:109:6"
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

## usage_mismatch:f7aa1ee22b43d84f9d29b28a6864a711:search

```yaml
regex_id: f7aa1ee22b43d84f9d29b28a6864a711
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/TOOLKIT_THOR_HackTools.yar:2775:2"
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

## usage_mismatch:f8824d316a4075586689b52369dcd264:search

```yaml
regex_id: f8824d316a4075586689b52369dcd264
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/large/APT_OPCleaver.yar:236:4"
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

## usage_mismatch:fb6782d7958a3bb19029db1ce4fa9b08:search

```yaml
regex_id: fb6782d7958a3bb19029db1ce4fa9b08
schema_version: "1"
kind: usage_mismatch
corpus: NetDefender
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/NetDefender/rules/rules/malware/APT_Derusbi.yar:281:8"
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

## property:inventory:rc-shape1-injection-alphabet:rc-shape1-injection-alphabet

```yaml
regex_id: "inventory:rc-shape1-injection-alphabet"
schema_version: "1"
kind: property
corpus: NetDefender
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
corpus: NetDefender
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
corpus: NetDefender
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
corpus: NetDefender
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

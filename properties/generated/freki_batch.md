---
schema_version: "1"
corpus: freki
findings: 51
---

# freki batch findings

## usage_mismatch:065d2986127ab541943ec4aa5926fc80:search

```yaml
regex_id: 065d2986127ab541943ec4aa5926fc80
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/Operation_Blockbuster/general.yara:13:2"
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

## usage_mismatch:09c2adad661f57ed1d93b980637838b3:search

```yaml
regex_id: 09c2adad661f57ed1d93b980637838b3
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/APT_APT29_Grizzly_Steppe.yar:109:6"
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

## usage_mismatch:0ccc4e72a88a0e14eb90e2eecc86d2b6:search

```yaml
regex_id: 0ccc4e72a88a0e14eb90e2eecc86d2b6
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/RAT_Indetectables.yar:29:2"
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

## usage_mismatch:199048bf80f13fb83cc0e1eb1a5a8337:search

```yaml
regex_id: 199048bf80f13fb83cc0e1eb1a5a8337
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/APT_Regin.yar:341:8"
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

## usage_mismatch:1ee98e802a32b1e498b43ddb454c9b8f:search

```yaml
regex_id: 1ee98e802a32b1e498b43ddb454c9b8f
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/MALW_Miscelanea.yar:679:2"
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

## usage_mismatch:2ed4482ead6b0506e45223d0dc328cc2:search

```yaml
regex_id: 2ed4482ead6b0506e45223d0dc328cc2
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/TOOLKIT_THOR_HackTools.yar:2775:2"
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

## intent_mismatch:38a82d172e5e7733e2db758fbbf45f3a:email

```yaml
regex_id: 38a82d172e5e7733e2db758fbbf45f3a
schema_version: "1"
kind: intent_mismatch
corpus: freki
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/TOOLKIT_FinFisher_.yar:16:8"
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

## usage_mismatch:3be249e3b799fdf8e34659102a55f3c8:search

```yaml
regex_id: 3be249e3b799fdf8e34659102a55f3c8
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/MALW_AlMashreq.yar:21:1"
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

## usage_mismatch:3defa77504eee8ffb44e5ffa9af1b266:search

```yaml
regex_id: 3defa77504eee8ffb44e5ffa9af1b266
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/APT_eqgrp_apr17.yar:2120:6"
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

## usage_mismatch:422110803d2404dc4cd9e7b04a953994:search

```yaml
regex_id: 422110803d2404dc4cd9e7b04a953994
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/MALW_Hsdfihdf_banking.yar:28:1"
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

## intent_mismatch:45f34b64a2cb6538a216d0a367613738:email

```yaml
regex_id: 45f34b64a2cb6538a216d0a367613738
schema_version: "1"
kind: intent_mismatch
corpus: freki
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/TOOLKIT_FinFisher_.yar:87:8"
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

## intent_mismatch:465dd709523907b1b19827c8f317908a:email

```yaml
regex_id: 465dd709523907b1b19827c8f317908a
schema_version: "1"
kind: intent_mismatch
corpus: freki
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/TOOLKIT_FinFisher_.yar:17:8"
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

## usage_mismatch:47c90d24200df73ce5b6c5bd985bfc7d:search

```yaml
regex_id: 47c90d24200df73ce5b6c5bd985bfc7d
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/RANSOM_Petya_MS17_010.yar:14:6"
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

## usage_mismatch:4a9e437fc8f94365a5eb04f1c0c67bbd:search

```yaml
regex_id: 4a9e437fc8f94365a5eb04f1c0c67bbd
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/APT_KeyBoy.yar:40:8"
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

## intent_mismatch:500a89bf4427b1c891487fdcb36bfe3e:email

```yaml
regex_id: 500a89bf4427b1c891487fdcb36bfe3e
schema_version: "1"
kind: intent_mismatch
corpus: freki
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/TOOLKIT_FinFisher_.yar:87:8"
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

## intent_mismatch:60979e76f0d7859d24bb7aa1610eae36:email

```yaml
regex_id: 60979e76f0d7859d24bb7aa1610eae36
schema_version: "1"
kind: intent_mismatch
corpus: freki
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/TOOLKIT_FinFisher_.yar:17:8"
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

## usage_mismatch:64ae1fad5d2292d176488a23508e298c:search

```yaml
regex_id: 64ae1fad5d2292d176488a23508e298c
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/APT_KeyBoy.yar:41:8"
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

## intent_mismatch:6790109e248abeeb60a1a671f37e820b:email

```yaml
regex_id: 6790109e248abeeb60a1a671f37e820b
schema_version: "1"
kind: intent_mismatch
corpus: freki
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/TOOLKIT_FinFisher_.yar:15:8"
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

## usage_mismatch:6bad7260d2c8073e9f5c4e639fe97d4d:search

```yaml
regex_id: 6bad7260d2c8073e9f5c4e639fe97d4d
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/APT_Poseidon_Group.yar:38:8"
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

## intent_mismatch:702d5cdfd74decca9975d969ea706434:email

```yaml
regex_id: 702d5cdfd74decca9975d969ea706434
schema_version: "1"
kind: intent_mismatch
corpus: freki
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/TOOLKIT_FinFisher_.yar:16:8"
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

## usage_mismatch:72342ed4587fdd644635f67ae6bfd92a:search

```yaml
regex_id: 72342ed4587fdd644635f67ae6bfd92a
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/APT_KeyBoy.yar:43:8"
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

## usage_mismatch:7244821f07c4084cfa809152e7e8163c:search

```yaml
regex_id: 7244821f07c4084cfa809152e7e8163c
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/APT_Derusbi.yar:281:8"
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

## usage_mismatch:870a6644ef31e4a7eb01cc874c38f477:search

```yaml
regex_id: 870a6644ef31e4a7eb01cc874c38f477
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/RANSOM_MS17-010_Wannacrypt.yar:172:6"
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

## intent_mismatch:8dbba0c89b43d2dfeb18f7704acb08e2:email

```yaml
regex_id: 8dbba0c89b43d2dfeb18f7704acb08e2
schema_version: "1"
kind: intent_mismatch
corpus: freki
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/TOOLKIT_FinFisher_.yar:86:8"
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

## usage_mismatch:8ec99dc51c8f16a897e590e4fbc7586f:search

```yaml
regex_id: 8ec99dc51c8f16a897e590e4fbc7586f
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/MALW_Miscelanea.yar:137:2"
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

## intent_mismatch:9241dc01ee39f8e3d22150401c8cdbf4:email

```yaml
regex_id: 9241dc01ee39f8e3d22150401c8cdbf4
schema_version: "1"
kind: intent_mismatch
corpus: freki
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/TOOLKIT_FinFisher_.yar:85:8"
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

## usage_mismatch:96a11310c5593465da720c0879a0b393:search

```yaml
regex_id: 96a11310c5593465da720c0879a0b393
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/APT_APT29_Grizzly_Steppe.yar:92:6"
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

## usage_mismatch:ab6b5afc46a86c5bb8b18405dbb8f223:search

```yaml
regex_id: ab6b5afc46a86c5bb8b18405dbb8f223
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/APT_OPCleaver.yar:236:4"
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

## intent_mismatch:b53fc8e190a80ad4baacdecc06310aa4:hostname

```yaml
regex_id: b53fc8e190a80ad4baacdecc06310aa4
schema_version: "1"
kind: intent_mismatch
corpus: freki
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/TOOLKIT_Chinese_Hacktools.yar:1876:2"
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

## usage_mismatch:bc71d504c3434adc2f173f29c3b32e89:search

```yaml
regex_id: bc71d504c3434adc2f173f29c3b32e89
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/APT_Snowglobe_Babar.yar:32:8"
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

## usage_mismatch:c349e7e113f9aebdda84e5356b34c62d:search

```yaml
regex_id: c349e7e113f9aebdda84e5356b34c62d
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/APT_APT29_Grizzly_Steppe.yar:89:6"
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

## usage_mismatch:cf2b14878802259b26e0a72848d4c22d:search

```yaml
regex_id: cf2b14878802259b26e0a72848d4c22d
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/RANSOM_MS17-010_Wannacrypt.yar:173:6"
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

## usage_mismatch:cf81bc5bb790becc3b18266eb431200b:search

```yaml
regex_id: cf81bc5bb790becc3b18266eb431200b
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/APT_KeyBoy.yar:42:8"
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

## usage_mismatch:cfb87f081910bf3f12ed68b5d269ebe9:search

```yaml
regex_id: cfb87f081910bf3f12ed68b5d269ebe9
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/APT_Derusbi.yar:263:8"
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

## intent_mismatch:d268f6aa8a81a4ea6002e6e193dc0c10:hostname

```yaml
regex_id: d268f6aa8a81a4ea6002e6e193dc0c10
schema_version: "1"
kind: intent_mismatch
corpus: freki
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/TOOLKIT_Chinese_Hacktools.yar:1874:2"
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

## usage_mismatch:e0348e2d5efbf570a9af41159043a3b2:search

```yaml
regex_id: e0348e2d5efbf570a9af41159043a3b2
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/RANSOM_Petya_MS17_010.yar:14:6"
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

## usage_mismatch:e0639e5ca913530341f807070c0bed39:search

```yaml
regex_id: e0639e5ca913530341f807070c0bed39
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/APT_Industroyer.yar:87:6"
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

## usage_mismatch:e0f681d8b5db0ece5a125508b210ff33:search

```yaml
regex_id: e0f681d8b5db0ece5a125508b210ff33
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/APT_OPCleaver.yar:594:8"
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

## intent_mismatch:e110a1c0536cb4aea21b31ddc3d271f4:email

```yaml
regex_id: e110a1c0536cb4aea21b31ddc3d271f4
schema_version: "1"
kind: intent_mismatch
corpus: freki
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/TOOLKIT_FinFisher_.yar:86:8"
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

## usage_mismatch:e748575a1f19856489351cba77a05faf:search

```yaml
regex_id: e748575a1f19856489351cba77a05faf
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/APT_KeyBoy.yar:39:8"
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

## usage_mismatch:e7be48c14db1cd05b6e3f7247b7ba4bf:search

```yaml
regex_id: e7be48c14db1cd05b6e3f7247b7ba4bf
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/APT_ThreatGroup3390.yar:38:8"
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

## usage_mismatch:edc7a771b5c7a398cd9c30cce53cbc0a:search

```yaml
regex_id: edc7a771b5c7a398cd9c30cce53cbc0a
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/APT_Derusbi.yar:318:8"
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

## intent_mismatch:ef80fb7e22a1680030c05da653b90e19:email

```yaml
regex_id: ef80fb7e22a1680030c05da653b90e19
schema_version: "1"
kind: intent_mismatch
corpus: freki
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/TOOLKIT_FinFisher_.yar:85:8"
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

## usage_mismatch:f2dd844d3afba8466170e27c0e4a2e89:search

```yaml
regex_id: f2dd844d3afba8466170e27c0e4a2e89
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/APT_Passcv.yar:158:6"
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

## usage_mismatch:f6639c9514e7eea467838c3209e39fd9:search

```yaml
regex_id: f6639c9514e7eea467838c3209e39fd9
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/RAT_PoisonIvy.yar:39:2"
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

## usage_mismatch:f679073655bfdfdb389d2479fc15ef0c:search

```yaml
regex_id: f679073655bfdfdb389d2479fc15ef0c
schema_version: "1"
kind: usage_mismatch
corpus: freki
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/APT_KeyBoy.yar:44:8"
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

## intent_mismatch:f68e4ba4a8a4ccbcdcfa5c9f0acaf62d:email

```yaml
regex_id: f68e4ba4a8a4ccbcdcfa5c9f0acaf62d
schema_version: "1"
kind: intent_mismatch
corpus: freki
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/freki/rules/freki/app/core/yara_rules/malware/TOOLKIT_FinFisher_.yar:15:8"
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

## property:inventory:rc-shape1-injection-alphabet:rc-shape1-injection-alphabet

```yaml
regex_id: "inventory:rc-shape1-injection-alphabet"
schema_version: "1"
kind: property
corpus: freki
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
corpus: freki
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
corpus: freki
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
corpus: freki
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

---
schema_version: "1"
corpus: Antivirus
findings: 50
---

# Antivirus batch findings

## usage_mismatch:0079f0adea27b96778d4391389263dc3:search

```yaml
regex_id: 0079f0adea27b96778d4391389263dc3
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/APT_KeyBoy.yar:41:8"
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

## usage_mismatch:1c3b2ccfde427cebb10df12b61ad87fb:search

```yaml
regex_id: 1c3b2ccfde427cebb10df12b61ad87fb
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/APT_Regin.yar:341:8"
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

## intent_mismatch:1caf6c902fd1a1cfc1529a92fbce37c8:email

```yaml
regex_id: 1caf6c902fd1a1cfc1529a92fbce37c8
schema_version: "1"
kind: intent_mismatch
corpus: Antivirus
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/TOOLKIT_FinFisher_.yar:85:8"
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

## usage_mismatch:1e494ec30df42baaabcbcc35ae64bb94:search

```yaml
regex_id: 1e494ec30df42baaabcbcc35ae64bb94
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/APT_OPCleaver.yar:236:4"
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

## usage_mismatch:211275522678e27b9bbd4f46a1d50bae:search

```yaml
regex_id: 211275522678e27b9bbd4f46a1d50bae
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/APT_Industroyer.yar:87:6"
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

## usage_mismatch:26557b122fe978fce6017e322c0eae2e:search

```yaml
regex_id: 26557b122fe978fce6017e322c0eae2e
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/APT_KeyBoy.yar:43:8"
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

## usage_mismatch:27f0409385363734c266764dbf40d13a:search

```yaml
regex_id: 27f0409385363734c266764dbf40d13a
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/APT_eqgrp_apr17.yar:2120:6"
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

## usage_mismatch:2cf1d33b8d6338588bc3a7c6ae09d745:search

```yaml
regex_id: 2cf1d33b8d6338588bc3a7c6ae09d745
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/APT_Derusbi.yar:263:8"
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

## intent_mismatch:32a89563a25d40a39c4ae2b118ff4fec:email

```yaml
regex_id: 32a89563a25d40a39c4ae2b118ff4fec
schema_version: "1"
kind: intent_mismatch
corpus: Antivirus
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/TOOLKIT_FinFisher_.yar:16:8"
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

## usage_mismatch:36f9e711ebfa396c9a1ea1cbc84b448c:search

```yaml
regex_id: 36f9e711ebfa396c9a1ea1cbc84b448c
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/APT_KeyBoy.yar:42:8"
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

## usage_mismatch:492be6b5a357b785b5c122721d3918ad:search

```yaml
regex_id: 492be6b5a357b785b5c122721d3918ad
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/RANSOM_Petya_MS17_010.yar:14:6"
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

## usage_mismatch:4e3603dfdb742698363243984d514650:search

```yaml
regex_id: 4e3603dfdb742698363243984d514650
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/APT_APT29_Grizzly_Steppe.yar:92:6"
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

## usage_mismatch:5d2f13164428cfb855ca9cc5ffeacedf:search

```yaml
regex_id: 5d2f13164428cfb855ca9cc5ffeacedf
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/APT_APT29_Grizzly_Steppe.yar:109:6"
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

## usage_mismatch:7360437a963cd51b75d3ae99cdc0aee7:search

```yaml
regex_id: 7360437a963cd51b75d3ae99cdc0aee7
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/APT_KeyBoy.yar:44:8"
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

## usage_mismatch:81758c360d9b21717e7401173b570192:search

```yaml
regex_id: 81758c360d9b21717e7401173b570192
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/MALW_Hsdfihdf_banking.yar:28:1"
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

## intent_mismatch:84392126f0a5a035aa7d32be759e2372:email

```yaml
regex_id: 84392126f0a5a035aa7d32be759e2372
schema_version: "1"
kind: intent_mismatch
corpus: Antivirus
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/TOOLKIT_FinFisher_.yar:87:8"
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

## usage_mismatch:88acf73a14bbbadd30cd98f607edc2d3:search

```yaml
regex_id: 88acf73a14bbbadd30cd98f607edc2d3
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/APT_KeyBoy.yar:39:8"
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

## intent_mismatch:88f920a06842ce53ede9211323a006cf:email

```yaml
regex_id: 88f920a06842ce53ede9211323a006cf
schema_version: "1"
kind: intent_mismatch
corpus: Antivirus
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/TOOLKIT_FinFisher_.yar:16:8"
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

## intent_mismatch:8cd76c75c07682635d30d0a99ac95a13:email

```yaml
regex_id: 8cd76c75c07682635d30d0a99ac95a13
schema_version: "1"
kind: intent_mismatch
corpus: Antivirus
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/TOOLKIT_FinFisher_.yar:87:8"
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

## usage_mismatch:9051b97a3d4620a2e6cca917cf6937a8:search

```yaml
regex_id: 9051b97a3d4620a2e6cca917cf6937a8
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/APT_Snowglobe_Babar.yar:32:8"
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

## usage_mismatch:922340093cad9f9df65a03e136e282f2:search

```yaml
regex_id: 922340093cad9f9df65a03e136e282f2
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/APT_Poseidon_Group.yar:38:8"
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

## usage_mismatch:92327bc51094bfda1b0dcfcbb95da8ab:search

```yaml
regex_id: 92327bc51094bfda1b0dcfcbb95da8ab
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/RAT_PoisonIvy.yar:39:2"
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

## intent_mismatch:94fd4d1f7ffa82157cb01f3c7d1ed63c:email

```yaml
regex_id: 94fd4d1f7ffa82157cb01f3c7d1ed63c
schema_version: "1"
kind: intent_mismatch
corpus: Antivirus
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/TOOLKIT_FinFisher_.yar:86:8"
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

## usage_mismatch:99ee12107064eb1fd36339ede3f0e31e:search

```yaml
regex_id: 99ee12107064eb1fd36339ede3f0e31e
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/APT_KeyBoy.yar:40:8"
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

## usage_mismatch:a5e8f21fac415fbd5ea5815476846bcb:search

```yaml
regex_id: a5e8f21fac415fbd5ea5815476846bcb
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/TOOLKIT_THOR_HackTools.yar:2775:2"
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

## usage_mismatch:ab5a50b9591195ad56801f7340914944:search

```yaml
regex_id: ab5a50b9591195ad56801f7340914944
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/RANSOM_MS17-010_Wannacrypt.yar:172:6"
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

## usage_mismatch:ad4d54d48ff338e788eb2a3d292dfa3e:search

```yaml
regex_id: ad4d54d48ff338e788eb2a3d292dfa3e
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/MALW_Miscelanea.yar:137:2"
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

## intent_mismatch:b36853da4befcb904e622644de61dcd8:hostname

```yaml
regex_id: b36853da4befcb904e622644de61dcd8
schema_version: "1"
kind: intent_mismatch
corpus: Antivirus
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/TOOLKIT_Chinese_Hacktools.yar:1876:2"
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

## intent_mismatch:b8ba2f60ed9e23ea16d6c5c062e822cf:email

```yaml
regex_id: b8ba2f60ed9e23ea16d6c5c062e822cf
schema_version: "1"
kind: intent_mismatch
corpus: Antivirus
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/TOOLKIT_FinFisher_.yar:15:8"
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

## usage_mismatch:b99f60e6270443d14a6c8a2d9c8daa77:search

```yaml
regex_id: b99f60e6270443d14a6c8a2d9c8daa77
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/RAT_Indetectables.yar:29:2"
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

## usage_mismatch:bbb8b3dad5da30dc1b1fa43df1f843fd:search

```yaml
regex_id: bbb8b3dad5da30dc1b1fa43df1f843fd
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/APT_ThreatGroup3390.yar:38:8"
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

## intent_mismatch:bd2623875b24e026e4c5b382998b13d5:email

```yaml
regex_id: bd2623875b24e026e4c5b382998b13d5
schema_version: "1"
kind: intent_mismatch
corpus: Antivirus
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/TOOLKIT_FinFisher_.yar:85:8"
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

## intent_mismatch:ca6b81cd46a1ba9a0af63bd981ae92d8:email

```yaml
regex_id: ca6b81cd46a1ba9a0af63bd981ae92d8
schema_version: "1"
kind: intent_mismatch
corpus: Antivirus
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/TOOLKIT_FinFisher_.yar:15:8"
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

## usage_mismatch:caf1fe4d15d41756ff8f6ba4ba36d7bb:search

```yaml
regex_id: caf1fe4d15d41756ff8f6ba4ba36d7bb
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/MALW_AlMashreq.yar:21:1"
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

## usage_mismatch:d208235df89c6879905edb2f4b105c9d:search

```yaml
regex_id: d208235df89c6879905edb2f4b105c9d
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/APT_OPCleaver.yar:594:8"
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

## usage_mismatch:d2e0c8ef423a6569d3ae25be76077246:search

```yaml
regex_id: d2e0c8ef423a6569d3ae25be76077246
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/APT_Passcv.yar:158:6"
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

## usage_mismatch:d4cd16a1a17b36ee209d3ee6cd3bd11a:search

```yaml
regex_id: d4cd16a1a17b36ee209d3ee6cd3bd11a
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/APT_Derusbi.yar:281:8"
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

## usage_mismatch:d8e2221fbbbb9d2463150501e59e5440:search

```yaml
regex_id: d8e2221fbbbb9d2463150501e59e5440
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/APT_APT29_Grizzly_Steppe.yar:89:6"
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

## intent_mismatch:dcfca87f902a049289c4a76df5a5df30:email

```yaml
regex_id: dcfca87f902a049289c4a76df5a5df30
schema_version: "1"
kind: intent_mismatch
corpus: Antivirus
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/TOOLKIT_FinFisher_.yar:17:8"
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

## intent_mismatch:ea9c57e19e15adcac85b2801ec6f6cd1:hostname

```yaml
regex_id: ea9c57e19e15adcac85b2801ec6f6cd1
schema_version: "1"
kind: intent_mismatch
corpus: Antivirus
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/TOOLKIT_Chinese_Hacktools.yar:1874:2"
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

## intent_mismatch:eaf72034663dbc6a015112442d965d22:email

```yaml
regex_id: eaf72034663dbc6a015112442d965d22
schema_version: "1"
kind: intent_mismatch
corpus: Antivirus
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/TOOLKIT_FinFisher_.yar:86:8"
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

## usage_mismatch:ecdf8919cb3d5363570598a582be96cb:search

```yaml
regex_id: ecdf8919cb3d5363570598a582be96cb
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/APT_Derusbi.yar:318:8"
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

## usage_mismatch:f0a4584bf2035296f4fc4c22e8b87297:search

```yaml
regex_id: f0a4584bf2035296f4fc4c22e8b87297
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/MALW_Miscelanea.yar:679:2"
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

## usage_mismatch:f736493baafd2447cf3a447ab7b83dc6:search

```yaml
regex_id: f736493baafd2447cf3a447ab7b83dc6
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/RANSOM_Petya_MS17_010.yar:14:6"
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

## usage_mismatch:f847838da8778579a677417a73a76cdf:search

```yaml
regex_id: f847838da8778579a677417a73a76cdf
schema_version: "1"
kind: usage_mismatch
corpus: Antivirus
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/RANSOM_MS17-010_Wannacrypt.yar:173:6"
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

## intent_mismatch:f8ce1c9cbbb4931c2d77465d4f811209:email

```yaml
regex_id: f8ce1c9cbbb4931c2d77465d4f811209
schema_version: "1"
kind: intent_mismatch
corpus: Antivirus
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Antivirus/rules/TOOLKIT_FinFisher_.yar:17:8"
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

## property:inventory:rc-shape1-injection-alphabet:rc-shape1-injection-alphabet

```yaml
regex_id: "inventory:rc-shape1-injection-alphabet"
schema_version: "1"
kind: property
corpus: Antivirus
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
corpus: Antivirus
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
corpus: Antivirus
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
corpus: Antivirus
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

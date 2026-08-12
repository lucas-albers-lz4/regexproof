---
schema_version: "1"
corpus: PEpper
findings: 64
---

# PEpper batch findings

## intent_mismatch:0366e06083c255ca085564072c0df24c:email

```yaml
regex_id: 0366e06083c255ca085564072c0df24c
schema_version: "1"
kind: intent_mismatch
corpus: PEpper
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/TOOLKIT_FinFisher_.yar:15:8"
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

## usage_mismatch:05f549d6ac06ae073d37b7d92e4e4108:search

```yaml
regex_id: 05f549d6ac06ae073d37b7d92e4e4108
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/APT_Derusbi.yar:263:8"
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

## intent_mismatch:06d0523a634843741d2b65a2bd5bfac0:email

```yaml
regex_id: 06d0523a634843741d2b65a2bd5bfac0
schema_version: "1"
kind: intent_mismatch
corpus: PEpper
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/TOOLKIT_FinFisher_.yar:16:8"
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

## usage_mismatch:0b2a0e4d7ac64de3f75addced2b68673:search

```yaml
regex_id: 0b2a0e4d7ac64de3f75addced2b68673
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/APT_KeyBoy.yar:44:8"
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

## usage_mismatch:16000a4d6f92f5b6300317ca4fc85ead:search

```yaml
regex_id: 16000a4d6f92f5b6300317ca4fc85ead
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/APT_ThreatGroup3390.yar:38:8"
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

## usage_mismatch:18a40a725aaa2aeda8c7a586e519c024:search

```yaml
regex_id: 18a40a725aaa2aeda8c7a586e519c024
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/APT_KeyBoy.yar:43:8"
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

## usage_mismatch:1b0f8c5c7f0d0198adc64805d8292635:search

```yaml
regex_id: 1b0f8c5c7f0d0198adc64805d8292635
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/APT_eqgrp_apr17.yar:2120:6"
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

## intent_mismatch:1b2a253ac5daaaba33b3b7ce89ddc7dd:hostname

```yaml
regex_id: 1b2a253ac5daaaba33b3b7ce89ddc7dd
schema_version: "1"
kind: intent_mismatch
corpus: PEpper
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/TOOLKIT_Chinese_Hacktools.yar:1874:2"
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

## usage_mismatch:20702341b1388820cc5d2f71f3216b3c:search

```yaml
regex_id: 20702341b1388820cc5d2f71f3216b3c
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/Webshells/WShell_THOR_Webshells.yar:7573:2"
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

## usage_mismatch:2563bf967141d37c45343459a5a26199:search

```yaml
regex_id: 2563bf967141d37c45343459a5a26199
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/APT_KeyBoy.yar:42:8"
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

## usage_mismatch:2a889f6dff4c6c0924f00bc8fc3f42ae:search

```yaml
regex_id: 2a889f6dff4c6c0924f00bc8fc3f42ae
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/Webshells/WShell_THOR_Webshells.yar:50:2"
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

## usage_mismatch:2c48f379c73b8cc729a599843b5cdc77:search

```yaml
regex_id: 2c48f379c73b8cc729a599843b5cdc77
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/Webshells/WShell_THOR_Webshells.yar:3813:2"
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

## usage_mismatch:337949a6ac615c186538dfbe42e2ed9e:search

```yaml
regex_id: 337949a6ac615c186538dfbe42e2ed9e
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/Webshells/WShell_PHP_in_images.yar:12:8"
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

## usage_mismatch:3850c7c0462f79a24c811f15d3026e6f:search

```yaml
regex_id: 3850c7c0462f79a24c811f15d3026e6f
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/TOOLKIT_THOR_HackTools.yar:2775:2"
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

## intent_mismatch:3c79aa9ba50ea2c2f139c27f59f07814:email

```yaml
regex_id: 3c79aa9ba50ea2c2f139c27f59f07814
schema_version: "1"
kind: intent_mismatch
corpus: PEpper
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/TOOLKIT_FinFisher_.yar:86:8"
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

## usage_mismatch:41ad7adb33e922d8237999bd99ab2d4d:search

```yaml
regex_id: 41ad7adb33e922d8237999bd99ab2d4d
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/APT_Industroyer.yar:87:6"
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

## intent_mismatch:451a64e96e4b19896f2fc8ba81b94ca3:email

```yaml
regex_id: 451a64e96e4b19896f2fc8ba81b94ca3
schema_version: "1"
kind: intent_mismatch
corpus: PEpper
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/TOOLKIT_FinFisher_.yar:15:8"
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

## usage_mismatch:475dd4321f7535fb224b830bd3e9903f:search

```yaml
regex_id: 475dd4321f7535fb224b830bd3e9903f
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/RAT_Indetectables.yar:29:2"
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

## usage_mismatch:4b972e48dd469c2005705dc8f199be20:search

```yaml
regex_id: 4b972e48dd469c2005705dc8f199be20
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/Webshells/WShell_THOR_Webshells.yar:6554:2"
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

## usage_mismatch:52904006c1bfe8cb466cbcba18361737:search

```yaml
regex_id: 52904006c1bfe8cb466cbcba18361737
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/MALW_Hsdfihdf_banking.yar:28:1"
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

## usage_mismatch:54453ed69ceacb7926639adc87f1b2df:search

```yaml
regex_id: 54453ed69ceacb7926639adc87f1b2df
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/Webshells/WShell_THOR_Webshells.yar:621:2"
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

## usage_mismatch:5569c0437dbdbe8486566ad64a33f6bf:search

```yaml
regex_id: 5569c0437dbdbe8486566ad64a33f6bf
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/APT_Regin.yar:341:8"
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

## usage_mismatch:64da7ea536c464b0453c16e48d1cce54:search

```yaml
regex_id: 64da7ea536c464b0453c16e48d1cce54
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/APT_OPCleaver.yar:594:8"
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

## usage_mismatch:64edf0794840c73b5440f2ad29eab98d:search

```yaml
regex_id: 64edf0794840c73b5440f2ad29eab98d
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/RANSOM_MS17-010_Wannacrypt.yar:172:6"
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

## intent_mismatch:662c93c88186a49f1a9ee5afd324b196:email

```yaml
regex_id: 662c93c88186a49f1a9ee5afd324b196
schema_version: "1"
kind: intent_mismatch
corpus: PEpper
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/TOOLKIT_FinFisher_.yar:17:8"
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

## usage_mismatch:7192b84f20a421ea269517bbcc60e406:search

```yaml
regex_id: 7192b84f20a421ea269517bbcc60e406
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/Webshells/WShell_THOR_Webshells.yar:89:2"
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

## usage_mismatch:73573969d91a2f5b8272fa00f32c1eb1:search

```yaml
regex_id: 73573969d91a2f5b8272fa00f32c1eb1
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/APT_Passcv.yar:158:6"
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

## intent_mismatch:750c32a0476f6a97998a0909a599c4ea:hostname

```yaml
regex_id: 750c32a0476f6a97998a0909a599c4ea
schema_version: "1"
kind: intent_mismatch
corpus: PEpper
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/TOOLKIT_Chinese_Hacktools.yar:1876:2"
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

## intent_mismatch:76d71b7216f7b77af8f923bdfad87455:email

```yaml
regex_id: 76d71b7216f7b77af8f923bdfad87455
schema_version: "1"
kind: intent_mismatch
corpus: PEpper
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/email/urls.yar:16:2"
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

## usage_mismatch:7770f10a7e442c943d6d092696363e6f:search

```yaml
regex_id: 7770f10a7e442c943d6d092696363e6f
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/APT_KeyBoy.yar:39:8"
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

## usage_mismatch:7cf3802b217604f552fc92823f1dc1db:search

```yaml
regex_id: 7cf3802b217604f552fc92823f1dc1db
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/APT_OPCleaver.yar:236:4"
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

## usage_mismatch:847e49a6b9f5900793c69346ca6f1693:search

```yaml
regex_id: 847e49a6b9f5900793c69346ca6f1693
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/MALW_Miscelanea.yar:679:2"
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

## usage_mismatch:8c26a87af37636eedbe17b45c4b74d34:search

```yaml
regex_id: 8c26a87af37636eedbe17b45c4b74d34
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/Webshells/WShell_THOR_Webshells.yar:3274:2"
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

## usage_mismatch:8c4e0fea9a62bf0ea7bdf1bee81a7512:search

```yaml
regex_id: 8c4e0fea9a62bf0ea7bdf1bee81a7512
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/APT_APT29_Grizzly_Steppe.yar:92:6"
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

## intent_mismatch:90d7b009c624974e6cdf86348611f591:email

```yaml
regex_id: 90d7b009c624974e6cdf86348611f591
schema_version: "1"
kind: intent_mismatch
corpus: PEpper
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/TOOLKIT_FinFisher_.yar:87:8"
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

## usage_mismatch:920a99811b1f533a1de531c506e32445:search

```yaml
regex_id: 920a99811b1f533a1de531c506e32445
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/Operation_Blockbuster/general.yara:13:2"
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

## intent_mismatch:93019009c3085f89e3514040216e0e50:email

```yaml
regex_id: 93019009c3085f89e3514040216e0e50
schema_version: "1"
kind: intent_mismatch
corpus: PEpper
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/email/urls.yar:31:2"
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

## intent_mismatch:9647e81e4d2109098999d4291b685dfc:email

```yaml
regex_id: 9647e81e4d2109098999d4291b685dfc
schema_version: "1"
kind: intent_mismatch
corpus: PEpper
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/TOOLKIT_FinFisher_.yar:87:8"
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

## usage_mismatch:9ee9d2f2bfd7ee22bc90551a02adda66:search

```yaml
regex_id: 9ee9d2f2bfd7ee22bc90551a02adda66
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/APT_Snowglobe_Babar.yar:32:8"
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

## usage_mismatch:a9a5c105b4a1c66e67fa3d40b4c81fae:search

```yaml
regex_id: a9a5c105b4a1c66e67fa3d40b4c81fae
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/APT_APT29_Grizzly_Steppe.yar:89:6"
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

## usage_mismatch:aa75ec146b41d610ecf2b956ec7c5581:search

```yaml
regex_id: aa75ec146b41d610ecf2b956ec7c5581
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/APT_Derusbi.yar:281:8"
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

## usage_mismatch:b5e318c91a062faf31fe9cf067075b90:search

```yaml
regex_id: b5e318c91a062faf31fe9cf067075b90
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/APT_KeyBoy.yar:40:8"
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

## usage_mismatch:b8635650f231177343d23cfa6ffbf182:search

```yaml
regex_id: b8635650f231177343d23cfa6ffbf182
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/APT_Poseidon_Group.yar:38:8"
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

## usage_mismatch:bd1bea91aec2e49d0318f3c9dc684ccd:search

```yaml
regex_id: bd1bea91aec2e49d0318f3c9dc684ccd
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/Webshells/WShell_THOR_Webshells.yar:7574:2"
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

## intent_mismatch:bd94aeb652e2a63f2973476eb6547f57:email

```yaml
regex_id: bd94aeb652e2a63f2973476eb6547f57
schema_version: "1"
kind: intent_mismatch
corpus: PEpper
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/TOOLKIT_FinFisher_.yar:86:8"
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

## intent_mismatch:bd9a59f44abe57b278aeb25125cdeff2:email

```yaml
regex_id: bd9a59f44abe57b278aeb25125cdeff2
schema_version: "1"
kind: intent_mismatch
corpus: PEpper
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/TOOLKIT_FinFisher_.yar:16:8"
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

## usage_mismatch:be1443cfbf98637bbbfaaf017dd05d65:search

```yaml
regex_id: be1443cfbf98637bbbfaaf017dd05d65
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/Webshells/WShell_THOR_Webshells.yar:6547:2"
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

## intent_mismatch:bf7fc5c305cab896a471a59a64f72968:email

```yaml
regex_id: bf7fc5c305cab896a471a59a64f72968
schema_version: "1"
kind: intent_mismatch
corpus: PEpper
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/TOOLKIT_FinFisher_.yar:85:8"
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

## intent_mismatch:bff6dcaa8ca1b2da2a9f4ee909373dc5:email

```yaml
regex_id: bff6dcaa8ca1b2da2a9f4ee909373dc5
schema_version: "1"
kind: intent_mismatch
corpus: PEpper
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/TOOLKIT_FinFisher_.yar:17:8"
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

## usage_mismatch:bffa29141e845b9d44ebf969098c7c91:search

```yaml
regex_id: bffa29141e845b9d44ebf969098c7c91
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/Webshells/WShell_THOR_Webshells.yar:6872:2"
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

## usage_mismatch:c712376ba8918e87532727c78cf58da3:search

```yaml
regex_id: c712376ba8918e87532727c78cf58da3
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/APT_APT29_Grizzly_Steppe.yar:109:6"
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

## usage_mismatch:ca6d3ce40b0bdf7ed712a963a0d287b2:search

```yaml
regex_id: ca6d3ce40b0bdf7ed712a963a0d287b2
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/MALW_Miscelanea.yar:137:2"
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

## usage_mismatch:caed7eab66360103ccc637bec9652aff:search

```yaml
regex_id: caed7eab66360103ccc637bec9652aff
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/Webshells/WShell_THOR_Webshells.yar:1880:2"
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

## usage_mismatch:cc23a38a6a5a372a014791d640217c62:search

```yaml
regex_id: cc23a38a6a5a372a014791d640217c62
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/Webshells/WShell_THOR_Webshells.yar:7335:2"
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

## usage_mismatch:d407fdc1fd03fd51e47a2cfabd23b1f0:search

```yaml
regex_id: d407fdc1fd03fd51e47a2cfabd23b1f0
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/APT_Derusbi.yar:318:8"
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

## usage_mismatch:d811f1b0ec6adee57a4376690c3a0fe2:search

```yaml
regex_id: d811f1b0ec6adee57a4376690c3a0fe2
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/RANSOM_MS17-010_Wannacrypt.yar:173:6"
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

## usage_mismatch:da8766ced2c419abf747cd7b904304fa:search

```yaml
regex_id: da8766ced2c419abf747cd7b904304fa
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/APT_KeyBoy.yar:41:8"
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

## usage_mismatch:eb33e0092279ff295e03a845eb83f065:search

```yaml
regex_id: eb33e0092279ff295e03a845eb83f065
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/Webshells/WShell_THOR_Webshells.yar:6262:2"
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

## usage_mismatch:f638f3b9cdfcc8e9bef3153ea8d59fa6:search

```yaml
regex_id: f638f3b9cdfcc8e9bef3153ea8d59fa6
schema_version: "1"
kind: usage_mismatch
corpus: PEpper
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/RAT_PoisonIvy.yar:39:2"
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

## intent_mismatch:f782e83fa8dddfaab1246d8b3fdc3483:email

```yaml
regex_id: f782e83fa8dddfaab1246d8b3fdc3483
schema_version: "1"
kind: intent_mismatch
corpus: PEpper
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/PEpper/rules/malware/TOOLKIT_FinFisher_.yar:85:8"
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
corpus: PEpper
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
corpus: PEpper
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
corpus: PEpper
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
corpus: PEpper
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

---
schema_version: "1"
corpus: SentinelX
findings: 86
---

# SentinelX batch findings

## intent_mismatch:04ad8d3c2242896ce2532d0e75d2eceb:email

```yaml
regex_id: 04ad8d3c2242896ce2532d0e75d2eceb
schema_version: "1"
kind: intent_mismatch
corpus: SentinelX
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/email/Email_PHP_Mailer.yar:53:8"
```

### Pattern

`X-PHP-Script: ([\w\.\/]+\/(.*\.php))?`

### Context

```json
{"admitted_char": "'\\n'", "keyword": "email", "reason": "name/comment claims validation but pattern admits excluded char"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0a3b340c5b198cd030b57689901f4441:search

```yaml
regex_id: 0a3b340c5b198cd030b57689901f4441
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/APT_KeyBoy.yar:39:8"
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

## usage_mismatch:0ceb735d6f51e4c779139227e1914481:search

```yaml
regex_id: 0ceb735d6f51e4c779139227e1914481
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/webshells/WShell_THOR_Webshells.yar:6547:2"
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

## usage_mismatch:0edfe8cbabf5261f9ed8070f80a19cad:search

```yaml
regex_id: 0edfe8cbabf5261f9ed8070f80a19cad
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/MALW_Miscelanea.yar:137:2"
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

## intent_mismatch:0ff2af656703c81a1a1e7c75c30ec4e5:hostname

```yaml
regex_id: 0ff2af656703c81a1a1e7c75c30ec4e5
schema_version: "1"
kind: intent_mismatch
corpus: SentinelX
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/TOOLKIT_Chinese_Hacktools.yar:1876:2"
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

## usage_mismatch:1902a7094e62415153ae58c4f096d8fe:search

```yaml
regex_id: 1902a7094e62415153ae58c4f096d8fe
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/APT_APT29_Grizzly_Steppe.yar:109:6"
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

## intent_mismatch:1f723fd735d35442289a816992d8918c:email

```yaml
regex_id: 1f723fd735d35442289a816992d8918c
schema_version: "1"
kind: intent_mismatch
corpus: SentinelX
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/TOOLKIT_FinFisher_.yar:85:8"
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

## usage_mismatch:1fdb56915b5faaca92f14f58155d11c3:search

```yaml
regex_id: 1fdb56915b5faaca92f14f58155d11c3
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/webshells/WShell_THOR_Webshells.yar:6554:2"
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

## usage_mismatch:20b524baf338cde9ca3d147f79912cee:search

```yaml
regex_id: 20b524baf338cde9ca3d147f79912cee
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/elastic-rules-repo/yara/rules/Windows_Trojan_ShadowPad.yar:44:8"
```

### Pattern

`xH\#wxH\#w:\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:25e0d61e7243079c77885987b4010f7c:search

```yaml
regex_id: 25e0d61e7243079c77885987b4010f7c
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/APT_ThreatGroup3390.yar:38:8"
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

## usage_mismatch:2e963e25abc44ebde8bf6fd39c092abc:search

```yaml
regex_id: 2e963e25abc44ebde8bf6fd39c092abc
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/APT_APT29_Grizzly_Steppe.yar:92:6"
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

## usage_mismatch:30e87d1b47986bdb221d051475e803c8:search

```yaml
regex_id: 30e87d1b47986bdb221d051475e803c8
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/elastic-rules-repo/yara/rules/Windows_Hacktool_SharpView.yar:22:8"
```

### Pattern

`\^\[0\-9A\-F\]\{8\}\-\(\[0\-9A\-F\]\{4\}\-\)\{3\}\[0\-9A\-F\]\{12\}\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:31fdec007271d34298dcc768942a6b95:email

```yaml
regex_id: 31fdec007271d34298dcc768942a6b95
schema_version: "1"
kind: intent_mismatch
corpus: SentinelX
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/TOOLKIT_FinFisher_.yar:15:8"
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

## usage_mismatch:336fc045ce04d874a36f9e857ae7df33:search

```yaml
regex_id: 336fc045ce04d874a36f9e857ae7df33
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/elastic-rules-repo/yara/rules/Windows_Trojan_Trickbot.yar:834:8"
```

### Pattern

`String\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:34da7518e3506382cacdfd8c4c01b8ab:search

```yaml
regex_id: 34da7518e3506382cacdfd8c4c01b8ab
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/webshells/WShell_THOR_Webshells.yar:7574:2"
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

## intent_mismatch:3688ebed532b242d5459102d03905fae:email

```yaml
regex_id: 3688ebed532b242d5459102d03905fae
schema_version: "1"
kind: intent_mismatch
corpus: SentinelX
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/TOOLKIT_FinFisher_.yar:17:8"
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

## usage_mismatch:370d0a683eaf51b8f08656f3b09f7c71:search

```yaml
regex_id: 370d0a683eaf51b8f08656f3b09f7c71
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/APT_OPCleaver.yar:594:8"
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

## intent_mismatch:3eab08a986fd7acdffbdb290297c1651:email

```yaml
regex_id: 3eab08a986fd7acdffbdb290297c1651
schema_version: "1"
kind: intent_mismatch
corpus: SentinelX
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/TOOLKIT_FinFisher_.yar:87:8"
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

## usage_mismatch:4937b9d64cd0898f544de582a4dc8452:search

```yaml
regex_id: 4937b9d64cd0898f544de582a4dc8452
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/Operation_Blockbuster/general.yara:13:2"
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

## usage_mismatch:56159c9042a8cd5ce9b85e730f3dfbd4:search

```yaml
regex_id: 56159c9042a8cd5ce9b85e730f3dfbd4
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/RAT_Indetectables.yar:29:2"
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

## usage_mismatch:58124f887f06730bc0655a91a0d2b39a:search

```yaml
regex_id: 58124f887f06730bc0655a91a0d2b39a
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/webshells/WShell_THOR_Webshells.yar:1880:2"
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

## intent_mismatch:6b73aae0e37c2e6e7619ada7c4866354:email

```yaml
regex_id: 6b73aae0e37c2e6e7619ada7c4866354
schema_version: "1"
kind: intent_mismatch
corpus: SentinelX
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/TOOLKIT_FinFisher_.yar:16:8"
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

## usage_mismatch:6ccda70905b72d90dc0853fdda20d3d3:search

```yaml
regex_id: 6ccda70905b72d90dc0853fdda20d3d3
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/webshells/WShell_THOR_Webshells.yar:3813:2"
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

## usage_mismatch:6fe448fddb253fbb7e18851cb14aefc3:search

```yaml
regex_id: 6fe448fddb253fbb7e18851cb14aefc3
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/APT_KeyBoy.yar:43:8"
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

## usage_mismatch:70c7ed5e93ecfff3c4b5c6801bd71bed:search

```yaml
regex_id: 70c7ed5e93ecfff3c4b5c6801bd71bed
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/RANSOM_Petya_MS17_010.yar:14:6"
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

## intent_mismatch:70fb01be3a17d0e13e77b442449984c7:email

```yaml
regex_id: 70fb01be3a17d0e13e77b442449984c7
schema_version: "1"
kind: intent_mismatch
corpus: SentinelX
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/email/Email_PHP_Mailer.yar:55:11"
```

### Pattern

`X-Source-Args: (\/[\w]+\/(.*\.php))?`

### Context

```json
{"admitted_char": "'\\n'", "keyword": "email", "reason": "name/comment claims validation but pattern admits excluded char"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:71e1d1bbd1fceea7d30079d2ddf24b0c:search

```yaml
regex_id: 71e1d1bbd1fceea7d30079d2ddf24b0c
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/webshells/WShell_THOR_Webshells.yar:7573:2"
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

## usage_mismatch:728d807436d3321b685905ca30b26952:search

```yaml
regex_id: 728d807436d3321b685905ca30b26952
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/webshells/WShell_THOR_Webshells.yar:6872:2"
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

## usage_mismatch:82170170f234859db8ad61c29acb5526:search

```yaml
regex_id: 82170170f234859db8ad61c29acb5526
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/RANSOM_MS17-010_Wannacrypt.yar:172:6"
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

## usage_mismatch:85c034d05c7c18e35eead2c3094c53e4:search

```yaml
regex_id: 85c034d05c7c18e35eead2c3094c53e4
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/elastic-rules-repo/yara/rules/Windows_Hacktool_SharpView.yar:31:8"
```

### Pattern

`\^S\-1\-5\-\.\*\-\[1\-9\]\\\\d\{3,\}\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:87f3dd3eee32aa3b4437c23a88ac22da:search

```yaml
regex_id: 87f3dd3eee32aa3b4437c23a88ac22da
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/APT_Poseidon_Group.yar:38:8"
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

## usage_mismatch:8917f5b90f430f397a7e2ff75b1b65ff:search

```yaml
regex_id: 8917f5b90f430f397a7e2ff75b1b65ff
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/APT_Derusbi.yar:263:8"
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

## usage_mismatch:8a1408488a9d5ebedb482dca2720ee8d:search

```yaml
regex_id: 8a1408488a9d5ebedb482dca2720ee8d
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/APT_KeyBoy.yar:44:8"
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

## usage_mismatch:8aac8bfab0ac5bb62363ee80f2ad4062:search

```yaml
regex_id: 8aac8bfab0ac5bb62363ee80f2ad4062
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/MALW_Miscelanea.yar:679:2"
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

## usage_mismatch:97d0e98d8d66fca47a92370508933bfe:search

```yaml
regex_id: 97d0e98d8d66fca47a92370508933bfe
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/webshells/WShell_PHP_in_images.yar:12:8"
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

## intent_mismatch:9ddbbdc41d04395c692aec4b1ef28f75:email

```yaml
regex_id: 9ddbbdc41d04395c692aec4b1ef28f75
schema_version: "1"
kind: intent_mismatch
corpus: SentinelX
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/email/Email_PHP_Mailer.yar:52:8"
```

### Pattern

`X-PHP-Originating-Script: ([\w\.]+(.*\.php))?`

### Context

```json
{"admitted_char": "'\\n'", "keyword": "email", "reason": "name/comment claims validation but pattern admits excluded char"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a06ee56ae325549a7cf48130e166b410:search

```yaml
regex_id: a06ee56ae325549a7cf48130e166b410
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/APT_KeyBoy.yar:41:8"
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

## usage_mismatch:a0c60984fadd57b670fbfd2140af1473:search

```yaml
regex_id: a0c60984fadd57b670fbfd2140af1473
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/elastic-rules-repo/yara/rules/Windows_Hacktool_SharpView.yar:31:8"
```

### Pattern

`\^S\-1\-5\-\.\*\-\[1\-9\]\\\\d\{3,\}\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a130538d8c43c7ddd2f0b842bd877651:search

```yaml
regex_id: a130538d8c43c7ddd2f0b842bd877651
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/RAT_PoisonIvy.yar:39:2"
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

## usage_mismatch:a17b99d45b2cc22ef8ba275c0df65174:search

```yaml
regex_id: a17b99d45b2cc22ef8ba275c0df65174
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/MALW_AlMashreq.yar:21:1"
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

## usage_mismatch:a318d026839c338c4aa93c7515dbb7a4:search

```yaml
regex_id: a318d026839c338c4aa93c7515dbb7a4
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/APT_KeyBoy.yar:42:8"
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

## intent_mismatch:a3f08e01cd07c2ac1b5c72a75b114824:email

```yaml
regex_id: a3f08e01cd07c2ac1b5c72a75b114824
schema_version: "1"
kind: intent_mismatch
corpus: SentinelX
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/TOOLKIT_FinFisher_.yar:16:8"
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

## usage_mismatch:a962c15405c44675203db568db222c24:search

```yaml
regex_id: a962c15405c44675203db568db222c24
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/elastic-rules-repo/yara/rules/Windows_Hacktool_SharpView.yar:26:8"
```

### Pattern

`\^\(\?:\[0\-9\]\{1,3\}\\\\\.\)\{3\}\[0\-9\]\{1,3\}\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:a9f62b7e778710cf13218014e1cda2ef:search

```yaml
regex_id: a9f62b7e778710cf13218014e1cda2ef
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/APT_Snowglobe_Babar.yar:32:8"
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

## usage_mismatch:aa85afdf5ef594a82416ab05b9990375:search

```yaml
regex_id: aa85afdf5ef594a82416ab05b9990375
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/APT_Regin.yar:341:8"
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

## usage_mismatch:aba045f0952277856f7c8aff155ec2e5:search

```yaml
regex_id: aba045f0952277856f7c8aff155ec2e5
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/elastic-rules-repo/yara/rules/Windows_Trojan_BruteRatel.yar:178:8"
```

### Pattern

`__imp_Kernel32\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:b693f52e8796a536413be7118eb7eba9:email

```yaml
regex_id: b693f52e8796a536413be7118eb7eba9
schema_version: "1"
kind: intent_mismatch
corpus: SentinelX
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/email/Email_PHP_Mailer.yar:54:8"
```

### Pattern

`X-PHP-Filename: (\/[\w]+\/(.*\.php))?`

### Context

```json
{"admitted_char": "'\\n'", "keyword": "email", "reason": "name/comment claims validation but pattern admits excluded char"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bc5ae67eefd5ce095ece33328246eaba:search

```yaml
regex_id: bc5ae67eefd5ce095ece33328246eaba
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/elastic-rules-repo/yara/rules/Windows_Trojan_BruteRatel.yar:181:8"
```

### Pattern

`__imp_NETAPI32\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c3c11f5d76ac01c56171218b5a4639b8:search

```yaml
regex_id: c3c11f5d76ac01c56171218b5a4639b8
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/APT_APT29_Grizzly_Steppe.yar:89:6"
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

## usage_mismatch:c5095185e868c0683fdb43632c1217b7:search

```yaml
regex_id: c5095185e868c0683fdb43632c1217b7
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/elastic-rules-repo/yara/rules/Windows_Hacktool_SharpView.yar:30:8"
```

### Pattern

`S\-1\-5\-21\-\[0\-9\]\+\-\[0\-9\]\+\-\[0\-9\]\+\-\[0\-9\]\+\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:c5502cb697e7fc6e4afbaa93a1eb9180:email

```yaml
regex_id: c5502cb697e7fc6e4afbaa93a1eb9180
schema_version: "1"
kind: intent_mismatch
corpus: SentinelX
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/TOOLKIT_FinFisher_.yar:15:8"
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

## usage_mismatch:c8e457e113580c42b25550a64c262f22:search

```yaml
regex_id: c8e457e113580c42b25550a64c262f22
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/webshells/WShell_THOR_Webshells.yar:89:2"
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

## usage_mismatch:c8efb4b875be9a115d52ed680b870292:search

```yaml
regex_id: c8efb4b875be9a115d52ed680b870292
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/webshells/WShell_THOR_Webshells.yar:3274:2"
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

## usage_mismatch:ca23f36d52a3cf41df4d33810bc609d2:search

```yaml
regex_id: ca23f36d52a3cf41df4d33810bc609d2
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/webshells/WShell_THOR_Webshells.yar:50:2"
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

## usage_mismatch:ca8342efa50a4f3e0849ee2d0110bb75:search

```yaml
regex_id: ca8342efa50a4f3e0849ee2d0110bb75
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/APT_KeyBoy.yar:40:8"
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

## intent_mismatch:cbed3c3e7221e41bdbe2290de7c35966:email

```yaml
regex_id: cbed3c3e7221e41bdbe2290de7c35966
schema_version: "1"
kind: intent_mismatch
corpus: SentinelX
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/email/urls.yar:31:2"
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

## usage_mismatch:cbf73864e30fecdf4100092160bd9374:search

```yaml
regex_id: cbf73864e30fecdf4100092160bd9374
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/webshells/WShell_THOR_Webshells.yar:621:2"
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

## intent_mismatch:cdf28c5faa8ec328d4827cac743b1ba3:email

```yaml
regex_id: cdf28c5faa8ec328d4827cac743b1ba3
schema_version: "1"
kind: intent_mismatch
corpus: SentinelX
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/TOOLKIT_FinFisher_.yar:86:8"
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

## usage_mismatch:cf708d3cb6f0a912ade102a4f8b9c409:search

```yaml
regex_id: cf708d3cb6f0a912ade102a4f8b9c409
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/webshells/WShell_THOR_Webshells.yar:7335:2"
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

## intent_mismatch:d394e5c2022239dd68acfa4de430f684:hostname

```yaml
regex_id: d394e5c2022239dd68acfa4de430f684
schema_version: "1"
kind: intent_mismatch
corpus: SentinelX
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/TOOLKIT_Chinese_Hacktools.yar:1874:2"
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

## usage_mismatch:d67c2b728a8c09b2ddc821da7659aa1a:search

```yaml
regex_id: d67c2b728a8c09b2ddc821da7659aa1a
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/RANSOM_MS17-010_Wannacrypt.yar:173:6"
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

## usage_mismatch:d8961ce0cfb5385e455c6595f99e0d32:search

```yaml
regex_id: d8961ce0cfb5385e455c6595f99e0d32
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/elastic-rules-repo/yara/rules/Windows_Hacktool_SharpView.yar:22:8"
```

### Pattern

`\^\[0\-9A\-F\]\{8\}\-\(\[0\-9A\-F\]\{4\}\-\)\{3\}\[0\-9A\-F\]\{12\}\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:da0e4afdb45550ac6a7237ec1741d9bb:search

```yaml
regex_id: da0e4afdb45550ac6a7237ec1741d9bb
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/APT_Derusbi.yar:318:8"
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

## usage_mismatch:db16617ae612c441a96ac11d13921ad6:search

```yaml
regex_id: db16617ae612c441a96ac11d13921ad6
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/webshells/WShell_THOR_Webshells.yar:6262:2"
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

## usage_mismatch:df8f1d4904cc491b8cf96f176069e4ad:search

```yaml
regex_id: df8f1d4904cc491b8cf96f176069e4ad
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/APT_Passcv.yar:158:6"
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

## usage_mismatch:e006a66d900a6be0920c2d8c3584b02f:search

```yaml
regex_id: e006a66d900a6be0920c2d8c3584b02f
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/elastic-rules-repo/yara/rules/Windows_Hacktool_SharpView.yar:26:8"
```

### Pattern

`\^\(\?:\[0\-9\]\{1,3\}\\\\\.\)\{3\}\[0\-9\]\{1,3\}\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:e113f5ee954b49ab41bb857e51c84b95:email

```yaml
regex_id: e113f5ee954b49ab41bb857e51c84b95
schema_version: "1"
kind: intent_mismatch
corpus: SentinelX
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/TOOLKIT_FinFisher_.yar:85:8"
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

## usage_mismatch:e4279d7814282de022193cce19983959:search

```yaml
regex_id: e4279d7814282de022193cce19983959
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/APT_eqgrp_apr17.yar:2120:6"
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

## usage_mismatch:e63fb882adb36324223b3d16ec446c49:search

```yaml
regex_id: e63fb882adb36324223b3d16ec446c49
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/elastic-rules-repo/yara/rules/Windows_Trojan_Trickbot.yar:730:8"
```

### Pattern

`\\\\\\\\%s\\\\IPC\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:ece8ae197d14785295b9e45a9808459e:search

```yaml
regex_id: ece8ae197d14785295b9e45a9808459e
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/TOOLKIT_THOR_HackTools.yar:2775:2"
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

## usage_mismatch:ecefa0a93522246feb60e8d0834bcc1e:search

```yaml
regex_id: ecefa0a93522246feb60e8d0834bcc1e
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/RANSOM_Petya_MS17_010.yar:14:6"
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

## intent_mismatch:eecea89303f0f0abbf7a241a5d36b5c1:email

```yaml
regex_id: eecea89303f0f0abbf7a241a5d36b5c1
schema_version: "1"
kind: intent_mismatch
corpus: SentinelX
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/email/urls.yar:16:2"
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

## intent_mismatch:eed25426e46436d96b6aae73139d4181:email

```yaml
regex_id: eed25426e46436d96b6aae73139d4181
schema_version: "1"
kind: intent_mismatch
corpus: SentinelX
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/TOOLKIT_FinFisher_.yar:17:8"
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

## usage_mismatch:f10b381dfc774e0c9b2bc8eb47eab56e:search

```yaml
regex_id: f10b381dfc774e0c9b2bc8eb47eab56e
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/APT_OPCleaver.yar:236:4"
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

## usage_mismatch:f22fd89cca12955c6127b3ae6d9d179d:search

```yaml
regex_id: f22fd89cca12955c6127b3ae6d9d179d
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/APT_Derusbi.yar:281:8"
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

## usage_mismatch:f23028ae26652e7b1843077538d58333:search

```yaml
regex_id: f23028ae26652e7b1843077538d58333
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/elastic-rules-repo/yara/rules/Windows_Trojan_CobaltStrike.yar:943:8"
```

### Pattern

`\$\$\$THREAD\.C\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:f31d22326d6fa13743af077a813a2e61:search

```yaml
regex_id: f31d22326d6fa13743af077a813a2e61
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/APT_Industroyer.yar:87:6"
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

## usage_mismatch:f8eb96582a48dd498b1ef78ebecaf737:search

```yaml
regex_id: f8eb96582a48dd498b1ef78ebecaf737
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/elastic-rules-repo/yara/rules/Windows_Hacktool_SharpView.yar:30:8"
```

### Pattern

`S\-1\-5\-21\-\[0\-9\]\+\-\[0\-9\]\+\-\[0\-9\]\+\-\[0\-9\]\+\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:f9966a8c1863c0356f2275e64fa7ed1a:email

```yaml
regex_id: f9966a8c1863c0356f2275e64fa7ed1a
schema_version: "1"
kind: intent_mismatch
corpus: SentinelX
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/TOOLKIT_FinFisher_.yar:87:8"
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

## usage_mismatch:fda144a8be1f8f6e3b84911096d4260c:search

```yaml
regex_id: fda144a8be1f8f6e3b84911096d4260c
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/elastic-rules-repo/yara/rules/Windows_Trojan_BruteRatel.yar:180:8"
```

### Pattern

`__imp_Advapi32\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:fed6341a3f3651793612f36a4168512b:email

```yaml
regex_id: fed6341a3f3651793612f36a4168512b
schema_version: "1"
kind: intent_mismatch
corpus: SentinelX
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/TOOLKIT_FinFisher_.yar:86:8"
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

## usage_mismatch:ffb74a12f36e66dde1ca28a5e018eed8:search

```yaml
regex_id: ffb74a12f36e66dde1ca28a5e018eed8
schema_version: "1"
kind: usage_mismatch
corpus: SentinelX
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/SentinelX/rules/rules/yara-rules-repo/malware/MALW_Hsdfihdf_banking.yar:28:1"
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

## property:inventory:rc-shape1-injection-alphabet:rc-shape1-injection-alphabet

```yaml
regex_id: "inventory:rc-shape1-injection-alphabet"
schema_version: "1"
kind: property
corpus: SentinelX
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
corpus: SentinelX
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
corpus: SentinelX
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
corpus: SentinelX
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

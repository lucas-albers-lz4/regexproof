---
schema_version: "1"
corpus: BlueBox
findings: 71
---

# BlueBox batch findings

## usage_mismatch:02daeb4c175d92b157c916c895c04bcc:search

```yaml
regex_id: 02daeb4c175d92b157c916c895c04bcc
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/MALW_Hsdfihdf_banking.yar:28:1"
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

## usage_mismatch:0ba0142c2b02aa360f90cf02c5eb6fee:search

```yaml
regex_id: 0ba0142c2b02aa360f90cf02c5eb6fee
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/webshells/WShell_THOR_Webshells.yar:6547:2"
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

## usage_mismatch:0d95bbcf0bff9ee2f8a47ffe91e17ff2:search

```yaml
regex_id: 0d95bbcf0bff9ee2f8a47ffe91e17ff2
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/APT_KeyBoy.yar:39:8"
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

## usage_mismatch:15f17ca49e6acf8bb965654df7e4376c:search

```yaml
regex_id: 15f17ca49e6acf8bb965654df7e4376c
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/webshells/WShell_THOR_Webshells.yar:89:2"
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

## intent_mismatch:16db0bd746519fa330c37c3ad0e6f1c3:email

```yaml
regex_id: 16db0bd746519fa330c37c3ad0e6f1c3
schema_version: "1"
kind: intent_mismatch
corpus: BlueBox
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/TOOLKIT_FinFisher_.yar:16:8"
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

## intent_mismatch:1914ef37c2802dafae96f7a2b706f4d0:email

```yaml
regex_id: 1914ef37c2802dafae96f7a2b706f4d0
schema_version: "1"
kind: intent_mismatch
corpus: BlueBox
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/TOOLKIT_FinFisher_.yar:87:8"
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

## usage_mismatch:205b4b3c0bd52a9411df999232a94b09:search

```yaml
regex_id: 205b4b3c0bd52a9411df999232a94b09
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/webshells/WShell_THOR_Webshells.yar:50:2"
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

## usage_mismatch:22af5f619fa4d08e1effd7379d320b25:search

```yaml
regex_id: 22af5f619fa4d08e1effd7379d320b25
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/APT_Poseidon_Group.yar:38:8"
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

## usage_mismatch:23171fced5851fda1e63136cc79b109d:search

```yaml
regex_id: 23171fced5851fda1e63136cc79b109d
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/webshells/WShell_THOR_Webshells.yar:6554:2"
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

## usage_mismatch:247c8ffe973fe543fc0c0375317572ca:search

```yaml
regex_id: 247c8ffe973fe543fc0c0375317572ca
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/webshells/WShell_THOR_Webshells.yar:6872:2"
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

## usage_mismatch:28c8d9a0f55eb95fb0f1df54f1db0007:search

```yaml
regex_id: 28c8d9a0f55eb95fb0f1df54f1db0007
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/APT_APT29_Grizzly_Steppe.yar:92:6"
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

## intent_mismatch:2a69f4071996584a95860ea30b8894a3:hostname

```yaml
regex_id: 2a69f4071996584a95860ea30b8894a3
schema_version: "1"
kind: intent_mismatch
corpus: BlueBox
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/TOOLKIT_Chinese_Hacktools.yar:1876:2"
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

## intent_mismatch:2f20c57096eb55e4bfd8e5edb4d70558:email

```yaml
regex_id: 2f20c57096eb55e4bfd8e5edb4d70558
schema_version: "1"
kind: intent_mismatch
corpus: BlueBox
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/TOOLKIT_FinFisher_.yar:17:8"
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

## usage_mismatch:2ff9b1f3d03a6803b4b4fb47da2bc31b:search

```yaml
regex_id: 2ff9b1f3d03a6803b4b4fb47da2bc31b
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/webshells/WShell_THOR_Webshells.yar:1880:2"
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

## usage_mismatch:38a705ab3e57a1df18b0e397f4055fe6:search

```yaml
regex_id: 38a705ab3e57a1df18b0e397f4055fe6
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/APT_Derusbi.yar:318:8"
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

## intent_mismatch:3b73cafe4aeaeb0102716120e8c4d7d2:hostname

```yaml
regex_id: 3b73cafe4aeaeb0102716120e8c4d7d2
schema_version: "1"
kind: intent_mismatch
corpus: BlueBox
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/TOOLKIT_Chinese_Hacktools.yar:1874:2"
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

## intent_mismatch:3ea0f114ed40aba340720a17e22d0fab:email

```yaml
regex_id: 3ea0f114ed40aba340720a17e22d0fab
schema_version: "1"
kind: intent_mismatch
corpus: BlueBox
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/email/urls.yar:31:2"
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

## usage_mismatch:42a815b05acd769f9eee7f37e1443867:search

```yaml
regex_id: 42a815b05acd769f9eee7f37e1443867
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/APT_Industroyer.yar:87:6"
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

## usage_mismatch:45c9ac250a43834f4ae9f6fe4a093d88:search

```yaml
regex_id: 45c9ac250a43834f4ae9f6fe4a093d88
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/APT_Derusbi.yar:263:8"
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

## usage_mismatch:4673cc529a5774f84f5260f123aff2a1:search

```yaml
regex_id: 4673cc529a5774f84f5260f123aff2a1
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/APT_KeyBoy.yar:43:8"
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

## intent_mismatch:48c4d74f2aa3c1d8cdbfdf27cf19dd61:email

```yaml
regex_id: 48c4d74f2aa3c1d8cdbfdf27cf19dd61
schema_version: "1"
kind: intent_mismatch
corpus: BlueBox
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/email/Email_PHP_Mailer.yar:52:8"
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

## intent_mismatch:49d1bae4806abdf87a77995d10623049:email

```yaml
regex_id: 49d1bae4806abdf87a77995d10623049
schema_version: "1"
kind: intent_mismatch
corpus: BlueBox
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/email/Email_PHP_Mailer.yar:53:8"
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

## intent_mismatch:506e55c8cd3feafdf3619a09f314eb29:email

```yaml
regex_id: 506e55c8cd3feafdf3619a09f314eb29
schema_version: "1"
kind: intent_mismatch
corpus: BlueBox
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/TOOLKIT_FinFisher_.yar:85:8"
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

## usage_mismatch:53a97f5e345be4db40c99bc7293d6497:search

```yaml
regex_id: 53a97f5e345be4db40c99bc7293d6497
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/APT_APT29_Grizzly_Steppe.yar:89:6"
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

## intent_mismatch:6223eb3afda804fd6bc12022101e2b61:email

```yaml
regex_id: 6223eb3afda804fd6bc12022101e2b61
schema_version: "1"
kind: intent_mismatch
corpus: BlueBox
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/TOOLKIT_FinFisher_.yar:15:8"
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

## usage_mismatch:63987b69208bb172aa5fafda33f1b44b:search

```yaml
regex_id: 63987b69208bb172aa5fafda33f1b44b
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/webshells/WShell_PHP_in_images.yar:12:8"
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

## usage_mismatch:64ec48ba9a146a3a98ab347ecc1d1403:search

```yaml
regex_id: 64ec48ba9a146a3a98ab347ecc1d1403
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/MALW_Miscelanea.yar:679:2"
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

## intent_mismatch:671c4e4a1d94862ba74ab38566df56ff:email

```yaml
regex_id: 671c4e4a1d94862ba74ab38566df56ff
schema_version: "1"
kind: intent_mismatch
corpus: BlueBox
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/TOOLKIT_FinFisher_.yar:86:8"
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

## usage_mismatch:6a91ef0fc5afcf4075519267342a774a:search

```yaml
regex_id: 6a91ef0fc5afcf4075519267342a774a
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/webshells/WShell_THOR_Webshells.yar:7574:2"
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

## usage_mismatch:6b8a948ad5b076542774b2090be0ff34:search

```yaml
regex_id: 6b8a948ad5b076542774b2090be0ff34
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/RAT_PoisonIvy.yar:39:2"
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

## usage_mismatch:6c3223615a241e9723d16297d236bf82:search

```yaml
regex_id: 6c3223615a241e9723d16297d236bf82
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/APT_Regin.yar:341:8"
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

## usage_mismatch:74b860a6724daff5104e263cdb24cc29:search

```yaml
regex_id: 74b860a6724daff5104e263cdb24cc29
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/webshells/WShell_THOR_Webshells.yar:3813:2"
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

## usage_mismatch:768e808696302468af8531adf96006e9:search

```yaml
regex_id: 768e808696302468af8531adf96006e9
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/APT_KeyBoy.yar:40:8"
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

## intent_mismatch:7f0f23ad979441e6636fdf2737373cac:email

```yaml
regex_id: 7f0f23ad979441e6636fdf2737373cac
schema_version: "1"
kind: intent_mismatch
corpus: BlueBox
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/TOOLKIT_FinFisher_.yar:85:8"
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

## usage_mismatch:8213b03414e158bff51f7f0734ff31aa:search

```yaml
regex_id: 8213b03414e158bff51f7f0734ff31aa
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/webshells/WShell_THOR_Webshells.yar:3274:2"
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

## intent_mismatch:8649e8a60c7050b6900b55f0a5cf481b:email

```yaml
regex_id: 8649e8a60c7050b6900b55f0a5cf481b
schema_version: "1"
kind: intent_mismatch
corpus: BlueBox
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/email/Email_PHP_Mailer.yar:55:11"
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

## usage_mismatch:874b4a4c8d69d9ec9b23aeed82f3c04b:search

```yaml
regex_id: 874b4a4c8d69d9ec9b23aeed82f3c04b
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/APT_Snowglobe_Babar.yar:32:8"
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

## usage_mismatch:8a73e180920d411fffab382a034fd8fc:search

```yaml
regex_id: 8a73e180920d411fffab382a034fd8fc
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/webshells/WShell_THOR_Webshells.yar:6262:2"
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

## usage_mismatch:8bc7316c8c36216d2575a4bfb15821c5:search

```yaml
regex_id: 8bc7316c8c36216d2575a4bfb15821c5
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/APT_KeyBoy.yar:41:8"
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

## usage_mismatch:9022704e91bf4650f2074b25f6dfef1f:search

```yaml
regex_id: 9022704e91bf4650f2074b25f6dfef1f
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/RANSOM_Petya_MS17_010.yar:14:6"
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

## usage_mismatch:91adb5958f958211a52c4275cad78c1d:search

```yaml
regex_id: 91adb5958f958211a52c4275cad78c1d
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/APT_KeyBoy.yar:42:8"
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

## usage_mismatch:9880a1835223b773d1c8a6fc01c5270e:search

```yaml
regex_id: 9880a1835223b773d1c8a6fc01c5270e
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/RANSOM_MS17-010_Wannacrypt.yar:173:6"
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

## usage_mismatch:9d95e05d312dc8bc622e74829052f72b:search

```yaml
regex_id: 9d95e05d312dc8bc622e74829052f72b
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/APT_Passcv.yar:158:6"
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

## intent_mismatch:9e38ee404110c6a7ccbc398d1b417d88:email

```yaml
regex_id: 9e38ee404110c6a7ccbc398d1b417d88
schema_version: "1"
kind: intent_mismatch
corpus: BlueBox
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/TOOLKIT_FinFisher_.yar:17:8"
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

## intent_mismatch:a51ec38764caa76d3f3a7ab720f3918a:email

```yaml
regex_id: a51ec38764caa76d3f3a7ab720f3918a
schema_version: "1"
kind: intent_mismatch
corpus: BlueBox
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/TOOLKIT_FinFisher_.yar:86:8"
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

## usage_mismatch:a670b47fd6e61733a03684d93603466a:search

```yaml
regex_id: a670b47fd6e61733a03684d93603466a
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/webshells/WShell_THOR_Webshells.yar:621:2"
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

## usage_mismatch:a8d8b992fce887bbdea48802073a8dd7:search

```yaml
regex_id: a8d8b992fce887bbdea48802073a8dd7
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/TOOLKIT_THOR_HackTools.yar:2775:2"
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

## intent_mismatch:ace806984d40fe3d50382b60a72829f2:email

```yaml
regex_id: ace806984d40fe3d50382b60a72829f2
schema_version: "1"
kind: intent_mismatch
corpus: BlueBox
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/TOOLKIT_FinFisher_.yar:16:8"
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

## intent_mismatch:b01ac998b4f51fe5a4a92e42c2bb905e:email

```yaml
regex_id: b01ac998b4f51fe5a4a92e42c2bb905e
schema_version: "1"
kind: intent_mismatch
corpus: BlueBox
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/TOOLKIT_FinFisher_.yar:15:8"
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

## usage_mismatch:b9ba36db09a32fb984ccdcc6495aa86c:search

```yaml
regex_id: b9ba36db09a32fb984ccdcc6495aa86c
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/APT_ThreatGroup3390.yar:38:8"
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

## intent_mismatch:ba8ffbb299e85ecbcb2996baef4a69a8:email

```yaml
regex_id: ba8ffbb299e85ecbcb2996baef4a69a8
schema_version: "1"
kind: intent_mismatch
corpus: BlueBox
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/email/urls.yar:16:2"
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

## usage_mismatch:ba958f1d15ef5589b3393470778dcdf7:search

```yaml
regex_id: ba958f1d15ef5589b3393470778dcdf7
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/RAT_Indetectables.yar:29:2"
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

## usage_mismatch:c19e0de1968c4d6cac6b7e38b0cddea3:search

```yaml
regex_id: c19e0de1968c4d6cac6b7e38b0cddea3
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/RANSOM_Petya_MS17_010.yar:14:6"
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

## usage_mismatch:c8bf034b8ba8e0cb15b96ac9c60e8436:search

```yaml
regex_id: c8bf034b8ba8e0cb15b96ac9c60e8436
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/MALW_AlMashreq.yar:21:1"
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

## usage_mismatch:c9b01c5dc040cd0bcedc3329670ab089:search

```yaml
regex_id: c9b01c5dc040cd0bcedc3329670ab089
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/MALW_Miscelanea.yar:137:2"
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

## intent_mismatch:d66e5834b78cbf58a1d8ba7cb0f8d86b:email

```yaml
regex_id: d66e5834b78cbf58a1d8ba7cb0f8d86b
schema_version: "1"
kind: intent_mismatch
corpus: BlueBox
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/TOOLKIT_FinFisher_.yar:87:8"
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

## usage_mismatch:d6acbaca2c83fd8a513eb96a10cb4b54:search

```yaml
regex_id: d6acbaca2c83fd8a513eb96a10cb4b54
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/APT_KeyBoy.yar:44:8"
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

## usage_mismatch:db85863b273c13f0252b7a2187711acd:search

```yaml
regex_id: db85863b273c13f0252b7a2187711acd
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/Operation_Blockbuster/general.yara:13:2"
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

## intent_mismatch:dc4c8ae440f3e798f812a1c5ad24b85f:email

```yaml
regex_id: dc4c8ae440f3e798f812a1c5ad24b85f
schema_version: "1"
kind: intent_mismatch
corpus: BlueBox
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/email/Email_PHP_Mailer.yar:54:8"
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

## usage_mismatch:e5f7b5fad76ddce9ba04f28b5d872182:search

```yaml
regex_id: e5f7b5fad76ddce9ba04f28b5d872182
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/APT_Derusbi.yar:281:8"
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

## usage_mismatch:e87e70462fd482e38932b875385ad13d:search

```yaml
regex_id: e87e70462fd482e38932b875385ad13d
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/webshells/WShell_THOR_Webshells.yar:7335:2"
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

## usage_mismatch:f28d8a1ae32ea385a4403c006208d3a8:search

```yaml
regex_id: f28d8a1ae32ea385a4403c006208d3a8
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/APT_eqgrp_apr17.yar:2120:6"
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

## usage_mismatch:f8cbdebb9145d250afd03ddb9e2d0260:search

```yaml
regex_id: f8cbdebb9145d250afd03ddb9e2d0260
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/APT_OPCleaver.yar:594:8"
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

## usage_mismatch:fc6beff26c64cd483079b8742452c358:search

```yaml
regex_id: fc6beff26c64cd483079b8742452c358
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/webshells/WShell_THOR_Webshells.yar:7573:2"
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

## usage_mismatch:fcc36c4b5edfccc89c3dd8f9f95a86ac:search

```yaml
regex_id: fcc36c4b5edfccc89c3dd8f9f95a86ac
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/RANSOM_MS17-010_Wannacrypt.yar:172:6"
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

## usage_mismatch:fee22aeb970ea2db4ebfce6980bd5d0f:search

```yaml
regex_id: fee22aeb970ea2db4ebfce6980bd5d0f
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/APT_APT29_Grizzly_Steppe.yar:109:6"
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

## usage_mismatch:ff8ee153d78e56bc74e6d411dd3eb2ff:search

```yaml
regex_id: ff8ee153d78e56bc74e6d411dd3eb2ff
schema_version: "1"
kind: usage_mismatch
corpus: BlueBox
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/BlueBox/rules/App/yarascripts/YaraScan/rules/malware/APT_OPCleaver.yar:236:4"
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

## property:inventory:rc-shape1-injection-alphabet:rc-shape1-injection-alphabet

```yaml
regex_id: "inventory:rc-shape1-injection-alphabet"
schema_version: "1"
kind: property
corpus: BlueBox
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
corpus: BlueBox
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
corpus: BlueBox
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
corpus: BlueBox
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

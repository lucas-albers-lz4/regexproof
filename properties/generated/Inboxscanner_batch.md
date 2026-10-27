---
schema_version: "1"
corpus: Inboxscanner
findings: 189
---

# Inboxscanner batch findings

## usage_mismatch:00c6f402ee9d0c78ba59149394eee15e:search

```yaml
regex_id: 00c6f402ee9d0c78ba59149394eee15e
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/malc0de/malc0de_index.yara:96:8"
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

## usage_mismatch:02020c8e2494b3e94c9bf2a6816d70d0:search

```yaml
regex_id: 02020c8e2494b3e94c9bf2a6816d70d0
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/patrickrolsen/patrickrolsen_index.yara:335:1"
```

### Pattern

`eval\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:0638dbb34449d2d4fefa735124a1940a:search

```yaml
regex_id: 0638dbb34449d2d4fefa735124a1940a
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Rapid7/Rapid7_index.yara:10:8"
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

## usage_mismatch:0639a5ec91d40feea450c532cd147cfd:search

```yaml
regex_id: 0639a5ec91d40feea450c532cd147cfd
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Florian Roth/apt_apt30_backspace.yar:824:2"
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

## usage_mismatch:06939e72160a56a9591c4dd18d9c6f12:search

```yaml
regex_id: 06939e72160a56a9591c4dd18d9c6f12
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Florian Roth/apt_poisonivy_gen3.yar:16:2"
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

## intent_mismatch:078f45d79273025b6715b84b9df67cfc:email

```yaml
regex_id: 078f45d79273025b6715b84b9df67cfc
schema_version: "1"
kind: intent_mismatch
corpus: Inboxscanner
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/TOOLKIT_FinFisher_.yar:16:8"
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

## usage_mismatch:08a0b3ede4149aba211b2a15f026b4c4:search

```yaml
regex_id: 08a0b3ede4149aba211b2a15f026b4c4
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Rapid7/KeyBoy_Backdoor.yar:12:8"
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

## usage_mismatch:09d40218592bd56995eccceff1b5c353:search

```yaml
regex_id: 09d40218592bd56995eccceff1b5c353
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_apt30_backspace.yar:141:2"
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

## usage_mismatch:0ab79f17820babb6b0c812bbea4e34d7:search

```yaml
regex_id: 0ab79f17820babb6b0c812bbea4e34d7
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Florian Roth/apt_derusbi.yar:32:8"
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

## usage_mismatch:0ce259704df9b2b0476d3a578bd906e3:search

```yaml
regex_id: 0ce259704df9b2b0476d3a578bd906e3
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/APT_Derusbi.yar:318:8"
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

## usage_mismatch:0d9b3b513a29003d4eb500c19743425d:search

```yaml
regex_id: 0d9b3b513a29003d4eb500c19743425d
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Seth Hardy/Babar.yar:26:8"
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

## usage_mismatch:0e095d53e88e93818217f2fdad2d84b4:search

```yaml
regex_id: 0e095d53e88e93818217f2fdad2d84b4
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/APT_Passcv.yar:158:6"
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

## usage_mismatch:0e1f1bebaaf8b100334919cd5284aea3:search

```yaml
regex_id: 0e1f1bebaaf8b100334919cd5284aea3
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/crime_malware_generic.yar:14:2"
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

## intent_mismatch:0e31500f4fefbd1f65ffb5327bb0785e:email

```yaml
regex_id: 0e31500f4fefbd1f65ffb5327bb0785e
schema_version: "1"
kind: intent_mismatch
corpus: Inboxscanner
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/TOOLKIT_FinFisher_.yar:87:8"
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

## usage_mismatch:0ef1b5e4e333f244c8f7d41344f899fb:search

```yaml
regex_id: 0ef1b5e4e333f244c8f7d41344f899fb
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Florian Roth/apt_indetectables_rat.yar:25:2"
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

## usage_mismatch:116a26880a1ab81e2e5217c136ab9a41:search

```yaml
regex_id: 116a26880a1ab81e2e5217c136ab9a41
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/spy_regin_fiveeyes.yar:323:5"
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

## usage_mismatch:13f5073218128126ea144cdb2ee69269:search

```yaml
regex_id: 13f5073218128126ea144cdb2ee69269
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Citizen Lab/filetypes.yara:9:8"
```

### Pattern

`^\s*{\\rt`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:1602972cf0aca9a49d38f67c31f21b20:search

```yaml
regex_id: 1602972cf0aca9a49d38f67c31f21b20
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/Webshells/WShell_THOR_Webshells.yar:50:2"
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

## usage_mismatch:161772fa1d62b2e10b90ba848385de2f:search

```yaml
regex_id: 161772fa1d62b2e10b90ba848385de2f
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/h3x2b/lin_irctelnet.yara:52:16"
```

### Pattern

`rm\ \-f\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:184b8d9b9abe89e93663191d53418b8d:search

```yaml
regex_id: 184b8d9b9abe89e93663191d53418b8d
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/thor-webshells.yar:6803:2"
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

## usage_mismatch:196411f64697a664a842160cd8ed6b7c:search

```yaml
regex_id: 196411f64697a664a842160cd8ed6b7c
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/RANSOM_MS17-010_Wannacrypt.yar:173:6"
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

## usage_mismatch:199ab846b44bdbc1056fc093dfedccf5:search

```yaml
regex_id: 199ab846b44bdbc1056fc093dfedccf5
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_snowglobe_babar.yar:27:2"
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

## intent_mismatch:1e471c3d5854efee14ea7b6cb70e196f:email

```yaml
regex_id: 1e471c3d5854efee14ea7b6cb70e196f
schema_version: "1"
kind: intent_mismatch
corpus: Inboxscanner
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/TOOLKIT_FinFisher_.yar:85:8"
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

## usage_mismatch:1e4b48f8ce4f28b954794f8ad80f3d40:search

```yaml
regex_id: 1e4b48f8ce4f28b954794f8ad80f3d40
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/thor-webshells.yar:7505:2"
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

## intent_mismatch:1e62c831658316f2d7bec16f0536a59d:email

```yaml
regex_id: 1e62c831658316f2d7bec16f0536a59d
schema_version: "1"
kind: intent_mismatch
corpus: Inboxscanner
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/TOOLKIT_FinFisher_.yar:17:8"
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

## intent_mismatch:1eeea9a608791ba52663bc8ea0e294e9:email

```yaml
regex_id: 1eeea9a608791ba52663bc8ea0e294e9
schema_version: "1"
kind: intent_mismatch
corpus: Inboxscanner
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/TOOLKIT_FinFisher_.yar:15:8"
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

## usage_mismatch:1f68676bf26eca990516d2f5d24958bc:search

```yaml
regex_id: 1f68676bf26eca990516d2f5d24958bc
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Florian Roth/apt_derusbi.yar:17:8"
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

## usage_mismatch:20aba79bec268300fa9877389bf1c2d5:search

```yaml
regex_id: 20aba79bec268300fa9877389bf1c2d5
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_eqgrp_apr17.yar:2102:6"
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

## usage_mismatch:2172c54390134c302aae497e1adedf02:search

```yaml
regex_id: 2172c54390134c302aae497e1adedf02
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Citizen Lab/Citizen_Lab_index.yara:685:8"
```

### Pattern

`^\s*{\\rt`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:21aa593c92a44397776c7f5a70886d9e:hostname

```yaml
regex_id: 21aa593c92a44397776c7f5a70886d9e
schema_version: "1"
kind: intent_mismatch
corpus: Inboxscanner
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Florian Roth/gen_cn_hacktools.yar:1983:2"
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

## usage_mismatch:2287f2ca59a380fdfa2d76e9f49bc580:search

```yaml
regex_id: 2287f2ca59a380fdfa2d76e9f49bc580
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_oilrig_rgdoor.yar:29:6"
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

## usage_mismatch:23a98d94c4544a842a51e088fcc3d83a:search

```yaml
regex_id: 23a98d94c4544a842a51e088fcc3d83a
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/Webshells/WShell_THOR_Webshells.yar:621:2"
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

## usage_mismatch:23ac7ad355ada7bd87264ee3587bf486:search

```yaml
regex_id: 23ac7ad355ada7bd87264ee3587bf486
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_apt30_backspace.yar:1134:2"
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

## usage_mismatch:2498a806c7aeb83d18933cb485f51b23:search

```yaml
regex_id: 2498a806c7aeb83d18933cb485f51b23
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Florian Roth/spy_regin_fiveeyes.yar:323:5"
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

## usage_mismatch:25a84bdb03384da58609e292fde36c29:search

```yaml
regex_id: 25a84bdb03384da58609e292fde36c29
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/thor-webshells.yar:8737:6"
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

## usage_mismatch:25d1b25bf8be1e28506ebfc47f048be7:search

```yaml
regex_id: 25d1b25bf8be1e28506ebfc47f048be7
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_apt29_grizzly_steppe.yar:81:6"
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

## usage_mismatch:27c1bdfadc2fb0a435fe3d2a4191d22f:search

```yaml
regex_id: 27c1bdfadc2fb0a435fe3d2a4191d22f
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/crime_wannacry.yar:34:6"
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

## usage_mismatch:28314feba4cd94dd5919a42a906ecf68:search

```yaml
regex_id: 28314feba4cd94dd5919a42a906ecf68
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/APT_Regin.yar:341:8"
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

## usage_mismatch:29e807a251127d4d3b6990958d2aa413:search

```yaml
regex_id: 29e807a251127d4d3b6990958d2aa413
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Florian Roth/apt_threatgroup_3390.yar:31:2"
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

## usage_mismatch:2a6a7ccc7be39e3f8cc90719dc26f9b4:search

```yaml
regex_id: 2a6a7ccc7be39e3f8cc90719dc26f9b4
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/thor-webshells.yar:6485:2"
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

## usage_mismatch:2af9de24576dce73b99af1875fe082db:search

```yaml
regex_id: 2af9de24576dce73b99af1875fe082db
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/thor-webshells.yar:8797:6"
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

## usage_mismatch:2b007fb6f0db7584131d44eb01738905:search

```yaml
regex_id: 2b007fb6f0db7584131d44eb01738905
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/MALW_Miscelanea.yar:679:2"
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

## usage_mismatch:2b0a49d9df13c25d78afc5271d7237db:search

```yaml
regex_id: 2b0a49d9df13c25d78afc5271d7237db
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/Webshells/WShell_THOR_Webshells.yar:7573:2"
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

## usage_mismatch:2bc82d78ce637c340b5ce9c5f0c28ce3:search

```yaml
regex_id: 2bc82d78ce637c340b5ce9c5f0c28ce3
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/Webshells/WShell_THOR_Webshells.yar:6547:2"
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

## usage_mismatch:2bd475a59666e5925137585cafaf834b:search

```yaml
regex_id: 2bd475a59666e5925137585cafaf834b
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/APT_OPCleaver.yar:594:8"
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

## usage_mismatch:2c156b6bae1cf5d7bb4e260553c3459b:search

```yaml
regex_id: 2c156b6bae1cf5d7bb4e260553c3459b
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/thor-webshells.yar:7266:2"
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

## usage_mismatch:2d78d1188476aa23c176336e273ece44:search

```yaml
regex_id: 2d78d1188476aa23c176336e273ece44
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/crime_wannacry.yar:35:6"
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

## intent_mismatch:2d96a7fdbfa3f5e60081924bb97de5df:hostname

```yaml
regex_id: 2d96a7fdbfa3f5e60081924bb97de5df
schema_version: "1"
kind: intent_mismatch
corpus: Inboxscanner
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/TOOLKIT_Chinese_Hacktools.yar:1874:2"
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

## usage_mismatch:30e2272c7142a5f1d9d1a60c013a945f:search

```yaml
regex_id: 30e2272c7142a5f1d9d1a60c013a945f
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/thor-webshells.yar:8660:6"
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

## usage_mismatch:33fc0103ec9015458d88d6d62df21871:search

```yaml
regex_id: 33fc0103ec9015458d88d6d62df21871
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/patrickrolsen/misc_shells.yar:15:1"
```

### Pattern

`eval\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:344467cd5033ec1dbd4a9d3b3bb7f8e0:search

```yaml
regex_id: 344467cd5033ec1dbd4a9d3b3bb7f8e0
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/one offs/Mebroot_Torpig.yar:9:2"
```

### Pattern

`Temp\$67we\.\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:345ac893684ba24530084ae0bd79b88a:search

```yaml
regex_id: 345ac893684ba24530084ae0bd79b88a
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/APT_ThreatGroup3390.yar:38:8"
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

## usage_mismatch:37399e5fa6a0df802322eba0535208de:search

```yaml
regex_id: 37399e5fa6a0df802322eba0535208de
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Florian Roth/apt_snowglobe_babar.yar:27:2"
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

## intent_mismatch:3a13b678f2c048e4436339cf961dd2f2:hostname

```yaml
regex_id: 3a13b678f2c048e4436339cf961dd2f2
schema_version: "1"
kind: intent_mismatch
corpus: Inboxscanner
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/gen_cn_hacktools.yar:1830:2"
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

## usage_mismatch:3a47c934915bb3d71db434327b15a4b7:search

```yaml
regex_id: 3a47c934915bb3d71db434327b15a4b7
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/cylance/cylance_index.yara:251:3"
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

## usage_mismatch:3a9531bd5d10c013d3e425b1e492c848:search

```yaml
regex_id: 3a9531bd5d10c013d3e425b1e492c848
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/APT_Derusbi.yar:281:8"
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

## usage_mismatch:3cd988d23b64a026f556dc8858cb6710:search

```yaml
regex_id: 3cd988d23b64a026f556dc8858cb6710
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/xanda/counterPHPredirectBHEK.yar:12:2"
```

### Pattern

`\<iframe\ src\=\"https?\:\/\/[a-zA-Z0-9\-\.]{4,260}\/counter\.php\"\ style\=\"visibility\:\ hidden\;\ position\:\ absolute\;\ left\:\ 0px\;\ top\:\ 0px\"\ width\=\"10\"\ height\=\"10\"\/\>$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:40ecf53840c48c94e54cb681f5472be5:search

```yaml
regex_id: 40ecf53840c48c94e54cb681f5472be5
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/InQuest/MC_Office_DDE.yar:62:8"
```

### Pattern

`^\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1\x00\x00\x00`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:41e7f9aa3f071bde290554ff6d204a55:search

```yaml
regex_id: 41e7f9aa3f071bde290554ff6d204a55
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Florian Roth/gen_transformed_strings.yar:47:2"
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

## usage_mismatch:4587cf09dd4e31b0cae1932d8d5cb1ed:search

```yaml
regex_id: 4587cf09dd4e31b0cae1932d8d5cb1ed
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Airbus/Airbus_index.yara:27:1"
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

## usage_mismatch:45b7a063521a1c042c872eb6da70f4f4:search

```yaml
regex_id: 45b7a063521a1c042c872eb6da70f4f4
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/gen_transformed_strings.yar:47:2"
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

## usage_mismatch:464585f3980883a6994d27345426855a:search

```yaml
regex_id: 464585f3980883a6994d27345426855a
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/Webshells/WShell_PHP_in_images.yar:12:8"
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

## usage_mismatch:47b519487ec377213e7113eca9c5d0b7:search

```yaml
regex_id: 47b519487ec377213e7113eca9c5d0b7
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_muddywater.yar:38:6"
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

## usage_mismatch:47d4c421394b63fba9ccd349ddc076ee:search

```yaml
regex_id: 47d4c421394b63fba9ccd349ddc076ee
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/gen_metasploit_payloads.yar:86:6"
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

## usage_mismatch:47eb87086ebe3c723099dbc7634e59dc:search

```yaml
regex_id: 47eb87086ebe3c723099dbc7634e59dc
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/Webshells/WShell_THOR_Webshells.yar:3813:2"
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

## usage_mismatch:48c0ea7efe17fd4ab4d46039f94f1ab1:search

```yaml
regex_id: 48c0ea7efe17fd4ab4d46039f94f1ab1
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/h3x2b/lin_irctelnet.yara:54:16"
```

### Pattern

`\ \&\&\ chmod\ \+x\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:498a28a165bb3aa48cbb52aa265b344e:search

```yaml
regex_id: 498a28a165bb3aa48cbb52aa265b344e
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_apt30_backspace.yar:751:2"
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

## usage_mismatch:49c6d55a1ffc0d13058b9cc1c640e4ba:search

```yaml
regex_id: 49c6d55a1ffc0d13058b9cc1c640e4ba
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/APT_APT29_Grizzly_Steppe.yar:109:6"
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

## usage_mismatch:4a1eb0b980fed309f17190f7bca9506d:search

```yaml
regex_id: 4a1eb0b980fed309f17190f7bca9506d
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/thor-webshells.yar:3809:2"
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

## usage_mismatch:4de626a460e5f639d57e0755895fcc80:search

```yaml
regex_id: 4de626a460e5f639d57e0755895fcc80
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Florian Roth/cn_pentestset_webshells.yar:18:2"
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

## intent_mismatch:4e21c3fb4d570b8a153619a2305395c6:email

```yaml
regex_id: 4e21c3fb4d570b8a153619a2305395c6
schema_version: "1"
kind: intent_mismatch
corpus: Inboxscanner
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/TOOLKIT_FinFisher_.yar:17:8"
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

## usage_mismatch:5007506906898bc17bfbf3701b971ea7:search

```yaml
regex_id: 5007506906898bc17bfbf3701b971ea7
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/thor-hacktools.yar:2692:6"
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

## usage_mismatch:5114478a1c7c331abc0260504ede0107:search

```yaml
regex_id: 5114478a1c7c331abc0260504ede0107
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Rapid7/Rapid7_index.yara:8:8"
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

## usage_mismatch:532a78b0c647fcd100778bce63cff37f:search

```yaml
regex_id: 532a78b0c647fcd100778bce63cff37f
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/Webshells/WShell_THOR_Webshells.yar:89:2"
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

## usage_mismatch:55e8d405fbd0e0e45867daffc6bb4f86:search

```yaml
regex_id: 55e8d405fbd0e0e45867daffc6bb4f86
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_indetectables_rat.yar:25:2"
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

## usage_mismatch:58fe60e60b279af2cc16fbe55d8fb15c:search

```yaml
regex_id: 58fe60e60b279af2cc16fbe55d8fb15c
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_cn_pp_zerot.yar:48:6"
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

## usage_mismatch:5b5d434df2cf8cf87c075da81a9cbb4c:search

```yaml
regex_id: 5b5d434df2cf8cf87c075da81a9cbb4c
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Airbus/derusbi_kernel.yar:10:4"
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

## usage_mismatch:5c4289af36c82a45ee2b069e3a60fb48:search

```yaml
regex_id: 5c4289af36c82a45ee2b069e3a60fb48
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/APT_KeyBoy.yar:41:8"
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

## usage_mismatch:5caa9175d0de91ddf18d9a5fd55cfa40:search

```yaml
regex_id: 5caa9175d0de91ddf18d9a5fd55cfa40
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_derusbi.yar:64:6"
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

## usage_mismatch:5d9a1f56f148ce08e9177189519c0e04:search

```yaml
regex_id: 5d9a1f56f148ce08e9177189519c0e04
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Rapid7/KeyBoy_Backdoor.yar:11:8"
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

## usage_mismatch:6206f2599e7aa25e6e0b2976aa8154c5:search

```yaml
regex_id: 6206f2599e7aa25e6e0b2976aa8154c5
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/h3x2b/lin_irctelnet.yara:53:16"
```

### Pattern

`wget\ \-O\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:64d2764995e79b9875489a9af371437a:search

```yaml
regex_id: 64d2764995e79b9875489a9af371437a
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/APT_KeyBoy.yar:43:8"
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

## usage_mismatch:680cda7e438bdfbfe8e7de34f209e589:search

```yaml
regex_id: 680cda7e438bdfbfe8e7de34f209e589
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/iDefense/WannaCrypt0r.yara:10:2"
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

## usage_mismatch:68d657e3c0bf30a8b34da316cd25eabd:search

```yaml
regex_id: 68d657e3c0bf30a8b34da316cd25eabd
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/Webshells/WShell_THOR_Webshells.yar:6872:2"
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

## usage_mismatch:69bca26e5d9fe30053e6220e873d4660:search

```yaml
regex_id: 69bca26e5d9fe30053e6220e873d4660
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/RAT_PoisonIvy.yar:39:2"
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

## usage_mismatch:6c017e72ee3aea14db80b50c537caaf6:search

```yaml
regex_id: 6c017e72ee3aea14db80b50c537caaf6
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/h3x2b/lin_irctelnet.yara:55:16"
```

### Pattern

`\ \&\&\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6e0602471ddc1ad02323977a712fe074:search

```yaml
regex_id: 6e0602471ddc1ad02323977a712fe074
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/malc0de/gdocupload_apt1.yar:4:8"
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

## usage_mismatch:6e84d702d4054d82807a622c59e17795:search

```yaml
regex_id: 6e84d702d4054d82807a622c59e17795
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/APT_OPCleaver.yar:236:4"
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

## usage_mismatch:70efcf9453217301b3ebc0d95622d403:search

```yaml
regex_id: 70efcf9453217301b3ebc0d95622d403
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_threatgroup_3390.yar:31:2"
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

## intent_mismatch:714fc9560a02062f97f3ea9d92aab11f:email

```yaml
regex_id: 714fc9560a02062f97f3ea9d92aab11f
schema_version: "1"
kind: intent_mismatch
corpus: Inboxscanner
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/TOOLKIT_FinFisher_.yar:87:8"
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

## usage_mismatch:74f9a96741b75d672eb7b2f6fe822722:search

```yaml
regex_id: 74f9a96741b75d672eb7b2f6fe822722
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/h3x2b/lin_irctelnet.yara:51:16"
```

### Pattern

`killall\ \-9\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:78f14565e64c115719a5034758c79ada:search

```yaml
regex_id: 78f14565e64c115719a5034758c79ada
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_fin7_backdoor.yar:23:6"
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

## usage_mismatch:793b7d793eeb74ffd1a4de274e771f1a:search

```yaml
regex_id: 793b7d793eeb74ffd1a4de274e771f1a
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/malc0de/hacksfase_apt1.yar:6:2"
```

### Pattern

`tthacksfas@\#\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:798a458b97068e849568b155f03948cd:search

```yaml
regex_id: 798a458b97068e849568b155f03948cd
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Florian Roth/apt_op_cleaver.yar:218:2"
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

## usage_mismatch:7b21ec020ec534af52fe0f5732feaed1:search

```yaml
regex_id: 7b21ec020ec534af52fe0f5732feaed1
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/APT_Poseidon_Group.yar:38:8"
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

## usage_mismatch:7bde00d41d4bb64675b5bf1eecd599fe:search

```yaml
regex_id: 7bde00d41d4bb64675b5bf1eecd599fe
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Seth Hardy/Seth_Hardy_index.yara:122:8"
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

## usage_mismatch:7c93facf97224993b4c3ee0a6cf37f5d:search

```yaml
regex_id: 7c93facf97224993b4c3ee0a6cf37f5d
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/thor-webshells.yar:6478:2"
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

## usage_mismatch:7ea94d20bc6d335cca4fdface0a97bf1:search

```yaml
regex_id: 7ea94d20bc6d335cca4fdface0a97bf1
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/thor-webshells.yar:1877:2"
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

## usage_mismatch:82eaade3edccd30e4d2182cdc50c8063:search

```yaml
regex_id: 82eaade3edccd30e4d2182cdc50c8063
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/thor-webshells.yar:8738:6"
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

## usage_mismatch:8352db6fb59704de025ac6275ffec10d:search

```yaml
regex_id: 8352db6fb59704de025ac6275ffec10d
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/cn_pentestset_webshells.yar:18:2"
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

## usage_mismatch:847d6c278be5e2abe9961ed27a49dc36:search

```yaml
regex_id: 847d6c278be5e2abe9961ed27a49dc36
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/APT_Derusbi.yar:263:8"
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

## usage_mismatch:84900e89e6d39c3acafb1d8ee771eced:search

```yaml
regex_id: 84900e89e6d39c3acafb1d8ee771eced
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Rapid7/Rapid7_index.yara:12:8"
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

## usage_mismatch:850aad239c076e314d63db0eae4049ad:search

```yaml
regex_id: 850aad239c076e314d63db0eae4049ad
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Rapid7/Rapid7_index.yara:11:8"
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

## usage_mismatch:854b9e420d403c83186832af756df874:search

```yaml
regex_id: 854b9e420d403c83186832af756df874
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/MALW_Miscelanea.yar:137:2"
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

## usage_mismatch:8ad1ccb0075039d2092d95ec78af841e:search

```yaml
regex_id: 8ad1ccb0075039d2092d95ec78af841e
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/Webshells/WShell_THOR_Webshells.yar:1880:2"
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

## usage_mismatch:8d71bebfff28461ab3be81c0f19171c4:search

```yaml
regex_id: 8d71bebfff28461ab3be81c0f19171c4
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_poseidon_group.yar:30:2"
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

## usage_mismatch:8d86742e90b91c2864f25645a12acb7b:search

```yaml
regex_id: 8d86742e90b91c2864f25645a12acb7b
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/thor-hacktools.yar:4000:6"
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

## usage_mismatch:8e558342f5d70136c2ff0a7e4b33c070:search

```yaml
regex_id: 8e558342f5d70136c2ff0a7e4b33c070
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Novetta/Novetta_index.yara:313:2"
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

## usage_mismatch:9176fbc276656f7a16ec682e9360a7ae:search

```yaml
regex_id: 9176fbc276656f7a16ec682e9360a7ae
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Rapid7/KeyBoy_Backdoor.yar:8:8"
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

## usage_mismatch:925e47c912a4cf6498c010dc67862d89:search

```yaml
regex_id: 925e47c912a4cf6498c010dc67862d89
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/thor-webshells.yar:3271:2"
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

## intent_mismatch:937161787f8ffb7062f14e36582d977f:hostname

```yaml
regex_id: 937161787f8ffb7062f14e36582d977f
schema_version: "1"
kind: intent_mismatch
corpus: Inboxscanner
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Florian Roth/gen_cn_hacktools.yar:1981:2"
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

## usage_mismatch:995525a2af7e874c7748a69820fe3778:search

```yaml
regex_id: 995525a2af7e874c7748a69820fe3778
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_industroyer.yar:88:6"
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

## usage_mismatch:99653ff193255e1471027a5a44ff318f:search

```yaml
regex_id: 99653ff193255e1471027a5a44ff318f
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_derusbi.yar:31:8"
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

## usage_mismatch:9ad59cd363ccfd6311dd461f9963f9af:search

```yaml
regex_id: 9ad59cd363ccfd6311dd461f9963f9af
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/patrickrolsen/patrickrolsen_index.yara:390:1"
```

### Pattern

`FILE\ UPLOADED\ TO\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:9c0c0afbf6678fc87ada679f273514d0:search

```yaml
regex_id: 9c0c0afbf6678fc87ada679f273514d0
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/optiv/autoit_scripting_pos_malware.yar:60:14"
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

## usage_mismatch:9c6b345bc2c355baae21a7b2d3543c8c:search

```yaml
regex_id: 9c6b345bc2c355baae21a7b2d3543c8c
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/Operation_Blockbuster/general.yara:13:2"
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

## usage_mismatch:a04b9f602867d79fbc6fb6e52dcd6bab:search

```yaml
regex_id: a04b9f602867d79fbc6fb6e52dcd6bab
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Florian Roth/gen_powershell_toolkit.yar:179:2"
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

## usage_mismatch:a0b564be789b70c7f5c7f62c8dc7f2e4:search

```yaml
regex_id: a0b564be789b70c7f5c7f62c8dc7f2e4
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/thor-webshells.yar:616:2"
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

## usage_mismatch:a3007257ba9c043e8185e91f80fc68e8:search

```yaml
regex_id: a3007257ba9c043e8185e91f80fc68e8
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/thor-webshells.yar:6212:2"
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

## intent_mismatch:a74d6d8f5d2655a03bd944ba854f72b0:email

```yaml
regex_id: a74d6d8f5d2655a03bd944ba854f72b0
schema_version: "1"
kind: intent_mismatch
corpus: Inboxscanner
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/TOOLKIT_FinFisher_.yar:85:8"
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

## usage_mismatch:a7ad5b7dae9de1b3a10f1c1a6d09a2d9:search

```yaml
regex_id: a7ad5b7dae9de1b3a10f1c1a6d09a2d9
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Rapid7/KeyBoy_Backdoor.yar:10:8"
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

## usage_mismatch:a9394f14c61c38fc6733359e3077ab2f:search

```yaml
regex_id: a9394f14c61c38fc6733359e3077ab2f
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/Webshells/WShell_THOR_Webshells.yar:6554:2"
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

## intent_mismatch:ab1719e24e3a24693033e62d6da6ee24:email

```yaml
regex_id: ab1719e24e3a24693033e62d6da6ee24
schema_version: "1"
kind: intent_mismatch
corpus: Inboxscanner
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/TOOLKIT_FinFisher_.yar:16:8"
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

## usage_mismatch:ae0c030d441c276b8263f9cbe489a1e5:search

```yaml
regex_id: ae0c030d441c276b8263f9cbe489a1e5
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/APT_KeyBoy.yar:39:8"
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

## usage_mismatch:b0d3fa4b97a7996348ba796c193dfde5:search

```yaml
regex_id: b0d3fa4b97a7996348ba796c193dfde5
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/RAT_Indetectables.yar:29:2"
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

## intent_mismatch:b1357bdd707f0e94e1098f9ff34239b1:hostname

```yaml
regex_id: b1357bdd707f0e94e1098f9ff34239b1
schema_version: "1"
kind: intent_mismatch
corpus: Inboxscanner
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/TOOLKIT_Chinese_Hacktools.yar:1876:2"
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

## usage_mismatch:b2cbdad51ce48a8de31b14eba45022c7:search

```yaml
regex_id: b2cbdad51ce48a8de31b14eba45022c7
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Florian Roth/apt_apt30_backspace.yar:1134:2"
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

## usage_mismatch:b2ed8bdeb502d5e7d5a46fc64b480a22:search

```yaml
regex_id: b2ed8bdeb502d5e7d5a46fc64b480a22
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/cylance/pvz_in.yar:7:3"
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

## usage_mismatch:b3cad8ad70d7436e48b08df607ab94b3:search

```yaml
regex_id: b3cad8ad70d7436e48b08df607ab94b3
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/gen_enigma_protector.yar:17:6"
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

## usage_mismatch:b52e1d768cb332691175bd4cf1fe03fe:search

```yaml
regex_id: b52e1d768cb332691175bd4cf1fe03fe
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Novetta/general.yara:13:2"
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

## usage_mismatch:b545f8d3fa43874d92e4b8b02ce57609:search

```yaml
regex_id: b545f8d3fa43874d92e4b8b02ce57609
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/Webshells/WShell_THOR_Webshells.yar:7574:2"
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

## usage_mismatch:b567e38507774bcefabcb90249eab453:search

```yaml
regex_id: b567e38507774bcefabcb90249eab453
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Florian Roth/apt_apt30_backspace.yar:751:2"
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

## usage_mismatch:b66c78cc986c64d8dfc3ef9c0517ef7d:search

```yaml
regex_id: b66c78cc986c64d8dfc3ef9c0517ef7d
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/Webshells/WShell_THOR_Webshells.yar:7335:2"
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

## usage_mismatch:b768a4acec4de197d507bfcdafacf24b:search

```yaml
regex_id: b768a4acec4de197d507bfcdafacf24b
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/MALW_Hsdfihdf_banking.yar:28:1"
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

## usage_mismatch:b7bc9a800e580803fbd7843bb018dd23:search

```yaml
regex_id: b7bc9a800e580803fbd7843bb018dd23
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Airbus/derusbi_linux.yar:9:4"
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

## usage_mismatch:bc2bc221c48c722d6240e262b38589e1:search

```yaml
regex_id: bc2bc221c48c722d6240e262b38589e1
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/Webshells/WShell_THOR_Webshells.yar:6262:2"
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

## usage_mismatch:bd5713ed912510d3b30d6ff12ed089ee:search

```yaml
regex_id: bd5713ed912510d3b30d6ff12ed089ee
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/patrickrolsen/patrickrolsen_index.yara:386:1"
```

### Pattern

`echo\ base64_decode\(\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:bd955881f732165a507470bb19f59c69:search

```yaml
regex_id: bd955881f732165a507470bb19f59c69
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_apt30_backspace.yar:824:2"
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

## usage_mismatch:bde4b97a81ad10de36cec946689ca7ec:search

```yaml
regex_id: bde4b97a81ad10de36cec946689ca7ec
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/APT_Industroyer.yar:87:6"
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

## usage_mismatch:be7cb89280737193a4fa1b180286f2fd:search

```yaml
regex_id: be7cb89280737193a4fa1b180286f2fd
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Florian Roth/apt_apt30_backspace.yar:606:2"
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

## intent_mismatch:bea1d4da35d9e8d6c3012fc2324a784b:email

```yaml
regex_id: bea1d4da35d9e8d6c3012fc2324a784b
schema_version: "1"
kind: intent_mismatch
corpus: Inboxscanner
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/TOOLKIT_FinFisher_.yar:86:8"
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

## usage_mismatch:bf56a68430c9d6bb01e680e9a4541bd3:search

```yaml
regex_id: bf56a68430c9d6bb01e680e9a4541bd3
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/gen_metasploit_payloads.yar:190:6"
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

## usage_mismatch:bf8b95eb38af402c4c8c435e8c514039:search

```yaml
regex_id: bf8b95eb38af402c4c8c435e8c514039
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_apt29_grizzly_steppe.yar:96:6"
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

## usage_mismatch:c14f2739a131ffc72829f45563422cc1:search

```yaml
regex_id: c14f2739a131ffc72829f45563422cc1
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/patrickrolsen/misc_shells.yar:70:1"
```

### Pattern

`FILE\ UPLOADED\ TO\ \$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:c3e1d01667c95d72928a39ca5613e69f:search

```yaml
regex_id: c3e1d01667c95d72928a39ca5613e69f
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_apt30_backspace.yar:817:2"
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

## usage_mismatch:c58418016d8d8d5d0d20a08332b19f10:search

```yaml
regex_id: c58418016d8d8d5d0d20a08332b19f10
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_ta18_149A.yar:21:6"
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

## usage_mismatch:c5eabbb080af524285af6215f7f6af43:search

```yaml
regex_id: c5eabbb080af524285af6215f7f6af43
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/APT_APT29_Grizzly_Steppe.yar:92:6"
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

## usage_mismatch:c6493c189605a680083e35d50f56fb87:search

```yaml
regex_id: c6493c189605a680083e35d50f56fb87
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/optiv/autoit_scripting_pos_malware.yar:60:14"
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

## usage_mismatch:c76719bcfd3b31582ed4add426b41646:search

```yaml
regex_id: c76719bcfd3b31582ed4add426b41646
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Rapid7/KeyBoy_Backdoor.yar:9:8"
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

## usage_mismatch:cccf16621c5d21eb07e904d731e4f867:search

```yaml
regex_id: cccf16621c5d21eb07e904d731e4f867
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/TOOLKIT_THOR_HackTools.yar:2775:2"
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

## intent_mismatch:ceaa50ef855e865d12ccf82bcdc99a7f:email

```yaml
regex_id: ceaa50ef855e865d12ccf82bcdc99a7f
schema_version: "1"
kind: intent_mismatch
corpus: Inboxscanner
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/TOOLKIT_FinFisher_.yar:86:8"
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

## usage_mismatch:d139036f621cea76e789c0a8abcafb83:search

```yaml
regex_id: d139036f621cea76e789c0a8abcafb83
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/thor-webshells.yar:45:2"
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

## usage_mismatch:d1dca8cfb1215d84402df6d7a0b81db1:search

```yaml
regex_id: d1dca8cfb1215d84402df6d7a0b81db1
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_apt30_backspace.yar:669:2"
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

## usage_mismatch:d3a5b46884b77fc4f91b1efa247a092e:search

```yaml
regex_id: d3a5b46884b77fc4f91b1efa247a092e
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/APT_APT29_Grizzly_Steppe.yar:89:6"
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

## intent_mismatch:d5805c64d6cde2010819e3cd78e66cbc:hostname

```yaml
regex_id: d5805c64d6cde2010819e3cd78e66cbc
schema_version: "1"
kind: intent_mismatch
corpus: Inboxscanner
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/gen_cn_hacktools.yar:1832:2"
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

## usage_mismatch:d61d37fb0d27aef72748e45113afc946:search

```yaml
regex_id: d61d37fb0d27aef72748e45113afc946
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Rapid7/Rapid7_index.yara:9:8"
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

## usage_mismatch:d70c0dc294dd7c3dabf73ee83e6e6494:search

```yaml
regex_id: d70c0dc294dd7c3dabf73ee83e6e6494
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/thor-webshells.yar:7504:2"
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

## usage_mismatch:da8eb89e49d19ea7e15b771f35237339:search

```yaml
regex_id: da8eb89e49d19ea7e15b771f35237339
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/APT_KeyBoy.yar:40:8"
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

## usage_mismatch:daca736542348f55171d43a5f8c88cc4:search

```yaml
regex_id: daca736542348f55171d43a5f8c88cc4
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_apt30_backspace.yar:606:2"
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

## usage_mismatch:dadbb3e2f70961a21bf3e3640448455d:search

```yaml
regex_id: dadbb3e2f70961a21bf3e3640448455d
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Florian Roth/apt_apt30_backspace.yar:817:2"
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

## usage_mismatch:db5bd5fdce37be1fe3bb3bcfe9e8b88d:search

```yaml
regex_id: db5bd5fdce37be1fe3bb3bcfe9e8b88d
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_op_cleaver.yar:218:2"
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

## usage_mismatch:dbb305a4e347ffc0ebb329ee8f7ea222:search

```yaml
regex_id: dbb305a4e347ffc0ebb329ee8f7ea222
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Florian Roth/apt_poseidon_group.yar:30:2"
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

## usage_mismatch:dbf1b5e8defef1f0e6027b472bf5877d:search

```yaml
regex_id: dbf1b5e8defef1f0e6027b472bf5877d
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/RANSOM_MS17-010_Wannacrypt.yar:172:6"
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

## usage_mismatch:dc2dbe6b77160812531fd863c3d30d16:search

```yaml
regex_id: dc2dbe6b77160812531fd863c3d30d16
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_apt29_grizzly_steppe.yar:77:6"
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

## usage_mismatch:dec3228e25245bfac7bbe6dc50e4f19d:search

```yaml
regex_id: dec3228e25245bfac7bbe6dc50e4f19d
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/APT_eqgrp_apr17.yar:2120:6"
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

## usage_mismatch:ded90131466f0e1f7cc5d55c03932e4a:search

```yaml
regex_id: ded90131466f0e1f7cc5d55c03932e4a
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/APT_KeyBoy.yar:44:8"
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

## usage_mismatch:dfa2faee76fba406e9bdd88dd21e668d:search

```yaml
regex_id: dfa2faee76fba406e9bdd88dd21e668d
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Florian Roth/apt_apt30_backspace.yar:141:2"
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

## usage_mismatch:e199902901c076d00349b7bcdc27b7d6:search

```yaml
regex_id: e199902901c076d00349b7bcdc27b7d6
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/malc0de/malc0de_index.yara:154:2"
```

### Pattern

`tthacksfas@\#\$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:e43453f9646135cc531872a3b8ba7e42:search

```yaml
regex_id: e43453f9646135cc531872a3b8ba7e42
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Florian Roth/apt_derusbi.yar:65:6"
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

## usage_mismatch:e47308019d2335844c1f44ed4c3eb4c5:search

```yaml
regex_id: e47308019d2335844c1f44ed4c3eb4c5
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/gen_metasploit_payloads.yar:187:6"
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

## usage_mismatch:e497c5759de35a80930656a6a0e74f42:search

```yaml
regex_id: e497c5759de35a80930656a6a0e74f42
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Rapid7/Rapid7_index.yara:13:8"
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

## usage_mismatch:e4e7d3fbef34eefad2e1a73d6eff3a6c:search

```yaml
regex_id: e4e7d3fbef34eefad2e1a73d6eff3a6c
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Florian Roth/crime_malware_generic.yar:14:2"
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

## usage_mismatch:e5eb3c6cfaae8de8d9e330a181c110a2:search

```yaml
regex_id: e5eb3c6cfaae8de8d9e330a181c110a2
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Airbus/Airbus_index.yara:10:1"
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

## usage_mismatch:e73c764a3c4282615bdaff5608604f74:search

```yaml
regex_id: e73c764a3c4282615bdaff5608604f74
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/Webshells/WShell_THOR_Webshells.yar:3274:2"
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

## usage_mismatch:e7ec1b832a3cca78839f979b0215fbc0:search

```yaml
regex_id: e7ec1b832a3cca78839f979b0215fbc0
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/gen_powershell_toolkit.yar:179:2"
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

## usage_mismatch:e8807ab24fb53fe83aba22760c2cf20a:search

```yaml
regex_id: e8807ab24fb53fe83aba22760c2cf20a
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_passcv.yar:142:6"
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

## usage_mismatch:eb45550ebb58ed826dd85db636d8b99c:search

```yaml
regex_id: eb45550ebb58ed826dd85db636d8b99c
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Rapid7/KeyBoy_Backdoor.yar:13:8"
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

## usage_mismatch:eeda3c8c35cb77492f1003f6963decfc:search

```yaml
regex_id: eeda3c8c35cb77492f1003f6963decfc
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/thor-webshells.yar:84:2"
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

## usage_mismatch:f239b6d76e80aca5b1c4c79fc0e3bcd4:search

```yaml
regex_id: f239b6d76e80aca5b1c4c79fc0e3bcd4
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/APT_KeyBoy.yar:42:8"
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

## intent_mismatch:f279f0ea3ac3ac45c0760a336689d395:email

```yaml
regex_id: f279f0ea3ac3ac45c0760a336689d395
schema_version: "1"
kind: intent_mismatch
corpus: Inboxscanner
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/TOOLKIT_FinFisher_.yar:15:8"
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

## usage_mismatch:f3390e76e2f1e4a141c272d252fa345f:search

```yaml
regex_id: f3390e76e2f1e4a141c272d252fa345f
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/Florian Roth/apt_apt30_backspace.yar:669:2"
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

## usage_mismatch:fa5461a8b9bffd639f912118bdfee6fe:search

```yaml
regex_id: fa5461a8b9bffd639f912118bdfee6fe
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/rules-master/malware/APT_Snowglobe_Babar.yar:32:8"
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

## usage_mismatch:fa8656eeacc074fb306f84fe059d6b62:search

```yaml
regex_id: fa8656eeacc074fb306f84fe059d6b62
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_derusbi.yar:17:8"
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

## usage_mismatch:fbaf2ac6c1f6b7c35e9f069dd094a1d7:search

```yaml
regex_id: fbaf2ac6c1f6b7c35e9f069dd094a1d7
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/signature-base-master/yara/apt_poisonivy_gen3.yar:16:2"
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

## usage_mismatch:fee2fb509154e514096f954b1fc64478:search

```yaml
regex_id: fee2fb509154e514096f954b1fc64478
schema_version: "1"
kind: usage_mismatch
corpus: Inboxscanner
call_kind: search
shape: null
result: finding
disclosure: private_first
site: "batch/corpora/Inboxscanner/rules/rules/Open-Source-YARA-rules-master/patrickrolsen/misc_shells.yar:66:1"
```

### Pattern

`echo\ base64_decode\(\$`

### Context

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
corpus: Inboxscanner
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
corpus: Inboxscanner
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
corpus: Inboxscanner
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
corpus: Inboxscanner
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

---
schema_version: "1"
corpus: validatorjs
findings: 108
---

# validatorjs batch findings

## usage_mismatch:0269fe932102e462305123a278fe322f

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:6:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[A-ZÆØÅ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:06e47fe50b20faf7e748009fac5df2bd

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:7:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[A-ZÄÖÜß]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:0cc3488f18e94c3d1e520bda88d67843

- result: `finding`
- site: `pilots/validatorjs/src/isURL.js:54:21`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^\[([^\]]+)\](?::([0-9]+))?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:12ac565232cb25e57503a9e7b7385603

- result: `finding`
- site: `pilots/validatorjs/src/isURL.js:126:33`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[a-zA-Z0-9\-_.%:]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:1346a9baf845d2d5dcb02f8a34552f15

- result: `finding`
- site: `pilots/validatorjs/src/isEmail.js:27:26`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[a-z\d!#\$%&'\*\+\-\/=\?\^_`{\|}~\u00A1-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:19cb57a873f9d7db5a4c737825833d1d

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:46:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[\u0A00-\u0A7F]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:1d69e165321abe5ae03655d483a1a874

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:61:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9A-ZÀÉÈÌÎÓÒÙ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:1db736d8ac342ed602b49b6c59cc46da

- result: `finding`
- site: `pilots/validatorjs/src/isEmail.js:28:28`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^([\s\x01-\x08\x0b\x0c\x0e-\x1f\x7f\x21\x23-\x5b\x5d-\x7e\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|(\\[\x01-\x09\x0b\x0c\x0d-\x7f\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## intent_mismatch:1db736d8ac342ed602b49b6c59cc46da

- result: `finding`
- site: `pilots/validatorjs/src/isEmail.js:28:28`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^([\s\x01-\x08\x0b\x0c\x0e-\x1f\x7f\x21\x23-\x5b\x5d-\x7e\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|(\\[\x01-\x09\x0b\x0c\x0d-\x7f\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))*$`

### Context

```json
{"admitted_char": "' '", "keyword": "email", "reason": "name/comment claims validation but pattern admits excluded char"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## intent_mismatch:1db736d8ac342ed602b49b6c59cc46da

- result: `finding`
- site: `pilots/validatorjs/src/isEmail.js:28:28`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^([\s\x01-\x08\x0b\x0c\x0e-\x1f\x7f\x21\x23-\x5b\x5d-\x7e\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|(\\[\x01-\x09\x0b\x0c\x0d-\x7f\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))*$`

### Context

```json
{"admitted_char": "' '", "keyword": "isemail", "reason": "name/comment claims validation but pattern admits excluded char"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:1ee44915d4bfa3e3c2dcd8cd3dbb2003

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:77:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9A-ZÇĞİıÖŞÜ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:1fb00f796ba6271f604e96b44d305cd6

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:70:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9А-ЯЁ\u04D8\u04B0\u0406\u04A2\u0492\u04AE\u049A\u04E8\u04BA]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:2265f96ca0b748a126c4b9266515a51a

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:41:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[\u0B80-\u0BFF]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:2585d6feb44242a7c8512e7e9cb14537

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:66:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9A-ZÆØÅ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:26d8c95e8fa49488084cd5055ac8b84d

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:90:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9\u0C00-\u0C7F.]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:29ec67c724dcdf37f280cbd954cde4c0

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:60:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9A-ZÀÂÆÇÉÈÊËÏÎÔŒÙÛÜŸ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:2a791d3a2165ca4eb7d598ac4ee151a7

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:67:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9A-ZĄĆĘŚŁŃÓŻŹ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:2f94c689b7a35ee61bf56153868b3d33

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:82:6`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[٠١٢٣٤٥٦٧٨٩0-9ءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىيًٌٍَُِّْٰ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:345b2e9551b666f7b87d787c0af5d70f

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:2:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[A-Z]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:36530b606bbe2896496ac9207f7a1878

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:52:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9A-VXYZÇƏĞİıÖŞÜ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:369ee60ca5c667bdb6084685d16160fb

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:24:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[A-ZÁČĎÉÍŇÓŠŤÚÝŽĹŔĽÄÔ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:375ce793e74ece61ed38e4d873eacfd6

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:73:17`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9A-ZČĆŽŠĐ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:3ebdbf5c5aee972e2fcdcf99fe95a3aa

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:88:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9\u0D80-\u0DFF]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:4060a437bd4022234f4f0fbaf9688da4

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:36:6`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^['آاءأؤئبپتثجچحخدذرزژسشصضطظعغفقکگلمنوهةی']+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:434ea64c07743dc7ebc5ea579f7f4c66

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:37:6`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^['ঀঁংঃঅআইঈউঊঋঌএঐওঔকখগঘঙচছজঝঞটঠডঢণতথদধনপফবভমযরলশষসহ়ঽািীুূৃৄেৈোৌ্ৎৗড়ঢ়য়ৠৡৢৣৰৱ৲৳৴৵৶৷৸৹৺৻']+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:47ba68b2e8f0814aacc5d3e723e0c0b3

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:85:6`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^['ঀঁংঃঅআইঈউঊঋঌএঐওঔকখগঘঙচছজঝঞটঠডঢণতথদধনপফবভমযরলশষসহ়ঽািীুূৃৄেৈোৌ্ৎৗড়ঢ়য়ৠৡৢৣ০১২৩৪৫৬৭৮৯ৰৱ৲৳৴৵৶৷৸৹৺৻']+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:4b49c8f6e094fbde31b8887038454605

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:76:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[ก-๙\s]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:4bb2e58a76195915cc602bb537a884d7

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:33:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[ئابپتجچحخدرڕزژسشعغفڤقکگلڵمنوۆھەیێيطؤثآإأكضصةظذ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:50e0bb5bb55c1764db545c56bb5156e5

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:16:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[A-ZÁÉËÏÓÖÜÚ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:53c49069f45be2003090a22b9654022e

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:22:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[А-ЯЁ\u04D8\u04B0\u0406\u04A2\u0492\u04AE\u049A\u04E8\u04BA]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:579fc4b3d00e645bf819a0f59e99b278

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:29:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[A-ZÇĞİıÖŞÜ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:5f555d940b63928ed06e2948353b86e3

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:65:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9A-ZÁÉËÏÓÖÜÚ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:6414feac6740bbd2b084e7bb50e00040

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:47:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[\u0B00-\u0B7F]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:656b251274803d30ba08e316fecdf81f

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:84:6`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^['0-9آاءأؤئبپتثجچحخدذرزژسشصضطظعغفقکگلمنوهةی۱۲۳۴۵۶۷۸۹۰']+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:6678d054899b7ffc4ad7b673e6e90403

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:23:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[A-ZČĆĐŠŽ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:66a0b3ea9fde7213d0adeda7acbcae59

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:39:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[\u0900-\u0961]+[\u0972-\u097F]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:673a7f9545d608198a038053af478fd8

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:38:6`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[ABCĈD-GĜHĤIJĴK-PRSŜTUŬVZ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:6aa8674f0f9dfc52e34bdcd8dfa6e6b2

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:53:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9А-Я]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:6f9e3d7ec412de462619f463436d0b1b

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:10:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:72844b5abe60c45885969f4008dfbb59

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:51:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9A-Z]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:72af04d05ce826215a3f03a21d7f4581

- result: `finding`
- site: `pilots/validatorjs/src/isAscii.js:4:14`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[\x00-\x7F]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:744be5bd65819d246fc99b72f096f61d

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:15:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[A-ZÆØÅ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:749194df806690460689178c915daba2

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:9:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[A-ZÁÉÍÑÓÚÜ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:766a5c8f4bf1bd143d5549708dc2df55

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:31:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[A-ZÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴĐÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:7b20a0245d108947f52f8727c1992235

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:58:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9A-ZÁÉÍÑÓÚÜ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:7c9faf0e3da9609fc5f31f03b2ef4e7d

- result: `finding`
- site: `pilots/validatorjs/src/isURL.js:241:9`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:810b8b7c9590b1030a01bccf83133e14

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:78:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9А-ЩЬЮЯЄIЇҐі]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:821c3c55f4e9a55115432b8718bbf967

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:18:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[A-ZÁÉÍÓÖŐÚÜŰ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:82775c0974e9ecb06d87184210120646

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:91:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9\u0C80-\u0CFF.]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:83acc5390f4da3d21735da28519f7502

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:21:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[А-ЯЁ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:840a7452b2ed02a43f3e6f61f409b82c

- result: `finding`
- site: `pilots/validatorjs/src/isEmail.js:26:24`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^([\s\x01-\x08\x0b\x0c\x0e-\x1f\x7f\x21\x23-\x5b\x5d-\x7e]|(\\[\x01-\x09\x0b\x0c\x0d-\x7f]))*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## intent_mismatch:840a7452b2ed02a43f3e6f61f409b82c

- result: `finding`
- site: `pilots/validatorjs/src/isEmail.js:26:24`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^([\s\x01-\x08\x0b\x0c\x0e-\x1f\x7f\x21\x23-\x5b\x5d-\x7e]|(\\[\x01-\x09\x0b\x0c\x0d-\x7f]))*$`

### Context

```json
{"admitted_char": "' '", "keyword": "email", "reason": "name/comment claims validation but pattern admits excluded char"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## intent_mismatch:840a7452b2ed02a43f3e6f61f409b82c

- result: `finding`
- site: `pilots/validatorjs/src/isEmail.js:26:24`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^([\s\x01-\x08\x0b\x0c\x0e-\x1f\x7f\x21\x23-\x5b\x5d-\x7e]|(\\[\x01-\x09\x0b\x0c\x0d-\x7f]))*$`

### Context

```json
{"admitted_char": "' '", "keyword": "isemail", "reason": "name/comment claims validation but pattern admits excluded char"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:85bb6157aa857528ff11b65078708a0f

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:40:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[\u0D80-\u0DFF]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:860d15a11c0f5e2d7cb35d24979c63db

- result: `finding`
- site: `pilots/validatorjs/src/isEmail.js:25:22`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[a-z\d]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:87ff7f94641f3f9b619e39cd99a554f9

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:71:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9A-ZČĆĐŠŽ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:88d6a76df68541b2965a341365c9f9f6

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:26:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[А-ЯЂЈЉЊЋЏ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:8f29da4cad44e03debc8719de1a2335a

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:42:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[\u0C00-\u0C7F]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:915d795d72d9c792455394e3c4aeab76

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:57:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9Α-ω]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:967328585a1cd093dcfbbeafec7bad82

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:3:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[A-VXYZÇƏĞİıÖŞÜ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:96bbcf281074ab04576ebe08c136b664

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:83:6`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9א-ת]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:97d8bce14dccd63d9e69a508532999cf

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:87:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[\u0900-\u0963]+[\u0966-\u097F]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:a2916255594260438b96073530048de2

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:20:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[A-ZÃÁÀÂÄÇÉÊËÍÏÕÓÔÖÚÜ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:a310b7ce02549c71fec7f7dbe0716eca

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:27:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[A-ZÅÄÖ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:a36c6a57fd269bf9fa53c80e57269d49

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:43:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[\u0C80-\u0CFF]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:a3d3b4865681d9d241f725ac38e4c9cc

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:45:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[\u0A80-\u0AFF]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:a4256cc1216985eed8b3343a0ff3cb2c

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:12:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[A-ZÀÂÆÇÉÈÊËÏÎÔŒÙÛÜŸ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:a916a1ba4d37a1e8d2a687e993118408

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:89:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9\u0B80-\u0BFF.]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:ac1543fa2d92d64cf07f3cd27bb23470

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:62:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9０-９ぁ-んァ-ヶｦ-ﾟ一-龠ー・。、]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:b2512fce227383b38cb4eb68ae67a136

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:17:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[A-ZÆØÅ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:b51c2e4cfebe6cc8ccee6b01e98ef042

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:59:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9A-ZÅÄÖ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:b9444708b03283a6b0b564b051f6ad32

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:93:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9\u0A80-\u0AFF.]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:bd687b825924cdabd6a7ea8de68609e2

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:34:6`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[ءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىيًٌٍَُِّْٰ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:c00e45965d1642ef882ac19ba20f8c4c

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:28:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[ก-๐\s]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:c14252a1bbbd87a8c8e8a9d37e2e881c

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:35:6`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[א-ת]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:c217150e3852ffd4308582734333323f

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:19:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[A-ZĄĆĘŚŁŃÓŻŹ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:c26143d5cd40e52923049cecaf5cdb40

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:32:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[ㄱ-ㅎㅏ-ㅣ가-힣]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:c52151d9129002def52afbcd06448954

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:75:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9A-ZÅÄÖ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:c5abebab5cb480988c0d47628c999a91

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:86:6`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9ABCĈD-GĜHĤIJĴK-PRSŜTUŬVZ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:c5f8f956f3611e9b58b7213af9bf36ab

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:5:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:cc0230d473dcfb3d8e5d846078951d42

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:25:17`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[A-ZČĆŽŠĐ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:cf2db4155ad1aa9bf082bc6929827046

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:79:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9ㄱ-ㅎㅏ-ㅣ가-힣]*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:d4a9c88413f46c7b4c929e7b3f1a7b58

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:95:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9\u0B00-\u0B7F.]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:d557a08422e5bce2d636957820d87963

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:69:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9А-ЯЁ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:d7bd2b6bd00720421d9777cb39c22dce

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:68:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9A-ZÃÁÀÂÄÇÉÊËÍÏÕÓÔÖÚÜ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:d7fe8d625e2c0fba5f23705e79fdfcfb

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:13:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[A-ZÀÉÈÌÎÓÒÙ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:dc717c37ced360bbb056eef7777056b4

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:55:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9A-ZÆØÅ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:e20210c2217e3c0fb45d9c1f3b257994

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:8:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[Α-ώ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:e526b783ed78f18c5a4d1156b72fd3b5

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:72:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9A-ZÁČĎÉÍŇÓŠŤÚÝŽĹŔĽÄÔ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:e5a3a761e328f30e619146cca2fbdd89

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:64:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9A-ZÆØÅ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:e608f223f30834b72c2a211cec20017c

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:81:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9A-ZÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴĐÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:e6700f7a5c0b379b735010566de43380

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:74:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9А-ЯЂЈЉЊЋЏ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:e8e7784ea8a94af7de766ab8655315b4

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:92:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9\u0D00-\u0D7F.]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:e975ad919801eb3f88e778b606d58d74

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:30:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[А-ЩЬЮЯЄIЇҐі]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:eadec792a051633827b7b60a95acc243

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:80:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[٠١٢٣٤٥٦٧٨٩0-9ئابپتجچحخدرڕزژسشعغفڤقکگلڵمنوۆھەیێيطؤثآإأكضصةظذ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:ebe7c4b41f675ba2179bba3c48612691

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:14:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[ぁ-んァ-ヶｦ-ﾟ一-龠ー・。、]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:ec761e48727e9653f74a3793a9861ab4

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:56:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9A-ZÄÖÜß]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:f506330f9f0970543a309069a0c0bc39

- result: `finding`
- site: `pilots/validatorjs/src/isEmail.js:24:44`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`=\?\^_`{\|}~]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:f7ce3c4a405dbc65f933168be88a8279

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:94:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9\u0A00-\u0A7F.]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:f82a5cf824aece5c04cfe39446fe9fe2

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:11:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[A-ZÅÄÖ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:fc8436a91c12381285726d12670c1c55

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:54:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:fc97803916db29f52899f39c73c4b2c1

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:4:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[А-Я]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:fcbe7cb1ec6174ed1230a33ab10bde48

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:44:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[\u0D00-\u0D7F]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## usage_mismatch:fe0bebba65f84199e57d14bfd87ed621

- result: `finding`
- site: `pilots/validatorjs/src/alpha.js:63:11`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

`^[0-9A-ZÁÉÍÓÖŐÚÜŰ]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## property:inventory:v-shape1-injection-chars

- result: `planned`
- site: `inventory:v-shape1-injection-chars`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

``

### Context

```json
{"question_id": "v-shape1-injection-chars", "threat": "Validator alphabet admits shell/HTML injection characters"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## property:inventory:v-shape2-whitelist-space

- result: `planned`
- site: `inventory:v-shape2-whitelist-space`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

``

### Context

```json
{"question_id": "v-shape2-whitelist-space", "threat": "Whitelisted string of bounded length contains forbidden separator"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## property:inventory:v-shape3-prefix-vs-full

- result: `planned`
- site: `inventory:v-shape3-prefix-vs-full`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

``

### Context

```json
{"question_id": "v-shape3-prefix-vs-full", "threat": "Prefix match accepts values that fail full-string validation intent"}
```

### Witness

```json
null
```

### Ground-truth

N/A

## property:inventory:v-shape4-escape-image

- result: `planned`
- site: `inventory:v-shape4-escape-image`
- ground_truth_status: `N/A`
- disclosure: `None`

### Pattern

``

### Context

```json
{"question_id": "v-shape4-escape-image", "threat": "Escaped output still contains raw control characters"}
```

### Witness

```json
null
```

### Ground-truth

N/A

---
schema_version: "1"
corpus: pass-culture-pass-culture-main
findings: 75
---

# pass-culture-pass-culture-main batch findings

## usage_mismatch:02f4f2dcd3fc1c0b1e31f2ece20a1e4c:search

```yaml
regex_id: 02f4f2dcd3fc1c0b1e31f2ece20a1e4c
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/Homepage/components/CollectiveOffersCardsContainer/CollectiveOffersCardsContainer.spec.tsx:82:51"
```

### Pattern

`^card-`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:05f553d54398d8f0f8086684719e6694:search

```yaml
regex_id: 05f553d54398d8f0f8086684719e6694
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/IndividualOffer/IndividualOfferPriceTable/commons/utils/__specs__/toThingStocksBulkUpsertBodyModel.spec.ts:84:6"
```

### Pattern

`T\d{2}:\d{2}:\d{2}Z$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:07328fc2259774e73d05b4b9ed69736e:email

```yaml
regex_id: 07328fc2259774e73d05b4b9ed69736e
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/EmailChangeValidation/EmailChangeValidation.spec.tsx:34:8"
```

### Pattern

`Merci d’avoir confirmé votre changement d’adresse email.`

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

## intent_mismatch:117f3c1308393b1e2b88f6e4ab954f93:email

```yaml
regex_id: 117f3c1308393b1e2b88f6e4ab954f93
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/ui-kit/form/EmailSpellCheckInput/EmailSpellCheckInput.spec.tsx:99:12"
```

### Pattern

`Appliquer la modification`

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

## usage_mismatch:11964d5306518f78977891dcf9b3942a:search

```yaml
regex_id: 11964d5306518f78977891dcf9b3942a
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/app/App/analytics/sentry.ts:150:6"
```

### Pattern

`^chrome:\/\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:13f90b3f364cede19e417618ff0f4e0b:email

```yaml
regex_id: 13f90b3f364cede19e417618ff0f4e0b
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/User/UserProfile/UserAnonymization/UserAnonymization.spec.tsx:119:30"
```

### Pattern

`Confirmer votre adresse email`

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

## intent_mismatch:1bd27ec651e7f3c4c545b79aa1b130e1:email

```yaml
regex_id: 1bd27ec651e7f3c4c545b79aa1b130e1
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/User/UserProfile/UserAnonymization/UserAnonymization.spec.tsx:296:47"
```

### Pattern

`Confirmer votre adresse email`

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

## usage_mismatch:27b85e962ca170848af44fbd1bb5a29e:search

```yaml
regex_id: 27b85e962ca170848af44fbd1bb5a29e
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/scripts/customRequest.ts:34:4"
```

### Pattern

`^(Blob|File)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:28d09e6bd8c3e1e10fc70fab35fb1b3a:email

```yaml
regex_id: 28d09e6bd8c3e1e10fc70fab35fb1b3a
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/LostPassword/LostPassword.spec.tsx:85:30"
```

### Pattern

`Adresse email *`

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

## intent_mismatch:2bb54d8554aed1a46f8eca2be457e4a9:email

```yaml
regex_id: 2bb54d8554aed1a46f8eca2be457e4a9
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/User/UserProfile/UserAnonymization/UserAnonymization.spec.tsx:252:47"
```

### Pattern

`Confirmer votre adresse email`

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

## usage_mismatch:2f78ba997d912b72695c0eaefa0b200b:search

```yaml
regex_id: 2f78ba997d912b72695c0eaefa0b200b
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/IndividualOffer/IndividualOfferMedia/commons/getUrlYoutubeError.ts:4:2"
```

### Pattern

`^(https?:\/\/)(www\.)?(m\.)?(youtube\.com\b|youtu\.be\b)(\/watch\?v=|\/embed\/|\/v\/|\/e\/|\/)([\w-]{11}\b)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:2f9667d6f38122a342fba704f8e7d93b:search

```yaml
regex_id: 2f9667d6f38122a342fba704f8e7d93b
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/app/App/analytics/sentry.ts:151:6"
```

### Pattern

`^chrome-extension:\/\/`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:308e278258ec1ad190116190fbb5b010:search

```yaml
regex_id: 308e278258ec1ad190116190fbb5b010
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/commons/utils/timezone.ts:11:18"
```

### Pattern

`^([01]?\d|2[0-3]):([0-5]\d)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:32c8c89c18cda124756a8d8fdd9ac601:email

```yaml
regex_id: 32c8c89c18cda124756a8d8fdd9ac601
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/Collaborators/__specs__/Collaborators.spec.tsx:116:23"
```

### Pattern

`Veuillez renseigner un email valide`

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

## intent_mismatch:333200259b339016a367f0a858fbb5d5:email

```yaml
regex_id: 333200259b339016a367f0a858fbb5d5
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/EmailChangeValidation/EmailChangeValidation.spec.tsx:47:8"
```

### Pattern

`Votre adresse email n’a pas été modifiée car le lien`

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

## intent_mismatch:395808f496b11bd680cf8d01e0a38e04:email

```yaml
regex_id: 395808f496b11bd680cf8d01e0a38e04
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/Onboarding/OnboardingOffersTypeChoice/OnboardingOffersTypeChoice.spec.tsx:19:8"
```

### Pattern

`Notre équipe vous contactera par email pour vous demander vos justificatifs d’inscription.`

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

## intent_mismatch:3afafd2bf4dcfd210137ce9bb300eb7e:email

```yaml
regex_id: 3afafd2bf4dcfd210137ce9bb300eb7e
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/Signup/SignupContainer/__specs__/SignupContainer.spec.tsx:159:16"
```

### Pattern

`Adresse email *`

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

## intent_mismatch:41251ea848a60aae06311cb954d7fe01:email

```yaml
regex_id: 41251ea848a60aae06311cb954d7fe01
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/AdageIframe/app/components/OffersInstantSearch/OffersSearch/Offers/OfferShareLink/__specs__/OfferShareLink.spec.tsx:45:14"
```

### Pattern

`Partager par email`

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

## usage_mismatch:43bad10ca9c0f969072fd6711b243fb9:search

```yaml
regex_id: 43bad10ca9c0f969072fd6711b243fb9
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/Homepage/components/CollectiveOffersCardsContainer/CollectiveOffersCardsContainer.spec.tsx:54:54"
```

### Pattern

`^card-`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:46dfc58c9a6be25a26c4ec8989e203bc:search

```yaml
regex_id: 46dfc58c9a6be25a26c4ec8989e203bc
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/ui-kit/InfoPanel/InfoPanel.spec.tsx:69:32"
```

### Pattern

`^\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:4c79db593c4f7c44400b10f4a52f2df1:email

```yaml
regex_id: 4c79db593c4f7c44400b10f4a52f2df1
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/IndividualOffer/IndividualOfferPracticalInfos/components/IndividualOfferPracticalInfosForm/IndividualOfferPracticalInfosForm.spec.tsx:119:28"
```

### Pattern

`Email auquel envoyer les notifications`

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

## usage_mismatch:4d1332f2baee0a3c59afd7cd04487fe5:search

```yaml
regex_id: 4d1332f2baee0a3c59afd7cd04487fe5
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/commons/store/user/dispatchers/__specs__/logout.spec.ts:38:28"
```

### Pattern

`\/users\/signout$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:4d7f349fea6ac0ab3360dec83b268b87:search

```yaml
regex_id: 4d7f349fea6ac0ab3360dec83b268b87
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/scripts/customRequest.ts:35:4"
```

### Pattern

`^(Blob|File)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:5a310eca7946914df0e4fccc806318fe:email

```yaml
regex_id: 5a310eca7946914df0e4fccc806318fe
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/ui-kit/form/EmailSpellCheckInput/EmailSpellCheckInput.spec.tsx:107:27"
```

### Pattern

`Voulez-vous plutôt dire`

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

## usage_mismatch:5ae391da56b6603dd0f92a123407ded1:search

```yaml
regex_id: 5ae391da56b6603dd0f92a123407ded1
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/Desk/components/validationDeskSchema.ts:4:27"
```

### Pattern

`^[A-Z0-9]+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:6110e8117784b8c0724c47863b9e80b1:search

```yaml
regex_id: 6110e8117784b8c0724c47863b9e80b1
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/commons/utils/coords.ts:3:2"
```

### Pattern

`^(-?(?:[1-8]?\d(?:\.\d+)?|90(?:\.0+)?|-90(?:\.0+)?))\s*,\s*(-?(?:1[0-7]\d|\d{1,2})(?:\.\d+)?|180(?:\.0+)?|-180(?:\.0+)?)$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:61538a7f564d402f1114259bdd772a6f:email

```yaml
regex_id: 61538a7f564d402f1114259bdd772a6f
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/LostPassword/LostPassword.spec.tsx:55:46"
```

### Pattern

`Vous allez recevoir un email`

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

## usage_mismatch:64212c9e4c08fd1310dd2fe3ac7eb7a6:search

```yaml
regex_id: 64212c9e4c08fd1310dd2fe3ac7eb7a6
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/Homepage/components/CollectiveOffersCardsContainer/CollectiveOffersCardsContainer.spec.tsx:88:48"
```

### Pattern

`^card-`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:6ab962d3acad5bcabc0af732653590f2:email

```yaml
regex_id: 6ab962d3acad5bcabc0af732653590f2
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/ui-kit/form/EmailSpellCheckInput/EmailSpellCheckInput.spec.tsx:55:25"
```

### Pattern

`Voulez-vous plutôt dire`

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

## intent_mismatch:6f619b1c5c8a4764a1f7bb8951e491a5:email

```yaml
regex_id: 6f619b1c5c8a4764a1f7bb8951e491a5
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/ui-kit/form/EmailSpellCheckInput/EmailSpellCheckInput.spec.tsx:66:25"
```

### Pattern

`Voulez-vous plutôt dire`

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

## intent_mismatch:72d0f093876c361355d1da18353bbcd1:email

```yaml
regex_id: 72d0f093876c361355d1da18353bbcd1
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/User/UserProfile/UserAnonymization/UserAnonymization.spec.tsx:274:47"
```

### Pattern

`Confirmer votre adresse email`

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

## usage_mismatch:749cbf755007169718fde11057fb672f:search

```yaml
regex_id: 749cbf755007169718fde11057fb672f
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/api/src/pcapi/static/backoffice/js/core/pc-event-handler.js:63:27"
```

### Pattern

`::\d+$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:759f79eb90f913d373d7939aeeaddc43:email

```yaml
regex_id: 759f79eb90f913d373d7939aeeaddc43
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/ui-kit/form/EmailSpellCheckInput/EmailSpellCheckInput.spec.tsx:77:25"
```

### Pattern

`Voulez-vous plutôt dire`

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

## intent_mismatch:76731aa2cce3d354406bdfc5be76fd18:email

```yaml
regex_id: 76731aa2cce3d354406bdfc5be76fd18
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/LostPassword/LostPassword.spec.tsx:190:30"
```

### Pattern

`Adresse email *`

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

## usage_mismatch:7995442da42e918e5cf444cf6d4d37b3:search

```yaml
regex_id: 7995442da42e918e5cf444cf6d4d37b3
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/commons/utils/isValidEmail.ts:6:4"
```

### Pattern

`^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:79efae35f16301a76408ed984c9510b1:email

```yaml
regex_id: 79efae35f16301a76408ed984c9510b1
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/Signup/SignupContainer/__specs__/SignupContainer.spec.tsx:482:18"
```

### Pattern

`Adresse email *`

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

## usage_mismatch:7b1a181d5b20851681b30761ff5f1afc:search

```yaml
regex_id: 7b1a181d5b20851681b30761ff5f1afc
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/Homepage/components/CollectiveOffersCardsContainer/CollectiveOffersCardsContainer.spec.tsx:44:51"
```

### Pattern

`^card-`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:8224fef423ef6850d2464231d00477ab:email

```yaml
regex_id: 8224fef423ef6850d2464231d00477ab
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/Signup/SignupContainer/__specs__/SignupContainer.spec.tsx:197:20"
```

### Pattern

`Adresse email *`

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

## usage_mismatch:83cec594e7e9fbdc3de2bc8a6611c4da:search

```yaml
regex_id: 83cec594e7e9fbdc3de2bc8a6611c4da
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/commons/utils/coords.ts:56:2"
```

### Pattern

`^(-?\d+(?:\.\d+)?)[°:d]?\s?(?:(\d+(?:\.\d+)?)['′ʹ:]?\s?(?:(\d+(?:\.\d+)?)["″ʺ]?)?)?\s?([NSEW])?`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:84682a9464b4c1380c0de0c111cacd88:email

```yaml
regex_id: 84682a9464b4c1380c0de0c111cacd88
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/LostPassword/LostPassword.spec.tsx:164:30"
```

### Pattern

`Adresse email *`

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

## usage_mismatch:84f38e0e725d54556d824cfd46718e17:search

```yaml
regex_id: 84f38e0e725d54556d824cfd46718e17
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/scripts/sanitize_enum_keys.js:12:22"
```

### Pattern

`^(export enum \w+ \{)([\s\S]*?)(^\})`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:899f46566901bf28e53130de95b1804c:email

```yaml
regex_id: 899f46566901bf28e53130de95b1804c
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/User/UserProfile/BannerPendingEmailValidation/BannerPendingEmailValidation.spec.tsx:9:12"
```

### Pattern

`Je n’ai pas reçu le lien de confirmation`

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

## intent_mismatch:920d030d3ae04264731d511d0dae0499:email

```yaml
regex_id: 920d030d3ae04264731d511d0dae0499
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/User/UserProfile/UserAnonymization/UserAnonymization.spec.tsx:225:47"
```

### Pattern

`Confirmer votre adresse email`

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

## usage_mismatch:92e48b64bedaeacaadf174f043f0207c:search

```yaml
regex_id: 92e48b64bedaeacaadf174f043f0207c
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/IndividualOffer/IndividualOfferPriceTable/commons/utils/__specs__/toThingStocksBulkUpsertBodyModel.spec.ts:142:6"
```

### Pattern

`2025-10-26T\d{2}:\d{2}:\d{2}Z$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:9461ec6b6982d1dc5b9a750557796c64:email

```yaml
regex_id: 9461ec6b6982d1dc5b9a750557796c64
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/Signup/SignupContainer/__specs__/SignupContainer.spec.tsx:398:32"
```

### Pattern

`Adresse email`

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

## intent_mismatch:96378239fc4b0f0f14f32f95ebbba3f8:email

```yaml
regex_id: 96378239fc4b0f0f14f32f95ebbba3f8
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/LostPassword/LostPassword.spec.tsx:111:30"
```

### Pattern

`Adresse email *`

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

## intent_mismatch:99a27b93c4ae99e870b7366d07c8f516:email

```yaml
regex_id: 99a27b93c4ae99e870b7366d07c8f516
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/CollectiveOffer/CollectiveOffer/components/OfferEducational/__specs__/OfferEducationalEdition.spec.tsx:70:28"
```

### Pattern

`Email auquel envoyer les notifications`

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

## usage_mismatch:99f6cee79146f85688963ee6cc5f371b:search

```yaml
regex_id: 99f6cee79146f85688963ee6cc5f371b
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/CollectiveOffer/CollectiveOffer/components/OfferEducational/validationSchema.ts:44:8"
```

### Pattern

`^$|(\d{1,2}:[0-5]\d)`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:9aeec805b749736c39fe3fd5b6c926d6:email

```yaml
regex_id: 9aeec805b749736c39fe3fd5b6c926d6
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/LostPassword/LostPassword.spec.tsx:123:46"
```

### Pattern

`Vous allez recevoir un email`

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

## usage_mismatch:9d4153906622865b3c20297b9008ea5e:search

```yaml
regex_id: 9d4153906622865b3c20297b9008ea5e
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/IndividualOffer/IndividualOfferDescription/commons/validationSchema.ts:90:21"
```

### Pattern

`^([01]?\d|2[0-3]):[0-5]\d$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:a3847315559e3e177bff1843283cb220:email

```yaml
regex_id: a3847315559e3e177bff1843283cb220
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/Signup/SignupContainer/__specs__/SignupContainer.spec.tsx:327:20"
```

### Pattern

`Adresse email *`

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

## intent_mismatch:a6decc9f6240001665c1518a16c0a6cb:email

```yaml
regex_id: a6decc9f6240001665c1518a16c0a6cb
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/components/ReSendEmailCallout/ReSendEmailCallout.spec.tsx:23:57"
```

### Pattern

`Email non reçu ?`

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

## intent_mismatch:b2ce80be238cab4269a516daeb86a064:email

```yaml
regex_id: b2ce80be238cab4269a516daeb86a064
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/Signup/SignupContainer/__specs__/SignupContainer.spec.tsx:264:20"
```

### Pattern

`Adresse email *`

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

## usage_mismatch:b2dba365cf1cf1bf9eb89f1b2d1c1b9c:search

```yaml
regex_id: b2dba365cf1cf1bf9eb89f1b2d1c1b9c
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/commons/utils/coords.ts:7:2"
```

### Pattern

`^(?:90|(?:[0-8]?\d))[°\s](?:[0-5]?\d)['\s](?:[0-5]?\d(?:[.,]\d{1,5})?)["\s]?[NS]\s(?:180|(?:1[0-7]\d)|(?:0?\d\d)|(?:\d))[°\s](?:[0-5]?\d)['\s](?:[0-5]?\d(?:[.,]\d{1,5})?)["\s]?[EW]$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:b3302c769d58b461a4591c44fd184b89:email

```yaml
regex_id: b3302c769d58b461a4591c44fd184b89
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/LostPassword/LostPassword.spec.tsx:94:46"
```

### Pattern

`Vous allez recevoir un email`

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

## intent_mismatch:bde886a7d1090fa687eae12979ada7f5:email

```yaml
regex_id: bde886a7d1090fa687eae12979ada7f5
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/AdageIframe/app/components/OffersInstantSearch/OffersSearch/Offers/OfferShareLink/__specs__/OfferShareLink.spec.tsx:57:12"
```

### Pattern

`Partager par email`

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

## intent_mismatch:bf58a32cb5d1079f2b3df1257d6c9cae:email

```yaml
regex_id: bf58a32cb5d1079f2b3df1257d6c9cae
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/Signup/__specs__/Signup.spec.tsx:72:28"
```

### Pattern

`Validez votre adresse email`

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

## usage_mismatch:c48a68b010a461a2b7334f88866d1658:search

```yaml
regex_id: c48a68b010a461a2b7334f88866d1658
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/Homepage/components/CollectiveOffersTemplateCard/components/CollectiveOffersTemplateLine/CollectiveOffersTemplateLine.spec.tsx:98:30"
```

### Pattern

`^Du `

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## usage_mismatch:d3a5b866e735e8e9d2de6a9ac224d4dd:search

```yaml
regex_id: d3a5b866e735e8e9d2de6a9ac224d4dd
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/commons/core/VenueEdition/getVolunteeringUrlError.ts:3:32"
```

### Pattern

`^\/organisations\/[^/]+\/?$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:d7d10a83972170a7098538008c151fbe:email

```yaml
regex_id: d7d10a83972170a7098538008c151fbe
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/User/UserProfile/UserAnonymization/UserAnonymization.spec.tsx:318:47"
```

### Pattern

`Confirmer votre adresse email`

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

## intent_mismatch:d9a57b935630808e92616cb5b534c6b6:email

```yaml
regex_id: d9a57b935630808e92616cb5b534c6b6
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/LostPassword/LostPassword.spec.tsx:200:46"
```

### Pattern

`Vous allez recevoir un email`

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

## intent_mismatch:dc325fa04a01a31a708694803f1d4448:email

```yaml
regex_id: dc325fa04a01a31a708694803f1d4448
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/Signup/SignupConfirmation/SignupConfirmation.spec.tsx:24:28"
```

### Pattern

`Email non reçu ?`

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

## intent_mismatch:dc7e8d4e1ac83602f52d4e67942ac717:email

```yaml
regex_id: dc7e8d4e1ac83602f52d4e67942ac717
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/Signup/SignupContainer/__specs__/SignupContainer.spec.tsx:431:18"
```

### Pattern

`Adresse email *`

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

## intent_mismatch:df3a199bfc033d3c694bc6fc5b0c7479:email

```yaml
regex_id: df3a199bfc033d3c694bc6fc5b0c7479
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/User/UserProfile/UserAnonymization/UserAnonymization.spec.tsx:197:47"
```

### Pattern

`Confirmer votre adresse email`

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

## intent_mismatch:dfea42383954b18e82b5218084a45791:email

```yaml
regex_id: dfea42383954b18e82b5218084a45791
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/LostPassword/LostPassword.spec.tsx:44:30"
```

### Pattern

`Adresse email *`

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

## usage_mismatch:dff7afe022b8c131384a8d456f63afed:search

```yaml
regex_id: dff7afe022b8c131384a8d456f63afed
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/IndividualOffer/IndividualOfferDescription/commons/validationSchema.ts:9:11"
```

### Pattern

`^\d*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:e1d8a35763c7e24a6c4da232d0cd008e:email

```yaml
regex_id: e1d8a35763c7e24a6c4da232d0cd008e
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/CollectiveOffer/CollectiveOffer/components/OfferEducational/OfferEducationalForm/FormContactTemplate/__specs__/FormContactTemplate.spec.tsx:43:14"
```

### Pattern

`Adresse email`

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

## usage_mismatch:e8a081fb17076c43f8087dee754ae9b5:search

```yaml
regex_id: e8a081fb17076c43f8087dee754ae9b5
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/scripts/sanitize_enum_keys.js:15:21"
```

### Pattern

`^(\s*)[^=\n]+=\s*'([^']+)'`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:f78c70e719bf3f2ac54ca9168d94a91c:email

```yaml
regex_id: f78c70e719bf3f2ac54ca9168d94a91c
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/ui-kit/form/EmailSpellCheckInput/EmailSpellCheckInput.spec.tsx:88:30"
```

### Pattern

`Voulez-vous plutôt dire`

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

## usage_mismatch:f84d56ef6c050cbf218ad9c12d23ab5d:search

```yaml
regex_id: f84d56ef6c050cbf218ad9c12d23ab5d
schema_version: "1"
kind: usage_mismatch
corpus: pass-culture-pass-culture-main
call_kind: search
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/scripts/format_generated_index_exports.js:12:18"
```

### Pattern

`^export\s*\{([^}]+)\}\s*from\s*('[^']+'|"[^"]+");?\s*$`

### Context

```json
{"call_kind": "search", "reason": "anchored pattern consumed via search/test"}
```

### Witness

```json
null
```

### Ground-truth

None

## intent_mismatch:fb97b166b5a72b730cdc9e2b8d608e6a:email

```yaml
regex_id: fb97b166b5a72b730cdc9e2b8d608e6a
schema_version: "1"
kind: intent_mismatch
corpus: pass-culture-pass-culture-main
shape: null
result: finding
disclosure: null
site: "batch/corpora/pass-culture-pass-culture-main/rules/pro/src/pages/Signup/__specs__/Signup.spec.tsx:47:33"
```

### Pattern

`Adresse email`

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
corpus: pass-culture-pass-culture-main
shape: 1
result: planned
ground_truth_status: planned
disclosure: null
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
corpus: pass-culture-pass-culture-main
shape: 2
result: planned
ground_truth_status: planned
disclosure: null
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
corpus: pass-culture-pass-culture-main
shape: 3
result: planned
ground_truth_status: planned
disclosure: null
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
corpus: pass-culture-pass-culture-main
shape: 4
result: planned
ground_truth_status: planned
disclosure: null
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

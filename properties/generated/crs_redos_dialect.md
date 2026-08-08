# CRS ReDoS + dialect triage

- @rx sites: 318
- encodable: 125
- ReDoS findings (uncapped): 153
- Noodler available: False (changed=False)

## Unencodable routing

| reason | count | route | note |
|---|---:|---|---|
| `ok` | 125 | prove | encodable — Z3 property / rule_diff / ReDoS |
| `pattern-too-long` | 73 | policy | Capacity cap (>256 chars), not a language limit. Policy: keep cap for interactive Z3 queries; triage long patterns to ReDoS-only / manual review. |
| `parse-error` | 53 | prove | Often lazy quantifiers / hex escapes — language-transparent strip candidates. |
| `negated-class` | 32 | prove | Encodable in principle (TRAPS #1/#10) — toolkit-fix candidate. |
| `word-boundary` | 22 | triage | Genuine stock-Z3 limit (gate-3 \b direction); ASCII domain declared for CRS. |
| `bad-range` | 6 | prove | \x{} / hex ranges — toolkit-fix candidate. |
| `inline-flag` | 6 | prove | Scoped (?i:...) lifting — toolkit-fix candidate. |
| `internal-anchor` | 1 | triage | unclassified reject — inspect |

## Pattern-too-long policy

Capacity cap (>256 chars), not a language limit. Policy: keep cap for interactive Z3 queries; triage long patterns to ReDoS-only / manual review.

## ReDoS PASS/FAIL rows (sample)

| regex_id | result | tool |
|---|---|---|
| `fc213c69c51a78074b9db7a79c0a3cdf` | safe | recheck |
| `2937d3663e1c9621508e03be9d879b61` | safe | recheck |
| `12da5e9c854a440c3271a24da8a58565` | safe | recheck |
| `3c24ea1b0584bffeaa6dfd0731c8be89` | safe | recheck |
| `3523bd737bc85e25c7236406bc21cbc3` | safe | recheck |
| `66342d357386a976e5c3067a8f22c622` | safe | recheck |
| `ab4ae45e6798cf6663e784b539612d63` | safe | recheck |
| `a3fa314f1b5c82395f1ce858acb1c548` | safe | recheck |
| `58fcb7c11cefdc74f1f070590a9c1549` | vulnerable | recheck |
| `c0e7e28a869ecf0b4de7d1570d713130` | safe | recheck |
| `f3816c7f31f2caf098af24054d5f1f54` | safe | recheck |
| `c48faa84fa2f603b59c86b2c2633d140` | safe | recheck |
| `d0472725596eaaf5cee4c1297e452564` | safe | recheck |
| `191a4bbb1e7848b9f480088785d4137d` | safe | recheck |
| `06a7034210bfa65225423a65c3017221` | safe | recheck |
| `75b75e10317d4301ecf3263599ed50f3` | safe | recheck |
| `3faed74b7451d9275e4a150fb64b283f` | safe | recheck |
| `9a3e3279ec79778cd1bfe889d9c643bb` | safe | recheck |
| `e344c90e3eab7f81fbf080964232dedf` | safe | recheck |
| `14359151d51ec5ecb0d0e16f09cd803a` | safe | recheck |
| `b9b7e7444a2c3dadc74d9df7bb537eb0` | safe | recheck |
| `9d719ad507dee5cd886bab92df78708e` | vulnerable | recheck |
| `0b76042e30119fbcea516c3db14508c7` | vulnerable | recheck |
| `dd66b721572897dff677acfe3f78695b` | safe | recheck |
| `0bc4ede9391be778873a3988c315430e` | safe | recheck |
| `3b92873315a00fd275a285a7a3468df9` | safe | recheck |
| `933ee22ddbc2159738a42467fea16d3f` | safe | recheck |
| `b39bd54afd2febfea334bd63ea54a658` | safe | recheck |
| `20e5b7f4c2cde8a77a976ef12be00bd2` | safe | recheck |
| `39762ab894d372041a94535811e92e5a` | safe | recheck |
| `b2ee9eeec3cead4b87d445c0a19625e1` | vulnerable | recheck |
| `ffb1f46ab8758d34b3c5c67790a2c86c` | safe | recheck |
| `a027ef7ab9641b543238fea8c6a080fe` | safe | recheck |
| `e3c6806362823ebd941af338deccc3a1` | safe | recheck |
| `e16cd91f0097fc5d7feff17de6ea3a71` | vulnerable | recheck |
| `bfa254997deda142de5d73672d58a740` | safe | recheck |
| `c6b729adf5250644e09188d9ae3b2105` | safe | recheck |
| `6d1299a5555a96d250d77a184808d70d` | safe | recheck |
| `a98bb570ee86b2af649c4b92aa830f76` | safe | recheck |
| `603130f8dc4e794d973d8240c3145776` | vulnerable | recheck |
| `6e84df510b504d343418d0d638c924ca` | safe | recheck |
| `5610f531e236dd58a09793508805952d` | safe | recheck |
| `eb28d663dc95436c697da1df01c0dcd4` | safe | recheck |
| `8d849010be9687c39d87d29eb97e1a68` | safe | recheck |
| `750fe2dc8941db188b27dadb70302df6` | safe | recheck |
| `88a3ee7765166a6c70c9932d2816c9ba` | safe | recheck |
| `a48e33eebad28a74e0589d8d2802f80a` | safe | recheck |
| `f3a7d202cbc7085e147133bbf4c06f9f` | safe | recheck |
| `455ac5bc32bb865be3080302ee35b287` | safe | recheck |
| `d8be5976558bc8007c251f5517d8df8f` | safe | recheck |
| … | (103 more) | |

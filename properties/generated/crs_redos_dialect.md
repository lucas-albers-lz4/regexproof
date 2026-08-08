# CRS ReDoS + dialect triage

- @rx sites: 318
- encodable: 206
- ReDoS findings (uncapped): 234
- Noodler available: False (changed=False)

## Unencodable routing

| reason | count | route | note |
|---|---:|---|---|
| `ok` | 206 | prove | encodable — Z3 property / rule_diff / ReDoS |
| `pattern-too-long` | 73 | policy | Capacity cap (>256 chars), not a language limit. Policy: keep cap for interactive Z3 queries; triage long patterns to ReDoS-only / manual review. See TRAPS #21. |
| `word-boundary` | 34 | triage | Genuine stock-Z3 limit (gate-3 \b direction); ASCII domain declared for CRS. |
| `internal-anchor` | 2 | triage | unclassified reject — inspect |
| `negated-shorthand` | 2 | triage | unclassified reject — inspect |
| `inline-flag` | 1 | prove | Scoped (?i:...) encoded for PCRE/RE2; mid-pattern (?i), (?-i:...), scoped m/s/x, and ECMA remain rejects. |

## Pattern-too-long policy

Capacity cap (>256 chars), not a language limit. Policy: keep cap for interactive Z3 queries; triage long patterns to ReDoS-only / manual review. See TRAPS #21.

## ReDoS PASS/FAIL rows (sample)

| regex_id | result | tool |
|---|---|---|
| `fc213c69c51a78074b9db7a79c0a3cdf` | safe | recheck |
| `2937d3663e1c9621508e03be9d879b61` | safe | recheck |
| `12da5e9c854a440c3271a24da8a58565` | safe | recheck |
| `3c24ea1b0584bffeaa6dfd0731c8be89` | safe | recheck |
| `e10b86ff17417e765c4e4e2d6e246a9c` | vulnerable | recheck |
| `84f8757d3c0fa8cc2efa1bec274241da` | safe | recheck |
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
| `ad788aa56aebde4c7e8e3591c8badd34` | safe | recheck |
| `c2d5e3c4c7d40074c4c7e3d3d9db9ba6` | safe | recheck |
| `e387b56e7c498c0a90f657f70273c562` | safe | recheck |
| `19df3bc67b16333d43829e3c12235539` | safe | recheck |
| `b1f808b9357a9cbe8281cc14d593c595` | vulnerable | recheck |
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
| `a5a5071868f6b77eff6bebbc2ec5a19d` | safe | recheck |
| `dd9d5b9b8486e131a0b389af24ac8396` | safe | recheck |
| `9622e6e203d147bd2614eb8f8a3af8a5` | vulnerable | recheck |
| `a027ef7ab9641b543238fea8c6a080fe` | safe | recheck |
| `e3c6806362823ebd941af338deccc3a1` | safe | recheck |
| `e16cd91f0097fc5d7feff17de6ea3a71` | vulnerable | recheck |
| `bfa254997deda142de5d73672d58a740` | safe | recheck |
| `d6c34928fa032a4e8516705a47c1bd46` | safe | recheck |
| `cd4f301dbbb2e45d1ee07150bb9332d1` | vulnerable | recheck |
| `8da9fd11b5a381f092c535318a4e1df6` | vulnerable | recheck |
| `c6b729adf5250644e09188d9ae3b2105` | safe | recheck |
| … | (184 more) | |

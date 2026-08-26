# OpenWrt LuCI conversion wave 1 — close-out

Pin: `openwrt/luci` @ `77dad3f31405bc11f8384d742f7ad95314179694`.
Family: `OW-luci`. Product engine: Node `RegExp` (`helpers/ecma/match.mjs`).
Not in `WAVE_CORPORA`. Not mixed into `OW-packages`.
Asked: **4** human contracts (ledger `properties_asked` 17 → 21).

Rank: [`openwrt_luci_rank.json`](openwrt_luci_rank.json) (vocab keep-15).
Seed attention: `validation.js` `netdevname` (not-in-top; still asked).

## 15 read → 4 asked

| Site | Decision | Why |
|---|---|---|
| adblock `adb_repfilter` `:870` | **asked** shape 1 (no `;`) | tcpdump filter alphabet → device `tcpdump -f`. New alphabet. |
| validation `netdevname` `:1006` | **asked** shape 1 finder | `[^:/%\s]` **admits** `;` — SAT + Node GT. Config → UCI/netifd. |
| firewall mark `:335` | **asked** shape 1 (no `;`) | hex/decimal mark atom → fw4. New alphabet. |
| dockerman publish `:836` | **asked** shape 3 (colon-free UNSAT) | HostIp capture identity on colon-free hosts len 1..16. Node fuzz. |
| banip expiry `:1073` | skip | packages banip-expiry class. |
| banip feed URL `:1021` | skip | FQDN/URL host charset sibling of hostname deny-list. |
| adblock/banip expandFlags `(.*?)\s*(…/…)` | skip | status-chip display (`internal`). |
| filemanager UCI `'([^']+)'` | skip | packages Mosquitto UCI-quote class. |
| filemanager md `^[-*]\s+(.*)` | skip | markdown render (`internal`). |
| adguardhome `^/etc(/[^/]+)?/?$` | skip | path allowlist; no injection sink beyond config path. |
| dockerman size / volumes / IPv6 publish | skip | siblings of asked publish-host; volumes `[^/]+` pattern-class. |
| firewall DSCP `:301` / limit `:362` | skip | mark alphabet covers fw digit/hex; limit unit is JS-scoping, not regex. |
| validation hostname / IPv4 / MAC / IPv6 | skip | packages deny-list. |

## Results

- 3 expected-UNSAT (adblock filter, firewall mark, dockerman colon-free capture).
- 1 SAT counterexample_finder (netdevname admits `;`) — Node `match.mjs` GT.
- Mutation coverage: `OW-luci-mutated-adblock-filter-semicolon`.

netdevname SAT is **config** alphabet-admission (operator paste), not a WAN
CVE. Disclosure: **`wont_file`** (pattern admits the metachar by design of
`[^:/%\s]`; no public OpenWrt filing). No `conversion-upstream.jsonl` row.

Acceptance (PR C / CodeRabbit fold from #535): every SAT property has
`ground_truth=` via Node; harness runs with `--require-ground-truth`; every
property has `kind=` / `family=OW-luci`.

## Stop vs next slice

**Wave 1 idiom slice done.** Do not re-ask tcpdump-filter / netdevname
semicolon / firewall-mark digit / dockerman colon-free host capture.

**Stop this cluster (2026-08-26):** leftover keep-list is siblings (qosify
digit/hex = firewall mark; hostname/MAC = packages deny-list; DSCP already
skipped). Do **not** run LuCI wave 2. Do **not** start OpenWrt core (same
ash dialect as packages). Keep the wave-1 deny-list of what not to re-ask.

**Do not:** packages wave 4, Smith drain, `WAVE_CORPORA`, ucode `.uc`, public
filing without approval.

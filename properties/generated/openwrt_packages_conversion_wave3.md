# OpenWrt packages conversion wave 3 — close-out

Pin: `openwrt/packages` @ `e99adbc49f7a11d0377c8135fe706c7757b9e68c` (unchanged).
Family: `OW-packages`. Not in `WAVE_CORPORA`.
Asked: **4** new human contracts (ledger `properties_asked` 13 → 17).
Wave-1 rank JSON was **not** overwritten.

## 15 read → 4 asked

| Site | Decision | Why |
|---|---|---|
| Aliyun `RecordId=[^&]*` `:115` | **asked** shape 3 finder | Query-string capture (not JSON `[^"]*`). Config `param_enc` → API RecordId. SAT at `&`. |
| DNSPod `"RecordId":[[:space:]]*[0-9]*` `:312` | **asked** shape 1 (no `;`) | JSON **number** id → ModifyRecord. Digit alphabet ≠ Huawei `[a-z0-9]`. |
| Mosquitto `auth_opt_.*='(.*)'` `:101` | **asked** shape 3 (quote-free UNSAT) | UCI dump → mosquitto.conf. Greedy `.*` is identity on quote-free values. BusyBox fuzz. |
| pbr nftset `s|[/.^$*\[\\]|\\&|g` `:1143` | **asked** shape 4 as passthrough alphabet (no `.`) | grep-E escape **image**, not extras→`_`. Live dnsmasq `nftset=` callers. |
| Namesilo XML `<record_id>` / `<detail>` / `<code>` | skip | Default `fmt=json` uses jshn; XML sed is a no-xmllint fallback. |
| adblock `^(wildcard/\|domains/)` `:58` | skip | UCI housekeeping migrate, not a security deny. |
| Freedns XML `<fault>` / serial | skip | XML-RPC success/fail grep; display/control flow. |
| one_com `[^.]+\.[^.]+$` `:24` | skip | Config domain split; no injection sink. |
| route53 `s/^.* //` | skip | openssl dgst prefix strip (`internal`). |
| cnkuai HTML `value="` | skip | quote-delimited HTML — same class as `[^"]*`. |
| DNSPod `"Value"` / `"Code"` `[^"]*` | skip | Cloudflare class. |
| `[USERNAME]` URL templates | skip | placeholder replace. |
| adblock `${value}` | skip | interpolated. |
| banip `"rule_4"` / `input\|forwardwan` | skip | housekeeping literals. |
| IPv6 `^[0-9a-eA-E]` `:824` | skip | private-IP sibling of wave-2 `:823`. |
| GoDaddy `.+data":"(.*)","t.+` | skip | wave-2 skip stands. |
| hostname / IP / MAC / TransIP / wan_mark / extras→`_` | skip | prior waves. |

## Results

- 3 expected-UNSAT (DNSPod digits, Mosquitto quote-free capture, nftset passthrough).
- 1 SAT counterexample_finder (Aliyun `[^&]*`) — BusyBox ground-truth.
- Mutation coverage still the wave-1 hostname guard.

Aliyun SAT is config query-string truncation, not a CVE. Do **not** file publicly. No new `conversion-upstream.jsonl` row.

## Stop vs next slice

**This idiom slice is done.** Do not re-ask query-string `[^&]*`, DNSPod digits, UCI single-quote capture, or nftset grep-E extras.

**Next packages bucket** (same pin, same family): leftover WAN/config captures that are **not** JSON `[^"]*`, query-string `[^&]*`, XML-fallback, or UCI quotes — e.g. other provider id alphabets, shell-token captures in `ddns`/`banip`/`adblock` with a named sink after this deny-list.

**Next cluster** (when that bucket is empty or yield is flat): LuCI (`openwrt/luci` + `luci-app-*` `htdocs` JS) — own probe, ECMA GT, new family.

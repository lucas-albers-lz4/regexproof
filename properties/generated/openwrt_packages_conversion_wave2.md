# OpenWrt packages conversion wave 2 — close-out

Pin: `openwrt/packages` @ `e99adbc49f7a11d0377c8135fe706c7757b9e68c` (unchanged).
Family: `OW-packages`. Not in `WAVE_CORPORA`.
Asked: **5** new human contracts (wave 1 had 5; ledger `properties_asked` 8 → 13).
**Idioms in this slice are exhausted.** Next packages work is a **new idiom
bucket** (not another hostname/IP/`[^"]*` wave). LuCI JS is a different
cluster (own probe, ECMA GT).

## 5 asked (new idioms only)

| Site | Decision | Why it is a different idiom |
|---|---|---|
| pbr `str_extras_to_underscore` `:213` | **asked** shape 4 as image alphabet (no `;`) | Extras map to `_`; not another hostname charset-disjointness. Helper has **no callers** at this pin; asked as the mapping image / regression gate. |
| ddns `IPV4_REGEX` definition `:69` | **asked** shape 1 (no `;`) | Prove the **constant** ([`docs/DYNAMIC.md`](../../docs/DYNAMIC.md)), not interpolated `$IPV4_REGEX`. New alphabet `[0-9.]`. |
| ddns `expand_ipv6` `:([0-9a-f]{3}):` | **asked** shape 3 (hex nibble total) | WAN IPv6 compared after DDNS GET; 3-hex domain has no colon so capture is total. BusyBox sed fuzz. |
| Cloudflare `"content":\s*"[^"]*` `:245` | **asked** shape 3 finder | WAN JSON `[^"]*` extract (BusyBox grep). Same truncation class as TransIP; Cloudflare `content` is a DNS record, not a JWT. |
| Huawei `"id":"[a-z0-9]+"` `:94` | **asked** shape 1 (no `;`) | WAN JSON id interpolated into API paths. New alphabet `[a-z0-9]`. |

## Skip (one-line)

| Site | Why |
|---|---|
| pbr `is_hostname` / `is_host` / FQDN (`:354`, `:355`) | already asked wave 1 |
| banip expiry | already asked wave 1 |
| TransIP token | already asked wave 1; CU-011 `wont_file` |
| wan_mark hex | already asked wave 1 |
| pbr IPv4 / MAC / IPv6 (`:364`, `:373`, `:374`, `:3375`) | more alphabet disjointness |
| ddns private-IP grep `:823` | `unencodable:per-alternative-anchor`; a single `^10\.` rewrite is tautological. Proved the `$IPV4_REGEX` **definition** instead. |
| GoDaddy `.+data":"(.+)","t.+` | same JSON-value-capture class as Cloudflare `[^"]*` |
| https-dns-proxy ANSI `\\x1b\\[` | log coloring (wave 1 skip stands) |
| mwan3 `ip route` / `--comment` | `internal` (wave 1 skip stands) |
| `str_extras_to_space` | `tr`, not regex |
| `SHELL_ESCAPE` / `DNS_CHARSET` | definitions only, unused in the pin file |
| Porkbun `__DOMAIN_REGEX` | interpolated; config parse |

## Results

- 4 expected-UNSAT (sanitizer image, IPV4 alphabet, expand_ipv6 nibble, Huawei id).
- 1 SAT counterexample_finder (Cloudflare content truncation) — BusyBox ground-truth.
- Mutation coverage still the wave-1 hostname guard (same family).

Cloudflare SAT is the same sed/grep `[^"]*` pattern class as TransIP / usrmanage P3. Do **not** file publicly (`would_open_public_upstream_issue` stays false). No new `conversion-upstream.jsonl` row this wave.

## Stop vs next slice

**This idiom slice is done.** Wave 1 expand is consumed. Do not re-ask
hostname/FQDN/IPv4/MAC/IPv6 alphabets, TransIP/Cloudflare `[^"]*`, wan_mark
hex, or the internals already skipped.

**Next packages bucket** (same pin, same family, after this close-out):
other provider JSON/sed that is **not** `[^"]*` truncation, banip/adblock
ingest, leftover WAN/config captures with a named sink. Rank 15 in that
bucket only.

**Next cluster** (when packages idiom yield is flat): LuCI
(`openwrt/luci` + `luci-app-*` `htdocs` JS) — own trust map, `ecma` GT,
new family. Then `openwrt/openwrt` core. Not mixed into `OW-packages`.

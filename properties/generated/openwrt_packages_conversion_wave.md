# OpenWrt packages conversion wave 1 — close-out

Pin: `openwrt/packages` @ `e99adbc49f7a11d0377c8135fe706c7757b9e68c`.
Rank: `properties/generated/openwrt_packages_rank.json` (15 keep).
Asked: **5** human contracts (family `OW-packages`). **Stop** (no +5).
Next cluster: not started.

## 15 read → 5 asked

| Rank site | Decision | Why |
|---|---|---|
| pbr `is_hostname` / `is_host` charset | **asked** shape 1 (2 properties: no `;`, no space) | UCI dest/domain token; alphabet disjointness; sink is nft/dnsmasq set names |
| banip `ban_nftexpiry` | **asked** shape 1 | UCI config timeout alphabet; `;` would break nft `timeout` |
| TransIP JSON `token` sed capture | **asked** shape 3 finder | WAN HTTPS body; BusyBox `[^"]*` truncates at first quote |
| pbr `wan_mark` `0x(.*)` | **asked** shape 3 (hex-only UNSAT) | UCI config rewrite; hex domain has no quote so capture is total |
| mwan3 `ip route` `dev` / `table` captures | skip | `internal` (`ip route` / `ip rule` parse) |
| mwan3 `--comment` | skip | iptables status parse, internal |
| https-dns-proxy ANSI `\\x1b\\[` | skip | log coloring, no security sink |
| pbr sanitizer charset | skip as product shape 1 | mapping extras→`_` is shape-4 image; hostname alphabet already covers injection chars |
| pbr IPv4 / MAC validators | skip | more of the same alphabet-disjointness after 2 hostname + 1 expiry |
| ddns private-IP grep | dropped at rank | `unencodable:per-alternative-anchor` |

## Results

- 4 expected-UNSAT (3 shape 1 + 1 hex wan_mark) — alphabet / hex domain.
- 1 SAT counterexample_finder (TransIP token truncation) — BusyBox ground-truth.
- Mutation guard: hostname alphabet weakened with `;`.

## Stop vs expand

**Stop the cluster.** Logged yield is 5 asked (mix matches the SOP). Expanding would repeat hostname/IP validators. Expand only on a new SAT+GT or a wrong-type first 5; this wave is the right type (config + one WAN capture).

No public OpenWrt filing from this wave (`would_open_public_upstream_issue` stays false). TransIP truncation is a known JSON-sed class (usrmanage P3 analogue), not an OpenWrt-specific CVE without a human approval file.

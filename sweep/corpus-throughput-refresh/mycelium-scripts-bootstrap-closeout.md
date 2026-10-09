# Mycelium `scripts-bootstrap` reconnaissance close-out

**Source:** `mycelium0/mycelium` at
`4b53dc7629ca3bc88bf5467db481ad2af7130711`
**Disposition:** no defensible human contract; no conversion wave opened
**Evidence:** [`mycelium-inventory.ndjson`](../../properties/generated/mycelium-inventory.ndjson)
rows 101–112 and the pinned source paths cited below.

This review covers the 12 deferred `scripts-bootstrap` inventory rows from
`scripts/fungi` and `scripts/node-bootstrap.sh`. It is a bounded Gate-1
reconnaissance of the unused idiom named by the Mycelium wave-1 close-out,
not a product conversion wave. Seven fixed-pattern sites are mechanically
out of scope, two raw dynamic patterns are unencodable, and three capture or
alternation shapes were dropped after source review because they inspect
host-local status rather than a security boundary.

| Inventory row | Site and pattern | Disposition | Source context and sink |
|---:|---|---|---|
| 101 | `scripts/fungi:42` `^# fungi — the one-command` | Drop: literal self-documentation marker | `usage()` searches its own source for a help header and prints through `# Exit:`. Input is internal source text; sink is help output. Source: `scripts/fungi:38–44`. |
| 102 | `scripts/fungi:43` `^# \\{0,1\\}` | Drop: substitution with no capture or charset property | Strips the comment prefix from that help text. Input is internal; sink is help output. Source: `scripts/fungi:41–43`. |
| 103 | `scripts/fungi:77` <code>127\\.0\\.0\\.1&#124;\\[::1\\]</code> | Keep by mechanical syntax; drop after source review | Reads `$4` from local `ss -ltnH` output, filters loopback addresses, then prints a status listing. Host-local input; display sink; no policy decision or mutation. Source: `scripts/fungi:69–82`. |
| 104 | `scripts/fungi:84` `.*version[[:space:]]*` | Drop: substitution with no capture or charset property | Parses local `sing-box version` output for display. Source: `scripts/fungi:83–85`. |
| 105 | `scripts/fungi:85` `^Xray[[:space:]]*` | Drop: substitution with no capture or charset property | Parses local Xray version output for display. Source: `scripts/fungi:83–85`. |
| 106 | `scripts/fungi:101` `.*version[[:space:]]*` | Drop: substitution with no capture or charset property | Parses local Sing-box version output to compare against a local manifest pin and print drift status; it does not upgrade the engine. Source: `scripts/fungi:96–106`. |
| 107 | `scripts/node-bootstrap.sh:307` `^# \\{0,1\\}` | Drop: substitution with no capture or charset property | Strips comments from help extracted from the script itself. Internal input; help-output sink. Source: `scripts/node-bootstrap.sh:307`. |
| 108 | `scripts/node-bootstrap.sh:621` `sing-box` with `-i` | Drop: literal feature/status search | Filters `ss -tulpn` output to log Sing-box-owned sockets; a miss emits a warning. Host-local input; diagnostics sink. Source: `scripts/node-bootstrap.sh:612–623`. |
| 109 | `scripts/node-bootstrap.sh:1083` `.*[:.]([0-9]+)$` | Keep by mechanical syntax; drop after source review | Parses a numeric suffix from local `ss -tlnH` output. It feeds `verify_listen_ports`, a post-apply health check. Host-local input, not untrusted boundary data. Source: `scripts/node-bootstrap.sh:1025–1043, 1082–1084`. |
| 110 | `scripts/node-bootstrap.sh:1084` `.*[:.]([0-9]+)$` | Keep by mechanical syntax; drop after source review | Same parser over local `ss -ulnH` output and same availability-check sink. Source: `scripts/node-bootstrap.sh:1025–1043, 1082–1084`. |
| 111 | `scripts/node-bootstrap.sh:1087` `$p` | Drop mechanically: raw dynamic pattern is unencodable | `$p` comes from `listen_port` values read from live config and is used in `grep -qx` for the TCP bound-port check. A miss feeds `verify_post_apply`. Source: `scripts/node-bootstrap.sh:1073–1087, 1025–1043`. |
| 112 | `scripts/node-bootstrap.sh:1091` `$p` | Drop mechanically: raw dynamic pattern is unencodable | Same config-derived value and check for UDP ports. Source: `scripts/node-bootstrap.sh:1078–1091, 1025–1043`. |

## Why the config-derived pair is not a contract

The hypothetical guarantee would be that a config-derived expected port
cannot broaden the grep pattern and falsely satisfy the post-apply bound-port
check. Its trust class would be operator configuration and its sink the
health-check failure/rollback path. That domain is not proven by the reviewed
source: `control/vocab.json:32–41` allowlists per-protocol port keys, but
`control/lib/nb_render_params.sh:145–166` copies allowlisted override values
without validating their value domain. Rendering uses `--argjson` for ports
(`control/lib/render_singbox.sh:274–292`), and the flow calls external
`sing-box check` (`control/lib/nb_update_apply.sh:387–395`); neither establishes
the numeric-only input domain needed to admit `$p` as a membership contract.
Do not count this as a vulnerability or product property without separate
domain evidence and a supported encoding route.

## Close-out

- Reviewed all 12 inventory rows; the counts are 7 mechanical drops, 3
  source-context drops, and 2 unencodable dynamic drops.
- No property was human-adopted or registered; no conversion row or product
  count is added.
- No active-review minutes are claimed. This reconnaissance did not open a
  conversion wave, which requires human site review and per-site timing.
- The `scripts-bootstrap` idiom remains deferred. The previous
  `control-failclosed` slice stays closed. This cluster may be considered
  closed for this package, so the next candidate cluster can be processed.

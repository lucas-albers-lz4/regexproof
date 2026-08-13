# mole — OT-protocol rule_diff vs admitted corpora

**Date:** 2026-08-13 · **Follow-on** from [#323](https://github.com/lucas-albers-lz4/regexproof/issues/323)
(README flagged: "Worth a follow-on rule_diff vs ICS-focused packs").

## Question

mole was admitted as `go` on the strength of its **novel OT-protocol NIDS
rules** (modbus/Siemens-S7/OPC-UA — industrial protocols absent from every
admitted yara pack). This diff verifies the novelty claim against the full
admitted inventory set: does ANY other corpus cover the same protocol
surface, at the rule level or the regex-literal level?

## Mole's OT surface (at pin `eb5356d5`)

13 protocol rule files, **235 rules**:

| File | Rules | Surface |
|---|---|---|
| modbus.yar | 19 | 41 hex + 1 regex (`\x02\x04\x05…` FC-byte class) |
| FINS.yar | 37 | 74 hex (Omron) |
| SLMP.yar | 38 | 38 hex (Mitsubishi) |
| MCCONNECT.yar | 46 | 46 hex (Mitsubishi MC) |
| Siemens-S7.yar | 13 | 17 hex (Set_Clock/Set_Password/Write_Var…) |
| DNP3.yar | 10 | 8 hex + 3 regex |
| OPC-DA.yar | 3 | 3 hex |
| OPC-UA.yar | 8 | 13 hex + 2 regex + 12 str |
| EIP.yar | 7 | 14 hex (EtherNet/IP) |
| ICS-Attacks.yar | 40 | 50 hex (yokogawa/wonderware/realwin exploits) |
| mqtt.yar | 5 | 9 hex |
| mtconnect.yar | 8 | 48 str (MTConnect XML) |
| demo.yar | 1 | sample |

The encodable regex surface is **6 literals**: FC-byte alternations
(`(\x02|\x04|\x05…`) for modbus/DNP3/OPC-UA function codes, private-IP
ranges (`10.`, `172.16-31.`, `192.168.`), and an IPv4-shape pattern. The
bulk of the OT signal lives in hex-byte protocol signatures (not regex).

## Rule-level diff: no other pack has OT detection rules

Scanned every admitted corpus inventory (53 corpora with committed
`-inventory.ndjson`) for protocol keyword classes
(modbus|s7comm|s7|opc|dnp3|slmp|mtconnect|fins|ethernet.ip|cip|mcconnect|iec104):

- **yara_rules, PEpper, sec_check, Antivirus, volatility3-mcp**: the only
  keyword hits are `CRC16_MODBUS` (a **string-literal name** inside a
  non-OT rule) and `iec104\.log` (a **file-matching pattern**, not a
  protocol signature). Zero OT detection rules.
- **SMAT**: 1 `dnp3` keyword hit — same class (name/substring), no DNP3
  rule.
- **All other 46 corpora**: zero keyword hits.

## Regex-literal diff: zero exact overlap

Exact-string comparison of mole's 6 regex literals against every admitted
inventory's pattern set: **0 exact matches in any corpus other than mole
itself.** No corpus shares a modbus FC-byte class, S7 function code, or
private-IP OT-whitelist literal with mole.

## Conclusion

**The novelty claim holds.** mole is the only admitted corpus with
OT-protocol detection rules; its regex literals are unique across the whole
admitted inventory set. The measured 0.9853 fraction (67/68) is therefore
novel encodable surface, not a re-measurement of an existing pack. The
protocol signatures are predominantly hex-byte (the `yara` extractor's
regex path only sees the 6 literals above), which is also why the corpus is
small in pattern count but high in value: the OT-rule family is
disjoint from the 21-bucket reject taxonomy's existing yara coverage
(fullword-boundary noise from big vendor packs is absent — hand-written
NIDS rules).

## Reproduce

```bash
git clone --filter=blob:none https://github.com/mole-ids/mole.git /tmp/mole-check
git -C /tmp/mole-check fetch --depth 1 origin eb5356d56e914552d6b1c8dc822f19bd6f0e5774
git -C /tmp/mole-check checkout eb5356d56e914552d6b1c8dc822f19bd6f0e5774
# keyword scan: regex over every properties/generated/*-inventory.ndjson pattern field
# literal diff: exact-set intersection of mole regex literals vs each inventory's patterns
```

# Phase 5 handoff pilot (P5/P7, #221 — mirror-route, U9-amended)

## D14 differential fuzz (real JS vs mirror, regression evidence)

| pattern | corpus | probes | in-domain divergences | boundary divergences |
|---|---|---|---|---|
| NON_FIREWALL_PREFIX | 937 | 950 | 0 | 1 |
| FIREWALL_HINT | 937 | 950 | 0 | 2 |
| ACTION_RE | 937 | 950 | 0 | 1 |
| DENY_ACTION | 937 | 950 | 0 | 1 |
| TCP_FLAG_TAIL | 937 | 950 | 0 | 2 |
| NETFILTER_KV_GLUE | 937 | 950 | 0 | 0 |

- total in-domain divergences: 0 (each would be a triage record; zero is the pass criterion)
- boundary divergences: 7 — the documented ASCII-domain edge (NBSP/U+2028 \s gap, measured Phase 1)

## fwlive handoff (P7) — mirror properties through the harness

| property | pattern | probe | expect | route | result | tier | destination |
|---|---|---|---|---|---|---|---|
| fwlive-NON_FIREWALL_PREFIX-accept | NON_FIREWALL_PREFIX | "dnsmasq" | accept | mirror | sat (ok=True) | seq-only | classify step 1: prefix gate (accept) → #120 |
| fwlive-NON_FIREWALL_PREFIX-reject | NON_FIREWALL_PREFIX | "xdnsmasq" | reject | mirror | unsat (ok=True) | seq-only | classify step 1: prefix gate (reject) → #120 |
| fwlive-FIREWALL_HINT-accept | FIREWALL_HINT | " kernel " | accept | mirror | sat (ok=True) | seq-only | classify step 2: hint gate (accept) → #120 |
| fwlive-FIREWALL_HINT-reject | FIREWALL_HINT | "xkernel" | reject | mirror | unsat (ok=True) | seq-only | classify step 2: hint gate (reject) → #120 |
| fwlive-ACTION_RE-accept | ACTION_RE | " ACCEPT " | accept | mirror | sat (ok=True) | seq-only | classify step 3: action gate (accept) → #120 |
| fwlive-ACTION_RE-reject | ACTION_RE | "xACCEPT" | reject | mirror | unsat (ok=True) | seq-only | classify step 3: action gate (reject) → #120 |
| fwlive-DENY_ACTION-accept | DENY_ACTION | " DROP " | accept | mirror | sat (ok=True) | seq-only | classify step 4: deny gate (accept) → #120 |
| fwlive-DENY_ACTION-reject | DENY_ACTION | "dropping" | reject | mirror | unsat (ok=True) | seq-only | classify step 4: deny gate (reject) → #120 |
| fwlive-TCP_FLAG_TAIL-accept | TCP_FLAG_TAIL | "SYN ACK FIN" | accept | mirror | sat (ok=True) | seq-only | classify step 5: tcp-flag tail (accept) → #120 |
| fwlive-TCP_FLAG_TAIL-reject | TCP_FLAG_TAIL | "xSYNxACK" | reject | mirror | unsat (ok=True) | seq-only | classify step 5: tcp-flag tail (reject) → #120 |
| fwlive-NETFILTER_KV_GLUE-accept | NETFILTER_KV_GLUE | "eth0IN=" | accept | mirror | sat (ok=True) | seq-only | classify step 6: kv glue (accept) → #120 |
| fwlive-NETFILTER_KV_GLUE-reject | NETFILTER_KV_GLUE | "eth0 IN=" | reject | mirror | unsat (ok=True) | seq-only | classify step 6: kv glue (reject) → #120 |

## U9 reopen trigger evaluation

- fwlive pattern inventory: 6 patterns, unchanged (no new pattern lacking a standard-encoding mirror)
- reopen trigger: NOT hit — the DROP decision stands

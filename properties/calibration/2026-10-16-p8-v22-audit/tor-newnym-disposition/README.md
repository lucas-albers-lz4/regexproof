# Tor NEWNYM response handling: local defect confirmed

**Repository pin:** `Leviticus-Triage/llm-honeypot-intelligence@65624396e263074bb8cb2e049f9a9ec6215ea5c1`
**Question:** `LH-llm-honeypot-tor-newnym-response-sequencing`
**Disposition:** local functional defect confirmed; deployed security impact not confirmed.

## Evidence

The exact-pinned `rotate-tor.sh` sends `AUTHENTICATE`, `SIGNAL NEWNYM`, and
`QUIT`, then runs `grep -q "250 OK"` over the combined ControlPort response.
The repo describes NEWNYM as required every 30–60 seconds and says the gateway
must stop if its rotator fails. The script branches on `send_newnym`'s exit
status: success logs “SIGNAL NEWNYM ok” and continues; failure exits.

The pinned helper's isolated response fixture is:

```text
250 OK
551 Internal error
250 closing connection
```

The exact helper returns success because the first authentication reply
matches, even though the later NEWNYM command failed. The existing local gate
also checks the failure-only control transcript and the success transcript;
the sequence result, replay, and gate artifacts are linked below. No live Tor
service, network request, scan, or project data was used.

The official Tor Control Protocol defines 5yz replies as unsuccessful; 551
means an internal error prevented fulfillment of the request. For `SIGNAL
NEWNYM`, the protocol describes switching to clean circuits for new requests
and says successful recognized signals receive 250. See the [Tor command
specification](https://spec.torproject.org/control-spec/commands.html) and
[reply-code specification](https://spec.torproject.org/control-spec/replies.html).

That evidence confirms a local false-success defect under a valid error
transcript. It does **not** establish that a real Tor instance produced this
transcript in deployment, that any scan continued on an old exit, or that
security/privacy impact occurred. Keep the security impact unconfirmed and the
third-party outcome counters at zero.

## Reproduction artifacts

- P2 source review: [review README](../../2026-10-15-p2-llm-honeypot-source-review/README.md)
- Original response fixtures: [product replay](../../2026-10-15-p2-llm-honeypot-source-review/product-replay.json)
- P6 replay: [P6 product replay](../../2026-10-15-p2-llm-honeypot-source-review/product-replay-p6.json)
- Local gate configuration: [gate config](../../2026-10-15-p2-llm-honeypot-source-review/gate.json)
- Machine-readable disposition: [disposition.json](disposition.json)

**External status:** private-first; no report was sent, and no maintainer was
contacted.

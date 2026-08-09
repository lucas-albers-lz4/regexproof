# DOMPurify triage (Wave 3 P4 / #115)

Decision: **go** (admission: security-boundary; fraction=0.5625)

Pin: `7392211bda80f9c1038db32fc090119685bfe425` — 16 sites (plan ~146 corrected).

## Buckets

- `a_encodable`: 9
- `b_dialect_gap`: 7

## Reasons

- `ok`: 9
- `stateful`: 6 (`g` flag on markup probes / template / whitespace)
- `per-alternative-anchor`: 1 (`IS_ALLOWED_URI`)

## Ecma rejects named

- `stateful` (`g` / `y`) — existing reject path
- `per-alternative-anchor` — `IS_ALLOWED_URI` multi-alternative `^…|…$` shape
- Lookarounds / `\p{}` / `u`/`v` flags: **none** at this pin

## Security note

`IS_ALLOWED_URI` / `IS_SCRIPT_OR_DATA` are sanitizer-boundary patterns.
Bypass-capable findings escalate to security severity (`SECURITY_TOOL_CORPORA`).
`IS_ALLOWED_URI` itself is currently unencodable (`per-alternative-anchor`).

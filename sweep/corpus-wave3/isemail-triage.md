# isemail triage (Wave 3 P4 / #115)

Admission: **no-go** (0/3 conditions; scale corrected 121→5).
Fraction: **go** (0.8000). See `ecma-frontier-nogo.md` + umbrella #111.

Pin: `8789d509d69f098350783fb2d8d2bf05f036b448`.

## Buckets

- `a_encodable`: 4
- `b_dialect_gap`: 1

## Reasons

- `ok`: 4 (nonASCII, ipV4, ipV6, ASCII domain-length)
- `backref`: 1 (`/[^\0]+/` NUL-normalize path — `\0` rejected as backref)

## Ecma rejects named

- `backref` — `\0` in character class / escape path
- Lookarounds / `\p{}` / `u`/`v` / `y`: **none** at this pin

Not a security tool — not in `SECURITY_TOOL_CORPORA`.

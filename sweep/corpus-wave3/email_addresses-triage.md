# email-addresses triage (Wave 3 P4 / #115)

Admission: **no-go** (0/3 conditions; scale corrected 71→4).
Fraction: **go** (0.5000). See `ecma-frontier-nogo.md` + umbrella #111.

Pin: `8e6be27770b7be223c2de035d7e52849f938c959`.

## Buckets

- `a_encodable`: 2
- `b_dialect_gap`: 2

## Reasons

- `ok`: 2 (`^\s*`, `\s*$`)
- `stateful`: 2 (`/g` whitespace collapse / strip)

## Ecma rejects named

- `stateful` (`g` flag) — existing reject path
- Lookarounds / `\p{}` / `u`/`v` / `y`: **none** at this pin

Not a security tool — not in `SECURITY_TOOL_CORPORA`. Parser is
hand-written RFC5322; regexes are whitespace normalizers only.

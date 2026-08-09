# YARA modifier-semantics spike (Corpus Wave 2 / P1)

Pinned CLI: **yara 4.5.8** (`brew install yara`; also `yarac` for compile checks).
Helper: `helpers/yara/match.py` (temp-file replay; never stdin).

## Probe inventory (YARA-Rules/rules, prior board probe)

| Modifier combo | Count (probe) | Lowering decision |
|---|---:|---|
| (plain / default ascii) | 196 | domain=`ascii`; single-byte mirror |
| `wide ascii` | 104 | **domain union**: emit per-variant records (ascii + wide) or real union mirror |
| `nocase wide ascii` | 16 | `nocase` → case-insensitive flag; domains as above |
| `wide` | 14 | domain=`wide` only (UTF-16LE); mirror embeds `\x00` between code units |
| `nocase` | 9 | case flag; domain=`ascii` |
| `fullword wide ascii` | 5 | fullword ≠ `\b` (see below); per encoding variant |
| oddities (`scomma`, …) | enumerate at P2 extract | **reject** unknown modifier combinations (never silent pass) |

## NUL / wide mirrors (Z3 5.0.x)

Verified: `z3.Re("a\x00b\x00c\x00")` + `InRe(StringVal(latin1), mirror)` agrees with
`yara` `wide` on UTF-16LE probes and rejects ASCII `abc`.

Deliberately-wrong wide mirror `z3.Re("abc")` accepts ASCII `abc` while real
`wide` does not — caught by `scripts/mirror-fidelity-gate.py`
(`wrong_wide_caught=true`).

## fullword ≠ `\\b`

YARA `fullword` boundaries are **alnum-only** and applied **per encoding
variant** (not over the ascii∪wide union). ASCII `\w` includes `_`, so
`x_abc` can match a `\babc\b` mirror but not YARA fullword `abc`.

**Decision for P2:** lower `fullword` to alnum token guards (`_token` /
`token_` style), never `_lower_word_bounded` / `\b`.

## Domain in regex_id

`ascii` vs `wide` variants of one pattern must not collide — P2 adds domain as
the 7th `regex_id` component (`EXTRACTOR_SCHEMA_VERSION` → 2).

## Fixture replay

`sweep/corpus-wave2/fixtures/yara.json` + gate surface `yara` (fail-closed).

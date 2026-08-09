# Cross-engine rule_diff — Coraza (go-re2) ↔ ModSecurity (pcre)

Wave-2 Phase 5 family contract (issue #100).

## Provenance

| Side | Engine | Dialect | Role |
|---|---|---|---|
| R1 | go-re2 helper | `re2` | Coraza WAF semantics |
| R2 | pcre2 helper | `pcre` | ModSecurity / CRS native |

Same CRS rule text at pin `55b09f5` (v4.28.0). Preflight fails closed on
missing rules root, wrong HEAD, or incomplete `REQUEST-*.conf` /
`RESPONSE-*.conf` manifest.

## Result classes

| Class | Meaning |
|---|---|
| `gap` | Both encodable; shape-5 SAT (pcre accepts a string re2 rejects in bound) |
| `no-gap` | Both encodable; shape-5 UNSAT in declared length bound |
| `non-comparable-re2` | go-re2 rejects at parse; pcre encodable |
| `non-comparable-both` | Both reject at parse (counted, not a finding) |

## Ground truth

Gap witnesses require **per-engine** evidence:

```json
{
  "status": "PASS",
  "pcre2": {"status": "PASS", "version": "...", "cmd": [...], "matched": true},
  "go_re2": {"status": "PASS", "version": "...", "cmd": [...], "matched": false}
}
```

`--require-ground-truth` rejects gaps lacking both engine objects.

## Mutation guards

Family `crs-cross-engine` (also registered in `z3-verify.py --all`):

- `crs-cross-engine-control` — identical mirrors → UNSAT
- `crs-cross-engine-widen-R1` — impossible R1 → SAT

## Disclosure

Verified gaps → `tag_disclosure(findings, corpus="coreruleset")` →
`private_first`.

## Run

```bash
python scripts/cross-engine-rule-diff-pilot.py --require-ground-truth
```

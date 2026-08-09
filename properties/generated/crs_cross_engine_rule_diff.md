# CRS cross-engine rule_diff (Coraza↔ModSecurity)

- pin: `55b09f5acfd16413e7b31041100711ceb7adc89c`
- classified: 80
- class_counts: `{"comparable": 58, "gap": 5, "no-gap": 3, "non-comparable-both": 22, "non-comparable-re2": 0}`
- solved pairs: 8
- gaps/findings: 5 (disclosure=private_first)
- mutation_guard_ok: True

## Family contract

```json
{
  "R1": "go-re2 (Coraza engine semantics)",
  "R2": "pcre2 (ModSecurity / CRS native)",
  "provenance": "same CRS rule text @ 55b09f5",
  "dialect_parity": "fullmatch mirrors; site call_kind=search",
  "ground_truth": "per-engine pcre2 + go_re2 replay",
  "mutation_guards": [
    "control",
    "widen-R1"
  ]
}
```


# Malcontent threat-hunting description to Markdown calibration, 20-r2

This one-question slice binds to
`chainguard-dev/malcontent@ea3e83e24676a1678a9522141da29b636c9451ab` and the
frozen `2026-09-12-calibration-20-r2` cohort. It covers the separately
reviewed `pkg/report/report.go:118:threatHuntingKeywordRe` path. Malcontent's
full 15-row source review is recorded in the adjacent
[P2 source-review artifact](../2026-10-15-p2-malcontent-source-review/README.md).

## Contract and replay

The adopted contract limits its question to a concrete one-line ASCII YARA
description value:

```text
Detection patterns for the tool 'Benign' | [click](https://attacker.invalid)' taken from the ThreatHunting-Keywords github project
```

At the exact source pin, YARA-X 1.19.0 compiles a valid rule containing that
description, matches the replay sentinel, and sends the metadata through
`report.Generate` and the real Markdown renderer. `mungeDescription` produces
`references 'Benign' | [click](https://attacker.invalid)' tool`; the report
contains that raw HTTPS link and pipe in the Markdown table. The pipe separates
another table cell in the emitted source. See
[`product-replay.json`](product-replay.json).

The frozen one-question roster predates solver execution. The regression gate
reproduces the product output, checks the counterexample and delimiter
mutation guard, and compares the Z3 regex mirror with Go RE2 over 33,209
inputs with zero mismatches. [`gate.json`](gate.json) binds the same gate to
the P6 runner, which writes its resumable attempt and checkpoint under
[`p6-wave/`](p6-wave/).

## Limits and accounting

This is a concrete product-output counterexample, not a proof over every YARA
description. It confirms raw Markdown structure only; no browser or downstream
Markdown viewer was run. Consumer impact remains `pending_product_triage`.
No external report was sent, no maintainer confirmed impact, and no fix or
consumer-adopted gate is recorded. The input comes from operator-enabled
third-party rule metadata and is classified as config.

Replaying the C API path requires the pinned Go binding and native
`yara_x_capi` 1.19.0 discoverable through `pkg-config`; the native build used
for this calibration remains in `/tmp`, not in the repository.

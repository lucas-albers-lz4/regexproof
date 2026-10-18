# Malcontent author metadata to Markdown calibration, 20-r2

This one-question slice binds to
`chainguard-dev/malcontent@ea3e83e24676a1678a9522141da29b636c9451ab` and the
frozen `2026-09-12-calibration-20-r2` cohort. The P2 source review covered all
15 Go-regex inventory rows at this pin: 11 skips, 3 unresolved candidates, 1
adopted contract, and 1 asked product question. That is complete review for
this repository only, not complete P2 coverage.

## Contract and replay

The adopted contract binds
`pkg/report/report.go:117:authorWithURLRe` to the Markdown author-link sink
in `pkg/render/markdown.go`. The witness is valid one-line ASCII YARA author
metadata:

```text
Name (https://example.invalid/)[click](https://attacker.invalid)
```

At the exact source pin, YARA-X 1.19.0 compiles a valid rule containing this
metadata, matches the replay sentinel, and passes the match through
`report.Generate` and Malcontent's Markdown renderer. The report stores the
captured URL as
`https://example.invalid/)[click](https://attacker.invalid` and emits:

```markdown
by [Name](https://example.invalid/)[click](https://attacker.invalid)
```

The standalone [`product-replay.json`](product-replay.json) records the exact
product output and source digests. The
[`gate-report.json`](gate-report.json) also records the counterexample, a
passing weakened-capture mutation guard, and zero mismatches across 2,034
Go-RE2 versus Z3 differential cases. The frozen one-question roster predates
the solver outcome.

The P6 runner uses [`gate.json`](gate.json) and writes resumable state under
[`p6-wave/`](p6-wave/). Because the proof outcome is SAT, its terminal wave
state requires downstream triage; a passing local reproducer is not a
confirmation that a particular Markdown consumer acted on the extra link.

## Limits and accounting

This establishes that the pinned product emits the second HTTPS Markdown link
for one reachable metadata value. It does not execute a browser or identify a
consumer that follows the link. Downstream impact remains
`pending_product_triage`; no external report was sent, no maintainer confirmed
impact, and no third-party fix or consumer-adopted gate is recorded. The input
is operator-enabled third-party YARA metadata, so the trust class is config.

The product replay needs the pinned Go binding and native `yara_x_capi`
1.19.0 discoverable through `pkg-config`. The calibration build used:

```sh
PKG_CONFIG_PATH=/tmp/yara-x-capi-pkgconfig \
LD_LIBRARY_PATH=/tmp/yara-x-capi-1.19.0-target/release \
.venv/bin/python scripts/malcontent-author-markdown-regression-gate.py \
  --output properties/calibration/2026-10-15-autonomous-malcontent-author-markdown-20r2/gate-report.json
```

The C API build is an environment prerequisite, not a checked-in binary.

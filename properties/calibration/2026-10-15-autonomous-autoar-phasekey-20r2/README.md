# AutoAR phase-log filename component calibration

This is a one-question exact-pin P6 calibration for the caller-controlled
`module` query used by `GET /api/scans/:id/logs`. The adopted contract is
limited to the module-derived filename component under `phase-logs`; it does
not cover `scanID`, the configured results root, symlinks, or collisions
between distinct sanitized module names.

## Evidence

- Source: AutoAR pin `01cd447ad3b1acfed7e0680596c2c74458a4cf06`,
  `internal/utils/phase_logs.go:206`, SHA-256
  `3dec250b5802efadac77c6ba9cf9ce19f5fec09a8111674ab13a56d35e601ddc`.
- Contract adoption used `autonomous-contracts-v1` and the standing user
  delegation. The roster was frozen before the formal solver question.
- The Shape-1 query is UNSAT: every one-character ASCII token `.`, `/`, and
  `\` is matched by the pinned Go RE2 replacement class.
- The SAT mutation guard allows `.` and `/`; its `.` witness replays against
  the exact helper and makes `../../outside.jsonl` resolve outside
  `phase-logs`.
- The pinned helper gate checked 662 inputs with zero mismatches under Go
  1.25.7: all 128 ASCII code points, 22 path/normalization seeds, and 512
  deterministic mixed strings including Unicode and controls.
- Final P6 state is `complete`: one UNSAT question, one passing mutation
  guard, and one local product gate.

The run preserved two failed terminal gate attempts. The first exposed a
replay assertion that compared the sanitized component with its `.jsonl`
suffix; after correcting it, a second resume exposed a roster validator using
the wrong manifest field. The final resume passed both mutation replay and the
local gate without retrying the already decided solver question. The state and
checkpoint retain all three attempts:
[`p6-wave-r1/`](p6-wave-r1/).

The 38-second work-log interval covers the initial P6 execution and both
gate-only resumes. Review and contract adoption happened before that interval,
so that timed row correctly records zero reviewed sites and zero adoptions.
The separate source review covers all 34 AutoAR Go regexp sites. This run
found no product violation, confirmed impact, consumer adoption, external
report, maintainer confirmation, or fix.

## Artifacts

- `contract.json`, `contracts.json`, `roster.json`, and `work-items.json` bind
  the adopted question and source identity.
- `gate-report.json` records exact source hashes, Go version, 662 cases, and
  the real weakened-source traversal result.
- `p6-wave-r1/checkpoint.json` is the final one-question P6 checkpoint; its
  first two failed gate states remain visible in `state.json`.
- `properties/generated/autonomous_work.jsonl` records the 38-second interval
  as `autoar-phase-key-20r2-p6-r1`.

Run the exact local product gate with:

```sh
.venv/bin/python scripts/autoar-phase-key-regression-gate.py \
  --product-only \
  --source-root /tmp/regexproof-pinned-sources/AutoAR-01cd447ad3b1acfed7e0680596c2c74458a4cf06 \
  --output properties/calibration/2026-10-15-autonomous-autoar-phasekey-20r2/gate-report.json
```

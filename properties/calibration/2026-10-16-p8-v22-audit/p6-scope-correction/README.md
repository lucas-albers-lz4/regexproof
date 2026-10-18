# P6 runner scope correction

This bundle contains a corrected three-question source-bound roster for the Aidevops webhook receiver: secret-name, SHA-token, and PR-token regex invariants. The roster binds to the 20-r2 cohort and the two revised regex-only contract digests.

The exact-pin standalone gate passes, but the bounded P6 runner refused the roster before solving because those question IDs have no entry in `scripts/emit-conversion-ndjson.py:SHAPE`. It created no state directory, started no solver questions, and did not run the product gate. The preflight failure is preserved in [JSON](preflight-failure.json). It is not counted as a proof attempt or a passing P6 wave.

This exposed a real P6 integration limit: the standalone proof/gate family existed, but the canonical emitter and resumable runner could not yet represent it. The frozen failure remains a valid record of that preflight. Shape 6 now covers source-language inclusion in an independent contract language over the full regular-language domain; the canonical emitter registers the three questions under this shape. They remain `kind=property` invariants, while shape-5 `rule_diff` stays reserved for bounded rule comparisons. The follow-on [shape-6 P6 wave](../p6-shape6-r1/README.md) completed after a second dry-run caught and corrected the numeric Bash source-column check. No solver or product-engine subprocess was started by the original failed preflight.

Inputs:

- [Corrected contracts and runner identity rows](contracts.json)
- [Frozen three-question roster](roster.json)
- [Exact-gate configuration](gate-config.json)
- [Preflight failure record](preflight-failure.json)

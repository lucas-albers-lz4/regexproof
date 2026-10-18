# BinaryAlert exact-pin P2 source review

This is a complete raw-regex review for one frozen cohort member. It does not
cover the other 19 repositories or close P2.

## Scope and result

- Repository: `airbnb/binaryalert`
- Pin: `a9c0f06affc35e1f8e45bb77f835b92350c68a0b`
- Extracted Python regex sites reviewed: **1**
- Evidence-backed skips: **1**
- Unresolved: **0**
- Adopted contracts / product questions: **0**

The Sphinx build configuration searches the repository-owned
`cli/__init__.py` for its literal `__version__` assignment and assigns the
capture to the documentation's release/version fields. The matched source is
build metadata; it does not process untrusted runtime input or enforce a
security boundary. The exact-pin review records the full source context in
[`evidence.json`](evidence.json) and the decision in [`reviews.json`](reviews.json).

## Reproduction

```sh
.venv/bin/python scripts/build-p2-source-review-evidence.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-15-p2-source-inventory-v2/inventory.json \
  --sites properties/calibration/2026-10-15-p2-source-inventory-v2/sites.ndjson \
  --reviews properties/calibration/2026-10-15-p2-binaryalert-source-review/reviews.json \
  --checkout /tmp/regexproof-pinned-sources/binaryalert-a9c0f06affc35e1f8e45bb77f835b92350c68a0b \
  --repo-id airbnb/binaryalert \
  --pin a9c0f06affc35e1f8e45bb77f835b92350c68a0b \
  --output properties/calibration/2026-10-15-p2-binaryalert-source-review/evidence.json
```

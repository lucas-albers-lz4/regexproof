# P2 Malcontent exact-pin source review

[`reviews.json`](reviews.json) records a second pass over all 15 Go-regex
inventory rows at the frozen Malcontent 20-r2 pin. The generated
[`evidence.json`](evidence.json) binds each review decision to the raw P2
inventory, source-file hashes, Git blob IDs, and cited source windows.

| Decision | Count | Meaning |
|---|---:|---|
| Skip | 11 | Inspected sites with no supported regex-specific product guarantee |
| Unresolved | 2 | Rule-removal/detection integrity and report-path privacy remain open |
| Adopted | 2 | Source-bound author-link and description-to-Markdown contracts |
| Product questions asked | 2 | Both adopted counterexample-finding questions were run |

Both asked questions reproduced metadata-derived HTTPS link syntax in exact
Malcontent Markdown output. The description witness also emitted an unescaped
table delimiter. Downstream consumer impact remains pending for both. The two
unresolved candidates are not silently counted as questions. This is one
repository's raw-site coverage and does not close P2: the other frozen cohort
members still need independently reviewed coverage, and Everclaw's missing
submodule mapping remains incomplete.

Regenerate the evidence with
[`build-p2-source-review-evidence.py`](../../../scripts/build-p2-source-review-evidence.py)
and the original cohort inventory:

```sh
.venv/bin/python scripts/build-p2-source-review-evidence.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-15-p2-source-inventory/inventory.json \
  --sites properties/calibration/2026-10-15-p2-source-inventory/sites.ndjson \
  --reviews properties/calibration/2026-10-15-p2-malcontent-source-review/reviews.json \
  --checkout /tmp/regexproof-pinned-sources/malcontent-ea3e83e24676a1678a9522141da29b636c9451ab \
  --repo-id chainguard-dev/malcontent \
  --pin ea3e83e24676a1678a9522141da29b636c9451ab \
  --output properties/calibration/2026-10-15-p2-malcontent-source-review/evidence.json
```

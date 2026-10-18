# Anax exact-pin source review

This second-pass review covers all 26 literal Go regexp sites in the frozen
20-r2 Anax member at `2f3fa5a506d6565fa68858b7963450567ddda114`. The original
source-window evidence is preserved in [`evidence.json`](evidence.json); the
updated decisions and re-bound source windows are in
[`evidence-after-transport.json`](evidence-after-transport.json).

| Decision | Count | Meaning |
|---|---:|---|
| Skip | 15 | Local configuration/system parsers, compatibility formatting, and two CR/LF checks unreachable through the pinned HTTP parser |
| Unresolved | 10 | Dependency filename containment, credential mode, Docker parsing/naming, and cache-key semantics need further product/spec evidence |
| Adopted | 1 | Narrow organization deny-list for the create/delete CLI paths |
| Product questions asked | 1 | The adopted contract is frozen before the formal proof run |

The source-bound `evidence.json` preserves the first complete review pass
(13 skips, 12 unresolved, 1 adopted). The two CORS rows were subsequently
resolved by an exact Go 1.25.7 standard-library inspection and raw HTTP
transport replay in
[`http-origin-transport-followup.json`](http-origin-transport-followup.json).
The replay verified that `net/http` folds continuation lines into spaces,
keeps CRLF-delimited following headers separate, and rejects a bare CR. The
pinned parser's header-value validator excludes both CR and LF, so neither
middleware can receive them embedded in `Header.Get("Origin")` on its network
listener path. The runnable replay and captured output are
[`origin-crlf-transport-replay.go`](origin-crlf-transport-replay.go) and
[`origin-crlf-transport-replay.jsonl`](origin-crlf-transport-replay.jsonl).

The adopted question covers only `_`, comma, Go RE2 ASCII whitespace, `?`, and
apostrophe. Its contract does not claim the accepted organization-name
characters are safe in paths. The unresolved dependency-filename rows are
retained because the regex transforms only the URL field while org/version
are interpolated into the same filename. The two CORS newline rows are
resolved only for the pinned standard listener path; a future synthetic
request path or alternate HTTP adapter would require a new review.

The registered Go source extractor previously recognized only `Compile` and
`MustCompile`, omitting static literal patterns passed to `regexp.Match*`.
This review uses the corrected raw inventory; dynamic pattern expressions
remain outside that literal-pattern extraction and require their separate
classification.

Rebuild the updated exact-pin source evidence with:

```sh
.venv/bin/python scripts/build-p2-source-review-evidence.py \
  --cohort properties/calibration/2026-09-12-calibration-20-r2/manifest.json \
  --inventory properties/calibration/2026-10-15-p2-source-inventory-v2/inventory.json \
  --sites properties/calibration/2026-10-15-p2-source-inventory-v2/sites.ndjson \
  --reviews properties/calibration/2026-10-15-p2-anax-source-review/reviews-after-transport.json \
  --checkout /tmp/regexproof-pinned-sources/anax-2f3fa5a506d6565fa68858b7963450567ddda114 \
  --repo-id open-horizon/anax \
  --pin 2f3fa5a506d6565fa68858b7963450567ddda114 \
  --output properties/calibration/2026-10-15-p2-anax-source-review/evidence-after-transport.json
```

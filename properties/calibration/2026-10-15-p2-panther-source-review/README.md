# Panther exact-pin P2 source review

This is a complete raw-regex review for one frozen cohort member. It is not a
review of the other 19 repositories or a complete P2 close-out.

## Scope and result

- Repository: `panther-labs/panther-analysis`
- Pin: `0cd0f5bd33469c9f03b578fe0104a4ebf23d9f4a`
- Extracted Python regex sites reviewed: **45**
- Evidence-backed skips: **44**
- Unresolved: **0**
- Adopted contracts / product questions: **1**

The 44 skips comprise 21 detection-event matchers without an independent
complete event-language contract, 19 telemetry enrichment or normalization
patterns, two internal Claude-verdict parsers, one metadata-format lint, and
one internal Git-diff metadata parser. The per-site evidence and rationale are
in [`reviews.json`](reviews.json); source-window and blob bindings are in
[`evidence.json`](evidence.json).

## Adopted question

The source has a pre-commit wrapper that invokes `.scripts/claude_review.py`.
The helper selects staged `.py`, YAML, and SQL paths, reads their staged
contents, and builds the prompt passed to `claude --print -`. Its exclusion
regex contains `secrets\.json` but does not match `secrets.py`. The formal
counterexample is that concrete staged path.

The policy basis is an inference: the separate `.claude/commands/pr-review.md`
asks that changed files matching `secrets` be excluded, but that slash command
is not called by the pre-commit helper. The adopted contract tests that
repository-level exclusion expectation against the helper; it does not assert
that the helper itself documents a shared policy. This is a reproduced policy
mismatch candidate, not a confirmed security finding.

## Proof and ground truth

[`proof-report.ndjson`](proof-report.ndjson) records two source-bound SAT
properties with the pinned Z3 5.0.0 solver:

- `PA-panther-staged-secrets-file-excluded-from-review-prompt`: witness
  `secrets.py`; the real pinned `get_changed_files` selects it and
  `read_file_contents` includes its synthetic sentinel.
- `PA-panther-exclusion-mutation-secret-file-pass-through`: after replacing
  the exclusion regex with `^$`, witness `password.secret.py` reaches the
  staged-content helper. The mutation guard also has real-helper replay.

The exact helper replay and nine-case path gate are recorded in
[`product-replay.json`](product-replay.json). Python 3.14.8 and Git 2.43.0
were used. The gate checks representative secret, credential, environment,
key, control, and ordinary paths against both Python `re.search` and the
helper's extension allowlist. It passes all nine cases and the mutation.
Neither replay invokes Claude or uses the network; every staged file contains
only synthetic marker text. No real secret content, developer machine, Claude
service, or downstream review result was inspected.

The P6 snapshot in [`p6-wave-r1/`](p6-wave-r1/) verifies the exact source pin,
mutation guard, and local gate. The runner correctly records `needs_review`
because the primary SAT candidate still needs product-impact disposition.

## Claims checked and limits

- The exclusion expression is a Python `search`, not a full-path validator.
- `secrets\.json` does not cover `secrets.py`; the direct witness reproduces
  that exact gap.
- `.env$`, `.pem$`, and `.key$` only match those suffixes. The helper also
  independently filters to `.py`, YAML, and SQL files, so a bare `.pem` file
  never reaches this helper's content reader by extension alone.
- The separate slash-command policy is not wired into the pre-commit helper;
  whether it is intended to govern the hook remains unconfirmed.
- The replay proves path selection and prompt construction only. It does not
  prove that any real secret was present or transmitted to an external
  service.

## Reproduction

```sh
.venv/bin/python scripts/z3-verify.py \
  PA-panther-staged-secrets-file-excluded-from-review-prompt \
  PA-panther-exclusion-mutation-secret-file-pass-through \
  --require-ground-truth --require-domain --require-contract --json \
  --fail-on-property-failure

.venv/bin/python scripts/panther-secret-path-regression-gate.py \
  --source-root /tmp/regexproof-pinned-sources/panther-analysis-0cd0f5bd33469c9f03b578fe0104a4ebf23d9f4a \
  --output properties/calibration/2026-10-15-p2-panther-source-review/product-replay.json
```

The one-question roster, gate definition, frozen source checkout, proof
artifacts, and P6 state are all retained beside this README.

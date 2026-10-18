# Implementation plan: replay forge-cli sensitive environment redaction

**Effort:** 2–4 hours for one contributor familiar with the regexproof harness.

**Parent context:** follow-up to [the helper-image slice](plan.md), wave 1 in
[`sweep/forge-cli-conversion/plan.md`](../forge-cli-conversion/plan.md), and the
human-contract-first conversion work in regexproof#551. Wave 1's close-out says
real helper-image replay remains unverified. This ticket takes one sink only.

## Goal

At the pinned forge-cli revision
`efcf8e4c0087def553a737dc1c4eebda5d8a90cd`, verify that
`build_runners/base.py:54` `SENSITIVE_ENV_KEY_RE` actually causes
`_render_command_for_log` to redact values for the documented sensitive
environment-key forms. Check the helper's output image as well as regex
membership; do not infer sink behavior from `SENSITIVE_ENV_KEY_RE` alone.

## Scope

- Adopt one human contract in family `FC-forge-cli`, wave `forge-cli_helper_image`.
- Cover the documented forms already listed in
  `regexproof/harness/forge_cli.py` (`password`, `passphrase`, `secret`,
  `token`, `credential`, `auth`, `api[_-]?key`, and `private[_-]?key`,
  including case variants and empty separator forms).
- Exercise the real `_render_command_for_log` at the pinned revision. Materialize
  or otherwise obtain that exact source revision for replay; do not replace the
  product helper with a locally reimplemented stand-in.
- Define the expected redacted command independently of the regex mirror.
- Add a mutation guard that weakens/removes sensitive-key recognition and
  demonstrates a cleartext value witness.
- Differential-check mirror classification and helper output against CPython
  `re` over the documented keys plus delimiter, empty-value, repeated-key,
  mixed-case, and terminal-newline cases. Exhaustive bounded key enumeration is
  preferred where practical.
- Add a `ground_truth` callback for SAT witnesses and run the family with
  `--require-ground-truth`.
- Emit a conversion row only after the contract, real replay, and mutation guard
  all pass; then regenerate the conversion ledger and write a short close-out
  recording domain, verdict, engine versions, and any refuted claims.

## Out of scope

- JAAS, Datamesh, URL, LLM endpoint, or copilot-memory sinks.
- Changes to forge-cli itself or public disclosure of any finding.
- A general regexproof helper-image framework or new solver backend.
- Treating `PRODUCT = MATCH`, solver-only acceptance, or a non-reproducing
  witness as a product result.

## Acceptance criteria

1. The contract names the configuration input, trust class, guarantee, declared
   domain, source pin, and `FC-forge-cli` family.
2. A test invokes the pinned product helper on real command inputs and confirms
   the exact output image, including that the sensitive value is absent.
3. The normal property is proven within its declared domain; `unknown`/timeout
   fails the run.
4. The mutation guard returns its expected SAT witness and shows the weakened
   policy can expose the value.
5. Differential checks find no disagreement between the mirror and CPython
   `re` / helper for the stated cases.
6. Any SAT witness is replayed by the ground-truth callback. No finding is
   reported or entered in the ledger if replay fails.
7. The family passes with `--require-contract --require-ground-truth` and the
   applicable mutation-coverage gate. The close-out clearly separates proven
   behavior from untested cases.

## Likely touch points

- `regexproof/harness/forge_cli.py`
- `tests/test_forge_cli_harness.py`
- `properties/generated/forge-cli_conversion.ndjson` (only if all gates pass)
- `properties/generated/conversion-ledger.json` and its markdown report
- `properties/generated/forge-cli_conversion_wave.md`

Follow repository `AGENTS.md`: inspect `docs/TRAPS.md` before encoding, mirror
search semantics accurately, ground-truth every witness, and treat timeout as
not proven.

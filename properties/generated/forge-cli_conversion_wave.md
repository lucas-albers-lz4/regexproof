# forge-cli conversion wave 1 — registration checkpoint

Pin: `Agenticstiger/forge-cli` @ `efcf8e4c0087def553a737dc1c4eebda5d8a90cd`.
Family: `FC-forge-cli`. Product engine: CPython `re` at the pinned source.
This checkpoint is not in `WAVE_CORPORA` and does not add the external source
tree to the repository.

## 15 read → 5 asked

The ranked reading set is frozen in [`forge-cli_rank.json`](forge-cli_rank.json).
The five adopted contracts cover the shared secret-redaction sinks for URL
userinfo, escaped-quote-safe JAAS values, dbt sensitive environment keys,
Datamesh error bodies, and LLM endpoint query credentials. The `_common.py`
Bearer/x-api-key fallbacks remain deferred because the surrounding source shows
central-redactor overlap; the generic assignment regex remains on the plan's
deny-list because its documented truncation is a residual limitation.

## Results

- 5 human-contract properties asked.
- 5 expected-UNSAT in the declared ASCII domains.
- 0 SAT and therefore 0 SAT witnesses requiring replay.
- 1 mutation guard SAT, confirming the URL-userinfo mirror is sensitive to an
  `@`-widening mutation.
- No upstream filing or disclosure decision is implied by this checkpoint.

The conversion rows are emitted in
[`forge-cli_conversion.ndjson`](forge-cli_conversion.ndjson). They record
`ground_truth_status: null` because no SAT witness was produced. This is not a
ground-truth claim about the entire application: the next step is a pinned
source checkout replay and differential fuzz of the actual helper/sink paths,
including escaped quotes, URL authority characters, delimiters, empty values,
and terminal newlines. A SAT witness or source/engine disagreement becomes a
separate ground-truthed finding before any filing decision.

## Stop vs next slice

Do not re-ask these five source sites in the same family. Continue only with
the planned source checkout replay. If the replay is clean, the next unused
idiom is the distinct x-api-key/Bearer persistence path; if it diverges, split
the finding by actual sink and keep it private-first until reviewed.

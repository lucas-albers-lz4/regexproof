# rust_regex corpus (Phase 1b) — inventory only

Pinned: **rust-lang/regex** `1.11.1`.

**No encodable fraction / go-no-go.** Walk `*.rs` and record file counts;
interesting patterns fold into the golden suite manually.

## Materialize

```bash
git clone --depth 1 --branch 1.11.1 \
  https://github.com/rust-lang/regex.git /tmp/corpus-wave/rust-regex
ln -sfn /tmp/corpus-wave/rust-regex batch/corpora/rust_regex/src
python -c "from pathlib import Path; from regexproof.extractors.rust_inventory import write_rust_inventory; write_rust_inventory(Path('batch/corpora/rust_regex/src'), Path('properties/generated/rust_regex_inventory_only.json'))"
```

Committed default path is `sample/` (tiny fixture) so the matrix row stays
reproducible without a checkout.

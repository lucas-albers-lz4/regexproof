# PCRE2 ground-truth helper

`match.py` parses and replays patterns via **real PCRE2** — never Python `re`.

## Provisioning (dev box / corpus wave pre-gate)

Install either:

1. **`pcre2grep`** on `PATH` (preferred for CI-less local work), e.g.
   `brew install pcre2` / `apt install pcre2-utils`, or
2. The **`pcre2`** Python bindings (`pip install pcre2`) when available for
   your Python minor.

Verify:

```bash
python helpers/pcre2/match.py parse 'a+'
printf 'aaa' | python helpers/pcre2/match.py match 'a+' ''
python -c "from regexproof.compiler.pcre import helper_used_for_parse_and_replay as h; assert h()"
```

CI currently pins `[pcre2] status = "n/a"` in `ci/toolchain.toml` (optional
helper). Corpus-wave PCRE inventories require a local helper before trusting
ground-truth.

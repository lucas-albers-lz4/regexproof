# shhgit corpus

Pinned eth0izzle/shhgit `config.yaml` signatures for Corpus Wave 3 Phase 3
(issue #114).

## Materialize the corpus

```bash
PIN=bac0c7d39519203d230b6c9a2c6e3eba18346aba
git clone https://github.com/eth0izzle/shhgit.git /tmp/shhgit
git -C /tmp/shhgit fetch --depth 1 origin "$PIN"
git -C /tmp/shhgit checkout "$PIN"
ln -sfn /tmp/shhgit batch/corpora/shhgit/repo
test "$(git -C /tmp/shhgit rev-parse HEAD)" = "$PIN"
```

Manifest pin: `bac0c7d39519203d230b6c9a2c6e3eba18346aba`.
Path: `batch/corpora/shhgit/repo` + `files: ["config.yaml"]` (or glob
`config.yaml`).

## Sample vs full

Wave corpus (full pin required for measure). `sample/config.yaml` holds
`^.*_rsa$` for local smoke. If `repo/` is missing/empty, measure **hard-error**.

## Extractor + dialect

- Extractor: `shhgit` (`regexproof/extractors/shhgit.py`)
- Dialect: `re2`, `call_kind=fullmatch` (anchored filename patterns)
- Flags: always `i` (`syntax.FoldCase` in `core/signatures.go`)
- Sample confirm: `^.*_rsa$` matches `FOO_RSA` via go-re2 helper with `i`

## Measure command

```bash
python scripts/measure-corpus-fraction.py --corpus shhgit --assert-determinism
```

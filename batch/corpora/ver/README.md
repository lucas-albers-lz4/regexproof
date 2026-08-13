# ver corpus

Pinned Smith GO admit [#302](https://github.com/lucas-albers-lz4/regexproof/issues/302) (RustPython),
[#301](https://github.com/lucas-albers-lz4/regexproof/issues/301) (cinder),
[#347](https://github.com/lucas-albers-lz4/regexproof/issues/347) (ver),
[#346](https://github.com/lucas-albers-lz4/regexproof/issues/346) (Hazer).

Python interpreter/fork. Top-60 .py files measured with the py_re family
norm (0.46-0.48). Non-security -> public-first.

## Materialize (example for RustPython)

```bash
PIN=24bd3b33f9c6d1a3d32ab297457f7a1b73984263
git clone --filter=blob:none https://github.com/RustPython/RustPython.git /tmp/RustPython
git -C /tmp/RustPython fetch --depth 1 origin "$PIN"
git -C /tmp/RustPython checkout "$PIN"
ln -sfn /tmp/RustPython batch/corpora/RustPython/rules
test "$(git -C /tmp/RustPython rev-parse HEAD)" = "$PIN"
```

Gate + Smith decisions in properties/generated/.

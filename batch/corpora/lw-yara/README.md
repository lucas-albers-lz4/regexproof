# lw-yara corpus

Pinned `Hestat/lw-yara` at `efd3cdaecae091357087fea6ecffded2eb6dba85` for Smith after admission `properties/generated/Hestat-lw-yara_gate_decision.json`.

Issue: #383. The manifest and Smith artifacts use the corpus key `lw-yara` from the gate record.

## Scope and result

The full pinned YARA tree: 175 files and 4,394 rule sites. The gate corpus key is `lw-yara`; the issue slug is recorded by the gate filename.

Measured fraction: `properties/generated/lw-yara_encodable_fraction.json`. Decision: **go**. `1,410/4,394 (32.09%) encode; fullword-boundary accounts for 2,981 sites, two patterns exceed the encoder length cap, and one named-backreference site is classified as backref. The run is complete with zero unclassified parse errors; this is compiler coverage only.`

The corpus is a security-tool source. Batch findings default to `private_first`; no public filing was performed. No conversion property is claimed by these compiler measurements.

## Materialize

```bash
python scripts/materialize-corpus.py --gate properties/generated/Hestat-lw-yara_gate_decision.json
```

## Measure / batch / record decision

```bash
python scripts/measure-corpus-fraction.py --corpus lw-yara --assert-determinism
python -m regexproof.batch --corpus lw-yara
python scripts/author-smith-decision.py --gate properties/generated/Hestat-lw-yara_gate_decision.json \
  --fraction properties/generated/lw-yara_encodable_fraction.json \
  --decision go --reason '1,410/4,394 (32.09%) encode; fullword-boundary accounts for 2,981 sites, two patterns exceed the encoder length cap, and one named-backreference site is classified as backref. The run is complete with zero unclassified parse errors; this is compiler coverage only.'
```

This corpus is not in `WAVE_CORPORA`; add it only after a separate conversion-wave decision.

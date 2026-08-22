"""Wave D synth cost control: default flip + explicit allowlist drift gates."""

from __future__ import annotations

from regexproof.batch.manifests import CORPUS_MANIFESTS
from regexproof.batch.synthesize import DEFAULT_SYNTH_MAX_SITES


def test_default_synth_max_sites_is_zero():
    assert DEFAULT_SYNTH_MAX_SITES == 0


def test_validatorjs_manifest_pins_explicit_synth_max_sites():
    meta = CORPUS_MANIFESTS["validatorjs"]
    assert "synth_max_sites" in meta
    assert meta["synth_max_sites"] == 200

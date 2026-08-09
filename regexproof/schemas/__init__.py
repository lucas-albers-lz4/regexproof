"""Versioned JSON Schema loaders for Phase-1/3/4/5 artifact contracts."""

from __future__ import annotations

import json
from pathlib import Path

SCHEMA_DIR = Path(__file__).resolve().parent

EXTRACTOR_SCHEMA_VERSION = "1"
COMPILED_SCHEMA_VERSION = "1"
REDOS_FINDING_SCHEMA_VERSION = "1"
ADMITTED_PAIR_SCHEMA_VERSION = "1"
RULE_DIFF_REPORT_SCHEMA_VERSION = "1"
QUESTION_INVENTORY_SCHEMA_VERSION = "1"
TRIAGE_RECORD_SCHEMA_VERSION = "1"
SCANNER_FINDING_SCHEMA_VERSION = "1"
GATE_DECISION_SCHEMA_VERSION = "1"


def load_schema(name: str) -> dict:
    path = SCHEMA_DIR / name
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def extractor_schema() -> dict:
    return load_schema("extractor_record.schema.json")


def compiled_pattern_schema() -> dict:
    return load_schema("compiled_pattern.schema.json")


def redos_finding_schema() -> dict:
    return load_schema("redos_finding.schema.json")


def admitted_pair_schema() -> dict:
    return load_schema("admitted_pair.schema.json")


def rule_diff_report_schema() -> dict:
    return load_schema("rule_diff_report.schema.json")


def question_inventory_schema() -> dict:
    return load_schema("question_inventory.schema.json")


def triage_record_schema() -> dict:
    return load_schema("triage_record.schema.json")


def scanner_finding_schema() -> dict:
    return load_schema("scanner_finding.schema.json")


def gate_decision_schema() -> dict:
    return load_schema("gate_decision.schema.json")

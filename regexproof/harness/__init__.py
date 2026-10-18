"""Importable Z3 property harness (canonical REGISTRY + run_one).

Replaces path-based ``importlib`` loads of ``scripts/z3-verify.py`` (#192).
"""

from __future__ import annotations

# Register built-in properties before re-exporting (side effect on REGISTRY).
import regexproof.harness.properties
import regexproof.harness.openwrt_packages
import regexproof.harness.openwrt_luci
import regexproof.harness.aidevops
import regexproof.harness.mycelium
import regexproof.harness.claude_code_plugins
import regexproof.harness.dogfood_shell
import regexproof.harness.doberman
import regexproof.harness.doberman_secret_paths
import regexproof.harness.forge_cli
import regexproof.harness.tracecat_origin
import regexproof.harness.tracecat_mcp_env_key
import regexproof.harness.tracecat_server_name
import regexproof.harness.tracecat_artifact_path_segment
import regexproof.harness.tracecat_workspace_sync_path_segment
import regexproof.harness.tracecat_rbac_scope
import regexproof.harness.tracecat_table_identifier
import regexproof.harness.tracecat_sandbox_env_key
import regexproof.harness.aidevops_cited_file
import regexproof.harness.aidevops_threshold
import regexproof.harness.mycelium_release
import regexproof.harness.mycelium_execstart
import regexproof.harness.malcontent_git_cve
import regexproof.harness.autoar_html_escape
import regexproof.harness.autoar_jsendpoints
import regexproof.harness.autoar_jsendpoints_scope
import regexproof.harness.aidevops_secret_read
import regexproof.harness.aidevops_webhook_receiver
import regexproof.harness.malcontent_author_markdown
import regexproof.harness.malcontent_description_markdown
import regexproof.harness.anax_org_validate
import regexproof.harness.autoar_phase_key
import regexproof.harness.xibo_csrf_cookie
import regexproof.harness.llm_honeypot
import regexproof.harness.panther_claude_review
import regexproof.harness.inhale_output_paths
import regexproof.harness.json_editor_enum_escape
import regexproof.harness.magic_js_base64url
import regexproof.harness.doberman_codex_apply_patch
import regexproof.harness.real_router_segment
import regexproof.harness.real_router_navigation  # noqa: F401
from regexproof.harness.cli import main
from regexproof.harness.core import (
    REGISTRY,
    SCHEMA_VERSION,
    Z3_VERSION,
    check_domain_coverage,
    check_mutation_coverage,
    ci,
    ci_class,
    engine_versions,
    prefix_match,
    prop,
    run_one,
    z3_str,
)

__all__ = [
    "REGISTRY",
    "SCHEMA_VERSION",
    "Z3_VERSION",
    "check_domain_coverage",
    "check_mutation_coverage",
    "ci",
    "ci_class",
    "engine_versions",
    "main",
    "prefix_match",
    "prop",
    "run_one",
    "z3_str",
]

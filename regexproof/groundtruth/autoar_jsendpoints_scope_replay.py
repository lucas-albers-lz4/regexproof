"""Exact-pin local HTTP replay for AutoAR's script-source scope boundary."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import tempfile
import threading
from dataclasses import dataclass
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from regexproof.groundtruth.autoar_html_escape_replay import source_root

PIN = "01cd447ad3b1acfed7e0680596c2c74458a4cf06"
REPOSITORY = "https://github.com/h0tak88r/AutoAR"
GO_TOOLCHAIN = "go1.25.7"
SOURCE_FILE = "internal/scanner/jsendpoints/jsendpoints.go"
SOURCE_SHA256 = "e9c03be11f7aab2a4310ea4944de5620e500f2400b13e22a3e1ea5b16745c549"
CALLER_FILE = "internal/scanner/subdomainmonitor/subdomainmonitor.go"
CALLER_SHA256 = "c9ad92e7c9aa6fdd8fa81df81c240ff4fd14a31009820bef3670ff8c2c2932dc"
README_SHA256 = "ff9fa0d8ec9e4be93b49a94ecc6104b32cb8db36dac08636740f63f90304a78d"
_JS_BODY = 'const apiUrl = "/api/v1/users";\n'


def _pinned_bytes(root: Path, relative: str, expected_sha256: str) -> bytes:
    path = root / relative
    if path.is_symlink() or not path.is_file():
        raise RuntimeError(f"pinned AutoAR source is missing or a symlink: {path}")
    source = path.read_bytes()
    committed = subprocess.run(
        ["git", "-C", str(root), "show", f"{PIN}:{relative}"],
        capture_output=True,
        check=True,
        timeout=30,
        shell=False,
    ).stdout
    if source != committed:
        raise RuntimeError(f"AutoAR bytes differ from {PIN}:{relative}")
    digest = hashlib.sha256(source).hexdigest()
    if digest != expected_sha256:
        raise RuntimeError(
            f"AutoAR {relative} digest is {digest}, expected {expected_sha256}"
        )
    return source


def verify_source_evidence() -> dict[str, Any]:
    """Bind the parser, its caller, and the documented target-scope rule."""
    root = source_root()
    parser = _pinned_bytes(root, SOURCE_FILE, SOURCE_SHA256)
    caller = _pinned_bytes(root, CALLER_FILE, CALLER_SHA256)
    readme = _pinned_bytes(root, "README.md", README_SHA256)
    required_parser = (
        b'var scriptSrcRe = regexp.MustCompile(`(?i)<script[^>]+src\\s*=\\s*["\']([^"\'>\\s]+)["\']`)',
        b"baseURL.ResolveReference(ref)",
        b'if abs.Scheme != "http" && abs.Scheme != "https" {',
        b'if !strings.Contains(strings.ToLower(abs.Path), ".js") {',
        b"content, err := downloadFile(client, jsURL)",
    )
    if any(parser.count(token) != 1 for token in required_parser):
        raise RuntimeError("pinned parser no longer has the reviewed URL resolution/fetch path")
    if (
        caller.count(b"db.ListLiveSubdomains(domain)") != 1
        or caller.count(b"jsendpoints.CollectEndpointsForHosts(hosts, threads)") != 1
    ):
        raise RuntimeError("pinned caller no longer connects live subdomains to the JS collector")
    scope_statement = (
        b"Only use it on targets where you have explicit written permission, "
        b"or on bug bounty programs where the target is in-scope."
    )
    if readme.count(scope_statement) != 1:
        raise RuntimeError("pinned README no longer contains the documented scope statement")
    return {
        "repository": REPOSITORY,
        "source_pin": PIN,
        "parser_file": SOURCE_FILE,
        "parser_sha256": SOURCE_SHA256,
        "caller_file": CALLER_FILE,
        "caller_sha256": CALLER_SHA256,
        "readme_file": "README.md",
        "readme_sha256": README_SHA256,
        "scope_statement": scope_statement.decode("ascii"),
        "resolution_path": [
            "scriptSrcRe captures an absolute HTTP URL from untrusted page HTML",
            "ResolveReference keeps the absolute URL's origin",
            "the collector checks HTTP(S) and a .js path but performs no origin or address-class check",
            "downloadFile issues the request from the scanner process",
        ],
        "caller_path": [
            "subdomainmonitor.diffJSEndpoints reads live subdomains for the scanned domain",
            "the caller supplies their HTTP(S) URLs to CollectEndpointsForHosts",
        ],
    }


def _section(
    source: bytes,
    start: bytes,
    end: bytes,
    label: str,
    *,
    closing: bytes = b"\n}",
) -> bytes:
    begin = source.find(start)
    finish = source.find(end, begin + len(start))
    if begin < 0 or finish < 0:
        raise RuntimeError(f"cannot uniquely bound exact pinned Go {label}")
    if source.find(start, begin + len(start)) >= 0:
        raise RuntimeError(f"pinned Go {label} start marker is not unique")
    return source[begin : finish + len(closing)]


def _go_wrapper(source: bytes) -> str:
    parser = source.decode("utf-8")
    script_decl = br"""var scriptSrcRe = regexp.MustCompile(`(?i)<script[^>]+src\s*=\s*["']([^"'>\s]+)["']`)"""
    endpoint_start = b"var endpointRegexes = []*regexp.Regexp{"
    endpoint_end = b"\n}\n\n// Run extracts API endpoints"
    declaration_start = parser.find(endpoint_start.decode("ascii"))
    declaration_end = parser.find(endpoint_end.decode("ascii"), declaration_start)
    if declaration_start < 0 or declaration_end < 0:
        raise RuntimeError("cannot extract pinned AutoAR endpoint regex declarations")
    endpoint_decl = parser[declaration_start : declaration_end + 2]
    # `scriptSrcRe` must be copied verbatim from the exact source bytes.
    if source.count(script_decl) != 1:
        raise RuntimeError("cannot uniquely identify the pinned scriptSrcRe declaration")
    script_line = next(
        line.decode("utf-8")
        for line in source.splitlines()
        if line.startswith(b"var scriptSrcRe = regexp.MustCompile(")
    )
    endpoint_type = _section(
        source,
        b"type Endpoint struct {",
        b"\n}\n\nconst (",
        "Endpoint type",
    ).decode("utf-8")
    constants = _section(
        source,
        b"const (\n\tmaxMonitorHosts = 100",
        b"\n)\n\n// CollectEndpointsForHosts",
        "monitor limits",
        closing=b"\n)",
    ).decode("utf-8")
    collect = _section(
        source,
        b"func CollectEndpointsForHosts(",
        b"\n}\n\n// normalizeHostURL",
        "collector",
    ).decode("utf-8")
    normalize = _section(
        source,
        b"func normalizeHostURL(",
        b"\n}\n\n// Options controls",
        "host normalization",
    ).decode("utf-8")
    extract = _section(
        source,
        b"func extractEndpoints(",
        b"\n}\n\n// isNoise",
        "endpoint extractor",
    ).decode("utf-8")
    noise = _section(
        source,
        b"func isNoise(",
        b"\n}\n\nfunc downloadFile",
        "noise filter",
    ).decode("utf-8")
    download = _section(
        source,
        b"func downloadFile(",
        b"\n}\n\nfunc readLines",
        "HTTP downloader",
    ).decode("utf-8")
    return f'''package main

import (
    "crypto/tls"
    "encoding/json"
    "fmt"
    "io"
    "net/http"
    "net/url"
    "os"
    "regexp"
    "runtime"
    "strings"
    "sync"
    "time"
)

{script_line}

{endpoint_type}

{constants}

{endpoint_decl}

{collect}

{normalize}

{extract}

{noise}

{download}

type noOpLogger struct{{}}
func (noOpLogger) Infof(string, ...any) {{}}
var logger = struct{{ GetLogger func() noOpLogger }}{{GetLogger: func() noOpLogger {{ return noOpLogger{{}} }}}}

type scenario struct {{
    Hosts []string `json:"hosts"`
    Threads int `json:"threads"`
}}
type request struct {{ Scenarios []scenario `json:"scenarios"` }}
type scenarioResult struct {{ Endpoints []Endpoint `json:"endpoints"`; Error string `json:"error"` }}
type response struct {{ GoVersion string `json:"go_version"`; Results []scenarioResult `json:"results"` }}

func main() {{
    var input request
    if err := json.NewDecoder(os.Stdin).Decode(&input); err != nil {{ panic(err) }}
    out := response{{GoVersion: runtime.Version(), Results: make([]scenarioResult, 0, len(input.Scenarios))}}
    for _, item := range input.Scenarios {{
        endpoints, err := CollectEndpointsForHosts(item.Hosts, item.Threads)
        row := scenarioResult{{Endpoints: endpoints}}
        if err != nil {{ row.Error = err.Error() }}
        out.Results = append(out.Results, row)
    }}
    if err := json.NewEncoder(os.Stdout).Encode(out); err != nil {{ panic(err) }}
}}
'''


@dataclass
class ScopeFixture:
    target: ThreadingHTTPServer
    canary: ThreadingHTTPServer
    target_thread: threading.Thread
    canary_thread: threading.Thread
    counts: dict[str, int]
    lock: threading.Lock
    same_origin: bool = False

    @property
    def target_url(self) -> str:
        return f"http://127.0.0.1:{self.target.server_port}/"

    @property
    def canary_origin(self) -> str:
        return f"http://127.0.0.1:{self.canary.server_port}"

    @property
    def canary_script_url(self) -> str:
        return f"{self.canary_origin}/bundle.js"

    @property
    def same_origin_script_url(self) -> str:
        return f"http://127.0.0.1:{self.target.server_port}/bundle.js"

    @property
    def external_html(self) -> str:
        return f'<html><script src="{self.canary_script_url}"></script></html>'

    @property
    def same_origin_html(self) -> str:
        return '<html><script src="/bundle.js"></script></html>'

    def counts_snapshot(self) -> dict[str, int]:
        with self.lock:
            return dict(sorted(self.counts.items()))

    def close(self) -> None:
        for server in (self.target, self.canary):
            server.shutdown()
            server.server_close()
        for thread in (self.target_thread, self.canary_thread):
            thread.join(timeout=5)
            if thread.is_alive():
                raise RuntimeError("AutoAR local HTTP fixture server did not stop")


def start_scope_fixture() -> ScopeFixture:
    """Start only two disposable HTTP listeners bound to IPv4 loopback."""
    counts: dict[str, int] = {}
    lock = threading.Lock()
    holder: dict[str, ScopeFixture] = {}

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # noqa: N802 - stdlib handler API
            fixture = holder["fixture"]
            role = "target" if self.server is fixture.target else "canary"
            key = f"{role} {self.path}"
            with fixture.lock:
                fixture.counts[key] = fixture.counts.get(key, 0) + 1
            if role == "target" and self.path == "/":
                body = fixture.same_origin_html if fixture.same_origin else fixture.external_html
            elif self.path == "/bundle.js":
                body = _JS_BODY
            else:
                self.send_error(404)
                return
            payload = body.encode("ascii")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8" if self.path == "/" else "application/javascript")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

        def log_message(self, _format: str, *_args: Any) -> None:
            return

    target = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    canary = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    target.daemon_threads = True
    canary.daemon_threads = True
    fixture = ScopeFixture(
        target=target,
        canary=canary,
        target_thread=threading.Thread(target=target.serve_forever, daemon=True),
        canary_thread=threading.Thread(target=canary.serve_forever, daemon=True),
        counts=counts,
        lock=lock,
    )
    holder["fixture"] = fixture
    fixture.target_thread.start()
    fixture.canary_thread.start()
    return fixture


def run_collector(scenarios: list[dict[str, Any]]) -> dict[str, Any]:
    """Run exact pinned CollectEndpointsForHosts in Go 1.25.7."""
    if not shutil.which("go"):
        raise RuntimeError("Go is required for AutoAR's pinned HTTP collector replay")
    root = source_root()
    source = _pinned_bytes(root, SOURCE_FILE, SOURCE_SHA256)
    with tempfile.TemporaryDirectory(prefix="regexproof-autoar-jsendpoints-scope-") as temp:
        work = Path(temp)
        (work / "go.mod").write_text(
            "module regexproof-autoar-jsendpoints-scope-replay\n\ngo 1.25.7\n",
            encoding="utf-8",
        )
        (work / "main.go").write_text(_go_wrapper(source), encoding="utf-8")
        env = os.environ.copy()
        env["GOTOOLCHAIN"] = GO_TOOLCHAIN
        try:
            proc = subprocess.run(
                ["go", "run", "."],
                cwd=work,
                input=json.dumps({"scenarios": scenarios}, ensure_ascii=True),
                capture_output=True,
                text=True,
                timeout=150,
                check=False,
                shell=False,
                env=env,
            )
        except subprocess.TimeoutExpired as exc:
            raise RuntimeError("AutoAR exact collector replay timed out") from exc
        if proc.returncode != 0:
            raise RuntimeError(
                f"AutoAR exact collector replay failed ({proc.returncode}): "
                f"{proc.stderr.strip()[-3000:]}"
            )
        try:
            response = json.loads(proc.stdout)
        except json.JSONDecodeError as exc:
            raise RuntimeError("AutoAR exact collector replay returned invalid JSON") from exc
    if response.get("go_version") != GO_TOOLCHAIN:
        raise RuntimeError(
            f"AutoAR exact collector used {response.get('go_version')!r}, expected {GO_TOOLCHAIN}"
        )
    results = response.get("results")
    if not isinstance(results, list) or len(results) != len(scenarios):
        raise RuntimeError("AutoAR exact collector replay returned an invalid result vector")
    for result in results:
        if not isinstance(result, dict) or result.get("error"):
            raise RuntimeError(f"AutoAR collector returned an error: {result!r}")
        endpoints = result.get("endpoints")
        if not isinstance(endpoints, list):
            raise RuntimeError("AutoAR exact collector replay returned malformed endpoints")
        if any(
            not isinstance(endpoint, dict)
            or not isinstance(endpoint.get("Path"), str)
            or not isinstance(endpoint.get("Source"), str)
            for endpoint in endpoints
        ):
            raise RuntimeError("AutoAR exact collector replay returned malformed endpoint rows")
    return response


def origins_differ(target_url: str, script_url: str) -> bool:
    target = urlparse(target_url)
    script = urlparse(script_url)
    return (target.scheme.lower(), target.hostname, target.port) != (
        script.scheme.lower(), script.hostname, script.port
    )


__all__ = [
    "CALLER_FILE",
    "CALLER_SHA256",
    "GO_TOOLCHAIN",
    "PIN",
    "README_SHA256",
    "REPOSITORY",
    "SOURCE_FILE",
    "SOURCE_SHA256",
    "ScopeFixture",
    "origins_differ",
    "run_collector",
    "start_scope_fixture",
    "verify_source_evidence",
]

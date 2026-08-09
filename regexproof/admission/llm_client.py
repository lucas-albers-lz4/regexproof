"""Injectable gate-decision classifier for P3b LLM draft mode (#134)."""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass, field
from typing import Any, Callable, Protocol

from regexproof.admission.templates import TEMPLATE_NAMES

PINNED_MODEL = "opencode/deepseek-v4-flash"
RETRY_BACKOFF_S = 60.0


@dataclass
class ClassificationResult:
    """Outcome of one classify attempt (or the final attempt after retry)."""

    label: str | None
    confidence: str = ""
    ok: bool = False
    latency_ms: int = 0
    tokens: int | None = None
    raw: str = ""
    error: str = ""
    attempts: list[dict[str, Any]] = field(default_factory=list)

    def as_audit_call(self, *, slug: str = PINNED_MODEL) -> dict[str, Any]:
        return {
            "slug": slug,
            "latency_ms": self.latency_ms,
            "tokens": self.tokens,
            "ok": self.ok,
            "label": self.label,
            "error": self.error or None,
        }


class GateClassifier(Protocol):
    def classify(self, draft: dict[str, Any]) -> ClassificationResult:
        """Return a template class label or a failed classification."""
        ...


def normalize_label(raw: str | None) -> str | None:
    if not raw:
        return None
    label = str(raw).strip().lower().replace("_", "-")
    # Accept "class: below-scale" style answers
    for name in TEMPLATE_NAMES:
        if name in label or label == name:
            return name
    return None


class StaticClassifier:
    """Test double: returns a fixed label or fails."""

    def __init__(
        self,
        label: str | None = None,
        *,
        fail_times: int = 0,
        error: str = "simulated failure",
    ):
        self.label = label
        self.fail_times = fail_times
        self.error = error
        self.calls = 0

    def classify(self, draft: dict[str, Any]) -> ClassificationResult:
        del draft
        self.calls += 1
        if self.calls <= self.fail_times:
            return ClassificationResult(
                label=None,
                ok=False,
                error=self.error,
                attempts=[{"ok": False, "error": self.error}],
            )
        if self.label is None:
            return ClassificationResult(
                label=None,
                ok=False,
                error="empty classification",
                attempts=[{"ok": False, "error": "empty"}],
            )
        return ClassificationResult(
            label=normalize_label(self.label),
            ok=normalize_label(self.label) is not None,
            confidence="high",
            latency_ms=1,
            tokens=0,
            raw=str(self.label),
            attempts=[{"ok": True, "label": self.label}],
        )


class RetryingClassifier:
    """Wrap a classifier with one retry + injectable backoff."""

    def __init__(
        self,
        inner: GateClassifier,
        *,
        sleep_fn: Callable[[float], None] = time.sleep,
        backoff_s: float = RETRY_BACKOFF_S,
    ):
        self.inner = inner
        self.sleep_fn = sleep_fn
        self.backoff_s = backoff_s

    def classify(self, draft: dict[str, Any]) -> ClassificationResult:
        first = self.inner.classify(draft)
        if first.ok and first.label:
            return first
        self.sleep_fn(self.backoff_s)
        second = self.inner.classify(draft)
        second.attempts = list(first.attempts) + list(second.attempts)
        second.latency_ms = int(first.latency_ms) + int(second.latency_ms)
        return second


class OpencodeDeepseekClassifier:
    """Live classifier via OpenAI-compatible chat completions (optional).

    Env: ``OPENCODE_API_BASE`` (default ``https://api.opencode.ai/v1``),
    ``OPENCODE_API_KEY`` or ``OPENAI_API_KEY``. Unit tests never call this.
    """

    def __init__(
        self,
        *,
        session: Any | None = None,
        model: str = PINNED_MODEL,
        sleep_fn: Callable[[float], None] = time.sleep,
    ):
        self.session = session
        self.model = model
        self.sleep_fn = sleep_fn

    def classify(self, draft: dict[str, Any]) -> ClassificationResult:
        # One attempt here; RetryingClassifier owns the second try.
        return self._once(draft)

    def _once(self, draft: dict[str, Any]) -> ClassificationResult:
        try:
            import requests
        except ImportError as e:  # pragma: no cover
            return ClassificationResult(label=None, ok=False, error=f"requests missing: {e}")

        sess = self.session or requests.Session()
        base = os.environ.get("OPENCODE_API_BASE", "https://api.opencode.ai/v1").rstrip("/")
        key = os.environ.get("OPENCODE_API_KEY") or os.environ.get("OPENAI_API_KEY") or ""
        headers = {"Content-Type": "application/json"}
        if key:
            headers["Authorization"] = f"Bearer {key}"
        probe = draft.get("probe") or {}
        prompt = (
            "Classify this regex corpus admission probe into exactly one label: "
            "new-surface | security-boundary | below-scale | repo-moved. "
            "Reply with only the label.\n\n"
            f"corpus={draft.get('corpus')!r} sites={probe.get('regex_sites')!r} "
            f"boundary={probe.get('security_boundary')!r} "
            f"dialect={json.dumps(probe.get('dialect') or {}, sort_keys=True)}"
        )
        t0 = time.monotonic()
        try:
            resp = sess.post(
                f"{base}/chat/completions",
                headers=headers,
                json={
                    "model": self.model,
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0,
                },
                timeout=60,
            )
        except Exception as e:  # pragma: no cover - network
            return ClassificationResult(
                label=None,
                ok=False,
                error=str(e),
                attempts=[{"ok": False, "error": str(e)}],
            )
        latency = int((time.monotonic() - t0) * 1000)
        if getattr(resp, "status_code", 0) != 200:
            err = f"HTTP {getattr(resp, 'status_code', '?')}: {getattr(resp, 'text', '')[:200]}"
            return ClassificationResult(
                label=None,
                ok=False,
                latency_ms=latency,
                error=err,
                attempts=[{"ok": False, "error": err}],
            )
        try:
            body = resp.json()
            content = body["choices"][0]["message"]["content"]
            tokens = (body.get("usage") or {}).get("total_tokens")
        except Exception as e:
            return ClassificationResult(
                label=None,
                ok=False,
                latency_ms=latency,
                error=f"bad response: {e}",
                attempts=[{"ok": False, "error": str(e)}],
            )
        label = normalize_label(content)
        return ClassificationResult(
            label=label,
            ok=label is not None,
            confidence="model",
            latency_ms=latency,
            tokens=tokens,
            raw=str(content),
            error="" if label else f"unrecognized label: {content!r}",
            attempts=[{"ok": label is not None, "label": label, "raw": content}],
        )

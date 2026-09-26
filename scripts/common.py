"""Shared helpers: environment, HTTP session, run health."""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
CONFIG_DIR = ROOT / "config"

USER_AGENT = "son-nerve/0.1 (Austin hospitality research; human-scale use)"
TIMEOUT = 60

load_dotenv(ROOT / ".env")


def env(name: str) -> str | None:
    """Return an env var, treating empty strings as unset."""
    value = os.environ.get(name, "").strip()
    return value or None


def session() -> requests.Session:
    s = requests.Session()
    s.headers["User-Agent"] = USER_AGENT
    token = env("SOCRATA_APP_TOKEN")
    if token:
        s.headers["X-App-Token"] = token
    return s


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def classify_error(exc: Exception) -> str:
    """Map a request failure to a run-health status."""
    if isinstance(exc, requests.exceptions.ProxyError):
        return "blocked_by_network"
    if isinstance(exc, requests.exceptions.HTTPError) and exc.response is not None:
        code = exc.response.status_code
        if code in (401, 403):
            return "auth_error"
        if code == 404:
            return "not_found"
        return f"http_{code}"
    if isinstance(exc, (requests.exceptions.Timeout, requests.exceptions.ConnectionError)):
        return "unreachable"
    return "error"


def redact(text: str) -> str:
    """Strip key values from text before it is logged or written to disk."""
    for name in ("FRED_API_KEY", "BLS_API_KEY", "SOCRATA_APP_TOKEN", "CENSUS_API_KEY", "EIA_API_KEY"):
        value = env(name)
        if value:
            text = text.replace(value, f"<{name}>")
    return text


def write_run_health(path: Path, job: str, results: list[dict]) -> None:
    ok = sum(1 for r in results if r.get("status") == "ok")
    payload = {
        "job": job,
        "run_at": now_utc().isoformat(timespec="seconds"),
        "sources_ok": ok,
        "sources_total": len(results),
        "success": ok == len(results),
        "results": results,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(redact(json.dumps(payload, indent=2, default=str)))

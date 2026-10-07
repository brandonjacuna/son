"""Offline tests for scripts/test_pull.py. No network."""

import json
import sys
from pathlib import Path

import pytest
import requests

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import common  # noqa: E402
import test_pull as tp  # noqa: E402


class FakeResponse:
    def __init__(self, payload=None, text="", status=200, url="https://example.test/"):
        self._payload, self.text, self.status_code, self.url = payload, text, status, url

    def json(self):
        return self._payload

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.exceptions.HTTPError(response=self)


class FakeSession:
    """Routes GETs by (path suffix, $select) to canned responses."""

    def __init__(self, routes):
        self.routes = routes

    def get(self, url, params=None, timeout=None):
        key = (url.rsplit("/", 1)[-1], (params or {}).get("$select"))
        return self.routes.get(key) or self.routes[(key[0], None)]


META = {
    "name": "Pending Applications",
    "rowsUpdatedAt": 1_790_000_000,
    "columns": [
        {"fieldName": ":id", "dataTypeName": "meta_data"},
        {"fieldName": "trade_name", "dataTypeName": "text"},
        {"fieldName": "address", "dataTypeName": "text"},
        {"fieldName": "city", "dataTypeName": "text"},
        {"fieldName": "license_type", "dataTypeName": "text"},
        {"fieldName": "submission_date", "dataTypeName": "calendar_date"},
    ],
}


@pytest.fixture(autouse=True)
def out_dir(tmp_path, monkeypatch):
    monkeypatch.setattr(tp, "OUT_DIR", tmp_path)
    return tmp_path


def socrata_session(meta=META):
    return FakeSession({
        ("mxm5-tdpj.json", None): FakeResponse(meta),
        ("mxm5-tdpj.json", "count(*) AS n"): FakeResponse([{"n": "1234"}]),
        ("mxm5-tdpj.json", "max(submission_date) AS m"): FakeResponse([{"m": "2026-09-25T00:00:00.000"}]),
    })


def test_socrata_probe_reports_counts_fields_freshness(out_dir, monkeypatch):
    s = socrata_session()
    rows = [{"trade_name": "A", "submission_date": "2026-09-25T00:00:00.000"}]
    orig = s.get
    s.get = lambda url, params=None, timeout=None: (
        FakeResponse(rows) if params and "$limit" in params else orig(url, params, timeout))
    res = tp.probe_socrata(s, tp.SOCRATA[0], sample=5)
    assert res["status"] == "ok", res["notes"]
    assert res["row_count"] == 1234
    assert "trade_name (text)" in res["fields"]
    assert not any(f.startswith(":") for f in res["fields"])
    assert res["freshness"]["latest_record_field"] == "submission_date"
    assert res["freshness"]["latest_record"] == "2026-09-25"
    assert (out_dir / "tabc_pending_sample.parquet").exists()


def test_socrata_probe_flags_missing_expected_fields():
    meta = {**META, "columns": [c for c in META["columns"] if c["fieldName"] != "trade_name"]}
    s = socrata_session(meta)
    orig = s.get
    s.get = lambda url, params=None, timeout=None: (
        FakeResponse([]) if params and "$limit" in params else orig(url, params, timeout))
    res = tp.probe_socrata(s, tp.SOCRATA[0], sample=5)
    assert res["status"] == "needs_review"
    assert any("trade" in n for n in res["notes"])


def test_socrata_probe_reports_bad_dataset_id():
    s = FakeSession({("mxm5-tdpj.json", None): FakeResponse(status=404)})
    assert tp.probe_socrata(s, tp.SOCRATA[0], sample=5)["status"] == "not_found"


def test_network_block_is_classified():
    assert common.classify_error(requests.exceptions.ProxyError("403")) == "blocked_by_network"


def test_fred_without_key_needs_key(monkeypatch):
    monkeypatch.delenv("FRED_API_KEY", raising=False)
    res = tp.probe_fred(FakeSession({}))
    assert {r["status"] for r in res} == {"needs_key"}


def test_page_helpers():
    html = ('<p>Released August 26, 2026. Next release September 30, 2099.</p>'
            '<a href="/files/tssos-data.xlsx">Data</a><a href="/about">About</a>')
    links = tp.page_links(html, "https://www.dallasfed.org/research/")
    assert ("https://www.dallasfed.org/files/tssos-data.xlsx", "Data") in links
    assert [u for u, t in links if tp.is_data_file(u, t)] == ["https://www.dallasfed.org/files/tssos-data.xlsx"]
    assert tp.latest_date_text(html) == "August 26, 2026"


def test_run_health_redacts_keys(tmp_path, monkeypatch):
    monkeypatch.setenv("FRED_API_KEY", "supersecret123")
    path = tmp_path / "run_health.json"
    common.write_run_health(path, "t", [{"status": "ok", "notes": ["url?api_key=supersecret123"]}])
    text = path.read_text()
    assert "supersecret123" not in text
    assert json.loads(text)["success"] is True

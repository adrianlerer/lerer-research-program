#!/usr/bin/env python3
"""Reconcile Zenodo records, README inventory rows, and mirrored paper files."""

from __future__ import annotations

import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
EXTERNAL_DUPLICATES = {
    "10.2139/ssrn.5584450": "10.5281/zenodo.18576911",
    "10.2139/ssrn.5405459": "10.5281/zenodo.20613103",
}


def live_records() -> list[dict]:
    query = 'creators.name:"LERER, Ignacio Adrian"'
    records: list[dict] = []
    page = 1
    while True:
        url = "https://zenodo.org/api/records?" + urllib.parse.urlencode(
            {"q": query, "size": 25, "page": page, "sort": "newest"}
        )
        last_error: Exception | None = None
        for attempt in range(4):
            try:
                request = urllib.request.Request(
                    url,
                    headers={"User-Agent": "Mozilla/5.0 lerer-research-inventory-auditor/1.0"},
                )
                with urllib.request.urlopen(request, timeout=60) as response:
                    payload = json.load(response)
                break
            except Exception as exc:
                last_error = exc
                time.sleep(1 + attempt)
        else:
            raise RuntimeError(f"Zenodo API failed after four verified-TLS attempts: {last_error}")
        batch = payload["hits"]["hits"]
        records.extend(batch)
        if not batch or len(records) >= int(payload["hits"]["total"]):
            break
        page += 1
    return list({str(record["id"]): record for record in records}.values())


def repo_inventory() -> tuple[set[str], list[str]]:
    text = README.read_text(encoding="utf-8")
    zenodo = text.split("## Papers — Zenodo", 1)[1].split("## Papers — SSRN Historical Archive", 1)[0]
    native = zenodo.split("### Native Zenodo DOI records", 1)[1].split(
        "### Zenodo-hosted records with external DOI", 1
    )[0]
    external = zenodo.split("### Zenodo-hosted records with external DOI", 1)[1]
    native_ids = set(re.findall(r"10\.5281/zenodo\.(\d+)", native))
    external_ids = set(re.findall(r"https://zenodo\.org/records/(\d+)", external))
    paper_links = sorted(set(re.findall(r"\]\((papers/[^)]+)\)", zenodo)))
    return native_ids | external_ids, paper_links


def main() -> int:
    records = live_records()
    live_ids = {str(record["id"]) for record in records}
    repo_ids, paper_links = repo_inventory()
    missing_files = [path for path in paper_links if not (ROOT / path).is_file()]
    external = []
    for record in records:
        metadata = record.get("metadata", {})
        doi = record.get("doi") or metadata.get("doi", "")
        if doi.startswith("10.5281/zenodo."):
            continue
        external.append(
            {
                "record_id": str(record["id"]),
                "doi": doi,
                "title": metadata.get("title", ""),
                "classification": "imported duplicate" if doi in EXTERNAL_DUPLICATES else "unique work",
                "canonical_doi": EXTERNAL_DUPLICATES.get(doi, doi),
            }
        )
    missing_in_repo = sorted(live_ids - repo_ids)
    stale_in_repo = sorted(repo_ids - live_ids)
    status = "PASS" if not missing_in_repo and not stale_in_repo and not missing_files else "FAIL"
    result = {
        "status": status,
        "zenodo_hosted_records": len(records),
        "native_zenodo_doi_records": len(records) - len(external),
        "external_doi_records": len(external),
        "imported_duplicate_records": sum(row["classification"] == "imported duplicate" for row in external),
        "unique_works": len(records) - sum(row["classification"] == "imported duplicate" for row in external),
        "repository_represented_records": len(repo_ids),
        "live_records_missing_from_repository": missing_in_repo,
        "repository_records_missing_from_zenodo": stale_in_repo,
        "missing_repository_files": missing_files,
        "external_records": sorted(external, key=lambda row: row["record_id"], reverse=True),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

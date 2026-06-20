#!/usr/bin/env python3
"""Sync repository PDFs into a NotebookLM notebook.

The script compares local filenames in papers/*.pdf with NotebookLM source
titles and uploads only missing files. It assumes the NotebookLM CLI (`nlm`)
is already authenticated.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
from pathlib import Path


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def resolve_nlm(explicit: str | None) -> str:
    candidates = [
        explicit,
        os.environ.get("NLM_BIN"),
        shutil.which("nlm"),
        str(Path.home() / ".local/bin/nlm"),
    ]
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return candidate
    raise SystemExit(
        "Could not find nlm. Set NLM_BIN or install/authenticate "
        "adrianlerer/notebooklm-mcp-cli."
    )


def source_titles(nlm: str, notebook_id: str) -> set[str]:
    proc = run([nlm, "source", "list", notebook_id, "--json"])
    if proc.returncode != 0:
        raise SystemExit(proc.stdout)
    try:
        sources = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Could not parse nlm source list JSON: {exc}") from exc
    return {source.get("title", "") for source in sources}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--notebook-id",
        default=os.environ.get("LERER_NOTEBOOKLM_ID"),
        help="NotebookLM notebook id. Defaults to LERER_NOTEBOOKLM_ID.",
    )
    parser.add_argument(
        "--papers-dir",
        default="papers",
        help="Directory containing PDF files to sync.",
    )
    parser.add_argument("--nlm-bin", help="Path to the nlm executable.")
    parser.add_argument(
        "--no-wait",
        action="store_true",
        help="Upload without waiting for NotebookLM processing.",
    )
    parser.add_argument(
        "--wait-timeout",
        default="240",
        help="Seconds to wait per source when waiting is enabled.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show missing sources without uploading.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Upload at most this many missing files.",
    )
    args = parser.parse_args()

    if not args.notebook_id:
        raise SystemExit("Pass --notebook-id or set LERER_NOTEBOOKLM_ID.")

    nlm = resolve_nlm(args.nlm_bin)
    papers_dir = Path(args.papers_dir)
    if not papers_dir.exists():
        raise SystemExit(f"Missing papers directory: {papers_dir}")

    pdfs = sorted(p for p in papers_dir.iterdir() if p.suffix.lower() == ".pdf")
    existing = source_titles(nlm, args.notebook_id)
    missing = [p for p in pdfs if p.name not in existing]
    if args.limit is not None:
        missing = missing[: args.limit]

    print(f"PDFs in repo: {len(pdfs)}")
    print(f"Missing in NotebookLM: {len(missing)}")
    for path in missing:
        print(path.name)

    if args.dry_run or not missing:
        return 0

    failures: list[tuple[str, str]] = []
    for index, path in enumerate(missing, start=1):
        cmd = [nlm, "source", "add", args.notebook_id, "--file", str(path)]
        if not args.no_wait:
            cmd += ["--wait", "--wait-timeout", args.wait_timeout]
        print(f"[{index}/{len(missing)}] uploading {path.name}", flush=True)
        proc = run(cmd)
        if proc.returncode != 0:
            failures.append((path.name, proc.stdout))
            print(f"FAIL {path.name}", flush=True)
            print(proc.stdout[-1200:], flush=True)
        else:
            print(f"OK {path.name}", flush=True)

    if failures:
        print("\nFailed uploads:")
        for name, output in failures:
            print(f"- {name}: {output[-300:].strip()}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

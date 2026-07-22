#!/usr/bin/env python3
"""Validate Ideas Hub reconciliation metadata and Architect task identity.

The validator intentionally uses only the Python standard library so it can run
locally and in CI without installing dependencies.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS_DIR = ROOT / "projects"
RUNS_DIR = ROOT / "architect" / "runs"

RECONCILIATION_FIELDS = (
    "repository",
    "default_branch",
    "authority_document",
    "authority_revision",
    "implementation_revision",
    "last_reconciled",
    "reconciliation_status",
)
RECONCILIATION_STATUSES = {
    "aligned",
    "documentation_ahead",
    "implementation_ahead",
    "conflicted",
    "unverified",
    "repository_unavailable",
}
TASK_STATUSES = {
    "proposed",
    "ready",
    "needs_discovery",
    "needs_spec",
    "needs_approval",
    "blocked",
    "running",
    "verifying",
    "completed",
    "failed",
    "skipped",
}
ACTIVE_TASK_STATUSES = {
    "proposed",
    "ready",
    "needs_discovery",
    "needs_spec",
    "needs_approval",
    "blocked",
    "running",
    "verifying",
}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
REPO_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
SHA_RE = re.compile(r"^[0-9a-fA-F]{7,40}$")
KEY_RE = re.compile(r"^[a-z0-9][a-z0-9-]*:[A-Za-z0-9][A-Za-z0-9_.:-]*$")


@dataclass(frozen=True)
class Finding:
    path: Path
    message: str

    def render(self) -> str:
        return f"{self.path.relative_to(ROOT)}: {self.message}"


def extract_heading_section(text: str, heading: str) -> str | None:
    pattern = re.compile(
        rf"^## {re.escape(heading)}\s*$\n(.*?)(?=^## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    return match.group(1).strip() if match else None


def extract_yaml_blocks(text: str) -> list[str]:
    return re.findall(r"```ya?ml\s*\n(.*?)```", text, re.DOTALL | re.IGNORECASE)


def parse_flat_yaml(block: str) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw_line in block.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"\'')
    return values


def validate_project(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    text = path.read_text(encoding="utf-8")
    section = extract_heading_section(text, "Reconciliation")
    if section is None:
        return findings

    blocks = extract_yaml_blocks(section)
    if not blocks:
        return [Finding(path, "Reconciliation section must contain a fenced YAML block")]

    metadata = parse_flat_yaml(blocks[0])
    missing = [field for field in RECONCILIATION_FIELDS if not metadata.get(field)]
    if missing:
        findings.append(Finding(path, f"missing reconciliation fields: {', '.join(missing)}"))
        return findings

    if not REPO_RE.fullmatch(metadata["repository"]):
        findings.append(Finding(path, "repository must use owner/name format"))
    if not metadata["default_branch"]:
        findings.append(Finding(path, "default_branch must not be empty"))
    if metadata["authority_revision"] != "not_available" and not SHA_RE.fullmatch(
        metadata["authority_revision"]
    ):
        findings.append(
            Finding(path, "authority_revision must be a 7-40 character git SHA or not_available")
        )
    if not SHA_RE.fullmatch(metadata["implementation_revision"]):
        findings.append(Finding(path, "implementation_revision must be a 7-40 character git SHA"))
    if not DATE_RE.fullmatch(metadata["last_reconciled"]):
        findings.append(Finding(path, "last_reconciled must use YYYY-MM-DD"))
    if metadata["reconciliation_status"] not in RECONCILIATION_STATUSES:
        findings.append(
            Finding(
                path,
                "unsupported reconciliation_status "
                f"{metadata['reconciliation_status']!r}",
            )
        )

    return findings


def task_records(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    records: list[dict[str, str]] = []
    for block in extract_yaml_blocks(text):
        parsed = parse_flat_yaml(block)
        if "task_id" in parsed or "work_key" in parsed:
            records.append(parsed)
    return records


def validate_tasks(paths: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    active_keys: dict[str, list[tuple[Path, str]]] = defaultdict(list)

    for path in paths:
        for index, task in enumerate(task_records(path), start=1):
            label = task.get("task_id", f"task block {index}")
            required = ("task_id", "work_key", "requirement_key", "status")
            missing = [field for field in required if not task.get(field)]
            if missing:
                findings.append(
                    Finding(path, f"{label}: missing task fields: {', '.join(missing)}")
                )
                continue

            status = task["status"]
            if status not in TASK_STATUSES:
                findings.append(Finding(path, f"{label}: unsupported status {status!r}"))
            if not KEY_RE.fullmatch(task["work_key"]):
                findings.append(Finding(path, f"{label}: invalid work_key {task['work_key']!r}"))
            requirement_key = task["requirement_key"]
            if requirement_key != "not_applicable" and not KEY_RE.fullmatch(requirement_key):
                findings.append(
                    Finding(path, f"{label}: invalid requirement_key {requirement_key!r}")
                )
            if status in ACTIVE_TASK_STATUSES:
                active_keys[task["work_key"]].append((path, label))

    for work_key, occurrences in sorted(active_keys.items()):
        if len(occurrences) < 2:
            continue
        rendered = ", ".join(
            f"{path.relative_to(ROOT)} ({label})" for path, label in occurrences
        )
        findings.append(
            Finding(occurrences[0][0], f"duplicate active work_key {work_key!r}: {rendered}")
        )

    return findings


def main() -> int:
    findings: list[Finding] = []
    project_paths = sorted(PROJECTS_DIR.glob("*.md")) if PROJECTS_DIR.exists() else []
    for path in project_paths:
        findings.extend(validate_project(path))

    task_paths = sorted(RUNS_DIR.glob("*/tasks.md")) if RUNS_DIR.exists() else []
    findings.extend(validate_tasks(task_paths))

    if findings:
        print("Ideas Hub validation failed:")
        for finding in findings:
            print(f"- {finding.render()}")
        return 1

    print(
        "Ideas Hub validation passed "
        f"({len(project_paths)} project files, {len(task_paths)} task queues checked)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

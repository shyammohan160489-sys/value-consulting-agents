"""JSON file-based deal persistence."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Optional

from ..models.deal import DealBrief
from ..models.output import DealPackage


class DealSummary:
    """Lightweight deal summary for listing."""

    def __init__(self, deal_id: str, client_name: str, deal_type: str,
                 created_at: str, has_package: bool):
        self.deal_id = deal_id
        self.client_name = client_name
        self.deal_type = deal_type
        self.created_at = created_at
        self.has_package = has_package


class DealStore:
    """Persists deals as JSON files in a directory."""

    def __init__(self, deals_dir: Path):
        self.deals_dir = deals_dir
        self.deals_dir.mkdir(parents=True, exist_ok=True)

    def _brief_path(self, deal_id: str) -> Path:
        return self.deals_dir / f"{deal_id}.json"

    def _package_path(self, deal_id: str) -> Path:
        return self.deals_dir / f"{deal_id}_package.json"

    def save_brief(self, brief: DealBrief) -> Path:
        """Save a deal brief as JSON."""
        brief.updated_at = datetime.now().isoformat()
        path = self._brief_path(brief.deal_id)
        path.write_text(brief.model_dump_json(indent=2))
        return path

    def load_brief(self, deal_id: str) -> DealBrief:
        """Load a deal brief by ID."""
        path = self._brief_path(deal_id)
        if not path.exists():
            raise FileNotFoundError(f"Deal not found: {deal_id}")
        return DealBrief.model_validate_json(path.read_text())

    def save_package(self, package: DealPackage) -> Path:
        """Save a complete deal package as JSON."""
        path = self._package_path(package.deal_brief.deal_id)
        path.write_text(package.model_dump_json(indent=2))
        return path

    def load_package(self, deal_id: str) -> DealPackage:
        """Load a complete deal package by ID."""
        path = self._package_path(deal_id)
        if not path.exists():
            raise FileNotFoundError(f"Deal package not found: {deal_id}")
        return DealPackage.model_validate_json(path.read_text())

    def list_deals(self) -> list[DealSummary]:
        """List all saved deals."""
        summaries = []
        for path in sorted(self.deals_dir.glob("*.json")):
            if path.name.endswith("_package.json"):
                continue
            try:
                brief = DealBrief.model_validate_json(path.read_text())
                has_package = self._package_path(brief.deal_id).exists()
                summaries.append(DealSummary(
                    deal_id=brief.deal_id,
                    client_name=brief.client.name,
                    deal_type=brief.deal_type.value,
                    created_at=brief.created_at,
                    has_package=has_package,
                ))
            except Exception:
                continue
        return summaries

    def deal_exists(self, deal_id: str) -> bool:
        """Check if a deal exists."""
        return self._brief_path(deal_id).exists()

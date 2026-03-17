"""Knowledge base loader — reads product cards, benchmarks, and construct patterns."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ..config import get_settings


class KnowledgeBase:
    """Loads and formats knowledge base content for injection into agent prompts."""

    def __init__(self, kb_dir: Path | None = None):
        settings = get_settings()
        self.kb_dir = kb_dir or settings.project_root / "knowledge_base"
        self._products: dict[str, str] = {}
        self._benchmarks: dict[str, Any] = {}
        self._construct_patterns: dict[str, Any] = {}
        self._deal_constructs_md: str = ""
        self._negotiation_md: str = ""
        self._loaded = False

    def load(self) -> None:
        """Load all knowledge base files."""
        if self._loaded:
            return

        # Product cards (markdown)
        products_dir = self.kb_dir / "products"
        if products_dir.exists():
            for md_file in sorted(products_dir.glob("*.md")):
                self._products[md_file.stem] = md_file.read_text()

        # Benchmarks (JSON)
        benchmarks_dir = self.kb_dir / "benchmarks"
        if benchmarks_dir.exists():
            seg_path = benchmarks_dir / "segment_benchmarks.json"
            if seg_path.exists():
                self._benchmarks = json.loads(seg_path.read_text())
            pat_path = benchmarks_dir / "construct_patterns.json"
            if pat_path.exists():
                self._construct_patterns = json.loads(pat_path.read_text())

        # Deal construct templates (markdown)
        templates_dir = self.kb_dir / "templates"
        constructs_path = templates_dir / "deal_constructs.md"
        if constructs_path.exists():
            self._deal_constructs_md = constructs_path.read_text()

        # Negotiation best practices (markdown)
        nego_path = templates_dir / "negotiation_best_practices.md"
        if nego_path.exists():
            self._negotiation_md = nego_path.read_text()

        self._loaded = True

    # ── Context builders for agent prompts ──────────────────────

    def get_product_context(self, module_names: list[str] | None = None) -> str:
        """Build product knowledge context string for agent prompts."""
        self.load()
        if not self._products:
            return ""

        sections = []
        for name, content in self._products.items():
            if module_names and name not in module_names:
                continue
            sections.append(content)

        if not sections:
            sections = list(self._products.values())

        return "--- PRODUCT KNOWLEDGE ---\n\n" + "\n\n".join(sections)

    def get_benchmark_context(self, segments: list[str] | None = None) -> str:
        """Build benchmark context string for agent prompts."""
        self.load()
        if not self._benchmarks:
            return ""

        lines = ["--- SEGMENT BENCHMARKS ---\n"]
        for seg, data in self._benchmarks.items():
            if segments and seg not in segments:
                continue
            lines.append(f"**{seg.upper()}**")
            lines.append(f"  ARPU range: ${data['arpu_range'][0]:.2f} – ${data['arpu_range'][1]:.2f}/user/year")
            lines.append(f"  Typical ARR: ${data['typical_arr_k'][0]}K – ${data['typical_arr_k'][1]}K")
            lines.append(f"  ARR growth: {data['typical_arr_growth_pct']}%")
            lines.append(f"  Margin: {data['margin_range_pct'][0]}% – {data['margin_range_pct'][1]}%")
            lines.append(f"  ROI: {data['roi_range_pct'][0]}% – {data['roi_range_pct'][1]}%")
            lines.append(f"  Payback: {data['payback_years'][0]} – {data['payback_years'][1]} years")
            lines.append(f"  Notes: {data['notes']}")
            lines.append("")

        return "\n".join(lines)

    def get_construct_patterns_context(self, deal_type: str | None = None) -> str:
        """Build construct pattern context for the strategist agent."""
        self.load()
        if not self._construct_patterns:
            return ""

        lines = ["--- CONSTRUCT SELECTION PATTERNS ---\n"]

        # Deal type defaults
        defaults = self._construct_patterns.get("deal_type_defaults", {})
        if deal_type and deal_type in defaults:
            lines.append(f"Default constructs for {deal_type}: {', '.join(defaults[deal_type])}")
            lines.append("")

        # Situational patterns
        patterns = self._construct_patterns.get("patterns", {})
        for name, pat in patterns.items():
            lines.append(f"**{name}**: {pat['rationale']}")
            lines.append(f"  Recommended: {', '.join(pat['recommended'])}")
            if pat.get("avoid"):
                lines.append(f"  Avoid: {', '.join(pat['avoid'])}")
            lines.append("")

        return "\n".join(lines)

    def get_construct_definitions_context(self) -> str:
        """Return the full construct definitions markdown."""
        self.load()
        if self._deal_constructs_md:
            return "--- CONSTRUCT DEFINITIONS ---\n\n" + self._deal_constructs_md
        return ""

    def get_negotiation_context(self) -> str:
        """Return negotiation best practices for the narrator/strategist."""
        self.load()
        if self._negotiation_md:
            return "--- NEGOTIATION BEST PRACTICES ---\n\n" + self._negotiation_md
        return ""

    def get_full_context(
        self,
        segments: list[str] | None = None,
        deal_type: str | None = None,
        modules: list[str] | None = None,
        include_negotiation: bool = False,
    ) -> str:
        """Build complete knowledge context for an agent."""
        parts = [
            self.get_product_context(modules),
            self.get_benchmark_context(segments),
            self.get_construct_patterns_context(deal_type),
            self.get_construct_definitions_context(),
        ]
        if include_negotiation:
            parts.append(self.get_negotiation_context())
        return "\n\n".join(p for p in parts if p)


# Module-level singleton
_kb: KnowledgeBase | None = None


def get_knowledge_base() -> KnowledgeBase:
    """Get or create the knowledge base singleton."""
    global _kb
    if _kb is None:
        _kb = KnowledgeBase()
    return _kb

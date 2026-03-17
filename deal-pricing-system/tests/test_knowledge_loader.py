"""Tests for the knowledge base loader."""

from pathlib import Path

import pytest

from deal_pricing.knowledge.loader import KnowledgeBase


@pytest.fixture
def kb():
    """Knowledge base pointing to the actual knowledge_base directory."""
    project_root = Path(__file__).parent.parent
    kb = KnowledgeBase(project_root / "knowledge_base")
    kb.load()
    return kb


class TestKnowledgeBase:
    def test_load_products(self, kb):
        ctx = kb.get_product_context()
        assert "Digital Banking" in ctx
        assert "Lending" in ctx
        assert "Assist" in ctx

    def test_load_products_filtered(self, kb):
        ctx = kb.get_product_context(module_names=["digital_banking"])
        assert "Digital Banking" in ctx
        # Should not include unrelated products when filtered
        # (Unless filter doesn't match, in which case all are returned)

    def test_load_benchmarks(self, kb):
        ctx = kb.get_benchmark_context()
        assert "RETAIL" in ctx
        assert "ARPU range" in ctx
        assert "WEALTH" in ctx

    def test_load_benchmarks_filtered(self, kb):
        ctx = kb.get_benchmark_context(segments=["retail"])
        assert "RETAIL" in ctx

    def test_load_construct_patterns(self, kb):
        ctx = kb.get_construct_patterns_context()
        assert "CONSTRUCT SELECTION PATTERNS" in ctx
        assert "flat_block" in ctx

    def test_load_construct_patterns_by_deal_type(self, kb):
        ctx = kb.get_construct_patterns_context(deal_type="renewal")
        assert "renewal" in ctx

    def test_construct_definitions(self, kb):
        ctx = kb.get_construct_definitions_context()
        assert "Flat Block" in ctx
        assert "Milestone" in ctx
        assert "Floor" in ctx

    def test_full_context(self, kb):
        ctx = kb.get_full_context(
            segments=["retail"],
            deal_type="renewal",
        )
        assert len(ctx) > 500  # Should be substantial
        assert "PRODUCT KNOWLEDGE" in ctx
        assert "SEGMENT BENCHMARKS" in ctx
        assert "CONSTRUCT SELECTION PATTERNS" in ctx

    def test_negotiation_context(self, kb):
        ctx = kb.get_negotiation_context()
        assert "NEGOTIATION BEST PRACTICES" in ctx
        assert "Martini" in ctx
        assert "Concession" in ctx

    def test_2025_editions_in_products(self, kb):
        ctx = kb.get_product_context()
        assert "2025" in ctx or "Essential" in ctx  # editions_2025.md loaded

    def test_full_context_with_negotiation(self, kb):
        ctx = kb.get_full_context(
            segments=["retail"],
            deal_type="renewal",
            include_negotiation=True,
        )
        assert "NEGOTIATION BEST PRACTICES" in ctx

    def test_base_fee_tiered_in_construct_patterns(self, kb):
        ctx = kb.get_construct_patterns_context(deal_type="renewal")
        assert "base_fee_tiered" in ctx

    def test_idempotent_load(self, kb):
        """Loading twice should be a no-op."""
        kb.load()
        kb.load()
        ctx = kb.get_product_context()
        assert "Digital Banking" in ctx

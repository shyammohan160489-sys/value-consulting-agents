"""Tests for output renderers."""

import tempfile
from pathlib import Path

import pytest

from deal_pricing.engine.financial_engine import compute_deal
from deal_pricing.models.output import (
    DealContext,
    DealNarrative,
    DealPackage,
    NextStep,
    ObjectionResponse,
)
from deal_pricing.models.pricing import ConstructType, PricingStrategy
from deal_pricing.output.html_renderer import render_html


@pytest.fixture
def sample_package(retail_renewal_brief, flat_block_construct, milestone_ramp_construct):
    """Build a complete DealPackage for testing output."""
    strategy = PricingStrategy(
        recommended=flat_block_construct,
        alternative=milestone_ramp_construct,
        rationale="Block pricing for ARR predictability.",
        key_trade_offs=["Simplicity vs. lower entry cost"],
    )
    financials = compute_deal(retail_renewal_brief, strategy)

    context = DealContext(
        deal_classification="Large retail renewal with expansion",
        baseline_summary="Test Bank currently spends $800K/year.",
        baseline_arr=800_000,
        baseline_per_user=0.53,
        client_pressure_points=["Budget approval", "Audit complexity"],
        backbase_pressure_points=["ARR growth", "Cross-sell"],
        strategic_considerations=["High growth market"],
        relevant_benchmarks=["Retail ARPU $1.50-$5.00"],
        recommended_construct_types=[ConstructType.FLAT_BLOCK, ConstructType.MILESTONE_RAMP],
    )

    narrative = DealNarrative(
        executive_summary="Test Bank is a high-growth retail bank. We recommend block pricing for predictable ARR.",
        deal_context_recap="Test Bank renewal with expansion into Assist.",
        construct_explanation="Block pricing charges a fixed price per block of 500K users.",
        objections=[
            ObjectionResponse(
                objection="Why block pricing?",
                response="Eliminates per-user audits and provides budget predictability.",
                supporting_data="Industry benchmark: 60% of large renewals use block pricing.",
            ),
        ],
        next_steps=[
            NextStep(step="Internal review", owner="Backbase", timeline="Week 1", deliverables=["Pricing memo"]),
            NextStep(step="Client presentation", owner="Joint", timeline="Week 2-3", deliverables=["Deck"]),
        ],
    )

    return DealPackage(
        deal_brief=retail_renewal_brief,
        deal_context=context,
        pricing_strategy=strategy,
        financials=financials,
        narrative=narrative,
    )


class TestHTMLRenderer:
    def test_render_html(self, sample_package):
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "test_deal.html"
            result = render_html(sample_package, output_path)

            assert result.exists()
            html = result.read_text()

            # Check key content is present
            assert "Test Bank" in html
            assert "Executive Summary" in html
            assert "Financial Projections" in html
            assert "Objection Handling" in html
            assert "Next Steps" in html
            assert "Block Pricing" in html

    def test_html_contains_financials(self, sample_package):
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "test_deal.html"
            render_html(sample_package, output_path)
            html = output_path.read_text()

            # Should contain year rows
            assert "Y1" in html
            assert "Y5" in html


class TestExcelRenderer:
    def test_render_excel(self, sample_package):
        try:
            from deal_pricing.output.excel_renderer import render_excel
        except ImportError:
            pytest.skip("openpyxl not installed")

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "test_deal.xlsx"
            result = render_excel(sample_package, output_path)
            assert result.exists()
            assert result.stat().st_size > 0


class TestDealPackageSerialization:
    def test_package_json_roundtrip(self, sample_package):
        json_str = sample_package.model_dump_json()
        restored = DealPackage.model_validate_json(json_str)

        assert restored.deal_brief.deal_id == sample_package.deal_brief.deal_id
        assert restored.deal_context.deal_classification == "Large retail renewal with expansion"
        assert len(restored.financials.recommended.yearly) == 5
        assert restored.narrative.executive_summary.startswith("Test Bank")

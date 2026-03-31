"""AI pricing engine tests — unit tests, stress tests, and Schroders regression."""

import math
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from deal_pricing.engine.ai_pricing_engine import (
    catalog_to_selections,
    compute_ai_pricing,
    compute_bic_consumption,
    compute_build_it_yourself_cost,
    compute_if_domain_pricing,
    compute_raw_inference_cost,
    load_agent_catalog,
    load_bic_reference,
    load_pillar_definitions,
)
from deal_pricing.models.ai_pricing import (
    AIAgentSelection,
    AIPillar,
    AIPricingConfig,
    BICConsumption,
)


# ─── Unit Tests ─────────────────────────────────────────────────


class TestCatalogLoading:
    def test_load_wealth_catalog(self):
        agents = load_agent_catalog("wealth")
        assert len(agents) == 10
        ids = [a.agent_id for a in agents]
        assert "review-prep-copilot" in ids
        assert "periodic-review" in ids

    def test_load_retail_catalog(self):
        agents = load_agent_catalog("retail")
        assert len(agents) >= 8

    def test_load_commercial_catalog(self):
        agents = load_agent_catalog("commercial")
        assert len(agents) >= 6

    def test_load_nonexistent_domain(self):
        agents = load_agent_catalog("nonexistent")
        assert agents == []

    def test_bic_reference_loads(self):
        ref = load_bic_reference()
        assert "bic_model" in ref
        assert "if_domain_base" in ref
        assert "bic_blocks" in ref

    def test_pillar_definitions_loads(self):
        defs = load_pillar_definitions()
        assert "pillars" in defs
        assert "embedded_ai" in defs["pillars"]
        assert "conversational_engine" in defs["pillars"]
        assert "process_automation" in defs["pillars"]


class TestBICConsumption:
    def test_single_agent(self):
        agents = [AIAgentSelection(
            agent_id="test",
            bic_weight=1.0,
            monthly_volume_per_user=10.0,
        )]
        bic = compute_bic_consumption(agents, user_count=100)
        # 1.0 × 10.0 × 100 × 12 = 12,000
        assert bic.total_annual_bics == 12000.0
        assert bic.blocks_required == 1

    def test_multiple_agents(self):
        agents = [
            AIAgentSelection(agent_id="a", bic_weight=2.0, monthly_volume_per_user=5.0),
            AIAgentSelection(agent_id="b", bic_weight=0.5, monthly_volume_per_user=20.0),
        ]
        bic = compute_bic_consumption(agents, user_count=100)
        # a: 2.0 × 5.0 × 100 × 12 = 12,000
        # b: 0.5 × 20.0 × 100 × 12 = 12,000
        assert bic.total_annual_bics == 24000.0
        assert bic.per_agent_annual_bics["a"] == 12000.0
        assert bic.per_agent_annual_bics["b"] == 12000.0

    def test_volume_override(self):
        agents = [AIAgentSelection(
            agent_id="test",
            bic_weight=1.0,
            monthly_volume_per_user=10.0,
            volume_override=50.0,
        )]
        bic = compute_bic_consumption(agents, user_count=100)
        # 1.0 × 50.0 × 100 × 12 = 60,000
        assert bic.total_annual_bics == 60000.0

    def test_zero_users(self):
        agents = [AIAgentSelection(agent_id="test", bic_weight=1.0, monthly_volume_per_user=10.0)]
        bic = compute_bic_consumption(agents, user_count=0)
        assert bic.total_annual_bics == 0.0
        assert bic.blocks_required == 0

    def test_block_calculation(self):
        agents = [AIAgentSelection(
            agent_id="test",
            bic_weight=1.0,
            monthly_volume_per_user=100.0,
        )]
        # 1.0 × 100 × 500 × 12 = 600,000 → 3 blocks of 250K
        bic = compute_bic_consumption(agents, user_count=500)
        assert bic.blocks_required == 3


class TestRawInferenceCost:
    def test_basic_cost(self):
        agents = [AIAgentSelection(
            agent_id="test",
            monthly_volume_per_user=10.0,
            raw_cost_per_action_usd=0.01,
        )]
        total, per_agent = compute_raw_inference_cost(agents, user_count=100)
        # 10.0 × 100 × 12 × 0.01 = 120.0
        assert total == 120.0
        assert per_agent["test"] == 120.0


class TestIFDomainPricing:
    def test_entry_tier(self):
        bic = BICConsumption(total_annual_bics=500000, blocks_required=2, block_size=250000)
        ifp = compute_if_domain_pricing(bic, raw_compute_annual=5000.0, domain_tier="entry")
        assert ifp.domain_base_annual_usd == 250000
        # 1 first block ($45K) + 1 additional ($39K) = $84K
        assert ifp.bic_blocks_annual_usd == 84000.0
        assert ifp.compute_passthrough_annual_usd == 5750.0  # 5000 × 1.15

    def test_standard_tier(self):
        bic = BICConsumption(total_annual_bics=250000, blocks_required=1, block_size=250000)
        ifp = compute_if_domain_pricing(bic, raw_compute_annual=3000.0, domain_tier="standard")
        assert ifp.domain_base_annual_usd == 350000
        assert ifp.bic_blocks_annual_usd == 45000.0  # 1 first block

    def test_three_layer_ordering(self):
        """Platform price must always be between raw compute and build-it-yourself."""
        bic = BICConsumption(total_annual_bics=500000, blocks_required=2, block_size=250000)
        ifp = compute_if_domain_pricing(bic, raw_compute_annual=5000.0)
        # Raw < Platform is guaranteed by domain base + blocks
        assert 5000.0 < ifp.total_if_annual_usd


class TestBuildItYourself:
    def test_nonzero_cost(self):
        agents = [AIAgentSelection(
            agent_id="test",
            bic_weight=3.5,  # complex
            monthly_volume_per_user=10.0,
        )]
        cost = compute_build_it_yourself_cost(agents, user_count=100)
        assert cost > 0

    def test_scales_with_agents(self):
        simple = [AIAgentSelection(agent_id="a", bic_weight=0.5, monthly_volume_per_user=10.0)]
        complex_ = [
            AIAgentSelection(agent_id="a", bic_weight=0.5, monthly_volume_per_user=10.0),
            AIAgentSelection(agent_id="b", bic_weight=5.0, monthly_volume_per_user=10.0),
        ]
        cost_1 = compute_build_it_yourself_cost(simple, 100)
        cost_2 = compute_build_it_yourself_cost(complex_, 100)
        assert cost_2 > cost_1


# ─── Schroders Regression ──────────────────────────────────────


class TestSchrodersRegression:
    """Validates against the Schroders deal: 225 advisors, wealth, 10 agents, ~£350-400K/yr."""

    def setup_method(self):
        catalog = load_agent_catalog("wealth")
        self.selections = catalog_to_selections(catalog)
        self.config = AIPricingConfig(
            pillars=[AIPillar.EMBEDDED_AI, AIPillar.PROCESS_AUTOMATION],
            selected_agents=self.selections,
            if_domain_tier="standard",  # Schroders used standard (~£199K base ≈ $350K)
            compute_markup_pct=15.0,
            ai_activation_year=2,
            currency="GBP",
            fx_rate=0.79,
        )
        self.result = compute_ai_pricing(self.config, user_count=225, domain="wealth")

    def test_agent_count(self):
        assert self.result.total_agents == 10

    def test_bic_consumption_range(self):
        """Schroders: ~602K BICs Phase 2, ~648K Phase 3."""
        total = self.result.bic_consumption.total_annual_bics
        assert 400000 < total < 800000, f"BICs {total} outside expected range"

    def test_raw_compute_under_15k(self):
        """Schroders: raw compute was ~£9K/yr (~$11K)."""
        assert self.result.raw_compute_annual_usd < 15000

    def test_platform_price_in_range_gbp(self):
        """Schroders target: £350-400K/yr."""
        gbp = self.result.if_pricing.total_if_annual_usd * 0.79
        assert 300000 < gbp < 500000, f"Platform £{gbp:,.0f} outside £300-500K range"

    def test_three_layer_ordering(self):
        """Raw compute < Platform price < Build-it-yourself."""
        assert self.result.raw_compute_annual_usd < self.result.platform_price_annual_usd
        assert self.result.platform_price_annual_usd < self.result.build_it_yourself_annual_usd

    def test_five_year_ramp(self):
        """Year 1 = 0 (AI not active), Year 2 = ramp, Year 3-5 = steady state."""
        rev = self.result.five_year_ai_revenue
        assert rev[0] == 0.0  # Year 1: no AI
        assert rev[1] > 0.0  # Year 2: ramp
        assert rev[2] > rev[1]  # Year 3: full
        assert rev[3] == rev[2]  # Year 4: steady
        assert rev[4] == rev[2]  # Year 5: steady


# ─── Stress Tests: Scale × Domain ──────────────────────────────


SCALE_POINTS = [50, 225, 500, 2000, 5000]
DOMAINS = ["retail", "wealth", "commercial"]


class TestStressScale:
    """Validates pricing model across different user counts."""

    @pytest.mark.parametrize("user_count", SCALE_POINTS)
    @pytest.mark.parametrize("domain", DOMAINS)
    def test_three_layer_ordering(self, user_count, domain):
        """Raw < Platform < BIY at every scale point."""
        config = AIPricingConfig(
            pillars=[AIPillar.EMBEDDED_AI, AIPillar.PROCESS_AUTOMATION],
            if_domain_tier="entry",
        )
        result = compute_ai_pricing(config, user_count=user_count, domain=domain)
        assert result.raw_compute_annual_usd < result.platform_price_annual_usd, \
            f"Raw ({result.raw_compute_annual_usd}) >= Platform ({result.platform_price_annual_usd}) at {user_count} users/{domain}"
        assert result.platform_price_annual_usd < result.build_it_yourself_annual_usd, \
            f"Platform ({result.platform_price_annual_usd}) >= BIY ({result.build_it_yourself_annual_usd}) at {user_count} users/{domain}"

    @pytest.mark.parametrize("user_count", SCALE_POINTS)
    @pytest.mark.parametrize("domain", DOMAINS)
    def test_positive_values(self, user_count, domain):
        """All pricing components must be positive."""
        config = AIPricingConfig(if_domain_tier="entry")
        result = compute_ai_pricing(config, user_count=user_count, domain=domain)
        assert result.raw_compute_annual_usd > 0
        assert result.platform_price_annual_usd > 0
        assert result.build_it_yourself_annual_usd > 0
        assert result.bic_consumption.total_annual_bics > 0
        assert result.total_agents > 0

    @pytest.mark.parametrize("user_count", SCALE_POINTS)
    def test_per_user_cost_decreases_with_scale(self, user_count):
        """Per-user AI cost should be higher at small scale (fixed cost spread)."""
        config = AIPricingConfig(if_domain_tier="entry")
        small = compute_ai_pricing(config, user_count=50, domain="retail")
        large = compute_ai_pricing(config, user_count=5000, domain="retail")
        assert small.per_user_ai_cost_annual_usd > large.per_user_ai_cost_annual_usd

    @pytest.mark.parametrize("domain", DOMAINS)
    def test_bic_scales_linearly_with_users(self, domain):
        """BIC consumption should scale roughly linearly with user count."""
        config = AIPricingConfig(if_domain_tier="entry")
        r100 = compute_ai_pricing(config, user_count=100, domain=domain)
        r200 = compute_ai_pricing(config, user_count=200, domain=domain)
        ratio = r200.bic_consumption.total_annual_bics / r100.bic_consumption.total_annual_bics
        assert 1.9 < ratio < 2.1, f"BIC ratio {ratio} not ~2x for {domain}"


class TestStressExtreme:
    """Edge cases and extreme inputs."""

    def test_single_user(self):
        config = AIPricingConfig(if_domain_tier="entry")
        result = compute_ai_pricing(config, user_count=1, domain="wealth")
        assert result.raw_compute_annual_usd > 0
        assert result.platform_price_annual_usd > 0

    def test_large_scale(self):
        config = AIPricingConfig(if_domain_tier="enterprise")
        result = compute_ai_pricing(config, user_count=10000, domain="retail")
        assert result.raw_compute_annual_usd > 0
        assert result.bic_consumption.blocks_required > 10

    def test_custom_agent_subset(self):
        """Only select 3 agents from the catalog."""
        catalog = load_agent_catalog("wealth")
        selections = catalog_to_selections(catalog[:3])
        config = AIPricingConfig(
            selected_agents=selections,
            if_domain_tier="entry",
        )
        result = compute_ai_pricing(config, user_count=225, domain="wealth")
        assert result.total_agents == 3

    def test_volume_override(self):
        """Override volume for one agent."""
        catalog = load_agent_catalog("wealth")
        selections = catalog_to_selections(catalog[:1])
        selections[0].volume_override = 100.0  # 10x normal
        config = AIPricingConfig(selected_agents=selections, if_domain_tier="entry")
        result = compute_ai_pricing(config, user_count=225, domain="wealth")
        # Should have much higher BIC consumption
        assert result.bic_consumption.total_annual_bics > 500000


class TestStressMargins:
    """Validates margin protection across all scenarios."""

    @pytest.mark.parametrize("user_count", SCALE_POINTS)
    @pytest.mark.parametrize("domain", DOMAINS)
    def test_platform_to_compute_ratio_minimum(self, user_count, domain):
        """Platform price must be at least 10x raw compute (domain base ensures this)."""
        config = AIPricingConfig(if_domain_tier="entry")
        result = compute_ai_pricing(config, user_count=user_count, domain=domain)
        assert result.platform_to_compute_ratio >= 10.0, \
            f"Ratio {result.platform_to_compute_ratio}x < 10x at {user_count} users/{domain}"

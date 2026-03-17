"""Tests for the financial engine and construct calculators."""

import pytest

from deal_pricing.engine.constructs import (
    compute_all_you_can_eat,
    compute_base_fee_tiered,
    compute_cross_sell_bundle,
    compute_dual_track,
    compute_flat_block,
    compute_floor_kicker,
    compute_milestone_ramp,
)
from deal_pricing.engine.financial_engine import compute_baseline, compute_deal, compute_scenario
from deal_pricing.models.pricing import ConstructType, PricingConstruct, PricingStrategy


class TestFlatBlock:
    def test_basic_block_calculation(self, retail_renewal_brief, flat_block_construct):
        yearly = compute_flat_block(retail_renewal_brief, flat_block_construct)

        assert len(yearly) == 5

        # Year 1: 1.5M users / 500K block = 3 blocks → 3 * 250K = 750K
        assert yearly[0].users == 1_500_000
        assert yearly[0].digital_banking_revenue == 750_000

        # Year 5: 3M users / 500K block = 6 blocks → 6 * 250K = 1.5M
        assert yearly[4].users == 3_000_000
        assert yearly[4].digital_banking_revenue == 1_500_000

    def test_block_boundary(self, retail_renewal_brief, flat_block_construct):
        """Users just over a block boundary should trigger next block."""
        yearly = compute_flat_block(retail_renewal_brief, flat_block_construct)

        # Year 3: 2.2M users → ceil(2.2M / 500K) = 5 blocks → $1.25M
        assert yearly[2].digital_banking_revenue == 1_250_000

    def test_assist_revenue_included(self, retail_renewal_brief, flat_block_construct):
        yearly = compute_flat_block(retail_renewal_brief, flat_block_construct)
        # 800 employees * $400/employee = $320K
        assert yearly[0].assist_revenue == 320_000

    def test_services_year_1_vs_ongoing(self, retail_renewal_brief, flat_block_construct):
        yearly = compute_flat_block(retail_renewal_brief, flat_block_construct)
        assert yearly[0].services_revenue == 300_000  # Y1
        assert yearly[1].services_revenue == 75_000   # Y2 ongoing


class TestMilestoneRamp:
    def test_ramp_multipliers(self, retail_renewal_brief, milestone_ramp_construct):
        yearly = compute_milestone_ramp(retail_renewal_brief, milestone_ramp_construct)

        # Year 1: 1.5M users * $3.00 * 0.7 = $3.15M
        assert yearly[0].digital_banking_revenue == pytest.approx(3_150_000, rel=0.01)

        # Year 2: 1.8M users * $3.00 * 0.85 = $4.59M
        assert yearly[1].digital_banking_revenue == pytest.approx(4_590_000, rel=0.01)

        # Year 3: 2.2M users * $3.00 * 1.0 = $6.6M
        assert yearly[2].digital_banking_revenue == pytest.approx(6_600_000, rel=0.01)

    def test_per_user_cost_decreasing(self, retail_renewal_brief, milestone_ramp_construct):
        """Per-user cost should decrease as ramp multiplier stays at 1.0 and users grow."""
        yearly = compute_milestone_ramp(retail_renewal_brief, milestone_ramp_construct)

        # Y3 to Y5 all have 1.0 multiplier but growing users → flat rate
        # The total per-user cost includes assist + services, which dilute as users grow
        # DB rate stays at $3/user, so per-user should move toward $3 at scale
        assert yearly[4].per_user_cost < yearly[2].per_user_cost


class TestFloorKicker:
    def test_below_threshold(self, new_logo_brief, floor_kicker_construct):
        """When users below threshold, only floor is charged."""
        yearly = compute_floor_kicker(new_logo_brief, floor_kicker_construct)

        # Year 1: 50K users < 500K threshold → floor = $1M
        assert yearly[0].digital_banking_revenue == 1_000_000

    def test_above_threshold(self, new_logo_brief, floor_kicker_construct):
        """When users exceed threshold, kicker kicks in."""
        # Modify to force above-threshold scenario
        from deal_pricing.models.deal import DemandProfile
        brief = new_logo_brief.model_copy()
        brief.demand = DemandProfile(
            current_active_users=0,
            year_1_users=600_000,
            year_2_users=800_000,
            year_3_users=1_000_000,
        )
        yearly = compute_floor_kicker(brief, floor_kicker_construct)

        # Year 1: 600K > 500K → 1M + (600K - 500K) * $1.5 = $1.15M
        assert yearly[0].digital_banking_revenue == pytest.approx(1_150_000, rel=0.01)


class TestAllYouCanEat:
    def test_flat_fee_within_cap(self, retail_renewal_brief, ayce_construct):
        yearly = compute_all_you_can_eat(retail_renewal_brief, ayce_construct)

        # All years within 3M user cap → flat $1.5M
        for y in yearly:
            assert y.digital_banking_revenue == 1_500_000

    def test_overage_above_cap(self, retail_renewal_brief, ayce_construct):
        """Users exceeding cap should trigger overage."""
        from deal_pricing.models.deal import DemandProfile
        brief = retail_renewal_brief.model_copy()
        brief.demand = DemandProfile(
            current_active_users=3_000_000,
            year_1_users=3_500_000,
        )
        yearly = compute_all_you_can_eat(brief, ayce_construct)

        # Year 1: 3.5M > 3M cap → 1.5M + (500K * $0.5) = $1.75M
        assert yearly[0].digital_banking_revenue == pytest.approx(1_750_000, rel=0.01)


class TestDualTrack:
    def test_with_track_definitions(self, retail_renewal_brief):
        construct = PricingConstruct(
            construct_type=ConstructType.DUAL_TRACK,
            label="Dual Track",
            description="Retail + Business tracks",
            licensing_logic="Separate tracks",
            track_definitions={
                "retail": {"rate": 2.0, "users": 1_000_000},
                "business": {"rate": 8.0, "users": 50_000, "start_year": 2},
            },
            services_year_1=200_000,
            services_ongoing_annual=50_000,
        )
        yearly = compute_dual_track(retail_renewal_brief, construct)

        # Year 1: only retail → 1M * $2 = $2M
        assert yearly[0].digital_banking_revenue == 2_000_000

        # Year 2: retail + business → 1M*2 + 50K*8 = $2.4M
        assert yearly[1].digital_banking_revenue == 2_400_000

    def test_fallback_per_user(self, retail_renewal_brief):
        """Without track_definitions, falls back to per-user."""
        construct = PricingConstruct(
            construct_type=ConstructType.DUAL_TRACK,
            label="Simple",
            description="Per user fallback",
            licensing_logic="Per user",
            digital_banking_rate=3.0,
            services_year_1=0,
            services_ongoing_annual=0,
        )
        yearly = compute_dual_track(retail_renewal_brief, construct)
        # Year 1: 1.5M * $3 = $4.5M
        assert yearly[0].digital_banking_revenue == 4_500_000


class TestCrossSellBundle:
    def test_bundle_pricing(self, retail_renewal_brief):
        construct = PricingConstruct(
            construct_type=ConstructType.CROSS_SELL_BUNDLE,
            label="Bundle",
            description="DB + Premium bundle",
            licensing_logic="Per-user bundle rate",
            digital_banking_rate=3.50,
            assist_rate=400,
            add_on_rates={"banking_premium": 150_000, "identity": 100_000},
            services_year_1=200_000,
            services_ongoing_annual=50_000,
        )
        yearly = compute_cross_sell_bundle(retail_renewal_brief, construct)

        # Year 1: 1.5M * $3.50 = $5.25M (DB) + $320K (assist) + $250K (add-ons)
        assert yearly[0].digital_banking_revenue == 5_250_000
        assert yearly[0].assist_revenue == 320_000
        assert yearly[0].add_on_revenue == 250_000
        assert yearly[0].license_revenue == pytest.approx(5_820_000, rel=0.01)


class TestFinancialEngine:
    def test_compute_baseline_existing(self, retail_renewal_brief):
        model = compute_baseline(retail_renewal_brief)

        assert model.scenario_label == "Current Baseline"
        assert len(model.yearly) == 5
        assert all(y.license_revenue == 800_000 for y in model.yearly)
        assert model.total_deal_value_5yr == 4_000_000

    def test_compute_baseline_new_logo(self, new_logo_brief):
        model = compute_baseline(new_logo_brief)
        assert all(y.license_revenue == 0 for y in model.yearly)

    def test_compute_scenario(self, retail_renewal_brief, flat_block_construct):
        model = compute_scenario(retail_renewal_brief, flat_block_construct, "Test Scenario")

        assert model.scenario_label == "Test Scenario"
        assert model.construct_type == ConstructType.FLAT_BLOCK
        assert model.total_deal_value_5yr > 0
        assert model.arr_year_1 > 0
        assert model.arr_year_5 > model.arr_year_1  # Growing deal

    def test_compute_deal(self, retail_renewal_brief, flat_block_construct, milestone_ramp_construct):
        strategy = PricingStrategy(
            recommended=flat_block_construct,
            alternative=milestone_ramp_construct,
            rationale="Block for predictability",
            key_trade_offs=["Simplicity vs. lower entry"],
        )
        comparison = compute_deal(retail_renewal_brief, strategy)

        assert comparison.baseline.scenario_label == "Current Baseline"
        assert comparison.recommended.scenario_label == "Recommended"
        assert comparison.alternative is not None
        assert comparison.alternative.scenario_label == "Alternative"
        assert comparison.arr_uplift_pct > 0  # Should uplift over baseline

    def test_compute_deal_no_alternative(self, retail_renewal_brief, flat_block_construct):
        strategy = PricingStrategy(
            recommended=flat_block_construct,
            rationale="Only one option",
        )
        comparison = compute_deal(retail_renewal_brief, strategy)
        assert comparison.alternative is None


class TestBaseFeeTiered:
    """Tests for the 2025 Base Fee + Tiered Users construct."""

    def test_within_included_users(self, retail_renewal_brief):
        """When users are within the included tier, only base fee applies."""
        from deal_pricing.models.deal import DemandProfile
        brief = retail_renewal_brief.model_copy()
        brief.demand = DemandProfile(
            current_active_users=10_000,
            year_1_users=15_000,
        )
        construct = PricingConstruct(
            construct_type=ConstructType.BASE_FEE_TIERED,
            label="Essential Edition",
            description="2025 Essential with base fee",
            licensing_logic="Base fee + tiered additional users",
            edition="essential",
            base_fee=494_400,
            included_users=20_000,
            tiered_user_rates=[
                {"up_to": 100_000, "rate": 6.52},
                {"up_to": 500_000, "rate": 3.20},
                {"up_to": 1_000_000, "rate": 1.02},
            ],
            services_year_1=0,
            services_ongoing_annual=0,
        )
        yearly = compute_base_fee_tiered(brief, construct)

        # 15K users < 20K included → only base fee
        assert yearly[0].digital_banking_revenue == 494_400

    def test_tiered_additional_users(self, retail_renewal_brief):
        """Users beyond included tier should be charged at tiered rates."""
        construct = PricingConstruct(
            construct_type=ConstructType.BASE_FEE_TIERED,
            label="Essential Edition",
            description="2025 Essential with base fee",
            licensing_logic="Base fee + tiered additional users",
            edition="essential",
            base_fee=494_400,
            included_users=20_000,
            tiered_user_rates=[
                {"up_to": 100_000, "rate": 6.52},
                {"up_to": 500_000, "rate": 3.20},
                {"up_to": 1_000_000, "rate": 1.02},
            ],
            services_year_1=200_000,
            services_ongoing_annual=50_000,
        )
        yearly = compute_base_fee_tiered(retail_renewal_brief, construct)

        # Year 1: 1.5M users, 20K included → 1.48M additional users
        # Tier 1 (up to 100K → 80K capacity): 80K * $6.52 = $521,600
        # Tier 2 (up to 500K → 400K capacity): 400K * $3.20 = $1,280,000
        # Tier 3 (up to 1M → 500K capacity): 500K * $1.02 = $510,000
        # Remaining (500K beyond all tiers): 500K * $1.02 = $510,000
        # Total = $494,400 + $521,600 + $1,280,000 + $510,000 + $510,000
        assert yearly[0].digital_banking_revenue > 494_400  # More than just base fee
        assert yearly[0].services_revenue == 200_000  # Year 1 services

    def test_base_fee_always_present(self, retail_renewal_brief):
        """Base fee should apply every year regardless of user count."""
        construct = PricingConstruct(
            construct_type=ConstructType.BASE_FEE_TIERED,
            label="Premium Edition",
            description="2025 Premium",
            licensing_logic="Base fee + tiered",
            edition="premium",
            base_fee=607_360,
            included_users=20_000,
            tiered_user_rates=[{"up_to": 500_000, "rate": 5.0}],
            services_year_1=0,
            services_ongoing_annual=0,
        )
        yearly = compute_base_fee_tiered(retail_renewal_brief, construct)

        # All years should have at least the base fee
        for y in yearly:
            assert y.digital_banking_revenue >= 607_360

    def test_registered_in_engine(self, retail_renewal_brief):
        """BASE_FEE_TIERED should work via compute_scenario."""
        construct = PricingConstruct(
            construct_type=ConstructType.BASE_FEE_TIERED,
            label="Essential",
            description="2025 model",
            licensing_logic="Base fee + tiered",
            base_fee=494_400,
            included_users=20_000,
            tiered_user_rates=[{"up_to": 500_000, "rate": 3.0}],
            services_year_1=100_000,
            services_ongoing_annual=25_000,
        )
        model = compute_scenario(retail_renewal_brief, construct, "2025 Test")
        assert model.scenario_label == "2025 Test"
        assert model.construct_type == ConstructType.BASE_FEE_TIERED
        assert model.total_deal_value_5yr > 0


class TestBreakeven:
    """Tests for breakeven calculation."""

    def test_breakeven_computed(self, retail_renewal_brief, flat_block_construct):
        model = compute_scenario(retail_renewal_brief, flat_block_construct, "Test")
        # Services Y1 = 300K, ARR Y1 = license revenue
        # breakeven = services_y1 / (arr_y1 / 12)
        assert model.breakeven_months is not None
        assert model.breakeven_months > 0

    def test_breakeven_zero_services(self, retail_renewal_brief):
        """No services = no breakeven (nothing to recoup)."""
        construct = PricingConstruct(
            construct_type=ConstructType.FLAT_BLOCK,
            label="No Services",
            description="Test",
            licensing_logic="Test",
            digital_banking_block_size=500_000,
            digital_banking_block_price=250_000,
            services_year_1=0,
            services_ongoing_annual=0,
        )
        model = compute_scenario(retail_renewal_brief, construct, "Test")
        # With 0 services, breakeven should be 0 or None
        assert model.breakeven_months is None or model.breakeven_months == 0


class TestComparator:
    def test_format_currency(self):
        from deal_pricing.engine.comparator import format_currency

        assert format_currency(1_500_000) == "$2M" or "M" in format_currency(1_500_000)
        assert "K" in format_currency(500_000)
        assert "$" in format_currency(50)

    def test_summarize_comparison(self, retail_renewal_brief, flat_block_construct):
        strategy = PricingStrategy(
            recommended=flat_block_construct,
            rationale="Test",
        )
        comparison = compute_deal(retail_renewal_brief, strategy)

        from deal_pricing.engine.comparator import summarize_comparison
        summary = summarize_comparison(comparison)

        assert "Baseline ARR" in summary
        assert "Recommended ARR (Y1)" in summary
        assert "5-Year Deal Value" in summary

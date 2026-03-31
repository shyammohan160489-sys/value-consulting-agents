"""Tests for data models."""

import json

import pytest

from deal_pricing.models.deal import (
    BankingSegment,
    ClientProfile,
    DealBrief,
    DealConstraints,
    DealType,
    DemandProfile,
    HostingModel,
    ModuleScope,
)
from deal_pricing.models.financial import FinancialModel, ScenarioComparison, YearlyBreakdown
from deal_pricing.models.output import DealPackage
from deal_pricing.models.pricing import ConstructType, PricingConstruct, PricingStrategy


class TestDemandProfile:
    def test_get_user_ramp_complete(self):
        d = DemandProfile(
            current_active_users=100,
            year_1_users=200,
            year_2_users=300,
            year_3_users=400,
            year_4_users=500,
            year_5_users=600,
        )
        assert d.get_user_ramp() == [200, 300, 400, 500, 600]

    def test_get_user_ramp_with_gaps(self):
        d = DemandProfile(
            current_active_users=100,
            year_1_users=200,
            year_3_users=400,
            year_5_users=600,
        )
        # Gaps filled by carry-forward
        ramp = d.get_user_ramp()
        assert ramp == [200, 200, 400, 400, 600]

    def test_get_user_ramp_all_none(self):
        d = DemandProfile(current_active_users=1000)
        assert d.get_user_ramp() == [1000, 1000, 1000, 1000, 1000]


class TestModuleScope:
    def test_all_modules_deduplication(self):
        m = ModuleScope(
            currently_licensed=["digital_banking", "onboarding"],
            proposed_additions=["digital_banking", "assist"],
        )
        assert set(m.all_modules) == {"digital_banking", "onboarding", "assist"}


class TestDealBrief:
    def test_serialization_roundtrip(self, retail_renewal_brief):
        json_str = retail_renewal_brief.model_dump_json()
        restored = DealBrief.model_validate_json(json_str)
        assert restored.deal_id == retail_renewal_brief.deal_id
        assert restored.client.name == "Test Bank"
        assert restored.demand.get_user_ramp() == [1_500_000, 1_800_000, 2_200_000, 2_600_000, 3_000_000]

    def test_auto_deal_id(self):
        brief = DealBrief(
            deal_type=DealType.NEW_LOGO,
            client=ClientProfile(
                name="X", region="EU", country="NL",
                segments=[BankingSegment.RETAIL],
            ),
            demand=DemandProfile(),
            scope=ModuleScope(),
            constraints=DealConstraints(),
        )
        assert brief.deal_id.startswith("DEAL-")
        assert len(brief.deal_id) == 13  # DEAL- + 8 hex chars


class TestFinancialModel:
    def test_compute_aggregates(self):
        yearly = [
            YearlyBreakdown(year=1, users=100, license_revenue=1000, services_revenue=500,
                           total_revenue=1500, per_user_cost=10, arr=1000),
            YearlyBreakdown(year=2, users=200, license_revenue=2000, services_revenue=100,
                           total_revenue=2100, per_user_cost=10, arr=2000),
        ]
        model = FinancialModel(
            scenario_label="Test",
            construct_type=ConstructType.FLAT_BLOCK,
            yearly=yearly,
        )
        model.compute_aggregates()

        assert model.total_license_5yr == 3000
        assert model.total_services_5yr == 600
        assert model.total_deal_value_5yr == 3600
        assert model.arr_year_1 == 1000
        assert model.arr_year_5 == 2000  # last year
        assert model.arr_cagr == pytest.approx(1.0, rel=0.01)  # 100% growth


class TestScenarioComparison:
    def test_compute_deltas(self):
        base_yearly = [YearlyBreakdown(year=1, users=100, license_revenue=1000, services_revenue=0,
                                       total_revenue=1000, per_user_cost=10, arr=1000)]
        rec_yearly = [YearlyBreakdown(year=1, users=100, license_revenue=1500, services_revenue=200,
                                      total_revenue=1700, per_user_cost=15, arr=1500)]

        base = FinancialModel(scenario_label="Base", construct_type=ConstructType.FLAT_BLOCK, yearly=base_yearly)
        rec = FinancialModel(scenario_label="Rec", construct_type=ConstructType.FLAT_BLOCK, yearly=rec_yearly)
        base.compute_aggregates()
        rec.compute_aggregates()

        comp = ScenarioComparison(baseline=base, recommended=rec)
        comp.compute_deltas()

        assert comp.arr_uplift_pct == pytest.approx(50.0)
        assert comp.arr_uplift_abs == 500
        assert comp.per_user_delta_year1 == 5


class TestPricingConstruct:
    def test_flat_block_fields(self, flat_block_construct):
        assert flat_block_construct.construct_type == ConstructType.FLAT_BLOCK
        assert flat_block_construct.digital_banking_block_size == 500_000
        assert flat_block_construct.digital_banking_block_price == 250_000

    def test_ramp_schedule_fields(self, milestone_ramp_construct):
        assert milestone_ramp_construct.ramp_schedule["1"] == 0.7
        assert milestone_ramp_construct.ramp_schedule["3"] == 1.0

    def test_base_fee_tiered_fields(self):
        from deal_pricing.models.pricing import EditionTier
        construct = PricingConstruct(
            construct_type=ConstructType.BASE_FEE_TIERED,
            label="Essential 2025",
            description="2025 edition model",
            licensing_logic="Base fee + tiered users",
            edition=EditionTier.ESSENTIAL,
            base_fee=494_400,
            included_users=20_000,
            tiered_user_rates=[
                {"up_to": 100_000, "rate": 6.52},
                {"up_to": 500_000, "rate": 3.20},
            ],
            hosting_embedded=True,
        )
        assert construct.construct_type == ConstructType.BASE_FEE_TIERED
        assert construct.base_fee == 494_400
        assert construct.included_users == 20_000
        assert len(construct.tiered_user_rates) == 2
        assert construct.hosting_embedded is True

    def test_negotiation_plan(self):
        from deal_pricing.models.pricing import ConcessionMove, NegotiationPlan
        plan = NegotiationPlan(
            opening_offer=["Full list price", "5-year term"],
            planned_concessions=[
                ConcessionMove(lever="pricing_tiers", description="10% tier discount", value_impact="-$50K ARR"),
            ],
            final_exec_give="Additional 3-month payment deferral",
            walk_away_terms=["Minimum 3-year commitment"],
            give_to_get_requirements=["Commitment to 5-year term", "Reference case study"],
        )
        assert len(plan.opening_offer) == 2
        assert len(plan.planned_concessions) == 1
        assert plan.final_exec_give is not None


class TestDemandFirmness:
    def test_demand_firmness_default(self):
        from deal_pricing.models.deal import DemandFirmness
        d = DemandProfile()
        assert d.demand_firmness == DemandFirmness.PROJECTED

    def test_demand_firmness_validated(self):
        from deal_pricing.models.deal import DemandFirmness
        d = DemandProfile(demand_firmness=DemandFirmness.VALIDATED)
        assert d.demand_firmness == DemandFirmness.VALIDATED


class TestDealConstraintsNew:
    def test_license_activation_default(self):
        from deal_pricing.models.deal import DealConstraints, LicenseActivation
        c = DealConstraints()
        assert c.license_activation == LicenseActivation.STAGGERED

    def test_renewal_cap(self):
        from deal_pricing.models.deal import DealConstraints
        c = DealConstraints(renewal_cap_pct=5.0, payment_terms="net-60")
        assert c.renewal_cap_pct == 5.0
        assert c.payment_terms == "net-60"


class TestProposalStoryline:
    def test_storyline_fields(self):
        from deal_pricing.models.output import ProposalStoryline
        s = ProposalStoryline(
            mutual_journey="Shared vision for digital transformation.",
            pricing_options_summary="Two options: Edition model and milestone ramp.",
            business_case="Breakeven in 14 months.",
            reasons_to_believe=["150+ implementations", "Top-3 Gartner"],
        )
        assert "Shared vision" in s.mutual_journey
        assert len(s.reasons_to_believe) == 2

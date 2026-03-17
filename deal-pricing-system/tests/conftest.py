"""Shared test fixtures."""

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
from deal_pricing.models.pricing import ConstructType, PricingConstruct, PricingStrategy


@pytest.fixture
def retail_renewal_brief() -> DealBrief:
    """A realistic retail renewal deal brief."""
    return DealBrief(
        deal_id="DEAL-TEST0001",
        deal_type=DealType.RENEWAL,
        client=ClientProfile(
            name="Test Bank",
            region="APAC",
            country="Indonesia",
            segments=[BankingSegment.RETAIL],
            institution_size_users=2_000_000,
            institution_size_employees=3_500,
            is_existing_customer=True,
            current_annual_spend=800_000,
        ),
        demand=DemandProfile(
            current_active_users=1_200_000,
            year_1_users=1_500_000,
            year_2_users=1_800_000,
            year_3_users=2_200_000,
            year_4_users=2_600_000,
            year_5_users=3_000_000,
            assist_employees=800,
        ),
        scope=ModuleScope(
            currently_licensed=["digital_banking", "onboarding"],
            proposed_additions=["assist", "banking_premium"],
            hosting_model=HostingModel.MANAGED,
        ),
        constraints=DealConstraints(
            client_concerns=["Budget", "Audit complexity"],
            arr_uplift_target_min=15,
            arr_uplift_target_max=30,
            preferred_contract_years=5,
        ),
    )


@pytest.fixture
def new_logo_brief() -> DealBrief:
    """A new logo deal brief with zero baseline."""
    return DealBrief(
        deal_id="DEAL-TEST0002",
        deal_type=DealType.NEW_LOGO,
        client=ClientProfile(
            name="New Bank Co",
            region="Europe",
            country="Sweden",
            segments=[BankingSegment.WEALTH, BankingSegment.RETAIL],
            institution_size_users=150_000,
            is_existing_customer=False,
            current_annual_spend=0,
        ),
        demand=DemandProfile(
            current_active_users=0,
            year_1_users=50_000,
            year_2_users=80_000,
            year_3_users=120_000,
            year_4_users=140_000,
            year_5_users=150_000,
            assist_employees=400,
            lending_aum=5_000_000_000,
        ),
        scope=ModuleScope(
            currently_licensed=[],
            proposed_additions=["digital_banking", "assist", "lending", "onboarding"],
            hosting_model=HostingModel.MANAGED,
        ),
        constraints=DealConstraints(
            preferred_contract_years=5,
        ),
    )


@pytest.fixture
def flat_block_construct() -> PricingConstruct:
    """A flat block pricing construct."""
    return PricingConstruct(
        construct_type=ConstructType.FLAT_BLOCK,
        label="Block Pricing",
        description="Fixed price per 500K user block",
        licensing_logic="Blocks of 500K users at $250K/block",
        digital_banking_block_size=500_000,
        digital_banking_block_price=250_000,
        assist_rate=400,
        services_year_1=300_000,
        services_ongoing_annual=75_000,
        pros_client=["Predictable"],
        pros_backbase=["ARR protection"],
        cons_client=["Overpay if under-utilized"],
        cons_backbase=["Capped within block"],
    )


@pytest.fixture
def milestone_ramp_construct() -> PricingConstruct:
    """A milestone ramp pricing construct."""
    return PricingConstruct(
        construct_type=ConstructType.MILESTONE_RAMP,
        label="Ramp Pricing",
        description="70% → 85% → 100% ramp over 3 years",
        licensing_logic="Per-user with year-based multiplier",
        digital_banking_rate=3.0,
        ramp_schedule={"1": 0.7, "2": 0.85, "3": 1.0, "4": 1.0, "5": 1.0},
        assist_rate=400,
        services_year_1=300_000,
        services_ongoing_annual=75_000,
        pros_client=["Lower entry"],
        pros_backbase=["Win competitive deal"],
        cons_client=["Rising costs"],
        cons_backbase=["Lower Y1 ARR"],
    )


@pytest.fixture
def floor_kicker_construct() -> PricingConstruct:
    """A floor + kicker pricing construct."""
    return PricingConstruct(
        construct_type=ConstructType.FLOOR_KICKER,
        label="Floor + Kicker",
        description="$1M floor with $1.50 kicker above 500K users",
        licensing_logic="Minimum ARR floor plus per-user kicker",
        floor_amount=1_000_000,
        kicker_threshold=500_000,
        kicker_rate=1.5,
        assist_rate=400,
        services_year_1=300_000,
        services_ongoing_annual=75_000,
        pros_client=["Growth optionality"],
        pros_backbase=["ARR floor"],
        cons_client=["Variable cost"],
        cons_backbase=["Capped if low growth"],
    )


@pytest.fixture
def ayce_construct() -> PricingConstruct:
    """An all-you-can-eat pricing construct."""
    return PricingConstruct(
        construct_type=ConstructType.ALL_YOU_CAN_EAT,
        label="All-You-Can-Eat",
        description="Flat $1.5M/year regardless of user count",
        licensing_logic="Fixed annual license fee",
        ayce_annual_fee=1_500_000,
        ayce_user_cap=3_000_000,
        kicker_rate=0.5,
        assist_rate=400,
        services_year_1=300_000,
        services_ongoing_annual=75_000,
        pros_client=["Simple", "No audits"],
        pros_backbase=["Predictable ARR"],
        cons_client=["Overpay at low usage"],
        cons_backbase=["Miss upside"],
    )

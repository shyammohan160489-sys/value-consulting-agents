"""Financial engine — orchestrates construct calculators and comparisons.

All computation is deterministic Python. No LLM involvement.
"""

from __future__ import annotations

from ..models.deal import DealBrief
from ..models.financial import FinancialModel, ScenarioComparison, YearlyBreakdown
from ..models.pricing import ConstructType, PricingConstruct, PricingStrategy
from .constructs import (
    compute_all_you_can_eat,
    compute_base_fee_tiered,
    compute_cross_sell_bundle,
    compute_dual_track,
    compute_flat_block,
    compute_floor_kicker,
    compute_milestone_ramp,
)

# Map construct types to their calculator functions
CONSTRUCT_CALCULATORS = {
    ConstructType.FLAT_BLOCK: compute_flat_block,
    ConstructType.MILESTONE_RAMP: compute_milestone_ramp,
    ConstructType.ALL_YOU_CAN_EAT: compute_all_you_can_eat,
    ConstructType.FLOOR_KICKER: compute_floor_kicker,
    ConstructType.DUAL_TRACK: compute_dual_track,
    ConstructType.CROSS_SELL_BUNDLE: compute_cross_sell_bundle,
    ConstructType.REGIONAL_STRUCTURE: compute_dual_track,  # regional uses dual-track mechanics
    ConstructType.BASE_FEE_TIERED: compute_base_fee_tiered,  # 2025 model
}


def compute_scenario(
    brief: DealBrief,
    construct: PricingConstruct,
    label: str,
) -> FinancialModel:
    """Compute a complete 5-year financial model for one scenario.

    Args:
        brief: Validated deal brief with user ramp and scope.
        construct: Pricing construct with rates and parameters.
        label: Human-readable scenario label.

    Returns:
        FinancialModel with yearly breakdowns and aggregates.
    """
    calculator = CONSTRUCT_CALCULATORS.get(construct.construct_type)
    if not calculator:
        raise ValueError(f"No calculator for construct type: {construct.construct_type}")

    yearly = calculator(brief, construct)

    model = FinancialModel(
        scenario_label=label,
        construct_type=construct.construct_type,
        yearly=yearly,
    )
    model.compute_aggregates()
    return model


def compute_baseline(brief: DealBrief) -> FinancialModel:
    """Compute a baseline financial model from current spend.

    If the client is existing, baseline = current spend projected flat.
    If new logo, baseline is zero (no current spend).
    """
    user_ramp = brief.demand.get_user_ramp()
    current_spend = brief.client.current_annual_spend or 0.0

    yearly = []
    for i, users in enumerate(user_ramp):
        year = i + 1
        yearly.append(YearlyBreakdown(
            year=year,
            users=users,
            license_revenue=round(current_spend, 2),
            services_revenue=0.0,
            total_revenue=round(current_spend, 2),
            per_user_cost=round(current_spend / users, 2) if users > 0 else 0.0,
            arr=round(current_spend, 2),
        ))

    model = FinancialModel(
        scenario_label="Current Baseline",
        construct_type=ConstructType.FLAT_BLOCK,  # baseline is always flat
        yearly=yearly,
    )
    model.compute_aggregates()
    return model


def compute_deal(
    brief: DealBrief,
    strategy: PricingStrategy,
) -> ScenarioComparison:
    """Compute complete deal financials: baseline + recommended + alternative.

    This is the main entry point for the financial engine.

    Args:
        brief: Validated deal brief.
        strategy: Pricing strategy from the strategist agent.

    Returns:
        ScenarioComparison with all scenarios and deltas.
    """
    baseline = compute_baseline(brief)
    recommended = compute_scenario(brief, strategy.recommended, "Recommended")

    alternative = None
    if strategy.alternative:
        alternative = compute_scenario(brief, strategy.alternative, "Alternative")

    comparison = ScenarioComparison(
        baseline=baseline,
        recommended=recommended,
        alternative=alternative,
    )
    comparison.compute_deltas()
    return comparison

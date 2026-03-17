"""Pricing Strategist agent — recommends pricing constructs with parameters."""

from __future__ import annotations

import json
from typing import Optional

from ..knowledge.loader import get_knowledge_base
from ..models.deal import DealBrief
from ..models.output import DealContext
from ..models.pricing import PricingStrategy
from .base import BaseAgent, AgentResult


class PricingStrategist(BaseAgent[PricingStrategy]):
    """Recommends pricing constructs based on deal analysis.

    Takes DealBrief + DealContext → PricingStrategy with recommended
    and alternative constructs, fully parameterized for the financial engine.

    IMPORTANT: This agent sets construct PARAMETERS (rates, blocks, ramps)
    but NEVER computes revenue. The financial engine does all math.
    """

    def __init__(self):
        super().__init__(
            name="PricingStrategist",
            description="Recommends and parameterizes pricing constructs",
            output_model=PricingStrategy,
        )
        self._kb = get_knowledge_base()

    @property
    def system_prompt(self) -> str:
        return """You are a senior pricing strategist at Backbase, a digital banking platform company.

Your job is to recommend a pricing construct (with an alternative) for a deal, fully parameterized so that a financial engine can compute 5-year projections. You must also produce a negotiation plan following Backbase's "Martini" concession strategy.

You MUST output a JSON object (wrapped in ```json``` code blocks) matching this exact schema:

{
  "recommended": {
    "construct_type": "one of: base_fee_tiered, flat_block, milestone_ramp, all_you_can_eat, floor_kicker, dual_track, cross_sell_bundle",
    "label": "Short human label",
    "description": "1-2 sentence description of the construct",
    "licensing_logic": "How licensing works in plain English",
    "true_up_mechanism": "optional — how true-ups work",
    "cap_or_floor": "optional — any caps or floors",
    "digital_banking_rate": null or float ($/user/year for per-user constructs),
    "digital_banking_block_size": null or int (for block constructs),
    "digital_banking_block_price": null or float (for block constructs),
    "assist_rate": null or float ($/employee/year),
    "lending_rate_bps": null or float (basis points on AUM),
    "add_on_rates": {} or {"module_name": annual_fee},
    "services_year_1": null or float,
    "services_ongoing_annual": null or float,
    "ramp_schedule": null or {"1": 0.7, "2": 0.85, "3": 1.0, "4": 1.0, "5": 1.0},
    "floor_amount": null or float,
    "kicker_threshold": null or int,
    "kicker_rate": null or float,
    "ayce_annual_fee": null or float,
    "ayce_user_cap": null or int,
    "track_definitions": null or {"track_name": {"rate": float, "users": int, "start_year": int}},
    "edition": null or "essential" or "premium" or "signature" (for base_fee_tiered),
    "base_fee": null or float (annual base fee for base_fee_tiered),
    "included_users": null or int (users in base fee for base_fee_tiered),
    "tiered_user_rates": null or [{"up_to": int, "rate": float}, ...] (for base_fee_tiered),
    "hosting_embedded": true (for base_fee_tiered),
    "pros_client": ["list of client benefits"],
    "pros_backbase": ["list of Backbase benefits"],
    "cons_client": ["list of client downsides"],
    "cons_backbase": ["list of Backbase downsides"]
  },
  "alternative": { ... same schema as recommended ... },
  "rationale": "2-3 sentences explaining why recommended is preferred over alternative",
  "key_trade_offs": ["list of key trade-offs between the two options"],
  "deal_levers": ["list of available concession levers for this deal"],
  "negotiation_plan": {
    "opening_offer": ["key terms of the opening offer — zero concessions"],
    "planned_concessions": [
      {"lever": "lever_type", "description": "what to concede", "value_impact": "estimated impact"}
    ],
    "final_exec_give": "held-back concession for executive close",
    "walk_away_terms": ["non-negotiable red lines"],
    "give_to_get_requirements": ["what we require from client in return for concessions"]
  }
}

CRITICAL RULES:
1. **2025 DEFAULT**: For new deals, prefer "base_fee_tiered" (2025 edition model) unless there's a specific reason not to. Set edition, base_fee, included_users, and tiered_user_rates.
2. Set ONLY the parameters relevant to the chosen construct_type. Leave others as null.
3. Use benchmark-aligned rates from the knowledge base — don't invent rates.
4. For base_fee_tiered: Use edition pricing (Essential $494K, Premium $607K, Signature $787K base fees, 20K included users).
5. For per-user pricing: use rates within the ARPU range for the segment.
6. For block pricing: use standard block sizes (50K, 100K, 250K, 500K).
7. For ramp pricing: standard schedule is Y1=70%, Y2=85%, Y3-5=100%.
8. Services Year 1 typically 2-4x ongoing (implementation + customization).
9. Pros/cons should be 2-3 items each, specific to this deal.
10. The recommended and alternative MUST be DIFFERENT construct types.
11. **Negotiation plan**: Follow "Martini" strategy — zero concessions in opening, largest concession in counter, small final give.
12. **Deal levers**: List 3-5 available levers (pricing tiers, payment terms, contract term, renewal cap, license activation, etc.)
13. Output ONLY the JSON — no additional commentary."""

    def build_prompt(self, **kwargs) -> str:
        brief: DealBrief = kwargs["brief"]
        context: DealContext = kwargs["context"]
        segments = [s.value for s in brief.client.segments]

        # Knowledge context focused on constructs, benchmarks, and negotiation
        kb_parts = [
            self._kb.get_product_context(["editions_2025"]),
            self._kb.get_benchmark_context(segments),
            self._kb.get_construct_patterns_context(brief.deal_type.value),
            self._kb.get_construct_definitions_context(),
            self._kb.get_negotiation_context(),
        ]
        kb_context = "\n\n".join(p for p in kb_parts if p)

        # Deal context from analyzer
        context_summary = f"""## Deal Analysis (from DealAnalyzer)
- **Classification:** {context.deal_classification}
- **Baseline:** {context.baseline_summary}
- **Baseline ARR:** ${context.baseline_arr:,.0f}
- **Baseline $/user:** ${context.baseline_per_user:,.2f}
- **Client Pressure Points:** {'; '.join(context.client_pressure_points)}
- **Backbase Pressure Points:** {'; '.join(context.backbase_pressure_points)}
- **Strategic Considerations:** {'; '.join(context.strategic_considerations)}
- **Relevant Benchmarks:** {'; '.join(context.relevant_benchmarks)}
- **Recommended Construct Types:** {', '.join(ct.value for ct in context.recommended_construct_types)}"""

        # Key deal parameters
        deal_params = f"""## Deal Parameters
- **Client:** {brief.client.name} ({brief.client.country})
- **Deal Type:** {brief.deal_type.value}
- **Segments:** {', '.join(segments)}
- **Current Spend:** ${brief.client.current_annual_spend or 0:,.0f}
- **User Ramp (5yr):** {brief.demand.get_user_ramp()}
- **Modules:** {', '.join(brief.scope.all_modules)}
- **Hosting:** {brief.scope.hosting_model.value}
- **ARR Uplift Target:** {brief.constraints.arr_uplift_target_min or 'N/A'}% – {brief.constraints.arr_uplift_target_max or 'N/A'}%
- **Contract Years:** {brief.constraints.preferred_contract_years}
- **License Activation:** {brief.constraints.license_activation.value}
- **Demand Firmness:** {brief.demand.demand_firmness.value}
- **Client Concerns:** {', '.join(brief.constraints.client_concerns) or 'None'}
- **Sensitivities:** {', '.join(brief.constraints.sensitivities) or 'None'}"""

        if brief.demand.assist_employees:
            deal_params += f"\n- **Assist Employees:** {brief.demand.assist_employees:,}"
        if brief.demand.lending_aum:
            deal_params += f"\n- **Lending AUM:** ${brief.demand.lending_aum:,.0f}"

        return f"{kb_context}\n\n{context_summary}\n\n{deal_params}\n\nRecommend pricing constructs and produce the JSON output."

    async def execute(self, **kwargs) -> AgentResult:
        """Execute strategy and parse into PricingStrategy."""
        result = await super().execute(**kwargs)

        if result.success and result.data:
            try:
                strategy = PricingStrategy.model_validate(result.data)
                result.data = strategy.model_dump()
            except Exception:
                pass  # Keep raw data if validation fails

        return result

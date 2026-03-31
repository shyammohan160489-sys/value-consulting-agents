"""Deal Analyzer agent — classifies deals and identifies pressure points."""

from __future__ import annotations

import json
from typing import Optional

from ..knowledge.loader import get_knowledge_base
from ..models.deal import DealBrief
from ..models.output import DealContext
from .base import BaseAgent, AgentResult


class DealAnalyzer(BaseAgent[DealContext]):
    """Analyzes a deal brief to produce strategic context.

    Outputs: DealContext with classification, pressure points,
    benchmarks, and recommended construct types.
    """

    def __init__(self):
        super().__init__(
            name="DealAnalyzer",
            description="Classifies deals and identifies strategic pressure points",
            output_model=DealContext,
        )
        self._kb = get_knowledge_base()

    @property
    def system_prompt(self) -> str:
        return """You are a senior deal pricing analyst at Backbase, a digital banking platform company.

Your job is to analyze a deal brief and produce a strategic deal context that will inform the pricing strategist.

You MUST output a JSON object (wrapped in ```json``` code blocks) with this exact schema:
{
  "deal_classification": "string — e.g. 'Large retail renewal with expansion opportunity'",
  "baseline_summary": "string — 1-2 sentences describing the current commercial relationship",
  "baseline_arr": 0.0,
  "baseline_per_user": 0.0,
  "client_pressure_points": ["list of client concerns/leverage points"],
  "backbase_pressure_points": ["list of Backbase objectives/leverage points"],
  "strategic_considerations": ["list of key strategic factors for pricing"],
  "relevant_benchmarks": ["list of relevant benchmark data points"],
  "recommended_construct_types": ["list of 2-3 construct type IDs from: flat_block, milestone_ramp, all_you_can_eat, floor_kicker, dual_track, cross_sell_bundle, regional_structure"]
}

Rules:
- Be specific and quantitative where possible
- Reference benchmark data from the knowledge base
- Consider deal type (renewal, expansion, new_logo, upsell) when recommending constructs
- Identify BOTH client and Backbase leverage/pressure points
- Keep each list to 3-5 items max
- Output ONLY the JSON — no additional commentary"""

    def build_prompt(self, **kwargs) -> str:
        brief: DealBrief = kwargs["brief"]
        segments = [s.value for s in brief.client.segments]

        # Build knowledge context
        kb_context = self._kb.get_full_context(
            segments=segments,
            deal_type=brief.deal_type.value,
            modules=brief.scope.all_modules,
        )

        # Build deal summary
        deal_summary = f"""## Deal Brief
- **Deal ID:** {brief.deal_id}
- **Deal Type:** {brief.deal_type.value}
- **Client:** {brief.client.name} ({brief.client.country}, {brief.client.region})
- **Segments:** {', '.join(segments)}
- **Existing Customer:** {'Yes' if brief.client.is_existing_customer else 'No'}
- **Current Annual Spend:** ${brief.client.current_annual_spend:,.0f}
- **Current Users:** {brief.demand.current_active_users or 'N/A'}
- **5-Year User Ramp:** {brief.demand.get_user_ramp()}
- **Licensed Modules:** {', '.join(brief.scope.currently_licensed) or 'None'}
- **Proposed Additions:** {', '.join(brief.scope.proposed_additions) or 'None'}
- **Hosting:** {brief.scope.hosting_model.value}
- **Client Concerns:** {', '.join(brief.constraints.client_concerns) or 'None stated'}
- **ARR Uplift Target:** {brief.constraints.arr_uplift_target_min or 'N/A'}% – {brief.constraints.arr_uplift_target_max or 'N/A'}%
- **Sensitivities:** {', '.join(brief.constraints.sensitivities) or 'None stated'}
- **Contract Years:** {brief.constraints.preferred_contract_years}
- **Notes:** {brief.constraints.notes or 'None'}"""

        if brief.demand.assist_employees:
            deal_summary += f"\n- **Assist Employees:** {brief.demand.assist_employees:,}"
        if brief.demand.lending_aum:
            deal_summary += f"\n- **Lending AUM:** ${brief.demand.lending_aum:,.0f}"

        return f"{kb_context}\n\n{deal_summary}\n\nAnalyze this deal and produce the JSON output."

    async def execute(self, **kwargs) -> AgentResult:
        """Execute analysis and parse into DealContext."""
        result = await super().execute(**kwargs)

        if result.success and result.data:
            try:
                # Validate against the model
                context = DealContext.model_validate(result.data)
                result.data = context.model_dump()
            except Exception:
                pass  # Keep raw data if validation fails

        return result

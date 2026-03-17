"""Deal Narrator agent — generates executive narrative and objection handling."""

from __future__ import annotations

from ..engine.comparator import format_currency, format_pct
from ..models.deal import DealBrief
from ..models.financial import ScenarioComparison
from ..models.output import DealContext, DealNarrative
from ..models.pricing import PricingStrategy
from .base import BaseAgent, AgentResult


class DealNarrator(BaseAgent[DealNarrative]):
    """Generates the narrative layer for a deal package.

    Takes the complete deal analysis, pricing strategy, and financial
    projections and produces executive summaries, objection handling,
    and next steps.
    """

    def __init__(self):
        super().__init__(
            name="DealNarrator",
            description="Generates deal narrative, objection handling, and next steps",
            output_model=DealNarrative,
        )

    @property
    def system_prompt(self) -> str:
        return """You are a senior deal advisor at Backbase, a digital banking platform company.

Your job is to write the narrative layer of a deal package following Backbase's Proposal Storyline structure:
1. Our Journey / Mutual Benefits
2. Pricing Options (2 scenarios)
3. Business Case (breakeven, ROI justification)
4. Case Studies / Reasons to Believe
5. Next Steps (Mutual Close Plan)

You MUST output a JSON object (wrapped in ```json``` code blocks) with this exact schema:

{
  "executive_summary": "3-5 sentences. McKinsey Situation-Complication-Resolution format. Lead with the strategic insight, not the numbers.",
  "deal_context_recap": "2-3 sentences recapping the deal context and why this pricing approach was chosen.",
  "construct_explanation": "3-5 sentences explaining HOW the recommended construct works in plain business language. Avoid jargon. Focus on why it's good for both sides.",
  "proposal_storyline": {
    "mutual_journey": "2-3 sentences anchoring back to what matters most to the customer — the shared journey and mutual benefits.",
    "pricing_options_summary": "2-3 sentences summarizing the 2 pricing scenarios (recommended + alternative) and why we lead with the recommended.",
    "business_case": "2-3 sentences on breakeven timeline, ROI, and investment justification. Target 12-16 month breakeven for CFO appeal.",
    "reasons_to_believe": ["list of 2-3 proof points, case studies, or market data that support the recommendation"]
  },
  "objections": [
    {
      "objection": "The specific objection the client might raise",
      "response": "The recommended response (2-3 sentences)",
      "supporting_data": "Optional data point that reinforces the response"
    }
  ],
  "next_steps": [
    {
      "step": "Specific action item",
      "owner": "Backbase or Client or Joint",
      "timeline": "e.g. 'Week 1', 'Within 2 weeks'",
      "deliverables": ["list of concrete deliverables"]
    }
  ]
}

RULES:
- Executive summary: Use SCR (Situation-Complication-Resolution) structure
- Proposal storyline: Follow the 4-part structure (Journey, Pricing, Business Case, Proof Points)
- Business case MUST reference breakeven timeline (target 12-16 months for CFO appeal)
- Include 3-5 likely objections with prepared responses
- Include 4-6 next steps forming a Mutual Close Plan (per best practices)
- Next steps MUST include: internal review, client presentation, negotiation rounds, exec sign-off, contract execution
- Be specific about timelines and owners
- Reference actual numbers from the financial projections
- Write in a professional but persuasive tone — this is a deal memo, not a report
- Output ONLY the JSON — no additional commentary"""

    def build_prompt(self, **kwargs) -> str:
        brief: DealBrief = kwargs["brief"]
        context: DealContext = kwargs["context"]
        strategy: PricingStrategy = kwargs["strategy"]
        financials: ScenarioComparison = kwargs["financials"]

        rec = financials.recommended
        base = financials.baseline

        # Financial summary
        fin_summary = f"""## Financial Summary
- **Baseline ARR:** {format_currency(base.arr_year_1)}
- **Recommended ARR (Y1):** {format_currency(rec.arr_year_1)}
- **Recommended ARR (Y5):** {format_currency(rec.arr_year_5)}
- **ARR Uplift:** {format_pct(financials.arr_uplift_pct)} ({format_currency(financials.arr_uplift_abs)})
- **5-Year Deal Value:** {format_currency(rec.total_deal_value_5yr)}
- **5-Year Uplift vs Baseline:** {format_currency(financials.total_uplift_abs)}
- **Avg $/User:** {format_currency(rec.avg_per_user_5yr, decimals=2)}
- **ARR CAGR:** {format_pct(rec.arr_cagr * 100)}
- **Breakeven:** {f'{rec.breakeven_months:.0f} months' if rec.breakeven_months else 'N/A'} (target: 12-16 months)"""

        # Year-by-year
        yearly_lines = ["## Year-by-Year Projection (Recommended)"]
        for y in rec.yearly:
            yearly_lines.append(
                f"  Y{y.year}: {y.users:,} users → "
                f"License {format_currency(y.license_revenue)}, "
                f"Total {format_currency(y.total_revenue)}, "
                f"$/user {format_currency(y.per_user_cost, decimals=2)}"
            )

        # Deal context
        ctx_summary = f"""## Deal Context
- **Client:** {brief.client.name} ({brief.client.country})
- **Deal Type:** {brief.deal_type.value}
- **Classification:** {context.deal_classification}
- **Client Pressure Points:** {'; '.join(context.client_pressure_points)}
- **Backbase Pressure Points:** {'; '.join(context.backbase_pressure_points)}"""

        # Pricing construct
        construct_summary = f"""## Recommended Pricing Construct
- **Type:** {strategy.recommended.construct_type.value}
- **Label:** {strategy.recommended.label}
- **Description:** {strategy.recommended.description}
- **Licensing Logic:** {strategy.recommended.licensing_logic}
- **Pros (Client):** {'; '.join(strategy.recommended.pros_client)}
- **Pros (Backbase):** {'; '.join(strategy.recommended.pros_backbase)}
- **Cons (Client):** {'; '.join(strategy.recommended.cons_client)}
- **Cons (Backbase):** {'; '.join(strategy.recommended.cons_backbase)}
- **Rationale:** {strategy.rationale}"""

        # Client concerns
        concerns = f"""## Client Concerns & Sensitivities
- **Concerns:** {', '.join(brief.constraints.client_concerns) or 'None stated'}
- **Sensitivities:** {', '.join(brief.constraints.sensitivities) or 'None stated'}"""

        # Negotiation plan (if available from strategist)
        nego_section = ""
        if strategy.negotiation_plan:
            np = strategy.negotiation_plan
            nego_section = f"""## Negotiation Plan
- **Opening Offer:** {'; '.join(np.opening_offer)}
- **Planned Concessions:** {'; '.join(c.description for c in np.planned_concessions)}
- **Final Exec Give:** {np.final_exec_give or 'TBD'}
- **Give-to-Get:** {'; '.join(np.give_to_get_requirements)}"""

        return "\n\n".join(filter(None, [
            ctx_summary,
            construct_summary,
            fin_summary,
            "\n".join(yearly_lines),
            concerns,
            nego_section,
            "Generate the deal narrative JSON output following the Proposal Storyline structure.",
        ]))

    async def execute(self, **kwargs) -> AgentResult:
        """Execute narration and parse into DealNarrative."""
        result = await super().execute(**kwargs)

        if result.success and result.data:
            try:
                narrative = DealNarrative.model_validate(result.data)
                result.data = narrative.model_dump()
            except Exception:
                pass  # Keep raw data if validation fails

        return result

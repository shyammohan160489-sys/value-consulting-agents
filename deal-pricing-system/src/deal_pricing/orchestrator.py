"""Deal pricing orchestrator — coordinates agents, engine, and output."""

from __future__ import annotations

import asyncio
from typing import Optional

from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

from .agents.deal_analyzer import DealAnalyzer
from .agents.deal_narrator import DealNarrator
from .agents.pricing_strategist import PricingStrategist
from .engine.comparator import build_yearly_table, summarize_comparison
from .engine.financial_engine import compute_deal
from .models.deal import DealBrief
from .models.financial import ScenarioComparison
from .models.output import DealContext, DealNarrative, DealPackage
from .models.pricing import PricingStrategy
from .storage.deal_store import DealStore

console = Console()


class Orchestrator:
    """Coordinates the full deal pricing pipeline.

    Pipeline:
    1. DealAnalyzer → DealContext (LLM)
    2. PricingStrategist → PricingStrategy (LLM)
    3. Financial Engine → ScenarioComparison (Python)
    4. DealNarrator → DealNarrative (LLM)
    5. Assemble → DealPackage
    """

    def __init__(self, store: DealStore):
        self.store = store
        self._analyzer = DealAnalyzer()
        self._strategist = PricingStrategist()
        self._narrator = DealNarrator()

    async def run(self, brief: DealBrief) -> DealPackage:
        """Execute the full deal pricing pipeline."""
        # Save the brief
        self.store.save_brief(brief)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            # Step 1: Analyze the deal
            task = progress.add_task("[cyan]Analyzing deal...", total=None)
            context = await self._step_analyze(brief)
            progress.update(task, description="[green]Deal analysis complete")
            progress.remove_task(task)

            # Step 2: Recommend pricing constructs
            task = progress.add_task("[cyan]Developing pricing strategy...", total=None)
            strategy = await self._step_strategize(brief, context)
            progress.update(task, description="[green]Pricing strategy complete")
            progress.remove_task(task)

            # Step 3: Compute financials (deterministic — instant)
            task = progress.add_task("[cyan]Computing financials...", total=None)
            financials = compute_deal(brief, strategy)
            progress.update(task, description="[green]Financial projections complete")
            progress.remove_task(task)

            # Step 4: Generate narrative
            task = progress.add_task("[cyan]Writing deal narrative...", total=None)
            narrative = await self._step_narrate(brief, context, strategy, financials)
            progress.update(task, description="[green]Narrative complete")
            progress.remove_task(task)

        # Step 5: Assemble the package
        package = DealPackage(
            deal_brief=brief,
            deal_context=context,
            pricing_strategy=strategy,
            financials=financials,
            narrative=narrative,
        )

        # Persist
        self.store.save_package(package)
        return package

    async def _step_analyze(self, brief: DealBrief) -> DealContext:
        """Step 1: Analyze the deal."""
        result = await self._analyzer.execute(brief=brief)

        if not result.success or not result.data:
            console.print(f"[red]Deal analysis failed: {result.error or 'No data returned'}[/red]")
            console.print("[yellow]Using fallback analysis...[/yellow]")
            return self._fallback_context(brief)

        try:
            return DealContext.model_validate(result.data)
        except Exception as e:
            console.print(f"[yellow]Analysis parsing failed ({e}), using fallback...[/yellow]")
            return self._fallback_context(brief)

    async def _step_strategize(self, brief: DealBrief, context: DealContext) -> PricingStrategy:
        """Step 2: Recommend pricing constructs."""
        result = await self._strategist.execute(brief=brief, context=context)

        if not result.success or not result.data:
            console.print(f"[red]Pricing strategy failed: {result.error or 'No data returned'}[/red]")
            console.print("[yellow]Using fallback strategy...[/yellow]")
            return self._fallback_strategy(brief, context)

        try:
            return PricingStrategy.model_validate(result.data)
        except Exception as e:
            console.print(f"[yellow]Strategy parsing failed ({e}), using fallback...[/yellow]")
            return self._fallback_strategy(brief, context)

    async def _step_narrate(
        self,
        brief: DealBrief,
        context: DealContext,
        strategy: PricingStrategy,
        financials: ScenarioComparison,
    ) -> DealNarrative:
        """Step 4: Generate deal narrative."""
        result = await self._narrator.execute(
            brief=brief,
            context=context,
            strategy=strategy,
            financials=financials,
        )

        if not result.success or not result.data:
            console.print(f"[red]Narrative generation failed: {result.error or 'No data returned'}[/red]")
            console.print("[yellow]Using fallback narrative...[/yellow]")
            return self._fallback_narrative(brief, strategy)

        try:
            return DealNarrative.model_validate(result.data)
        except Exception as e:
            console.print(f"[yellow]Narrative parsing failed ({e}), using fallback...[/yellow]")
            return self._fallback_narrative(brief, strategy)

    # ── Fallback generators ─────────────────────────────────────

    def _fallback_context(self, brief: DealBrief) -> DealContext:
        """Generate minimal context when LLM fails."""
        from .models.pricing import ConstructType

        segments = [s.value for s in brief.client.segments]
        users = brief.demand.get_user_ramp()
        current_spend = brief.client.current_annual_spend or 0

        return DealContext(
            deal_classification=f"{brief.deal_type.value.replace('_', ' ').title()} — {brief.client.name}",
            baseline_summary=f"Current annual spend: ${current_spend:,.0f} across {', '.join(segments)} segments.",
            baseline_arr=current_spend,
            baseline_per_user=current_spend / users[0] if users[0] > 0 else 0,
            client_pressure_points=brief.constraints.client_concerns[:3] or ["Budget optimization"],
            backbase_pressure_points=["ARR growth", "Platform stickiness"],
            strategic_considerations=[f"5-year user ramp: {users[0]:,} → {users[-1]:,}"],
            relevant_benchmarks=[],
            recommended_construct_types=[ConstructType.BASE_FEE_TIERED, ConstructType.MILESTONE_RAMP],
        )

    def _fallback_strategy(self, brief: DealBrief, context: DealContext) -> PricingStrategy:
        """Generate minimal strategy when LLM fails."""
        from .models.pricing import ConstructType, PricingConstruct

        users_y1 = brief.demand.get_user_ramp()[0]

        recommended = PricingConstruct(
            construct_type=ConstructType.FLAT_BLOCK,
            label="Block Pricing",
            description="Fixed-price blocks of users for predictable ARR.",
            licensing_logic="Pre-purchased user blocks. Next block activates on boundary crossing.",
            digital_banking_block_size=100_000,
            digital_banking_block_price=250_000,
            services_year_1=200_000,
            services_ongoing_annual=50_000,
            pros_client=["Predictable costs", "No per-user audits"],
            pros_backbase=["ARR predictability", "Block upside on growth"],
            cons_client=["May overpay if under-utilized"],
            cons_backbase=["Capped upside within block"],
        )

        alternative = PricingConstruct(
            construct_type=ConstructType.MILESTONE_RAMP,
            label="Milestone Ramp",
            description="Reduced rates in early years, full pricing at adoption maturity.",
            licensing_logic="Per-user pricing with year-based multiplier ramp.",
            digital_banking_rate=3.0,
            ramp_schedule={"1": 0.7, "2": 0.85, "3": 1.0, "4": 1.0, "5": 1.0},
            services_year_1=200_000,
            services_ongoing_annual=50_000,
            pros_client=["Lower entry cost", "Aligned to adoption curve"],
            pros_backbase=["Competitive entry pricing", "Full rate by Y3"],
            cons_client=["Rising costs each year"],
            cons_backbase=["Lower Y1 ARR"],
        )

        return PricingStrategy(
            recommended=recommended,
            alternative=alternative,
            rationale="Block pricing recommended for ARR predictability. Milestone ramp as alternative if client needs lower Y1 commitment.",
            key_trade_offs=["Predictability vs. lower entry cost", "Block simplicity vs. usage alignment"],
        )

    def _fallback_narrative(self, brief: DealBrief, strategy: PricingStrategy) -> DealNarrative:
        """Generate minimal narrative when LLM fails."""
        from .models.output import NextStep, ObjectionResponse, ProposalStoryline

        return DealNarrative(
            executive_summary=f"Deal pricing recommendation for {brief.client.name} ({brief.deal_type.value.replace('_', ' ')}).",
            deal_context_recap=f"{brief.client.name} is a {', '.join(s.value for s in brief.client.segments)} bank in {brief.client.country}.",
            construct_explanation=f"We recommend {strategy.recommended.label}: {strategy.recommended.description}",
            proposal_storyline=ProposalStoryline(
                mutual_journey=f"Our partnership with {brief.client.name} is built on a shared vision of digital banking transformation.",
                pricing_options_summary=f"We present two options: {strategy.recommended.label} (recommended) and {strategy.alternative.label if strategy.alternative else 'N/A'} (alternative).",
                business_case="Investment breakeven is targeted within 12-16 months, making this an attractive proposition for board approval.",
                reasons_to_believe=["Proven platform with 150+ bank implementations globally"],
            ),
            objections=[
                ObjectionResponse(
                    objection="Why this pricing model over alternatives?",
                    response=strategy.rationale,
                ),
            ],
            next_steps=[
                NextStep(
                    step="Internal deal review and pricing approval",
                    owner="Backbase",
                    timeline="Week 1",
                    deliverables=["Pricing memo", "Financial projections"],
                ),
                NextStep(
                    step="Present proposal to client",
                    owner="Joint",
                    timeline="Week 2-3",
                    deliverables=["Client presentation", "Deal terms sheet"],
                ),
                NextStep(
                    step="Negotiation rounds",
                    owner="Joint",
                    timeline="Week 3-5",
                    deliverables=["Counter-proposal", "Final terms"],
                ),
                NextStep(
                    step="Executive sign-off and contract execution",
                    owner="Joint",
                    timeline="Week 6-8",
                    deliverables=["Signed contract"],
                ),
            ],
        )

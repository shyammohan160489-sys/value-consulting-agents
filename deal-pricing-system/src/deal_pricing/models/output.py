"""Output models — the complete deal package."""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from .deal import DealBrief
from .financial import ScenarioComparison
from .pricing import ConstructType, PricingStrategy


class DealContext(BaseModel):
    """Strategic context from the Deal Analyzer agent."""

    deal_classification: str
    baseline_summary: str
    baseline_arr: float = 0.0
    baseline_per_user: float = 0.0
    client_pressure_points: list[str] = Field(default_factory=list)
    backbase_pressure_points: list[str] = Field(default_factory=list)
    strategic_considerations: list[str] = Field(default_factory=list)
    relevant_benchmarks: list[str] = Field(default_factory=list)
    recommended_construct_types: list[ConstructType] = Field(default_factory=list)


class ObjectionResponse(BaseModel):
    """Pre-emptive objection handling."""

    objection: str
    response: str
    supporting_data: Optional[str] = None


class NextStep(BaseModel):
    """Concrete next step with ownership."""

    step: str
    owner: str
    timeline: str
    deliverables: list[str] = Field(default_factory=list)


class ProposalStoryline(BaseModel):
    """Proposal packaging per best practices: Journey → Pricing → Business Case → Close Plan."""

    mutual_journey: str  # Anchor back to what matters most to customer
    pricing_options_summary: str  # 2 options (recommended + alternative)
    business_case: str  # Justification for the investment (breakeven, ROI)
    reasons_to_believe: list[str] = Field(default_factory=list)  # Case studies / proof points


class DealNarrative(BaseModel):
    """Narrative sections from the Deal Narrator agent."""

    executive_summary: str
    deal_context_recap: str
    construct_explanation: str
    proposal_storyline: Optional[ProposalStoryline] = None
    objections: list[ObjectionResponse] = Field(default_factory=list)
    next_steps: list[NextStep] = Field(default_factory=list)


class DealPackage(BaseModel):
    """The final deliverable — everything needed for the deal memo."""

    deal_brief: DealBrief
    deal_context: DealContext
    pricing_strategy: PricingStrategy
    financials: ScenarioComparison
    narrative: DealNarrative
    generated_at: str = Field(default_factory=lambda: datetime.now().isoformat())

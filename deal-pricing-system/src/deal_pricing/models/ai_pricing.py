"""AI pricing models — Intelligence Fabric, BIC, and pillar-based pricing."""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class AIPillar(str, Enum):
    """The three pillars of the Backbase AI strategy, plus BYO."""
    EMBEDDED_AI = "embedded_ai"
    CONVERSATIONAL_ENGINE = "conversational_engine"
    PROCESS_AUTOMATION = "process_automation"
    BYO_PLATFORM = "byo_platform"


class AIAgentComplexity(str, Enum):
    """Agent complexity for build-it-yourself cost estimation."""
    SIMPLE = "simple"
    MEDIUM = "medium"
    COMPLEX = "complex"


class AIAgent(BaseModel):
    """An AI agent from the domain catalog."""

    agent_id: str
    name: str
    pillar: AIPillar
    category: str
    description: str = ""
    bic_weight: float
    monthly_volume_per_user: float
    avg_tokens_per_action: int = 0
    model_routing: str = "claude-sonnet"
    raw_cost_per_action_usd: float = 0.0
    phase: int = 1
    value_narrative: str = ""

    @property
    def complexity(self) -> AIAgentComplexity:
        """Derive complexity from BIC weight."""
        if self.bic_weight <= 1.0:
            return AIAgentComplexity.SIMPLE
        elif self.bic_weight <= 3.0:
            return AIAgentComplexity.MEDIUM
        return AIAgentComplexity.COMPLEX


class AIAgentSelection(BaseModel):
    """A selected agent with optional volume overrides."""

    agent_id: str
    name: str = ""
    pillar: AIPillar = AIPillar.EMBEDDED_AI
    bic_weight: float = 1.0
    monthly_volume_per_user: float = 0.0
    avg_tokens_per_action: int = 0
    model_routing: str = "claude-sonnet"
    raw_cost_per_action_usd: float = 0.0
    phase: int = 1

    # Overrides — if set, take precedence over catalog values
    volume_override: Optional[float] = None
    bic_weight_override: Optional[float] = None

    @property
    def effective_volume(self) -> float:
        return self.volume_override if self.volume_override is not None else self.monthly_volume_per_user

    @property
    def effective_bic_weight(self) -> float:
        return self.bic_weight_override if self.bic_weight_override is not None else self.bic_weight

    @property
    def complexity(self) -> AIAgentComplexity:
        w = self.effective_bic_weight
        if w <= 1.0:
            return AIAgentComplexity.SIMPLE
        elif w <= 3.0:
            return AIAgentComplexity.MEDIUM
        return AIAgentComplexity.COMPLEX


class BICConsumption(BaseModel):
    """BIC consumption breakdown."""

    total_annual_bics: float = 0.0
    per_agent_annual_bics: dict[str, float] = Field(default_factory=dict)
    blocks_required: int = 0
    block_size: int = 250000


class IFDomainPricing(BaseModel):
    """Intelligence Fabric domain pricing — the three layers."""

    # Layer 1: Domain Base (fixed)
    domain_base_tier: str = "entry"
    domain_base_annual_usd: float = 0.0

    # Layer 2: BIC Blocks (consumption-based)
    bic_blocks_count: int = 0
    bic_blocks_annual_usd: float = 0.0
    total_bics_allocated: float = 0.0

    # Layer 3: Compute Pass-through
    raw_compute_annual_usd: float = 0.0
    compute_markup_pct: float = 15.0
    compute_passthrough_annual_usd: float = 0.0

    @property
    def total_if_annual_usd(self) -> float:
        return self.domain_base_annual_usd + self.bic_blocks_annual_usd + self.compute_passthrough_annual_usd


class PillarPricingResult(BaseModel):
    """Pricing result for a single pillar."""

    pillar: AIPillar
    pricing_model: str = ""
    annual_usd: float = 0.0
    detail: dict = Field(default_factory=dict)


class AIPricingConfig(BaseModel):
    """Input configuration for AI pricing calculation."""

    # Which pillars to price
    pillars: list[AIPillar] = Field(default_factory=list)

    # Agent selections (from catalog or custom)
    selected_agents: list[AIAgentSelection] = Field(default_factory=list)

    # IF configuration
    if_domain_tier: str = "entry"  # entry, standard, enterprise
    compute_markup_pct: float = 15.0

    # Conversational engine config
    conversational_tier: str = "entry"  # entry, critical, enterprise
    employee_workspace_monthly_interactions: Optional[int] = None
    conversational_banking_monthly_interactions: Optional[int] = None

    # BYO config
    byo_tier: Optional[str] = None  # standard, enterprise
    byo_custom_agent_count: int = 0

    # Phasing
    ai_activation_year: int = 2  # year AI goes live (1-5)

    # Currency
    currency: str = "USD"
    fx_rate: float = 1.0  # multiply USD by this to get target currency


class AIPricingResult(BaseModel):
    """Complete AI pricing output — the three-layer model."""

    # Three-layer transparency (mandatory)
    raw_compute_annual_usd: float = 0.0
    platform_price_annual_usd: float = 0.0
    build_it_yourself_annual_usd: float = 0.0

    # IF domain pricing breakdown
    if_pricing: Optional[IFDomainPricing] = None

    # BIC consumption
    bic_consumption: Optional[BICConsumption] = None

    # Per-pillar breakdown
    pillar_results: list[PillarPricingResult] = Field(default_factory=list)

    # Per-agent detail
    agent_annual_bics: dict[str, float] = Field(default_factory=dict)
    agent_annual_compute: dict[str, float] = Field(default_factory=dict)

    # Summary metrics
    per_user_ai_cost_annual_usd: float = 0.0
    per_user_ai_cost_monthly_usd: float = 0.0
    platform_to_compute_ratio: float = 0.0
    total_agents: int = 0

    # 5-year projection
    five_year_ai_revenue: list[float] = Field(default_factory=list)

    # Currency output
    currency: str = "USD"
    fx_rate: float = 1.0

    @property
    def platform_price_local(self) -> float:
        return self.platform_price_annual_usd * self.fx_rate

    @property
    def raw_compute_local(self) -> float:
        return self.raw_compute_annual_usd * self.fx_rate

    @property
    def build_it_yourself_local(self) -> float:
        return self.build_it_yourself_annual_usd * self.fx_rate

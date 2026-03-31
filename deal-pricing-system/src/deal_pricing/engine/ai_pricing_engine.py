"""AI pricing engine — pure Python, deterministic.

Computes Intelligence Fabric pricing using the three-layer model:
  Layer 1: IF Domain Base (fixed annual fee)
  Layer 2: BIC Blocks (consumption-based, pre-purchased)
  Layer 3: Compute Pass-through (raw LLM cost + orchestration margin)

Also computes per-pillar pricing (conversational engine per-interaction,
process automation per-execution) and build-it-yourself cost anchors.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Optional

from ..models.ai_pricing import (
    AIAgent,
    AIAgentComplexity,
    AIAgentSelection,
    AIPillar,
    AIPricingConfig,
    AIPricingResult,
    BICConsumption,
    IFDomainPricing,
    PillarPricingResult,
)


# ─── Reference Data Loading ────────────────────────────────────

_KB_DIR = Path(__file__).resolve().parent.parent.parent.parent / "knowledge_base"


def _load_json(path: Path) -> dict:
    """Load a JSON file, return empty dict on failure."""
    if path.exists():
        return json.loads(path.read_text())
    return {}


def load_agent_catalog(domain: str) -> list[AIAgent]:
    """Load the agent catalog for a domain (retail, wealth, commercial)."""
    path = _KB_DIR / "ai_agents" / f"{domain}.json"
    data = _load_json(path)
    agents = []
    for entry in data.get("agents", []):
        agents.append(AIAgent(
            agent_id=entry["agent_id"],
            name=entry["name"],
            pillar=AIPillar(entry["pillar"]),
            category=entry.get("category", ""),
            description=entry.get("description", ""),
            bic_weight=entry["bic_weight"],
            monthly_volume_per_user=entry["monthly_volume_per_user"],
            avg_tokens_per_action=entry.get("avg_tokens_per_action", 0),
            model_routing=entry.get("model_routing", "claude-sonnet"),
            raw_cost_per_action_usd=entry.get("raw_cost_per_action_usd", 0.0),
            phase=entry.get("phase", 1),
            value_narrative=entry.get("value_narrative", ""),
        ))
    return agents


def load_bic_reference() -> dict:
    """Load BIC pricing reference data."""
    return _load_json(_KB_DIR / "ai_pricing" / "bic_reference.json")


def load_pillar_definitions() -> dict:
    """Load pillar pricing definitions."""
    return _load_json(_KB_DIR / "ai_pricing" / "pillar_definitions.json")


def catalog_to_selections(agents: list[AIAgent]) -> list[AIAgentSelection]:
    """Convert a full agent catalog to selections (no overrides)."""
    return [
        AIAgentSelection(
            agent_id=a.agent_id,
            name=a.name,
            pillar=a.pillar,
            bic_weight=a.bic_weight,
            monthly_volume_per_user=a.monthly_volume_per_user,
            avg_tokens_per_action=a.avg_tokens_per_action,
            model_routing=a.model_routing,
            raw_cost_per_action_usd=a.raw_cost_per_action_usd,
            phase=a.phase,
        )
        for a in agents
    ]


# ─── BIC Consumption ───────────────────────────────────────────


def compute_bic_consumption(
    agents: list[AIAgentSelection],
    user_count: int,
    block_size: int = 250000,
) -> BICConsumption:
    """Calculate total annual BIC consumption across all agents.

    Formula: sum(bic_weight × monthly_volume_per_user × users × 12)
    """
    per_agent = {}
    total = 0.0

    for agent in agents:
        annual_bics = (
            agent.effective_bic_weight
            * agent.effective_volume
            * user_count
            * 12
        )
        per_agent[agent.agent_id] = round(annual_bics, 1)
        total += annual_bics

    blocks_required = max(1, math.ceil(total / block_size)) if total > 0 else 0

    return BICConsumption(
        total_annual_bics=round(total, 1),
        per_agent_annual_bics=per_agent,
        blocks_required=blocks_required,
        block_size=block_size,
    )


# ─── Raw Inference Cost ────────────────────────────────────────


def compute_raw_inference_cost(
    agents: list[AIAgentSelection],
    user_count: int,
) -> tuple[float, dict[str, float]]:
    """Calculate actual LLM token costs (no markup).

    Returns (total_annual_usd, {agent_id: annual_usd}).
    Uses the raw_cost_per_action_usd from the agent catalog.
    """
    per_agent = {}
    total = 0.0

    for agent in agents:
        annual_actions = agent.effective_volume * user_count * 12
        annual_cost = annual_actions * agent.raw_cost_per_action_usd
        per_agent[agent.agent_id] = round(annual_cost, 2)
        total += annual_cost

    return round(total, 2), per_agent


# ─── IF Domain Pricing (Three Layers) ──────────────────────────


def compute_if_domain_pricing(
    bic_consumption: BICConsumption,
    raw_compute_annual: float,
    domain_tier: str = "entry",
    compute_markup_pct: float = 15.0,
) -> IFDomainPricing:
    """Compute the Intelligence Fabric pricing using the three-layer model.

    Layer 1: IF Domain Base (fixed fee based on tier)
    Layer 2: BIC Blocks (consumption-based, pre-purchased blocks)
    Layer 3: Compute Pass-through (raw cost + markup)
    """
    ref = load_bic_reference()

    # Layer 1: Domain Base
    domain_tiers = ref.get("if_domain_base", {}).get("tiers", {})
    tier_data = domain_tiers.get(domain_tier, domain_tiers.get("entry", {}))
    domain_base = tier_data.get("annual_usd", 250000)

    # Layer 2: BIC Blocks
    block_ref = ref.get("bic_blocks", {})
    first_block_price = block_ref.get("first_block", {}).get("price_usd", 45000)
    additional_block_price = block_ref.get("additional_blocks", {}).get("price_usd", 39000)

    blocks_needed = bic_consumption.blocks_required
    if blocks_needed <= 0:
        bic_blocks_cost = 0.0
    elif blocks_needed == 1:
        bic_blocks_cost = first_block_price
    else:
        bic_blocks_cost = first_block_price + (blocks_needed - 1) * additional_block_price

    # Apply volume discounts
    discount_pct = _get_volume_discount(bic_consumption.total_annual_bics, ref)
    bic_blocks_cost *= (1 - discount_pct / 100)

    # Layer 3: Compute Pass-through
    compute_with_markup = raw_compute_annual * (1 + compute_markup_pct / 100)

    return IFDomainPricing(
        domain_base_tier=domain_tier,
        domain_base_annual_usd=round(domain_base, 2),
        bic_blocks_count=blocks_needed,
        bic_blocks_annual_usd=round(bic_blocks_cost, 2),
        total_bics_allocated=blocks_needed * bic_consumption.block_size,
        raw_compute_annual_usd=round(raw_compute_annual, 2),
        compute_markup_pct=compute_markup_pct,
        compute_passthrough_annual_usd=round(compute_with_markup, 2),
    )


def _get_volume_discount(total_bics: float, ref: dict) -> float:
    """Get volume discount percentage based on BIC consumption."""
    tiers = ref.get("volume_discount_curves", {}).get("tiers", [])
    for tier in reversed(tiers):
        if total_bics >= tier.get("min_bics_annual", 0):
            return tier.get("discount_pct", 0)
    return 0.0


# ─── Build-It-Yourself Cost ────────────────────────────────────


def compute_build_it_yourself_cost(
    agents: list[AIAgentSelection],
    user_count: int,
) -> float:
    """Estimate what it would cost the client to build equivalent agents internally.

    Based on: engineering FTEs × loaded cost + infrastructure overhead + maintenance.
    This is the value anchor — the ceiling that makes the platform price look rational.
    """
    ref = load_bic_reference()
    benchmarks = ref.get("build_it_yourself_benchmarks", {})

    fte_cost = benchmarks.get("engineering_fte_loaded_cost_usd", 180000)
    ftes_per_agent = benchmarks.get("ftes_per_agent", {"simple": 1.5, "medium": 2.5, "complex": 4.0})
    infra_overhead_pct = benchmarks.get("infrastructure_overhead_pct", 25)
    maintenance_pct = benchmarks.get("maintenance_pct_of_build", 30)

    total_fte_cost = 0.0
    for agent in agents:
        complexity = agent.complexity.value
        ftes = ftes_per_agent.get(complexity, 2.5)
        total_fte_cost += ftes * fte_cost

    # Annual cost = FTE build cost + infrastructure + maintenance
    # Build cost is a one-time cost amortised over 3 years, plus ongoing maintenance
    annual_build_amortised = total_fte_cost / 3
    infra_cost = total_fte_cost * (infra_overhead_pct / 100) / 3
    maintenance_cost = total_fte_cost * (maintenance_pct / 100)

    return round(annual_build_amortised + infra_cost + maintenance_cost, 2)


# ─── Conversational Engine Pricing ─────────────────────────────


def compute_conversational_pricing(
    config: AIPricingConfig,
) -> PillarPricingResult:
    """Compute Pillar 2: Conversational Engine pricing.

    Base fee (by SLA tier) + variable per-interaction.
    """
    defs = load_pillar_definitions()
    conv = defs.get("pillars", {}).get("conversational_engine", {})

    # Base fee
    base_tiers = conv.get("base_fee_tiers", {})
    tier_data = base_tiers.get(config.conversational_tier, base_tiers.get("entry", {}))
    base_fee = tier_data.get("annual_fee_usd", 500000)

    # Variable — Employee Workspace
    ew_annual = 0.0
    ew_monthly = config.employee_workspace_monthly_interactions or 0
    if ew_monthly > 0:
        ew_rates = conv.get("per_interaction_rates", {}).get("employee_workspace", {})
        ew_rate = _get_tiered_rate(ew_monthly, ew_rates.get("volume_tiers", []))
        ew_annual = ew_monthly * ew_rate * 12

    # Variable — Conversational Banking
    cb_annual = 0.0
    cb_monthly = config.conversational_banking_monthly_interactions or 0
    if cb_monthly > 0:
        cb_rates = conv.get("per_interaction_rates", {}).get("conversational_banking", {})
        cb_rate = _get_tiered_rate(cb_monthly, cb_rates.get("volume_tiers", []))
        cb_annual = cb_monthly * cb_rate * 12

    total = base_fee + ew_annual + cb_annual

    return PillarPricingResult(
        pillar=AIPillar.CONVERSATIONAL_ENGINE,
        pricing_model="base_fee_plus_per_interaction",
        annual_usd=round(total, 2),
        detail={
            "base_fee_usd": round(base_fee, 2),
            "base_fee_tier": config.conversational_tier,
            "employee_workspace_annual_usd": round(ew_annual, 2),
            "employee_workspace_monthly_interactions": ew_monthly,
            "conversational_banking_annual_usd": round(cb_annual, 2),
            "conversational_banking_monthly_interactions": cb_monthly,
        },
    )


def _get_tiered_rate(monthly_volume: int, tiers: list[dict]) -> float:
    """Get the applicable rate from a tiered volume schedule."""
    for tier in tiers:
        if "above_monthly" in tier:
            return tier["rate_usd"]
        if monthly_volume <= tier.get("up_to_monthly", float("inf")):
            return tier["rate_usd"]
    return tiers[-1]["rate_usd"] if tiers else 0.0


# ─── BYO Platform Pricing ──────────────────────────────────────


def compute_byo_pricing(config: AIPricingConfig) -> PillarPricingResult:
    """Compute Pillar 4: Build Your Own Agent Platform pricing."""
    defs = load_pillar_definitions()
    byo = defs.get("pillars", {}).get("byo_platform", {})

    byo_tier = config.byo_tier or "standard"

    # Platform access fee
    platform_fees = byo.get("platform_access_fee_usd", {})
    platform_fee = platform_fees.get(byo_tier, 150000)

    # Per-agent deployment
    deployment = byo.get("per_agent_deployment_fee_usd", {})
    monthly_per_agent = deployment.get("monthly_per_agent", 2500)
    included = deployment.get("included_agents_by_tier", {}).get(byo_tier, 3)
    billable_agents = max(0, config.byo_custom_agent_count - included)
    deployment_annual = billable_agents * monthly_per_agent * 12

    total = platform_fee + deployment_annual

    return PillarPricingResult(
        pillar=AIPillar.BYO_PLATFORM,
        pricing_model="platform_fee_plus_deployment",
        annual_usd=round(total, 2),
        detail={
            "platform_fee_usd": platform_fee,
            "platform_tier": byo_tier,
            "custom_agents": config.byo_custom_agent_count,
            "included_agents": included,
            "billable_agents": billable_agents,
            "deployment_annual_usd": round(deployment_annual, 2),
        },
    )


# ─── Master Calculator ─────────────────────────────────────────


def compute_ai_pricing(
    config: AIPricingConfig,
    user_count: int,
    domain: str = "retail",
) -> AIPricingResult:
    """Master AI pricing calculator.

    Computes the complete three-layer pricing model:
    1. Raw compute cost (what LLMs actually cost)
    2. Platform price (what Backbase charges — IF Domain + BICs + Compute)
    3. Build-it-yourself (what it would cost the client internally)

    Plus per-pillar breakdowns for conversational and process automation.
    """
    agents = config.selected_agents

    # If no agents selected, load from domain catalog
    if not agents:
        catalog = load_agent_catalog(domain)
        agents = catalog_to_selections(catalog)

    # BIC consumption
    bic = compute_bic_consumption(agents, user_count)

    # Raw inference cost
    raw_total, raw_per_agent = compute_raw_inference_cost(agents, user_count)

    # IF Domain Pricing (three layers)
    if_pricing = compute_if_domain_pricing(
        bic_consumption=bic,
        raw_compute_annual=raw_total,
        domain_tier=config.if_domain_tier,
        compute_markup_pct=config.compute_markup_pct,
    )

    # Build-it-yourself
    biy_cost = compute_build_it_yourself_cost(agents, user_count)

    # Per-pillar pricing
    pillar_results = []

    # Embedded AI — included in IF pricing (no separate line)
    embedded_agents = [a for a in agents if a.pillar == AIPillar.EMBEDDED_AI]
    if embedded_agents:
        embedded_bic = compute_bic_consumption(embedded_agents, user_count)
        embedded_raw, _ = compute_raw_inference_cost(embedded_agents, user_count)
        pillar_results.append(PillarPricingResult(
            pillar=AIPillar.EMBEDDED_AI,
            pricing_model="signature_tier_plus_token_passthrough",
            annual_usd=0.0,  # included in IF / Signature tier
            detail={
                "annual_bics": round(embedded_bic.total_annual_bics, 1),
                "annual_compute_usd": round(embedded_raw, 2),
                "agent_count": len(embedded_agents),
                "note": "Included in Signature Tier license + IF pricing",
            },
        ))

    # Conversational Engine
    if AIPillar.CONVERSATIONAL_ENGINE in config.pillars:
        pillar_results.append(compute_conversational_pricing(config))

    # Process Automation — priced within IF/BIC model
    pa_agents = [a for a in agents if a.pillar == AIPillar.PROCESS_AUTOMATION]
    if pa_agents:
        pa_bic = compute_bic_consumption(pa_agents, user_count)
        pa_raw, _ = compute_raw_inference_cost(pa_agents, user_count)
        pillar_results.append(PillarPricingResult(
            pillar=AIPillar.PROCESS_AUTOMATION,
            pricing_model="per_execution_via_bic",
            annual_usd=0.0,  # included in IF/BIC
            detail={
                "annual_bics": round(pa_bic.total_annual_bics, 1),
                "annual_compute_usd": round(pa_raw, 2),
                "agent_count": len(pa_agents),
                "note": "Priced within BIC model (IF pricing)",
            },
        ))

    # BYO Platform
    if AIPillar.BYO_PLATFORM in config.pillars and config.byo_tier:
        pillar_results.append(compute_byo_pricing(config))

    # Total platform price = IF + conversational + BYO
    conv_annual = sum(p.annual_usd for p in pillar_results if p.pillar == AIPillar.CONVERSATIONAL_ENGINE)
    byo_annual = sum(p.annual_usd for p in pillar_results if p.pillar == AIPillar.BYO_PLATFORM)
    platform_total = if_pricing.total_if_annual_usd + conv_annual + byo_annual

    # Per-user metrics
    per_user_annual = platform_total / user_count if user_count > 0 else 0.0
    per_user_monthly = per_user_annual / 12

    # Platform-to-compute ratio
    ratio = platform_total / raw_total if raw_total > 0 else 0.0

    # 5-year projection (ramp: AI activates in config.ai_activation_year)
    five_year = []
    for year in range(1, 6):
        if year < config.ai_activation_year:
            five_year.append(0.0)
        elif year == config.ai_activation_year:
            five_year.append(round(platform_total * 0.75, 2))  # ramp year
        else:
            five_year.append(round(platform_total, 2))

    return AIPricingResult(
        raw_compute_annual_usd=round(raw_total, 2),
        platform_price_annual_usd=round(platform_total, 2),
        build_it_yourself_annual_usd=round(biy_cost, 2),
        if_pricing=if_pricing,
        bic_consumption=bic,
        pillar_results=pillar_results,
        agent_annual_bics=bic.per_agent_annual_bics,
        agent_annual_compute=raw_per_agent,
        per_user_ai_cost_annual_usd=round(per_user_annual, 2),
        per_user_ai_cost_monthly_usd=round(per_user_monthly, 2),
        platform_to_compute_ratio=round(ratio, 1),
        total_agents=len(agents),
        five_year_ai_revenue=five_year,
        currency=config.currency,
        fx_rate=config.fx_rate,
    )

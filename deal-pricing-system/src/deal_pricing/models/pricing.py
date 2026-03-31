"""Pricing construct models."""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ConstructType(str, Enum):
    FLAT_BLOCK = "flat_block"
    MILESTONE_RAMP = "milestone_ramp"
    ALL_YOU_CAN_EAT = "all_you_can_eat"
    FLOOR_KICKER = "floor_kicker"
    DUAL_TRACK = "dual_track"
    CROSS_SELL_BUNDLE = "cross_sell_bundle"
    REGIONAL_STRUCTURE = "regional_structure"
    BASE_FEE_TIERED = "base_fee_tiered"  # 2025 model: Base Fee + included tier + tiered additional users


class EditionTier(str, Enum):
    """Backbase 2025 product editions."""
    ESSENTIAL = "essential"
    PREMIUM = "premium"
    SIGNATURE = "signature"


class PricingConstruct(BaseModel):
    """A complete pricing construct definition.

    Defines HOW pricing works — the Financial Engine uses this
    to compute actual numbers. The LLM strategist populates this
    but never computes revenue figures.
    """

    construct_type: ConstructType
    label: str
    description: str
    licensing_logic: str
    true_up_mechanism: Optional[str] = None
    cap_or_floor: Optional[str] = None

    # Per-module pricing inputs
    digital_banking_rate: Optional[float] = None  # per user per year
    digital_banking_block_size: Optional[int] = None  # if block-based
    digital_banking_block_price: Optional[float] = None  # price per block
    assist_rate: Optional[float] = None  # per employee per year
    lending_rate_bps: Optional[float] = None  # basis points on AUM
    add_on_rates: dict[str, float] = Field(default_factory=dict)

    # Services
    services_year_1: Optional[float] = None
    services_ongoing_annual: Optional[float] = None

    # Ramp parameters (for milestone_ramp)
    ramp_schedule: Optional[dict[str, float]] = None  # "1" → 0.7, "2" → 0.85, etc.

    # Floor/kicker parameters
    floor_amount: Optional[float] = None
    kicker_threshold: Optional[int] = None  # user count trigger
    kicker_rate: Optional[float] = None  # per user above threshold

    # All-you-can-eat parameters
    ayce_annual_fee: Optional[float] = None
    ayce_user_cap: Optional[int] = None  # max users included

    # Dual-track parameters
    track_definitions: Optional[dict[str, dict]] = None

    # 2025 Base Fee + Tiered Users parameters
    edition: Optional[EditionTier] = None
    base_fee: Optional[float] = None  # annual base fee (includes first user tier)
    included_users: Optional[int] = None  # users included in base fee
    tiered_user_rates: Optional[list[dict[str, float]]] = None  # [{"up_to": 100000, "rate": 6.52}, ...]
    hosting_embedded: bool = True  # 2025 model embeds hosting in base fee

    # Pros/cons
    pros_client: list[str] = Field(default_factory=list)
    pros_backbase: list[str] = Field(default_factory=list)
    cons_client: list[str] = Field(default_factory=list)
    cons_backbase: list[str] = Field(default_factory=list)


class ConcessionMove(BaseModel):
    """A single concession move in a negotiation round."""

    lever: str  # e.g. "pricing_discount", "payment_terms", "contract_term"
    description: str
    value_impact: Optional[str] = None  # e.g. "-$50K ARR", "net-60 terms"


class NegotiationPlan(BaseModel):
    """3-round negotiation plan per PDF best practices (Martini strategy)."""

    opening_offer: list[str] = Field(default_factory=list)  # Key terms of initial offer
    planned_concessions: list[ConcessionMove] = Field(default_factory=list)  # Counter-offer levers
    final_exec_give: Optional[str] = None  # Held-back concession for exec close
    walk_away_terms: list[str] = Field(default_factory=list)  # Non-negotiable red lines
    give_to_get_requirements: list[str] = Field(default_factory=list)  # What we require in return


class PricingStrategy(BaseModel):
    """Output from the Pricing Strategist agent."""

    recommended: PricingConstruct
    alternative: Optional[PricingConstruct] = None
    rationale: str
    key_trade_offs: list[str] = Field(default_factory=list)
    negotiation_plan: Optional[NegotiationPlan] = None
    deal_levers: list[str] = Field(default_factory=list)  # Available levers for this deal

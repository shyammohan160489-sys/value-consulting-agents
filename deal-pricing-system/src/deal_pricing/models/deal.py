"""Deal input models — the intake 'contract'."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, Field


class DealType(str, Enum):
    NEW_LOGO = "new_logo"
    RENEWAL = "renewal"
    UPSELL = "upsell"
    EXPANSION = "expansion"


class HostingModel(str, Enum):
    MANAGED = "managed"
    CLIENT_HOSTED = "client_hosted"
    HYBRID = "hybrid"


class BankingSegment(str, Enum):
    RETAIL = "retail"
    SME = "sme"
    COMMERCIAL = "commercial"
    WEALTH = "wealth"
    UNIVERSAL = "universal"


class ClientProfile(BaseModel):
    """Client identification and sizing."""

    name: str
    region: str
    country: str
    segments: list[BankingSegment]
    institution_size_users: Optional[int] = None
    institution_size_employees: Optional[int] = None
    institution_size_aum: Optional[float] = None  # USD
    is_existing_customer: bool = False
    contract_start_date: Optional[str] = None
    contract_renewal_date: Optional[str] = None
    current_annual_spend: Optional[float] = None  # actual, not list price


class DemandFirmness(str, Enum):
    """Demand firmness level per negotiation best practices."""
    VALIDATED = "validated"  # Budgeted, has project owner/schedule
    PROJECTED = "projected"  # Credible interest, may not be budgeted yet
    PIPELINE = "pipeline"    # Limited exposure, unconsidered needs


class DemandProfile(BaseModel):
    """User/volume forecasts and planned launches."""

    current_active_users: Optional[int] = None
    year_1_users: Optional[int] = None
    year_2_users: Optional[int] = None
    year_3_users: Optional[int] = None
    year_4_users: Optional[int] = None
    year_5_users: Optional[int] = None
    demand_firmness: DemandFirmness = DemandFirmness.PROJECTED
    planned_launches: list[str] = Field(default_factory=list)
    assist_employees: Optional[int] = None
    lending_aum: Optional[float] = None

    def get_user_ramp(self) -> list[int]:
        """Return 5-year user ramp as a list, interpolating gaps."""
        raw = [
            self.year_1_users,
            self.year_2_users,
            self.year_3_users,
            self.year_4_users,
            self.year_5_users,
        ]
        # Fill None values by interpolation
        result = []
        last_known = self.current_active_users or 0
        for val in raw:
            if val is not None:
                last_known = val
            result.append(last_known)
        return result


class ModuleScope(BaseModel):
    """Licensed and proposed modules."""

    currently_licensed: list[str] = Field(default_factory=list)
    proposed_additions: list[str] = Field(default_factory=list)
    hosting_model: HostingModel = HostingModel.MANAGED
    ai_analytics_plans: Optional[str] = None
    services_scope: Optional[str] = None

    # Structured AI pricing configuration (replaces ai_analytics_plans for computation)
    ai_pricing_config: Optional[dict] = None  # serialised AIPricingConfig

    @property
    def all_modules(self) -> list[str]:
        """All modules (current + proposed)."""
        return list(set(self.currently_licensed + self.proposed_additions))


class LicenseActivation(str, Enum):
    """License activation model per negotiation best practices."""
    BUY_UPFRONT = "buy_upfront"        # Activate all users up-front at flat rate
    STAGGERED = "staggered"            # Match activation to roll-out schedule
    PRICE_RAMP = "price_ramp"          # All users up-front, increase cost annually


class DealConstraints(BaseModel):
    """Client concerns and internal objectives."""

    client_concerns: list[str] = Field(default_factory=list)
    arr_uplift_target_min: Optional[float] = None
    arr_uplift_target_max: Optional[float] = None
    sensitivities: list[str] = Field(default_factory=list)
    tax_jurisdiction_preference: Optional[str] = None
    preferred_contract_years: int = 5
    license_activation: LicenseActivation = LicenseActivation.STAGGERED
    payment_terms: Optional[str] = None  # e.g. "net-30", "net-60"
    renewal_cap_pct: Optional[float] = None  # max annual renewal uplift %
    notes: Optional[str] = None


class DealBrief(BaseModel):
    """Complete deal input — the validated intake contract."""

    deal_id: str = Field(default_factory=lambda: f"DEAL-{uuid4().hex[:8].upper()}")
    deal_type: DealType
    client: ClientProfile
    demand: DemandProfile
    scope: ModuleScope
    constraints: DealConstraints
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = Field(default_factory=lambda: datetime.now().isoformat())

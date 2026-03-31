"""Financial output models — all values computed by Python, never by LLM."""

from __future__ import annotations

import math
from typing import Optional

from pydantic import BaseModel, Field

from .pricing import ConstructType


class YearlyBreakdown(BaseModel):
    """Single year in a 5-year financial schedule."""

    year: int
    users: int
    license_revenue: float
    services_revenue: float
    total_revenue: float
    per_user_cost: float  # $/user optics (license / users)
    arr: float  # annual recurring = license only
    margin_estimate: Optional[float] = None

    # Module-level detail
    digital_banking_revenue: float = 0.0
    assist_revenue: float = 0.0
    lending_revenue: float = 0.0
    add_on_revenue: float = 0.0

    # AI pricing layer (stacks on platform licensing)
    ai_revenue: float = 0.0
    ai_bic_consumption: float = 0.0


class FinancialModel(BaseModel):
    """Complete 5-year financial projection for one scenario."""

    scenario_label: str
    construct_type: ConstructType
    yearly: list[YearlyBreakdown]

    # AI pricing detail (optional, populated when AI config is present)
    ai_pricing_detail: Optional[dict] = None  # serialised AIPricingResult

    # Aggregates (computed)
    total_license_5yr: float = 0.0
    total_services_5yr: float = 0.0
    total_deal_value_5yr: float = 0.0
    avg_per_user_5yr: float = 0.0
    arr_year_1: float = 0.0
    arr_year_5: float = 0.0
    arr_cagr: float = 0.0
    breakeven_months: Optional[float] = None  # months to recover Y1 investment (target: 12-16)

    def compute_aggregates(self, implementation_cost: Optional[float] = None) -> None:
        """Compute summary metrics from yearly data.

        Args:
            implementation_cost: Optional total implementation investment for
                breakeven calculation. If not provided, uses Y1 services revenue.
        """
        if not self.yearly:
            return

        self.total_license_5yr = sum(y.license_revenue for y in self.yearly)
        self.total_services_5yr = sum(y.services_revenue for y in self.yearly)
        self.total_deal_value_5yr = self.total_license_5yr + self.total_services_5yr

        total_users = sum(y.users for y in self.yearly)
        if total_users > 0:
            self.avg_per_user_5yr = self.total_license_5yr / total_users

        self.arr_year_1 = self.yearly[0].arr
        self.arr_year_5 = self.yearly[-1].arr

        if self.arr_year_1 > 0 and len(self.yearly) > 1:
            n = len(self.yearly) - 1
            self.arr_cagr = (self.arr_year_5 / self.arr_year_1) ** (1 / n) - 1

        # Breakeven: months for cumulative license revenue to exceed implementation cost
        # Target is 12-16 months per best practices (appealing to CFOs)
        invest = implementation_cost or self.yearly[0].services_revenue
        if invest > 0 and self.arr_year_1 > 0:
            monthly_arr = self.arr_year_1 / 12
            self.breakeven_months = round(invest / monthly_arr, 1) if monthly_arr > 0 else None


class ScenarioComparison(BaseModel):
    """Side-by-side comparison of baseline vs proposed scenarios."""

    baseline: FinancialModel
    recommended: FinancialModel
    alternative: Optional[FinancialModel] = None

    # Deltas (computed)
    arr_uplift_pct: float = 0.0
    arr_uplift_abs: float = 0.0
    total_uplift_abs: float = 0.0
    per_user_delta_year1: float = 0.0
    per_user_delta_year5: float = 0.0

    def compute_deltas(self) -> None:
        """Compute comparison metrics."""
        if self.baseline.arr_year_1 > 0:
            self.arr_uplift_abs = self.recommended.arr_year_1 - self.baseline.arr_year_1
            self.arr_uplift_pct = self.arr_uplift_abs / self.baseline.arr_year_1 * 100

        self.total_uplift_abs = (
            self.recommended.total_deal_value_5yr - self.baseline.total_deal_value_5yr
        )

        if self.baseline.yearly and self.recommended.yearly:
            self.per_user_delta_year1 = (
                self.recommended.yearly[0].per_user_cost
                - self.baseline.yearly[0].per_user_cost
            )
            self.per_user_delta_year5 = (
                self.recommended.yearly[-1].per_user_cost
                - self.baseline.yearly[-1].per_user_cost
            )

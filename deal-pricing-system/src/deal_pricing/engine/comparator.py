"""Scenario comparison utilities."""

from __future__ import annotations

from ..models.financial import FinancialModel, ScenarioComparison


def format_currency(value: float, decimals: int = 0) -> str:
    """Format a number as currency string."""
    if abs(value) >= 1_000_000:
        return f"${value / 1_000_000:,.{decimals}f}M"
    elif abs(value) >= 1_000:
        return f"${value / 1_000:,.{decimals}f}K"
    return f"${value:,.{decimals}f}"


def format_pct(value: float, decimals: int = 1) -> str:
    """Format a number as percentage string."""
    return f"{value:+.{decimals}f}%"


def summarize_comparison(comparison: ScenarioComparison) -> dict[str, str]:
    """Generate a human-readable summary of scenario comparison.

    Returns dict of metric → formatted value for display.
    """
    rec = comparison.recommended
    base = comparison.baseline

    summary = {
        "Baseline ARR": format_currency(base.arr_year_1),
        "Recommended ARR (Y1)": format_currency(rec.arr_year_1),
        "Recommended ARR (Y5)": format_currency(rec.arr_year_5),
        "ARR Uplift": f"{format_pct(comparison.arr_uplift_pct)} ({format_currency(comparison.arr_uplift_abs)})",
        "5-Year Deal Value": format_currency(rec.total_deal_value_5yr),
        "5-Year Uplift vs Baseline": format_currency(comparison.total_uplift_abs),
        "Avg $/User (5yr)": format_currency(rec.avg_per_user_5yr, decimals=2),
        "ARR CAGR": format_pct(rec.arr_cagr * 100),
    }

    if rec.yearly:
        summary["$/User Y1"] = format_currency(rec.yearly[0].per_user_cost, decimals=2)
        summary["$/User Y5"] = format_currency(rec.yearly[-1].per_user_cost, decimals=2)

    if comparison.alternative:
        alt = comparison.alternative
        summary["Alternative ARR (Y1)"] = format_currency(alt.arr_year_1)
        summary["Alternative 5-Year Value"] = format_currency(alt.total_deal_value_5yr)

    return summary


def build_yearly_table(model: FinancialModel) -> list[dict[str, str]]:
    """Build a formatted yearly table for display.

    Returns list of row dicts suitable for Rich table rendering.
    """
    rows = []
    for y in model.yearly:
        rows.append({
            "Year": str(y.year),
            "Users": f"{y.users:,}",
            "License": format_currency(y.license_revenue),
            "Services": format_currency(y.services_revenue),
            "Total": format_currency(y.total_revenue),
            "$/User": format_currency(y.per_user_cost, decimals=2),
            "ARR": format_currency(y.arr),
        })

    # Add totals row
    rows.append({
        "Year": "Total",
        "Users": "",
        "License": format_currency(model.total_license_5yr),
        "Services": format_currency(model.total_services_5yr),
        "Total": format_currency(model.total_deal_value_5yr),
        "$/User": format_currency(model.avg_per_user_5yr, decimals=2),
        "ARR": "",
    })

    return rows

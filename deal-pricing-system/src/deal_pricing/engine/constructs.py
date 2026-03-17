"""Pricing construct calculators — pure Python, deterministic.

Each function takes a DealBrief + PricingConstruct and returns
a list of YearlyBreakdown objects. No LLM involvement.
"""

from __future__ import annotations

import math
from typing import Optional

from ..models.deal import DealBrief
from ..models.financial import YearlyBreakdown
from ..models.pricing import PricingConstruct


def compute_flat_block(brief: DealBrief, construct: PricingConstruct) -> list[YearlyBreakdown]:
    """Flat block pricing: fixed price per block of users.

    E.g., 500K user block at $X/block. Client pays for blocks consumed.
    When users exceed a block boundary, next block kicks in.
    """
    user_ramp = brief.demand.get_user_ramp()
    block_size = construct.digital_banking_block_size or 100_000
    block_price = construct.digital_banking_block_price or 0.0

    results = []
    for i, users in enumerate(user_ramp):
        year = i + 1
        blocks_needed = max(1, math.ceil(users / block_size))
        db_revenue = blocks_needed * block_price

        assist_rev = _calc_assist(brief, construct)
        lending_rev = _calc_lending(brief, construct)
        addon_rev = _calc_addons(construct)
        license_rev = db_revenue + assist_rev + lending_rev + addon_rev
        services_rev = _calc_services(construct, year)

        results.append(YearlyBreakdown(
            year=year,
            users=users,
            license_revenue=round(license_rev, 2),
            services_revenue=round(services_rev, 2),
            total_revenue=round(license_rev + services_rev, 2),
            per_user_cost=round(license_rev / users, 2) if users > 0 else 0.0,
            arr=round(license_rev, 2),
            digital_banking_revenue=round(db_revenue, 2),
            assist_revenue=round(assist_rev, 2),
            lending_revenue=round(lending_rev, 2),
            add_on_revenue=round(addon_rev, 2),
        ))

    return results


def compute_milestone_ramp(brief: DealBrief, construct: PricingConstruct) -> list[YearlyBreakdown]:
    """Milestone-based ramp: reduced rates in early years, full rate at maturity.

    Uses ramp_schedule: {"1": 0.7, "2": 0.85, "3": 1.0, "4": 1.0, "5": 1.0}
    Multiplier applied to the base per-user rate.
    """
    user_ramp = brief.demand.get_user_ramp()
    base_rate = construct.digital_banking_rate or 0.0
    ramp = construct.ramp_schedule or {}

    results = []
    for i, users in enumerate(user_ramp):
        year = i + 1
        multiplier = ramp.get(str(year), 1.0)
        effective_rate = base_rate * multiplier
        db_revenue = users * effective_rate

        assist_rev = _calc_assist(brief, construct)
        lending_rev = _calc_lending(brief, construct)
        addon_rev = _calc_addons(construct)
        license_rev = db_revenue + assist_rev + lending_rev + addon_rev
        services_rev = _calc_services(construct, year)

        results.append(YearlyBreakdown(
            year=year,
            users=users,
            license_revenue=round(license_rev, 2),
            services_revenue=round(services_rev, 2),
            total_revenue=round(license_rev + services_rev, 2),
            per_user_cost=round(license_rev / users, 2) if users > 0 else 0.0,
            arr=round(license_rev, 2),
            digital_banking_revenue=round(db_revenue, 2),
            assist_revenue=round(assist_rev, 2),
            lending_revenue=round(lending_rev, 2),
            add_on_revenue=round(addon_rev, 2),
        ))

    return results


def compute_all_you_can_eat(brief: DealBrief, construct: PricingConstruct) -> list[YearlyBreakdown]:
    """All-you-can-eat: flat annual fee regardless of user count.

    Optional user cap — overage charged at kicker_rate if exceeded.
    """
    user_ramp = brief.demand.get_user_ramp()
    annual_fee = construct.ayce_annual_fee or 0.0
    user_cap = construct.ayce_user_cap
    overage_rate = construct.kicker_rate or 0.0

    results = []
    for i, users in enumerate(user_ramp):
        year = i + 1
        db_revenue = annual_fee
        if user_cap and users > user_cap:
            db_revenue += (users - user_cap) * overage_rate

        assist_rev = _calc_assist(brief, construct)
        lending_rev = _calc_lending(brief, construct)
        addon_rev = _calc_addons(construct)
        license_rev = db_revenue + assist_rev + lending_rev + addon_rev
        services_rev = _calc_services(construct, year)

        results.append(YearlyBreakdown(
            year=year,
            users=users,
            license_revenue=round(license_rev, 2),
            services_revenue=round(services_rev, 2),
            total_revenue=round(license_rev + services_rev, 2),
            per_user_cost=round(license_rev / users, 2) if users > 0 else 0.0,
            arr=round(license_rev, 2),
            digital_banking_revenue=round(db_revenue, 2),
            assist_revenue=round(assist_rev, 2),
            lending_revenue=round(lending_rev, 2),
            add_on_revenue=round(addon_rev, 2),
        ))

    return results


def compute_floor_kicker(brief: DealBrief, construct: PricingConstruct) -> list[YearlyBreakdown]:
    """Floor + kicker: guaranteed minimum ARR with upside sharing.

    Below threshold: pay floor_amount.
    Above threshold: floor + kicker_rate * (users - threshold).
    Protects Backbase ARR while giving client growth optionality.
    """
    user_ramp = brief.demand.get_user_ramp()
    floor = construct.floor_amount or 0.0
    threshold = construct.kicker_threshold or 0
    kicker_rate = construct.kicker_rate or 0.0

    results = []
    for i, users in enumerate(user_ramp):
        year = i + 1
        if users > threshold and threshold > 0:
            db_revenue = floor + (users - threshold) * kicker_rate
        else:
            db_revenue = floor

        assist_rev = _calc_assist(brief, construct)
        lending_rev = _calc_lending(brief, construct)
        addon_rev = _calc_addons(construct)
        license_rev = db_revenue + assist_rev + lending_rev + addon_rev
        services_rev = _calc_services(construct, year)

        results.append(YearlyBreakdown(
            year=year,
            users=users,
            license_revenue=round(license_rev, 2),
            services_revenue=round(services_rev, 2),
            total_revenue=round(license_rev + services_rev, 2),
            per_user_cost=round(license_rev / users, 2) if users > 0 else 0.0,
            arr=round(license_rev, 2),
            digital_banking_revenue=round(db_revenue, 2),
            assist_revenue=round(assist_rev, 2),
            lending_revenue=round(lending_rev, 2),
            add_on_revenue=round(addon_rev, 2),
        ))

    return results


def compute_dual_track(brief: DealBrief, construct: PricingConstruct) -> list[YearlyBreakdown]:
    """Dual-track: separate pricing tracks by segment/channel.

    track_definitions example:
    {
        "retail": {"rate": 2.0, "users_key": "year_X_users"},
        "business": {"rate": 5.0, "start_year": 2, "users": 50000}
    }
    Falls back to simple per-user if track_definitions not set.
    """
    user_ramp = brief.demand.get_user_ramp()
    tracks = construct.track_definitions or {}

    results = []
    for i, users in enumerate(user_ramp):
        year = i + 1
        db_revenue = 0.0

        if tracks:
            for track_name, track_def in tracks.items():
                start_year = track_def.get("start_year", 1)
                if year < start_year:
                    continue
                track_rate = track_def.get("rate", 0.0)
                track_users = track_def.get("users", users)
                db_revenue += track_users * track_rate
        else:
            rate = construct.digital_banking_rate or 0.0
            db_revenue = users * rate

        assist_rev = _calc_assist(brief, construct)
        lending_rev = _calc_lending(brief, construct)
        addon_rev = _calc_addons(construct)
        license_rev = db_revenue + assist_rev + lending_rev + addon_rev
        services_rev = _calc_services(construct, year)

        results.append(YearlyBreakdown(
            year=year,
            users=users,
            license_revenue=round(license_rev, 2),
            services_revenue=round(services_rev, 2),
            total_revenue=round(license_rev + services_rev, 2),
            per_user_cost=round(license_rev / users, 2) if users > 0 else 0.0,
            arr=round(license_rev, 2),
            digital_banking_revenue=round(db_revenue, 2),
            assist_revenue=round(assist_rev, 2),
            lending_revenue=round(lending_rev, 2),
            add_on_revenue=round(addon_rev, 2),
        ))

    return results


def compute_cross_sell_bundle(brief: DealBrief, construct: PricingConstruct) -> list[YearlyBreakdown]:
    """Cross-sell bundle: bundled pricing for multiple modules.

    Uses per-user rate for digital banking + add_on_rates for bundles.
    Add-ons may have their own start years via track_definitions.
    """
    user_ramp = brief.demand.get_user_ramp()
    rate = construct.digital_banking_rate or 0.0

    results = []
    for i, users in enumerate(user_ramp):
        year = i + 1
        db_revenue = users * rate
        assist_rev = _calc_assist(brief, construct)
        lending_rev = _calc_lending(brief, construct)
        addon_rev = _calc_addons(construct)
        license_rev = db_revenue + assist_rev + lending_rev + addon_rev
        services_rev = _calc_services(construct, year)

        results.append(YearlyBreakdown(
            year=year,
            users=users,
            license_revenue=round(license_rev, 2),
            services_revenue=round(services_rev, 2),
            total_revenue=round(license_rev + services_rev, 2),
            per_user_cost=round(license_rev / users, 2) if users > 0 else 0.0,
            arr=round(license_rev, 2),
            digital_banking_revenue=round(db_revenue, 2),
            assist_revenue=round(assist_rev, 2),
            lending_revenue=round(lending_rev, 2),
            add_on_revenue=round(addon_rev, 2),
        ))

    return results


def compute_base_fee_tiered(brief: DealBrief, construct: PricingConstruct) -> list[YearlyBreakdown]:
    """2025 pricing model: Base Fee with included user tier + tiered additional users.

    Per the 2025 edition model:
    - Fixed base fee includes first N users (e.g., 20K users in base)
    - Managed hosting embedded in base fee
    - Additional users charged at tiered rates (only discountable component)
    - Tiered rates: [{up_to: 100000, rate: 6.52}, {up_to: 500000, rate: 3.20}, ...]
      Last tier's rate applies to all users beyond its threshold.
    """
    user_ramp = brief.demand.get_user_ramp()
    base_fee = construct.base_fee or 0.0
    included_users = construct.included_users or 0
    tiers = construct.tiered_user_rates or []

    # Sort tiers by up_to threshold ascending
    tiers = sorted(tiers, key=lambda t: t.get("up_to", float("inf")))

    results = []
    for i, users in enumerate(user_ramp):
        year = i + 1

        # Base fee always applies
        db_revenue = base_fee

        # Additional users beyond included tier
        additional_users = max(0, users - included_users)
        if additional_users > 0 and tiers:
            remaining = additional_users
            prev_boundary = 0
            for tier in tiers:
                tier_ceiling = tier.get("up_to", float("inf")) - included_users
                tier_capacity = max(0, tier_ceiling - prev_boundary)
                users_in_tier = min(remaining, tier_capacity)
                db_revenue += users_in_tier * tier["rate"]
                remaining -= users_in_tier
                prev_boundary = tier_ceiling
                if remaining <= 0:
                    break
            # If users exceed all defined tiers, charge remainder at last tier rate
            if remaining > 0 and tiers:
                db_revenue += remaining * tiers[-1]["rate"]
        elif additional_users > 0:
            # Fallback: if no tiers defined, use digital_banking_rate
            rate = construct.digital_banking_rate or 0.0
            db_revenue += additional_users * rate

        assist_rev = _calc_assist(brief, construct)
        lending_rev = _calc_lending(brief, construct)
        addon_rev = _calc_addons(construct)
        license_rev = db_revenue + assist_rev + lending_rev + addon_rev
        services_rev = _calc_services(construct, year)

        results.append(YearlyBreakdown(
            year=year,
            users=users,
            license_revenue=round(license_rev, 2),
            services_revenue=round(services_rev, 2),
            total_revenue=round(license_rev + services_rev, 2),
            per_user_cost=round(license_rev / users, 2) if users > 0 else 0.0,
            arr=round(license_rev, 2),
            digital_banking_revenue=round(db_revenue, 2),
            assist_revenue=round(assist_rev, 2),
            lending_revenue=round(lending_rev, 2),
            add_on_revenue=round(addon_rev, 2),
        ))

    return results


# ─── Shared helpers ──────────────────────────────────────────────


def _calc_assist(brief: DealBrief, construct: PricingConstruct) -> float:
    """Calculate Assist revenue (per-employee)."""
    if not construct.assist_rate or not brief.demand.assist_employees:
        return 0.0
    return brief.demand.assist_employees * construct.assist_rate


def _calc_lending(brief: DealBrief, construct: PricingConstruct) -> float:
    """Calculate Lending revenue (AUM-based, basis points)."""
    if not construct.lending_rate_bps or not brief.demand.lending_aum:
        return 0.0
    return brief.demand.lending_aum * (construct.lending_rate_bps / 10_000)


def _calc_addons(construct: PricingConstruct) -> float:
    """Calculate total add-on revenue."""
    return sum(construct.add_on_rates.values())


def _calc_services(construct: PricingConstruct, year: int) -> float:
    """Calculate services revenue for a given year."""
    if year == 1:
        return construct.services_year_1 or 0.0
    return construct.services_ongoing_annual or 0.0

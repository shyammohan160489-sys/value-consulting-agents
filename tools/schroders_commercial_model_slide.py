#!/usr/bin/env python3
"""
Schroders Commercial Model — 2-Slide PPTX

Slide 1: Pricing Bridge — September 2025 → March 2026
Slide 2: Commercial Model — Enterprise vs PAG

Usage:
    python3 tools/schroders_commercial_model_slide.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.pptx_presenter import PptxPresenter
from pptx.util import Inches, Pt, Emu
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor


class CommercialModelSlide(PptxPresenter):
    """Two-slide deck: Pricing Bridge + Enterprise vs PAG commercial model."""

    # Extra colors
    BLUE_TINT = RGBColor(0xE8, 0xF0, 0xFF)    # very light blue card bg
    AMBER_TINT = RGBColor(0xFE, 0xF7, 0xE8)   # very light amber card bg
    BLUE_BORDER = RGBColor(0x99, 0xBB, 0xFF)   # soft blue border
    AMBER_BORDER = RGBColor(0xF0, 0xC6, 0x6E)  # soft amber border
    STAT_BG = RGBColor(0xF0, 0xF4, 0xF8)       # neutral stat box bg
    INSIGHT_BG = RGBColor(0xF3, 0xF4, 0xF6)    # insight card bg
    RED = RGBColor(0xDC, 0x26, 0x26)

    def _pill(self, slide, text, left, top, w, h, fill, text_color=None):
        """Small rounded pill badge."""
        sh = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, w, h)
        sh.fill.solid()
        sh.fill.fore_color.rgb = fill
        sh.line.fill.background()
        self._txt(slide, text, left, top + Pt(1), w, h,
                  size=Pt(7), color=text_color or self.WHITE, bold=True,
                  align=PP_ALIGN.CENTER)

    # ──────────────────────────────────────────────────────
    #  SLIDE 1: WHAT WE SHOWED IN SEPTEMBER
    # ──────────────────────────────────────────────────────
    def _build_september_slide(self):
        s = self._new_slide()
        MUTED = RGBColor(0x9C, 0xA3, 0xAF)

        # Header
        self._section_label(s, 'SEPTEMBER 2025')
        self._heading(s, 'What we showed ', 'back then.', size=Pt(30))
        self._txt(s, 'Indicative pricing shared during assessment phase. Scope limited to servicing & onboarding. '
                  'No AI, no marketplace, no ramped pricing.',
                  self.ML, Inches(1.15), self.CW, Inches(0.35),
                  size=Pt(11), color=self.SUB_TEXT)

        # ── Layout constants ─────────────────────────────
        card_gap = Inches(0.4)
        card_a_w = Inches(6.6)
        card_b_w = Inches(5.1)
        cards_y = Inches(1.7)
        card_a_x = self.ML
        card_b_x = card_a_x + card_a_w + card_gap
        card_h = Inches(3.55)

        # ══════════════════════════════════════════════════
        #  SCENARIO A — ADOPT (left card)
        # ══════════════════════════════════════════════════
        self._card(s, card_a_x, cards_y, card_a_w, card_h,
                   fill=self.WHITE, border=MUTED)

        # Grey top accent line
        self._bar_rect(s, card_a_x + Pt(4), cards_y + Pt(2),
                       card_a_w - Pt(8), Pt(3), MUTED)

        self._txt(s, 'SCENARIO A · ADOPT',
                  card_a_x + Inches(0.3), cards_y + Inches(0.18),
                  Inches(3.5), Inches(0.25),
                  size=Pt(9), color=MUTED, bold=True)

        # Scope description
        self._txt(s, 'Digital Banking Wealth Signature + Onboarding',
                  card_a_x + Inches(0.3), cards_y + Inches(0.52),
                  card_a_w - Inches(0.6), Inches(0.25),
                  size=Pt(12), color=self.DARK_TEXT, bold=True)

        # Year rows (flat pricing)
        yr_x = card_a_x + Inches(0.4)
        yr_top = cards_y + Inches(0.95)
        yr_spacing = Inches(0.30)

        a_years = [
            ('Year 1', '£2.07M', 'List price (zero discount)'),
            ('Year 2', '£2.07M', 'Flat — no ramp'),
            ('Year 3', '£2.07M', 'Flat — no ramp'),
            ('Year 4', '£2.07M', 'Flat — no ramp'),
            ('Year 5', '£2.07M', 'Flat — no ramp'),
        ]

        for i, (yr, price, note) in enumerate(a_years):
            y = yr_top + i * yr_spacing
            if i % 2 == 0:
                self._bar_rect(s, card_a_x + Inches(0.2), y - Pt(1),
                               Inches(3.4), Inches(0.27),
                               RGBColor(0xF5, 0xF5, 0xF5))
            self._txt(s, yr, yr_x, y, Inches(1.1), Inches(0.25),
                      size=Pt(11), color=self.SUB_TEXT)
            self._txt(s, price, yr_x + Inches(1.1), y, Inches(0.9), Inches(0.25),
                      size=Pt(14), color=self.DARK_TEXT, bold=True,
                      align=PP_ALIGN.RIGHT)
            self._txt(s, note, yr_x + Inches(2.1), y + Pt(1), Inches(1.2), Inches(0.25),
                      size=Pt(8), color=MUTED)

        # Description (right side)
        self._txt(s, 'Replaces existing web & mobile apps.\nIntroduces RM Portal and digital onboarding.\n\n22,000 users (flat).\n£4bn AUM scope.\n\nNo AI. No Grand Central.\nNo marketplace vendors.',
                  card_a_x + Inches(3.8), cards_y + Inches(0.55),
                  Inches(2.5), Inches(2.5),
                  size=Pt(9), color=self.SUB_TEXT)

        # Stat boxes
        stat_y = cards_y + card_h - Inches(0.72)
        stat_h = Inches(0.55)
        stat_gap = Inches(0.15)
        a_stat_w = (card_a_w - Inches(0.6) - 2 * stat_gap) / 3

        for i, (val, lbl, vc, bg) in enumerate([
            ('£10.3M', '5-YR LICENCE', MUTED, RGBColor(0xF3, 0xF4, 0xF6)),
            ('0%', 'DISCOUNT', MUTED, RGBColor(0xF3, 0xF4, 0xF6)),
            ('Flat', 'NO RAMP', MUTED, RGBColor(0xF3, 0xF4, 0xF6)),
        ]):
            sx = card_a_x + Inches(0.3) + i * (a_stat_w + stat_gap)
            self._stat_box(s, val, lbl, sx, stat_y, a_stat_w, stat_h,
                           val_color=vc, bg=bg)

        # ══════════════════════════════════════════════════
        #  SCENARIO C — ADOPT & EXPAND (right card)
        # ══════════════════════════════════════════════════
        self._card(s, card_b_x, cards_y, card_b_w, card_h,
                   fill=self.WHITE, border=MUTED)

        self._bar_rect(s, card_b_x + Pt(4), cards_y + Pt(2),
                       card_b_w - Pt(8), Pt(3), MUTED)

        self._txt(s, 'SCENARIO C · ADOPT & EXPAND',
                  card_b_x + Inches(0.3), cards_y + Inches(0.18),
                  Inches(3.5), Inches(0.25),
                  size=Pt(9), color=MUTED, bold=True)

        self._txt(s, '+ Grand Central, Agentic AI, Advisory',
                  card_b_x + Inches(0.3), cards_y + Inches(0.52),
                  card_b_w - Inches(0.6), Inches(0.25),
                  size=Pt(12), color=self.DARK_TEXT, bold=True)

        # Year rows
        c_years = [
            ('Year 1', '£2.55M', '33% discount'),
            ('Year 2', '£2.55M', 'Flat — no ramp'),
            ('Year 3+', '£2.55M', 'Flat — no ramp'),
        ]

        pag_yr_x = card_b_x + Inches(0.4)
        for i, (yr, price, note) in enumerate(c_years):
            y = yr_top + i * yr_spacing
            if i % 2 == 0:
                self._bar_rect(s, card_b_x + Inches(0.2), y - Pt(1),
                               Inches(3.2), Inches(0.27),
                               RGBColor(0xF5, 0xF5, 0xF5))
            self._txt(s, yr, pag_yr_x, y, Inches(1.1), Inches(0.25),
                      size=Pt(11), color=self.SUB_TEXT)
            self._txt(s, price, pag_yr_x + Inches(1.1), y, Inches(0.9), Inches(0.25),
                      size=Pt(14), color=self.DARK_TEXT, bold=True,
                      align=PP_ALIGN.RIGHT)
            self._txt(s, note, pag_yr_x + Inches(2.1), y + Pt(1), Inches(1.2), Inches(0.25),
                      size=Pt(8), color=MUTED)

        # Description
        self._txt(s, 'Extended scope: Grand Central, Agentic AI Foundation, Advisory (TVP).\n\n22K → 35K users over 5yr.\n£4bn AUM scope.\n\n33% discount applied.\nNo marketplace.\nNo connector slots.',
                  card_b_x + Inches(0.4), cards_y + Inches(1.85),
                  Inches(4.2), Inches(1.5),
                  size=Pt(9), color=self.SUB_TEXT)

        # Stat boxes
        b_stat_w = (card_b_w - Inches(0.6) - 2 * stat_gap) / 3
        for i, (val, lbl, vc, bg) in enumerate([
            ('£12.7M', '5-YR LICENCE', MUTED, RGBColor(0xF3, 0xF4, 0xF6)),
            ('33%', 'DISCOUNT', MUTED, RGBColor(0xF3, 0xF4, 0xF6)),
            ('Flat', 'NO RAMP', MUTED, RGBColor(0xF3, 0xF4, 0xF6)),
        ]):
            sx = card_b_x + Inches(0.3) + i * (b_stat_w + stat_gap)
            self._stat_box(s, val, lbl, sx, stat_y, b_stat_w, stat_h,
                           val_color=vc, bg=bg)

        # ── What was NOT included ───────────────────────
        not_y = cards_y + card_h + Inches(0.2)
        self._txt(s, 'NOT INCLUDED IN SEPTEMBER',
                  self.ML, not_y, Inches(3), Inches(0.2),
                  size=Pt(8), color=self.RED, bold=True)

        items = [
            'Agentic Runtime / AI use cases',
            'CLO / Digital Engage',
            'Marketplace vendors (Jumio, Twilio, etc.)',
            'Custom connector slots (Folio, T24, ContentStack)',
            'Digital Assist licences',
            'Ramped pricing model',
        ]
        for i, item in enumerate(items):
            col = i // 3
            row = i % 3
            ix = self.ML + col * Inches(4.2)
            iy = not_y + Inches(0.22) + row * Inches(0.2)
            self._txt(s, '✕  ' + item, ix, iy, Inches(4.0), Inches(0.2),
                      size=Pt(9), color=self.SUB_TEXT)

        # ── Key context bar ─────────────────────────────
        ctx_y = not_y + Inches(0.9)
        self._insight_card(s, 'INDICATIVE RANGE',
            'Annual licence: £1.68M – £2.95M. Implementation: £1.5M – £2.25M. '
            'Managed services: £675K/yr. All flat, no ramp, no AI, limited AUM scope.',
            self.ML, ctx_y, self.CW, Inches(0.55))

        self._footer(s, slide_number=3)

    # ──────────────────────────────────────────────────────
    #  SLIDE 2: COMMERCIAL MODEL
    # ──────────────────────────────────────────────────────
    def _build_commercial_model(self):
        s = self._new_slide()

        # ── Header ───────────────────────────────────────────
        self._section_label(s, 'COMMERCIAL MODEL')
        self._heading(s, 'Enterprise or ', 'Pay As You Grow.', size=Pt(30))
        self._txt(s, 'Same platform. Same delivery. Same value. Two commercial structures — choose the model that fits your commitment profile.',
                  self.ML, Inches(1.15), self.CW, Inches(0.35),
                  size=Pt(11), color=self.SUB_TEXT)

        # ── Layout constants ─────────────────────────────────
        card_gap = Inches(0.4)
        ent_w = Inches(6.6)
        pag_w = Inches(5.1)
        cards_y = Inches(1.7)
        ent_x = self.ML
        pag_x = ent_x + ent_w + card_gap
        ent_h = Inches(3.55)
        pag_h = Inches(3.55)

        # ══════════════════════════════════════════════════════
        #  ENTERPRISE CARD (left, larger)
        # ══════════════════════════════════════════════════════
        self._card(s, ent_x, cards_y, ent_w, ent_h,
                   fill=self.WHITE, border=self.BLUE)

        # Blue top accent line
        self._bar_rect(s, ent_x + Pt(4), cards_y + Pt(2),
                       ent_w - Pt(8), Pt(3), self.BLUE)

        # Label + Recommended badge
        self._txt(s, 'OPTION A · ENTERPRISE',
                  ent_x + Inches(0.3), cards_y + Inches(0.18),
                  Inches(3), Inches(0.25),
                  size=Pt(9), color=self.BLUE, bold=True)

        self._pill(s, '★ Recommended',
                   ent_x + ent_w - Inches(1.8), cards_y + Inches(0.15),
                   Inches(1.5), Inches(0.22), self.GREEN)

        # Year-by-year pricing
        yr_x = ent_x + Inches(0.4)
        yr_w = Inches(2.8)
        yr_top = cards_y + Inches(0.6)
        yr_spacing = Inches(0.30)

        ent_years = [
            ('Year 1', '£2.3M', '60% discount'),
            ('Year 2', '£2.6M', '55% discount'),
            ('Year 3', '£3.6M', '55% discount'),
            ('Year 4', '£4.0M', '50% discount'),
            ('Year 5', '£4.4M', '45% discount'),
        ]

        for i, (yr, price, discount) in enumerate(ent_years):
            y = yr_top + i * yr_spacing
            # Alternate subtle row backgrounds
            if i % 2 == 0:
                self._bar_rect(s, ent_x + Inches(0.2), y - Pt(1),
                               Inches(3.2), Inches(0.27),
                               RGBColor(0xF5, 0xF8, 0xFF))
            self._txt(s, yr, yr_x, y, Inches(1.1), Inches(0.25),
                      size=Pt(11), color=self.SUB_TEXT)
            self._txt(s, price, yr_x + Inches(1.1), y, Inches(0.9), Inches(0.25),
                      size=Pt(14), color=self.DARK_TEXT, bold=True,
                      align=PP_ALIGN.RIGHT)
            self._txt(s, discount, yr_x + Inches(2.1), y + Pt(1), Inches(1.0), Inches(0.25),
                      size=Pt(8), color=self.GREEN)

        # Description text (right side of Enterprise card)
        desc_x = ent_x + Inches(3.7)
        desc_w = Inches(2.7)
        self._txt(s, 'Full platform commitment from Day 1.\n\nScaling entry — you pay less upfront, more as value compounds.\n\nAll AI capabilities available immediately.',
                  desc_x, cards_y + Inches(0.55), desc_w, Inches(2.0),
                  size=Pt(9), color=self.SUB_TEXT)

        # Enterprise stat boxes (bottom of card)
        stat_y = cards_y + ent_h - Inches(0.72)
        stat_h = Inches(0.55)
        stat_gap = Inches(0.15)
        ent_stat_w = (ent_w - Inches(0.6) - 2 * stat_gap) / 3

        for i, (val, lbl, vc, bg) in enumerate([
            ('£16.9M', '5-YR LICENCE', self.BLUE, self.BLUE_LIGHT),
            ('~7.0×', 'ROI', self.GREEN, self.GREEN_LIGHT),
            ('Month 8', 'BREAKEVEN', self.PURPLE, self.PURPLE_LIGHT),
        ]):
            sx = ent_x + Inches(0.3) + i * (ent_stat_w + stat_gap)
            self._stat_box(s, val, lbl, sx, stat_y, ent_stat_w, stat_h,
                           val_color=vc, bg=bg)

        # ══════════════════════════════════════════════════════
        #  PAG CARD (right, slightly smaller)
        # ══════════════════════════════════════════════════════
        self._card(s, pag_x, cards_y, pag_w, pag_h,
                   fill=self.WHITE, border=self.AMBER)

        # Amber top accent line
        self._bar_rect(s, pag_x + Pt(4), cards_y + Pt(2),
                       pag_w - Pt(8), Pt(3), self.AMBER)

        # Label
        self._txt(s, 'OPTION B · PAY AS YOU GROW',
                  pag_x + Inches(0.3), cards_y + Inches(0.18),
                  Inches(3.5), Inches(0.25),
                  size=Pt(9), color=self.AMBER, bold=True)

        # PAG year-by-year
        pag_yr_x = pag_x + Inches(0.4)
        pag_yr_w = Inches(2.8)
        pag_yr_top = cards_y + Inches(0.6)

        pag_years = [
            ('Year 1', '£2.7M', '30% volume discount'),
            ('Year 2', '£3.5M', '30% volume discount'),
            ('Year 3+', '£4.8M', '30% volume discount'),
        ]

        for i, (yr, price, discount) in enumerate(pag_years):
            y = pag_yr_top + i * yr_spacing
            if i % 2 == 0:
                self._bar_rect(s, pag_x + Inches(0.2), y - Pt(1),
                               Inches(3.2), Inches(0.27),
                               RGBColor(0xFF, 0xFB, 0xF2))
            self._txt(s, yr, pag_yr_x, y, Inches(1.1), Inches(0.25),
                      size=Pt(11), color=self.SUB_TEXT)
            self._txt(s, price, pag_yr_x + Inches(1.1), y, Inches(0.9), Inches(0.25),
                      size=Pt(14), color=self.DARK_TEXT, bold=True,
                      align=PP_ALIGN.RIGHT)
            self._txt(s, discount, pag_yr_x + Inches(2.1), y + Pt(1), Inches(1.5), Inches(0.25),
                      size=Pt(8), color=self.GREEN)

        # PAG description
        self._txt(s, 'Modular activation. Licence grows as modules go live.\n\nAI capabilities unlock progressively with tier upgrades.\n\nAgentic Runtime from Year 1.',
                  pag_x + Inches(0.4), cards_y + Inches(1.55), Inches(4.2), Inches(1.6),
                  size=Pt(9), color=self.SUB_TEXT)

        # PAG stat boxes (3 boxes matching Enterprise)
        pag_stat_w = (pag_w - Inches(0.6) - 2 * stat_gap) / 3
        for i, (val, lbl, vc, bg) in enumerate([
            ('£20.7M', '5-YR LICENCE', self.AMBER, self.AMBER_LIGHT),
            ('~5.9×', 'ROI', self.GREEN, self.GREEN_LIGHT),
            ('Month 9', 'BREAKEVEN', self.PURPLE, self.PURPLE_LIGHT),
        ]):
            sx = pag_x + Inches(0.3) + i * (pag_stat_w + stat_gap)
            self._stat_box(s, val, lbl, sx, stat_y, pag_stat_w, stat_h,
                           val_color=vc, bg=bg)

        # ══════════════════════════════════════════════════════
        #  MIDDLE CALLOUT STATS (below cards)
        # ══════════════════════════════════════════════════════
        callout_y = cards_y + ent_h + Inches(0.25)
        callout_w = Inches(2.6)
        callout_h = Inches(0.55)
        callout_gap = Inches(0.3)
        total_callout_w = 2 * callout_w + callout_gap
        callout_start = (self.SLIDE_W - total_callout_w) / 2

        self._stat_box(s, '£495K', 'AGENTIC RUNTIME (INCLUDED)',
                       callout_start, callout_y, callout_w, callout_h,
                       val_color=self.PURPLE, bg=self.PURPLE_LIGHT)
        self._stat_box(s, '5', 'MARKETPLACE VENDORS INCLUDED',
                       callout_start + callout_w + callout_gap, callout_y,
                       callout_w, callout_h,
                       val_color=self.DARK_TEXT, bg=self.STAT_BG)

        # ══════════════════════════════════════════════════════
        #  KEY INSIGHT BAR (bottom)
        # ══════════════════════════════════════════════════════
        insight_y = callout_y + callout_h + Inches(0.25)
        self._insight_card(s, 'KEY INSIGHT',
            'Enterprise is £0.4M less in Year 1 and £3.7M less over five years. '
            'Every price increase maps to a specific module or connector activation. '
            'Nothing is arbitrary.',
            self.ML, insight_y, self.CW, Inches(0.6))

        # ── Footer ───────────────────────────────────────────
        self._footer(s, slide_number=4)

    def generate(self, output_path):
        self._init_presentation()
        self._build_september_slide()
        self._build_commercial_model()
        self.save(output_path)


if __name__ == '__main__':
    out_dir = Path(__file__).resolve().parent.parent / 'Engagement' / 'Schroders Group' / 'Output'
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / 'schroders_commercial_model_slide.pptx'

    gen = CommercialModelSlide()
    gen.generate(str(out_path))
    print(f'✓ Generated {out_path} ({out_path.stat().st_size / 1024:.0f} KB)')

#!/usr/bin/env python3
"""
Evelyn Partners — 3 Business Outcome slides for the April 15 Proposal.

Insert these after the Advisor Workspace / AI section (slide 16)
and before the Commercial Offer section (slide 21).

Slides:
  1. "Why Now" — Three forcing functions
  2. "Business Outcomes That Matter" — 4 quantified outcome cards
  3. "The Cost of Standing Still" — Two-column comparison table

Usage:
    python3 tools/evelyn_business_outcomes_pptx.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.pptx_presenter import PptxPresenter
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE


class EvelynBusinessOutcomes(PptxPresenter):
    """Generates 3 business outcome slides for Evelyn Partners proposal."""

    # Accent colors for the forcing-function icons
    ICON_RENEWAL = RGBColor(0x33, 0x66, 0xFF)   # blue
    ICON_ACQUIS  = RGBColor(0x7B, 0x2F, 0xFF)   # purple
    ICON_AI      = RGBColor(0x05, 0x96, 0x69)    # green

    def generate(self, output_path: str):
        self._init_presentation()
        self._slide_section_divider()
        self._slide_why_now()
        self._slide_business_outcomes()
        self._slide_cost_of_standing_still()
        self.save(output_path)

    # ── Slide 0: Section divider ─────────────────────────
    def _slide_section_divider(self):
        s = self._slide_cover(
            title_lines=[
                ('Business Case', self.WHITE),
                ('for Change', self.CYAN_BRIGHT),
            ],
            subtitle='Why this matters for Evelyn — beyond the renewal',
            label='STRATEGIC PARTNERSHIP PROPOSAL',
        )

    # ── Slide 1: Why Now ─────────────────────────────────
    def _slide_why_now(self):
        s = self._new_slide(dark=True)
        self._section_label(s, 'BUSINESS CASE FOR CHANGE', dark=True)
        self._heading(s, 'A Convergence of ', accent='Timing and Ambition',
                      dark=True, size=Pt(32))
        self._subtitle(
            s,
            'Three forces align to make this the right moment for Evelyn to act.',
            dark=True,
        )

        # Three forcing-function cards
        card_w = Inches(3.7)
        card_h = Inches(3.5)
        gap = Inches(0.5)
        total = 3 * card_w + 2 * gap
        start_x = (self.SLIDE_W - total) / 2
        card_top = Inches(2.3)

        cards = [
            {
                'icon_color': self.ICON_RENEWAL,
                'number': '01',
                'title': 'Renewal Window',
                'body': (
                    'Contract renewal in May 2027 creates a natural decision '
                    'point. Early action secures preferential terms, avoids '
                    'disruption, and locks in the upgrade path before the '
                    'current stack reaches end-of-support.'
                ),
            },
            {
                'icon_color': self.ICON_ACQUIS,
                'number': '02',
                'title': 'Post-Acquisition Scrutiny',
                'body': (
                    'NatWest ownership brings new governance, new reporting '
                    'standards, and heightened expectations on operational '
                    'efficiency. The digital platform must be board-ready — '
                    'not legacy-dependent.'
                ),
            },
            {
                'icon_color': self.ICON_AI,
                'number': '03',
                'title': 'AI Momentum',
                'body': (
                    'The successful AI POC proved the art of the possible. '
                    'Waiting risks losing internal champions and falling '
                    'behind peers who are moving to production AI now. '
                    'The window to capitalise is open.'
                ),
            },
        ]

        for i, c in enumerate(cards):
            cx = start_x + i * (card_w + gap)

            # Card background
            self._card(s, cx, card_top, card_w, card_h, dark=True)

            # Numbered circle
            circle_size = Inches(0.5)
            circle = s.shapes.add_shape(
                MSO_SHAPE.OVAL, cx + Inches(0.25), card_top + Inches(0.3),
                circle_size, circle_size,
            )
            circle.fill.solid()
            circle.fill.fore_color.rgb = c['icon_color']
            circle.line.fill.background()

            self._txt(
                s, c['number'],
                cx + Inches(0.25), card_top + Inches(0.33),
                circle_size, circle_size,
                size=Pt(14), color=self.WHITE, bold=True,
                align=PP_ALIGN.CENTER,
            )

            # Title
            self._txt(
                s, c['title'],
                cx + Inches(0.25), card_top + Inches(1.0),
                card_w - Inches(0.5), Inches(0.4),
                size=Pt(16), color=self.WHITE, bold=True,
            )

            # Body
            self._txt(
                s, c['body'],
                cx + Inches(0.25), card_top + Inches(1.5),
                card_w - Inches(0.5), Inches(1.8),
                size=Pt(11), color=self.MUTED,
            )

        # Bottom-line quote
        self._txt(
            s,
            '"The question is not whether to modernise — '
            'it\'s whether to do it on your terms or under pressure."',
            Inches(1.5), Inches(6.3), Inches(10), Inches(0.5),
            size=Pt(12), color=self.CYAN_BRIGHT, bold=False,
            align=PP_ALIGN.CENTER,
        )

        self._footer(s, 2, dark=True)

    # ── Slide 2: Business Outcomes ───────────────────────
    def _slide_business_outcomes(self):
        s = self._new_slide(dark=False)
        self._section_label(s, 'BUSINESS CASE FOR CHANGE')
        self._heading(s, 'What This Means ', accent='for Evelyn', size=Pt(32))
        self._subtitle(s, 'Quantified business outcomes from the platform upgrade and AI enablement.')

        # 4 outcome cards in a 2x2 grid
        card_w = Inches(5.8)
        card_h = Inches(2.15)
        gap_x = Inches(0.5)
        gap_y = Inches(0.35)
        grid_left = self.ML
        grid_top = Inches(2.0)

        outcomes = [
            {
                'stat': '40%',
                'label': 'Reduction in Advisor Admin Time',
                'body': (
                    'Advisor Workspace and AI assistants shift advisors from '
                    'data gathering to client engagement. Industry benchmark: '
                    'advisors spend 60%+ of time on admin; best-in-class is '
                    'under 40%.'
                ),
                'accent_color': self.BLUE,
                'bg': self.BLUE_LIGHT,
            },
            {
                'stat': '4x Faster',
                'label': 'Meeting Preparation',
                'body': (
                    'AI-powered meeting preparation — demonstrated in the '
                    'Evelyn POC — reduces prep from 2+ hours to under 30 '
                    'minutes per client meeting. Immediate, measurable savings '
                    'per advisor, per day.'
                ),
                'accent_color': self.GREEN,
                'bg': self.GREEN_LIGHT,
            },
            {
                'stat': '6x',
                'label': 'Faster Client Onboarding',
                'body': (
                    'Wealth 2.0 digital onboarding with document vault and '
                    'e-signature compresses onboarding from weeks to days. '
                    'Peer benchmark: 31 days to 5 days — a competitive '
                    'advantage in client acquisition.'
                ),
                'accent_color': self.PURPLE,
                'bg': self.PURPLE_LIGHT,
            },
            {
                'stat': 'Lower TCO',
                'label': 'Platform Consolidation',
                'body': (
                    'Moving from custom legacy to product-standard reduces '
                    'maintenance burden, eliminates custom code risk, and '
                    'positions for continuous innovation — without bespoke '
                    'upgrade cycles.'
                ),
                'accent_color': self.AMBER,
                'bg': self.AMBER_LIGHT,
            },
        ]

        for idx, o in enumerate(outcomes):
            col = idx % 2
            row = idx // 2
            cx = grid_left + col * (card_w + gap_x)
            cy = grid_top + row * (card_h + gap_y)

            # Card
            self._card(s, cx, cy, card_w, card_h)

            # Colored top accent line
            self._colored_top_line(s, cx, cy, card_w, o['accent_color'])

            # Stat number
            self._txt(
                s, o['stat'],
                cx + Inches(0.3), cy + Inches(0.25),
                card_w - Inches(0.6), Inches(0.55),
                size=Pt(36), color=o['accent_color'], bold=True,
            )

            # Label
            self._txt(
                s, o['label'].upper(),
                cx + Inches(0.3), cy + Inches(0.9),
                card_w - Inches(0.6), Inches(0.3),
                size=Pt(9), color=self.DARK_TEXT, bold=True,
            )

            # Body text
            self._txt(
                s, o['body'],
                cx + Inches(0.3), cy + Inches(1.2),
                card_w - Inches(0.6), Inches(0.85),
                size=Pt(10), color=self.SUB_TEXT,
            )

        # Source attribution
        self._txt(
            s,
            'Benchmarks from Backbase wealth management engagements '
            '(Goodbody, HNB, industry analysis)',
            self.ML, Inches(6.85), self.CW, Inches(0.3),
            size=Pt(7), color=self.MUTED,
        )

        self._footer(s, 3)

    # ── Slide 3: Cost of Standing Still ──────────────────
    def _slide_cost_of_standing_still(self):
        s = self._new_slide(dark=True)
        self._section_label(s, 'BUSINESS CASE FOR CHANGE', dark=True)
        self._heading(s, 'What Happens If ', accent='Nothing Changes',
                      dark=True, size=Pt(32))
        self._subtitle(
            s,
            'A side-by-side view: auto-renewal on the current stack vs. '
            'early renewal with upgrade.',
            dark=True,
        )

        # Two-column comparison
        col_w = Inches(5.5)
        col_gap = Inches(0.6)
        total = 2 * col_w + col_gap
        start_x = (self.SLIDE_W - total) / 2
        col_top = Inches(2.2)
        col_h = Inches(3.8)

        # ── Left column: Stay on Current ──
        lx = start_x
        self._card(s, lx, col_top, col_w, col_h, dark=True,
                   border=RGBColor(0x3D, 0x1A, 0x1A))
        self._colored_top_line(s, lx, col_top, col_w, self.RED)

        self._txt(
            s, 'STAY ON CURRENT STACK',
            lx + Inches(0.3), col_top + Inches(0.2),
            col_w - Inches(0.6), Inches(0.3),
            size=Pt(11), color=self.RED, bold=True,
        )

        left_items = [
            'Custom code = growing maintenance cost',
            'Manual advisor workflows persist',
            'Legacy onboarding = slow client acquisition',
            'No AI foundation = starting from scratch later',
            'Harder to demonstrate value to NatWest board',
        ]

        item_y = col_top + Inches(0.7)
        for item in left_items:
            # Red dash prefix
            self._txt(
                s, f'\u2014  {item}',
                lx + Inches(0.3), item_y,
                col_w - Inches(0.6), Inches(0.45),
                size=Pt(11), color=self.MUTED,
            )
            item_y += Inches(0.55)

        # ── Right column: Move to Wealth 2.0 + AI ──
        rx = start_x + col_w + col_gap
        self._card(s, rx, col_top, col_w, col_h, dark=True,
                   border=RGBColor(0x0A, 0x3D, 0x2A))
        self._colored_top_line(s, rx, col_top, col_w, self.GREEN)

        self._txt(
            s, 'MOVE TO WEALTH 2.0 + AI',
            rx + Inches(0.3), col_top + Inches(0.2),
            col_w - Inches(0.6), Inches(0.3),
            size=Pt(11), color=self.GREEN, bold=True,
        )

        right_items = [
            'Product-standard = continuous innovation',
            'AI-augmented advisors from day one',
            'Digital-first onboarding = competitive advantage',
            'POC momentum \u2192 production in 2027',
            'Clear modernisation story for new ownership',
        ]

        item_y = col_top + Inches(0.7)
        for item in right_items:
            self._txt(
                s, f'\u2714  {item}',
                rx + Inches(0.3), item_y,
                col_w - Inches(0.6), Inches(0.45),
                size=Pt(11), color=self.MUTED,
            )
            item_y += Inches(0.55)

        # Bottom-line quote
        self._txt(
            s,
            '"Auto-renewal preserves the status quo. Early renewal with '
            'upgrade positions Evelyn as a digital leader under NatWest '
            '— at preferential economics."',
            Inches(1.5), Inches(6.3), Inches(10), Inches(0.5),
            size=Pt(12), color=self.CYAN_BRIGHT, bold=False,
            align=PP_ALIGN.CENTER,
        )

        self._footer(s, 4, dark=True)


if __name__ == '__main__':
    out = 'Evelyn_Business_Outcomes.pptx'
    deck = EvelynBusinessOutcomes()
    deck.generate(out)
    print(f'\nInsert these slides after slide 16 (AI features) '
          f'and before slide 21 (Commercial Offer) in the main deck.')

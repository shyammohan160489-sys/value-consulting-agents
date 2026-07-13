#!/usr/bin/env python3
"""
Evelyn Partners — Options to Consider + Mutual Activity Plan slides.

Slides:
  1. "Three Paths Forward" — 3-column options comparison
  2. "Mutual Activity Plan" — Timeline from April to October 2026

Usage:
    python3 tools/evelyn_options_pptx.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.pptx_presenter import PptxPresenter
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE


class EvelynOptions(PptxPresenter):
    """Generates Options + Activity Plan slides for Evelyn Partners."""

    def generate(self, output_path: str):
        self._init_presentation()
        self._slide_options()
        self._slide_activity_plan()
        self.save(output_path)

    # ── Slide 1: Three Paths Forward ─────────────────────
    def _slide_options(self):
        s = self._new_slide(dark=True)
        self._section_label(s, 'PATH FORWARD', dark=True)
        self._heading(s, 'Three Paths ', accent='to Consider', dark=True, size=Pt(30))
        self._subtitle(s, 'Each path reflects a different level of commitment — and a different level of Backbase investment.', dark=True)

        # Three columns
        col_w = Inches(3.7)
        col_h = Inches(4.5)
        gap = Inches(0.45)
        total = 3 * col_w + 2 * gap
        start_x = (self.SLIDE_W - total) / 2
        col_top = Inches(2.1)

        options = [
            {
                'title': 'Auto-Renew',
                'subtitle': 'Do Nothing',
                'accent': self.MUTED,
                'border': RGBColor(0x47, 0x55, 0x69),
                'items': [
                    '12-month rolling renewal',
                    'Stay on current LTS 2409',
                    'Extended support becomes chargeable (Oct 2026)',
                    'No Backbase investment',
                ],
                'risk': 'Unsupported Alpha stack core when NatWest arrives. No innovation story. Reactive.',
                'bb_invest': 'None',
                'natwest': 'Weak',
                'invest_color': self.MUTED,
                'badge': None,
            },
            {
                'title': 'Upgrade Only',
                'subtitle': 'Stay Current',
                'accent': self.AMBER,
                'border': RGBColor(0x4A, 0x3A, 0x1A),
                'items': [
                    'Upgrade to LTS 26.09',
                    'Short-term renewal (1-2 years)',
                    'Digital Wealth Essentials (parity)',
                    'Evelyn funds the upgrade',
                ],
                'risk': 'Current but not competitive. No advisor workspace, no AI, no NatWest story.',
                'bb_invest': 'Limited',
                'natwest': 'Moderate',
                'invest_color': self.AMBER,
                'badge': None,
            },
            {
                'title': 'Strategic Partnership',
                'subtitle': 'Commit & Innovate',
                'accent': self.BLUE,
                'border': RGBColor(0x1A, 0x2E, 0x5E),
                'items': [
                    'Multi-year renewal (3-5 years)',
                    '26.09 + Digital Wealth Premium',
                    'Advisor Workspace + AI capabilities',
                    'Backbase invests in the upgrade',
                    'Incremental discounting on commitment',
                ],
                'risk': 'Positions Evelyn as digital leader under NatWest. Proactive, not reactive.',
                'bb_invest': 'Material',
                'natwest': 'Strong',
                'invest_color': self.GREEN,
                'badge': 'RECOMMENDED',
            },
        ]

        for i, o in enumerate(options):
            cx = start_x + i * (col_w + gap)

            # Card background
            card = self._card(s, cx, col_top, col_w, col_h, dark=True,
                              border=o['border'])

            # Top accent line
            self._colored_top_line(s, cx, col_top, col_w, o['accent'])

            # RECOMMENDED badge
            if o['badge']:
                badge_w = Inches(1.3)
                badge_h = Inches(0.22)
                badge_x = cx + col_w - badge_w - Inches(0.15)
                badge_y = col_top + Inches(0.12)
                badge = self._bar_rect(s, badge_x, badge_y, badge_w, badge_h, self.BLUE)
                self._txt(s, o['badge'], badge_x, badge_y + Inches(0.02),
                          badge_w, badge_h,
                          size=Pt(7), color=self.WHITE, bold=True,
                          align=PP_ALIGN.CENTER)

            # Option title
            self._txt(s, o['title'],
                      cx + Inches(0.25), col_top + Inches(0.2),
                      col_w - Inches(0.5), Inches(0.35),
                      size=Pt(15), color=self.WHITE, bold=True)

            # Option subtitle
            self._txt(s, o['subtitle'],
                      cx + Inches(0.25), col_top + Inches(0.52),
                      col_w - Inches(0.5), Inches(0.2),
                      size=Pt(9), color=o['accent'], bold=True)

            # Divider line
            self._bar_rect(s, cx + Inches(0.25), col_top + Inches(0.8),
                          col_w - Inches(0.5), Pt(1),
                          fill=RGBColor(0x1E, 0x2D, 0x45))

            # Bullet items
            item_y = col_top + Inches(0.95)
            for item in o['items']:
                self._txt(s, f'\u2192 {item}',
                          cx + Inches(0.25), item_y,
                          col_w - Inches(0.5), Inches(0.32),
                          size=Pt(9), color=self.MUTED)
                item_y += Inches(0.32)

            # Risk/outcome text
            self._txt(s, o['risk'],
                      cx + Inches(0.25), col_top + Inches(3.0),
                      col_w - Inches(0.5), Inches(0.65),
                      size=Pt(8), color=o['accent'], bold=False)

            # Bottom metrics row
            metrics_y = col_top + col_h - Inches(0.7)
            self._bar_rect(s, cx + Inches(0.1), metrics_y,
                          col_w - Inches(0.2), Pt(1),
                          fill=RGBColor(0x1E, 0x2D, 0x45))

            # Backbase Investment label + value
            self._txt(s, 'BB INVESTMENT',
                      cx + Inches(0.25), metrics_y + Inches(0.1),
                      Inches(1.5), Inches(0.15),
                      size=Pt(6), color=self.MUTED, bold=True)
            self._txt(s, o['bb_invest'],
                      cx + Inches(0.25), metrics_y + Inches(0.25),
                      Inches(1.5), Inches(0.2),
                      size=Pt(11), color=o['invest_color'], bold=True)

            # NatWest Readiness label + value
            self._txt(s, 'NATWEST READINESS',
                      cx + Inches(2.0), metrics_y + Inches(0.1),
                      Inches(1.5), Inches(0.15),
                      size=Pt(6), color=self.MUTED, bold=True)
            self._txt(s, o['natwest'],
                      cx + Inches(2.0), metrics_y + Inches(0.25),
                      Inches(1.5), Inches(0.2),
                      size=Pt(11), color=o['invest_color'], bold=True)

        self._footer(s, 1, dark=True)

    # ── Slide 2: Mutual Activity Plan ────────────────────
    def _slide_activity_plan(self):
        s = self._new_slide(dark=False)
        self._section_label(s, 'PATH FORWARD')
        self._heading(s, 'Mutual Activity Plan ', accent='| April 2026', size=Pt(26))
        self._subtitle(s, 'Proposed timeline from strategic alignment to contract signature and upgrade kickoff.')

        milestones = [
            ['1', 'Strategic Alignment', 'Confirm appetite, identify decision-makers, agree next steps', 'April 15, 2026', 'This Meeting'],
            ['2', 'Joint Solution Deep-Dives', '2-3 workshops: solution scope, integration mapping, bill of materials', 'Late Apr – May 2026', 'Both Teams'],
            ['3', 'Validated Solution Scope', 'Agreed feature set, product editions, integration requirements', 'End May 2026', 'Backbase'],
            ['4', 'NatWest Regulatory Green Light', 'FCA approval enables NatWest–Evelyn communication', 'June 2026', 'Evelyn / NatWest'],
            ['5', 'Business Case for NatWest', 'ROI model + executive decision paper for Bids / Paul Gettis', 'June–July 2026', 'Both Teams'],
            ['6', 'Commercial Proposal (B&F)', 'Best & final offer: licensing, services, investment structure', 'July 2026', 'Backbase'],
            ['7', 'Contract Negotiation', 'Legal review, procurement (Peter), MSA amendments', 'August 2026', 'Both Teams'],
            ['8', 'Contract Signature', 'Renewal + product upsell + services commitment', 'September 2026', 'Both'],
            ['9', 'LTS 26.09 Upgrade Kickoff', 'Backbase-led upgrade with Michiel\'s services investment', 'October 2026', 'Both'],
        ]

        headers = ['#', 'Milestone', 'Description', 'Target Date', 'Owner']
        col_widths = [0.3, 1.6, 4.2, 1.5, 1.2]

        rows = [headers] + milestones
        self._add_table(s, rows, col_widths,
                        left=Inches(0.6), top=Inches(1.7),
                        row_height=Inches(0.48),
                        body_size=Pt(7.5))

        # Call to action
        self._txt(s,
                  'Immediate ask: Confirm Option 3 appetite  \u2192  Schedule deep-dive workshops  \u2192  Identify NatWest decision-maker',
                  Inches(0.6), Inches(6.7), Inches(11.5), Inches(0.3),
                  size=Pt(9), color=self.BLUE, bold=True)

        self._footer(s, 2)


if __name__ == '__main__':
    out = 'Engagement/Evelyn Partners/Output/Evelyn_Options_and_Plan.pptx'
    deck = EvelynOptions()
    deck.generate(out)

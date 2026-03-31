#!/usr/bin/env python3
"""
CIH Bank — Commercial Proposal PPTX Generator

16-slide executive briefing matching CIH_Executive_Proposal.html v2.3.
Google Slides compatible (13.333" × 7.5" widescreen). Backbase brand.

Usage:
    python3 tools/cih_commercial_pptx.py
"""

import sys
sys.path.insert(0, '/Users/shyam/cortex')

from tools.pptx_presenter import PptxPresenter
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN


class CIHCommercialPptx(PptxPresenter):
    """Generates 16-slide CIH Bank commercial proposal PPTX."""

    def generate(self, output_path):
        self._init_presentation()
        n = 0

        # ── 1. COVER ──────────────────────────────────────────
        n += 1
        self._slide_cover(
            title_lines=[
                ('Deepening Customer Value', self.WHITE),
                ('with CIH Bank.', self.GREEN),
            ],
            subtitle='Managed Hosting · Digital Assist Premium · Customer Lifecycle Orchestrator',
            label='UPSELL PROPOSAL · MARCH 2026 · CONFIDENTIAL',
            pills=[
                ('500K Wallet-Only Users', self.RED),
                ('3.5M Target Users', self.BLUE),
                ('€3.6M Annual Value', self.GREEN),
            ],
        )

        # ── 2. OUR JOURNEY TOGETHER ───────────────────────────
        n += 1
        s = self._slide_content('OUR PARTNERSHIP', 'Five years of ',
                                'digital growth.', slide_number=n)
        # Timeline
        phases = [
            ('Jul 2019', 'Backbase Selected', 'Digital banking platform chosen'),
            ('2020-21', 'Core Launch', 'Retail & SME banking live'),
            ('2022-23', 'Scale', '2M+ active digital users'),
            ('Jul 2024', 'Contract Renewal', '5-year renewal through Jul 2029'),
            ('2026', 'Next Phase', 'Upsell: MH + DA + CLO'),
        ]
        line_y = Inches(2.4)
        self._divider(s, line_y, color=self.BLUE)
        step_w = self.CW / len(phases)
        for i, (date, title, desc) in enumerate(phases):
            cx = self.ML + i * step_w + step_w / 2
            dot_size = Inches(0.12)
            color = self.GREEN if i < 4 else self.BLUE
            self._bar_rect(s, cx - dot_size / 2, line_y - dot_size / 2,
                           dot_size, dot_size, fill=color)
            self._txt(s, date, cx - Inches(0.7), line_y + Inches(0.2),
                      Inches(1.4), Inches(0.2),
                      size=Pt(8), bold=True, color=self.DARK_TEXT,
                      align=PP_ALIGN.CENTER)
            self._txt(s, title, cx - Inches(0.7), line_y + Inches(0.4),
                      Inches(1.4), Inches(0.2),
                      size=Pt(9), bold=True, color=color,
                      align=PP_ALIGN.CENTER)
            self._txt(s, desc, cx - Inches(0.7), line_y + Inches(0.6),
                      Inches(1.4), Inches(0.3),
                      size=Pt(7), color=self.SUB_TEXT,
                      align=PP_ALIGN.CENTER)
        # Summary stats
        gap = Inches(0.2)
        sw = (self.CW - 3 * gap) / 4
        stats = [
            ('2M+', 'Active Users', self.GREEN, self.GREEN_LIGHT),
            ('7 yrs', 'Partnership', self.BLUE, self.BLUE_LIGHT),
            ('€5.85M', 'Current TCV', self.PURPLE, self.PURPLE_LIGHT),
            ('Jul 2029', 'Contract End', self.AMBER, self.AMBER_LIGHT),
        ]
        for i, (val, lbl, vc, bg) in enumerate(stats):
            self._stat_box(s, val, lbl,
                           self.ML + i * (sw + gap), Inches(4.0), sw, Inches(0.55),
                           val_color=vc, bg=bg)

        # ── 3. STRATEGIC PRIORITIES ───────────────────────────
        n += 1
        s = self._slide_content('CIH STRATEGY', "CIH Bank's digital ",
                                'ambition.', slide_number=n)
        priorities = [
            ('GROW DIGITAL REVENUE', 'Convert 500K wallet-only users into product holders through digital origination and cross-sell campaigns.', self.GREEN),
            ('MODERNIZE INFRASTRUCTURE', 'Migrate to managed hosting to reduce ops burden, improve uptime, and free engineering capacity.', self.BLUE),
            ('EMPOWER BANQUE DIRECTE', 'Equip 50 remote advisors with AI-assisted tools to increase selling time and revenue per agent.', self.PURPLE),
        ]
        card_w = (self.CW - 2 * gap) / 3
        for i, (title, desc, color) in enumerate(priorities):
            x = self.ML + i * (card_w + gap)
            y = self.CT
            self._card(s, x, y, card_w, Inches(1.6))
            self._colored_top_line(s, x, y, card_w, color)
            self._txt(s, title, x + Inches(0.15), y + Inches(0.15),
                      card_w - Inches(0.3), Inches(0.2),
                      size=Pt(8), bold=True, color=color)
            self._txt(s, desc, x + Inches(0.15), y + Inches(0.45),
                      card_w - Inches(0.3), Inches(1.0),
                      size=Pt(9), color=self.SUB_TEXT)

        # ── 4. THE OPPORTUNITY ────────────────────────────────
        n += 1
        s = self._slide_content('THE OPPORTUNITY', 'Three interconnected ',
                                'growth plays.', slide_number=n)
        opps = [
            ('WALLET-ONLY UPSELL', '500K users with wallets but no products. CLO identifies propensity, triggers personalized offers, converts to product holders.', self.GREEN, '€1.1M'),
            ('PRODUCT ORIGINATION', 'Digital-first loan, card, and insurance origination. End-to-end journeys replace manual branch processes.', self.BLUE, '€1.88M'),
            ('OPERATIONAL EFFICIENCY', 'Managed hosting eliminates infra overhead. DA Premium frees agent time for revenue generation.', self.PURPLE, '€600K'),
        ]
        for i, (title, desc, color, value) in enumerate(opps):
            x = self.ML + i * (card_w + gap)
            y = self.CT
            self._card(s, x, y, card_w, Inches(2.0))
            self._colored_top_line(s, x, y, card_w, color)
            self._txt(s, title, x + Inches(0.15), y + Inches(0.15),
                      card_w - Inches(0.3), Inches(0.2),
                      size=Pt(8), bold=True, color=color)
            self._txt(s, desc, x + Inches(0.15), y + Inches(0.45),
                      card_w - Inches(0.3), Inches(1.0),
                      size=Pt(8), color=self.SUB_TEXT)
            self._txt(s, value, x + Inches(0.15), y + Inches(1.5),
                      card_w - Inches(0.3), Inches(0.3),
                      size=Pt(18), bold=True, color=color,
                      align=PP_ALIGN.RIGHT)
            self._txt(s, 'annual value', x + Inches(0.15), y + Inches(1.75),
                      card_w - Inches(0.3), Inches(0.15),
                      size=Pt(7), color=self.MUTED, align=PP_ALIGN.RIGHT)

        # ── 5. VALUE AT STAKE ─────────────────────────────────
        n += 1
        s = self._slide_dark_feature('VALUE AT STAKE',
                                     '€3.6M ', 'per year in untapped value.',
                                     subtitle_text='Product origination, cross-sell, revenue generation, branch reduction, and ops efficiency — quantified conservatively.',
                                     slide_number=n)
        gap = Inches(0.3)
        sw = (self.CW - 3 * gap) / 4
        value_stats = [
            ('€1.1M', 'Product origination\n& cross-sell', self.GREEN),
            ('€300K', 'DA revenue\ngeneration', self.PURPLE),
            ('€1.88M', 'Branch traffic\nreduction', self.AMBER),
            ('€300K', 'MH ops\nsavings', self.BLUE),
        ]
        for i, (val, lbl, vc) in enumerate(value_stats):
            x = self.ML + i * (sw + gap)
            self._card(s, x, Inches(3.0), sw, Inches(0.8), dark=True)
            self._txt(s, val, x, Inches(3.06), sw, Inches(0.35),
                      size=Pt(22), bold=True, color=vc,
                      align=PP_ALIGN.CENTER)
            self._txt(s, lbl, x, Inches(3.45), sw, Inches(0.3),
                      size=Pt(7), color=self.MUTED,
                      align=PP_ALIGN.CENTER)

        # ── 6. WHAT YOU'RE BUYING ─────────────────────────────
        n += 1
        s = self._slide_content('SCOPE', 'Three modules, ',
                                'one growth platform.',
                                subtitle_text='Each module addresses a specific strategic priority. Together, they unlock the full €3.6M value.',
                                slide_number=n)
        modules = [
            ('MANAGED HOSTING\nENTERPRISE 2', 'Infrastructure', 'Fully managed cloud hosting. Eliminates internal infra team, guarantees SLA uptime, frees engineering for product work.', self.BLUE, '€541,575/yr'),
            ('DIGITAL ASSIST\nPREMIUM', 'Agent Enablement', '50-seat AI-assisted advisor platform for Banque Directe. Frees 20% of agent time from admin → revenue-generating activities.', self.PURPLE, '€210,084/yr'),
            ('CUSTOMER LIFECYCLE\nORCHESTRATOR', 'Revenue Engine', 'Propensity-driven campaigns targeting 500K wallet-only users. Personalized product origination at scale.', self.GREEN, '€515,071/yr'),
        ]
        card_w = (self.CW - 2 * gap) / 3
        for i, (title, cat, desc, color, price) in enumerate(modules):
            x = self.ML + i * (card_w + gap)
            y = Inches(1.8)
            self._card(s, x, y, card_w, Inches(2.6))
            self._colored_top_line(s, x, y, card_w, color)
            self._txt(s, cat.upper(), x + Inches(0.15), y + Inches(0.12),
                      card_w - Inches(0.3), Inches(0.15),
                      size=Pt(7), bold=True, color=color)
            self._txt(s, title, x + Inches(0.15), y + Inches(0.3),
                      card_w - Inches(0.3), Inches(0.45),
                      size=Pt(11), bold=True, color=self.DARK_TEXT)
            self._txt(s, desc, x + Inches(0.15), y + Inches(0.85),
                      card_w - Inches(0.3), Inches(1.0),
                      size=Pt(8), color=self.SUB_TEXT)
            self._txt(s, price, x + Inches(0.15), y + Inches(2.1),
                      card_w - Inches(0.3), Inches(0.3),
                      size=Pt(12), bold=True, color=color,
                      align=PP_ALIGN.CENTER)

        # ── 7. WHY CLO ────────────────────────────────────────
        n += 1
        s = self._slide_content('WHY CLO', 'From wallets to ',
                                'product holders.',
                                subtitle_text='500K CIH users have wallets but no products. CLO turns passive users into revenue-generating customers.',
                                slide_number=n)
        steps = [
            ('1', 'IDENTIFY', 'AI analyzes 500K wallet-only users.\nPropensity scoring ranks by conversion likelihood.', self.BLUE),
            ('2', 'ENGAGE', 'Personalized campaigns via push, email, in-app.\nRight product, right time, right channel.', self.PURPLE),
            ('3', 'CONVERT', 'End-to-end digital origination.\n5% target conversion = 25,000 new product holders.', self.GREEN),
        ]
        step_w = (self.CW - 2 * gap) / 3
        for i, (num, title, desc, color) in enumerate(steps):
            x = self.ML + i * (step_w + gap)
            y = Inches(1.8)
            self._card(s, x, y, step_w, Inches(1.5))
            self._colored_top_line(s, x, y, step_w, color)
            # Step number
            self._txt(s, num, x + Inches(0.15), y + Inches(0.12),
                      Inches(0.3), Inches(0.3),
                      size=Pt(20), bold=True, color=color)
            self._txt(s, title, x + Inches(0.5), y + Inches(0.15),
                      step_w - Inches(0.65), Inches(0.2),
                      size=Pt(9), bold=True, color=color)
            self._txt(s, desc, x + Inches(0.15), y + Inches(0.55),
                      step_w - Inches(0.3), Inches(0.8),
                      size=Pt(8), color=self.SUB_TEXT)
        # Impact stat
        self._stat_box(s, '€1.1M', 'ANNUAL VALUE FROM CLO ALONE',
                       self.ML + Inches(4), Inches(3.8),
                       Inches(4), Inches(0.6),
                       val_color=self.GREEN, bg=self.GREEN_LIGHT)

        # ── 8. COMMERCIAL OPTIONS (comparison) ────────────────
        n += 1
        s = self._slide_content('COMMERCIAL OPTIONS', 'Two options, ',
                                'one decision.', slide_number=n)
        half_w = (self.CW - gap) / 2
        y = self.CT

        # Option 1 card (standard)
        self._card(s, self.ML, y, half_w, Inches(3.6))
        self._txt(s, 'OPTION 1', self.ML + Inches(0.2), y + Inches(0.15),
                  Inches(2), Inches(0.2),
                  size=Pt(8), bold=True, color=self.BLUE)
        self._txt(s, '3-Year Co-Term', self.ML + Inches(0.2), y + Inches(0.35),
                  half_w - Inches(0.4), Inches(0.3),
                  size=Pt(16), bold=True, color=self.DARK_TEXT)
        opt1_rows = [
            ('Annual commitment', '€1,266,730'),
            ('Contract term', '3 years'),
            ('TCV (new add-on)', '€3.8M'),
            ('Combined TCV to Jul \'29', '€9.65M'),
            ('ROI (base case)', '2.8x'),
            ('Contract alignment', 'Co-terms Jul \'29'),
        ]
        for i, (label, val) in enumerate(opt1_rows):
            row_y = y + Inches(0.75) + i * Inches(0.38)
            self._txt(s, label, self.ML + Inches(0.2), row_y,
                      Inches(2.5), Inches(0.2),
                      size=Pt(9), color=self.SUB_TEXT)
            val_color = self.GREEN if val in ('2.8x',) else (self.BLUE if 'Co-terms' in val else self.DARK_TEXT)
            self._txt(s, val, self.ML + half_w - Inches(2.2), row_y,
                      Inches(2), Inches(0.2),
                      size=Pt(10), bold=True, color=val_color,
                      align=PP_ALIGN.RIGHT)
            if i < len(opt1_rows) - 1:
                self._bar_rect(s, self.ML + Inches(0.2), row_y + Inches(0.28),
                               half_w - Inches(0.4), Pt(0.5), fill=self.BORDER)
        # Best for callout
        self._insight_card(s, 'BEST FOR', 'Shorter commitment, aligns with existing contract, modular pricing transparency.',
                           self.ML + Inches(0.15), y + Inches(3.1), half_w - Inches(0.3), Inches(0.4),
                           label_color=self.BLUE, bg=self.BLUE_LIGHT)

        # Option 2 card (recommended — purple border)
        opt2_x = self.ML + half_w + gap
        self._card(s, opt2_x, y, half_w, Inches(3.6),
                   border=self.PURPLE)
        # RECOMMENDED badge
        badge_w = Inches(1.6)
        badge_x = opt2_x + (half_w - badge_w) / 2
        self._bar_rect(s, badge_x, y - Inches(0.12), badge_w, Inches(0.24),
                       fill=self.PURPLE)
        self._txt(s, 'RECOMMENDED', badge_x, y - Inches(0.1),
                  badge_w, Inches(0.2),
                  size=Pt(7), color=self.WHITE, bold=True,
                  align=PP_ALIGN.CENTER)
        self._txt(s, 'OPTION 2', opt2_x + Inches(0.2), y + Inches(0.15),
                  Inches(2), Inches(0.2),
                  size=Pt(8), bold=True, color=self.PURPLE)
        self._txt(s, '5-Year Growth Bundle', opt2_x + Inches(0.2), y + Inches(0.35),
                  half_w - Inches(0.4), Inches(0.3),
                  size=Pt(16), bold=True, color=self.DARK_TEXT)
        opt2_rows = [
            ('Annual commitment', '€1,150,000'),
            ('Contract term', '5 years'),
            ('TCV (new add-on)', '€5.75M'),
            ('Combined TCV (all)', '€11.6M'),
            ('ROI (base case)', '3.1x'),
            ('Pricing model', 'All-inclusive flat'),
        ]
        for i, (label, val) in enumerate(opt2_rows):
            row_y = y + Inches(0.75) + i * Inches(0.38)
            self._txt(s, label, opt2_x + Inches(0.2), row_y,
                      Inches(2.5), Inches(0.2),
                      size=Pt(9), color=self.SUB_TEXT)
            val_color = self.GREEN if val in ('3.1x',) else (self.PURPLE if 'All-inclusive' in val else self.DARK_TEXT)
            self._txt(s, val, opt2_x + half_w - Inches(2.2), row_y,
                      Inches(2), Inches(0.2),
                      size=Pt(10), bold=True, color=val_color,
                      align=PP_ALIGN.RIGHT)
            if i < len(opt2_rows) - 1:
                self._bar_rect(s, opt2_x + Inches(0.2), row_y + Inches(0.28),
                               half_w - Inches(0.4), Pt(0.5), fill=self.BORDER)
        self._insight_card(s, 'BEST FOR', 'Budget predictability, unlimited CLO campaigns, single bundled price.',
                           opt2_x + Inches(0.15), y + Inches(3.1), half_w - Inches(0.3), Inches(0.4),
                           label_color=self.PURPLE, bg=self.PURPLE_LIGHT)
        # Summary callout
        self._txt(s, 'Incremental commitment: €1.15M (Opt 2) to €1.27M (Opt 1) — against €3.6M projected annual value.',
                  self.ML, Inches(5.5), self.CW, Inches(0.3),
                  size=Pt(9), color=self.SUB_TEXT, align=PP_ALIGN.CENTER)

        # ── 9. OPTION 1 DETAIL ────────────────────────────────
        n += 1
        s = self._slide_content('OPTION 1 — DETAIL', '3-Year Co-Termed ',
                                'Add-On.',
                                subtitle_text='Aligns with your existing contract end date (July 2029). No new long-term commitment.',
                                slide_number=n)
        rows = [
            ['Module', 'List Price', 'Discount', 'Annual Fee'],
            ['Managed Hosting Enterprise 2 (180 RPS)', '€601,750', '10%', '€541,575'],
            ['Digital Assist Premium (50 users)', '€350,140', '40%', '€210,084'],
            ['CLO — Base Platform', '€381,000', '30%', '€266,700'],
            ['CLO — User Fee (500K × €0.70)', '€354,816', '30%', '€248,371'],
            ['TOTAL NEW ANNUAL COMMITMENT', '', '', '€1,266,730'],
        ]
        self._add_table(s, rows, col_widths=[4.5, 2.5, 1.5, 2.5],
                        left=self.ML, top=Inches(1.7))
        # Stats below table
        gap3 = Inches(0.2)
        sw3 = (self.CW - 2 * gap3) / 3
        for i, (val, lbl, vc, bg) in enumerate([
            ('€3.8M', '3YR TCV', self.GREEN, self.GREEN_LIGHT),
            ('Aug \'26 — Jul \'29', 'TERM', self.DARK_TEXT, self.BLUE_LIGHT),
            ('2.8x', 'ROI (BASE CASE)', self.GREEN, self.GREEN_LIGHT),
        ]):
            self._stat_box(s, val, lbl,
                           self.ML + i * (sw3 + gap3), Inches(4.3), sw3, Inches(0.55),
                           val_color=vc, bg=bg)
        self._insight_card(s, 'CO-TERMS WITH YOUR EXISTING CONTRACT',
                           'Both contracts end July 2029. At renewal, everything consolidates into a single agreement.',
                           self.ML, Inches(5.1), self.CW, Inches(0.45),
                           label_color=self.BLUE, bg=self.BLUE_LIGHT)

        # ── 10. OPTION 2 DETAIL ───────────────────────────────
        n += 1
        s = self._slide_content('OPTION 2 — DETAIL', '5-Year Growth ',
                                'Bundle.',
                                subtitle_text='Single all-inclusive annual fee. Unlimited CLO campaigns. Maximum budget predictability.',
                                slide_number=n)
        rows2 = [
            ['Component', 'Coverage', 'Annual Fee'],
            ['Managed Hosting Enterprise 2', '180 RPS, fully managed', 'Included'],
            ['Digital Assist Premium', '50 seats, AI-assisted', 'Included'],
            ['Customer Lifecycle Orchestrator', 'Full platform + unlimited campaigns', 'Included'],
            ['TOTAL ALL-INCLUSIVE ANNUAL FEE', '', '€1,150,000'],
        ]
        self._add_table(s, rows2, col_widths=[4.5, 4.0, 2.5],
                        left=self.ML, top=Inches(1.7))
        for i, (val, lbl, vc, bg) in enumerate([
            ('€5.75M', '5YR TCV', self.GREEN, self.GREEN_LIGHT),
            ('€11.6M', 'COMBINED TCV', self.PURPLE, self.PURPLE_LIGHT),
            ('3.1x', 'ROI (BASE CASE)', self.GREEN, self.GREEN_LIGHT),
        ]):
            self._stat_box(s, val, lbl,
                           self.ML + i * (sw3 + gap3), Inches(3.8), sw3, Inches(0.55),
                           val_color=vc, bg=bg)
        self._insight_card(s, 'BUDGET PREDICTABILITY',
                           'One flat fee covers all three modules. No per-user CLO charges, no variable costs. Simplifies procurement and forecasting.',
                           self.ML, Inches(4.6), self.CW, Inches(0.45),
                           label_color=self.PURPLE, bg=self.PURPLE_LIGHT)

        # ── 11. ROADMAP ───────────────────────────────────────
        n += 1
        s = self._slide_content('IMPLEMENTATION ROADMAP', 'From signing to ',
                                'full value.',
                                subtitle_text='Phased deployment with value milestones at each stage.',
                                slide_number=n)
        phases = [
            ('Q3 2026', 'FOUNDATION', ['MH migration kickoff', 'DA Premium deployment', 'CLO integration begins'], self.BLUE),
            ('Q4 2026', 'ACTIVATE', ['MH fully live', 'DA agents onboarded', 'First CLO campaigns'], self.GREEN),
            ('H1 2027', 'SCALE', ['Product origination campaigns', 'Cross-sell optimization', 'Branch traffic reduction'], self.PURPLE),
            ('H2 2027+', 'COMPOUND', ['Full CLO maturity', 'AI-driven personalization', 'Value target: €3.6M/yr'], self.GREEN),
        ]
        card_w4 = (self.CW - 3 * Inches(0.15)) / 4
        for i, (date, title, items, color) in enumerate(phases):
            x = self.ML + i * (card_w4 + Inches(0.15))
            y = self.CT
            self._card(s, x, y, card_w4, Inches(2.2))
            self._colored_top_line(s, x, y, card_w4, color)
            self._txt(s, date, x + Inches(0.12), y + Inches(0.12),
                      card_w4 - Inches(0.24), Inches(0.15),
                      size=Pt(7), bold=True, color=self.MUTED)
            self._txt(s, title, x + Inches(0.12), y + Inches(0.3),
                      card_w4 - Inches(0.24), Inches(0.2),
                      size=Pt(10), bold=True, color=color)
            self._bullet_list(s, items,
                              x + Inches(0.12), y + Inches(0.6),
                              card_w4 - Inches(0.24), Inches(1.4),
                              size=Pt(8))

        # ── 12. NEXT STEPS ────────────────────────────────────
        n += 1
        s = self._slide_content('NEXT STEPS', 'Mutual close plan — ',
                                'path to value.',
                                slide_number=n)
        steps_data = [
            ('1', 'Commercial Alignment', 'Agree on option, confirm terms', 'March 2026', self.BLUE),
            ('2', 'Technical Scoping', 'MH migration plan, DA integration, CLO config', 'April 2026', self.PURPLE),
            ('3', 'Contract Execution', 'Sign and mobilize', 'May 2026', self.GREEN),
            ('4', 'Kickoff & Deployment', 'Phased go-live starting Q3 2026', 'June 2026', self.GREEN),
        ]
        for i, (num, title, desc, date, color) in enumerate(steps_data):
            y = self.CT + i * Inches(0.75)
            self._bar_rect(s, self.ML, y, Inches(0.35), Inches(0.35), fill=color)
            self._txt(s, num, self.ML, y + Inches(0.02), Inches(0.35), Inches(0.35),
                      size=Pt(14), bold=True, color=self.WHITE,
                      align=PP_ALIGN.CENTER)
            self._txt(s, title, self.ML + Inches(0.5), y,
                      Inches(3), Inches(0.2),
                      size=Pt(11), bold=True, color=self.DARK_TEXT)
            self._txt(s, desc, self.ML + Inches(0.5), y + Inches(0.2),
                      Inches(6), Inches(0.2),
                      size=Pt(9), color=self.SUB_TEXT)
            self._txt(s, date, self.ML + Inches(9), y + Inches(0.05),
                      Inches(3), Inches(0.2),
                      size=Pt(9), bold=True, color=color,
                      align=PP_ALIGN.RIGHT)

        # ── 13. APPENDIX: VALUE LEVERS ────────────────────────
        n += 1
        s = self._slide_content('APPENDIX — VALUE METHODOLOGY',
                                'Five value levers, ',
                                'conservatively estimated.',
                                subtitle_text='Each lever uses CIH-specific data and Moroccan retail banking benchmarks.',
                                slide_number=n)
        levers = [
            ('CLO — PRODUCT ORIGINATION', '€500K', '500K wallet users × 5% conversion × €200 avg product revenue', 'Benchmark: 5% conservative vs 8-12% industry', self.GREEN),
            ('CLO — CROSS-SELL UPLIFT', '€600K', '1.5% products-per-customer uplift × 2M active × €20/product', 'Benchmark: 1.5% vs 3-5% mature CLO', self.BLUE),
            ('DA — REVENUE GENERATION', '€300K', '50 agents × 20% more selling time × €30K revenue/agent/yr', 'DA frees 20% agent time → revenue activities', self.PURPLE),
            ('BRANCH TRAFFIC REDUCTION', '€1.88M', '25% digital shift × €2.50/txn × 3M branch transactions/yr', 'Benchmark: €2.50 MENA branch txn cost', self.AMBER),
            ('MH — OPS SAVINGS', '€300K', '3-4 FTEs redeployed × €75-100K fully loaded cost/FTE', 'Morocco infra FTE cost benchmarks', self.CYAN),
        ]
        for i, (title, value, calc, bench, color) in enumerate(levers):
            col = i % 3
            row = i // 3
            x = self.ML + col * (card_w + gap)
            y = Inches(1.8) + row * Inches(1.5)
            self._card(s, x, y, card_w, Inches(1.3))
            self._colored_top_line(s, x, y, card_w, color)
            self._txt(s, title, x + Inches(0.12), y + Inches(0.1),
                      card_w - Inches(0.24), Inches(0.15),
                      size=Pt(7), bold=True, color=color)
            self._txt(s, value, x + Inches(0.12), y + Inches(0.3),
                      card_w - Inches(0.24), Inches(0.3),
                      size=Pt(22), bold=True, color=color)
            self._txt(s, calc, x + Inches(0.12), y + Inches(0.65),
                      card_w - Inches(0.24), Inches(0.3),
                      size=Pt(7), color=self.SUB_TEXT)
            self._txt(s, bench, x + Inches(0.12), y + Inches(0.95),
                      card_w - Inches(0.24), Inches(0.25),
                      size=Pt(6.5), color=self.MUTED)
        # Total card in position 6 (row 1, col 2)
        x = self.ML + 2 * (card_w + gap)
        y = Inches(1.8) + 1 * Inches(1.5)
        self._card(s, x, y, card_w, Inches(1.3), fill=self.GREEN_LIGHT)
        self._txt(s, 'TOTAL ANNUAL VALUE', x + Inches(0.12), y + Inches(0.2),
                  card_w - Inches(0.24), Inches(0.15),
                  size=Pt(7), bold=True, color=self.GREEN,
                  align=PP_ALIGN.CENTER)
        self._txt(s, '€3.58M', x + Inches(0.12), y + Inches(0.45),
                  card_w - Inches(0.24), Inches(0.4),
                  size=Pt(28), bold=True, color=self.GREEN,
                  align=PP_ALIGN.CENTER)
        self._txt(s, 'Conservative estimate across all 5 levers',
                  x + Inches(0.12), y + Inches(0.9),
                  card_w - Inches(0.24), Inches(0.2),
                  size=Pt(7), color=self.SUB_TEXT, align=PP_ALIGN.CENTER)

        # ── 14. APPENDIX: ROI SENSITIVITY ─────────────────────
        n += 1
        s = self._slide_content('APPENDIX — ROI & SENSITIVITY',
                                'At 50% realization, the investment delivers ',
                                'strong returns.',
                                subtitle_text='Three scenarios based on Option 2 investment of €1.15M/yr.',
                                slide_number=n)
        scenarios = [
            ('CONSERVATIVE (25%)', '€895K', '0.8x', 'Below breakeven', self.AMBER, self.AMBER_LIGHT),
            ('BASE CASE (50%)', '€1.79M', '1.6x', 'Solid return', self.BLUE, self.BLUE_LIGHT),
            ('FULL POTENTIAL (100%)', '€3.58M', '3.1x', 'Full delivery', self.GREEN, self.GREEN_LIGHT),
        ]
        for i, (label, value, roi, desc, color, bg) in enumerate(scenarios):
            x = self.ML + i * (card_w + gap)
            y = self.CT
            self._card(s, x, y, card_w, Inches(1.5), fill=bg)
            self._colored_top_line(s, x, y, card_w, color)
            self._txt(s, label, x + Inches(0.15), y + Inches(0.12),
                      card_w - Inches(0.3), Inches(0.15),
                      size=Pt(7), bold=True, color=color)
            self._txt(s, value, x + Inches(0.15), y + Inches(0.35),
                      card_w - Inches(0.3), Inches(0.3),
                      size=Pt(24), bold=True, color=color,
                      align=PP_ALIGN.CENTER)
            self._txt(s, 'Annual value realized', x + Inches(0.15), y + Inches(0.7),
                      card_w - Inches(0.3), Inches(0.15),
                      size=Pt(8), color=self.SUB_TEXT, align=PP_ALIGN.CENTER)
            self._txt(s, roi, x + Inches(0.15), y + Inches(0.95),
                      card_w - Inches(0.3), Inches(0.25),
                      size=Pt(16), bold=True, color=color,
                      align=PP_ALIGN.CENTER)
            self._txt(s, f'ROI — {desc.lower()}', x + Inches(0.15), y + Inches(1.2),
                      card_w - Inches(0.3), Inches(0.15),
                      size=Pt(7), color=self.SUB_TEXT, align=PP_ALIGN.CENTER)
        # Key assumptions
        assumptions = [
            ['Assumption', 'Value', 'Source'],
            ['Avg product revenue', '€200', 'Moroccan retail banking (blended)'],
            ['Wallet conversion rate', '5%', 'Conservative vs 8-12% (Forrester 2024)'],
            ['Branch transaction cost', '€2.50', 'MENA average (McKinsey)'],
            ['Cross-sell uplift', '1.5%', 'Half of 3-5% mature benchmark'],
            ['Revenue per agent', '€30K', 'Moroccan market rates'],
            ['Infra FTE cost', '€75-100K', 'Fully loaded, Morocco'],
        ]
        self._add_table(s, assumptions, col_widths=[3.0, 1.5, 6.5],
                        left=self.ML, top=Inches(3.5))

        # ── 15. APPENDIX: VALUE TIMELINE ──────────────────────
        n += 1
        s = self._slide_content('APPENDIX — VALUE REALIZATION TIMELINE',
                                'When each lever ',
                                'kicks in.',
                                subtitle_text='Value builds progressively as each module goes live and campaigns mature.',
                                slide_number=n)
        timeline_rows = [
            ['Value Lever', 'H2 2026', '2027', '2028', '2029-30', 'Full Potential'],
            ['Product Origination (CLO)', '—', '€250K', '€500K', '€500K', '€500K'],
            ['Cross-Sell Uplift (CLO)', '—', '€200K', '€450K', '€600K', '€600K'],
            ['DA Revenue Generation', '€75K', '€225K', '€300K', '€300K', '€300K'],
            ['Branch Traffic Reduction', '€188K', '€940K', '€1.50M', '€1.88M', '€1.88M'],
            ['MH Ops Savings', '€150K', '€300K', '€300K', '€300K', '€300K'],
            ['TOTAL ANNUAL VALUE', '€413K', '€1.92M', '€3.05M', '€3.58M', '€3.58M'],
        ]
        self._add_table(s, timeline_rows,
                        col_widths=[3.5, 1.7, 1.7, 1.7, 1.7, 1.7],
                        left=self.ML, top=Inches(1.7))
        # Cumulative stat
        self._insight_card(s, 'CUMULATIVE 5-YEAR VALUE',
                           '€12.5M+ value created  |  Investment (Option 2, 5yr): €5.2M  |  Net value: €7.4M+',
                           self.ML, Inches(4.8), self.CW, Inches(0.45),
                           label_color=self.GREEN, bg=self.GREEN_LIGHT)
        self._txt(s, 'Phasing: MH and DA from go-live (Jul 2026). CLO campaigns from 2027. Full potential by 2028-29.',
                  self.ML, Inches(5.4), self.CW, Inches(0.3),
                  size=Pt(8), color=self.MUTED)

        # ── 16. APPENDIX: VALUE VS INVESTMENT ─────────────────
        n += 1
        s = self._slide_content('APPENDIX — VALUE VS. INVESTMENT',
                                'Your investment pays back in ',
                                '12 months.',
                                subtitle_text='Year-over-year value realization vs. Option 2 investment (€1.15M/yr). Value compounds while cost stays flat.',
                                slide_number=n)
        vi_rows = [
            ['', 'H2 2026', '2027', '2028', '2029', '2030', 'Total'],
            ['Value Realized', '€413K', '€1.92M', '€3.05M', '€3.58M', '€3.58M', '€12.5M'],
            ['Investment', '€575K', '€1.15M', '€1.15M', '€1.15M', '€1.15M', '€5.2M'],
            ['Annual Net Value', '-€162K', '+€770K', '+€1.90M', '+€2.43M', '+€2.43M', '+€7.4M'],
            ['Cumulative Net', '-€162K', '+€608K', '+€2.51M', '+€4.93M', '+€7.36M', '€7.4M+'],
        ]
        self._add_table(s, vi_rows,
                        col_widths=[2.5, 1.6, 1.6, 1.6, 1.6, 1.6, 1.5],
                        left=self.ML, top=Inches(1.7))
        # Stats
        for i, (val, lbl, vc, bg) in enumerate([
            ('Month 12', 'BREAKEVEN', self.GREEN, self.AMBER_LIGHT),
            ('€7.4M+', '5-YEAR NET VALUE', self.GREEN, self.GREEN_LIGHT),
            ('2.4x', 'VALUE MULTIPLE', self.BLUE, self.BLUE_LIGHT),
        ]):
            self._stat_box(s, val, lbl,
                           self.ML + i * (sw3 + gap3), Inches(4.3), sw3, Inches(0.6),
                           val_color=vc, bg=bg)
        self._txt(s, 'Based on Option 2 (recommended). €1.15M/yr flat × 5 years. Every €1 invested returns €2.40 in business value.',
                  self.ML, Inches(5.2), self.CW, Inches(0.3),
                  size=Pt(8), color=self.SUB_TEXT, align=PP_ALIGN.CENTER)

        # ── SAVE ──────────────────────────────────────────────
        self.save(output_path)


if __name__ == '__main__':
    deck = CIHCommercialPptx()
    deck.generate('/Users/shyam/cortex/Engagement/CIH Bank/Output/CIH_Commercial_Proposal.pptx')

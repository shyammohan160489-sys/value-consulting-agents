#!/usr/bin/env python3
"""exhibit_pptx — the Backbase exhibit-style PPTX engine.

Extracted VERBATIM from the validated production builders:
  - Engagement/SNB Capital/Output/build_snbc_vc_pptx.py   (21 Jul 2026, chrome v3 FINAL)
  - Engagement/BACB/Output/build_scripts/bacb_close_exhibit_pptx.py (16 Jul 2026)

v4.0 (18 Sep 2026, the Claude Design look — mining round 6, additive):
  - ExhibitDeck(look='v4') switches the deck to the look measured from the Nedbank
    ENBI Voice VC report (Claude Design export): v4 palette (navy 091C35, blue
    3366FF, tints E5EBFF / F3F6F9, mid 7D9DFF), three-rule frame without the right
    rail, 9pt navy kicker, 28pt regular title, 9pt grey page number, client logo
    top right (ExhibitDeck(client_logo=...) or d.set_client_logo()).
  - New helpers: card / card_row / lane_grid / weight_legend (the fill-weight ramp),
    stat_block / stat_grid, hero_number, mini_stat, stat_column, panel,
    statement_line, cover_page, divider_band, vision_band, film_frame,
    numbered_rows, from_to_columns, pillar_row, share_bar, step_flow,
    compare_rows, stacked_hbars, wave_track, option_card, numbered_card,
    timeline_lanes, who_signs. Every existing signature is unchanged; the default
    look stays v3, so decks built before this date render exactly as before.
    Spec: references/visual-grammar-v4.md. Log: knowledge/design-system/
    claude-design-exhibit-kit/EXHIBIT_MINING_ROUND6_CLAUDE_DESIGN.md.

v3.4 (7 Sep 2026, the evidence layer — BCG-archive mining, round 4):
  - ADDITIVE ONLY, grammar mined from Shyam's 1,622-slide BCG archive (layout
    grammar only, re-expressed in exhibit tokens; no BCG content or palette):
    harvey balls + evaluation matrix, logo chips/walls (clean-text fallback),
    dossier fact rail, dashed leader notes, uniform tile grids, agenda tracker
    rail, ring stats, RAG coverage matrix, honesty tag chips. Serial-template
    law: N comparable things = ONE template slide repeated N times.
    Specs: knowledge/design-system/claude-design-exhibit-kit/
    EXHIBIT_MINING_ROUND4_BCG.md (catalog T30-T39).

v3.3 (4 Sep 2026, the comparison layer — feeding-list items 3-6 executed):
  - ADDITIVE ONLY, sources: MGI/BCG exhibit grammar via the round-2 mid-year mining
    (waterfall, paired From-To bars), IBCS attainment discipline (bullet_bars with
    plan ticks), JPM investor-day grammar (the KPI walk + growth_arrow), and PPTX
    parity for the HTML engine's layouts (segbar = bar-segmented, quadrant,
    milestone_strip). Title law CONFIRMED by Shyam 2026-09-04: one line, always.

v3.2 (4 Sep 2026, the data-exhibit layer — TD 1Mn-calls mining, round 3):
  - ADDITIVE ONLY: chart primitives so magnitude/trend/share messages render as
    drawn charts instead of boxes — bars, hbars, line_panel, sparkline, dot_grid,
    hero_stat, implication_card, so_what_rail, pulse_panel, panel_grid, lane_row,
    stage_column, frame_band, ramp. Zero native chart parts: everything is flat
    shapes + freeform polylines, Google Slides-safe like the rest of the engine.
  - Nothing above this layer changed: chrome, palette, laws, existing primitives
    are byte-identical to v3.1. Specs: knowledge/design-system/
    claude-design-exhibit-kit/EXHIBIT_MINING_ROUND3_TD.md.

v3.1 (28 Jul 2026, ratified by Shyam as the DEFAULT for all PPTX decks):
  - right hairline rail standard (mirrors the left rail at x=12.760) — per the SNB 22 Jul deck
  - title default 25pt, ONE line, <=63 chars (28.5 only for short punch titles)
  - chip() primitive added (swim-lane cells, channel tags, coral STEER prompts)
  - page numbers are LIVE fields (a:fld type="slidenum") — auto-renumber on insert/
    reorder in PowerPoint & Google Slides; mechanism from the Product Factory deck
    (Mayur PDP session), styling unchanged (12.75pt bold black on the divider)
  Reference builds: build_snbc_vc_pptx.py + build_snbc_journey_maps_pptx.py (SNB Capital).

Every geometry number, color, and XML fix in here was verified against decks that
survived a Google Slides round-trip and were presented to clients. DO NOT retune
values here per deck — the whole point of this module is that the style never moves.

Usage (per-deck build script):

    from exhibit_pptx import ExhibitDeck, NAVY, BLUE, TINT, ...

    d = ExhibitDeck()                      # 13.333 x 7.5 in, blank layouts
    s = d.slide()
    d.chrome(s, "Kicker · section", "Action title as a full sentence")
    ... compose the exhibit with d.rect / d.txt / d.oval / d.hline ...
    d.takeaway_band(s, "Bold lead: ", "one-line remainder.")
    d.footnote(s, "Source: ...")
    d.notes(s, "Speaker notes incl. DEFENSE lines.")
    d.save("out.pptx")                     # runs the mandatory flat/strip pass
"""
import os
import copy

from pptx import Presentation
from pptx.util import Inches as I, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.oxml.ns import qn

# ---------------------------------------------------------------- palette (LOCKED)
NAVY  = RGBColor(0x07, 0x12, 0x24)   # ink + dark surfaces
BLUE  = RGBColor(0x40, 0x66, 0xF5)   # primary accent (kicker, lead bars, glyph)
BLUE2 = RGBColor(0x1F, 0x37, 0x99)   # deep secondary
BLUE3 = RGBColor(0x5F, 0x7D, 0xF7)   # mid secondary
BLUE4 = RGBColor(0xB5, 0xC1, 0xF1)   # light secondary
TINT  = RGBColor(0xE6, 0xEB, 0xFE)   # blue tint fill
TINT2 = RGBColor(0xF5, 0xF6, 0xFA)   # neutral tint fill
CYAN  = RGBColor(0x93, 0xFB, 0xFE)   # highlight on dark only — never a gradient step
CORAL = RGBColor(0xEC, 0x5E, 0x48)   # gates, risks, placeholders, ILLUSTRATIVE only
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
MUT   = RGBColor(0x6A, 0x71, 0x7C)   # muted body
GRAY55= RGBColor(0x77, 0x7D, 0x87)   # micro-labels ("PROVEN HERE")
FN    = RGBColor(0x8F, 0x94, 0x9C)   # footnotes
HAIR  = RGBColor(0xD2, 0xD4, 0xD8)   # hairlines
HAIR_ROW = RGBColor(0xE6, 0xE7, 0xE9)  # table row rules
DASHC = RGBColor(0xA8, 0xAC, 0xB2)   # dashed "yours/not built" outlines
DIVGR = RGBColor(0x9A, 0x9E, 0xA6)   # footer page-number divider
# dark-slide companions
HAIR_D = RGBColor(0x3E, 0x46, 0x54)
SUB_D  = RGBColor(0xC1, 0xC4, 0xC8)
# v4 tokens (18 Sep 2026); under the v3 palette they map to existing v3 tokens
GREY       = BLUE4    # "today, as is" bars and done nodes (v4: C9D1DC)
CARD_LINE  = HAIR     # faint card border, vertical separators (v4: D6DBE6)
LINE_SOFT  = HAIR_ROW # question and option card border (v4: E3E8EF)
COVER_LINE = HAIR_D   # cover frame lines (v4: 6B7786)

# ---------------------------------------------------------------- palettes (v3 locked, v4 measured)
# v3 = the locked exhibit palette above. v4 = the Claude Design look measured from the Nedbank
# ENBI Voice VC report (references/visual-grammar-v4.md §3). set_palette() rebinds the module
# tokens AND the colour defaults of every ExhibitDeck method, so helpers written against the
# tokens draw in the active palette. ExhibitDeck(look='v4') calls it for you.
_PALETTE_KEYS = ["NAVY", "BLUE", "BLUE2", "BLUE3", "BLUE4", "TINT", "TINT2", "CYAN", "CORAL",
                 "MUT", "GRAY55", "FN", "HAIR", "HAIR_ROW", "DASHC", "DIVGR", "HAIR_D", "SUB_D",
                 "GREY", "CARD_LINE", "LINE_SOFT", "COVER_LINE"]
PALETTES = {
    'v3': {k: globals()[k] for k in _PALETTE_KEYS},
    'v4': {
        "NAVY": RGBColor(0x09, 0x1C, 0x35), "BLUE": RGBColor(0x33, 0x66, 0xFF),
        "BLUE2": RGBColor(0x33, 0x66, 0xFF), "BLUE3": RGBColor(0x7D, 0x9D, 0xFF),
        "BLUE4": RGBColor(0xC4, 0xD2, 0xFF), "TINT": RGBColor(0xE5, 0xEB, 0xFF),
        "TINT2": RGBColor(0xF3, 0xF6, 0xF9), "CYAN": RGBColor(0x69, 0xFE, 0xFF),
        "CORAL": RGBColor(0xFF, 0x50, 0x3C), "MUT": RGBColor(0x55, 0x64, 0x7E),
        "GRAY55": RGBColor(0x6E, 0x7B, 0x91), "FN": RGBColor(0x6E, 0x7B, 0x91),
        "HAIR": RGBColor(0xD2, 0xD4, 0xD8), "HAIR_ROW": RGBColor(0xE4, 0xE8, 0xF0),
        "DASHC": RGBColor(0x9A, 0xA6, 0xB8), "DIVGR": RGBColor(0x9A, 0x9E, 0xA6),
        "HAIR_D": RGBColor(0x2E, 0x4A, 0x7A), "SUB_D": RGBColor(0xDD, 0xE5, 0xFF),
        "GREY": RGBColor(0xC9, 0xD1, 0xDC), "CARD_LINE": RGBColor(0xD6, 0xDB, 0xE6),
        "LINE_SOFT": RGBColor(0xE3, 0xE8, 0xEF), "COVER_LINE": RGBColor(0x6B, 0x77, 0x86),
    },
}
ACTIVE_PALETTE = 'v3'


def set_palette(name):
    """Switch the module palette ('v3' | 'v4'). Rebinds the tokens and remaps the colour
    defaults of every ExhibitDeck method from the previous palette to the new one. Call it once,
    before binding token names in a build script (or build with ExhibitDeck(look='v4') and read
    colours from d.pal). Returns the active palette name."""
    global ACTIVE_PALETTE
    if name not in PALETTES:
        raise ValueError("unknown palette %r (use %s)" % (name, ", ".join(PALETTES)))
    if name == ACTIVE_PALETTE:
        return name
    old, new = PALETTES[ACTIVE_PALETTE], PALETTES[name]
    mapping = {}
    for k in _PALETTE_KEYS:
        mapping.setdefault(old[k], new[k])
    g = globals()
    for k in _PALETTE_KEYS:
        g[k] = new[k]
    import types
    for fn in list(vars(ExhibitDeck).values()):
        f = fn if isinstance(fn, types.FunctionType) else getattr(fn, '__func__', None)
        if f is not None and f.__defaults__:
            f.__defaults__ = tuple(mapping.get(dv, dv) if isinstance(dv, RGBColor) else dv
                                   for dv in f.__defaults__)
    ACTIVE_PALETTE = name
    return name


def palette_namespace():
    """The active tokens as attributes (d.pal.NAVY, d.pal.BLUE, ...)."""
    import types
    return types.SimpleNamespace(**{k: globals()[k] for k in _PALETTE_KEYS}, WHITE=WHITE)

FONT = "Libre Franklin"
W, H = 13.333, 7.5

_ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
LOGO_BLACK = os.path.abspath(os.path.join(_ASSETS, "backbase_logo_black.png"))
LOGO_WHITE = os.path.abspath(os.path.join(_ASSETS, "backbase_wordmark_white.png"))


class ExhibitDeck:
    """One deck, exhibit chrome baked in. All coordinates in inches on 13.333x7.5."""

    def __init__(self, logo=LOGO_BLACK, look='v3', palette=None, client_logo=None,
                 client_logo_box=(12.6, -0.08, 0.6, 0.69), frame=True):
        """look='v3' (default, the locked 28 Jul 2026 chrome) or 'v4' (the Claude Design look,
        18 Sep 2026: v4 palette, three-rule frame, 9pt navy kicker, 28pt regular title, grey
        page number, client logo top right). palette forces 'v3' or 'v4' regardless of look
        (the default v3 deck leaves the module tokens untouched, so scripts that patch them by
        hand keep working). client_logo: path to the client's PNG, placed by chrome() on every
        slide; client_logo_box = (x, y, w, h). frame=False drops the rules and the corner mark."""
        if look not in ('v3', 'v4'):
            raise ValueError("look must be 'v3' or 'v4'")
        self.look = look
        if palette or look == 'v4':
            set_palette(palette or 'v4')
        self.pal = palette_namespace()
        self.client_logo = client_logo
        self.client_logo_box = tuple(client_logo_box)
        self.frame = frame
        self.prs = Presentation()
        self.prs.slide_width = I(W)
        self.prs.slide_height = I(H)
        self._blank = self.prs.slide_layouts[6]
        self.logo = logo
        self.page = 0

    # ------------------------------------------------------------ slide factory
    def slide(self, dark=False):
        self.page += 1
        s = self.prs.slides.add_slide(self._blank)
        for ph in list(s.placeholders):
            ph._element.getparent().remove(ph._element)
        if dark:
            self.dark_bg(s)
        return s

    # ------------------------------------------------------------ primitives
    @staticmethod
    def flat(shp):
        """Explicit empty a:effectLst — LibreOffice/Google re-add theme shadows otherwise."""
        spPr = shp._element.spPr
        for el in spPr.findall(qn('a:effectLst')):
            spPr.remove(el)
        spPr.append(spPr.makeelement(qn('a:effectLst'), {}))

    def hline(self, s, x1, y1, x2, y2, color=HAIR, wpt=0.75):
        ln = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, I(x1), I(y1), I(x2), I(y2))
        ln.line.color.rgb = color
        ln.line.width = Pt(wpt)
        ln.shadow.inherit = False
        spPr = ln._element.spPr
        spPr.append(spPr.makeelement(qn('a:effectLst'), {}))
        # strip the theme style reference (its effectRef re-adds a shadow in some renderers)
        el = ln._element
        for st in el.findall(qn('p:style')):
            el.remove(st)
        return ln

    def dashed_conn(self, s, x1, y1, x2, y2, color=BLUE, wpt=1.6, dash='dash'):
        conn = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, I(x1), I(y1), I(x2), I(y2))
        conn.line.color.rgb = color
        conn.line.width = Pt(wpt)
        conn.shadow.inherit = False
        lnel = conn.line._get_or_add_ln()
        lnel.append(lnel.makeelement(qn('a:prstDash'), {'val': dash}))
        el = conn._element
        for st in el.findall(qn('p:style')):
            el.remove(st)
        return conn

    def step_glyph(self, s, x, y, w, h, fill):
        """The authentic Backbase step glyph (custGeom from the June master deck):
        a square with its top-left quadrant removed. Path units 9168 x 9096.
        NOT a plain square, NOT two stacked rects."""
        sx = w * 914400 / 9168.0
        sy = h * 914400 / 9096.0
        fb = s.shapes.build_freeform(19, 4762, scale=(sx, sy))
        fb.add_line_segments([(4567, 4762), (4566, 0), (9168, 0), (9168, 9096), (0, 9096)], close=True)
        shp = fb.convert_to_shape(I(x), I(y))
        shp.fill.solid()
        shp.fill.fore_color.rgb = fill
        shp.line.fill.background()
        shp.shadow.inherit = False
        self.flat(shp)
        return shp

    def rect(self, s, x, y, w, h, fill=None, line=None, line_w=0.75, round_=False, dash=None):
        shp = s.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE if round_ else MSO_SHAPE.RECTANGLE,
            I(x), I(y), I(w), I(h))
        if round_:
            try:
                shp.adjustments[0] = 0.08
            except Exception:
                pass
        if fill is None:
            shp.fill.background()
        else:
            shp.fill.solid()
            shp.fill.fore_color.rgb = fill
        if line is None:
            shp.line.fill.background()
        else:
            shp.line.color.rgb = line
            shp.line.width = Pt(line_w)
            if dash:
                ln = shp.line._get_or_add_ln()
                d = ln.makeelement(qn('a:prstDash'), {'val': dash})
                ln.append(d)
        shp.shadow.inherit = False
        self.flat(shp)
        return shp

    def diamond(self, s, x, y, w, h, fill=None, line=None, line_w=1.0):
        """Gate marker for wave timelines / milestone strips (T04, T08).
        Blue = platform release, coral = a decision the client owns."""
        shp = s.shapes.add_shape(MSO_SHAPE.DIAMOND, I(x), I(y), I(w), I(h))
        if fill is None:
            shp.fill.background()
        else:
            shp.fill.solid()
            shp.fill.fore_color.rgb = fill
        if line is None:
            shp.line.fill.background()
        else:
            shp.line.color.rgb = line
            shp.line.width = Pt(line_w)
        shp.shadow.inherit = False
        self.flat(shp)
        return shp

    def oval(self, s, x, y, w, h, fill, label=None, tc=WHITE, fs=11, bold=True):
        ov = s.shapes.add_shape(MSO_SHAPE.OVAL, I(x), I(y), I(w), I(h))
        ov.shadow.inherit = False
        ov.line.fill.background()
        ov.fill.solid()
        ov.fill.fore_color.rgb = fill
        self.flat(ov)
        if label is not None:
            tf = ov.text_frame
            tf.word_wrap = True
            tf.margin_left = 0
            tf.margin_right = 0
            p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER
            r = p.add_run()
            r.text = label
            f = r.font
            f.name = FONT
            f.size = Pt(fs)
            f.bold = bold
            f.color.rgb = tc
        return ov

    def txt(self, s, x, y, w, h, runs, size=14, color=NAVY, bold=False,
            align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, sp_after=2, line_sp=1.0,
            wrap=True, track=None):
        """runs: plain string, OR list of paragraphs, each a list of (text, size, color, bold)."""
        tb = s.shapes.add_textbox(I(x), I(y), I(w), I(h))
        tf = tb.text_frame
        tf.word_wrap = wrap
        tf.vertical_anchor = anchor
        tf.margin_left = 0
        tf.margin_right = 0
        tf.margin_top = 0
        tf.margin_bottom = 0
        if isinstance(runs, str):
            runs = [[(runs, size, color, bold)]]
        first = True
        for para in runs:
            p = tf.paragraphs[0] if first else tf.add_paragraph()
            first = False
            p.alignment = align
            p.space_after = Pt(sp_after)
            p.line_spacing = line_sp
            for (t, sz, c, b) in para:
                r = p.add_run()
                r.text = t
                f = r.font
                f.name = FONT
                f.size = Pt(sz)
                f.color.rgb = c
                f.bold = b
                if track is not None:
                    r._r.get_or_add_rPr().set('spc', str(track))
        return tb

    def page_field(self, s, page, x=12.872, y=7.118, w=0.42, h=0.249, size=12.75, color=None,
                   bold=True):
        """LIVE slide-number field (<a:fld type="slidenum">): auto-renumbers when
        slides are added, removed or reordered in PowerPoint/Google Slides — no more
        hardcoded-number renumbering passes. Mechanism ported from the Product
        Factory deck (Mayur PDP session, 28 Jul 2026); styled to the exhibit footer
        spec. The literal text is the build-time fallback for renderers that don't
        evaluate fields."""
        tb = s.shapes.add_textbox(I(x), I(y), I(w), I(h))
        tf = tb.text_frame
        tf.word_wrap = False
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf.margin_left = 0
        tf.margin_right = 0
        tf.margin_top = 0
        tf.margin_bottom = 0
        p = tf.paragraphs[0]._p
        fld = p.makeelement(qn('a:fld'), {
            'id': '{B7A1C0DE-2026-4728-8000-%012X}' % int(page), 'type': 'slidenum'})
        rPr = p.makeelement(qn('a:rPr'), {'lang': 'en-US', 'sz': str(int(round(size * 100))),
                                          'b': '1' if bold else '0', 'dirty': '0'})
        fill = p.makeelement(qn('a:solidFill'), {})
        clr = p.makeelement(qn('a:srgbClr'), {'val': ('000000' if color is None else str(color))})
        fill.append(clr)
        rPr.append(fill)
        rPr.append(p.makeelement(qn('a:latin'), {'typeface': FONT}))
        t = p.makeelement(qn('a:t'), {})
        t.text = str(int(page))
        fld.append(rPr)
        fld.append(t)
        p.append(fld)
        return tb

    # ------------------------------------------------------------ chrome (v3.1)
    def chrome(self, s, kicker, title, page=None, title_size=None, marker=None, right_rail=None,
               look=None, frame=None, client_logo=None, client_logo_box=None):
        """Standard white-slide chrome. page defaults to the running counter.
        Title law (v3.1): ONE line, <=63 chars at 25pt; 28.5 only for short punch
        titles (<=48 chars). Never let a title wrap.
        marker: optional (labels, active) tuple for a top-right session strip,
        e.g. (["OPEN","DEMO","CLOSE"], "OPEN"). Off by default.
        v4 (18 Sep 2026): look defaults to the deck's look. look='v4' draws the measured
        Claude Design chrome (three rules, no right rail, 9pt navy kicker, 28pt regular
        title without a period, 9pt grey page number, client logo top right). frame=False
        drops the rules and the corner mark. client_logo / client_logo_box override the
        deck-level logo for this slide. Under look='v3' every default is as before."""
        page = self.page if page is None else page
        look = look or getattr(self, 'look', 'v3')
        frame = getattr(self, 'frame', True) if frame is None else frame
        if look == 'v4':
            return self._chrome_v4(s, kicker, title, page, title_size, frame, client_logo,
                                   client_logo_box)
        title_size = 25 if title_size is None else title_size
        right_rail = True if right_rail is None else right_rail
        if frame:
            # full-bleed hairlines (#D2D4D8, 0.75pt); right rail standard since v3.1
            self.hline(s, 0, 0.573, W, 0.573)
            self.hline(s, 0.573, 0, 0.573, 7.042)
            if right_rail:
                self.hline(s, 12.760, 0, 12.760, 7.042)
            self.hline(s, 0, 7.042, W, 7.042)
            # authentic step glyph hugging the hairline crossing; corner ends at (0.573, 0.573)
            self.step_glyph(s, 0.406, 0.406, 0.167, 0.166, BLUE)
        if marker:
            labels, active = marker
            for i, l in enumerate(labels):
                on = (l == active)
                b = self.rect(s, 10.9 + i * 0.58, 0.20, 0.54, 0.26,
                              fill=BLUE if on else None, line=None if on else HAIR, line_w=0.75)
                tf = b.text_frame
                tf.word_wrap = False
                tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
                p = tf.paragraphs[0]
                p.alignment = PP_ALIGN.CENTER
                r = p.add_run(); r.text = l
                f = r.font; f.name = FONT; f.size = Pt(8.5); f.bold = on
                f.color.rgb = WHITE if on else MUT
        # kicker 13.5 regular blue at 0.812; title 28.5 bold navy at 1.104, trailing period
        self.txt(s, 1.0, 0.812, 10.42, 0.25, kicker.upper(), size=13.5, color=BLUE, bold=False, track="120")
        t = title if title.rstrip().endswith((".", "?", ":")) else title + "."
        self.txt(s, 1.0, 1.104, 10.94, 1.05, t, size=title_size, color=NAVY, bold=True, line_sp=1.04)
        # white footer: large black wordmark │ page number
        if self.logo and os.path.exists(self.logo):
            s.shapes.add_picture(self.logo, I(11.633), I(7.185), I(1.067), I(0.173))
        else:
            self.txt(s, 10.6, 7.16, 2.1, 0.25, "Backbase", size=13, color=RGBColor(0, 0, 0),
                     bold=True, align=PP_ALIGN.RIGHT)
        self.hline(s, 12.802, 7.118, 12.802, 7.367, color=DIVGR, wpt=0.9)
        self.page_field(s, page)
        self.client_logo_mark(s, client_logo, client_logo_box)

    def footnote(self, s, text, y=None, size=None, color=None, rule=None, line_sp=1.15):
        """Every numeric slide ends with one. v3: hairline + 9.5pt source line at y=6.50.
        v4: no hairline, 8.5pt FN text at y=6.55 (the measured footnote). Pass y, size,
        color or rule to override either look."""
        look = getattr(self, 'look', 'v3')
        if y is None:
            y = 6.50 if look == 'v3' else 6.55
        if rule is None:
            rule = (look == 'v3')
        if size is None:
            size = 9.5 if look == 'v3' else 8.5
        color = FN if color is None else color
        if rule:
            self.hline(s, 1.0, y + 0.06, 12.708, y + 0.06)
            self.txt(s, 1.0, y + 0.14, 11.708, 0.40, text, size=size, color=color, line_sp=line_sp)
        else:
            self.txt(s, 1.0, y, 11.95, 0.45, text, size=size, color=color, line_sp=line_sp)

    def notes(self, s, text):
        s.notes_slide.notes_text_frame.text = text

    def takeaway_band(self, s, lead, rest, y=5.62, x=1.0, w=11.708):
        """Navy punchline strip: bold cyan lead-in + white remainder.
        EXACTLY one sentence, fitting ONE line — cut words until it does."""
        self.rect(s, x, y, w, 0.479, fill=NAVY, round_=True)
        self.txt(s, x + 0.25, y + 0.125, w - 0.5, 0.28,
                 [[(lead, 13.5, CYAN, True), (rest, 13.5, WHITE, False)]])

    def open_badge(self, s, x, y, w, lead, rest, h=0.72):
        """Coral dashed box = still open / placeholder / illustrative-outside-in."""
        self.rect(s, x, y, w, h, line=CORAL, line_w=1.2, round_=True, dash='dash')
        self.txt(s, x + 0.25, y + 0.11, w - 0.5, h - 0.2,
                 [[(lead, 11.5, CORAL, True), (rest, 11.5, NAVY, False)]], line_sp=1.12)

    def stat_card(self, s, x, y, from_text, value, label, w=2.775, h=1.21):
        """Impact stat card (ratified 28 Jul 2026 — Shyam prefers this over the
        3-hero-tile close: 'a lot cleaner'). Tint card: muted "from →" line,
        30pt deep-blue landing value, one/two-line muted label. Standard row =
        FOUR across the content width at x=1.0, pitch 2.975 (gap 0.2)."""
        self.rect(s, x, y, w, h, fill=TINT, round_=True)
        self.txt(s, x + 0.18, y + 0.13, w - 0.36, 0.24, from_text + "  →", size=11.5, color=MUT)
        self.txt(s, x + 0.18, y + 0.40, w - 0.36, 0.48, value, size=30, color=BLUE2, bold=True)
        self.txt(s, x + 0.18, y + 0.85, w - 0.36, 0.34, label, size=10, color=MUT, line_sp=1.05)

    def proven_band(self, s, items, y=5.62, x=1.0, w=11.708, h=0.34, lead="Proven here:  "):
        """Tint credibility strip above the footnote: bold blue lead + where it
        runs live (Backbase client names allowed per anonymization rules)."""
        self.rect(s, x, y, w, h, fill=TINT2, round_=True)
        self.txt(s, x + 0.30, y + 0.055, w - 0.60, h - 0.10,
                 [[(lead, 11.5, BLUE, True), (items, 11.5, NAVY, False)]])

    def chip(self, s, x, y, w, h, text, fill=TINT2, tc=NAVY, fs=8.5, bold=False,
             line=None, dash=None, align=PP_ALIGN.LEFT):
        """Small rounded label chip (v3.1): swim-lane cells, stage headers, channel
        tags, workshop STEER prompts. Text vertically centered, 0.09in side inset.
        fill=None + line=CORAL + dash='dash' = the coral STEER/open prompt.
        Keep the chip's bottom edge >=0.06in clear of the footnote hairline."""
        self.rect(s, x, y, w, h, fill=fill, line=line, dash=dash, round_=True)
        self.txt(s, x + 0.09, y + 0.04, w - 0.18, h - 0.08, text, size=fs, color=tc,
                 bold=bold, line_sp=0.98, align=align, anchor=MSO_ANCHOR.MIDDLE)

    # ------------------------------------------------------------ data-exhibit layer (v3.2)
    # Charts are DRAWN — flat rects and freeform polylines, never native chart parts
    # (native charts break the Google Slides round-trip and the flat look). Verified
    # against the TD 1Mn-calls deck, which renders this entire vocabulary as shapes.

    @staticmethod
    def _lerp(c1, c2, t):
        """Linear blend between two RGBColors, t in [0,1]."""
        return RGBColor(int(c1[0] + (c2[0] - c1[0]) * t),
                        int(c1[1] + (c2[1] - c1[1]) * t),
                        int(c1[2] + (c2[2] - c1[2]) * t))

    def ramp(self, n, mode='time'):
        """Bar-fill intensity ramp within the locked palette.
        'time': light -> saturated left to right (BLUE4 -> BLUE) — 'the base solidifies'.
        'rank': saturated first then fading (BLUE, then BLUE3 -> BLUE4) — T02's law."""
        if n <= 1:
            return [BLUE]
        if mode == 'rank':
            rest = [self._lerp(BLUE3, BLUE4, i / max(1, n - 2)) for i in range(n - 1)]
            return [BLUE] + rest
        return [self._lerp(BLUE4, BLUE, i / (n - 1)) for i in range(n)]

    def bars(self, s, x, y, w, h, items, mode='time', hi=None,
             val_size=19, delta_size=10.5, cat_size=11.5, bar_frac=0.55):
        """Drawn column chart (P2, TD slides 5-6). items: (cat, value) or
        (cat, value, label) or (cat, value, label, delta). No y-axis, no gridlines —
        the value labels ARE the data: bold navy above each bar, muted delta under
        them, categories under a navy baseline. hi: index whose bar+label go full
        BLUE (default: last bar in 'time' mode). Returns [(center_x, bar_top_y)]
        for annotations."""
        norm = []
        for it in items:
            it = list(it) + [None] * (4 - len(it))
            cat, val, label, delta = it[:4]
            norm.append((cat, float(val), label if label is not None else str(val), delta))
        n = len(norm)
        fills = self.ramp(n, mode)
        if hi is None and mode == 'time':
            hi = n - 1
        has_delta = any(d for (_, _, _, d) in norm)
        top_zone = 0.30 + (0.24 if has_delta else 0.0)
        baseline = y + h - 0.34
        plot_h = baseline - (y + top_zone)
        vmax = max(v for (_, v, _, _) in norm) or 1.0
        pitch = w / n
        bw = pitch * bar_frac
        out = []
        for i, (cat, val, label, delta) in enumerate(norm):
            bh = plot_h * (val / vmax)
            bx = x + i * pitch + (pitch - bw) / 2.0
            bt = baseline - bh
            fill = BLUE if i == hi else fills[i]
            self.rect(s, bx, bt, bw, bh, fill=fill)
            ly = bt - top_zone
            vcol = BLUE if i == hi else NAVY
            self.txt(s, x + i * pitch, ly, pitch, 0.30, label, size=val_size,
                     color=vcol, bold=True, align=PP_ALIGN.CENTER, wrap=False)
            if delta:
                self.txt(s, x + i * pitch, ly + 0.29, pitch, 0.22, delta, size=delta_size,
                         color=MUT, align=PP_ALIGN.CENTER, wrap=False)
            self.txt(s, x + i * pitch, baseline + 0.07, pitch, 0.26, cat, size=cat_size,
                     color=NAVY, align=PP_ALIGN.CENTER, wrap=False)
            out.append((bx + bw / 2.0, bt))
        self.hline(s, x, baseline, x + w, baseline, color=NAVY, wpt=1.1)
        return out

    def hbars(self, s, x, y, w, h, items, client_idx=None, row_h=0.64, label_w=0.85):
        """T02 sorted horizontal bars, codified from the S3 idiom. items:
        (name, value, display_label). Ranked: lead bar BLUE, rest fading; the
        client's own row (client_idx) goes NAVY with a bold name — plot it from
        THEIR number. Values auto-scale to the widest bar."""
        n = len(items)
        fills = self.ramp(n, 'rank')
        vmax = max(float(v) for (_, v, _) in items) or 1.0
        yy = y
        for i, (name, val, lab) in enumerate(items):
            col = NAVY if i == client_idx else fills[i]
            self.txt(s, x, yy, w - label_w, 0.26, name, size=12, color=NAVY,
                     bold=(i == client_idx))
            self.txt(s, x + w - label_w, yy, label_w, 0.26, lab, size=12, color=NAVY,
                     bold=True, align=PP_ALIGN.RIGHT)
            self.rect(s, x, yy + 0.28, w * (float(val) / vmax), 0.22, fill=col)
            yy += row_h
        return yy

    def _polyline(self, s, pts, color, lw):
        """Open freeform polyline through absolute-inch points. Flat, no fill."""
        emu = [(int(px * 914400), int(py * 914400)) for (px, py) in pts]
        fb = s.shapes.build_freeform(emu[0][0], emu[0][1], scale=1.0)
        fb.add_line_segments(emu[1:], close=False)
        shp = fb.convert_to_shape()
        shp.fill.background()
        shp.line.color.rgb = color
        shp.line.width = Pt(lw)
        shp.shadow.inherit = False
        self.flat(shp)
        return shp

    def line_panel(self, s, x, y, w, h, series, label=None, color=BLUE3, lw=2.25,
                   ticks=None, annos=None, end_dot=False):
        """Drawn line panel (P3, TD slide 7). series: list of values, evenly spaced.
        label sits ON the panel top-left in the series color. ticks: [(idx, text)]
        under the baseline. annos: [(idx, bold_text, phrase_or_None, side)] with
        side 'up'/'down' — a dot on the point plus a bold value and optional muted
        phrase. Panels stack: two thin panels beat one dual-axis chart."""
        top = y + (0.30 if label else 0.08)
        bottom = y + h - (0.30 if ticks else 0.08)
        n = len(series)
        vmin, vmax = min(series), max(series)
        pad = (vmax - vmin) * 0.10 or (abs(vmax) * 0.10 or 1.0)
        vmin, vmax = vmin - pad, vmax + pad
        pts = []
        for i, v in enumerate(series):
            px = x + (w * i / (n - 1) if n > 1 else 0)
            py = bottom - (v - vmin) / (vmax - vmin) * (bottom - top)
            pts.append((px, py))
        if label:
            self.txt(s, x, y, w * 0.8, 0.26, label, size=11.5, color=color, bold=True)
        self.hline(s, x, bottom, x + w, bottom, color=HAIR, wpt=0.75)
        self._polyline(s, pts, color, lw)
        if end_dot:
            ex, ey = pts[-1]
            self.oval(s, ex - 0.05, ey - 0.05, 0.10, 0.10, color)
        for a in (annos or []):
            idx, btxt, phrase, side = (list(a) + ['up'])[:4]
            px, py = pts[idx]
            self.oval(s, px - 0.055, py - 0.055, 0.11, 0.11, color)
            # value and phrase stack AWAY from the dot so neither crosses the line
            if side == 'up':
                vy = py - (0.58 if phrase else 0.34)
                py_phrase = py - 0.33
            else:
                vy = py + 0.10
                py_phrase = py + 0.34
            self.txt(s, px - 1.6, vy, 3.2, 0.26, btxt, size=12.5, color=NAVY, bold=True,
                     align=PP_ALIGN.CENTER, wrap=False)
            if phrase:
                self.txt(s, px - 1.9, py_phrase, 3.8, 0.24, phrase, size=10, color=MUT,
                         align=PP_ALIGN.CENTER, wrap=False)
        for (idx, t) in (ticks or []):
            px = x + (w * idx / (n - 1) if n > 1 else 0)
            self.txt(s, px - 0.6, bottom + 0.06, 1.2, 0.24, t, size=11, color=NAVY,
                     align=PP_ALIGN.CENTER, wrap=False)
        return pts

    def sparkline(self, s, x, y, w, h, series, color=BLUE3, lw=1.4, end_dot=True):
        """Micro trend line for pulse panels (P4). No axes, optional end dot."""
        n = len(series)
        vmin, vmax = min(series), max(series)
        rng = (vmax - vmin) or 1.0
        pts = [(x + (w * i / (n - 1) if n > 1 else 0),
                y + h - (v - vmin) / rng * h) for i, v in enumerate(series)]
        self._polyline(s, pts, color, lw)
        if end_dot:
            ex, ey = pts[-1]
            self.oval(s, ex - 0.035, ey - 0.035, 0.07, 0.07, color)

    def dot_grid(self, s, x, y, cols, rows, filled, dot=0.14, gap=0.055,
                 on=BLUE, off=TINT):
        """T09 unit dot-grid, codified. One dot = one unit; `filled` dots colored
        from the BOTTOM row up, left to right (the taken-out share sits at the
        base, TD slide 3). Returns the grid's total height."""
        full, part = divmod(int(filled), cols)
        for r in range(rows):
            from_bottom = rows - 1 - r
            for c in range(cols):
                is_on = from_bottom < full or (from_bottom == full and c < part)
                self.oval(s, x + c * (dot + gap), y + r * (dot + gap), dot, dot,
                          on if is_on else off)
        return rows * (dot + gap) - gap

    def hero_stat(self, s, x, y, w, num, caption, color=BLUE, num_size=30,
                  cap_size=11, h=0.98):
        """Rail hero stat (P1): short vertical tick bar in the stat's color, a big
        light-weight number in the same color, a 1-2 line muted caption. Coral
        number + tick = the tension stat. Stack 2-3 in the so-what rail."""
        self.rect(s, x, y + 0.04, 0.045, 0.42, fill=color)
        self.txt(s, x + 0.16, y, w - 0.16, 0.46, num, size=num_size, color=color,
                 bold=False, wrap=False)
        self.txt(s, x + 0.16, y + 0.50, w - 0.16, h - 0.50, caption, size=cap_size,
                 color=MUT, line_sp=1.12)

    def implication_card(self, s, x, y, w, h, text, label="IMPLICATION", fill=NAVY):
        """The so-what card (P1): navy, cyan uppercase label, white reasoning.
        3-5 short lines. On data slides this replaces box-clutter: the chart is
        the evidence, this card is the argument."""
        self.rect(s, x, y, w, h, fill=fill, round_=True)
        self.txt(s, x + 0.20, y + 0.14, w - 0.40, 0.24, label, size=10.5, color=CYAN,
                 bold=True, track="120")
        self.txt(s, x + 0.20, y + 0.44, w - 0.40, h - 0.58, text, size=11.5,
                 color=WHITE, line_sp=1.22)

    def so_what_rail(self, s, stats, implication, x=9.98, w=2.70, y=2.0,
                     y_end=6.30, imp_label="IMPLICATION"):
        """The data slide's right rail (P1): 2-3 hero stats stacked over the
        implication card. Pairs with an exhibit drawn at x=1.0 .. 9.6. stats:
        [(num, caption, color)]. The card fills down to y_end."""
        yy = y
        for (num, cap, col) in stats:
            self.hero_stat(s, x, yy, w, num, cap, color=col)
            yy += 0.98
        self.implication_card(s, x, yy + 0.06, w, max(0.9, y_end - yy - 0.06),
                              implication, label=imp_label)

    def pulse_panel(self, s, x, y, w, h, label, series, range_text, theme=BLUE3):
        """One telemetry micro-card (P4): themed top bar (blue = day job, coral =
        friction, deep navy = growth), label, sparkline, observed range."""
        self.rect(s, x, y, w, h, fill=TINT2)
        self.rect(s, x, y, w, 0.035, fill=theme)
        self.txt(s, x + 0.12, y + 0.10, w - 0.24, 0.40, label, size=10.5, color=NAVY,
                 bold=True, line_sp=1.0)
        self.sparkline(s, x + 0.14, y + 0.52, w - 0.34, h - 0.92, series, color=theme)
        self.txt(s, x + 0.12, y + h - 0.30, w - 0.24, 0.24, range_text, size=9.5,
                 color=MUT, wrap=False)

    def panel_grid(self, s, x, y, w, cells, cols, panel_h=1.06, gap=0.12):
        """Grid of pulse panels (P4). cells: [{label, series, range, theme}].
        Returns the y just under the grid."""
        pw = (w - gap * (cols - 1)) / cols
        for i, c in enumerate(cells):
            r, k = divmod(i, cols)
            self.pulse_panel(s, x + k * (pw + gap), y + r * (panel_h + gap), pw,
                             panel_h, c["label"], c["series"], c["range"],
                             theme=c.get("theme", BLUE3))
        rows = (len(cells) + cols - 1) // cols
        return y + rows * (panel_h + gap) - gap

    def lane_row(self, s, x, y, w, h, title, sub=None):
        """Dark swimlane header (P9): product/actor name + one-line role."""
        self.rect(s, x, y, w, h, fill=NAVY)
        runs = [[(title, 13, WHITE, True)]]
        if sub:
            runs.append([(sub, 9.5, SUB_D, False)])
        self.txt(s, x + 0.16, y + (0.12 if sub else 0.0), w - 0.32, h - 0.16, runs,
                 line_sp=1.1, sp_after=3,
                 anchor=MSO_ANCHOR.TOP if sub else MSO_ANCHOR.MIDDLE)

    def stage_column(self, s, x, y, w, h, title, plays, accent=BLUE):
        """Double-click stage column (P8): tint card, blue stage header, numbered
        plays as bold lead + muted body. plays: [(n, name, body)] or [(name, body)]."""
        self.rect(s, x, y, w, h, fill=TINT2)
        self.txt(s, x + 0.14, y + 0.12, w - 0.28, 0.28, title, size=12.5, color=accent,
                 bold=True)
        runs = []
        for i, p in enumerate(plays):
            p = list(p)
            if len(p) == 2:
                p = [i + 1] + p
            nnum, name, body = p[:3]
            runs.append([("%s. %s" % (nnum, name), 11, NAVY, True)])
            runs.append([(body, 10, MUT, False)])
        tb = self.txt(s, x + 0.14, y + 0.48, w - 0.28, h - 0.60, runs, line_sp=1.12,
                      sp_after=3)
        for i, para in enumerate(tb.text_frame.paragraphs):
            if i % 2 == 1:
                para.space_after = Pt(8)
        return tb

    def frame_band(self, s, x, y, w, label, text, h=0.42, accent=BLUE):
        """Dashed framing band (P8): OPPORTUNITY on top of a board, VALUE under it.
        Bold colored label + one navy sentence, ONE line."""
        self.rect(s, x, y, w, h, line=DASHC, line_w=1.0, dash='dash')
        self.txt(s, x + 0.22, y + 0.04, w - 0.44, h - 0.08,
                 [[(label + "   ", 11, accent, True), (text, 11, NAVY, False)]],
                 anchor=MSO_ANCHOR.MIDDLE, wrap=False)

    # ------------------------------------------------------------ comparison layer (v3.3)
    # Waterfall + paired bars (MGI/BCG grammar, round-2 mining) · bullet bars (IBCS)
    # · growth arrow (JPM investor-day walk) · segbar/quadrant/milestone strip
    # (PPTX twins of the HTML engine's layouts). Same discipline: drawn flat shapes.

    def growth_arrow(self, s, x1, y1, x2, y2, label=None, color=BLUE, wpt=1.6,
                     dash=None):
        """Arrowed connector (JPM CAGR style): straight line with a triangle head,
        optional bold label above the midpoint ('+2.1x', '+7% a year'). dash='dash'
        gives the quadrant 'move' arrow."""
        conn = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, I(x1), I(y1), I(x2), I(y2))
        conn.line.color.rgb = color
        conn.line.width = Pt(wpt)
        conn.shadow.inherit = False
        lnel = conn.line._get_or_add_ln()
        if dash:
            lnel.append(lnel.makeelement(qn('a:prstDash'), {'val': dash}))
        lnel.append(lnel.makeelement(qn('a:tailEnd'),
                                     {'type': 'triangle', 'w': 'med', 'len': 'med'}))
        el = conn._element
        for st in el.findall(qn('p:style')):
            el.remove(st)
        if label:
            mx, my = (x1 + x2) / 2.0, min(y1, y2) - 0.30
            self.txt(s, mx - 1.2, my, 2.4, 0.26, label, size=11.5, color=color,
                     bold=True, align=PP_ALIGN.CENTER, wrap=False)
        return conn

    def waterfall(self, s, x, y, w, h, items, val_size=13, cat_size=11,
                  positive='up'):
        """Target-walk waterfall (MGI/IBCS/JPM; round-2 P1). items: (cat, value,
        kind) + optional display — kind 'start'/'end' (absolute, NAVY), 'up' and
        'down' (deltas). `positive` names the GOOD direction: those bars go BLUE,
        the counterweight goes CORAL — on a cost walk pass positive='down' so the
        savings are blue and the honest add-back coral. Floating bars linked by
        dashed step lines; labels above bars carry the numbers; no y-axis."""
        levels, lv = [], 0.0
        for it in items:
            cat, val, kind = it[0], float(it[1]), it[2]
            if kind == 'start':
                lv = val; levels.append((lv - val, lv))
            elif kind == 'up':
                levels.append((lv, lv + val)); lv += val
            elif kind == 'down':
                levels.append((lv - val, lv)); lv -= val
            else:  # end
                levels.append((0.0, val)); lv = val
        vmax = max(top for (_, top) in levels) or 1.0
        baseline = y + h - 0.34
        plot_h = baseline - (y + 0.32)
        pitch = w / len(items)
        bw = pitch * 0.56
        prev_edge = None
        for i, (it, (lo, hi)) in enumerate(zip(items, levels)):
            cat, val, kind = it[0], float(it[1]), it[2]
            disp = it[3] if len(it) > 3 else (
                ("%g" % val) if kind in ('start', 'end') else
                ("+%g" % val if kind == 'up' else "-%g" % val))
            fill = NAVY if kind in ('start', 'end') else (
                BLUE if kind == positive else CORAL)
            bx = x + i * pitch + (pitch - bw) / 2.0
            by = baseline - (hi / vmax) * plot_h
            bh = max(0.02, (hi - lo) / vmax * plot_h)
            self.rect(s, bx, by, bw, bh, fill=fill)
            self.txt(s, x + i * pitch, by - 0.28, pitch, 0.26, disp, size=val_size,
                     color=fill if kind in ('up', 'down') else NAVY, bold=True,
                     align=PP_ALIGN.CENTER, wrap=False)
            self.txt(s, x + i * pitch, baseline + 0.07, pitch, 0.26, cat, size=cat_size,
                     color=NAVY, align=PP_ALIGN.CENTER, wrap=False)
            if prev_edge is not None and kind != 'start':
                # the step joins at the level carried over: an up-bar's floor,
                # a down-bar's (or total's) ceiling
                step_v = lo if kind == 'up' else hi
                step_y = baseline - (step_v / vmax) * plot_h
                self.dashed_conn(s, prev_edge, step_y, bx, step_y, color=DASHC, wpt=0.9)
            prev_edge = bx + bw
        self.hline(s, x, baseline, x + w, baseline, color=NAVY, wpt=1.1)

    def bullet_bars(self, s, x, y, w, items, name_w=2.6, val_w=1.15, row_h=0.62,
                    plan_frac=0.70):
        """IBCS-style attainment rows (round-2 P1): light track, solid BLUE actual,
        NAVY plan tick, bold value right, colored delta after it. items:
        (name, actual, plan, display, delta_display) — delta starting with '-'
        renders CORAL, else BLUE. Each row scales to ITS OWN plan (mixed units
        welcome): the plan tick sits at plan_frac of every track and the bar's
        length is attainment against it, so over-plan rows visibly cross the tick."""
        track_w = w - name_w - val_w - 0.25
        yy = y
        for (name, actual, plan, disp, delta) in items:
            self.txt(s, x, yy + 0.06, name_w - 0.15, 0.26, name, size=12, color=NAVY)
            self.rect(s, x + name_w, yy + 0.06, track_w, 0.20, fill=TINT2)
            attain = float(actual) / float(plan) if float(plan) else 0.0
            bw = min(track_w, track_w * plan_frac * attain)
            self.rect(s, x + name_w, yy + 0.06, bw, 0.20, fill=BLUE)
            px = x + name_w + track_w * plan_frac
            self.rect(s, px - 0.014, yy - 0.005, 0.028, 0.33, fill=NAVY)
            dcol = CORAL if str(delta).startswith("-") else BLUE
            self.txt(s, x + name_w + track_w + 0.15, yy + 0.02, val_w + 0.10, 0.26,
                     [[(disp + "  ", 12.5, NAVY, True), (delta, 10.5, dcol, True)]],
                     wrap=False)
            yy += row_h
        self.txt(s, x + name_w, yy + 0.02, track_w + val_w, 0.22,
                 [[("bar = actual   ", 9.5, MUT, False), ("| = plan", 9.5, NAVY, True),
                   ("   · each row to its own plan", 9.5, MUT, False)]])
        return yy

    def paired_bars(self, s, x, y, w, h, items, from_label="Today",
                    to_label="Target", val_size=13, cat_size=11):
        """From-To paired columns (round-2 P1: 'current vs Backbase as data').
        items: (cat, v_from, v_to, disp_from, disp_to). From = BLUE4, To = BLUE;
        legend drawn top-right of the plot area."""
        vmax = max(max(float(a), float(b)) for (_, a, b, _, _) in items) * 1.12
        baseline = y + h - 0.34
        plot_h = baseline - (y + 0.30)
        pitch = w / len(items)
        bw = pitch * 0.26
        for i, (cat, va, vb, da, db) in enumerate(items):
            cx = x + i * pitch + pitch / 2.0
            ha = float(va) / vmax * plot_h
            hb = float(vb) / vmax * plot_h
            self.rect(s, cx - bw - 0.03, baseline - ha, bw, ha, fill=BLUE4)
            self.rect(s, cx + 0.03, baseline - hb, bw, hb, fill=BLUE)
            self.txt(s, cx - 0.63 - bw / 2 - 0.03, baseline - ha - 0.26, 1.2, 0.24, da,
                     size=val_size - 2, color=MUT, align=PP_ALIGN.CENTER, wrap=False)
            self.txt(s, cx + 0.03 + bw / 2 - 0.6, baseline - hb - 0.28, 1.2, 0.26, db,
                     size=val_size, color=NAVY, bold=True, align=PP_ALIGN.CENTER,
                     wrap=False)
            self.txt(s, x + i * pitch, baseline + 0.07, pitch, 0.26, cat,
                     size=cat_size, color=NAVY, align=PP_ALIGN.CENTER, wrap=False)
        self.hline(s, x, baseline, x + w, baseline, color=NAVY, wpt=1.1)
        lx = x + w - 2.6
        self.rect(s, lx, y - 0.06, 0.14, 0.14, fill=BLUE4)
        self.txt(s, lx + 0.20, y - 0.09, 1.0, 0.22, from_label, size=9.5, color=MUT)
        self.rect(s, lx + 1.25, y - 0.06, 0.14, 0.14, fill=BLUE)
        self.txt(s, lx + 1.45, y - 0.09, 1.2, 0.22, to_label, size=9.5, color=NAVY,
                 bold=True)

    def segbar(self, s, x, y, w, segments, bar_h=0.62, total=None):
        """T03 segmented to-scale bar, engine-backed (HTML 'bar-segmented' twin).
        segments: (name, value, display). Widths strictly proportional; display
        inside the segment (white on dark fills, navy on tints), name below.
        Label every segment only above ~8% share — group the tail first."""
        fills = [BLUE2, BLUE, BLUE3, BLUE4, TINT, TINT2]
        tot = sum(float(v) for (_, v, _) in segments)
        if total:
            self.txt(s, x, y - 0.30, w, 0.24, total, size=12, color=NAVY, bold=True,
                     align=PP_ALIGN.RIGHT, wrap=False)
        sx = x
        for i, (name, v, disp) in enumerate(segments):
            sw = w * float(v) / tot
            fill = fills[i % len(fills)]
            dark = fill in (BLUE2, BLUE, NAVY)
            self.rect(s, sx, y, sw, bar_h, fill=fill)
            self.txt(s, sx, y + bar_h / 2 - 0.13, sw, 0.26, disp, size=12.5,
                     color=WHITE if dark else NAVY, bold=True, align=PP_ALIGN.CENTER,
                     wrap=False)
            self.txt(s, sx, y + bar_h + 0.08, sw, 0.24, name, size=10, color=MUT,
                     align=PP_ALIGN.CENTER, wrap=False)
            sx += sw

    def quadrant(self, s, x, y, w, h, pts, x_title, y_title, zone_caps=None,
                 move=None, dot=0.17, target_zone='tr'):
        """T05 quadrant bubble, engine-backed (HTML 'quadrant' twin). pts:
        (label, fx, fy) with fractions 0-1 from bottom-left. Target quadrant
        tinted, dashed midlines, uppercase zone captions at zone tops, uniform
        BLUE dots; move=(fx1,fy1,fx2,fy2) draws the dashed move arrow."""
        zones = {'tl': (x, y), 'tr': (x + w / 2, y), 'bl': (x, y + h / 2),
                 'br': (x + w / 2, y + h / 2)}
        if target_zone in zones:
            zx, zy = zones[target_zone]
            self.rect(s, zx, zy, w / 2, h / 2, fill=TINT)
        self.rect(s, x, y, w, h, line=HAIR, line_w=0.9)
        self.dashed_conn(s, x + w / 2, y, x + w / 2, y + h, color=DASHC, wpt=0.9)
        self.dashed_conn(s, x, y + h / 2, x + w, y + h / 2, color=DASHC, wpt=0.9)
        if zone_caps:
            spots = [(x + 0.12, y + 0.08), (x + w / 2 + 0.12, y + 0.08),
                     (x + 0.12, y + h / 2 + 0.08), (x + w / 2 + 0.12, y + h / 2 + 0.08)]
            for cap, (cx, cy) in zip(zone_caps, spots):
                if cap:
                    self.txt(s, cx, cy, w / 2 - 0.24, 0.2, cap.upper(), size=9,
                             color=GRAY55, bold=True, track="110")
        for (label, fx, fy) in pts:
            px = x + fx * w
            py = y + (1 - fy) * h
            self.oval(s, px - dot / 2, py - dot / 2, dot, dot, BLUE)
            if fx > 0.78:
                self.txt(s, px - 1.85, py - 0.10, 1.7, 0.22, label, size=10,
                         color=NAVY, bold=True, align=PP_ALIGN.RIGHT, wrap=False)
            else:
                self.txt(s, px + 0.14, py - 0.10, 1.9, 0.22, label, size=10,
                         color=NAVY, bold=True, wrap=False)
        if move:
            f1x, f1y, f2x, f2y = move
            self.growth_arrow(s, x + f1x * w, y + (1 - f1y) * h,
                              x + f2x * w, y + (1 - f2y) * h, color=BLUE, dash='dash')
        self.txt(s, x, y + h + 0.10, w, 0.24, x_title, size=10.5, color=MUT,
                 align=PP_ALIGN.CENTER)
        ty = self.txt(s, x - 1.06, y + h / 2 - 0.13, 1.9, 0.26, y_title, size=10.5,
                      color=MUT, align=PP_ALIGN.CENTER, wrap=False)
        ty.rotation = 270

    def milestone_strip(self, s, x, y, w, items, band=None):
        """T08 milestone strip, engine-backed. items: (numeral, label, sub) — 3 or
        4 oversized numerals over gate diamonds on one line; optional navy band
        (lead, rest) beneath."""
        n = len(items)
        line_y = y + 0.92
        self.hline(s, x + 0.2, line_y, x + w - 0.2, line_y, color=HAIR, wpt=1.1)
        for i, (num, label, sub) in enumerate(items):
            cx = x + w * (i + 0.5) / n
            self.txt(s, cx - 1.2, y - 0.10, 2.4, 0.85, str(num), size=40, color=BLUE2,
                     bold=False, align=PP_ALIGN.CENTER, wrap=False)
            self.diamond(s, cx - 0.075, line_y - 0.075, 0.15, 0.15, BLUE)
            self.txt(s, cx - 1.5, line_y + 0.16, 3.0, 0.26, label, size=12, color=NAVY,
                     bold=True, align=PP_ALIGN.CENTER, wrap=False)
            if sub:
                self.txt(s, cx - 1.7, line_y + 0.42, 3.4, 0.4, sub, size=10, color=MUT,
                         align=PP_ALIGN.CENTER, line_sp=1.1)
        if band:
            lead, rest = band
            self.takeaway_band(s, lead, rest, y=line_y + 1.05, x=x, w=w)

    # ------------------------------------------------------------ evidence layer (v3.4)
    # Grammar mined from the BCG archive (round 4) — layout only, exhibit tokens.
    # Verdict glyphs (harvey, RAG, rings), logo grammar, dossier spine, tiles,
    # tracker rail. Good/covered = BLUE family, tension/gap = CORAL. Never green.

    def harvey(self, s, x, y, d, frac):
        """Quarter-step verdict pie (T30): TINT2 disc + HAIR ring, BLUE wedge
        clockwise from 12 o'clock. frac 0..1 (use 0/.25/.5/.75/1 in ledgers)."""
        import math
        base = s.shapes.add_shape(MSO_SHAPE.OVAL, I(x), I(y), I(d), I(d))
        base.fill.solid()
        base.fill.fore_color.rgb = TINT2
        base.line.color.rgb = HAIR
        base.line.width = Pt(0.9)
        base.shadow.inherit = False
        self.flat(base)
        if frac <= 0:
            return
        if frac >= 1:
            base.fill.fore_color.rgb = BLUE
            base.line.fill.background()
            return
        cx, cy, r = x + d / 2.0, y + d / 2.0, d / 2.0
        E = 914400
        pts = [(int(cx * E), int(cy * E))]
        steps = max(2, int(24 * frac))
        for i in range(steps + 1):
            a = -math.pi / 2 + 2 * math.pi * frac * i / steps
            pts.append((int((cx + r * math.cos(a)) * E), int((cy + r * math.sin(a)) * E)))
        fb = s.shapes.build_freeform(pts[0][0], pts[0][1], scale=1.0)
        fb.add_line_segments(pts[1:], close=True)
        shp = fb.convert_to_shape()
        shp.fill.solid()
        shp.fill.fore_color.rgb = BLUE
        shp.line.fill.background()
        shp.shadow.inherit = False
        self.flat(shp)

    def logo_chip(self, s, x, y, w, h, img=None, name=None, caption=None):
        """White logo card (T32): hairline border, centered logo image, or the
        name as clean 12pt bold navy text when no asset exists (never fabricate
        a logo). Optional 9.5 caption pinned to the chip's bottom."""
        self.rect(s, x, y, w, h, fill=WHITE, line=HAIR, line_w=0.75, round_=True)
        area_h = h - (0.24 if caption else 0.0)
        if img and os.path.exists(img):
            try:
                from PIL import Image as _Im
                iw, ih = _Im.open(img).size
                pad = 0.12
                sc = min((w - 2 * pad) / iw, (area_h - 2 * pad) / ih)
                pw, ph = iw * sc, ih * sc
                s.shapes.add_picture(img, I(x + (w - pw) / 2),
                                     I(y + (area_h - ph) / 2), I(pw), I(ph))
            except Exception:
                img = None
        if not img and name:
            self.txt(s, x + 0.06, y, w - 0.12, area_h, name, size=12, color=NAVY,
                     bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
                     line_sp=0.98)
        if caption:
            self.txt(s, x + 0.06, y + h - 0.26, w - 0.12, 0.20, caption, size=9.5,
                     color=MUT, align=PP_ALIGN.CENTER, wrap=False)

    def logo_wall(self, s, x, y, w, items, cols, chip_h=0.55, gap=0.10):
        """Grid of logo chips (T32). items: name strings or dicts
        {img, name, caption}. Returns the y just under the wall."""
        cw = (w - gap * (cols - 1)) / cols
        for i, it in enumerate(items):
            if isinstance(it, str):
                it = {"name": it}
            r, c = divmod(i, cols)
            self.logo_chip(s, x + c * (cw + gap), y + r * (chip_h + gap), cw,
                           chip_h, img=it.get("img"), name=it.get("name"),
                           caption=it.get("caption"))
        rows = (len(items) + cols - 1) // cols
        return y + rows * (chip_h + gap) - gap

    def eval_matrix(self, s, x, y, w, cols, rows, cells, name_w=2.75, row_h=0.62,
                    ball=0.30, legend=True):
        """Evaluation matrix (T31): vendor columns (logo img or clean-text name +
        sub-label) x criteria rows (monogram square + label), harvey verdict per
        cell, hairline row rules, legend. cells[i][j] = frac 0..1 or None."""
        n = len(cols)
        pitch = (w - name_w) / n
        for j, c in enumerate(cols):
            if isinstance(c, str):
                c = {"name": c}
            cxm = x + name_w + j * pitch
            if c.get("img") and os.path.exists(c["img"]):
                self.logo_chip(s, cxm + pitch / 2 - 0.55, y, 1.1, 0.42, img=c["img"])
            else:
                self.txt(s, cxm, y + 0.02, pitch, 0.24, c["name"], size=11,
                         color=NAVY, bold=True, align=PP_ALIGN.CENTER, wrap=False)
            if c.get("sub"):
                self.txt(s, cxm, y + 0.26, pitch, 0.2, c["sub"], size=9, color=MUT,
                         align=PP_ALIGN.CENTER, wrap=False)
        top = y + 0.54
        self.hline(s, x, top, x + w, top, color=HAIR, wpt=0.9)
        yy = top + 0.10
        for i, r in enumerate(rows):
            glyph, label = (r if isinstance(r, (list, tuple)) else ("·", r))[:2]
            self.rect(s, x, yy + row_h / 2 - 0.11, 0.22, 0.22, fill=TINT, round_=True)
            self.txt(s, x + 0.015, yy + row_h / 2 - 0.095, 0.19, 0.19, glyph, size=10,
                     color=BLUE, bold=True, align=PP_ALIGN.CENTER, wrap=False)
            self.txt(s, x + 0.32, yy + row_h / 2 - 0.20, name_w - 0.4, 0.44, label,
                     size=11, color=NAVY, line_sp=1.02, anchor=MSO_ANCHOR.MIDDLE)
            for j in range(len(cols)):
                v = cells[i][j]
                if v is None:
                    continue
                bx = x + name_w + j * pitch + pitch / 2 - ball / 2
                self.harvey(s, bx, yy + row_h / 2 - ball / 2, ball, v)
            yy += row_h
            self.hline(s, x, yy, x + w, yy, color=HAIR_ROW, wpt=0.75)
        if legend:
            self.harvey(s, x + w - 3.30, yy + 0.12, 0.16, 1.0)
            self.txt(s, x + w - 3.08, yy + 0.11, 1.2, 0.2, "fulfilled", size=9.5, color=MUT, wrap=False)
            self.harvey(s, x + w - 1.95, yy + 0.12, 0.16, 0.0)
            self.txt(s, x + w - 1.73, yy + 0.11, 1.7, 0.2, "not fulfilled", size=9.5, color=MUT, wrap=False)
        return yy

    def fact_rail(self, s, x, y, w, items, pitch=0.56):
        """Dossier fact rail (T33): monogram square + bold label + muted value,
        one fact per row. items: (glyph, label, value)."""
        yy = y
        for (glyph, label, value) in items:
            self.rect(s, x, yy, 0.24, 0.24, fill=TINT, round_=True)
            self.txt(s, x + 0.01, yy + 0.015, 0.22, 0.21, glyph, size=10.5, color=BLUE,
                     bold=True, align=PP_ALIGN.CENTER, wrap=False)
            self.txt(s, x + 0.38, yy - 0.015, w - 0.38, pitch - 0.06,
                     [[(label + ":  ", 11, NAVY, True), (value, 11, MUT, False)]],
                     line_sp=1.05)
            yy += pitch
        return yy

    def leader_note(self, s, x1, y1, x2, y2, lead, body=None, w=1.95,
                    align=PP_ALIGN.LEFT):
        """Dashed leader line to a floating note (T34): bold navy lead, muted
        body. The dossier/product-shot annotation grammar."""
        self.dashed_conn(s, x1, y1, x2, y2, color=DASHC, wpt=0.9)
        tx = x2 if align == PP_ALIGN.LEFT else x2 - w
        runs = [[(lead, 10.5, NAVY, True)]]
        if body:
            runs.append([(body, 10, MUT, False)])
        self.txt(s, tx + (0.08 if align == PP_ALIGN.LEFT else -0.08), y2 - 0.10, w,
                 0.8, runs, line_sp=1.1, sp_after=2, align=align)

    def tiles(self, s, x, y, w, cells, cols, h=1.25, gap=0.12):
        """Uniform tile grid (T35): TINT2 cards with a thin accent top bar, bold
        title, muted body, optional BLUE bold footer stat. cells: {title, body,
        stat?, accent?}. Whitespace law: never stretch tiles to fill — add tiles
        or shrink the grid."""
        cw = (w - gap * (cols - 1)) / cols
        for i, c in enumerate(cells):
            r, k = divmod(i, cols)
            tx = x + k * (cw + gap)
            ty = y + r * (h + gap)
            self.rect(s, tx, ty, cw, h, fill=TINT2)
            self.rect(s, tx, ty, cw, 0.035, fill=c.get("accent", BLUE3))
            self.txt(s, tx + 0.14, ty + 0.13, cw - 0.28, 0.42, c["title"], size=11.5,
                     color=NAVY, bold=True, line_sp=1.02)
            self.txt(s, tx + 0.14, ty + 0.47, cw - 0.28, h - (0.82 if c.get("stat") else 0.60),
                     c["body"], size=10, color=MUT, line_sp=1.14)
            if c.get("stat"):
                self.txt(s, tx + 0.14, ty + h - 0.32, cw - 0.28, 0.24, c["stat"],
                         size=11.5, color=BLUE, bold=True, wrap=False)
        rows = (len(cells) + cols - 1) // cols
        return y + rows * (h + gap) - gap

    def agenda_rail(self, s, x, y, w, items, active, row_h=0.56):
        """Agenda/tracker rail (T36): numbered rows, the active chapter lit BLUE.
        Re-show it at each chapter with the light moved — the serial-agenda
        device. `active` is 1-based."""
        yy = y
        for i, label in enumerate(items, start=1):
            on = (i == active)
            self.rect(s, x, yy, 0.34, 0.34, fill=BLUE if on else TINT2, round_=True)
            self.txt(s, x + 0.005, yy + 0.045, 0.33, 0.26, str(i), size=12,
                     color=WHITE if on else MUT, bold=True, align=PP_ALIGN.CENTER,
                     wrap=False)
            self.txt(s, x + 0.52, yy + 0.045, w - 0.52, 0.30, label,
                     size=13 if on else 12.5, color=NAVY if on else MUT, bold=on,
                     wrap=False)
            yy += row_h
        return yy

    def ring_stat(self, s, x, y, d, value, caption=None, color=BLUE, vs=19):
        """Outlined ring stat (T37): open circle, bold value inside, caption
        below. Row of 3-5 rings = the proof strip."""
        ov = s.shapes.add_shape(MSO_SHAPE.OVAL, I(x), I(y), I(d), I(d))
        ov.fill.background()
        ov.line.color.rgb = color
        ov.line.width = Pt(2.5)
        ov.shadow.inherit = False
        self.flat(ov)
        self.txt(s, x - 0.3, y + d / 2 - 0.17, d + 0.6, 0.34, value, size=vs,
                 color=color, bold=True, align=PP_ALIGN.CENTER, wrap=False,
                 anchor=MSO_ANCHOR.MIDDLE)
        if caption:
            self.txt(s, x - 0.45, y + d + 0.08, d + 0.9, 0.42, caption, size=10,
                     color=MUT, align=PP_ALIGN.CENTER, line_sp=1.08)

    def rag_matrix(self, s, x, y, w, row_labels, col_labels, cells, row_h=0.42,
                   label_w=2.7, legend=True):
        """Coverage matrix (T38): rows x columns of verdict chips — 'g' covered
        (BLUE, white), 'p' partial (BLUE4, navy), 'r' gap (CORAL, white),
        'n' n/a (TINT2, muted). cells[i][j] = code or (code, text). Legend
        mandatory in client decks."""
        colors = {'g': (BLUE, WHITE, "covered"), 'p': (BLUE4, NAVY, "partial"),
                  'r': (CORAL, WHITE, "gap"), 'n': (TINT2, MUT, "not needed")}
        n = len(col_labels)
        pitch = (w - label_w) / n
        for j, cl in enumerate(col_labels):
            self.txt(s, x + label_w + j * pitch, y, pitch, 0.24, cl, size=10.5,
                     color=NAVY, bold=True, align=PP_ALIGN.CENTER, wrap=False)
        yy = y + 0.34
        for i, rl in enumerate(row_labels):
            self.txt(s, x, yy + 0.05, label_w - 0.15, 0.3, rl, size=10.5, color=NAVY,
                     wrap=False)
            for j in range(n):
                v = cells[i][j]
                code, text = (v if isinstance(v, (list, tuple)) else (v, None))[:2]
                fill, tc, _ = colors[code]
                cxm = x + label_w + j * pitch
                self.rect(s, cxm + 0.06, yy, pitch - 0.12, row_h - 0.10, fill=fill,
                          round_=True)
                if text:
                    self.txt(s, cxm + 0.10, yy + 0.03, pitch - 0.20, row_h - 0.16,
                             text, size=8.5, color=tc, align=PP_ALIGN.CENTER,
                             anchor=MSO_ANCHOR.MIDDLE, line_sp=0.95)
            yy += row_h
        if legend:
            lx = x + label_w
            for code in ('g', 'p', 'r', 'n'):
                fill, tc, lab = colors[code]
                self.rect(s, lx, yy + 0.10, 0.22, 0.16, fill=fill, round_=True)
                self.txt(s, lx + 0.28, yy + 0.085, 1.15, 0.2, lab, size=9.5,
                         color=MUT, wrap=False)
                lx += 1.45
        return yy

    def tag_chip(self, s, text, x=None, y=0.62, kind='honest'):
        """Top-right status tag (T39): ILLUSTRATIVE / PRELIMINARY / NOT
        EXHAUSTIVE (coral outline — extends the honesty-badge convention) or
        BACKUP (quiet tint). Sits just under the top hairline."""
        w = 0.30 + len(text) * 0.082
        if x is None:
            x = 12.66 - w
        if kind == 'honest':
            self.rect(s, x, y, w, 0.26, line=CORAL, line_w=1.0, dash='dash', round_=True)
            tc = CORAL
        else:
            self.rect(s, x, y, w, 0.26, fill=TINT2, round_=True)
            tc = MUT
        self.txt(s, x, y + 0.045, w, 0.18, text.upper(), size=8.5, color=tc,
                 bold=True, align=PP_ALIGN.CENTER, wrap=False, track="110")

    # ------------------------------------------------------------ v4 layer (18 Sep 2026): the Claude Design look
    # Measured from the Nedbank ENBI Voice VC report (mining round 6, references/visual-grammar-v4.md).
    # Every helper reads the ACTIVE palette at call time, so it draws in v3 tokens under
    # ExhibitDeck() and in v4 tokens under ExhibitDeck(look='v4'). Additive: nothing above changed.

    WEIGHT_BREAKS = (2, 8, 16)

    def _weight(self, weight):
        """(fill, border, dash, title colour, sub colour) for a card weight. The ramp: faint
        (TINT2 + CARD_LINE border) < light (TINT) < mid (BLUE3) < dark (NAVY); blue = the active
        step; outline = someone else's stack; dashed = comparison only; grey = today, as is."""
        table = {
            'faint':   (TINT2, CARD_LINE, None, NAVY, MUT),
            'light':   (TINT, None, None, NAVY, MUT),
            'mid':     (BLUE3, None, None, WHITE, SUB_D),
            'dark':    (NAVY, None, None, WHITE, SUB_D),
            'blue':    (BLUE, None, None, WHITE, WHITE),
            'grey':    (GREY, None, None, NAVY, MUT),
            'outline': (WHITE, CARD_LINE, None, NAVY, MUT),
            'dashed':  (WHITE, DASHC, 'dash', NAVY, MUT),
            'white':   (WHITE, None, None, NAVY, MUT),
        }
        if weight not in table:
            raise ValueError("unknown weight %r (use one of %s)" % (weight, ", ".join(table)))
        return table[weight]

    @staticmethod
    def weight_for(count, breaks=None):
        """Reuse count to weight, slide 15's legend: <=2 faint, <=8 light, <=16 mid, else dark."""
        if count is None:
            return 'light'
        b = breaks or ExhibitDeck.WEIGHT_BREAKS
        n = int(count)
        return 'faint' if n <= b[0] else 'light' if n <= b[1] else 'mid' if n <= b[2] else 'dark'

    @staticmethod
    def _est_lines(text, w, size, em=0.48):
        """Rough line count of `text` in a w-inch box at `size` pt (Libre Franklin runs at about
        0.48 em per character). Used to bottom-anchor captions; pass cap_lines to override."""
        import math
        if not text:
            return 0
        cpl = max(1.0, w * 72.0 / (size * em))
        return max(1, int(math.ceil(len(text) / cpl)))

    # ---- client logo (v4 rule: client decks carry the client's logo, internal decks do not)
    def set_client_logo(self, path, box=None):
        """Deck-level client logo. Every chrome() after this call places it top right.
        box = (x, y, w, h); the measured default is (12.60, -0.08, 0.60, 0.69)."""
        self.client_logo = path
        if box:
            self.client_logo_box = tuple(box)

    def client_logo_mark(self, s, path=None, box=None, stretch=False):
        """Place the client logo once on a slide. The export stretches the image into the box;
        by default the engine fits it inside the box and keeps its aspect (stretch=True
        reproduces the export exactly). Returns the picture or None when no file exists."""
        path = path or self.client_logo
        if not path or not os.path.exists(path):
            return None
        x, y, w, h = box or self.client_logo_box
        if not stretch:
            try:
                from PIL import Image as _Im
                iw, ih = _Im.open(path).size
                sc = min(w / float(iw), h / float(ih))
                pw, ph = iw * sc, ih * sc
                x, y, w, h = x + (w - pw) / 2.0, y + (h - ph) / 2.0, pw, ph
            except Exception:
                pass
        return s.shapes.add_picture(path, I(x), I(y), I(w), I(h))

    def _chrome_v4(self, s, kicker, title, page, title_size, frame, client_logo, client_logo_box):
        """The v4 chrome: three rules + corner mark, 9pt navy kicker, 28pt regular title without a
        trailing period, wordmark at 11.35, 9pt grey page number, client logo top right."""
        if frame:
            self.hline(s, 0, 0.573, W, 0.573)
            self.hline(s, 0.573, 0, 0.573, 7.042)
            self.hline(s, 0, 7.042, W, 7.042)
            self.step_glyph(s, 0.406, 0.406, 0.167, 0.166, BLUE)
        if kicker:
            self.txt(s, 1.0, 0.86, 8.0, 0.22, kicker.upper(), size=9, color=NAVY, track="60")
        if title:
            self.txt(s, 1.0, 1.10, 11.9, 0.9, title, size=(28 if title_size is None else title_size),
                     color=NAVY, bold=False, line_sp=1.04)
        if self.logo and os.path.exists(self.logo):
            s.shapes.add_picture(self.logo, I(11.35), I(7.185), I(1.067), I(0.173))
        else:
            self.txt(s, 10.3, 7.16, 2.1, 0.25, "Backbase", size=13, color=RGBColor(0, 0, 0),
                     bold=True, align=PP_ALIGN.RIGHT)
        self.page_field(s, page, x=12.55, y=7.16, w=0.5, h=0.24, size=9, color=FN, bold=False)
        self.client_logo_mark(s, client_logo, client_logo_box)

    # ---- cards
    def card(self, s, x, y, w, title, sub=None, count=None, weight='light', h=0.62,
             title_size=None, sub_size=7.5, count_size=8.5):
        """The v4 card (slide 15): w x 0.62 box, 9pt title at (+0.10, +0.07), 8.5pt count badge
        right-aligned at (x+w-0.50, +0.05), 7.5pt sub-line at (+0.10, +0.29). h=0.50 gives the
        system tile (8pt title, no sub). weight: faint | light | mid | dark | blue | outline |
        dashed | grey | white (see _weight)."""
        fill, line, dash, tc, sc = self._weight(weight)
        self.rect(s, x, y, w, h, fill=fill, line=line, line_w=0.75, dash=dash)
        ts = title_size or (9 if h >= 0.6 else 8)
        tw = w - (0.37 if count is not None else 0.20)
        th = 0.21 if sub else min(0.38, h - 0.14)
        self.txt(s, x + 0.10, y + 0.07, tw, th, title, size=ts, color=tc, line_sp=1.0)
        if count is not None:
            self.txt(s, x + w - 0.50, y + 0.05, 0.44, 0.21, str(count), size=count_size, color=tc,
                     align=PP_ALIGN.RIGHT, wrap=False)
        if sub:
            self.txt(s, x + 0.10, y + 0.29, w - 0.16, max(0.22, h - 0.33), sub, size=sub_size,
                     color=sc, line_sp=1.05)
        return y + h

    def card_row(self, s, x, y, cards, unit_w=1.62, h=0.62, gap=0.11, cols=None, row_gap=0.06,
                 count_breaks=None):
        """A row of cards. cards: dicts {title, sub, count, weight, span}. A card without a weight
        takes it from its count (weight_for). span=2 makes the double card (2 units + gap). With
        cols, the row wraps after that many units. Returns the y under the last row."""
        cx, cy, used = x, y, 0
        for c in cards:
            span = int(c.get('span', 1))
            w = unit_w * span + gap * (span - 1)
            if cols and used and used + span > cols:
                cx, cy, used = x, cy + h + row_gap, 0
            weight = c.get('weight') or self.weight_for(c.get('count'), count_breaks)
            self.card(s, cx, cy, w, c['title'], c.get('sub'), c.get('count'), weight, h=h,
                      title_size=c.get('title_size'))
            cx += w + gap
            used += span
        return cy + h

    def lane_grid(self, s, x, y, lanes, label_w=1.55, unit_w=1.62, h=0.62, gap=0.11,
                  lane_gap=0.13, count_breaks=None):
        """Slide 15: labelled lanes, cards to the right. lanes: dicts {label, sub, cards} plus
        optional per-lane unit_w, h, gap, cols, row_gap. Label 8pt BLUE uppercase at (+0.06),
        sub 8pt MUT at (+0.25); cards start at x + label_w. Returns the y under the last lane."""
        yy = y
        for ln in lanes:
            lh = ln.get('h', h)
            self.txt(s, x, yy + 0.06, label_w - 0.05, 0.18, ln['label'].upper(), size=8, color=BLUE,
                     track="40", wrap=False)
            if ln.get('sub'):
                self.txt(s, x, yy + 0.25, label_w + 0.04, 0.21, ln['sub'], size=8, color=MUT, wrap=False)
            bottom = self.card_row(s, x + label_w, yy, ln['cards'], unit_w=ln.get('unit_w', unit_w),
                                   h=lh, gap=ln.get('gap', gap), cols=ln.get('cols'),
                                   row_gap=ln.get('row_gap', 0.06), count_breaks=count_breaks)
            yy = bottom + lane_gap
        return yy - lane_gap

    def weight_legend(self, s, x, y, items, lead="Reused by", note=None, note_right=12.60, size=8.5):
        """The fill-weight legend (slide 15, y=6.40): lead 8.5 MUT, 0.16 swatches, labels,
        optional right-aligned note in FN. items: [(weight, label)]."""
        xx = x
        if lead:
            self.txt(s, xx, y, 0.98, 0.21, lead, size=size, color=MUT, wrap=False)
            xx += 0.85
        for weight, label in items:
            fill, line, dash, _, _ = self._weight(weight)
            self.rect(s, xx, y + 0.03, 0.16, 0.16, fill=fill, line=line, line_w=0.75, dash=dash)
            self.txt(s, xx + 0.24, y, 2.2, 0.21, label, size=size, color=MUT, wrap=False)
            xx += max(1.35, 0.24 + len(label) * 0.065 + 0.55)
        if note:
            self.txt(s, xx, y, max(1.0, note_right - xx), 0.21, note, size=size, color=FN,
                     align=PP_ALIGN.RIGHT, wrap=False)
        return y + 0.21

    # ---- numbers
    def stat_block(self, s, x, y, w, h, number, caption, dark=False, icon=None, num_size=33,
                   cap_size=9, cap_lines=None):
        """Slide 6: a 2.73 x 2.22 stat block. TINT2 (or NAVY) card, optional 0.25 icon top left,
        33pt number (BLUE on tint, CYAN on dark) and 9pt caption bottom-anchored 0.17 above the
        card's bottom edge. cap_lines overrides the estimated caption line count."""
        self.rect(s, x, y, w, h, fill=(NAVY if dark else TINT2))
        if icon and os.path.exists(icon):
            s.shapes.add_picture(icon, I(x + 0.21), I(y + 0.21), I(0.25), I(0.25))
        cw = w - 0.33
        lines = cap_lines or self._est_lines(caption, cw, cap_size)
        cap_h = 0.175 * lines + 0.045
        cap_y = y + h - 0.17 - cap_h
        self.txt(s, x + 0.21, cap_y - 0.56, w - 0.19, 0.50, number, size=num_size,
                 color=(CYAN if dark else BLUE), wrap=False)
        self.txt(s, x + 0.21, cap_y, cw, cap_h, caption, size=cap_size,
                 color=(WHITE if dark else NAVY), line_sp=1.1)
        return y + h

    def stat_grid(self, s, x, y, cells, cols=4, w=2.73, h=2.22, gap=0.145, row_gap=0.14):
        """The eight-number floor: a grid of stat blocks. cells: dicts {number, caption, dark,
        icon, num_size, cap_lines}. Returns the y under the grid."""
        for i, c in enumerate(cells):
            r, k = divmod(i, cols)
            self.stat_block(s, x + k * (w + gap), y + r * (h + row_gap), w, h, c["number"],
                            c["caption"], dark=c.get("dark", False), icon=c.get("icon"),
                            num_size=c.get("num_size", 33), cap_lines=c.get("cap_lines"))
        rows = (len(cells) + cols - 1) // cols
        return y + rows * (h + row_gap) - row_gap

    def hero_number(self, s, x, y, w, h, number, caption, dark=True, layout='side', num_size=33,
                    cap_size=9):
        """Slides 27 and 37: the dark block with the cyan number. layout='side' puts the caption
        to the right of the number (5.83 x 0.83 block); 'stack' puts it under (3.65 x 1.28).
        dark=False gives the tinted companion (TINT2 block, BLUE number, NAVY caption)."""
        self.rect(s, x, y, w, h, fill=(NAVY if dark else TINT2))
        nc = CYAN if dark else BLUE
        cc = WHITE if dark else NAVY
        nh = num_size / 72.0 * 1.1
        if layout == 'side':
            self.txt(s, x + 0.21, y + 0.19, 2.56, nh, number, size=num_size, color=nc, wrap=False)
            self.txt(s, x + 2.77, y + (0.24 if num_size >= 30 else 0.19), w - 2.98, h - 0.36,
                     caption, size=cap_size, color=cc, line_sp=1.1)
        else:
            self.txt(s, x + 0.21, y + 0.21, w - 0.31, nh, number, size=num_size, color=nc, wrap=False)
            self.txt(s, x + 0.21, y + 0.21 + nh, w - 0.53, h - nh - 0.30, caption, size=cap_size,
                     color=cc, line_sp=1.1)
        return y + h

    def mini_stat(self, s, x, y, w, label, value, suffix=None, suffix_color=None, dark=False,
                  label_size=7.5, value_size=13.5, suffix_size=8.25):
        """Slides 31 and 44: 7.5pt uppercase label over a 13.5pt value, optional small suffix
        (a delta in BLUE, a unit in NAVY). Returns the y under the value."""
        lc = WHITE if dark else NAVY
        self.txt(s, x, y, w, 0.17, label.upper(), size=label_size, color=lc, track="20", wrap=False)
        runs = [(value, value_size, lc, False)]
        if suffix:
            runs.append((" " + suffix, suffix_size, suffix_color or lc, False))
        vy = y + 0.12 + max(0.0, value_size - 13.5) * 0.0035
        self.txt(s, x, vy, w, value_size / 72.0 * 1.35, [runs], line_sp=1.0)
        return vy + value_size / 72.0 * 1.35

    def stat_column(self, s, x, y, w, label, number, sub, body, color=None, highlight=False,
                    num_size=34):
        """Slide 26 (stat trio): 8.5pt label, 34pt number, 11.5pt sub, 9.5pt muted body.
        highlight=True draws the TINT panel behind the column and lifts the number to BLUE."""
        if highlight:
            self.rect(s, x - 0.20, y - 0.22, w + 0.35, 3.90, fill=TINT)
        self.txt(s, x, y, w, 0.19, label.upper(), size=8.5, color=(BLUE if highlight else MUT),
                 track="40", wrap=False)
        self.txt(s, x, y + 0.28, w, 0.51, number, size=num_size,
                 color=(color or (BLUE if highlight else NAVY)), wrap=False)
        self.txt(s, x, y + 1.08, w + 0.24, 0.21, sub, size=11.5, color=NAVY, wrap=False)
        self.txt(s, x, y + 1.48, w - 0.05, 1.2, body, size=9.5, color=MUT, line_sp=1.15)
        return y + 2.7

    def panel(self, s, x, y, w, h, weight='faint', border=None, round_=False):
        """Tinted panel behind a composed exhibit (slide 31's three states, highlight panels).
        border: None (slide 31), 'soft' = LINE_SOFT (question and option cards), 'hair' =
        CARD_LINE. weight='dashed' gives the comparison-only panel."""
        fill, _, dash, _, _ = self._weight(weight)
        line = {None: None, 'soft': LINE_SOFT, 'hair': CARD_LINE, 'dashed': DASHC}[border]
        if weight == 'dashed':
            line, dash = DASHC, 'dash'
        return self.rect(s, x, y, w, h, fill=fill, line=line, line_w=0.75, dash=dash, round_=round_)

    def statement_line(self, s, x, y, w, lead, rest, size=12, rest_color=None):
        """The 12pt line under an exhibit (slides 10, 14): NAVY lead + BLUE (or MUT) rest."""
        return self.txt(s, x, y, w, 0.41, [[(lead + " ", size, NAVY, False),
                                            (rest, size, rest_color or BLUE, False)]], line_sp=1.15)

    # ---- pages and bands
    def cover_page(self, kicker, title_runs, date_line=None, client_logo=None, accent=None,
                   title_size=54):
        """Slide 1: navy cover with the offset frame (COVER_LINE 0.5pt: top rule at 1.62, inner
        vertical at 8.64, inner horizontal at 5.20 to 8.64, rails at 0.55 and 12.78), white glyph
        at the inner crossing, wordmark top left, client logo at (1.19, 1.76), 9.5pt kicker, 54pt
        title, 12pt date line. title_runs: a string, or [(text, colour)] with the accent word in
        `accent` (default CYAN). Creates and returns the slide."""
        s = self.slide()
        self.rect(s, 0, 0, W, H, fill=NAVY)
        self.hline(s, 0.55, 1.62, 12.79, 1.62, color=COVER_LINE, wpt=0.5)
        self.hline(s, 8.64, 0, 8.64, H, color=COVER_LINE, wpt=0.5)
        self.hline(s, 0.55, 5.20, 8.64, 5.20, color=COVER_LINE, wpt=0.5)
        self.hline(s, 0.55, 0, 0.55, H, color=COVER_LINE, wpt=0.5)
        self.hline(s, 12.78, 0, 12.78, H, color=COVER_LINE, wpt=0.5)
        self.step_glyph(s, 8.47, 1.62, 0.167, 0.166, WHITE)
        if LOGO_WHITE and os.path.exists(LOGO_WHITE):
            s.shapes.add_picture(LOGO_WHITE, I(0.60), I(0.42), I(1.05), I(0.17))
        else:
            self.txt(s, 0.60, 0.40, 3.0, 0.35, "Backbase", size=16, color=WHITE, bold=True)
        self.client_logo_mark(s, client_logo, (1.19, 1.76, 0.60, 0.69))
        if kicker:
            self.txt(s, 1.09, 2.45, 8.0, 0.22, kicker.upper(), size=9.5, color=WHITE, track="80")
        if isinstance(title_runs, str):
            title_runs = [(title_runs, WHITE)]
        acc = accent or CYAN
        runs = [[(t, title_size, (c if c is not None else acc), False) for (t, c) in title_runs]]
        self.txt(s, 1.06, 2.95, 11.2, 1.5, runs, line_sp=1.05)
        if date_line:
            self.txt(s, 1.00, 5.71, 6.61, 0.27, date_line, size=12, color=WHITE)
        return s

    def divider_band(self, title, kicker=None, sub=None, fill=None):
        """Slide 62: the appendix divider. Full BLUE page, white 0.5pt rules (y=1.62 across, y=4.86
        from the left rail, rails at x=0.55 and 12.78), white glyph at (0.38, 1.45), 40pt white
        title at (1.11, 2.95). Creates and returns the slide (it counts a page)."""
        s = self.slide()
        self.rect(s, 0, 0, W, H, fill=(fill or BLUE))
        self.hline(s, 0, 1.62, 12.79, 1.62, color=WHITE, wpt=0.5)
        self.hline(s, 0.55, 4.86, 12.79, 4.86, color=WHITE, wpt=0.5)
        self.hline(s, 0.55, 0, 0.55, H, color=WHITE, wpt=0.5)
        self.hline(s, 12.78, 0, 12.78, H, color=WHITE, wpt=0.5)
        self.step_glyph(s, 0.38, 1.45, 0.167, 0.166, WHITE)
        if kicker:
            self.txt(s, 1.11, 2.21, 8.0, 0.27, kicker.upper(), size=13, color=WHITE, track="60")
        self.txt(s, 1.11, 2.95, 10.5, 0.9, title, size=40, color=WHITE, bold=False)
        if sub:
            self.txt(s, 1.11, 4.05, 8.0, 0.6, sub, size=14, color=WHITE, line_sp=1.2)
        return s

    def vision_band(self, s, kicker, runs, y=1.85, h=3.70, fill=None, accent=None, notch=True,
                    size=30):
        """Slide 2: the vision band. A tint band across the frame (0.57 to 12.77) with two white
        notches cut out (top left 3.69 x 0.55, bottom right 2.77 x 0.45), the kicker in the top
        notch, a 30pt statement with its core in the accent colour. runs: a string, or
        [(text, colour_or_None)] where None takes `accent` (default BLUE). Call chrome() with
        empty kicker and title first."""
        self.rect(s, 0.57, y, 12.20, h, fill=(fill or TINT))
        if notch:
            self.rect(s, 0.58, y, 3.69, 0.55, fill=WHITE)
            self.rect(s, 10.00, y + h - 0.45, 2.77, 0.45, fill=WHITE)
        if kicker:
            self.txt(s, 1.00, y + 0.18, 4.0, 0.20, kicker.upper(), size=9, color=NAVY, track="60")
        if isinstance(runs, str):
            runs = [(runs, NAVY)]
        acc = accent or BLUE
        para = [[(t, size, (c if c is not None else acc), False) for (t, c) in runs]]
        self.txt(s, 1.00, y + 1.00, 11.12, h - 1.40, para, line_sp=1.12)
        return y + h

    def film_frame(self, s, x, y, w, poster=None, caption=None, sub=None, movie=None, tag="film",
                   h=None):
        """Slide 22: a 16:9 film frame with the navy "film" tag at its bottom left, 9pt caption
        under it, 8pt muted sub. poster = image path; movie = mp4 path (embedded with the poster
        as its frame); neither = a navy placeholder frame. Returns the y under the image."""
        h = h or w * 9 / 16.0
        if movie and os.path.exists(movie):
            s.shapes.add_movie(movie, I(x), I(y), I(w), I(h), poster_frame_image=poster,
                               mime_type="video/mp4")
        elif poster and os.path.exists(poster):
            s.shapes.add_picture(poster, I(x), I(y), I(w), I(h))
        else:
            self.rect(s, x, y, w, h, fill=NAVY)
            self.txt(s, x, y + h / 2 - 0.2, w, 0.4, "▶", size=18, color=WHITE,
                     align=PP_ALIGN.CENTER, wrap=False)
        self.rect(s, x, y + h - 0.30, 0.95, 0.30, fill=NAVY)
        self.txt(s, x + 0.08, y + h - 0.27, 0.9, 0.21, tag, size=8.5, color=WHITE, wrap=False)
        if caption:
            self.txt(s, x, y + h + 0.10, w + 0.22, 0.40, caption, size=9, color=NAVY, line_sp=1.05)
        if sub:
            self.txt(s, x, y + h + 0.56, w + 0.08, 0.60, sub, size=8, color=MUT, line_sp=1.1)
        return y + h

    # ---- rows, columns, flows
    def numbered_rows(self, s, x, y, w, items, pitch=0.78, num_size=15, size=11.5, num_w=0.90):
        """Slide 5 (agenda): 15pt BLUE two-digit numbers, 11.5pt lines, CARD_LINE rules."""
        yy = y
        self.rect(s, x, yy, w, 0.01, fill=CARD_LINE)
        for i, t in enumerate(items, 1):
            self.txt(s, x, yy + 0.13, 0.78, 0.25, "%02d" % i, size=num_size, color=BLUE, wrap=False)
            self.txt(s, x + num_w, yy + 0.17, w - num_w, 0.24, t, size=size, color=NAVY, wrap=False)
            yy += pitch
            self.rect(s, x, yy, w, 0.01, fill=CARD_LINE)
        return yy

    def from_to_columns(self, s, y, from_label, from_items, to_label, to_items, x=1.0, w=11.6,
                        pitch=0.66, size=10):
        """Slide 3: two bullet columns, muted on the left (from), navy with blue bullets on the
        right (to), a vertical rule between them carrying a 22pt blue arrow. Returns the y under
        the longer column."""
        colw = 5.10 * (w / 11.6)
        lx, rx = x, x + 6.40 * (w / 11.6)
        self.txt(s, lx, y, 4.0, 0.19, from_label.upper(), size=8.5, color=MUT, track="40", wrap=False)
        self.txt(s, rx, y, 4.0, 0.19, to_label.upper(), size=8.5, color=MUT, track="40", wrap=False)
        yy = y + 0.28
        n = max(len(from_items), len(to_items))
        for i in range(n):
            if i < len(from_items):
                self.txt(s, lx, yy, 0.28, 0.21, "•", size=size, color=MUT, wrap=False)
                self.txt(s, lx + 0.25, yy, colw, pitch - 0.08, from_items[i], size=size, color=MUT,
                         line_sp=1.12)
            if i < len(to_items):
                self.txt(s, rx, yy, 0.28, 0.21, "•", size=size, color=BLUE, wrap=False)
                self.txt(s, rx + 0.25, yy, colw, pitch - 0.08, to_items[i], size=size, color=NAVY,
                         line_sp=1.12)
            yy += pitch
        mid = x + 5.60 * (w / 11.6)
        self.rect(s, mid, y - 0.02, 0.01, yy - y - 0.12, fill=CARD_LINE)
        self.txt(s, mid - 0.59, y + (yy - y) / 2.0 - 0.28, 1.18, 0.35, "→", size=22, color=BLUE,
                 align=PP_ALIGN.CENTER, wrap=False)
        return yy

    def pillar_row(self, s, x, y, w, items, label=None, name_size=11, body_size=8.5, rule=True):
        """Slide 3 (bottom): a rule, a section label, then N columns of 11pt BLUE name + 8.5pt
        muted body with vertical separators. items: [(name, body)]. Returns the y under it."""
        yy = y
        if rule:
            self.rect(s, x, yy, w, 0.01, fill=CARD_LINE)
            yy += 0.12
        if label:
            self.txt(s, x, yy, w, 0.19, label.upper(), size=8.5, color=MUT, track="40", wrap=False)
            yy += 0.23
        n = max(1, len(items))
        pitch = (w + 0.20) / n
        for i, (name, body) in enumerate(items):
            cx = x + i * pitch
            self.txt(s, cx, yy, pitch - 0.2, 0.21, name, size=name_size, color=BLUE, wrap=False)
            self.txt(s, cx, yy + 0.30, pitch - 0.37, 0.70, body, size=body_size, color=MUT, line_sp=1.12)
            if i:
                self.rect(s, cx - 0.15, yy, 0.01, 0.80, fill=CARD_LINE)
        return yy + 0.95

    def share_bar(self, s, x, y, w, segments, h=0.85, notes=None, note_y=None, val_size=15,
                  lab_size=8.5):
        """Slide 7: one full-width bar split to scale. segments: (value, display, label, weight)
        with weights blue | dark | grey | light | mid. Value 15pt and label 8.5pt sit inside each
        segment (white on blue and dark). notes: [(lead, body, x, w, lead_colour)] drawn under
        the bar with vertical separators. Returns the y under the bar."""
        tot = float(sum(seg[0] for seg in segments)) or 1.0
        sx = x
        for (v, disp, label, weight) in segments:
            sw = w * float(v) / tot
            fill, _, _, tc, _ = self._weight(weight)
            self.rect(s, sx, y, sw, h, fill=fill)
            self.txt(s, sx + 0.12, y + 0.12, max(0.3, sw - 0.12), 0.25, disp, size=val_size, color=tc,
                     wrap=False)
            if label and sw > 0.9:
                self.txt(s, sx + 0.12, y + 0.48, sw - 0.12, 0.21, label, size=lab_size, color=tc,
                         wrap=False)
            sx += sw
        if notes:
            ny = note_y or (y + h + 0.40)
            for i, nt in enumerate(notes):
                lead, body, nx, nw = nt[:4]
                lc = nt[4] if len(nt) > 4 else (BLUE if i == 0 else NAVY)
                self.txt(s, nx, ny, nw, 0.22, lead, size=12.5, color=lc, wrap=False)
                self.txt(s, nx, ny + 0.40, nw - 0.25, 0.85, body, size=10, color=MUT, line_sp=1.12)
                if i:
                    self.rect(s, nx - 0.20, ny, 0.01, 1.75, fill=CARD_LINE)
        return y + h

    def step_flow(self, s, x, y, items, card_w=1.72, card_h=2.10, gap=0.26, arrow=True):
        """Slide 14: N step cards with 12pt arrows between them. items: (number, title, body,
        weight) with weights faint | outline | blue | dark. Returns the y under the cards."""
        cx = x
        for i, (num, title, body, weight) in enumerate(items):
            fill, line, dash, tc, sc = self._weight(weight)
            if weight == 'faint':
                line = None
            self.rect(s, cx, y, card_w, card_h, fill=fill, line=line, line_w=0.75, dash=dash)
            self.txt(s, cx + 0.15, y + 0.15, card_w - 0.3, 0.21, str(num), size=9.5,
                     color=(BLUE if tc == NAVY else WHITE), wrap=False)
            self.txt(s, cx + 0.15, y + 0.43, card_w - 0.3, 0.50, title, size=11, color=tc, line_sp=1.05)
            self.txt(s, cx + 0.15, y + 1.00, card_w - 0.34, card_h - 1.10, body, size=8.5,
                     color=(sc if tc == NAVY else WHITE), line_sp=1.1)
            if arrow and i < len(items) - 1:
                self.txt(s, cx + card_w - 0.03, y + 0.80, gap + 0.07, 0.21, "→", size=12, color=MUT,
                         align=PP_ALIGN.CENTER, wrap=False)
            cx += card_w + gap
        return y + card_h

    def compare_rows(self, s, x, y, headers, rows, cell_w=3.44, cell_h=0.73, pitch=0.80,
                     effort_w=2.73, label_w=1.44):
        """Slide 18: moment-by-moment table. headers: four strings (the third renders BLUE).
        rows: (moment, today_cell, with_cell, effort) where a cell is text or (text, sub) and
        effort is (value, caption) or None. Today cell TINT2, with cell TINT, blue arrow between.
        Returns the y under the last row."""
        hx = [x, x + 1.60, x + 5.40, x + 8.88]
        hc = [NAVY, NAVY, BLUE, NAVY]
        for hxx, htxt, col in zip(hx, headers, hc):
            self.txt(s, hxx, y, 3.6, 0.18, htxt.upper(), size=7.9, color=col, track="20", wrap=False)
        yy = y + 0.21
        for (moment, today, with_, effort) in rows:
            self.txt(s, x, yy + 0.13, label_w, 0.65, moment, size=9.4, color=NAVY, line_sp=1.05)
            for (cx, cell, fill) in ((x + 1.46, today, TINT2), (x + 5.25, with_, TINT)):
                self.rect(s, cx, yy, cell_w, cell_h, fill=fill)
                t, sub = (cell if isinstance(cell, (list, tuple)) else (cell, None))[:2]
                self.txt(s, cx + 0.14, yy + 0.09, cell_w - 0.20, 0.45, t, size=9, color=NAVY, line_sp=1.05)
                if sub:
                    self.txt(s, cx + 0.14, yy + cell_h - 0.19, cell_w - 0.14, 0.18, sub, size=7.9,
                             color=NAVY, wrap=False)
            self.txt(s, x + 4.85, yy, 0.44, cell_h, "→", size=12, color=BLUE, align=PP_ALIGN.CENTER,
                     anchor=MSO_ANCHOR.MIDDLE, wrap=False)
            if effort:
                v, cap = effort
                self.txt(s, x + 8.88, yy + 0.21, effort_w, 0.27, v, size=15, color=BLUE, wrap=False)
                self.txt(s, x + 8.88, yy + 0.46, effort_w, 0.33, cap, size=8.6, color=NAVY, line_sp=1.05)
            yy += pitch
        return yy

    def stacked_hbars(self, s, x, y, w, rows, pitch=0.50, label_w=3.20, scale=None, fills=None):
        """Slide 34: per row, a faint reference track ("do nothing") over a stacked bar
        (NAVY / BLUE / BLUE3 segments), labels after each bar. rows: (code, name, ref_value,
        [segment values], ref_display, bar_display). scale = inches per unit (auto: the widest
        reference track takes the width less 2.0 for its label). Returns the y under the rows."""
        bx = x + label_w
        vmax = max(float(r[2]) for r in rows) or 1.0
        scale = scale or (w - label_w - 2.0) / vmax
        fills = fills or [NAVY, BLUE, BLUE3, BLUE4]
        yy = y
        for (code, name, ref_v, segs, ref_disp, bar_disp) in rows:
            self.txt(s, x, yy, label_w, 0.21, [[(code + " · ", 9.5, BLUE, False), (name, 9.5, NAVY, False)]],
                     wrap=False)
            rw = float(ref_v) * scale
            self.rect(s, bx, yy - 0.10, rw, 0.20, fill=TINT2, line=CARD_LINE, line_w=0.75)
            self.txt(s, bx + rw + 0.10, yy - 0.12, 2.2, 0.21, ref_disp, size=8.5, color=MUT, wrap=False)
            sx = bx
            for k, v in enumerate(segs):
                sw = float(v) * scale
                self.rect(s, sx, yy + 0.14, sw, 0.20, fill=fills[k % len(fills)])
                sx += sw
            self.txt(s, sx + 0.10, yy + 0.12, 2.2, 0.21, bar_disp, size=8.5, color=NAVY, wrap=False)
            yy += pitch
        return yy

    def wave_track(self, s, x, y, w, waves, pitch=2.88, progress=None, marker=None, col_w=2.98,
                   gate_h=1.00):
        """Slide 40: a track with square nodes and one column per wave. waves: dicts {tag, name,
        date, body, gate, node, dark} with node in done | live | next | future and gate = text or
        (lead, text). progress = fraction of the track drawn BLUE. marker = (index, label) above
        a node. Returns the y under the gate cards."""
        self.rect(s, x, y + 0.12, w, 0.02, fill=HAIR)
        if progress:
            self.rect(s, x, y + 0.12, w * float(progress), 0.02, fill=BLUE)
        node_style = {'done': (GREY, None), 'live': (BLUE, None), 'next': (BLUE3, None),
                      'future': (WHITE, BLUE3)}
        for i, wv in enumerate(waves):
            nx = x + i * pitch
            fill, line = node_style[wv.get('node', 'next')]
            self.rect(s, nx, y, 0.25, 0.25, fill=fill, line=line, line_w=0.75,
                      dash=('dash' if line is not None else None))
            if marker and marker[0] == i:
                self.txt(s, nx + 0.35, y - 0.23, 2.6, 0.17, marker[1].upper(), size=7.5, color=BLUE,
                         track="20", wrap=False)
            self.txt(s, nx, y + 0.40, col_w, 0.19, wv['tag'].upper(), size=8.25, color=BLUE, track="20",
                     wrap=False)
            self.txt(s, nx, y + 0.55, col_w, 0.29, wv['name'], size=15, color=NAVY, wrap=False)
            if wv.get('date'):
                self.txt(s, nx, y + 0.82, col_w, 0.19, wv['date'], size=8.25, color=NAVY, wrap=False)
            self.txt(s, nx, y + 1.07, col_w - 0.18, 1.29, wv['body'], size=8.6, color=NAVY, line_sp=1.12)
            if wv.get('gate'):
                gy = y + 2.42
                dark = bool(wv.get('dark'))
                gh = gate_h + (0.05 if dark else 0.0)
                self.rect(s, nx, gy, 2.71, gh, fill=(NAVY if dark else TINT2))
                g = wv['gate']
                lead, text = (g if isinstance(g, (list, tuple)) else ("Gate you own", g))[:2]
                self.txt(s, nx + 0.15, gy + 0.13, 2.4, 0.17, lead.upper(), size=7.5,
                         color=(CYAN if dark else BLUE), track="20", wrap=False)
                self.txt(s, nx + 0.15, gy + 0.30, 2.35, gh - 0.38, text, size=8.25,
                         color=(WHITE if dark else NAVY), line_sp=1.1)
        return y + 2.42 + gate_h + 0.05

    def option_card(self, s, x, y, w, h, tag, name, body, stats, bars=None, note=None, kind='faint',
                    badge=None):
        """Slide 44: an option card. kind: dark (recommended; CYAN badge), faint (TINT2 +
        LINE_SOFT border), dashed (comparison only; outlined badge). stats: [(label, value)],
        two across at 19.5pt. bars: (lead, [(fraction, label, fill)]) thin 0.15 bars. note: text
        or runs [[(text, size, colour, bold)]] pinned to the card's bottom."""
        if kind == 'dark':
            fill, line, dash, tc, lc = NAVY, None, None, WHITE, CYAN
        elif kind == 'dashed':
            fill, line, dash, tc, lc = WHITE, DASHC, 'dash', NAVY, NAVY
        else:
            fill, line, dash, tc, lc = TINT2, LINE_SOFT, None, NAVY, BLUE
        self.rect(s, x, y, w, h, fill=fill, line=line, line_w=0.75, dash=dash)
        ix = x + 0.23
        self.txt(s, ix, y + 0.25, 2.2, 0.19, tag.upper(), size=8.25, color=lc, track="20", wrap=False)
        if badge:
            bw = 0.30 + len(badge) * 0.062
            bx = x + w - 0.24 - bw
            if kind == 'dark':
                self.rect(s, bx, y + 0.23, bw, 0.20, fill=CYAN)
                self.txt(s, bx, y + 0.245, bw, 0.18, badge, size=7.9, color=NAVY,
                         align=PP_ALIGN.CENTER, wrap=False)
            else:
                self.rect(s, bx, y + 0.24, bw, 0.22, line=DASHC, line_w=0.75)
                self.txt(s, bx, y + 0.265, bw, 0.18, badge, size=7.9, color=NAVY,
                         align=PP_ALIGN.CENTER, wrap=False)
        self.txt(s, ix, y + 0.57, w - 0.40, 0.32, name, size=16.5, color=tc, wrap=False)
        self.txt(s, ix, y + 0.99, w - 0.60, 0.50, body, size=9, color=tc, line_sp=1.1)
        sx = ix
        for (lab, val) in list(stats)[:2]:
            self.mini_stat(s, sx, y + 1.55, 1.70, lab, val, dark=(kind == 'dark'), label_size=7.9,
                           value_size=19.5)
            sx += 1.65
        self.rect(s, ix, y + 2.16, w - 0.46, 0.01, fill=(WHITE if kind == 'dark' else HAIR))
        if bars:
            lead, items = bars
            self.txt(s, ix, y + 2.29, w - 0.40, 0.18, lead.upper(), size=7.9, color=tc, track="20",
                     wrap=False)
            by = y + 2.50
            for (frac, label, col) in items:
                bw_ = (w - 1.25) * float(frac)
                self.rect(s, ix, by, bw_, 0.15, fill=col)
                self.txt(s, ix + bw_ + 0.10, by - 0.03, 1.3, 0.21, label, size=9.75, color=tc, wrap=False)
                by += 0.23
        if note:
            if isinstance(note, str):
                note = [[(note, 9.4, tc, False)]]
            self.txt(s, ix, y + h - 0.60, w - 0.50, 0.50, note, line_sp=1.1)
        return y + h

    def numbered_card(self, s, x, y, w, h, n, title, body, tag=None, kind='faint'):
        """Slide 48: a question card. 25.5pt BLUE number top left, outlined page chip top right
        (tag), 10.5pt title, 8.6pt body. kind: faint | dashed | dark (dark = the "how to read"
        card: uppercase CYAN label in `title`, white body, no number)."""
        if kind == 'dark':
            self.rect(s, x, y, w, h, fill=NAVY)
            self.txt(s, x + 0.17, y + 1.09, w - 0.3, 0.18, str(title).upper(), size=7.9, color=CYAN,
                     track="20", wrap=False)
            self.txt(s, x + 0.17, y + 1.31, w - 0.42, h - 1.45, body, size=9, color=WHITE, line_sp=1.15)
            return y + h
        if kind == 'dashed':
            self.rect(s, x, y, w, h, fill=WHITE, line=DASHC, line_w=0.75, dash='dash')
            chip_line, chip_tc = DASHC, NAVY
        else:
            self.rect(s, x, y, w, h, fill=TINT2, line=LINE_SOFT, line_w=0.75)
            chip_line, chip_tc = BLUE, BLUE
        self.txt(s, x + 0.18, y + 0.18, 0.7, 0.40, str(n), size=25.5, color=BLUE, wrap=False)
        if tag:
            cw = 0.16 + len(tag) * 0.058
            self.rect(s, x + w - 0.16 - cw, y + 0.34, cw, 0.19, line=chip_line, line_w=0.75)
            self.txt(s, x + w - 0.16 - cw, y + 0.365, cw, 0.17, tag, size=7.5, color=chip_tc,
                     align=PP_ALIGN.CENTER, wrap=False)
        tl = self._est_lines(title, w - 0.30, 10.5)
        self.txt(s, x + 0.18, y + 0.61, w - 0.30, 0.22 * tl, title, size=10.5, color=NAVY, line_sp=1.05)
        by = y + 0.88 + 0.18 * (tl - 1)
        self.txt(s, x + 0.18, by, w - 0.28, h - (by - y) - 0.12, body, size=8.6, color=NAVY, line_sp=1.15)
        return y + h

    # ---- the mutual plan
    def timeline_lanes(self, s, x, y, w, nodes, lanes, label_w=1.30, lane_h=(1.28, 1.20),
                       committed=None):
        """Slide 61: nodes on a line with owner lanes under it. nodes: dicts {date, title, texts:
        [one per lane], kind: start | step | future | end, bold}. lanes: [(name, sub)]. The line
        is NAVY 1.2pt up to the `committed` node (default: the last node) and BLUE4 after it.
        Dates 8.5pt MUT uppercase at y, the line at y+0.45, titles at y+0.62; lane rules HAIR_ROW,
        the closing rule CARD_LINE. Returns the y of the closing rule."""
        n = max(1, len(nodes))
        x0 = x + label_w
        cw = (w - label_w) / float(n)
        ly = y + 0.45
        cxs = [x0 + i * cw + 0.09 for i in range(n)]
        cidx = (n - 1) if committed is None else int(committed)
        self.hline(s, cxs[0], ly, cxs[cidx], ly, color=NAVY, wpt=1.2)
        if cidx < n - 1:
            self.hline(s, cxs[cidx], ly, cxs[-1], ly, color=BLUE4, wpt=1.2)
        for i, nd in enumerate(nodes):
            cx = x0 + i * cw
            self.txt(s, cx, y, cw - 0.10, 0.14, nd['date'].upper(), size=8.5, color=MUT, track="20",
                     wrap=False)
            kind = nd.get('kind', 'step')
            r = 0.11 if kind in ('start', 'end') else 0.08
            fill = NAVY if kind == 'start' else (BLUE4 if kind == 'future' else BLUE)
            self.oval(s, cxs[i] - r, ly - r, 2 * r, 2 * r, fill)
            self.txt(s, cx, ly + 0.17, cw - 0.12, 0.40, nd['title'], size=9.5, color=NAVY,
                     bold=bool(nd.get('bold')), line_sp=1.05)
        heights = list(lane_h) if isinstance(lane_h, (list, tuple)) else [lane_h] * len(lanes)
        while len(heights) < len(lanes):
            heights.append(heights[-1])
        yy = ly + 0.63
        for j, lane in enumerate(lanes):
            name, sub = (list(lane) + [None])[:2]
            lh = heights[j]
            self.hline(s, x, yy, x + w, yy, color=HAIR_ROW)
            self.txt(s, x, yy + 0.12, label_w - 0.1, 0.17, name, size=10, color=NAVY, wrap=False)
            if sub:
                self.txt(s, x, yy + 0.37, label_w - 0.1, 0.13, sub, size=7.5, color=MUT, wrap=False)
            for i, nd in enumerate(nodes):
                texts = nd.get('texts') or []
                if j < len(texts) and texts[j]:
                    self.txt(s, x0 + i * cw, yy + 0.12, cw - 0.14, lh - 0.20, texts[j], size=7.5,
                             color=MUT, line_sp=1.15)
            yy += lh
        self.hline(s, x, yy, x + w, yy, color=CARD_LINE)
        return yy

    def who_signs(self, s, x, y, w, roles, lead="Who signs", desc=None, status="to name today",
                  chip_w=1.50, chip_h=0.64, gap=0.085, label_w=2.10):
        """Slide 61 (bottom): the who-signs row. Lead 9.5pt + 7.5pt muted description at the
        left; one TINT2 rounded chip per role (8pt role, 7pt BLUE status). roles: strings or
        (role, status). Returns the y under the chips."""
        self.txt(s, x, y + 0.02, 2.0, 0.16, lead, size=9.5, color=NAVY, wrap=False)
        if desc:
            self.txt(s, x, y + 0.28, 1.95, 0.60, desc, size=7.5, color=MUT, line_sp=1.12)
        cx = x + label_w
        for r in roles:
            role, st = (r if isinstance(r, (list, tuple)) else (r, status))[:2]
            self.rect(s, cx, y, chip_w, chip_h, fill=TINT2, round_=True)
            self.txt(s, cx + 0.10, y + 0.06, chip_w - 0.20, 0.30, role, size=8, color=NAVY, line_sp=1.05)
            if st:
                self.txt(s, cx + 0.10, y + 0.41, chip_w - 0.20, 0.12, st, size=7, color=BLUE, wrap=False)
            cx += chip_w + gap
        return y + chip_h

    # ------------------------------------------------------------ dark slides
    def dark_bg(self, s):
        self.rect(s, 0, 0, W, H, fill=NAVY)
        self.rect(s, 6.0, -2.2, 9.5, 5.2, fill=RGBColor(0x14, 0x2A, 0x6E))  # glow approximation
        self.rect(s, 8.2, -1.4, 6.2, 3.2, fill=RGBColor(0x1B, 0x38, 0x94))
        return s

    def divider(self, number, title, subtitle=None):
        """T14 chapter divider: dark, big light-weight number + title."""
        s = self.slide(dark=True)
        self.step_glyph(s, 0.406, 0.406, 0.167, 0.166, CYAN)
        self.rect(s, 0.57, 0.57, 12.19, 0.013, fill=RGBColor(0x2E, 0x3A, 0x52))
        self.txt(s, 1.0, 2.55, 3.0, 1.6, str(number), size=96, color=RGBColor(0x3A, 0x4A, 0x6B), bold=False)
        self.txt(s, 1.0, 4.15, 10.8, 0.9, title, size=34, color=WHITE, bold=True, line_sp=1.05)
        if subtitle:
            self.txt(s, 1.0, 4.95, 9.5, 0.7, subtitle, size=14, color=SUB_D, line_sp=1.25)
        self.rect(s, 0.57, 6.95, 12.19, 0.013, fill=RGBColor(0x2E, 0x3A, 0x52))
        self.txt(s, 11.7, 7.05, 1.06, 0.3, "Backbase", size=11, color=WHITE, bold=True, align=PP_ALIGN.RIGHT)
        return s

    # ------------------------------------------------------------ save
    def _strip_theme_styles(self):
        """Mandatory save pass: remove <p:style> from every shape and guarantee an
        explicit empty <a:effectLst> — otherwise LibreOffice/Google Slides re-apply
        theme drop-shadows (found the hard way on the BACB close deck)."""
        for slide_ in self.prs.slides:
            for shp in slide_.shapes:
                el = shp._element
                for st in el.findall(qn('p:style')):
                    el.remove(st)
                spPr = getattr(el, 'spPr', None)
                if spPr is not None and not spPr.findall(qn('a:effectLst')):
                    spPr.append(spPr.makeelement(qn('a:effectLst'), {}))

    def save(self, path):
        self._strip_theme_styles()
        self.prs.save(path)
        return path

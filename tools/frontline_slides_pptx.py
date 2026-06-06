#!/usr/bin/env python3
"""
BackbaseSlidesPresenter — PPTX builder for the Frontline 2026 Slide Engine.

Renders the same 17 layout types as engine.js to Google Slides-compatible PPTX.
Uses the same data schema (layout name + properties) so HTML and PPTX skills
produce visually consistent output from identical input.

Tokens align to Master Template theme1.xml — see knowledge/design-system/frontline-tokens.json.

Usage:
    from tools.frontline_slides_pptx import BackbaseSlidesPresenter

    deck = BackbaseSlidesPresenter('Deck Title')
    deck.add_cover_color_block('BACKBASE', 'Title\\nLine 2', 'April 2026')
    deck.add_content_standard('light', 'TOPIC', 'Title', 'Subtitle', '<ul><li>Point</li></ul>')
    deck.add_thank_you()
    deck.save('output.pptx')
"""

import re
import io
from pathlib import Path
from html.parser import HTMLParser
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.enum.shapes import MSO_SHAPE


class _HTMLToText(HTMLParser):
    """Minimal HTML-to-text converter for body fields."""
    def __init__(self):
        super().__init__()
        self._lines = []
        self._current = ''
        self._in_li = False

    def handle_starttag(self, tag, attrs):
        if tag == 'li':
            self._in_li = True
            self._current = '\u2192 '
        elif tag == 'br':
            self._lines.append(self._current)
            self._current = ''
        elif tag in ('p', 'div'):
            if self._current:
                self._lines.append(self._current)
                self._current = ''

    def handle_endtag(self, tag):
        if tag == 'li':
            self._lines.append(self._current)
            self._current = ''
            self._in_li = False
        elif tag in ('p', 'div', 'ul', 'ol'):
            if self._current:
                self._lines.append(self._current)
                self._current = ''

    def handle_data(self, data):
        self._current += data.strip()

    def get_text(self):
        if self._current:
            self._lines.append(self._current)
        return '\n'.join(l for l in self._lines if l)


def html_to_text(html_str):
    """Convert simple HTML body content to plain text with arrow bullets."""
    if not html_str:
        return ''
    parser = _HTMLToText()
    parser.feed(html_str)
    return parser.get_text()


def strip_html_tags(text):
    """Remove HTML tags, keeping text. Converts <span class="hl">X</span> to X."""
    if not text:
        return ''
    return re.sub(r'<[^>]+>', '', text)


class BackbaseSlidesPresenter:
    """PPTX builder matching the Backbase Slide Template Engine's 17 layouts."""

    # ── Dimensions (Google Slides widescreen) ─────────────
    SLIDE_W = Inches(13.333)
    SLIDE_H = Inches(7.5)

    # ── Colors (matching engine.js design tokens) ─────────
    NAVY       = RGBColor(0x04, 0x13, 0x26)
    NAVY_DARK  = RGBColor(0x04, 0x13, 0x26)
    BLUE       = RGBColor(0x33, 0x67, 0xFF)
    CYAN       = RGBColor(0x69, 0xFE, 0xFF)
    RED        = RGBColor(0xFF, 0x50, 0x3C)
    LIGHT_BLUE = RGBColor(0xE5, 0xEB, 0xFF)
    OFF_WHITE  = RGBColor(0xF3, 0xF6, 0xF9)
    WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
    BLACK      = RGBColor(0x00, 0x00, 0x00)

    # Text colors
    TEXT_DARK    = RGBColor(0x04, 0x13, 0x26)
    TEXT_MUTED   = RGBColor(0x64, 0x74, 0x8B)
    TEXT_MUTED_W = RGBColor(0x99, 0x99, 0xAA)  # white bg muted
    TEXT_WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
    LABEL_DARK   = RGBColor(0x04, 0x13, 0x26)
    LABEL_WHITE  = RGBColor(0xCC, 0xCC, 0xDD)

    # Grid line colors (very subtle — matches HTML rgba opacity)
    GRID_LIGHT = RGBColor(0xE0, 0xE3, 0xE8)  # light slides: barely visible
    GRID_DARK  = RGBColor(0x1A, 0x2D, 0x45)  # dark slides: very subtle against navy

    # Bar colors for roadmap
    BAR_COLORS = {
        'blue': RGBColor(0x33, 0x67, 0xFF),
        'navy': RGBColor(0x04, 0x13, 0x26),
        'cyan': RGBColor(0x2B, 0xBC, 0xC4),
        'red':  RGBColor(0xFF, 0x50, 0x3C),
    }

    # Statement band backgrounds
    BAND_BLUE = RGBColor(0xE5, 0xEB, 0xFF)
    BAND_RED  = RGBColor(0xFF, 0xEF, 0xEC)

    # ── Typography ────────────────────────────────────────
    FONT = 'Libre Franklin'

    # ── Layout constants (percentages → inches at 13.333 × 7.5) ──
    # Content area margins
    ML = Inches(0.77)   # ~5.8% of 13.333
    MR = Inches(0.39)   # ~2.9% of 13.333
    CW = Inches(11.73)  # ~88% content width

    def __init__(self, title='Backbase Presentation'):
        self.title = title
        self.prs = Presentation()
        self.prs.slide_width = self.SLIDE_W
        self.prs.slide_height = self.SLIDE_H
        self.blank_layout = self.prs.slide_layouts[6]
        self._slide_num = 0

    # ══════════════════════════════════════════════════════
    #  INTERNAL HELPERS
    # ══════════════════════════════════════════════════════

    def _new_slide(self, bg_color=None):
        """Add a blank slide with specified background color."""
        self._slide_num += 1
        slide = self.prs.slides.add_slide(self.blank_layout)
        for ph in list(slide.placeholders):
            sp = ph._element
            sp.getparent().remove(sp)
        bg = slide.background.fill
        bg.solid()
        bg.fore_color.rgb = bg_color or self.WHITE
        return slide

    def _txt(self, slide, text, left, top, width, height, size=Pt(12),
             color=None, bold=False, align=PP_ALIGN.LEFT, name=None):
        """Add a textbox with auto_size disabled (Google Slides rule)."""
        tb = slide.shapes.add_textbox(left, top, width, height)
        tf = tb.text_frame
        tf.word_wrap = True
        tf.auto_size = MSO_AUTO_SIZE.NONE
        p = tf.paragraphs[0]
        p.text = str(text)
        p.font.size = size
        p.font.bold = bold
        p.font.color.rgb = color or self.TEXT_DARK
        p.font.name = name or self.FONT
        p.alignment = align
        tb.name = f"txt_{self._slide_num}_{left}"
        return tf

    def _multi_line_txt(self, slide, lines, left, top, width, height,
                        size=Pt(12), color=None, bold=False, align=PP_ALIGN.LEFT,
                        spacing=Pt(4)):
        """Multi-line textbox from a list of strings."""
        tb = slide.shapes.add_textbox(left, top, width, height)
        tf = tb.text_frame
        tf.word_wrap = True
        tf.auto_size = MSO_AUTO_SIZE.NONE
        for i, line in enumerate(lines):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.text = str(line)
            p.font.size = size
            p.font.bold = bold
            p.font.color.rgb = color or self.TEXT_DARK
            p.font.name = self.FONT
            p.alignment = align
            p.space_after = spacing
        return tf

    def _label(self, slide, text, left, top, dark=False):
        """Uppercase section label."""
        color = self.LABEL_WHITE if dark else self.LABEL_DARK
        self._txt(slide, text.upper(), left, top,
                  Inches(4), Pt(20), size=Pt(9),
                  color=color, bold=False)

    def _title(self, slide, text, left, top, width=None, size=Pt(28),
               dark=False):
        """Main title text, supports \\n line breaks."""
        color = self.TEXT_WHITE if dark else self.TEXT_DARK
        lines = text.split('\n') if text else ['']
        w = width or self.CW
        self._multi_line_txt(slide, lines, left, top, w, Inches(1.2),
                             size=size, color=color, bold=False)

    def _subtitle_text(self, slide, text, left, top, width=None, dark=False):
        """Subtitle text."""
        color = self.TEXT_MUTED_W if dark else self.BLUE
        w = width or Inches(9.3)
        self._txt(slide, text, left, top, w, Inches(0.6),
                  size=Pt(14), color=color)

    def _body_text(self, slide, html_body, left, top, width=None, dark=False):
        """Body text from HTML content — converts to plain text for PPTX."""
        text = html_to_text(html_body)
        if not text:
            return
        color = self.TEXT_WHITE if dark else self.TEXT_DARK
        w = width or self.CW
        lines = text.split('\n')
        self._multi_line_txt(slide, lines, left, top, w, Inches(3.5),
                             size=Pt(11), color=color, spacing=Pt(6))

    def _footer(self, slide, dark=False):
        """Backbase wordmark + slide number at bottom-right."""
        text_color = self.TEXT_MUTED_W if dark else self.TEXT_MUTED
        # "Backbase  |  N"
        tb = slide.shapes.add_textbox(
            self.SLIDE_W - Inches(2.0), self.SLIDE_H - Inches(0.4),
            Inches(1.7), Inches(0.3)
        )
        tf = tb.text_frame
        tf.word_wrap = False
        tf.auto_size = MSO_AUTO_SIZE.NONE
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.RIGHT
        r1 = p.add_run()
        r1.text = 'Backbase'
        r1.font.size = Pt(9)
        r1.font.color.rgb = text_color
        r1.font.name = self.FONT
        r2 = p.add_run()
        r2.text = '   |   '
        r2.font.size = Pt(9)
        r2.font.color.rgb = self.GRID_LIGHT if not dark else self.GRID_DARK
        r2.font.name = self.FONT
        r3 = p.add_run()
        r3.text = str(self._slide_num)
        r3.font.size = Pt(9)
        r3.font.color.rgb = text_color
        r3.font.name = self.FONT
        tb.name = f"footer_{self._slide_num}"

    def _grid_line_v(self, slide, x_pct, dark=False, top_pct=0, bottom_pct=100):
        """Vertical grid line at x% of slide width. Hairline (1px equivalent)."""
        color = self.GRID_DARK if dark else self.GRID_LIGHT
        left = Emu(int(self.SLIDE_W.emu * x_pct / 100))
        top = Emu(int(self.SLIDE_H.emu * top_pct / 100))
        h = Emu(int(self.SLIDE_H.emu * (bottom_pct - top_pct) / 100))
        # Use a line shape for true hairline width
        s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, Emu(6350), h)
        s.fill.solid()
        s.fill.fore_color.rgb = color
        s.line.fill.background()
        s.name = f"grid_v_{x_pct}"

    def _grid_line_h(self, slide, y_pct, dark=False, left_pct=0, right_pct=100):
        """Horizontal grid line at y% of slide height. Hairline (1px equivalent)."""
        color = self.GRID_DARK if dark else self.GRID_LIGHT
        left = Emu(int(self.SLIDE_W.emu * left_pct / 100))
        top = Emu(int(self.SLIDE_H.emu * y_pct / 100))
        w = Emu(int(self.SLIDE_W.emu * (right_pct - left_pct) / 100))
        s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, w, Emu(6350))
        s.fill.solid()
        s.fill.fore_color.rgb = color
        s.line.fill.background()
        s.name = f"grid_h_{y_pct}"

    def _motif(self, slide, left, top, color=None):
        """Small Backbase motif shape — tiny accent square at grid intersections."""
        c = color or self.BLUE
        size = Inches(0.10)  # very small — just a subtle accent mark
        s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                    left - size, top - size, size, size)
        s.fill.solid()
        s.fill.fore_color.rgb = c
        s.line.fill.background()
        s.name = f"motif_{self._slide_num}"

    def _band_shape(self, slide, color):
        """Colored band across the middle of the slide (for statement layouts).
        The HTML uses a clip-path polygon (step shape). In PPTX we approximate
        with two overlapping rectangles to create the stepped look."""
        left = Emu(int(self.SLIDE_W.emu * 2.9 / 100))
        width = Emu(int(self.SLIDE_W.emu * 94.2 / 100))
        # Upper band: from 25.13% to 65.9% height, right portion (32.7% to 97.1% x)
        upper_left = Emu(int(self.SLIDE_W.emu * 2.9 / 100))
        upper_top = Emu(int(self.SLIDE_H.emu * 25.13 / 100))
        upper_h = Emu(int(self.SLIDE_H.emu * (65.9 - 25.13) / 100))
        s1 = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                     upper_left, upper_top, width, upper_h)
        s1.fill.solid()
        s1.fill.fore_color.rgb = color
        s1.line.fill.background()
        s1.name = f"band_upper_{self._slide_num}"
        # Lower step: from 65.9% to 73% height, left portion (2.9% to 58% x)
        lower_left = Emu(int(self.SLIDE_W.emu * 2.9 / 100))
        lower_top = Emu(int(self.SLIDE_H.emu * 65.9 / 100))
        lower_w = Emu(int(self.SLIDE_W.emu * (58 - 2.9) / 100))
        lower_h = Emu(int(self.SLIDE_H.emu * (73 - 65.9) / 100))
        s2 = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                     lower_left, lower_top, lower_w, lower_h)
        s2.fill.solid()
        s2.fill.fore_color.rgb = color
        s2.line.fill.background()
        s2.name = f"band_lower_{self._slide_num}"

    # ══════════════════════════════════════════════════════
    #  17 LAYOUT METHODS
    # ══════════════════════════════════════════════════════

    def add_cover_color_block(self, label='BACKBASE', title='Title',
                               date='', partner=False):
        """Layout 1: Navy background with blue accent. Opening slide."""
        slide = self._new_slide(self.NAVY)
        # Subtle blue accent oval in bottom-right (simulates CSS radial-gradient)
        accent = slide.shapes.add_shape(
            MSO_SHAPE.OVAL,
            Emu(int(self.SLIDE_W.emu * 0.55)),
            Emu(int(self.SLIDE_H.emu * 0.60)),
            Emu(int(self.SLIDE_W.emu * 0.50)),
            Emu(int(self.SLIDE_H.emu * 0.50))
        )
        accent.fill.solid()
        accent.fill.fore_color.rgb = RGBColor(0x0D, 0x21, 0x3F)  # very subtle blue tint
        accent.line.fill.background()
        accent.name = "cover_glow"
        # Grid lines
        self._grid_line_v(slide, 4.13, dark=True)
        self._grid_line_v(slide, 54.1, dark=True)
        self._grid_line_v(slide, 95.86, dark=True)
        self._grid_line_h(slide, 21.54, dark=True)
        self._grid_line_h(slide, 64.86, dark=True)
        self._grid_line_h(slide, 92.65, dark=True)
        # Motif
        self._motif(slide, Emu(int(self.SLIDE_W.emu * 0.541)),
                    Emu(int(self.SLIDE_H.emu * 0.2154)), self.WHITE)
        # Logo text (bold, white, smaller — wordmark style)
        self._txt(slide, 'Backbase', Inches(1.07), Inches(0.53),
                  Inches(2), Inches(0.4), size=Pt(13),
                  color=self.TEXT_WHITE, bold=True)
        # Label
        if label:
            self._label(slide, label, Inches(1.07), Inches(1.91), dark=True)
        # Title (large, light weight feel)
        self._title(slide, title, Inches(1.07), Inches(2.4),
                    width=Inches(6.4), size=Pt(48), dark=True)
        # Date
        if date:
            self._txt(slide, date, Inches(1.07), Inches(5.25),
                      Inches(4), Inches(0.4), size=Pt(14),
                      color=self.TEXT_MUTED_W)

    def add_cover_photo(self, label='', title='', date='',
                        image_path=None, partner=None):
        """Layout 2: Cover with optional photo or navy variant."""
        if image_path:
            # Photo variant — white panel overlay
            slide = self._new_slide(self.NAVY)
            try:
                slide.shapes.add_picture(image_path, 0, 0,
                                          self.SLIDE_W, self.SLIDE_H)
            except Exception:
                pass
            # White panel (left half)
            left = Emu(int(self.SLIDE_W.emu * 0.0413))
            top = Emu(int(self.SLIDE_H.emu * 0.2154))
            w = Emu(int(self.SLIDE_W.emu * 0.50))
            h = Emu(int(self.SLIDE_H.emu * 0.72))
            panel = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, w, h)
            panel.fill.solid()
            panel.fill.fore_color.rgb = self.WHITE
            panel.fill.fore_color.brightness = -0.0
            panel.line.fill.background()
            panel.name = "cover_panel"
            # Content on panel
            if label:
                self._label(slide, label, Inches(1.07), Inches(1.91))
            self._title(slide, title, Inches(1.07), Inches(2.4),
                        width=Inches(6.4), size=Pt(42))
            if date:
                self._txt(slide, date, Inches(1.07), Inches(5.25),
                          Inches(4), Inches(0.4), size=Pt(14),
                          color=self.TEXT_MUTED)
        else:
            # Navy variant (no photo)
            slide = self._new_slide(self.NAVY_DARK)
            self._grid_line_v(slide, 4.13, dark=True)
            self._grid_line_v(slide, 54.1, dark=True)
            self._grid_line_v(slide, 95.86, dark=True)
            self._grid_line_h(slide, 21.54, dark=True)
            self._grid_line_h(slide, 64.86, dark=True)
            # Logo
            self._txt(slide, 'Backbase', Inches(1.07), Inches(0.53),
                      Inches(2), Inches(0.4), size=Pt(14),
                      color=self.TEXT_WHITE, bold=True)
            if label:
                self._label(slide, label, Inches(1.07), Inches(1.91), dark=True)
            self._title(slide, title, Inches(1.07), Inches(2.4),
                        width=Inches(6.4), size=Pt(42), dark=True)
            if date:
                self._txt(slide, date, Inches(1.07), Inches(5.25),
                          Inches(4), Inches(0.4), size=Pt(14),
                          color=self.TEXT_MUTED_W)

    def add_chapter_numbered(self, theme='navy', number='01', label='',
                              title='', subtitle=''):
        """Layout 3: Large number left, title right. Section divider."""
        dark = True
        bg = self.NAVY_DARK if theme == 'navy' else self.BLUE
        slide = self._new_slide(bg)
        # Subtle blue accent for navy theme
        if theme == 'navy':
            accent = slide.shapes.add_shape(
                MSO_SHAPE.OVAL,
                Emu(int(self.SLIDE_W.emu * 0.55)),
                Emu(int(self.SLIDE_H.emu * 0.60)),
                Emu(int(self.SLIDE_W.emu * 0.50)),
                Emu(int(self.SLIDE_H.emu * 0.50))
            )
            accent.fill.solid()
            accent.fill.fore_color.rgb = RGBColor(0x08, 0x1A, 0x30)
            accent.line.fill.background()
            accent.name = "chapter_glow"
        # Grid
        self._grid_line_v(slide, 4.13, dark=True)
        self._grid_line_v(slide, 27, dark=True, top_pct=21.54, bottom_pct=64.86)
        self._grid_line_v(slide, 95.86, dark=True)
        self._grid_line_h(slide, 21.54, dark=True)
        self._grid_line_h(slide, 64.86, dark=True)
        # Motif
        mc = self.WHITE if theme == 'blue' else self.BLUE
        self._motif(slide, Emu(int(self.SLIDE_W.emu * 0.0413)),
                    Emu(int(self.SLIDE_H.emu * 0.2154)), mc)
        # Number
        num_color = self.WHITE if theme == 'blue' else self.BLUE
        self._txt(slide, number, Emu(int(self.SLIDE_W.emu * 0.0413)),
                  Emu(int(self.SLIDE_H.emu * 0.115)),
                  Emu(int(self.SLIDE_W.emu * 0.2287)),
                  Emu(int(self.SLIDE_H.emu * 0.5336)),
                  size=Pt(84), color=num_color, align=PP_ALIGN.CENTER)
        # Label
        if label:
            self._label(slide, label, Emu(int(self.SLIDE_W.emu * 0.29)),
                        Emu(int(self.SLIDE_H.emu * 0.25)), dark=True)
        # Title
        self._title(slide, title, Emu(int(self.SLIDE_W.emu * 0.29)),
                    Emu(int(self.SLIDE_H.emu * 0.32)),
                    width=Emu(int(self.SLIDE_W.emu * 0.62)),
                    size=Pt(34), dark=True)
        # Subtitle
        if subtitle:
            self._txt(slide, subtitle, Emu(int(self.SLIDE_W.emu * 0.29)),
                      Emu(int(self.SLIDE_H.emu * 0.55)),
                      Emu(int(self.SLIDE_W.emu * 0.60)),
                      Inches(1), size=Pt(14), color=self.TEXT_MUTED_W)

    def add_chapter_standard(self, theme='navy', label='', title='',
                              subtitle=''):
        """Layout 4: Full-width title section divider."""
        bg = self.NAVY_DARK if theme == 'navy' else self.BLUE
        slide = self._new_slide(bg)
        self._grid_line_v(slide, 4.13, dark=True)
        self._grid_line_v(slide, 95.86, dark=True)
        self._grid_line_h(slide, 21.54, dark=True)
        self._grid_line_h(slide, 64.86, dark=True)
        mc = self.WHITE if theme == 'blue' else self.BLUE
        self._motif(slide, Emu(int(self.SLIDE_W.emu * 0.0413)),
                    Emu(int(self.SLIDE_H.emu * 0.2154)), mc)
        if label:
            self._label(slide, label, self.ML, Emu(int(self.SLIDE_H.emu * 0.25)),
                        dark=True)
        self._title(slide, title, self.ML, Emu(int(self.SLIDE_H.emu * 0.32)),
                    width=Emu(int(self.SLIDE_W.emu * 0.85)), size=Pt(34), dark=True)
        if subtitle:
            self._txt(slide, subtitle, self.ML, Emu(int(self.SLIDE_H.emu * 0.55)),
                      Emu(int(self.SLIDE_W.emu * 0.60)), Inches(1),
                      size=Pt(14), color=self.TEXT_MUTED_W)

    def add_toc(self, label='AGENDA', title='Contents', items=None,
                numbered=True):
        """Layout 5: Table of contents with numbered/plain rows."""
        items = items or []
        slide = self._new_slide(self.WHITE)
        self._grid_line_v(slide, 2.9)
        self._grid_line_v(slide, 40)
        self._grid_line_v(slide, 97.1)
        self._grid_line_h(slide, 5.15)
        self._grid_line_h(slide, 94.85)
        self._motif(slide, Emu(int(self.SLIDE_W.emu * 0.029)),
                    Emu(int(self.SLIDE_H.emu * 0.0515)))
        if label:
            self._label(slide, label, self.ML, Emu(int(self.SLIDE_H.emu * 0.10)))
        if title:
            self._title(slide, title, self.ML, Emu(int(self.SLIDE_H.emu * 0.15)),
                        width=Inches(4))
        # TOC rows on the right side
        row_left = Emu(int(self.SLIDE_W.emu * 0.40))
        row_width = Emu(int(self.SLIDE_W.emu * 0.57))
        row_top_start = Emu(int(self.SLIDE_H.emu * 0.0515))
        row_area_h = Emu(int(self.SLIDE_H.emu * 0.897))
        n = len(items)
        if n == 0:
            self._footer(slide)
            return
        row_h = row_area_h // n
        for idx, item in enumerate(items):
            y = row_top_start + row_h * idx
            # Divider line between rows
            if idx > 0:
                s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                            row_left, y, row_width, Pt(0.5))
                s.fill.solid()
                s.fill.fore_color.rgb = self.GRID_LIGHT
                s.line.fill.background()
            prefix = f"{str(idx + 1).zfill(2)}    " if numbered else ''
            self._txt(slide, f"{prefix}{item}", row_left + Inches(0.2),
                      y + Emu(row_h // 3),
                      row_width - Inches(0.4), Emu(row_h // 2),
                      size=Pt(13), color=self.TEXT_DARK)
        self._footer(slide)

    def add_content_standard(self, theme='light', label='', title='',
                              subtitle='', body=''):
        """Layout 6: General-purpose content slide. Most versatile."""
        dark = theme == 'dark'
        bg = self.NAVY if dark else self.WHITE
        slide = self._new_slide(bg)
        self._grid_line_v(slide, 2.9, dark=dark)
        self._grid_line_v(slide, 97.1, dark=dark)
        self._grid_line_h(slide, 5.15, dark=dark)
        self._grid_line_h(slide, 94.85, dark=dark)
        self._motif(slide, Emu(int(self.SLIDE_W.emu * 0.029)),
                    Emu(int(self.SLIDE_H.emu * 0.0515)))
        if label:
            self._label(slide, label, self.ML,
                        Emu(int(self.SLIDE_H.emu * 0.10)), dark=dark)
        if title:
            self._title(slide, title, self.ML,
                        Emu(int(self.SLIDE_H.emu * 0.15)), dark=dark)
        if subtitle:
            self._subtitle_text(slide, subtitle, self.ML,
                                Emu(int(self.SLIDE_H.emu * 0.24)),
                                dark=dark)
        if body:
            self._body_text(slide, body, self.ML,
                            Emu(int(self.SLIDE_H.emu * 0.32)),
                            dark=dark)
        self._footer(slide, dark=dark)

    def add_content_columns(self, label='', title='', columns=None):
        """Layout 7: 2-5 equal columns below a title."""
        columns = columns or []
        slide = self._new_slide(self.WHITE)
        self._grid_line_v(slide, 2.9)
        self._grid_line_v(slide, 97.1)
        self._grid_line_h(slide, 5.15)
        self._grid_line_h(slide, 27.53)
        self._grid_line_h(slide, 32.42)
        self._grid_line_h(slide, 94.85)
        self._motif(slide, Emu(int(self.SLIDE_W.emu * 0.029)),
                    Emu(int(self.SLIDE_H.emu * 0.0515)))
        if label:
            self._label(slide, label, self.ML, Emu(int(self.SLIDE_H.emu * 0.10)))
        if title:
            self._title(slide, title, self.ML, Emu(int(self.SLIDE_H.emu * 0.15)))
        # Columns area
        n = len(columns)
        if n == 0:
            self._footer(slide)
            return
        col_left_start = Emu(int(self.SLIDE_W.emu * 0.029))
        col_area_w = Emu(int(self.SLIDE_W.emu * 0.942))
        col_top = Emu(int(self.SLIDE_H.emu * 0.3242))
        col_h = Emu(int(self.SLIDE_H.emu * 0.6243))
        col_w = col_area_w // n
        for i, col in enumerate(columns):
            x = col_left_start + col_w * i
            # Column divider
            if i > 0:
                s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                            x, col_top, Pt(0.5), col_h)
                s.fill.solid()
                s.fill.fore_color.rgb = self.GRID_LIGHT
                s.line.fill.background()
            # Column subtitle
            if col.get('subtitle'):
                self._txt(slide, col['subtitle'], x + Inches(0.15),
                          col_top + Inches(0.15),
                          Emu(col_w - Inches(0.3).emu), Inches(0.4),
                          size=Pt(11), color=self.BLUE, bold=True)
            # Column body
            if col.get('body'):
                self._txt(slide, col['body'], x + Inches(0.15),
                          col_top + Inches(0.55),
                          Emu(col_w - Inches(0.3).emu), Emu(col_h - Inches(0.7).emu),
                          size=Pt(9), color=self.TEXT_MUTED)
        self._footer(slide)

    def add_overview_about(self, label='', title='', subtitle='',
                            image_path=None, stats=None):
        """Layout 8: Content left, image right, 5 stats at bottom."""
        stats = stats or []
        slide = self._new_slide(self.WHITE)
        self._grid_line_v(slide, 2.9)
        self._grid_line_v(slide, 59.45)
        self._grid_line_v(slide, 97.1)
        self._grid_line_h(slide, 5.15)
        self._grid_line_h(slide, 74.85)
        self._grid_line_h(slide, 94.85)
        self._motif(slide, Emu(int(self.SLIDE_W.emu * 0.029)),
                    Emu(int(self.SLIDE_H.emu * 0.0515)))
        if label:
            self._label(slide, label, self.ML, Emu(int(self.SLIDE_H.emu * 0.10)))
        if title:
            self._title(slide, title, self.ML, Emu(int(self.SLIDE_H.emu * 0.15)),
                        width=Inches(5.3))
        if subtitle:
            self._txt(slide, subtitle, self.ML, Emu(int(self.SLIDE_H.emu * 0.28)),
                      Inches(5.3), Inches(2.5), size=Pt(11), color=self.TEXT_MUTED)
        # Image area (right)
        img_left = Emu(int(self.SLIDE_W.emu * 0.5945))
        img_top = Emu(int(self.SLIDE_H.emu * 0.0515))
        img_w = Emu(int(self.SLIDE_W.emu * 0.3765))
        img_h = Emu(int(self.SLIDE_H.emu * 0.697))
        if image_path:
            try:
                slide.shapes.add_picture(image_path, img_left, img_top, img_w, img_h)
            except Exception:
                self._placeholder_rect(slide, img_left, img_top, img_w, img_h)
        else:
            self._placeholder_rect(slide, img_left, img_top, img_w, img_h)
        # Stats row at bottom
        self._stats_row(slide, stats, Emu(int(self.SLIDE_W.emu * 0.029)),
                        Emu(int(self.SLIDE_H.emu * 0.7485)),
                        Emu(int(self.SLIDE_W.emu * 0.942)),
                        Emu(int(self.SLIDE_H.emu * 0.20)))
        self._footer(slide)

    def add_overview_stats(self, label='', title='', subtitle='',
                            image_path=None, stats=None):
        """Layout 9: Similar to overview-about with 4 stats."""
        stats = stats or []
        slide = self._new_slide(self.WHITE)
        self._grid_line_v(slide, 2.9)
        self._grid_line_v(slide, 50)
        self._grid_line_v(slide, 97.1)
        self._grid_line_h(slide, 5.15)
        self._grid_line_h(slide, 74.85)
        self._grid_line_h(slide, 94.85)
        self._motif(slide, Emu(int(self.SLIDE_W.emu * 0.029)),
                    Emu(int(self.SLIDE_H.emu * 0.0515)))
        if label:
            self._label(slide, label, self.ML, Emu(int(self.SLIDE_H.emu * 0.10)))
        if title:
            self._title(slide, title, self.ML, Emu(int(self.SLIDE_H.emu * 0.15)),
                        width=Inches(5.0))
        if subtitle:
            self._txt(slide, subtitle, self.ML, Emu(int(self.SLIDE_H.emu * 0.28)),
                      Inches(5.0), Inches(2.5), size=Pt(11), color=self.TEXT_DARK)
        # Image (right half)
        img_left = Emu(int(self.SLIDE_W.emu * 0.50))
        img_top = Emu(int(self.SLIDE_H.emu * 0.0515))
        img_w = Emu(int(self.SLIDE_W.emu * 0.471))
        img_h = Emu(int(self.SLIDE_H.emu * 0.697))
        if image_path:
            try:
                slide.shapes.add_picture(image_path, img_left, img_top, img_w, img_h)
            except Exception:
                self._placeholder_rect(slide, img_left, img_top, img_w, img_h)
        else:
            self._placeholder_rect(slide, img_left, img_top, img_w, img_h)
        # Stats
        self._stats_row(slide, stats, Emu(int(self.SLIDE_W.emu * 0.029)),
                        Emu(int(self.SLIDE_H.emu * 0.7485)),
                        Emu(int(self.SLIDE_W.emu * 0.942)),
                        Emu(int(self.SLIDE_H.emu * 0.20)))
        self._footer(slide)

    def add_product(self, label='', title='', subtitle='', body='',
                     image_path=None, image_bg=True):
        """Layout 10: Title + bullets left, screenshot right."""
        slide = self._new_slide(self.WHITE)
        self._grid_line_v(slide, 2.9)
        self._grid_line_v(slide, 50)
        self._grid_line_v(slide, 97.1)
        self._grid_line_h(slide, 5.15)
        self._grid_line_h(slide, 94.85)
        self._motif(slide, Emu(int(self.SLIDE_W.emu * 0.029)),
                    Emu(int(self.SLIDE_H.emu * 0.0515)))
        if label:
            self._label(slide, label, self.ML, Emu(int(self.SLIDE_H.emu * 0.10)))
        if title:
            self._title(slide, title, self.ML, Emu(int(self.SLIDE_H.emu * 0.15)),
                        width=Inches(5.3))
        if subtitle:
            self._subtitle_text(slide, subtitle, self.ML,
                                Emu(int(self.SLIDE_H.emu * 0.28)),
                                width=Inches(5.3))
        if body:
            self._body_text(slide, body, self.ML,
                            Emu(int(self.SLIDE_H.emu * 0.53)),
                            width=Inches(5.3))
        # Image area (right half)
        img_left = Emu(int(self.SLIDE_W.emu * 0.50))
        img_top = Emu(int(self.SLIDE_H.emu * 0.0515))
        img_w = Emu(int(self.SLIDE_W.emu * 0.471))
        img_h = Emu(int(self.SLIDE_H.emu * 0.897))
        if image_bg:
            bg_rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                              img_left, img_top, img_w, img_h)
            bg_rect.fill.solid()
            bg_rect.fill.fore_color.rgb = self.LIGHT_BLUE
            bg_rect.line.fill.background()
        if image_path:
            try:
                slide.shapes.add_picture(image_path, img_left + Inches(0.2),
                                          img_top + Inches(0.2),
                                          Emu(img_w - Inches(0.4).emu),
                                          Emu(img_h - Inches(0.4).emu))
            except Exception:
                pass
        self._footer(slide)

    def add_statement(self, accent='blue', label='', text='', variant=None):
        """Layout 11: Large text on colored band. Impactful quotes."""
        dark = variant == 'dark'
        bg = self.NAVY if dark else self.WHITE
        slide = self._new_slide(bg)
        self._grid_line_v(slide, 2.9, dark=dark)
        self._grid_line_v(slide, 97.1, dark=dark)
        self._grid_line_h(slide, 5.15, dark=dark)
        self._grid_line_h(slide, 94.85, dark=dark)
        mc = self.WHITE if dark else self.BLUE
        self._motif(slide, Emu(int(self.SLIDE_W.emu * 0.029)),
                    Emu(int(self.SLIDE_H.emu * 0.0515)), mc)
        # Band
        if dark:
            band_color = RGBColor(0x14, 0x2A, 0x45)
        elif accent == 'red':
            band_color = self.BAND_RED
        else:
            band_color = self.BAND_BLUE
        self._band_shape(slide, band_color)
        # Label
        if label:
            self._label(slide, label, self.ML,
                        Emu(int(self.SLIDE_H.emu * 0.2727)), dark=dark)
        # Text (strip HTML tags for PPTX)
        clean_text = strip_html_tags(text)
        text_color = self.TEXT_WHITE if dark else self.TEXT_DARK
        self._txt(slide, clean_text, self.ML,
                  Emu(int(self.SLIDE_H.emu * 0.37)),
                  Emu(int(self.SLIDE_W.emu * 0.88)),
                  Inches(2.5), size=Pt(18), color=text_color)
        self._footer(slide, dark=dark)

    def add_statement_stat(self, accent='blue', label='', stat='70%',
                            text='', source=''):
        """Layout 12: Big number + description on colored band."""
        slide = self._new_slide(self.WHITE)
        self._grid_line_v(slide, 2.9)
        self._grid_line_v(slide, 97.1)
        self._grid_line_h(slide, 5.15)
        self._grid_line_h(slide, 94.85)
        self._motif(slide, Emu(int(self.SLIDE_W.emu * 0.029)),
                    Emu(int(self.SLIDE_H.emu * 0.0515)))
        # Band
        band_color = self.BAND_RED if accent == 'red' else self.BAND_BLUE
        self._band_shape(slide, band_color)
        # Label
        if label:
            self._label(slide, label, self.ML,
                        Emu(int(self.SLIDE_H.emu * 0.2727)))
        # Stat number (large, left)
        stat_color = self.RED if accent == 'red' else self.BLUE
        self._txt(slide, stat, self.ML,
                  Emu(int(self.SLIDE_H.emu * 0.35)),
                  Inches(4), Inches(1.5), size=Pt(60),
                  color=stat_color, bold=True)
        # Description text (right of number)
        clean_text = strip_html_tags(text)
        self._txt(slide, clean_text,
                  Inches(5.5), Emu(int(self.SLIDE_H.emu * 0.38)),
                  Inches(6.5), Inches(1.5), size=Pt(13),
                  color=self.TEXT_DARK)
        # Source
        if source:
            self._txt(slide, f"Source: {source}",
                      Inches(5.5), Emu(int(self.SLIDE_H.emu * 0.55)),
                      Inches(6), Inches(0.3), size=Pt(9),
                      color=self.TEXT_MUTED)
        self._footer(slide)

    def add_testimonial(self, logo='', quote='', name='', role='',
                         image_path=None):
        """Layout 13: Customer photo left, quote right."""
        slide = self._new_slide(self.WHITE)
        self._grid_line_v(slide, 2.9)
        self._grid_line_v(slide, 33)
        self._grid_line_v(slide, 97.1)
        self._grid_line_h(slide, 5.15)
        self._grid_line_h(slide, 94.85)
        self._motif(slide, Emu(int(self.SLIDE_W.emu * 0.029)),
                    Emu(int(self.SLIDE_H.emu * 0.0515)))
        # Image (left)
        img_left = self.ML
        img_top = Emu(int(self.SLIDE_H.emu * 0.20))
        img_w = Emu(int(self.SLIDE_W.emu * 0.21))
        img_h = Emu(int(self.SLIDE_H.emu * 0.48))
        if image_path:
            try:
                slide.shapes.add_picture(image_path, img_left, img_top, img_w, img_h)
            except Exception:
                self._placeholder_rect(slide, img_left, img_top, img_w, img_h)
        else:
            self._placeholder_rect(slide, img_left, img_top, img_w, img_h)
        # Label
        self._label(slide, 'TESTIMONIAL',
                    Emu(int(self.SLIDE_W.emu * 0.33)),
                    Emu(int(self.SLIDE_H.emu * 0.085)))
        # Vertical divider
        div_x = Emu(int(self.SLIDE_W.emu * 0.33))
        s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, div_x,
                                    Emu(int(self.SLIDE_H.emu * 0.12)),
                                    Pt(0.5),
                                    Emu(int(self.SLIDE_H.emu * 0.76)))
        s.fill.solid()
        s.fill.fore_color.rgb = self.GRID_LIGHT
        s.line.fill.background()
        # Content (right of divider)
        content_left = Emu(int(self.SLIDE_W.emu * 0.35))
        content_w = Emu(int(self.SLIDE_W.emu * 0.60))
        # Logo/company name
        if logo:
            self._txt(slide, logo, content_left,
                      Emu(int(self.SLIDE_H.emu * 0.20)),
                      content_w, Inches(0.5), size=Pt(22),
                      color=self.TEXT_DARK, bold=True)
        # Quote
        self._txt(slide, f'"{quote}"', content_left,
                  Emu(int(self.SLIDE_H.emu * 0.32)),
                  content_w, Inches(2.5), size=Pt(13),
                  color=self.TEXT_DARK)
        # Author divider
        author_y = Emu(int(self.SLIDE_H.emu * 0.72))
        s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, content_left, author_y,
                                    content_w, Pt(0.5))
        s.fill.solid()
        s.fill.fore_color.rgb = self.GRID_LIGHT
        s.line.fill.background()
        # Author name
        self._txt(slide, name, content_left,
                  Emu(int(self.SLIDE_H.emu * 0.75)),
                  content_w, Inches(0.3), size=Pt(12), color=self.BLUE)
        # Author role
        self._txt(slide, role, content_left,
                  Emu(int(self.SLIDE_H.emu * 0.80)),
                  content_w, Inches(0.3), size=Pt(10), color=self.TEXT_MUTED)
        self._footer(slide)

    def add_team(self, label='', title='', members=None):
        """Layout 14: Auto-layout grid for team introductions."""
        members = members or []
        slide = self._new_slide(self.WHITE)
        self._grid_line_v(slide, 2.9)
        self._grid_line_v(slide, 97.1)
        self._grid_line_h(slide, 5.15)
        self._grid_line_h(slide, 94.85)
        self._motif(slide, Emu(int(self.SLIDE_W.emu * 0.029)),
                    Emu(int(self.SLIDE_H.emu * 0.0515)))
        if label:
            self._label(slide, label, self.ML, Emu(int(self.SLIDE_H.emu * 0.10)))
        if title:
            self._title(slide, title, self.ML, Emu(int(self.SLIDE_H.emu * 0.15)))
        # Grid area
        n = len(members)
        if n == 0:
            self._footer(slide)
            return
        grid_left = Emu(int(self.SLIDE_W.emu * 0.029))
        grid_top = Emu(int(self.SLIDE_H.emu * 0.3242))
        grid_w = Emu(int(self.SLIDE_W.emu * 0.942))
        grid_h = Emu(int(self.SLIDE_H.emu * 0.6243))
        # Calculate grid dimensions
        cols = min(n, 5) if n <= 5 else min(n, 4)
        rows = (n + cols - 1) // cols
        cell_w = grid_w // cols
        cell_h = grid_h // rows
        for idx, member in enumerate(members):
            r = idx // cols
            c = idx % cols
            x = grid_left + cell_w * c
            y = grid_top + cell_h * r
            # Cell background
            cell = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                           x, y, cell_w, cell_h)
            cell.fill.solid()
            cell.fill.fore_color.rgb = self.WHITE
            cell.line.color.rgb = self.GRID_LIGHT
            cell.line.width = Pt(0.5)
            # Photo placeholder (left third)
            photo_w = Emu(int(cell_w * 0.35))
            photo = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                            x, y, photo_w, cell_h)
            photo.fill.solid()
            photo.fill.fore_color.rgb = self.OFF_WHITE
            photo.line.fill.background()
            if member.get('image'):
                try:
                    slide.shapes.add_picture(member['image'], x, y,
                                              photo_w, cell_h)
                except Exception:
                    pass
            # Name and role (right of photo)
            text_x = x + photo_w + Inches(0.15)
            text_w = Emu(cell_w - photo_w - Inches(0.3).emu)
            self._txt(slide, member.get('name', ''), text_x,
                      y + Emu(cell_h // 3), text_w, Inches(0.3),
                      size=Pt(10), color=self.BLUE)
            self._txt(slide, member.get('role', ''), text_x,
                      y + Emu(cell_h // 3) + Inches(0.25),
                      text_w, Inches(0.3),
                      size=Pt(8), color=self.TEXT_MUTED)
        self._footer(slide)

    def add_agenda_table(self, label='', title='', headers=None, rows=None):
        """Layout 15: Navy table with highlighted rows."""
        headers = headers or ['Session', 'Time', 'Location', 'Speaker']
        rows = rows or []
        slide = self._new_slide(self.NAVY_DARK)
        self._grid_line_v(slide, 2.9, dark=True)
        self._grid_line_v(slide, 97.1, dark=True)
        self._grid_line_h(slide, 5.15, dark=True)
        self._grid_line_h(slide, 94.85, dark=True)
        self._motif(slide, Emu(int(self.SLIDE_W.emu * 0.029)),
                    Emu(int(self.SLIDE_H.emu * 0.0515)), self.BLUE)
        if label:
            self._label(slide, label, self.ML,
                        Emu(int(self.SLIDE_H.emu * 0.14)), dark=True)
        if title:
            self._title(slide, title, self.ML,
                        Emu(int(self.SLIDE_H.emu * 0.19)), dark=True)
        # Table
        table_left = Emu(int(self.SLIDE_W.emu * 0.029))
        table_top = Emu(int(self.SLIDE_H.emu * 0.30))
        table_w = Emu(int(self.SLIDE_W.emu * 0.942))
        n_rows = len(rows) + 1  # +1 for header
        n_cols = len(headers)
        row_h = Inches(0.45)
        tbl_shape = slide.shapes.add_table(n_rows, n_cols,
                                            table_left, table_top,
                                            table_w, row_h * n_rows)
        tbl = tbl_shape.table
        col_w = table_w // n_cols
        for ci in range(n_cols):
            tbl.columns[ci].width = col_w
        # Header row
        for ci, h in enumerate(headers):
            cell = tbl.cell(0, ci)
            cell.text = h
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(8)
                p.font.bold = True
                p.font.name = self.FONT
                p.font.color.rgb = self.TEXT_MUTED_W
            cell.fill.solid()
            cell.fill.fore_color.rgb = self.NAVY_DARK
        # Data rows
        for ri, row in enumerate(rows):
            highlight = row.get('highlight', False)
            cells = row.get('cells', [])
            for ci, val in enumerate(cells):
                if ci >= n_cols:
                    break
                cell = tbl.cell(ri + 1, ci)
                cell.text = str(val)
                for p in cell.text_frame.paragraphs:
                    p.font.size = Pt(9)
                    p.font.name = self.FONT
                    p.font.color.rgb = RGBColor(0xDD, 0xDD, 0xEE)
                cell.fill.solid()
                if highlight:
                    cell.fill.fore_color.rgb = RGBColor(0x0F, 0x23, 0x3D)
                else:
                    cell.fill.fore_color.rgb = self.NAVY_DARK
        self._footer(slide, dark=True)

    def add_roadmap(self, label='', title='', months=None, rows=None):
        """Layout 16: Gantt-style timeline with colored bars."""
        months = months or ['Q1', 'Q2', 'Q3', 'Q4']
        rows = rows or []
        slide = self._new_slide(self.WHITE)
        self._grid_line_v(slide, 2.9)
        self._grid_line_v(slide, 97.1)
        self._grid_line_h(slide, 5.15)
        self._grid_line_h(slide, 94.85)
        self._motif(slide, Emu(int(self.SLIDE_W.emu * 0.029)),
                    Emu(int(self.SLIDE_H.emu * 0.0515)))
        if label:
            self._label(slide, label, self.ML, Emu(int(self.SLIDE_H.emu * 0.10)))
        if title:
            self._title(slide, title, self.ML, Emu(int(self.SLIDE_H.emu * 0.15)))
        # Chart area
        chart_left = Emu(int(self.SLIDE_W.emu * 0.029))
        chart_top = Emu(int(self.SLIDE_H.emu * 0.25))
        chart_w = Emu(int(self.SLIDE_W.emu * 0.942))
        chart_h = Emu(int(self.SLIDE_H.emu * 0.70))
        label_w = Emu(int(chart_w * 0.15))
        track_w = chart_w - label_w
        track_left = chart_left + label_w
        # Month headers
        n_months = len(months)
        month_w = track_w // n_months
        for mi, m in enumerate(months):
            x = track_left + month_w * mi
            self._txt(slide, m, x, chart_top, month_w, Inches(0.35),
                      size=Pt(9), color=self.TEXT_DARK, bold=True,
                      align=PP_ALIGN.CENTER)
        # Month dividers
        for mi in range(n_months + 1):
            x = track_left + month_w * mi
            s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                        x, chart_top + Inches(0.35),
                                        Pt(0.5), chart_h - Inches(0.35).emu)
            s.fill.solid()
            s.fill.fore_color.rgb = self.GRID_LIGHT
            s.line.fill.background()
        # Rows
        n_rows = len(rows)
        if n_rows == 0:
            self._footer(slide)
            return
        row_top = chart_top + Inches(0.4)
        row_area_h = chart_h - Inches(0.4).emu
        row_h = Emu(row_area_h) // n_rows
        for ri, row in enumerate(rows):
            y = Emu(row_top) + row_h * ri
            # Row label
            self._txt(slide, row.get('label', ''),
                      chart_left + Inches(0.1), y + Emu(row_h // 4),
                      Emu(label_w - Inches(0.2).emu), Emu(row_h // 2),
                      size=Pt(9), color=self.TEXT_DARK)
            # Row divider
            s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                        chart_left, y + row_h,
                                        chart_w, Pt(0.5))
            s.fill.solid()
            s.fill.fore_color.rgb = self.GRID_LIGHT
            s.line.fill.background()
            # Bars
            for bar in row.get('bars', []):
                bar_start = bar.get('start', 0)
                bar_dur = bar.get('duration', 1)
                bar_color = self.BAR_COLORS.get(bar.get('color', 'blue'), self.BLUE)
                bar_label = bar.get('label', '')
                bx = track_left + Emu(int(month_w * bar_start))
                bw = Emu(int(month_w * bar_dur))
                bar_h = Emu(int(row_h * 0.6))
                by = y + Emu(int(row_h * 0.2))
                rect = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                               bx, by, bw, bar_h)
                rect.fill.solid()
                rect.fill.fore_color.rgb = bar_color
                rect.line.fill.background()
                if bar_label:
                    self._txt(slide, bar_label, bx + Inches(0.1),
                              by + Emu(bar_h // 4),
                              Emu(bw - Inches(0.2).emu), Emu(bar_h // 2),
                              size=Pt(8), color=self.WHITE)
        self._footer(slide)

    def add_thank_you(self):
        """Layout 17: Navy background with 'Thank you' text."""
        slide = self._new_slide(self.NAVY_DARK)
        self._grid_line_v(slide, 2.9, dark=True)
        self._grid_line_v(slide, 97.1, dark=True)
        self._grid_line_h(slide, 26.11, dark=True)
        self._grid_line_h(slide, 73.8, dark=True)
        # Logo
        self._txt(slide, 'Backbase', Inches(1.07), Inches(0.53),
                  Inches(2), Inches(0.4), size=Pt(14),
                  color=self.TEXT_WHITE, bold=True)
        # Motif
        self._motif(slide, Emu(int(self.SLIDE_W.emu * 0.029)),
                    Emu(int(self.SLIDE_H.emu * 0.2611)), self.WHITE)
        # Thank you text
        self._txt(slide, 'Thank you', self.ML,
                  Emu(int(self.SLIDE_H.emu * 0.35)),
                  Emu(int(self.SLIDE_W.emu * 0.85)),
                  Inches(1.5), size=Pt(72),
                  color=self.TEXT_WHITE)

    # ══════════════════════════════════════════════════════
    #  INTERNAL HELPERS (continued)
    # ══════════════════════════════════════════════════════

    def _placeholder_rect(self, slide, left, top, w, h):
        """Grey placeholder rectangle for missing images."""
        s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, w, h)
        s.fill.solid()
        s.fill.fore_color.rgb = self.OFF_WHITE
        s.line.fill.background()
        s.name = f"placeholder_{self._slide_num}"

    def _stats_row(self, slide, stats, left, top, width, height):
        """Row of stat items with value + label."""
        n = len(stats)
        if n == 0:
            return
        # Top border
        s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, Pt(0.5))
        s.fill.solid()
        s.fill.fore_color.rgb = self.GRID_LIGHT
        s.line.fill.background()
        stat_w = width // n
        for i, stat in enumerate(stats):
            x = left + stat_w * i
            # Divider between stats
            if i > 0:
                d = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                            x, top, Pt(0.5), height)
                d.fill.solid()
                d.fill.fore_color.rgb = self.GRID_LIGHT
                d.line.fill.background()
            # Value
            self._txt(slide, stat.get('value', ''),
                      x + Inches(0.15), top + Emu(height // 4),
                      Emu(stat_w - Inches(0.3).emu), Inches(0.4),
                      size=Pt(20), color=self.BLUE, bold=True)
            # Label
            self._txt(slide, stat.get('label', ''),
                      x + Inches(0.15), top + Emu(int(height * 0.6)),
                      Emu(stat_w - Inches(0.3).emu), Inches(0.3),
                      size=Pt(9), color=self.TEXT_DARK)

    # ══════════════════════════════════════════════════════
    #  OUTPUT
    # ══════════════════════════════════════════════════════

    def save(self, output_path):
        """Save the presentation and print summary."""
        self.prs.save(output_path)
        size_kb = Path(output_path).stat().st_size // 1024
        slide_count = len(self.prs.slides)
        print(f'\u2713 Saved {output_path} ({size_kb} KB, {slide_count} slides)')

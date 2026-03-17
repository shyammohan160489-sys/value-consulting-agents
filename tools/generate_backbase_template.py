#!/usr/bin/env python3
"""
Generate Backbase Slide Template — Lightweight PPTX template with brand theming.

Creates a minimal PPTX template (~30KB) with:
  - 13.333" x 7.5" widescreen dimensions (Google Slides compatible)
  - Backbase brand theme colors baked into the XML
  - Libre Franklin as the default font
  - A blank slide layout suitable for programmatic generation

This is run once. The output is committed to the repo and used by PptxPresenter.

Usage:
    python3 tools/generate_backbase_template.py

Output:
    templates/presentations/backbase_slides.pptx
"""

from pathlib import Path
from lxml import etree
from pptx import Presentation
from pptx.util import Inches

# Output path
REPO_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = REPO_ROOT / 'templates' / 'presentations'
OUTPUT_PATH = OUTPUT_DIR / 'backbase_slides.pptx'

# Backbase brand colors (from design-system.md, validated against Master Template theme)
THEME_COLORS = {
    'dk1':     '091C35',  # Primary dark
    'lt1':     'FFFFFF',  # White
    'dk2':     '3366FF',  # Primary blue
    'lt2':     '000000',  # Black
    'accent1': '69FEFF',  # Cyan
    'accent2': 'FF503C',  # Red
    'accent3': 'E5EBFF',  # Light blue
    'accent4': 'C2FBFF',  # Pale cyan
    'accent5': 'F3F6F9',  # Off-white
    'accent6': 'FAE0DE',  # Pale pink
    'hlink':   '264EC7',  # Hyperlink blue
    'folHlink':'0097A7',  # Followed link teal
}

# DrawingML namespace
NS_A = 'http://schemas.openxmlformats.org/drawingml/2006/main'
THEME_REL = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme'


def _get_theme_part(prs):
    """Get the theme Part object from the slide master's relationships."""
    sm = prs.slide_masters[0]
    for rel in sm.part.rels.values():
        if rel.reltype == THEME_REL:
            return rel.target_part
    return None


def _set_theme_colors(prs):
    """Inject Backbase brand colors into the presentation's theme XML."""
    theme_part = _get_theme_part(prs)
    if not theme_part:
        print('Warning: Could not find theme part. Colors not set.')
        return

    # Parse theme XML from blob
    theme_xml = etree.fromstring(theme_part.blob)

    # Find <a:clrScheme>
    clr_scheme = None
    for el in theme_xml.iter():
        if el.tag == f'{{{NS_A}}}clrScheme':
            clr_scheme = el
            break

    if clr_scheme is None:
        print('Warning: Could not find clrScheme in theme XML. Colors not set.')
        return

    # Rename to Backbase
    clr_scheme.set('name', 'Backbase')

    # Update each color slot
    for slot_name, hex_color in THEME_COLORS.items():
        for child in clr_scheme:
            if child.tag == f'{{{NS_A}}}{slot_name}':
                # Remove existing color children
                for color_el in list(child):
                    child.remove(color_el)
                # Add srgbClr with our value
                new_el = etree.SubElement(child, f'{{{NS_A}}}srgbClr')
                new_el.set('val', hex_color)
                break

    # Write modified XML back to theme part
    theme_part._blob = etree.tostring(theme_xml, xml_declaration=True,
                                       encoding='UTF-8', standalone=True)


def _set_default_font(prs):
    """Set Libre Franklin as the major and minor font in the theme."""
    theme_part = _get_theme_part(prs)
    if not theme_part:
        return

    theme_xml = etree.fromstring(theme_part.blob)

    # Update all <a:latin> typeface attributes in majorFont and minorFont
    for el in theme_xml.iter():
        tag_local = el.tag.split('}')[-1] if '}' in el.tag else el.tag
        if tag_local in ('majorFont', 'minorFont'):
            for child in el:
                child_local = child.tag.split('}')[-1] if '}' in child.tag else child.tag
                if child_local == 'latin':
                    child.set('typeface', 'Libre Franklin')

    # Write back
    theme_part._blob = etree.tostring(theme_xml, xml_declaration=True,
                                       encoding='UTF-8', standalone=True)


def generate_template():
    """Generate the lightweight Backbase PPTX template."""
    prs = Presentation()

    # Set Google Slides-compatible widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Inject Backbase brand colors into theme
    _set_theme_colors(prs)

    # Set Libre Franklin as default font
    _set_default_font(prs)

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Save
    prs.save(str(OUTPUT_PATH))
    size_kb = OUTPUT_PATH.stat().st_size // 1024
    print(f'\u2713 Generated {OUTPUT_PATH} ({size_kb} KB)')
    print(f'  Dimensions: 13.333" x 7.5" (Google Slides widescreen)')
    print(f'  Theme: Backbase brand colors')
    print(f'  Font: Libre Franklin')


if __name__ == '__main__':
    generate_template()

"""PDF output renderer using WeasyPrint."""

from __future__ import annotations

from pathlib import Path


def render_pdf(html_path: Path, pdf_path: Path) -> Path:
    """Convert an HTML file to PDF using WeasyPrint.

    Args:
        html_path: Path to the source HTML file.
        pdf_path: Path where the PDF will be written.

    Returns:
        Path to the generated PDF.
    """
    try:
        from weasyprint import HTML
    except ImportError:
        raise RuntimeError(
            "WeasyPrint is required for PDF export. "
            "Install it with: pip install weasyprint"
        )

    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    HTML(filename=str(html_path)).write_pdf(str(pdf_path))
    return pdf_path

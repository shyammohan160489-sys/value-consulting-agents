"""CLI entry point for the deal pricing system."""

from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from .config import get_settings
from .engine.comparator import build_yearly_table, format_currency, format_pct, summarize_comparison
from .models.deal import DealBrief
from .models.output import DealPackage
from .orchestrator import Orchestrator
from .storage.deal_store import DealStore

console = Console()


def _get_store() -> DealStore:
    settings = get_settings()
    return DealStore(settings.project_root / "deals")


def _print_summary(comparison) -> None:
    """Print a formatted scenario comparison summary."""
    summary = summarize_comparison(comparison)

    table = Table(title="Deal Summary", show_header=True, header_style="bold cyan")
    table.add_column("Metric", style="bold")
    table.add_column("Value", justify="right")

    for metric, value in summary.items():
        table.add_row(metric, value)

    console.print(table)


def _print_yearly(model, title: str) -> None:
    """Print a formatted yearly breakdown."""
    rows = build_yearly_table(model)

    table = Table(title=title, show_header=True, header_style="bold cyan")
    for col in ["Year", "Users", "License", "Services", "Total", "$/User", "ARR"]:
        justify = "left" if col == "Year" else "right"
        table.add_column(col, justify=justify)

    for row in rows:
        style = "bold" if row["Year"] == "Total" else None
        table.add_row(*[row[c] for c in ["Year", "Users", "License", "Services", "Total", "$/User", "ARR"]], style=style)

    console.print(table)


def _print_package(package: DealPackage) -> None:
    """Print a full deal package summary."""
    console.print()
    console.print(Panel(
        f"[bold]{package.deal_brief.client.name}[/bold] — {package.deal_brief.deal_type.value.replace('_', ' ').title()}\n"
        f"Deal ID: {package.deal_brief.deal_id}",
        title="Deal Package",
        border_style="green",
    ))

    # Deal context
    ctx = package.deal_context
    console.print(Panel(
        f"[bold]Classification:[/bold] {ctx.deal_classification}\n"
        f"[bold]Baseline:[/bold] {ctx.baseline_summary}\n"
        f"[bold]Client Pressure:[/bold] {'; '.join(ctx.client_pressure_points)}\n"
        f"[bold]Backbase Pressure:[/bold] {'; '.join(ctx.backbase_pressure_points)}",
        title="Deal Analysis",
        border_style="cyan",
    ))

    # Pricing strategy
    strat = package.pricing_strategy
    console.print(Panel(
        f"[bold]Recommended:[/bold] {strat.recommended.label} ({strat.recommended.construct_type.value})\n"
        f"  {strat.recommended.description}\n\n"
        f"[bold]Alternative:[/bold] {strat.alternative.label if strat.alternative else 'None'}"
        f"{' (' + strat.alternative.construct_type.value + ')' if strat.alternative else ''}\n"
        f"  {strat.alternative.description if strat.alternative else ''}\n\n"
        f"[bold]Rationale:[/bold] {strat.rationale}",
        title="Pricing Strategy",
        border_style="cyan",
    ))

    # Financial summary
    _print_summary(package.financials)
    console.print()
    _print_yearly(package.financials.recommended, "Recommended — Year-by-Year")

    if package.financials.alternative:
        console.print()
        _print_yearly(package.financials.alternative, "Alternative — Year-by-Year")

    # Narrative
    narr = package.narrative
    console.print(Panel(narr.executive_summary, title="Executive Summary", border_style="green"))

    if narr.objections:
        obj_lines = []
        for obj in narr.objections:
            obj_lines.append(f"[bold]Q:[/bold] {obj.objection}")
            obj_lines.append(f"[bold]A:[/bold] {obj.response}")
            if obj.supporting_data:
                obj_lines.append(f"   [dim]{obj.supporting_data}[/dim]")
            obj_lines.append("")
        console.print(Panel("\n".join(obj_lines), title="Objection Handling", border_style="yellow"))

    if narr.next_steps:
        steps_table = Table(title="Next Steps", show_header=True, header_style="bold cyan")
        steps_table.add_column("#", justify="center", width=3)
        steps_table.add_column("Step")
        steps_table.add_column("Owner")
        steps_table.add_column("Timeline")
        for i, step in enumerate(narr.next_steps, 1):
            steps_table.add_row(str(i), step.step, step.owner, step.timeline)
        console.print(steps_table)


def cmd_run(brief_path: str) -> None:
    """Run the full deal pricing pipeline from a JSON brief."""
    path = Path(brief_path)
    if not path.exists():
        console.print(f"[red]File not found: {brief_path}[/red]")
        sys.exit(1)

    try:
        brief = DealBrief.model_validate_json(path.read_text())
    except Exception as e:
        console.print(f"[red]Invalid deal brief: {e}[/red]")
        sys.exit(1)

    console.print(Panel(
        f"[bold]{brief.client.name}[/bold] — {brief.deal_type.value.replace('_', ' ').title()}\n"
        f"Segments: {', '.join(s.value for s in brief.client.segments)}\n"
        f"Users Y1: {brief.demand.get_user_ramp()[0]:,}",
        title=f"Processing Deal {brief.deal_id}",
        border_style="blue",
    ))

    store = _get_store()
    orchestrator = Orchestrator(store)
    package = asyncio.run(orchestrator.run(brief))

    _print_package(package)
    console.print(f"\n[green]Deal package saved to: deals/{brief.deal_id}_package.json[/green]")


def cmd_list() -> None:
    """List all saved deals."""
    store = _get_store()
    deals = store.list_deals()

    if not deals:
        console.print("[yellow]No deals found. Run 'deal-pricing run <brief.json>' to create one.[/yellow]")
        return

    table = Table(title="Saved Deals", show_header=True, header_style="bold cyan")
    table.add_column("Deal ID")
    table.add_column("Client")
    table.add_column("Type")
    table.add_column("Created")
    table.add_column("Package?")

    for d in deals:
        table.add_row(
            d.deal_id,
            d.client_name,
            d.deal_type,
            d.created_at[:10],
            "[green]Yes[/green]" if d.has_package else "[dim]No[/dim]",
        )

    console.print(table)


def cmd_show(deal_id: str) -> None:
    """Show a saved deal package."""
    store = _get_store()
    try:
        package = store.load_package(deal_id)
        _print_package(package)
    except FileNotFoundError:
        try:
            brief = store.load_brief(deal_id)
            console.print(Panel(
                f"[bold]{brief.client.name}[/bold] — {brief.deal_type.value}\n"
                f"Deal ID: {brief.deal_id}\n"
                f"[yellow]No package generated yet. Run the pipeline first.[/yellow]",
                title="Deal Brief",
                border_style="yellow",
            ))
        except FileNotFoundError:
            console.print(f"[red]Deal not found: {deal_id}[/red]")
            sys.exit(1)


def cmd_export(deal_id: str, fmt: str = "html") -> None:
    """Export a deal package to HTML/PDF."""
    store = _get_store()
    try:
        package = store.load_package(deal_id)
    except FileNotFoundError:
        console.print(f"[red]Deal package not found: {deal_id}[/red]")
        sys.exit(1)

    settings = get_settings()
    output_dir = settings.project_root / "output"
    output_dir.mkdir(exist_ok=True)

    if fmt == "html":
        from .output.html_renderer import render_html
        html_path = output_dir / f"{deal_id}.html"
        render_html(package, html_path)
        console.print(f"[green]HTML exported to: {html_path}[/green]")

    elif fmt == "pdf":
        from .output.html_renderer import render_html
        from .output.pdf_renderer import render_pdf
        html_path = output_dir / f"{deal_id}.html"
        pdf_path = output_dir / f"{deal_id}.pdf"
        render_html(package, html_path)
        render_pdf(html_path, pdf_path)
        console.print(f"[green]PDF exported to: {pdf_path}[/green]")

    elif fmt == "excel":
        from .output.excel_renderer import render_excel
        excel_path = output_dir / f"{deal_id}.xlsx"
        render_excel(package, excel_path)
        console.print(f"[green]Excel exported to: {excel_path}[/green]")

    else:
        console.print(f"[red]Unknown format: {fmt}. Use html, pdf, or excel.[/red]")
        sys.exit(1)


def main():
    """Main CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        prog="deal-pricing",
        description="Backbase Deal Pricing Agent System",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # run
    run_parser = subparsers.add_parser("run", help="Run the full pricing pipeline")
    run_parser.add_argument("brief", help="Path to deal brief JSON file")

    # list
    subparsers.add_parser("list", help="List all saved deals")

    # show
    show_parser = subparsers.add_parser("show", help="Show a saved deal package")
    show_parser.add_argument("deal_id", help="Deal ID to show")

    # export
    export_parser = subparsers.add_parser("export", help="Export deal to HTML/PDF/Excel")
    export_parser.add_argument("deal_id", help="Deal ID to export")
    export_parser.add_argument("--format", "-f", default="html", choices=["html", "pdf", "excel"],
                               help="Output format (default: html)")

    args = parser.parse_args()

    if args.command == "run":
        cmd_run(args.brief)
    elif args.command == "list":
        cmd_list()
    elif args.command == "show":
        cmd_show(args.deal_id)
    elif args.command == "export":
        cmd_export(args.deal_id, args.format)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

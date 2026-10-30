"""Command-line entry point: `triage fetch`, `triage run`, `triage report`."""

import typer

from triage.config import load_settings

app = typer.Typer(help="AI bug triage agent. Suggests only; never changes issues in the tracker.")


@app.command()
def fetch(limit: int = typer.Option(500, help="How many recent issues to pull.")):
    """Pull recent issues from the tracker and cache them locally as JSON."""
    settings = load_settings()
    typer.echo(f"[phase 2] fetch not implemented yet (repo={settings.repo}, limit={limit})")


@app.command()
def run(limit: int | None = typer.Option(None, help="Only process the first N issues (cheap test runs).")):
    """Find duplicates, route, score severity, summarize and detect trends. Writes suggestions.json."""
    typer.echo(f"[phases 3-5] run not implemented yet (limit={limit})")


@app.command()
def report():
    """Render the HTML report from the latest suggestions.json."""
    typer.echo("[phase 6] report not implemented yet")


if __name__ == "__main__":
    app()

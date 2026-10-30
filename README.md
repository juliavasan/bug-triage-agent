# Bug Triage Agent

An AI assistant that reads incoming bug reports and does the first pass of triage that engineers usually do by hand:

1. **Duplicates**: finds reports that describe the same problem, even in different words, and groups them into clusters
2. **Routing**: suggests the most likely owning area (app, cloud, device firmware, networking, partner integration, …)
3. **Severity**: suggests a severity from user impact and how many duplicates exist
4. **Summaries**: three lines per bug covering repro steps, affected devices/platforms, and likely cause
5. **Trends**: flags changes such as "reports about X tripled since the last release"

The demo data is public GitHub issues from the Matter smart-home SDK, [project-chip/connectedhomeip](https://github.com/project-chip/connectedhomeip).

> **Status:** in progress. See [docs/TASKS.md](docs/TASKS.md) for the phased build plan.

## Design principles

- **Deterministic first.** Plain code handles what rules can decide (exact duplicates, label-based routing). The LLM handles only judgment calls.
- **A human approves.** The tool only suggests and never changes issues in the tracker. It outputs an HTML report and a `suggestions.json`.
- **Tracker-agnostic.** All fetching sits behind a small `IssueTracker` interface, so Jira or another tracker could plug in later.
- **Explainable.** Every AI decision includes a short "why" and a confidence score.
- **Cheap to rerun.** Issues, embeddings and LLM answers are cached on disk. `--limit` keeps test runs small.

## Quick start

```bash
python3.11 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt        # or: uv sync --extra dev
cp .env.example .env                   # add GITHUB_TOKEN and OPENAI_API_KEY

triage fetch                           # pull ~500 recent issues into data/issues.json
triage run --limit 50                  # triage a small batch → output/suggestions.json
triage report                          # → output/report.html
```

## Project layout

```
src/triage/
  cli.py           # typer CLI: fetch / run / report
  config.py        # settings from env and .env
  models.py        # tracker-neutral Issue type
  trackers/
    base.py        # IssueTracker interface
tests/             # pytest
docs/TASKS.md      # phased build plan
examples/          # sample report (phase 8)
data/              # local caches (git-ignored)
```

## Running tests

```bash
pytest
```

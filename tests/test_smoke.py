from typer.testing import CliRunner

from triage.cli import app
from triage.config import load_settings


def test_default_settings(monkeypatch):
    monkeypatch.delenv("TRIAGE_REPO", raising=False)
    settings = load_settings()
    assert settings.repo == "project-chip/connectedhomeip"
    assert settings.embedding_model == "text-embedding-3-small"


def test_cli_commands_exist():
    runner = CliRunner()
    for command in ["fetch", "run", "report"]:
        result = runner.invoke(app, [command, "--help"])
        assert result.exit_code == 0, result.output

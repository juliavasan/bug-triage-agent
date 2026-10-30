"""All settings in one place. Values come from environment variables, loaded from .env if present."""

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    repo: str
    github_token: str | None
    openai_api_key: str | None
    embedding_model: str
    chat_model: str
    data_dir: Path

    @property
    def issues_cache(self) -> Path:
        return self.data_dir / "issues.json"

    @property
    def embeddings_cache(self) -> Path:
        return self.data_dir / "embeddings.parquet"

    @property
    def llm_cache(self) -> Path:
        return self.data_dir / "llm_cache.json"

    @property
    def output_dir(self) -> Path:
        return Path("output")


def load_settings() -> Settings:
    return Settings(
        repo=os.getenv("TRIAGE_REPO", "project-chip/connectedhomeip"),
        github_token=os.getenv("GITHUB_TOKEN") or None,
        openai_api_key=os.getenv("OPENAI_API_KEY") or None,
        embedding_model=os.getenv("TRIAGE_EMBEDDING_MODEL", "text-embedding-3-small"),
        chat_model=os.getenv("TRIAGE_CHAT_MODEL", "gpt-4o-mini"),
        data_dir=Path(os.getenv("TRIAGE_DATA_DIR", "data")),
    )

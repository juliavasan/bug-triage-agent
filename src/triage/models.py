"""Tracker-neutral data types. Every stage of the pipeline works on these, not on raw GitHub JSON."""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Issue:
    id: str  # tracker-specific key, e.g. "12345" for GitHub or "HOME-42" for Jira
    title: str
    body: str
    state: str  # "open" or "closed"
    labels: list[str]
    created_at: datetime
    closed_at: datetime | None = None
    url: str = ""
    comments_count: int = 0
    reactions_count: int = 0
    # Ground-truth hints used by evals, e.g. the issue this one was closed as a duplicate of.
    duplicate_of: str | None = None
    extra: dict = field(default_factory=dict)

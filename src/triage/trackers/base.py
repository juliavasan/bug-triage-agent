"""The only thing the pipeline needs from a bug tracker. GitHub implements it today; Jira could later."""

from typing import Protocol

from triage.models import Issue


class IssueTracker(Protocol):
    def fetch_issues(self, limit: int) -> list[Issue]:
        """Return up to `limit` recent issues (open and closed), newest first. Read-only."""
        ...

    def list_labels(self) -> list[str]:
        """Return all label names defined in the tracker, used to derive owning areas."""
        ...

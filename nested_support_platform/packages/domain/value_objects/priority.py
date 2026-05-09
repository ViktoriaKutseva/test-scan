from __future__ import annotations

from packages.domain.exceptions import DomainError


_PRIORITY_RANK = {
    "low": 1,
    "medium": 2,
    "high": 3,
    "urgent": 4,
}

class Priority(str):
    """Canonical support ticket priority value."""

    def __new__(cls, value: str) -> "Priority":
        normalized = value.strip().lower()
        if normalized not in _PRIORITY_RANK:
            raise DomainError(
                "Unsupported priority",
                code="invalid_priority",
                details={"allowed": sorted(_PRIORITY_RANK)},
            )
        return str.__new__(cls, normalized)

    @property
    def rank(self) -> int:
        return _PRIORITY_RANK[str(self)]

    def requires_fast_response(self) -> bool:
        return self in {"high", "urgent"}

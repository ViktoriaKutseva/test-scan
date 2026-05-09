from __future__ import annotations

from packages.domain.exceptions import DomainError


_ALLOWED_TRANSITIONS = {
    "new": {"open", "closed"},
    "open": {"pending", "resolved", "closed"},
    "pending": {"open", "resolved", "closed"},
    "resolved": {"closed", "reopened"},
    "reopened": {"open", "closed"},
    "closed": set(),
}

class Status(str):
    """Canonical ticket status and transition guard."""

    def __new__(cls, value: str) -> "Status":
        normalized = value.strip().lower()
        if normalized not in _ALLOWED_TRANSITIONS:
            raise DomainError(
                "Unsupported ticket status",
                code="invalid_status",
                details={"allowed": sorted(_ALLOWED_TRANSITIONS)},
            )
        return str.__new__(cls, normalized)

    def can_transition_to(self, next_status: str) -> bool:
        return next_status.strip().lower() in _ALLOWED_TRANSITIONS[str(self)]

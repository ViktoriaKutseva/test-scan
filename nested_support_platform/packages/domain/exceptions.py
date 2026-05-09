"""domain exceptions."""

from __future__ import annotations

from typing import Any

class DomainError(Exception):
    """Base exception for domain failures with structured metadata."""

    def __init__(
        self,
        message: str,
        *,
        code: str = "domain_error",
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.code = code
        self.details = details or {}

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-safe representation for APIs and logs."""
        return {
            "error": {
                "code": self.code,
                "message": str(self),
                "details": self.details,
            }
        }

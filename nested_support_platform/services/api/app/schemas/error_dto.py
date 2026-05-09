"""error_dto schema."""

from __future__ import annotations

from typing import Any

class ErrorDto(dict):
    """Transport format for API errors."""

    @classmethod
    def build(
        cls,
        *,
        code: str,
        message: str,
        details: dict[str, Any] | None = None,
        retryable: bool = False,
    ) -> "ErrorDto":
        return cls(
            {
                "code": code,
                "message": message,
                "details": details or {},
                "retryable": retryable,
            }
        )

    @classmethod
    def from_exception(cls, exc: Exception) -> "ErrorDto":
        details = getattr(exc, "details", {})
        code = getattr(exc, "code", "internal_error")
        return cls.build(code=code, message=str(exc), details=details)

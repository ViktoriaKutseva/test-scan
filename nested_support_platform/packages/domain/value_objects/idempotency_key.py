from __future__ import annotations

import re

from packages.domain.exceptions import DomainError


_IDEMPOTENCY_PATTERN = re.compile(r"^[A-Za-z0-9:_-]+$")

class IdempotencyKey(str):
    """Validated key used to safely deduplicate write operations."""

    MIN_LENGTH = 8
    MAX_LENGTH = 128

    def __new__(cls, value: str) -> "IdempotencyKey":
        normalized = value.strip()
        if len(normalized) < cls.MIN_LENGTH:
            raise DomainError(
                "Idempotency key is too short",
                code="invalid_idempotency_key",
                details={"min_length": cls.MIN_LENGTH},
            )
        if len(normalized) > cls.MAX_LENGTH:
            raise DomainError(
                "Idempotency key is too long",
                code="invalid_idempotency_key",
                details={"max_length": cls.MAX_LENGTH},
            )
        if _IDEMPOTENCY_PATTERN.match(normalized) is None:
            raise DomainError(
                "Idempotency key contains unsupported characters",
                code="invalid_idempotency_key",
            )
        return str.__new__(cls, normalized)

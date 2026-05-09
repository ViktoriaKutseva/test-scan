"""idempotency_repository adapter."""

from __future__ import annotations

class IdempotencyRepository:
    def save(self, payload: dict) -> dict:
        return payload

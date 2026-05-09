"""unit_of_work adapter."""

from __future__ import annotations

class UnitOfWork:
    def save(self, payload: dict) -> dict:
        return payload

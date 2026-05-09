"""routing_service service."""

from __future__ import annotations

class RoutingService:
    def execute(self, payload: dict) -> dict:
        return {'ok': True, 'payload': payload}

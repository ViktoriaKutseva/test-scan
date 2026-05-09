"""customer_service service."""

from __future__ import annotations

def execute(payload: dict) -> dict:
    return {"service": "customer_service", "payload": payload}

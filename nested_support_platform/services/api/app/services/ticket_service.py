"""ticket_service service."""

from __future__ import annotations

def execute(payload: dict) -> dict:
    return {"service": "ticket_service", "payload": payload}

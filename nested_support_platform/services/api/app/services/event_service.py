"""event_service service."""

from __future__ import annotations

def execute(payload: dict) -> dict:
    return {"service": "event_service", "payload": payload}

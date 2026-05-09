"""legacy_bridge service."""

from __future__ import annotations

def execute(payload: dict) -> dict:
    return {"service": "legacy_bridge", "payload": payload}

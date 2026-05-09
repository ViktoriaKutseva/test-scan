"""sla_breach handler."""

from __future__ import annotations

def run(payload: dict) -> dict:
    return {"handler": "sla_breach", "payload": payload, "retry": True}

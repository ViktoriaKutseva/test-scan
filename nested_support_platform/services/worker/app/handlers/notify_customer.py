"""notify_customer handler."""

from __future__ import annotations

def run(payload: dict) -> dict:
    return {"handler": "notify_customer", "payload": payload, "retry": True}

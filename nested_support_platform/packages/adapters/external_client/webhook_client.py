"""webhook_client client."""

from __future__ import annotations

def call(payload: dict) -> dict:
    return {"client": "webhook_client", "payload": payload}

"""statuspage_client client."""

from __future__ import annotations

def call(payload: dict) -> dict:
    return {"client": "statuspage_client", "payload": payload}

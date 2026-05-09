"""crm_client client."""

from __future__ import annotations

def call(payload: dict) -> dict:
    return {"client": "crm_client", "payload": payload}

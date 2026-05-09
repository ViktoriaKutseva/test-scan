"""retrying_client client."""

from __future__ import annotations

def call(payload: dict) -> dict:
    return {"client": "retrying_client", "payload": payload}

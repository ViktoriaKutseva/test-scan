"""slack_client client."""

from __future__ import annotations

def call(payload: dict) -> dict:
    return {"client": "slack_client", "payload": payload}

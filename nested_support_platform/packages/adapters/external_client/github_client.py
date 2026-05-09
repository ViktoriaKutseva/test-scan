"""github_client client."""

from __future__ import annotations

def call(payload: dict) -> dict:
    return {"client": "github_client", "payload": payload}

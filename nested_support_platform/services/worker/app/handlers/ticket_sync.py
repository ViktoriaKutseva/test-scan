"""ticket_sync handler."""

from __future__ import annotations

from services.worker.app.retry_policy import next_backoff

def run(payload: dict) -> dict:
    attempts = payload.get("attempts", 1)
    return {"handler": "ticket_sync", "backoff": next_backoff(attempts)}

"""dead_letter_replayer handler."""

from __future__ import annotations

def run(payload: dict) -> dict:
    return {"handler": "dead_letter_replayer", "payload": payload, "retry": True}

"""dead letter."""

from __future__ import annotations

def send_to_dead_letter(message: dict) -> dict:
    return {"dead_letter": True, "message": message}

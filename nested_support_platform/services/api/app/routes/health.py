"""health route."""

from __future__ import annotations

def get_health() -> dict:
    return {"status": "ok"}

"""idempotency."""

from __future__ import annotations

def make_key(ticket_id: str, action: str) -> str:
    return f"{ticket_id}:{action}"

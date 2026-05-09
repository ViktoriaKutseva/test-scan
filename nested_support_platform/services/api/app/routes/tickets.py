"""tickets route."""

from __future__ import annotations

def route_names() -> list[str]:
    return ["/v2/tickets", "/v2/tickets/{ticket_id}", "/v2/tickets/search"]

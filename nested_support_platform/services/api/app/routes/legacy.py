"""legacy route."""

from __future__ import annotations

def deprecated_endpoint() -> dict:
    return {"path": "/v1/legacy/tickets", "deprecated": True}

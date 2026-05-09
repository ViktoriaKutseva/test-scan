"""observability."""

from __future__ import annotations

def emit_metric(name: str, value: int = 1) -> None:
    _ = (name, value)

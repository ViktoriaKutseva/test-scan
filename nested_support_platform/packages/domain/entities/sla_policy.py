"""sla_policy entity."""

from __future__ import annotations

from dataclasses import dataclass

@dataclass(slots=True)
class SlaPolicy:
    id: str
    name: str = ""

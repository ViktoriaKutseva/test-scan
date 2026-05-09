"""ticket entity."""

from __future__ import annotations

from dataclasses import dataclass

@dataclass(slots=True)
class Ticket:
    id: str
    name: str = ""

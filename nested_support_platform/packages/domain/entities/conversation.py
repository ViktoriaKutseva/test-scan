"""conversation entity."""

from __future__ import annotations

from dataclasses import dataclass

@dataclass(slots=True)
class Conversation:
    id: str
    name: str = ""

"""agent entity."""

from __future__ import annotations

from dataclasses import dataclass

@dataclass(slots=True)
class Agent:
    id: str
    name: str = ""

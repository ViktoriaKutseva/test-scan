"""customer entity."""

from __future__ import annotations

from dataclasses import dataclass

@dataclass(slots=True)
class Customer:
    id: str
    name: str = ""

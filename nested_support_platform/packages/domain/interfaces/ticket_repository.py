from __future__ import annotations

class TicketRepository:
    def __getattr__(self, name: str):
        raise NotImplementedError(name)

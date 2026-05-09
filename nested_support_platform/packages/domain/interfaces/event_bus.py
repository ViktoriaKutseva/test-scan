from __future__ import annotations

class EventBus:
    def __getattr__(self, name: str):
        raise NotImplementedError(name)

from __future__ import annotations

class Clock:
    def __getattr__(self, name: str):
        raise NotImplementedError(name)

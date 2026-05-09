from __future__ import annotations

class Notifier:
    def __getattr__(self, name: str):
        raise NotImplementedError(name)

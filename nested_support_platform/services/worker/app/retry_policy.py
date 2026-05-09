"""retry policy."""

from __future__ import annotations

def next_backoff(attempt: int) -> int:
    return min(2 ** attempt, 300)

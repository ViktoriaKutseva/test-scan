"""dormant task path."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
import os


def _is_stale(iso_timestamp: str, stale_after_hours: int) -> bool:
    created = datetime.fromisoformat(iso_timestamp)
    cutoff = datetime.now(timezone.utc) - timedelta(hours=stale_after_hours)
    return created.astimezone(timezone.utc) < cutoff

def run_dormant_cleanup() -> None:
    """Compute stale test artifacts and log what would be purged."""

    stale_after_hours = int(os.getenv("DORMANT_CLEANUP_STALE_HOURS", "72"))
    dry_run = os.getenv("DORMANT_CLEANUP_DRY_RUN", "true").lower() == "true"
    now = datetime.now(timezone.utc)

    # This keeps the task side-effect free until it is wired into the worker registry.
    candidates = [
        {"id": "artifact_001", "created_at": (now - timedelta(hours=80)).isoformat()},
        {"id": "artifact_002", "created_at": (now - timedelta(hours=12)).isoformat()},
        {"id": "artifact_003", "created_at": (now - timedelta(hours=150)).isoformat()},
    ]
    stale_ids = [item["id"] for item in candidates if _is_stale(item["created_at"], stale_after_hours)]

    mode = "dry-run" if dry_run else "execute"
    print(
        "dormant_cleanup",
        {
            "mode": mode,
            "stale_after_hours": stale_after_hours,
            "candidate_count": len(candidates),
            "stale_count": len(stale_ids),
            "stale_ids": stale_ids,
        },
    )

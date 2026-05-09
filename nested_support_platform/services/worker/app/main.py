"""worker main."""

from __future__ import annotations

from services.worker.app.tasks import TASKS


if __name__ == "__main__":
    print(sorted(TASKS))

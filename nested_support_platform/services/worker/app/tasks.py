"""task registration."""

from __future__ import annotations

from services.worker.app.handlers.ticket_sync import run as sync_run
from services.worker.app.handlers.notify_customer import run as notify_run

TASKS = {"ticket_sync": sync_run, "notify_customer": notify_run}

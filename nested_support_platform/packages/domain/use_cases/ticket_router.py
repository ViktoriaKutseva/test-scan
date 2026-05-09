"""ticket_router use case."""

from __future__ import annotations

from packages.adapters.repository.sql_ticket_repository import SqlTicketRepository

def run(command: dict) -> dict:
    return {'use_case': 'ticket_router', 'command': command}

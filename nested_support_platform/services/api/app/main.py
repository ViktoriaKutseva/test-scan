"""api main."""

from __future__ import annotations

from services.api.app.routes import health, tickets


def app_summary() -> dict:
    return {"health": health.get_health(), "routes": tickets.route_names()}


if __name__ == "__main__":
    print(app_summary())

"""Helpers for parsing input datetimes and rendering UTC responses."""
from datetime import datetime, timezone


def parse_input_datetime(value: str) -> datetime:
    dt = datetime.fromisoformat(value)

    if dt.tzinfo is not None:
        dt = dt.astimezone(timezone.utc).replace(tzinfo=None)

    return dt


def iso_utc(dt: datetime) -> str:
    """Render a stored (naive UTC) datetime with an explicit UTC designator."""
    return dt.replace(tzinfo=timezone.utc).isoformat()

# utils.py
from datetime import datetime, timedelta
from typing import List, Tuple


class DateUtils:
    """Static utility class for date operations."""

    @staticmethod
    def parse_datetime(datetime_str: str) -> datetime:
        """Parse a string into a datetime object.
        Expected format: 'YYYY-MM-DD HH:MM'
        """
        try:
            return datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
        except ValueError as e:
            raise ValueError(
                f"Invalid datetime format: {datetime_str}. Expected 'YYYY-MM-DD HH:MM'"
            ) from e

    @staticmethod
    def generate_time_slots(
        date: datetime,
        start_hour: int = 9,
        end_hour: int = 18,
        slot_duration: int = 60
    ) -> List[Tuple[datetime, datetime]]:
        """Generate a list of time slots for a given date.
        Each slot is a tuple (start, end). Default: 9:00 to 18:00, 1-hour slots.
        """
        slots = []
        start_time = datetime(date.year, date.month, date.day, start_hour, 0)
        end_time = datetime(date.year, date.month, date.day, end_hour, 0)

        current = start_time
        while current + timedelta(minutes=slot_duration) <= end_time:
            slot_end = current + timedelta(minutes=slot_duration)
            slots.append((current, slot_end))
            current = slot_end
        return slots

    @staticmethod
    def format_datetime(dt: datetime) -> str:
        """Format datetime for display."""
        return dt.strftime("%Y-%m-%d %H:%M")

    @staticmethod
    def is_valid_booking_time(start: datetime, end: datetime) -> bool:
        """Check if booking time is valid (start before end, within working hours, etc.)"""
        if start >= end:
            return False
        if start.date() != end.date():
            return False
        # Working hours: 9:00 - 18:00
        work_start = start.replace(hour=9, minute=0, second=0, microsecond=0)
        work_end = start.replace(hour=18, minute=0, second=0, microsecond=0)
        return start >= work_start and end <= work_end

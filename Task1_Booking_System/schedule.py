from typing import List, Optional
from datetime import datetime
from booking import Booking

class Scheduler:
    def __init__(self):
        self.bookings: List[Booking] = []

    def _check_conflict(self, new_booking: Booking) -> bool:
        """
        Private method: Check if a new booking conflicts with existing ones
        :param new_booking: The new booking to be checked
        :return: True if conflict exists, False if no conflict
        """
        new_room = new_booking.meeting_room
        new_start, new_end = new_booking.get_time_interval()

        for booking in self.bookings:
            if booking.meeting_room == new_room:
                exist_start, exist_end = booking.get_time_interval()
                if not (new_end <= exist_start or new_start >= exist_end):
                    return True
        return False

    def add_booking(self, new_booking: Booking) -> bool:
        """
        Add new booking: Check for conflicts first, add if no conflict
        :param new_booking: The booking object to be added
        :return: True if added successfully, False if conflict occurs
        """
        if self._check_conflict(new_booking):
            print("❌ Booking conflict: This meeting room is already booked at this time!")
            return False
        print("✅ Booking successful!")
        self.bookings.append(new_booking)
        return True

    def query_bookings_by_room(self, meeting_room) -> List[Booking]:
        """Query all bookings for a specific meeting room"""
        return [b for b in self.bookings if b.meeting_room == meeting_room]

    def query_bookings_by_employee(self, employee) -> List[Booking]:
        """Query all bookings for a specific employee"""
        return [b for b in self.bookings if b.employee == employee]

    def get_all_bookings(self) -> List[Booking]:
        """Retrieve all booking records"""
        return self.bookings

from datetime import datetime

class Booking:
    def __init__(self, employee, meeting_room, start_time: datetime, end_time: datetime):
        """
        :param employee: Employee object
        :param meeting_room: Meeting room object
        :param start_time: Booking start time
        :param end_time: Booking end time
        """
        self.employee = employee
        self.meeting_room = meeting_room
        self.start_time = start_time
        self.end_time = end_time

    def get_time_interval(self) -> tuple[datetime, datetime]:
        """Return the time interval of the booking (start_time, end_time)"""
        return (self.start_time, self.end_time)

    def __str__(self) -> str:
        """
        Return a string representation of the booking:
        f"Booking: Employee[{self.employee.get_name()}] "
        f"MeetingRoom[{self.meeting_room.get_name()}] "
        f"Time: {self.start_time.strftime('%Y-%m-%d %H:%M')} ~ {self.end_time.strftime('%Y-%m-%d %H:%M')}"
        """
        return (f"Booking: Employee[{self.employee.get_name()}] "
                f"MeetingRoom[{self.meeting_room.get_name()}] "
                f"Time: {self.start_time.strftime('%Y-%m-%d %H:%M')} ~ {self.end_time.strftime('%Y-%m-%d %H:%M')}")

# room.py

from abc import ABC, abstractmethod


class MeetingRoom(ABC):
    """
    Abstract base class for all types of meeting rooms.
    Demonstrates abstraction and encapsulation.
    """

    total_rooms = 0  # Class variable to track total number of rooms

    def __init__(self, room_id: str, name: str, capacity: int):
        self.__room_id = room_id
        self.__name = name
        self.__capacity = capacity
        MeetingRoom.total_rooms += 1

    # Getter methods
    def get_room_id(self) -> str:
        return self.__room_id

    def get_name(self) -> str:
        return self.__name

    def get_capacity(self) -> int:
        return self.__capacity

    @abstractmethod
    def display_info(self) -> str:
        """
        Abstract method to enforce polymorphism in subclasses.
        """
        pass

    @classmethod
    def get_total_rooms(cls):
        return cls.total_rooms


class SmallRoom(MeetingRoom):
    """
    Small meeting room subclass.
    Demonstrates inheritance and polymorphism.
    """

    def __init__(self, room_id: str, name: str, capacity: int, has_projector: bool = False):
        super().__init__(room_id, name, capacity)
        self.__has_projector = has_projector

    def has_projector(self) -> bool:
        return self.__has_projector

    def display_info(self) -> str:
        return (
            f"[Small Room] ID: {self.get_room_id()}, "
            f"Name: {self.get_name()}, "
            f"Capacity: {self.get_capacity()}, "
            f"Projector: {self.__has_projector}"
        )

    def __str__(self):
        return self.display_info()


class BigRoom(MeetingRoom):
    """
    Big meeting room subclass.
    Demonstrates inheritance and polymorphism.
    """

    def __init__(self, room_id: str, name: str, capacity: int, video_system: bool = True):
        super().__init__(room_id, name, capacity)
        self.__video_system = video_system

    def has_video_system(self) -> bool:
        return self.__video_system

    def display_info(self) -> str:
        return (
            f"[Big Room] ID: {self.get_room_id()}, "
            f"Name: {self.get_name()}, "
            f"Capacity: {self.get_capacity()}, "
            f"Video System: {self.__video_system}"
        )

    def __str__(self):
        return self.display_info()
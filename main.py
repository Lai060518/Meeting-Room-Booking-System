# Main GUI module for the Meeting Room Booking System.
# Uses tkinter to provide a simple interface.

import tkinter as tk
from tkinter import messagebox, simpledialog
from typing import List, Optional

# Import other modules (will be fully implemented later)
from room import MeetingRoom, SmallRoom, BigRoom
from employee import Employee
from booking import Booking
from schedule import Scheduler
from utils import DateUtils


class BookingApp:
    # Main application window for the booking system.

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Meeting Room Booking System")
        self.root.geometry("900x700")

        # Core data objects (to be replaced with actual logic later)
        self.schedule = Scheduler()
        self.current_user = Employee("E001", "Alice", "Engineering")
        self.rooms: List[Room] = [
            SmallRoom("R01", "Small Meeting A", 6),
            BigRoom("R02", "Large Conference B", 20, True),
            SmallRoom("R03", "Small Meeting C", 4)
        ]

        # Build the GUI
        self.create_widgets()

    def create_widgets(self):
        # Create and arrange all GUI components.
        # Title
        tk.Label(self.root, text="Meeting Room Booking System",
                 font=("Arial", 20, "bold")).pack(pady=10)

        # Main content frame (left: room list, right: calendar)
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.create_room_panel(main_frame)
        self.create_calendar_panel(main_frame)
        self.create_button_panel()

    def create_room_panel(self, parent):
        # Left panel: list of rooms and their details.
        panel = tk.Frame(parent, relief=tk.GROOVE, bd=2)
        panel.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        tk.Label(panel, text="Rooms", font=("Arial", 14)).pack(pady=5)

        self.room_listbox = tk.Listbox(panel, width=25, height=15)
        self.room_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Populate room list
        for room in self.rooms:
            self.room_listbox.insert(tk.END, f"{room.get_room_id()} - {room.get_name()}")

        # Room details (placeholder)
        tk.Label(panel, text="Capacity: ...").pack(anchor=tk.W, padx=5)
        tk.Label(panel, text="Rate: ...").pack(anchor=tk.W, padx=5)

    def create_calendar_panel(self, parent):
        # Right panel: calendar view of availability.
        panel = tk.Frame(parent, relief=tk.GROOVE, bd=2)
        panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        tk.Label(panel, text="Today's Availability", font=("Arial", 14)).pack(pady=5)

        # Canvas for drawing time slots (will be implemented later)
        self.calendar_canvas = tk.Canvas(panel, bg="white", height=400)
        self.calendar_canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Placeholder text on canvas
        self.calendar_canvas.create_text(200, 200, text="Calendar view will be drawn here")

    def create_button_panel(self):
        # Bottom panel: action buttons.
        panel = tk.Frame(self.root)
        panel.pack(fill=tk.X, padx=10, pady=10)

        tk.Button(panel, text="Book Room", command=self.book_room,
                  width=15, bg="lightblue").pack(side=tk.LEFT, padx=5)
        tk.Button(panel, text="My Bookings", command=self.view_my_bookings,
                  width=15, bg="lightgreen").pack(side=tk.LEFT, padx=5)
        tk.Button(panel, text="Refresh", command=self.refresh_calendar,
                  width=15, bg="lightgray").pack(side=tk.LEFT, padx=5)
        tk.Button(panel, text="Exit", command=self.root.quit,
                  width=10, bg="salmon").pack(side=tk.RIGHT, padx=5)

    def book_room(self):
        # Open a new window to make a booking.
        # TODO: implement booking dialog
        messagebox.showinfo("Info", "Booking feature will be implemented soon.")

    def view_my_bookings(self):
        # Show bookings of the current user.
        # TODO: implement view
        messagebox.showinfo("Info", "My Bookings feature will be implemented soon.")

    def refresh_calendar(self):
        # Redraw the calendar with latest availability.
        # TODO: implement calendar drawing
        self.calendar_canvas.delete("all")
        self.calendar_canvas.create_text(200, 200, text="Calendar refreshed (placeholder)")


def main():
    # Entry point of the application.
    root = tk.Tk()
    app = BookingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

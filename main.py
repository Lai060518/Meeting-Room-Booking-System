# Task1_Booking_System/main.py
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from datetime import datetime
from typing import List, Optional

from room import MeetingRoom, SmallRoom, BigRoom
from employee import Employee
from booking import Booking
from schedule import Scheduler
from utils import DateUtils


class BookingApp:
    """Main application window for the booking system."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Meeting Room Booking System")
        self.root.geometry("900x700")

        # Core data objects
        self.schedule = Scheduler()
        self.current_user = Employee("E001", "Alice", "Engineering")

        self.current_view_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

        # Rooms (use correct class names)
        self.rooms: List[MeetingRoom] = [
            SmallRoom("R01", "Small Meeting A", 6),
            BigRoom("R02", "Large Conference B", 20, True),
            SmallRoom("R03", "Small Meeting C", 4),
        ]

        # Selected room for calendar display
        self.selected_room = None

        # Build GUI
        self.create_widgets()

        # Initialize calendar with first room
        if self.rooms:
            self.selected_room = self.rooms[0]
            self.room_listbox.selection_set(0)
            self.refresh_calendar()

    def create_widgets(self):
        """Create and arrange all GUI components."""
        # Title
        tk.Label(
            self.root,
            text="Meeting Room Booking System",
            font=("Arial", 20, "bold")
        ).pack(pady=10)

        # Main content frame (left: room list, right: calendar)
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.create_room_panel(main_frame)
        self.create_calendar_panel(main_frame)
        self.create_button_panel()

    def create_room_panel(self, parent):
        """Left panel: list of rooms and their details."""
        panel = tk.Frame(parent, relief=tk.GROOVE, bd=2)
        panel.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        tk.Label(panel, text="Rooms", font=("Arial", 14)).pack(pady=5)

        self.room_listbox = tk.Listbox(panel, width=25, height=15)
        self.room_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        for room in self.rooms:
            self.room_listbox.insert(
                tk.END,
                f"{room.get_room_id()} - {room.get_name()}"
            )

        # Bind selection event
        self.room_listbox.bind("<<ListboxSelect>>", self.on_room_select)

        # Room details label
        self.room_details_label = tk.Label(panel, text="", justify=tk.LEFT)
        self.room_details_label.pack(anchor=tk.W, padx=5, pady=5)

        # Update details for initial selection
        if self.rooms:
            self.update_room_details(self.rooms[0])

    def update_room_details(self, room):
        """Update the room details label."""
        if isinstance(room, SmallRoom):
            details = f"Capacity: {room.get_capacity()}\nProjector: {room.has_projector()}"
        elif isinstance(room, BigRoom):
            details = f"Capacity: {room.get_capacity()}\nVideo System: {room.has_video_system()}"
        else:
            details = f"Capacity: {room.get_capacity()}"
        self.room_details_label.config(text=details)

    def on_room_select(self, event):
        """Handle room selection in listbox."""
        selection = self.room_listbox.curselection()
        if selection:
            idx = selection[0]
            self.selected_room = self.rooms[idx]
            self.update_room_details(self.selected_room)
            self.refresh_calendar()

    def create_calendar_panel(self, parent):
        """Right panel: calendar view of availability."""
        panel = tk.Frame(parent, relief=tk.GROOVE, bd=2)
        panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Room name label
        self.calendar_title = tk.Label(panel, text="", font=("Arial", 12))
        self.calendar_title.pack(pady=5)

        # Canvas for drawing time slots
        self.calendar_canvas = tk.Canvas(panel, bg="white", height=400)
        self.calendar_canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Scrollbar for canvas
        scrollbar = ttk.Scrollbar(panel, orient=tk.VERTICAL, command=self.calendar_canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.calendar_canvas.configure(yscrollcommand=scrollbar.set)
        self.calendar_canvas.bind("<Configure>", self.on_canvas_configure)

        # Inner frame for time slots
        self.calendar_inner = tk.Frame(self.calendar_canvas, bg="white")
        self.calendar_canvas.create_window((0, 0), window=self.calendar_inner, anchor="nw")

        self.calendar_inner.bind("<Configure>", self.on_inner_configure)

    def on_canvas_configure(self, event):
        """Update scrollregion when canvas resizes."""
        self.calendar_canvas.configure(scrollregion=self.calendar_canvas.bbox("all"))

    def on_inner_configure(self, event):
        """Update scrollregion when inner frame resizes."""
        self.calendar_canvas.configure(scrollregion=self.calendar_canvas.bbox("all"))

    def create_button_panel(self):
        """Bottom panel: action buttons."""
        panel = tk.Frame(self.root)
        panel.pack(fill=tk.X, padx=10, pady=10)

        tk.Button(
            panel, text="Book Room", command=self.book_room,
            width=15, bg="lightblue"
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(
            panel, text="My Bookings", command=self.view_my_bookings,
            width=15, bg="lightgreen"
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(
            panel, text="Refresh", command=self.refresh_calendar,
            width=15, bg="lightgray"
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(
            panel, text="Exit", command=self.root.quit,
            width=10, bg="salmon"
        ).pack(side=tk.RIGHT, padx=5)

    def book_room(self):
        """Open a new window to make a booking."""
        if not self.selected_room:
            messagebox.showwarning("No Room", "Please select a room first.")
            return

        # Create booking dialog
        dialog = tk.Toplevel(self.root)
        dialog.title("Book Room")
        dialog.geometry("400x300")
        dialog.transient(self.root)
        dialog.grab_set()

        # Date
        tk.Label(dialog, text="Date (YYYY-MM-DD):").pack(pady=5)
        date_entry = tk.Entry(dialog)
        date_entry.pack()
        date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))

        # Start time
        tk.Label(dialog, text="Start Time (HH:MM):").pack(pady=5)
        start_entry = tk.Entry(dialog)
        start_entry.pack()
        start_entry.insert(0, "09:00")

        # End time
        tk.Label(dialog, text="End Time (HH:MM):").pack(pady=5)
        end_entry = tk.Entry(dialog)
        end_entry.pack()
        end_entry.insert(0, "10:00")

        # Error label
        error_label = tk.Label(dialog, text="", fg="red")
        error_label.pack(pady=5)

        def do_booking():
            # Parse inputs
            date_str = date_entry.get().strip()
            start_str = start_entry.get().strip()
            end_str = end_entry.get().strip()
            try:
                start_datetime = DateUtils.parse_datetime(f"{date_str} {start_str}")
                end_datetime = DateUtils.parse_datetime(f"{date_str} {end_str}")
            except ValueError as e:
                error_label.config(text=str(e))
                return

            # Validate
            if not DateUtils.is_valid_booking_time(start_datetime, end_datetime):
                error_label.config(
                    text="Invalid time: Must be within 9:00-18:00 and same day."
                )
                return

            # Create booking
            new_booking = Booking(
                self.current_user,
                self.selected_room,
                start_datetime,
                end_datetime
            )

            # Add to scheduler
            if self.schedule.add_booking(new_booking):
                self.current_view_date = start_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
                dialog.destroy()
                self.refresh_calendar()
            else:
                error_label.config(text="Time slot already booked for this room.")

        tk.Button(dialog, text="Confirm Booking", command=do_booking).pack(pady=20)

    def view_my_bookings(self):
        """Show bookings of the current user."""
        bookings = self.schedule.query_bookings_by_employee(self.current_user)
        if not bookings:
            messagebox.showinfo("My Bookings", "You have no bookings.")
            return

        # Create a new window to display bookings
        win = tk.Toplevel(self.root)
        win.title("My Bookings")
        win.geometry("500x300")

        # Listbox to show bookings
        listbox = tk.Listbox(win, width=70, height=15)
        listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        for b in bookings:
            listbox.insert(
                tk.END,
                f"{b.meeting_room.get_name()} | {DateUtils.format_datetime(b.start_time)} - {DateUtils.format_datetime(b.end_time)}"
            )

        # Close button
        tk.Button(win, text="Close", command=win.destroy).pack(pady=5)

    def refresh_calendar(self):
        """Redraw the calendar with latest availability for selected room."""
        if not self.selected_room:
            self.calendar_title.config(text="No room selected")
            return

        view_date_str = self.current_view_date.strftime("%Y-%m-%d")
        self.calendar_title.config(text=f"Availability for {self.selected_room.get_name()} on {view_date_str}")
        
        # Clear inner frame
        for widget in self.calendar_inner.winfo_children():
            widget.destroy()

        slots = DateUtils.generate_time_slots(self.current_view_date)

        # Get bookings for this room
        room_bookings = self.schedule.query_bookings_by_room(self.selected_room)

        # Color code: green = free, red = booked
        for start, end in slots:
            # Check if this slot is booked
            is_booked = False
            booked_by = None
            for booking in room_bookings:
                if start >= booking.start_time and end <= booking.end_time:
                    is_booked = True
                    booked_by = booking.employee.get_name()
                    break

            # Create frame for slot
            slot_frame = tk.Frame(self.calendar_inner, relief=tk.RIDGE, bd=1)
            slot_frame.pack(fill=tk.X, padx=5, pady=2)

            # Color background
            color = "lightgreen" if not is_booked else "salmon"
            slot_frame.configure(bg=color)

            # Time label
            time_label = tk.Label(
                slot_frame,
                text=f"{DateUtils.format_datetime(start)} - {DateUtils.format_datetime(end)}",
                bg=color,
                width=30,
                anchor=tk.W
            )
            time_label.pack(side=tk.LEFT, padx=5)

            # Status label
            status_text = "Available" if not is_booked else f"Booked by {booked_by}"
            status_label = tk.Label(
                slot_frame,
                text=status_text,
                bg=color,
                anchor=tk.W
            )
            status_label.pack(side=tk.LEFT, padx=5)

            # If free, add a book button
            if not is_booked:
                btn = tk.Button(
                    slot_frame,
                    text="Book",
                    command=lambda s=start, e=end: self.quick_book(s, e)
                )
                btn.pack(side=tk.RIGHT, padx=5)

    def quick_book(self, start, end):
        """Quick booking from calendar slot."""
        if not self.selected_room:
            return
        new_booking = Booking(self.current_user, self.selected_room, start, end)
        if self.schedule.add_booking(new_booking):
            self.current_view_date = start.replace(hour=0, minute=0, second=0, microsecond=0)
            self.refresh_calendar()
        else:
            messagebox.showerror("Booking Failed", "This slot is no longer available.")


def main():
    """Entry point of the application."""
    root = tk.Tk()
    app = BookingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox, ttk
# Import existing modules
from room import SmallRoom, BigRoom  # Adjusted: room.py contains subclasses SmallRoom and BigRoom
from employee import Employee
from schedule import Scheduler  # Adjusted: schedule.py defines class Scheduler
from datetime import datetime

class MeetingRoomApp:
    """
    Main Application Class representing the GUI.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("HKMU Meeting Room Booking System")
        self.root.geometry("700x500")
        
        # Initialize the backend logic (corresponds to Scheduler in schedule.py)
        self.system = Scheduler()
        self.initialize_default_data()
        
        # Build the User Interface
        self.create_widgets()

    def initialize_default_data(self):
        # Pre-load some rooms for demonstration purposes
        # Using subclasses defined in your room.py
        r1 = SmallRoom("R101", "Meeting Room A", 10, has_projector=True)
        r2 = BigRoom("R202", "Conference Hall", 50, video_system=True)
        
        # Initialize the bookings list in Scheduler
        self.system.bookings = [] 
        self.rooms_list = [r1, r2] # Maintain a list for UI display

    def create_widgets(self):
        # UI components replacement for console menu
        header_label = tk.Label(self.root, text="Meeting Room Management System", 
                                font=("Helvetica", 18, "bold"), pady=20)
        header_label.pack()

        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        btn_style = {"width": 25, "font": ("Helvetica", 11), "pady": 10}

        # Main Function Buttons linked to system logic
        tk.Button(frame, text="🔍 View All Rooms", command=self.handle_view_rooms, **btn_style).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(frame, text="➕ Create New Booking", command=self.handle_create_booking, **btn_style).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(frame, text="📅 Show All Bookings", command=self.handle_show_bookings, **btn_style).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(frame, text="❌ Cancel a Booking", command=self.handle_cancel_booking, **btn_style).grid(row=1, column=1, padx=10, pady=10)

        # Footer Status Bar
        self.status = tk.Label(self.root, text="System Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    # --- Button Logic Handlers ---

    def handle_view_rooms(self):
        # Function to display all rooms stored in the system
        if not hasattr(self, 'rooms_list') or not self.rooms_list:
            messagebox.showinfo("Rooms", "No rooms available.")
            return
        
        # Call display_info() method from room.py
        room_info = "\n".join([r.display_info() for r in self.rooms_list])
        messagebox.showinfo("Available Meeting Rooms", room_info)

    def handle_create_booking(self):
        # Connection hint for backend logic
        messagebox.showinfo("Action", "Booking logic connected. Please enter details via console or extend this UI.")

    def handle_show_bookings(self):
        # Retrieve all booking records from schedule.py
        bookings = self.system.get_all_bookings()
        if not bookings:
            messagebox.showinfo("Bookings", "No active bookings found.")
        else:
            booking_info = "\n".join([str(b) for b in bookings])
            messagebox.showinfo("Current Bookings", booking_info)

    def handle_cancel_booking(self):
        messagebox.showwarning("Cancel", "Please select a booking ID to remove.")

# Execution of the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MeetingRoomApp(root)
    root.mainloop()

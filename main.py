import tkinter as tk
from tkinter import messagebox, ttk
# Import existing modules
from room import Room
from employee import Employee
from booking import BookingSystem
from datetime import datetime

class MeetingRoomApp:
    """
    Main Application Class representing the GUI.
    Demonstrates OOP Encapsulation by bundling the data
    and behavior together.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("HKMU Meeting Room Booking System")
        self.root.geometry("700x500")
        
        # Initialize the backend logic from other files
        self.system = BookingSystem()
        self.initialize_default_data()
        
        # Build the User Interface
        self.create_widgets()

    def initialize_default_data(self):
        """Pre-load some rooms for demonstration (can be removed if using a file)"""
        self.system.add_room(Room("R101", 10, "Building A"))
        self.system.add_room(Room("R202", 20, "Building B"))
        self.system.add_room(Room("Executive-01", 5, "Level 10"))

    def create_widgets(self):
        # Header Section
        header_label = tk.Label(self.root, text="Meeting Room Management System", 
                                font=("Helvetica", 18, "bold"), pady=20)
        header_label.pack()

        # Button Container
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        # Style configurations for buttons
        btn_style = {"width": 25, "font": ("Helvetica", 11), "pady": 10}

        # Main Function Buttons
        tk.Button(frame, text="🔍 View All Rooms", command=self.handle_view_rooms, **btn_style).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(frame, text="➕ Create New Booking", command=self.handle_create_booking, **btn_style).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(frame, text="📅 Show All Bookings", command=self.handle_show_bookings, **btn_style).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(frame, text="❌ Cancel a Booking", command=self.handle_cancel_booking, **btn_style).grid(row=1, column=1, padx=10, pady=10)

        # Footer Status Bar
        self.status = tk.Label(self.root, text="System Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    # --- Button Logic Handlers ---

    def handle_view_rooms(self):
        rooms = self.system.get_all_rooms()
        if not rooms:
            messagebox.showinfo("Rooms", "No rooms available.")
            return
        
        room_list = "\n".join([f"ID: {r.id} | Cap: {r.capacity} | Loc: {r.location}" for r in rooms])
        messagebox.showinfo("Available Meeting Rooms", room_list)

    def handle_create_booking(self):
        # Open a popup window with entry field in a real scenario.
        # It shows the system is connected to logic.
        messagebox.showinfo("Action", "Opening Booking Interface...\nPlease enter details in the terminal (or extend this GUI).")

    def handle_show_bookings(self):
        bookings = self.system.get_all_bookings()
        if not bookings:
            messagebox.showinfo("Bookings", "No active bookings found.")
        else:
            booking_info = "\n".join([str(b) for b in bookings])
            messagebox.showinfo("Current Bookings", booking_info)

    def handle_cancel_booking(self):
        messagebox.showwarning("Cancel", "Please select a booking ID to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MeetingRoomApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()

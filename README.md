Meeting Room Booking System (COMP2090SEF)
1. Project Overview
This is a Python-based Meeting Room Booking System developed for the HKMU Course Project. The system provides a graphical user interface (GUI) to help organizations manage room schedules, avoid booking conflicts, and improve resource transparency.

2. Key Features
Interactive Calendar Grid: Real-time visualization of room availability using color-coded slots (Green for available, Red for booked).

Conflict Detection: A backend algorithm (_check_conflict) that prevents double-booking by verifying time interval overlaps.

OOP-Driven Architecture: Fully utilizes Object-Oriented Programming concepts including Encapsulation, Inheritance, Polymorphism, and Abstraction.

Dynamic Information Display: Specialized room details (e.g., projector availability) are displayed based on the selected room type.

3. Project Structure
The project follows a modular programming approach:

main.py: The entry point and GUI management using Tkinter.

room.py: Defines the MeetingRoom abstract base class and its subclasses (SmallRoom, BigRoom).

schedule.py: Contains the Scheduler class for booking logic and conflict checks.

booking.py: Defines the Booking data model.

employee.py: Defines the Employee entity.

utils.py: Provides DateUtils for date parsing and automated time slot generation.

4. How to Run
Ensure you have Python 3.x installed.

Clone this repository:

Bash
git clone https://github.com/Lai060518/Meeting-Room-Booking-System.git
Run the application:

Bash
python main.py
5. Demonstration
Introductory Video: [Insert Your 5-Minute Video Link Here]

Screenshots: Please refer to the Appendix in the Project Report for detailed UI demonstrations.

6. Contributors
LI Zhuohao (SID: 13619319) - Development of room.py & employee.py.

WU Zijun (SID: 13747250) - Video shooter, development of booking.py & schedule.py.

LAI Suchang (SID: 13768558) - Project Coordinator, development of main.py & utils.py.

7. License & Declaration
This project is submitted for academic purposes at Hong Kong Metropolitan University (HKMU). We declare that this work is original and complies with the university's policy on academic honesty.

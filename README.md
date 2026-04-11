🚀 Meeting Room Booking System (COMP2090SEF)
An Intelligent, GUI-based Solution for Modern Workplace Scheduling.

📌 Table of Contents
1. Project Overview
2. Core Features
3. OOP Implementation
4. Repository Structure
5. Getting Started
6. Demonstration
7. Meet the Team

📖 1. Project Overview
This repository hosts a robust Meeting Room Booking System designed to streamline resource allocation in corporate environments. Developed using Python and Tkinter, it provides a seamless user experience for managing reservations while maintaining data integrity through backend validation.
✨ 2. Core Features
📅 Dynamic Calendar Grid: Visualizes real-time room availability with distinct color indicators.
🛡️ Conflict Guard: A high-precision interval-overlap algorithm ensures no room is double-booked.
⚡ Real-time Sync: Instant UI updates when switching between different room categories (Small/Big).
🖥️ Responsive GUI: An intuitive interface built on the Tkinter framework for rapid interaction.

🧱 3. OOP Implementation
This project serves as a practical application of the four pillars of Object-Oriented Programming:Encapsulation: Private attributes (e.g., __room_id) secured via getter/setter methods.Inheritance: Specialized SmallRoom and BigRoom classes derived from a common MeetingRoom base.Polymorphism: Dynamic method overriding for room-specific feature display.Abstraction: Utilization of the abc module to define strict blueprints for room entities.

📂 4. Repository StructurePlaintext├── main.py        # System Entry Point & GUI Controller
├── schedule.py    # Logic Engine & Conflict Detection├── room.py        # OOP Hierarchy & Entity Definitions├── booking.py     # Reservation Data Model├── employee.py    # User Entity Class├── utils.py       # Date Parsing & Time-Slot Utilities└── assets/        # System Icons and Documentation Images

🚀 5. Getting StartedTo get the system running locally:Bash# Clone the repository
git clone https://github.com/Lai060518/Meeting-Room-Booking-System.git

# Navigate to the project folder
cd Meeting-Room-Booking-System

# Run the application
python main.py
📺 6. DemonstrationProduct Demo: Watch the 5-Minute Intro Video HereFull Report: Access the detailed Technical Report PDF for comprehensive test cases.👥 7. Meet the TeamNameSIDKey ContributionsLI Zhuohao13619319room.py, employee.py, Logic DesignWU Zijun13747250booking.py, schedule.py, Video ProductionLAI Suchang13768558main.py, utils.py, Project Coordination

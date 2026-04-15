# 🚀 Meeting Room Booking System & Algorithm Study (COMP2090SEF)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

---

## 📌 Table of Contents
* [1. Project Overview](#1-project-overview)
* [2. Task 1: OOP Booking System](#2-task-1-oop-booking-system)
* [3. Task 2: Self-study (Data Structures & Algorithms)](#3-task-2-self-study-data-structures--algorithms)
* [4. Repository Structure](#4-repository-structure)
* [5. Getting Started & User Guide](#5-getting-started-user-guide)
* [6. Demonstration (Video Links)](#6-demonstration)

---

## 📖 1. Project Overview
This repository contains two major components for the HKMU course project:
1. **Task 1**: A functional **Meeting Room Booking System** built with Python/Tkinter, focusing on OOP principles.
2. **Task 2**: A research-based implementation of a **New Data Structure & Algorithm** (Self-study component).

---

## ✨ 2. Task 1: OOP Booking System
* **📅 Dynamic Calendar**: Real-time visualization of room availability.
* **🛡️ Conflict Guard**: Robust logic to prevent double-booking.
* **🧩 OOP Pillars**: 
  - **Encapsulation**: Private state management using `__` attributes.
  - **Inheritance**: Specialized room classes derived from a base `MeetingRoom`.
  - **Polymorphism**: Unified booking interface for different room categories.
  - **Abstraction**: Using `abc` module for structural blueprints.

---

## 🔬 3. Task 2: Self-study (DS & Algorithms)
This part demonstrates the implementation and complexity analysis of:
* **Data Structure**: [Heap Data Structure]
* **Algorithm**: [Heap Sort Algorithm]
* **Scope**: Focuses on data extraction efficiency, ADT definition, and NoSQL storage.

---

## 📂 4. Repository Structure
```text
     /task1_research/        # Task 1: Meetig Room Booking System
    ├──main.py               # Task 1: System Entry Point
    ├── schedule.py          # Task 1: Logic Engine
    ├── room.py              # Task 1: OOP Hierarchy
    ├── booking.py           # Task 1: Data Model
    ├── employee.py          # Task 1: User Entity
    ├── utils.py             # Task 1: Utilities
     /task2_research/        # Task 2: Self-study Research Files
    ├── algorithm_core.py    # Task 2: Main Logic
    ├── data_model.py        # Task 2: Data Structure
    └── user_guide.txt       # Task 2: Technical Instructions
```
## 🚀 5. Getting Started & 📖 . User Guide

### 5a. Task 1: Meeting Room Booking System
1. **Initialize**: Run `python main.py` to start the GUI.
2. **Room Selection**: Select a room from the sidebar. Note the polymorphic display of room details (e.g., Projector/Video System status).
3. **Check Availability**: The grid displays slots from 09:00 to 18:00. Green slots are free.
4. **Make a Booking**: Click "Book" on any green slot. The `Scheduler` will run a conflict check against `self.bookings`.
5. **Real-time Update**: The UI refreshes instantly upon a successful booking via `refresh_calendar()`.

### 5b. Task 2: Heap Sort Study
1. **Run Demo**: Execute `python heap_sort.py`.
2. **Algorithm Execution**: 
   - The script builds a **Max-Heap** from a sample array.
   - It performs **Heap Sort** by repeatedly extracting the maximum element.
3. **Verify Output**: Check the console for the sorted array output to verify the $O(n \log n)$ complexity performance.
---

## 📺 6. Demonstration:
* Task1 [https://github.com/Lai060518/Meeting-Room-Booking-System/releases/download/task1/task1_demo.mp4]
* Task2 [https://github.com/Lai060518/Meeting-Room-Booking-System/releases/download/v1.0/task2_demo.mp4]

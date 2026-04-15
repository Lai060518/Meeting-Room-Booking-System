# 🚀 Meeting Room Booking System & Algorithm Study (COMP2090SEF/8090SEF)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📌 Table of Contents
* [1. Project Overview](#1-project-overview)
* [2. Task 1: OOP Booking System](#2-task-1-oop-booking-system)
* [3. Task 2: Self-study (Heap & Heap Sort)](#3-task-2-self-study-heap--heap-sort)
* [4. Repository Structure](#4-repository-structure)
* [5. Getting Started & User Guide](#5-getting-started--user-guide)
* [6. Demonstration (Video Links)](#6-demonstration)

---

## 📖 1. Project Overview
This repository contains the course project for HKMU COMP2090SEF:
1. **Task 1**: A **Meeting Room Booking System** implementing all core OOP concepts (Inheritance, Polymorphism, Encapsulation, Abstraction).
2. **Task 2**: A self-study research on **Heap Data Structure** and **Heap Sort Algorithm**, including ADT definition and complexity analysis.

---

## ✨ 2. Task 1: OOP Booking System
* **📅 Dynamic Calendar**: Visualizes real-time room availability in 1-hour slots.
* **🛡️ Conflict Guard**: Internal `_check_conflict` logic ensures data integrity.
* **🧩 OOP Pillars**: 
  - **Inheritance**: `SmallRoom` and `BigRoom` inherit from abstract `MeetingRoom`.
  - **Polymorphism**: Specialized `display_info()` implementation for different room types.
  - **Encapsulation**: Private attributes (e.g., `__emp_id`, `__room_id`) protected by getters/setters.
  - **Abstraction**: Defined `MeetingRoom` as an Abstract Base Class (ABC).

---

## 🔬 3. Task 2: Self-study (Heap & Heap Sort)
Based on the research report, this task implements:
* **Data Structure**: **Max-Heap** (represented using a 1D Array).
* **Algorithm**: **Heap Sort** with $O(n \log n)$ time complexity.
* **Core Logic**: Includes `heapify()` for maintaining heap properties and in-place sorting.

---

## 📂 4. Repository Structure
```text
├── main.py              # Task 1: GUI Entry Point
├── schedule.py          # Task 1: Scheduler & Conflict Logic
├── room.py              # Task 1: Room Hierarchy (OOP)
├── booking.py           # Task 1: Booking Data Model
├── employee.py          # Task 1: Employee Entity
├── utils.py             # Task 1: Date & Time Utilities
└── heap_sort.py         # Task 2: Heap & Heap Sort Implementation

---
```
## 🚀 5. Getting Started & User Guide
### 🛠️ 5a. Task 1: Meeting Room Booking System
Run: Execute python main.py.

Interact: Select a room from the list. Notice the polymorphic display of "Projector" (SmallRoom) vs "Video System" (BigRoom).

Book: Click a green "Book" button. The system creates a Booking instance and updates the GUI via refresh_calendar().

### 🛠️ 5b. Task 2: Heap Sort Demonstration
Run: Execute python heap_sort.py.

Process:

The script initializes an unsorted array: [4, 10, 3, 5, 1].

It builds a Max-Heap and then performs sorting.

Result: Check the console output to see the step-by-step transformation to a sorted array.

---

## 📺 6. Demonstration:
* Task1 [https://github.com/Lai060518/Meeting-Room-Booking-System/releases/download/task1/task1_demo.mp4]
* Task2 [https://github.com/Lai060518/Meeting-Room-Booking-System/releases/download/v1.0/task2_demo.mp4]

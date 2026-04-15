# 🚀 Meeting Room Booking System & Algorithm Study (COMP2090SEF/8090SEF)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📌 Table of Contents
* [1. Project Overview](#1-project-overview)
* [2. Task 1: OOP Booking System](#2-task-1-oop-booking-system)
* [3. Task 2: Self-study (Data Structures & Algorithms)](#3-task-2-self-study-data-structures--algorithms)
* [4. Repository Structure](#4-repository-structure)
* [5. Getting Started & User Guide](#5-getting-started--user-guide)
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
├── main.py              # Task 1: System Entry Point
├── schedule.py          # Task 1: Logic Engine
├── room.py              # Task 1: OOP Hierarchy
├── booking.py           # Task 1: Data Model
├── employee.py          # Task 1: User Entity
├── utils.py             # Task 1: Utilities
└── /task2_research/     # Task 2: Self-study Research Files
    ├── algorithm_core.py # Task 2: Main Logic
    ├── data_model.py     # Task 2: Data Structure
    └── user_guide.txt    # Task 2: Technical Instructions
```
## 🚀 5. Getting Started & User Guide
## 🛠️ 5a. Task 1 (Booking App)
How to run:

Bash
python main.py
User Guide:

Login: Register or log in with your Employee ID.

View: Select a room from the sidebar to view its current schedule.

Book: Click 'Book', input the time slot. The Conflict Guard will validate the request.

Refresh: Use the Refresh button to sync data if updates are not shown.

## 🛠️ 5b. Task 2 (Self-study Demo)
How to run:

Bash
cd task2_research
pip install -r requirements.txt  # If any
python algorithm_core.py
User Guide:

The script will fetch data using the implemented algorithm.

Observe the console for complexity analysis and data structure performance.


## 📺 6. Demonstration:
* Task1 [https://github.com/Lai060518/Meeting-Room-Booking-System/releases/download/task1/task1_demo.mp4]
* Task2 [https://github.com/Lai060518/Meeting-Room-Booking-System/releases/download/v1.0/task2_demo.mp4]

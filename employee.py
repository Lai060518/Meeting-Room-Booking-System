# employee.py
class Employee:

    def __init__(self, emp_id, name, department):
        self.__emp_id = emp_id
        self.__name = name
        self.__department = department

    def get_emp_id(self):
        return self.__emp_id

    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

    def display_info(self):
        return f"Employee ID: {self.__emp_id}, Name: {self.__name}, Department: {self.__department}"

    def __str__(self):
        return self.display_info()
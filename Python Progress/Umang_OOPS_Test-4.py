"""
Create a class Person that inherited by class Employee and class Manager.
Generate a new salary by bonus to an old salary for both employee and manager.
Use all OOPS concepts.
"""
from abc import ABC, abstractmethod


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")


class Employee(Person):
    employee_count = 0  # Class variable to keep track of the number of employees

    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary
        Employee.employee_count += 1

    def display_details(self):      # Polymorphism
        super().display_details()
        print(f"Employee ID = {self.employee_id}")
        print(f"Salary = ₹ {self.salary}")

    def calculate_bonus(self, bonus_percentage):
        b = lambda s, x: (x / 100) * s      # Using Lambda
        bonus = b(bonus_percentage, self.salary)
        self.salary = self.salary + bonus
        print("\n ----- New Salary With New Bonus -----")
        print(f"Bonus = ₹ {bonus}")
        print(f"New Salary = ₹ {self.salary} ")


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display_details(self):
        super().display_details()
        print(f"Department: {self.department}")


class Developer(Employee):
    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()
        print(f"Programming Language: {self.programming_language}")


class ALL_DATA(Manager, Developer, ABC):     # Abstract Class
    @abstractmethod
    def __Data(self):       # Abstract Method
        pass


class Validation:   # Encapsulation
    def __VAL(self):
        e = Employee("umang", 20, "E001", 85000)
        __ename = e.name
        __ename = e.age
        __ename = e.employee_id
        __ename = e.salary
        print("\nData Has Been Private Successfully !")

    @staticmethod
    def EMP(password):
        if password == "manager@123":
            print("Password Correct !")
        else:
            print("Invalid Password !")


print("\n ----- MANAGER DETAILS -----")
m_name = input("Enter NAME of Manager = ")
m_age = int(input("Enter AGE of Manager = "))
m_id = input("Enter ID of Manager = ")
m_salary = int(input("Enter Salary of Manager = "))
m_department = input("Enter Department of Manager = ")
emp1 = Manager(m_name, m_age, m_id, m_salary, m_department)

print("\n ----- DEVELOPER DETAILS -----")
d_name = input("Enter NAME of Developer = ")
d_age = int(input("Enter AGE of Developer = "))
d_id = input("Enter ID of Developer = ")
d_salary = int(input("Enter Salary of Developer = "))
d_language = input("Enter Language of Developer = ")
emp2 = Developer(d_name, d_age, d_id, d_salary, d_language)


print("\nEmployee 1 (Manager) Details:")
emp1.display_details()
m_bonus = int(input("Enter Bonus % for Manager = "))
emp1.calculate_bonus(m_bonus)

print("\nEmployee 2 (Developer) Details:")
emp2.display_details()
d_bonus = int(input("Enter Bonus % for Developer = "))
emp2.calculate_bonus(d_bonus)

print(f"\nTotal Employees: {Employee.employee_count}")

p = input("Enter Password = ")
v = Validation()
v.EMP(p)

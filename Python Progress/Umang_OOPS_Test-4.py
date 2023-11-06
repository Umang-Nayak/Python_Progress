"""
Create a class Person that inherited by class Employee and class Manager.
Generate a new salary by bonus to an old salary for both employee and manager.
Use all OOPS concepts.

1) Class
2) Objects
3) Access Modifiers
4) Constructor
5) Destructor
6) Super Method
7) Static Method
8) Magic Methods
9) Polymorphism
10) Encapsulation
11) Inheritance (Single, Hierarchical, Multi-Level, Hybrid)
12) Data Abstraction, Interface
13) F String
14) Lambda

"""
from abc import ABC, abstractmethod


class Person:
    def __init__(self, name, age):      # Constructor
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")


class Employee(Person):     # Inheritance
    employee_count = 0  # Class variable to keep track of the number of employees

    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)     # Super Method
        self.employee_id = employee_id
        self.salary = salary
        Employee.employee_count += 1

    def display_details(self):      # Polymorphism
        super().display_details()
        print(f"Employee ID = {self.employee_id}")      # F Strings
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

    def __add__(self, other):
        return self.salary + other.salary


class Developer(Employee):
    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()
        print(f"Programming Language: {self.programming_language}")

    def __add__(self, other):
        return self.salary + other.salary


class ALL_DATA(ABC):     # Interface
    @abstractmethod
    def __Data(self):       # Abstract Method
        pass


class Owner:   # Encapsulation
    def __init__(self):
        self.__Owner_Name = "XYZ ABC"       # Access Modifiers
        self.__Owner_Age = 35
        self.__Owner_Income = 1000000
        self.__Owner_DOB = "3rd May 2003"
        self.__Owner_WorkExperience = 5

    def __del__(self):
        self.__Owner_Name = 0
        self.__Owner_Age = 0
        self.__Owner_Income = 0
        self.__Owner_DOB = 0
        self.__Owner_WorkExperience = 0
        print("!!! Owner's Data Removed !!!")

    def __Data(self):
        print(f"NAME = {self.__Owner_Name}")
        print(f"AGE = {self.__Owner_Age}")
        print(f"INCOME = {self.__Owner_Income}")
        print(f"DOB = {self.__Owner_DOB}")
        print(f"WORK EXPERIENCE = {self.__Owner_WorkExperience}")

    @staticmethod
    def EMP(password):  # Static Method
        if password == "XYZ@123":
            print("Password Correct !")
            s = Owner()
            print(s.__Data())

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

p = input("Enter Password = ")
o = Owner()
o.EMP(p)


d1 = Developer("Bhavin", 20, "M004", 80000, "Java")
d2 = Developer("Chetan", 21, "M005", 35000, ".Net")
d3 = Developer("Savan", 22, "M006", 100000, "Python")
d4 = Developer("Utsav", 23, "M007", 20000, "PHP")
d5 = Developer("Manthan", 24, "M008", 50000, "Node JS")
d6 = Developer("Rahul", 25, "M009", 70000, "Angular")

x1 = d1.__add__(d2)     # Magic Method
x2 = d3.__add__(d4)
x3 = d5.__add__(d6)
total_salary = x1 + x2 + x3
print("Total Developer Salary New 6 Developer  = ", total_salary)

print(f"\nTotal Employees: {Employee.employee_count}")
del o

class Employee:
    def __init__(self, e_id, e_name, e_salary):
        self.Eid = e_id
        self.Ename = e_name
        self.Esalary = e_salary

    def show_data(self):
        print(f"ID = {self.Eid}")
        print(f"NAME = {self.Ename}")
        print(f"SALARY = {self.Esalary}")

    def __add__(self, other):
        return self.Esalary + other.Esalary

    def __sub__(self, other):
        return self.Esalary - other.Esalary

    def __repr__(self):
        return f"Employee ({self.Eid}, {self.Ename}, {self.Esalary})"


obj1 = Employee(1, "Umang", 70000)
obj2 = Employee(2, "Hemil", 70000)

# Usually we can not perform addition to object of class !
# But with the use of __add__() method , we can perform addition to object of class !
print("Total + Salary =", obj1 + obj2)
print("Total - Salary =", obj1 - obj2)


# We can say __str__ inherits the properties of __repr__ until we overwrite it !
print(str(obj1))
print(repr(obj2))
print(obj2)

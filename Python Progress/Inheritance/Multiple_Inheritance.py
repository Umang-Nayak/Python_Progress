"""
Multiple Inheritance :-
    -> Multiple inheritance allows a class to inherit properties and behaviors from more than one parent class.
    -> There are many programming language that does not support Multiple inheritance but,
        Python is one of the programming languages that supports Multiple inheritance.
    -> In Multiple inheritance, a child class can have multiple parent class.
    -> Syntax :-
        class Parent_Class1:
            // Content
        class Parent_Class2:
            // Content
        class Child_Class(Parent_Class1, Parent_Class2):
            // Content
        obj = Child_Class()
"""


class Maths_Teacher:
    def __init__(self, name, maths, science):
        self.name = name
        self.maths = maths
        self.science = science

    def test_1(self):
        print(f"{self.name} got {self.maths} marks in Maths subject !")


class Science_Teacher:
    def __init__(self, name, maths, science):
        self.name = name
        self.maths = maths
        self.science = science

    def test_2(self):
        print(f"{self.name} got {self.science} marks in Science subject !")


class Student(Maths_Teacher, Science_Teacher):
    def bio(self):
        print(f"Total marks = {self.science + self.maths}")


s = Student("Umang", 95, 73)
s.test_1()
s.test_2()
s.bio()

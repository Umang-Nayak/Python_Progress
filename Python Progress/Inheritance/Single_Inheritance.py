"""
Single Inheritance :-
    -> Single inheritance allows a class to inherit properties and behaviors from a single parent class or base class.
    -> In single inheritance, a child class can have only one immediate parent class.
    -> Syntax :-
        class Parent_Class:
            // Content
        class Child_Class(Parent_Class):
            // Content
        obj = Child_Class()
"""


class Teacher:
    def __init__(self, name, sub):
        self.name = name
        self.sub = sub

    def test(self):
        print(f"The name of Student is {self.name} !")


class Student(Teacher):
    def bio(self):
        print(f"{self.sub} is a favourite subject of {self.name} !")


s = Student("Umang", "Maths")
s.test()
s.bio()

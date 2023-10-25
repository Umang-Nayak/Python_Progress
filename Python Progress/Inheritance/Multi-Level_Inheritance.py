"""
Multi-Level Inheritance :-
    -> Multilevel inheritance is a type of inheritance in object-oriented
        programming where a derived class inherits from a base class,
        and then another class inherits from the derived class.
    -> It creates a chain of inheritance with multiple levels or layers.
    -> In Multi-Level Inheritance, a grand child class have child class and
        that child class have parent class.
    -> Syntax :-
        class Parent_Class:
            // Content
        class Child_Class(Parent_Class):
            // Content
        class Grand_Child_Class(Child_Class):
            // Content
        obj = Grand_Child_Class()
"""


class Principal:
    def pl(self):
        print("I am Principal !")


class Teacher(Principal):
    def tr(self):
        print("I am Teacher !")


class Student(Teacher):
    def st(self):
        print("I am Student !")


s = Student()
s.st()
s.tr()
s.pl()

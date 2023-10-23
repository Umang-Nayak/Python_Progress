"""
Constructor :-
    -> Constructor is a special method used to initialize objects of a class.
    -> Constructor method is called automatically when an object of the class is created.
    -> Syntax :-
        def __init__():
            //content

Destructor :-
    -> Destructor is used to perform cleanup operation when an object is no longer needed or is about to be destroyed.
    -> The concept of Garbage collector & Destructor in python is similar.
    -> We don't have to define destructors in your Python classes because the garbage collector
        takes care of releasing memory and cleaning up resources when objects are no longer referenced.
    -> Destructor is member method of a class.
    -> It deletes the memory of the object.
    -> It can be called with object.
    -> Syntax :-
        def __del__():
            //content
"""

print("--------------- CONSTRUCTOR ---------------")

class MyClass:
    def __init__(self):
        print("""\nHello , I am Constructor ! 
        I am automatically called when object of this class is created !""")

    def clap(self):
        print("I am a normal method in class !")


obj = MyClass()  # Constructor Called

"""
-> Here, we can see the object of MyClass (obj = MyClass()) is created.
-> And when we create object of class,
    it automatically called __init__() method, 
    which is constructor of class. 
"""


class Student:
    def __init__(self):
        print("\nEnter Marks Between 0 to 100 !!!")
        self.mh = int(input("Enter Marks of Hindi = "))
        self.me = int(input("Enter Marks of English = "))
        self.ms = int(input("Enter Marks of Science = "))
        self.mc = int(input("Enter Marks of Computer = "))
        self.mm = int(input("Enter Marks of Maths = "))

    def Total(self):
        print("\nTotal Marks = 500")
        self.t = self.mh + self.me + self.ms + self.mc + self.mm
        self.p = self.t / 5
        print(f"You Got {self.t} Marks in Exam !")
        print(f"Percentage = {self.p} %")


s = Student()  # Constructor Called
s.Total()

print("--------------- DESTRUCTOR ---------------")


class Test:
    def __init__(self):
        print("\n!!! CONSTRUCTOR !!!")

    def simple(self):
        print("!!! SIMPLE METHOD !!!")

    def __del__(self):
        print("!!! DESTRUCTOR !!!")


t = Test()  # Constructor(__init__()) Called
del t  # Destructor(__del__()) Called

"""
-> Here, we can see the object of Test (t = Test()) is created.
-> And when we delete object of class using "del" keyword,
    it automatically called __del__() method of Test class, 
    which is destructor of class. 
"""


class Area:
    def __init__(self):
        print("\nArea of Square !!!")
        self.s = int(input("Enter length of square in c.m. = "))
        print("\nArea of Circle !!!")
        self.c = int(input("Enter radius of circle in c.m. = "))

    def opr(self):
        self.a1 = self.s * self.s
        self.a2 = 3.14 * (self.c * self.c)

    def __del__(self):
        print(f"Area of Square = {self.a1:.2f} c.m.²")
        print(f"Area of Circle = {self.a2:.2f} c.m.²")
        print("Bye ! Bye !")


a = Area()  # Constructor Called
a.opr()
del a  # Destructor Called
# a.opr()
# The above statement throws error because object "a" is already deleted !

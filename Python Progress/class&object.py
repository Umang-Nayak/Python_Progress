"""
class :-
    1) Class is a collection of attributes & methods.
    2) attribute = variable & method = function
    3) Class is a blueprint for creating object(instance).
    4) Class has 3 methods :-
        i) instance method
        ii) class method - @classmethod
        iii) static method - @staticmethod
    5) Syntax :-
        class class_name:
            //content

object :-
    1) Object is an instance of a class.
    2) With use of object , we can use methods & variables of class.
    3) Each object in Python has a unique identity, which is a reference to its location in memory.
"""


class Student:
    def marks(self):
        self.a = int(input("Enter Marks Out of 100 = "))

    def grade(self):
        if self.a < 33:
            print("Fail !!!")
        else:
            print("Pass !!!")


s = Student()
s.marks()
s.grade()
print("MARKS =", s.a)

"""
Here,
"Student" is a class. 
"s" is an object of Student class.
To call the method of Student class, we have to use object like : s.marks() 
To call the variable of Student class, we have to use object like : s.a
"""


# Instance Method

class Test:
    def __init__(self, val):
        self.val = val

    def display(self):
        print("Value :", self.val)


obj = Test(10)
obj.display()  # Calling an instance method
"""
-> Instance methods are the most common type of methods in Python classes.
-> They are defined with the self parameter as the first argument, 
    which represents the instance of the class.
"""


# Class Method

class MyClass:
    class_variable = "I am a class variable"

    @classmethod
    def scv(cls):
        print(cls.class_variable)


m = MyClass()
MyClass.scv()  # Calling a class method
m.scv()
"""
-> To create class method, we have to write @classmethod before class method. 
-> Basically we can change the value of class variable with the use of class method.
-> We can directly call the class method with class name. 
"""


# Static Method

class Apple:
    @staticmethod
    def calc(x, y):
        print("Addition = ", x + y)
        print("Multiplication = ", x * y)


a = Apple()
a.calc(10, 20)  # Calling a static method
"""
-> To create class method, we have to write @classmethod before class method. 
-> Static methods are often used for utility functions that don't 
    depend on the class state and can be called without creating instances.
"""
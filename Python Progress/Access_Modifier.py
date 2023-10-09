"""
Access Modifier = Access Specifier

Public Members :-
    - In Python, all attributes and methods of a class are public by default,
        which means they can be accessed from anywhere.

Protected Members :-
    -Python uses a single underscore prefix (e.g., _variable or _method())
        to indicate that a member is intended for internal use within the class or its subclasses.
    - It's a convention rather than a strict access control mechanism.

Private Members :-
    - Python uses a double underscore prefix (e.g., __variable or __method()) to indicate name mangling,
        which makes it harder to access the member from outside the class.
    - However, it's still possible to access it with the mangled name (e.g., _ClassName__variable).


PUBLIC = Everywhere (Outside of class)
PROTECTED = Inside Parent Class & Child Class
PRIVATE = Inside Parent Class
"""


# PUBLIC
class Student1:
    def __init__(self):
        self.name = "UMANG"
        self.age = 20
        self.gender = "Male"

    def click(self):
        print("PUBLIC METHOD")

obj = Student1()
print("Name = ", obj.name)
print("Age = ", obj.age)
print("Gender = ", obj.gender)
obj.click()


print("--------------------------------------------------------")
# PROTECTED
class Student2:
    def __init__(self):
        self._n = "UMANG"
        self._a = 20
        self._g = "Male"

    def _clk(self):
        print("PROTECTED METHOD")


obj = Student2()
print("Name = ", obj._n)
print("Age = ", obj._a)
print("Gender = ", obj._g)
obj._clk()


print("--------------------------------------------------------")
# PRIVATE
class Test:
    def __init__(self):
        self.__nt = "UMANG"
        self.__at = 20
        self.__gt = "Male"

    def __clk(self):
        print("PRIVATE METHOD")


obj = Test()
print("Name = ", obj._Test__nt)
print("Age = ", obj._Test__at)
print("Gender = ", obj._Test__gt)
obj._Test__clk()

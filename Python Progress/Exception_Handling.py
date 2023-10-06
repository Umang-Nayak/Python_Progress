"""
Exception Handling :-
    1) try  :
        The code where you expect an exception to occur is written in try block.
        If an exception is raised within this block,
        Python will immediately jump to the corresponding except block.

    2) except :
        The except block is used to catch and handle exceptions from try block.
        There are so many type of exception available in python.
        Example - ValueError, IndexError, TypeError, NameError, ZeroDivisionError etc.....

    3) finally :
        The try block generate error or not , finally block execute always.
        It's commonly used for cleanup tasks.

    4) else :
        If try block raised and error that corresponding to
        except block then it goes to except block, or it goes to else block.
        In a simple way , else code should be executed if no exception raised in try block.
"""

# Built-in Error :-

try:
    a = int(input("Enter Number : "))
    print("Number =", a)

except ValueError:
    print("Enter Number Only !!!")

finally:
    print("ALWAYS")

"""
AssertionError: Raised when an assert statement fails.

AttributeError: Raised when you try to access an attribute or method that does not exist on an object.

EOFError: Raised when the input() function reaches the end of the file.

FileNotFoundError: Raised when you attempt to open or manipulate a file that does not exist.

IndexError: Raised when you try to access a list or other sequence with an invalid index.

IOError: Raised for various input/output-related errors.

IndentationError: Raised when there is an issue with the indentation of your code, such as inconsistent spacing.

ImportError: Raised when there is an issue with importing a module.

KeyError: Raised when you try to access a dictionary key that does not exist.

KeyboardInterrupt: Raised when the user interrupts the program by pressing Ctrl+C in the console.

ModuleNotFoundError: Raised when a module you're trying to import cannot be found.

MemoryError: Raised when the program runs out of memory.

NameError: Raised when you try to access a variable or function that is not defined.

PermissionError: Raised when there is an issue with file or directory permissions.

RuntimeError: A generic error that can be raised for various runtime errors.

SyntaxError: Raised when there is a syntax error in your code.

TypeError: Raised when you perform an operation on an object of an inappropriate type.

ValueError: Raised when you perform an operation on an object of the correct type, but with an inappropriate or invalid value.

ZeroDivisionError: Raised when you try to divide a number by zero.
"""

# Custom Error :-

age = int(input("Enter Age : "))

if age < 0 or age > 100:
    raise ValueError("Age Must be between 0 to 100 !!!")
else:
    print("Data Accepted !")


# Defining Custom Exception :-
# To define custom exception , we have to create a new class that is derived from built-in exception class.

class CustomErrorName(Exception):
    # CODE
    pass


# Using Custom Exception :-

try:
    # CODE
    pass

except CustomErrorName:
    # CODE
    pass


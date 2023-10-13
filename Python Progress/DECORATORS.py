"""
Decorators :-
    1) Python decorators allow you to modify the behavior of functions and methods.
    2) Decorators are a way to extend the functionality of a function or method
        without modifying its source code.
    3) Decorator function takes another function as an argument.
    4) And returns a new function that modifies the behavior of the original function.
    5) Syntax :-
        @decorator_function
        def my_function():
            pass
"""


def hola(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx


@hola
def hello():
    print("Hello world")


@hola
def add(a, b):
    print(a + b)


# greet(hello)()
hello()
# greet(add)(1, 2)
add(1, 2)

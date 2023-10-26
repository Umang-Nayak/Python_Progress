"""
1st Question :-
    Write a Python program to compute the square of the first n Fibonacci numbers,
    using the map function and generate a list of the numbers. [UMANG]

First 10 Fibonacci numbers:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

After squaring said numbers of the list:
[0, 1, 1, 4, 9, 25, 64, 169, 441, 1156]
"""

try:    # Using Try Block To Catch Any Error
    def fib(n):  # Using Function
        f1 = 0
        f2 = 1
        fs = []
        for i in range(n):
            fs.append(f1)
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        print(f"First {n} Fibonacci Numbers =", fs)  # Using f String
        sq = lambda z: z * z  # Using Lambda Function
        f_list = list(map(sq, fs))  # Using Map Function
        print(f"First {n} Squared Fibonacci Numbers =", f_list)

    num = int(input("Enter Number = "))
    fib(num)    # Calling Function


except Exception as e:  # Using Except Block To Handle Any Error
    print("\n!!! Some Error Occur !!!")
    print(f"Error = {e}")   # Print Error type

finally:    # Finally block Always Execute
    print("\n<^-^> Thank You <^-^>")


"""
2nd Question :-
    Write a Python program to create a decorator function of
    Fibonacci series up to n using Lambda. [UMANG]

Fibonacci series upto 2:
[0, 1]
Fibonacci series upto 5:
[0, 1, 1, 2, 3]
Fibonacci series upto 6:
[0, 1, 1, 2, 3, 5]
"""

try:    # Using Try Block To Catch Error
    def fibonacci_decorator(func):  # Decorator Function
        def wrapper(n):
            fib = lambda x: x if x <= 1 else fib(x - 1) + fib(x - 2)  # Using Lambda Function
            result = [fib(i) for i in range(n)]     # Using List Comprehension1
            return func(result)
        return wrapper


    @fibonacci_decorator  # Using Decorator Function
    def print_fibonacci_series(fib_series):
        print(f"Fibonacci Series : {fib_series}")  # Using F-String


    num = int(input("Enter Number = "))  # Change n to the desired number of Fibonacci numbers
    print_fibonacci_series(num)  # Calling Function


except Exception as e:  # Using Except Block To Handle Error
    print("\n!!! SOME ERROR OCCUR !!!")
    print(f"Error = {e}")

finally:    # Finally Block Always Execute
    print("\n<^-^> Thank You <^-^>")

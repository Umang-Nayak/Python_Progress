"""
Question :-
    Write a Python program to compute the square of the first N Fibonacci numbers,
    using the map function and generate a list of the numbers. [UMANG]

First 10 Fibonacci numbers:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

After squaring said numbers of the list:
[0, 1, 1, 4, 9, 25, 64, 169, 441, 1156]
"""

try:
    n = int(input("Enter Number = "))
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

except Exception as e:
    print("\n!!! Some Error Occur !!!")
    print(f"Error = {e}")

finally:
    print("\n<^-^> Thank You <^-^>")



"""
Question :-
    Write a Python program to create a decorator function of
    Fibonacci series up to n using Lambda. [UMANG]

Fibonacci series upto 2:
[0, 1]
Fibonacci series upto 5:
[0, 1, 1, 2, 3]
Fibonacci series upto 6:
[0, 1, 1, 2, 3, 5]
"""

try:
    def sample(fx):
        def mfx(arg):
            f1 = 0
            f2 = 1
            fl = []
            for i in range(arg):
                fl.append(f1)
                f3 = f1 + f2
                f1 = f2
                f2 = f3
            fx(arg)
            print(fl)
        return mfx


    @sample
    def add(x):
        print(f"Fibonacci Series upto {x}:")


    size = int(input("Enter Size = "))
    add(size)


except Exception as e:
    print("\n!!! SOME ERROR OCCUR !!!")
    print(f"Error = {e}")

finally:
    print("\n<^-^> Thank You <^-^>")

"""
Reduce :-
    1) The reduce function applies the function to the first two element
        in the iterable. (For ex. List,Tuple)
    2) And then applies the function and to the result, and so on.
    3) The reduce function return the final element.
    4) To use the reduce function, we have to import reduce
        from functools on top of the code.
    5) Syntax :-
        reduce(function , iterable)
"""

from functools import reduce


def total(x, y):
    return x + y


numbers = [5, 7, 13, 15, 24, 28]
print(reduce(total, numbers))

system = ["Handle", "Clutch", "Break", "Tyre"]
print(reduce(total, system))

myList1 = [100, 5, 4, 10, 15, 1]
myList2 = [5, 4, 10, 15, 1, 100]
out = lambda m, n: m-n
print("Reduce 1 =", reduce(out, myList1))
print("Reduce 2 =", reduce(out, myList2))


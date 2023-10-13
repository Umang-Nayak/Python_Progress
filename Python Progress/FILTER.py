"""
Filter :-
    1) Filter is a function that filter each element in sequence based on a given predicate.
    2) Predicate means a function that return boolean value.
    3) And return a new sequence contain only filtered value.
    4) Syntax :-
        filter(predicate, iterable)
"""


def GreaterThan5(value):
    return value > 5


myList = [4, 10, 4, 7, 17, 1, 3, 5, 11, 5, 9]
print("Filter Object =", filter(GreaterThan5, myList))
print("List of filtered value (Value > 5) =", list(filter(GreaterThan5, myList)))
print("Filtering value using Lambda function (Value > 8)=", list(filter(lambda z: z > 8, myList)))

leap = lambda x: x % 4 == 0

year = [2010, 2024, 2222, 2023, 1004, 1989, 1276, 1234, 1523]
ans = list(filter(leap, year))
print("Leap Year =", ans)


def is_even(n):
    return n % 2 == 0


nums = [22,8,9,7,5,12,56,89,85,67,19,38,65,16,37,16]
evens = list(filter(is_even,nums))
print("Even Numbers =", evens)

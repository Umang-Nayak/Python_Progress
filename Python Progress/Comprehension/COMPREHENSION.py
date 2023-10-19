"""
Comprehension :-
    Comprehensions in Python are short and readable ways to create new sequences (lists, sets, dictionaries)
    by performing some operation on each item in an existing sequence (list, tuple, string, etc.).

Main Three Types :-
    1) List Comprehension
    2) Set Comprehension
    3) Dictionary Comprehension
"""

# List Comprehension
# new_list = [expression for item in iterable]

s = [i for i in range(100) if i % 10 == 0]
print(s)

numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers if x % 2 == 0]
print(squared_numbers)


# Dictionary Comprehension
# new_dict = {key_expression: value_expression for item in iterable if condition}

names = ["AMAN", "UmangNayak", "HemilBro"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)

# Set Comprehension
# new_set = {expression for item in iterable if condition}

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = {x for x in numbers}
print(unique_numbers)

# Generator Comprehension
# new_gen = (expression for item in iterable)

s = (i for i in range(10) if i % 3 == 0)
print(s.__next__())
print(s.__next__())
print(s.__next__())
print(s.__next__())

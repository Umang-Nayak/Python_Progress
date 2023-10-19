"""
Set Comprehension :-
    -> Set comprehensions is used to create sets by applying an expression to each item in an iterable.
    -> Sets are an unordered collection of unique elements,
        so any duplicates are automatically removed in the resulting set.
    -> It use "{}"(curly bracket).
    -> Syntax :-
        mySet = {expression for item in iterable if condition}
"""

myset = {i for i in range(5)}
print(myset)

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {x**2 for x in numbers}
print(unique_squares)

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even = {x for x in numbers if x % 2 == 0}
odd = {x for x in numbers if x % 2 != 0}
print("Even Numbers =", even)
print("Odd Numbers =", odd)

words = {"hello", "umang", "bhai"}
uppercase = {word.upper() for word in words}
print("Words in uppercase =", uppercase)

numbers = {1, 2, 3, 4, 5}
squared_pairs = {(x, x ** 2) for x in numbers}
print("Number & their square =", squared_pairs)

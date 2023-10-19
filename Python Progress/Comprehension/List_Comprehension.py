"""
List Comprehension :-
    -> List comprehension is a short and pythonic way to create lists by applying
        an expression to each item in an iterable, such as a list, tuple, or range.
    -> It can also include conditionals to filter the items.
    -> It use "[]"(square bracket).
    -> Syntax :-
        mylist = [expression for item in iterable if condition]

expression :-
    The operation or value to be included in the new list for each item that meets the condition.

item :-
    A variable that represents each element in the iterable.

iterable :-
    The original iterable (e.g., a list, tuple, or range) over which you want to iterate.

condition (optional) :-
    An optional filter that specifies whether the item should be included in the new list.
    If omitted, all items are included
"""

mylist = [i for i in range(5)]
print(mylist)

squares = [x ** 2 for x in range(10)]
print(squares)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 != 0]
print("Even Numbers =", even)
print("Odd Numbers =", odd)

words = ["hello", "umang", "bhai"]
uppercase = [word.upper() for word in words]
print("Words in uppercase =", uppercase)

numbers = [1, 2, 3, 4, 5]
squared_pairs = [(x, x ** 2) for x in numbers]
print("Number & their square =", squared_pairs)

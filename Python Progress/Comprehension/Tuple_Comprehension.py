"""
Tuple Comprehension :-
    -> We can create a tuple comprehension using a generator comprehension.
    -> Just simply type "tuple" keyword before generator comprehension.
    -> By writing "tuple" before generator comprehension converts into tuple comprehension.
    -> It use "()" round bracket.
    -> Syntax :-
        mytuple = tuple(expression for element in iterable if condition)

"""

squares_tuple = tuple(x*5 for x in range(1, 6))
print(squares_tuple)

word = ("nayak", "umang", "patel", "bhavin")
uppercase = tuple(w.upper() for w in word)
print(uppercase)

num = (1, 35, 6880, 632, 32, 445, 76, 6, 2, 23, 5466, 67, 434, 42, 45656, 52, 13247)
m = tuple(x for x in num if x % 2 == 0)
n = tuple(x for x in num if x % 2 != 0)
print("Even numbers =", m)
print("Odd numbers =", n)

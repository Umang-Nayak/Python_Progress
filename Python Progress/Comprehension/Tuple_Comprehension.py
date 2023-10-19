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

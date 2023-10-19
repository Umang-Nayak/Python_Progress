"""
Dictionary Comprehension :-
    -> Dictionary comprehension allows to create a new dictionary by specifying how the key-value pairs
        should be generated using a compact and expressive syntax.
    -> It use "{}"(curly bracket).
    -> Syntax :-
        mydict = {key_expression: value_expression for element in iterable}

key_expression :- This is an expression that defines the keys of the dictionary.
value_expression :- This is an expression that defines the values associated with the keys.
element :- A variable that represents each element in the iterable.
iterable :- The collection of elements over which you are iterating.
"""

squared_dict = {x: x**2 for x in range(1, 6)}
print(squared_dict)

words = ["apple", "banana", "cherry", "date"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
print(even_squares)

mylist = ["Umang", "Hemil", "Aman", "Tirth", "Pratik"]
names = {i: mylist[i] for i in range(len(mylist))}
print(names)

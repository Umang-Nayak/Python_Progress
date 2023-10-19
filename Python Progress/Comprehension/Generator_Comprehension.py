"""
Generator Comprehension :-
    -> Generator comprehension is similar to list comprehensions but produces values one at a time,
        rather than creating a complete list in memory.
    -> This can be very useful when working with large datasets or when you don't need to
        store all the generated values in memory at once.
    -> It use "()" round bracket.
    -> We can print value of generator variable in two simple way.
        1) With all type of loop to print all value
        2) With __next__() to print value one by one
    -> Syntax :-
        mygen = (expression for element in iterable if condition)
"""

sqr = (x**2 for x in range(5))
print("TYPE =", type(sqr))  # Print type of sqr variable
print("OBJECT =", sqr)  # Print Generator Object

print("------------------------------------------")

print("Using __next__() method to print value :- ")
print(sqr.__next__())  # 0
print(sqr.__next__())  # 1
print(sqr.__next__())  # 2
print(sqr.__next__())  # 3
print(sqr.__next__())  # 4
# print(squares.__next__()) This statement throws error, because sqr variable generate value only 5 times.

print("---------------------------------")

print("Using for loop to print value :- ")
numb = (x for x in range(101) if x % 10 == 0)
for i in numb:
    print(i)

print("-----------------------------------------------------------")

print("Names in Uppercase :- ")
word = ("hemil", "umang", "pranav", "bhavin")
uppercase = (w.upper() for w in word)
for i in uppercase:
    print(i)

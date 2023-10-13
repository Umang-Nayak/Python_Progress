"""
Map :-
    1) Map is a function that applies a function to each element in sequence. (For ex. - List)
    2) And it returns a new sequence containing the transformed element.
    3) Syntax :-
        map(function, iterable)
"""

cube = lambda z: z*z*z
print(cube(2))

myList = [5, 3, 8, 1, 4, 2, 6, 9, 7]

print("Traditional way with for loop:- ")
newList1 = []
for i in myList:
    newList1.append(cube(i))
print(newList1)

print("New way with map unction :- ")
print("Return Map Object =", map(cube, myList))
print("Return List by passing a Normal Function =", list(map(cube, myList)))
print("Return List by passing a Lambda Function =", list(map(lambda n: n*n*n, myList)))

L1 = ["m", "nayk", "klt", "prtk", "kalu", "khtrm"]
print(tuple(map(lambda x: True if "a" in x else False, L1)))
print(list(map(lambda x: True if "a" in x else False, L1)))
print(set(map(lambda x: True if "a" in x else False, L1)))
print(str(map(lambda x: True if "a" in x else False, L1)))

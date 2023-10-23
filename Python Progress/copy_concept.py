"""
1) Assignment Operator (=) :-
    -> The = operator is used for variable assignment. It is used to bind a variable to a value or object.
    -> When we use = operator, we are creating a reference to the same object in memory.
    -> This means that if you modify the object through one variable,
        the change will be reflected in all variables that reference the same object.
"""
import copy

print("\n--- Using (=) ---")
x = [5, 10, 15, 20, 25]
y = x  # Assigning variable "x" as a variable "y"
y[2] = 100
print(f"List x = {x}")
print(f"List y = {y}")


"""
2) copy.copy() :- (Shallow copy)
    -> The copy function is used to create a shallow copy of an object.
    -> A shallow copy of an object creates a new object that is a copy of the original object with a new reference.
    -> But it doesn't create copies of the objects contained within the original object.
    -> Instead, it references the same objects that are inside the original object.
    -> Shallow copies are useful when you want to duplicate the top-level structure of a complex object.
"""
print("\n--- Using (copy) ---")
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = copy.copy(a)
b[1][2] = 100
print(f"Original = {a}")  # [[1, 2, 3], [4, 5, 100], [7, 8, 9]]
print(f"Copy = {b}")  # [[1, 2, 3], [4, 5, 100], [7, 8, 9]]


"""
3) copy.deepcopy() :- (Deep copy)
    -> The deepcopy function is used to create a deep copy of an object.
    ->  A deep copy of an object creates a new object with new references
        for all objects contained within the original object.
    -> This means that changes made to objects within the deep copy do
        not affect the original object or any other copies.
    -> Deep copies are useful when you want to completely duplicate an object.
"""
print("\n--- Using (deepcopy) ---")
j = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = copy.deepcopy(j)
k[1][2] = 100
print(f"Original = {j}")  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Deep Copy = {k}")  # [[1, 2, 3], [4, 5, 100], [7, 8, 9]]

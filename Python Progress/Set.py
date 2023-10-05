"""
Set :-
    1) Set is a collection of multiple Data type value.
    2) Set is changeable ,but you can only add new value in set, and you can not remove existing value from set.
    3) The values of a set are in non-sequential order and cannot contain same value in a set.
    4) set are defined using square brackets {}.
"""

s1 = {}
s2 = {5, "Umang", 1, "Nayak", 3, "Bhai"}
s3 = set()

print(type(s1))
print(type(s2))
print(type(s3))


s = {"Umang", 55, True, 13, "Nayak", False}

print(s)
for i in s:
    print(i)

x = {1, 2, 5, 6}
y = {3, 6, 7}
print("u1 =", x)
print("u2 =", y)

print("Union = ", x.union(y))
print("Intersection =", x.intersection(y))

x = {1, 2, 5, 6}
y = {3, 6, 7}
x.update(y)
print("Union Update =", x)

x = {1, 2, 5, 6}
y = {3, 6, 7}
x.intersection_update(y)
print("Intersection Update =", x)

x = {1, 2, 5, 6}
y = {3, 6, 7}
x.symmetric_difference(y)
print("Symmetric Difference to x = ", x)

x = {1, 2, 5, 6}
y = {3, 6, 7}
x.symmetric_difference_update(y)
print("Symmetric Difference Update to x = ", x)

x = {1, 2, 5, 6}
y = {3, 6, 7}
k = x.difference(y)
print("Difference to x = ", k)

x = {1, 2, 3}
y = {4, 5, 6}
print("Disjoint =", x.isdisjoint(y))

x = {1, 2, 3}
y = {3, 4, 5, 6}
print("Disjoint =", x.isdisjoint(y))

x = {1, 2, 3, 4, 5, 6, 7, 8, 9}
y = {5, 6, 7}
print("Superset =", x.issuperset(y))
print("Subset =", y.issubset(x))

m = {"Umang", "Hemil", "Bhavin", "Chetan"}
print("Set =", m)
m.add("Savan")
print("After Adding Savan =", m)
m.remove("Umang")
print("After Removing Umang =", m)
z = {"Uma", "Bhai", "Nayak"}
m.update(z)
print("After Updating to variable z =", m)
m.pop()
print("After Poping random item =", m)
m.discard("Bhai")
print("After Discarding Bhai =", m)

m.clear()
print("After Clearing set =", m)


# Deleting set
del m
print(m)

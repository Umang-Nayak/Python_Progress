"""
List :-
    1) List is a collection of multiple Data type value.
    2) List is mutable, that mean you can change the value of list.
    3) The values in list is in a sequential order.
    4) Lists are defined using square brackets []. 
"""

mylist = [10, 20, 30, 40, 50]

print(mylist)

for i in mylist:
    print(i)


m = ["Umang", "Nayak", 20, "Male", True, ["U", "M", "A", "N", "G"]]

print(m)

for i in m:
    print(i)

print(m[0][3])
print(m[5][2])

# All List Methods

x = [10, 20, 15, 5, "Umang", 13]
print(x)

x.append(17)
print("After Append = ", x)

x.insert(2, "Bhai")
print("After Insert = ", x)

a = x.index(5)
print("Index of 5 = ", a)

b = [3, 2, 1, 4, 7, 6]
b.sort()
print("After Sorting = ", b)

x.pop()
print("After pop = ", x)

z = x.copy()
print("After Copy = ", z)

a = x.count(5)
print("Count of 5 = ", a)

x.remove(5)
print("After Removing 5 = ", x)

x.extend(b)
print("After Extending = ", x)

x.reverse()
print("After Reversing = ", x)

x.clear()
print("After Clearing = ", x)


k = [i for i in range(15)]
for i in k:
    print(i, ",", end="")


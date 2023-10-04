"""
Tuple :-
    1) Tuple is like a List.
    2) Tuple is immutable, that mean you can not change the value of Tuple.
    3) The values in Tuple is in a sequential order.
    4) Tuples are defined using round brackets ().
"""

mylist = (10, 20, 30, 40, 50)

print(mylist)

for i in mylist:
    print(i)


m = ("Umang", "Nayak", 20, "Male", True, ["U", "M", "A", "N", "G"])

print(m)

for i in m:
    print(i)

print(m[0][3])
print(m[5][2])

# All Tuple Methods

x = (10, 20, 15, 5, "Umang", 13)
print(x)

a = x.index(5)
print("Index of 5 = ", a)

a = x.count(5)
print("Count of 5 = ", a)


"""
Note :- These method can implement in List but not in Tuple !

append
insert
pop
copy
remove
extend
reverse
clear
sort

Note :- 
    If you have to perform all these method to tuple,
    then you have to change the type of tuple to list and
    apply the methods then again change to tuple.
    
"""
# For example :-

t = (10, 20, 30)
print(t)
k = list(t)
k.append(40)
t = tuple(k)
print(t)


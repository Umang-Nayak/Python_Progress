
mylist = ["Umang","Bhavin","Chetan","Savan","Hemil"]

a = iter(mylist)

print(a)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


b = iter(range(100000))

print(b)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

#iterable = iter()
#iterator = next()

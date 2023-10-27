print("\n----- Using Magic Method __add__() -----")

print("Addition of 10 & 20 using + operator =", 10 + 20)
a = 32
b = 56
print("Addition of 32 & 56 using __add__() method =", a.__add__(b))


# We can change the behaviour of all magic method by overriding that function !!!
def __add__(other):
    return a - other


print("Addition of 32 & 56 using __add__() method =", __add__(b))


x = 50
y = 20

print(x.__sub__(y))
print(x.__mul__(y))
print(x.__truediv__(y))
print(x.__eq__(y))
print(x.__ne__(y))
print(x.__lt__(y))
print(x.__gt__(y))
print(x.__le__(y))
print(x.__ge__(y))

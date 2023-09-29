"""
The walrus operator, also known as the assignment
expression operator,is a new feature in Python 3.8.
It is denoted by the := symbol and allows you to 
assign a value to a variable within an expression.
This can be useful for avoiding repetitive code
and making your code more concise.
"""


#Arithmetic Operator
a=7
b=3

print("Addition =", a+b)
print("Subtraction =", a-b)
print("Multiplication  =", a*b)
print("Division  =", a/b)
print("Modulus  =", a%b)
print("Exponentiation =", a**b)
print("Floor division  =", a//b)


#Assignment Operator
x=10
print("Simple Assignment =", x)
x=10
x += 3
print("Addition and assignment  =", x)
x=10
x -= 3
print("Subtraction and assignment =", x)
x=10
x *= 3
print("Multiplication and assignment =", x)
x=10
x /= 3
print("Division and assignment =", x)
x=10
x %= 3
print("Modulus and assignment  =", x)
x=10
x //= 3
print("Floor division and assignment =", x)
x=10
x **= 3
print("Exponentiation and assignment =", x)
x=10
x &= 3
print("Bitwise and assignment ", x)
x=10
x |= 3
print("Bitwise or assignment", x)
x=10
x ^= 3
print("Bitwise exclusive or assignment =", x)
x=10
x >>= 3
print("Bitwise right shift assignment =", x)
x=10
x <<= 3
print("Bitwise left shift assignment =", x)


#Comparison Operator
J=10
K=20

if(J > K):
    print("J is greater !")
elif(J < K):
    print("K is greater !")
else:
    print("J and K is equal !")
"""
Types of comparison operator :-
1) Equal to (==)
2) Not equal to (!=)
3) Greater than (>)
4) Less than (<)
5) Greater than or equal to (>=)
6) Less than or equal to (<=)
"""


#Logical Operator
a = True
b = False

if a and b:
    print("Both a and b are True")
else:
    print("Either a or b is False")
"""
1) and :- 
Returns True if both operands are True, and False otherwise.
2) or :-
Returns True if either operand is True, and False otherwise.
3) not :-
Returns True if the operand is False, and False otherwise.
"""

#Identity Operator
a = 10
b = 10

if a is b:
    print("a and b are the same object")
else:
    print("a and b are not the same object")
"""
1) is :- 
Returns True if the two operands are the same object, 
and False otherwise.
2) is not :-
Returns True if the two operands are not the same object, 
and False otherwise.
"""

#Membership Operator
a = [5,10,5,20,25,30]
b = 10

if a in b:
    print("The number is present in the List")
else:
    print("The number is not present in the List")
"""
1) in :- 
Returns True if the left operand is a member of
the right operand, and False otherwise.
2) not in :-
Returns True if the two operands are not 
the same object, and False otherwise.
"""
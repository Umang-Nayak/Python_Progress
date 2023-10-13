"""
Lambda :-
    1) Lambda is used to create anonymous function.
    2) Lambda function does not have name.
    3) Lambda function can take multiple value as an argument and return output of that expression.
    4) We can also pass lambda function to an argument of other function.
    4) Syntax :-
        lambda argument: expression
"""

# Example of lambda
"""
def double(x):
    return x * 2
"""

double = lambda x: x*2
print("Double of 5 =", double(5))
print("Double of 7 =", double(7))
print("Double of 11 =", double(11))


# Passing multiple argument in lambda function
avgof3 = lambda x, y, z: (x+y+z)/3
print(avgof3(12, 22, 32))
print(avgof3(21, 42, 75))


# Passing lambda function to an argument of other function
def stick(f, value):
    return 5 + f(value)


print(stick(double, 10))
print(stick(lambda x: x*2, 10))

x=1
y=2

def test():
    a=10
    b=20
    print("1)",a," & ",b)
    print("2)",x," & ",y)
    
test()

"""
print("3)",a," & ",b)
Here, this statment shows error because
the scope of a & b is only in test() function.

x & y = Global variable
a & b = Local variable
"""
print("4)",x," & ",y)
    

# Data types & Variable

t1 = 132
t2 = 0
t3 = -5
t4 = 1.25
t5 = 0.00001
t6 = -13.45
t7 = "Umang"
t8 = 'k'
t9 ="""
    ok
    ok
    ok
    """
t10 = True
t11 = False
t12 = 3+8j
t13 = 0.15+9.7j

print("The type of",t1,"=",type(t1))
print("The type of",t2,"=",type(t2))
print("The type of",t3,"=",type(t3))
print("The type of",t4,"=",type(t4))
print("The type of",t5,"=",type(t5))
print("The type of",t6,"=",type(t6))
print("The type of",t7,"=",type(t7))
print("The type of",t8,"=",type(t8))
print("The type of",t9,"=",type(t9))
print("The type of",t10,"=",type(t10))
print("The type of",t11,"=",type(t11))
print("The type of",t12,"=",type(t12))
print("The type of",t13,"=",type(t13))

# Variable declaration rule
"""
Variable Name Rules:

Variable names can contain letters :-
    1) a-z
    2) A-Z
    3) digits (0-9)
    4) underscores (_)
    
Variable names must start with :-
    1) a-z
    2) A-Z
    3) underscore (_)

Note :- 
    1)They cannot start with a digit (0-9).
    2)Variable names are case-sensitive.
    3)This means that "myVar" and "myvar" are considered different variables.
    4)Variable name should not contain Special Characters(except underscore "_").
        For ex. - @, $, %, etc.
    5)You cannot use Python reserved words (also known as keywords) as variable names.
        For ex. - if,else,while,for,True,False,None
        

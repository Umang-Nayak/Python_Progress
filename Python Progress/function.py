#Function
"""

-> Main 2 Types of Function :-
    1)Built-in Function
        Example - max(), min(), print(), len(), input()        
    2)User Define Function
    
-> Two Types of user define function :-
    i)Default Function (No Argument)
        Example - def Student(): , def Test(): 
    ii)Parameterised Function (Single or Multiple Argument)
        Example - def Student(a): , def Test(x,y,z):

"""

# 1) Built-in Function

a = max(10,5,3,30,25,18)
print(a)

mylist = ["Umang","Nayak","20","Male","03/05/2003","M.Sc.IT"]
b = len(mylist)
print(b)


# 2) User Define Function
# --------------------------


#   def average(a, b, c=1):
#       print("The average is ", (a + b + c) / 2)


def average(*numbers):
#   print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
#       print("Average is: ", sum / len(numbers))
#       return 7
        return sum / len(numbers)


# average(4, 6)
# average(b=9)

c = average(5, 6, 7, 1)
print(c)


#   def name(**name):
#       print(type(name))
#       print("Hello,", name["fname"], name["mname"], name["lname"])


# name(mname="Buchanan", lname="Barnes", fname="James")

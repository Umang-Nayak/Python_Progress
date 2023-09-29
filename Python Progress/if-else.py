#if-else statment

a=10
b=20

if(a > b):
    print("a is a big number")
else:
    print("b is a big number")


#if-elif-else statment

marks = int(input("Enter marks out of 100 :- "))

if(marks > 90):
    print("A grade")
elif(marks > 70):
    print("B grade")
elif(marks > 50):
    print("C grade")
elif(marks > 30):
    print("D grade")
else:
    print("Fail")


#Nestd if statment

age = int(input("Enter Your Age :- "))
weight = int(input("Enter Your Weight :- "))

if(age >= 18 and age <=40):
    if(weight >= 40 and weight <=70):
        print("Congratulation ! You can join any sprt activity !")
    else:
        print("Sorry ! Weight Restriction !")
else:
    print("Sorry ! Age Restriction !")
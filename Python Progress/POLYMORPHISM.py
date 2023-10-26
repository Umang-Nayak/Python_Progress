"""
What Is Polymorphism?
    -> In the basic English language, Polymorphism means to exist in different states.
    -> The same object or thing changing its state from one form to another is known as polymorphic.
    -> The same function or method, being used differently in different scenarios,
        can perfectly describe Polymorphism.
    -> It occurs mostly with base and derived classes.
    -> The concept of Polymorphism has very strong ties with the method overriding concept.

Method Overloading :-
    -> In Python, When a class defines a method, and we can use it with a different set of parameters
        is referred as Method Overloading.
    -> In Python, method overloading isn't supported in the same way as in languages like Java or C++.
    -> If you define multiple methods with the same name in a class, Python will simply consider the last
        defined method as the one to be used, and the earlier methods will be overridden.
    -> Python methods are dynamically typed and can accept any number of arguments,
        so method overloading is usually achieved through default arguments or by
        explicitly checking the number and types of arguments within the method.

Method Overriding :-
    -> When a child class defines a method with the same name as a method with same
        parameter in its parent class, it's referred to as Method Overriding.

Overloading = Same method name but different parameters
Overriding = Same method name with same parameters
"""

print("\n---------- Simple Example of Polymorphism ----------")
# Below statement is also example of polymorphism
# Because "+" Operator is performing 2 task
# 1st is Addition & 2nd is Concatenation
print("1) Addition = ", 10 + 20)  # Output : 30
print("2) Concatenation = ", "10" + "20")  # Output : 1020


print("\n---------- Method Overloading ----------")
class Top:
    def calc(self, *args):
        if len(args) == 2:
            print(f"{args[0]} + {args[1]} = {args[0] + args[1]}")
        elif len(args) == 3:
            print(f"{args[0]} + {args[1]} + {args[2]} = {args[0] + args[1] + args[2]}")
        elif len(args) == 4:
            print(f"{args[0]} + {args[1]} + {args[2]} + {args[3]} = {args[0] + args[1] + args[2] + args[3]}")
        elif len(args) == 5:
            print(f"{args[0]} + {args[1]} + {args[2]} + {args[3]} + {args[4]} = {args[0] + args[1] + args[2] + args[3] + args[4]}")
        else:
            print("Please Give Argument Between 2 To 5 !!!")


t = Top()
t.calc(10, 20)
t.calc(10, 20, 30)
t.calc(10, 20, 30, 40)
t.calc(10, 20, 30, 40, 50)
t.calc(10, 20, 30, 40, 50, 60)


print("\n---------- Method Overriding ----------")
class HighTop:
    def calc(self, x, y):
        print(f"Addition = {x + y}")


class LowBottom(HighTop):
    def calc(self, x, y):
        print(f"Multiplication = {x * y}")


b = LowBottom()
b.calc(10, 20)


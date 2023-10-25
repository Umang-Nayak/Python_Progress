"""
Hierarchical Inheritance :-
    -> Hierarchical inheritance allows multiple subclasses inherit from a single common superclass.
    -> In Hierarchical inheritance, multiple child class have only one parent class.
    -> Syntax :-
        class Parent_Class:
            // Content
        class Child_Class1(Parent_Class):
            // Content
        class Child_Class2(Parent_Class):
            // Content
        obj1 = Child_Class1()
        obj2 = Child_Class2()
"""


class Father:
    def __init__(self, f_name, s_name, d_name):
        self.f_name = f_name
        self.s_name = s_name
        self.d_name = d_name

    def fam(self):
        print(f"1) My name is {self.f_name}")
        print(f"2) I am a father of {self.s_name} & {self.d_name}")


class Son(Father):
    def bio(self):
        print(f"3) {self.s_name}'s Class")


class Daughter(Father):
    def bio(self):
        print(f"4) {self.d_name}'s Class")


s = Son("Shailesh", "Umang", "Megha")
s.fam()
s.bio()

d = Daughter("Shailesh", "Umang", "Megha")
d.fam()
d.bio()

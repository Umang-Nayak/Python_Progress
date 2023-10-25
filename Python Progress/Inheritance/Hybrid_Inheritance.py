"""
Hybrid Inheritance :-
    -> Hybrid inheritance is a combination of different types of inheritance within the same program.
    -> It allows you to use a mix of single, multiple, multilevel,
        or hierarchical inheritance in a single class hierarchy.
    -> Syntax :-
        class Parent_Class:
            // Content
        class Child_Class1(Parent_Class):
            // Content
        class Child_Class2(Parent_Class):
            // Content
        class Grand_Child_Class(Child_Class1, Child_Class2):
            // Content
        obj = Grand_Child_Class()
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
    def bio_s(self):
        print(f"3) {self.s_name}'s Class")


class Daughter(Father):
    def bio_d(self):
        print(f"4) {self.d_name}'s Class")


class BFF(Son, Daughter):
    def chat(self):
        print(f"5) I am a friend of {self.s_name} & {self.d_name}")


b = BFF("Erik", "Chris", "Eva")
b.fam()
b.bio_s()
b.bio_d()
b.chat()


"""
super() :-
    -> super() is a built-in function that is used to call a method from the parent class within a child class.
    -> It is commonly used in the context of inheritance.
    -> super() helps to maintain the principle of code reusability and ensures that the parent class's behavior
        is retained and extended in the child class.
"""


print("\n ---------- Example 1 ----------")
class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def speak(self):
        super().speak()  # Using super() keyword to call speak method of parent class
        print("Dog barks")


dog = Dog()  # Create an instance of the Dog class
dog.speak()  # Call the speak method of the Dog class


print("\n ---------- Example 2 ----------")

class Teacher:
    def getData(self):
        self.id = int(input("Enter ID = "))
        self.name = input("Enter NAME = ")
        self.std = int(input("Enter STANDER = "))

    def top(self):
        print("\nI am a method of Teacher Class !!!")
        print(f"Student ID = {self.id}")
        print(f"Student NAME = {self.name}")
        print(f"Student STANDER = {self.std}")


class Student(Teacher):
    def getData(self):
        super().getData()
        print("\nGetting Data in student class")
        self.gender = input("Enter GENDER = ")
        self.age = int(input("Enter AGE = "))


    def bottom(self):
        print("\nI am a method of Student Class !!!")
        print(f"My ID = {self.id}")
        print(f"My NAME = {self.name}")
        print(f"My STANDER = {self.std}")
        print(f"My GENDER = {self.gender}")
        print(f"My AGE = {self.age}")


s = Student()
s.getData()
s.top()
s.bottom()

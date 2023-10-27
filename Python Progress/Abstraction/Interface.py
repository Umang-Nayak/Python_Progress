from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def formula(self):
        pass


class Square(Shape):
    def show(self):
        print("\nSquare has 4 sides !!!")

    def formula(self):
        s1 = float(input("Enter Length in Centi Meter = "))
        area = s1 * s1
        print(f"Area of Square = {area} c.m.²")


class Triangle(Shape):
    def show(self):
        print("\nSquare has 3 sides !!!")

    def formula(self):
        b = float(input("Enter Breadth in Centi Meter = "))
        h = float(input("Enter Height in Centi Meter = "))
        area = 0.5 * (b*h)
        print(f"Area of Triangle = {area} c.m.²")


class Circle(Shape):
    def show(self):
        print("\nCircle has no sides !!!")

    def formula(self):
        r = float(input("Enter Radius in Centi Meter = "))
        area = 3.14 * (r*r)
        print(f"Area of Circle = {area} c.m.²")


s = Square()
t = Triangle()
c = Circle()

s.show()
s.formula()

t.show()
t.formula()

c.show()
c.formula()

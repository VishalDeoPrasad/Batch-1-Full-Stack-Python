from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        print("Default Araa")

    @abstractmethod
    def perimeter(self):
        print("Defalult perimeter")

class Rectangle(Shape):
    def area(self):
        print("Rectangle Area")

    def perimeter(self):
        print("Rectangle Perimeter")

    def anything(self):
        print("anything method..")


r = Rectangle()
r.area()
r.perimeter()
r.anything()
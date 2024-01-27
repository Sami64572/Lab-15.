from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius**2

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

rectangle = Rectangle(4, 6)
circle = Circle(5)

print(f"Rectangle Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")
print(f"Circle Area: {circle.area()}, Perimeter: {circle.perimeter()}")
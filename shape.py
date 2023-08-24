"""
Shape Factory:
Implement a ShapeFactory that creates different types of shapes (Circle, Square, Triangle) based on user input.
"""
from abc import ABC, abstractmethod

class ShapeFactory(ABC):
    @abstractmethod
    def display_info(self):
        pass

class Circle(ShapeFactory):
    def __init__(self, radius):
        self.radius = radius

    def display_info(self):
        print(f"This is a Circle with radius {self.radius}")

class Square(ShapeFactory):
    def __init__(self, side):
        self.side = side

    def display_info(self):
        print(f"This is a Square with side {self.side}")

class Triangle(ShapeFactory):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def display_info(self):
        print(f"This is a Triangle with sides {self.side1}, {self.side2}, {self.side3}")

def main():
    circle = Circle(5)
    square = Square(5)
    triangle = Triangle(5, 5, 5)

    shapes = [circle, square, triangle]
    for shape in shapes:
        shape.display_info()

if __name__ == "__main__":
    main()



import math


class Shape:
    """
    Base class for geometric shapes.
    Defines the area() method which must be overridden by subclasses.
    """

    def area(self):
        """
        Calculates the area of the shape.
        Raises an error to ensure subclasses implement their own version.
        """
        raise NotImplementedError("Subclass must implement abstract method 'area'")


class Rectangle(Shape):
    """
    Derived class for a rectangle. Overrides area().
    """

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculates the area of the rectangle: length * width."""
        return self.length * self.width


class Circle(Shape):
    """
    Derived class for a circle. Overrides area().
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculates the area of the circle: π * radius²."""
        return math.pi * (self.radius**2)

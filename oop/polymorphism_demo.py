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
        # Raising NotImplementedError exactly as a placeholder
        raise NotImplementedError


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
        # Use math.pi and ** 2 for clear implementation
        return math.pi * (self.radius**2)

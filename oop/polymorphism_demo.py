#!/usr/bin/env python3
# polymorphism_demo.py

import math


class Shape:
    """Base class for different shapes."""

    def area(self):
        """Placeholder method to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement the area() method.")


class Rectangle(Shape):
    """Rectangle shape class inheriting from Shape."""

    def __init__(self, length, width):
        """Initialize rectangle dimensions."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Circle shape class inheriting from Shape."""

    def __init__(self, radius):
        """Initialize circle radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)

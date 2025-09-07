#!/usr/bin/env python3
# book_class.py

class Book:
    """A class to represent a book using Python magic methods."""

    def __init__(self, title, author, year):
        """Constructor: Initialize book attributes."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Print message when object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Human-readable string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

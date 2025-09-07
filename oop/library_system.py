#!/usr/bin/env python3
# library_system.py

class Book:
    """Base class representing a generic book."""

    def __init__(self, title, author):
        """Initialize common book attributes."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation for a regular book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""

    def __init__(self, title, author, file_size):
        """Initialize EBook attributes along with base Book attributes."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """String representation for an EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a printed book."""

    def __init__(self, title, author, page_count):
        """Initialize PrintBook attributes along with base Book attributes."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation for a PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class demonstrating composition by managing a collection of books."""

    def __init__(self):
        """Initialize the library with an empty collection of books."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            print(book)

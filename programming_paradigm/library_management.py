class Book:
    """Represents a book with a title, author, and availability status."""

    def __init__(self, title, author):
        # Public attributes
        self.title = title
        self.author = author

        # Private attribute for state tracking (availability)
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out (unavailable)."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns the current availability status."""
        return not self._is_checked_out

    def __str__(self):
        """String representation for user-friendly display."""
        return f"{self.title} by {self.author}"


class Library:
    """Manages a collection of Book objects."""

    def __init__(self):
        # Private list to store Book objects
        self._books = []

    def add_book(self, book):
        """Adds a Book object to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Finds a book by title and attempts to check it out."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out: {title}")
                return
        print(f"Error: '{title}' is either not found or already checked out.")

    def return_book(self, title):
        """Finds a book by title and marks it as returned."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned: {title}")
                return
        print(f"Error: '{title}' is not found or was never checked out.")

    def list_available_books(self):
        """Prints the title and author of all books currently available."""
        found_available = False
        for book in self._books:
            if book.is_available():
                print(str(book))
                found_available = True

        if not found_available:
            print("No books are currently available.")

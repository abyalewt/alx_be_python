class Book:
    """Base class for all books with common attributes (title, author)."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_details(self):
        """Returns the basic details of the book."""
        # Expected: Book: Pride and Prejudice by Jane Austen
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class for an electronic book, inheriting from Book."""

    def __init__(self, title, author, file_size):
        # Calls the parent class constructor
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self):
        """Overrides the base method to include file size details."""
        # Expected: EBook: Snow Crash by Neal Stephenson, File Size: 500
        # The comma and spacing must be exact.
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}"


class PrintBook(Book):
    """Derived class for a physical book, inheriting from Book."""

    def __init__(self, title, author, page_count):
        # Calls the parent class constructor
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self):
        """Overrides the base method to include page count details."""
        # Expected: PrintBook: The Catcher in the Rye by J.D. Salinger, Page Count: 234
        # The comma and spacing must be exact.
        return (
            f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
        )


class Library:
    """
    Implements Composition: The Library 'has-a' list of books.
    """

    def __init__(self):
        self.books = []  # Attribute must be named 'books'

    def add_book(self, book):
        """Adds any Book object to the library's collection."""
        self.books.append(book)

    def list_books(self):
        """Prints details of each book using polymorphism."""
        for book in self.books:
            # Crucial: Must print the result of calling the get_details() method
            print(book.get_details())

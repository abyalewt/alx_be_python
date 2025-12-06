class Book:
    """Base class for all books with common attributes (title, author)."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_details(self):
        """Returns the basic details of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class for an electronic book, inheriting from Book."""

    def __init__(self, title, author, file_size):
        # Calls the parent class constructor to initialize title and author
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self):
        """Overrides the base method to include file size details."""
        # Start with base details and append specific info, ensuring correct prefix
        base_details = super().get_details().replace("Book: ", "EBook: ")
        return f"{base_details}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class for a physical book, inheriting from Book."""

    def __init__(self, title, author, page_count):
        # Calls the parent class constructor to initialize title and author
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self):
        """Overrides the base method to include page count details."""
        # Start with base details and append specific info, ensuring correct prefix
        base_details = super().get_details().replace("Book: ", "PrintBook: ")
        return f"{base_details}, Page Count: {self.page_count}"


class Library:
    """
    Implements Composition: The Library 'has-a' list of books.
    """

    def __init__(self):
        self.books = []  # List to hold Book, EBook, and PrintBook instances

    def add_book(self, book):
        """Adds any Book object to the library's collection."""
        self.books.append(book)

    def list_books(self):
        """Prints details of each book using polymorphism."""
        for book in self.books:
            # Polymorphism: The correct get_details() method is called
            # based on the specific type of object (Book, EBook, or PrintBook).
            print(book.get_details())

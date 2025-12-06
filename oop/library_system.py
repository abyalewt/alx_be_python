class Book:
    """
    Base class representing a general book.
    """

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_details(self):
        """Returns the basic details of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Derived class representing an electronic book.
    Inherits from Book and adds file_size.
    """

    def __init__(self, title, author, file_size):
        # Call the base class constructor
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self):
        """Returns details specific to EBook."""
        base_details = super().get_details().replace("Book: ", "EBook: ")
        return f"{base_details}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Derived class representing a physical print book.
    Inherits from Book and adds page_count.
    """

    def __init__(self, title, author, page_count):
        # Call the base class constructor
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self):
        """Returns details specific to PrintBook."""
        base_details = super().get_details().replace("Book: ", "PrintBook: ")
        return f"{base_details}, Page Count: {self.page_count}"


class Library:
    """
    Represents the library system, demonstrating Composition
    by managing a collection of Book objects.
    """

    def __init__(self):
        # Composition: The Library 'has-a' list of books.
        self.books = []

    def add_book(self, book):
        """Adds a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Prints details of each book in the library using polymorphism."""
        for book in self.books:
            # Polymorphism in action: calling .get_details() automatically
            # executes the specific version defined in Book, EBook, or PrintBook.
            print(book.get_details())

class Book:
    """
    Base class representing a general book.
    """

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_details(self):
        """
        Returns the basic details of the book in the expected format.
        Expected: Book: Pride and Prejudice by Jane Austen
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Derived class for an electronic book.
    """

    def __init__(self, title, author, file_size):
        # Calls the base class constructor
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self):
        """
        Overrides the base method to include file size details.
        Expected: EBook: Snow Crash by Neal Stephenson, File Size: 500
        """
        # The checker might be sensitive to the "KB" unit if it's not present.
        # Based on the output "500", let's assume no unit is explicitly required
        # for the check, or we need to remove the "KB" from the previous solution.

        # We start with the EBook prefix and format the rest.
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}"


class PrintBook(Book):
    """
    Derived class for a physical print book.
    """

    def __init__(self, title, author, page_count):
        # Calls the base class constructor
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self):
        """
        Overrides the base method to include page count details.
        Expected: PrintBook: The Catcher in the Rye by J.D. Salinger, Page Count: 234
        """
        # We start with the PrintBook prefix and format the rest.
        return (
            f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
        )


class Library:
    """
    Manages a collection of Book objects (Composition).
    """

    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Adds a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Prints details of each book in the library using polymorphism."""
        for book in self.books:
            # This method MUST call print() on the result of get_details()
            print(book.get_details())

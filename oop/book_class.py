class Book:
    """
    A class representing a book, demonstrating Python magic methods
    for initialization, deletion, and string representation.
    """

    # --- Constructor Method ---
    def __init__(self, title, author, year):
        """Initializes a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    # --- Destructor Method ---
    def __del__(self):
        """Prints a message when the object is deleted."""
        print(f"Deleting {self.title}")

    # --- Informal String Representation Method (__str__) ---
    def __str__(self):
        """Returns a user-friendly, informal string representation."""
        # Format: (title) by (author), published in (year)
        return f"{self.title} by {self.author}, published in {self.year}"

    # --- Official String Representation Method (__repr__) ---
    def __repr__(self):
        """Returns an unambiguous string that can recreate the object."""
        # Format: Book('title', 'author', year)
        return f"Book('{self.title}', '{self.author}', {self.year})"


# Note: The main execution logic is expected to be in a separate main.py file.

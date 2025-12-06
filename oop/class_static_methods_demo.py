class Calculator:
    """
    A calculator class demonstrating the difference between static methods
    and class methods by performing basic arithmetic operations.
    """

    # Class Attribute: Accessible by class methods (via 'cls')
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static Method: Performs addition.
        Does not access class state (cls) or instance state (self).
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class Method: Performs multiplication.
        Accesses and prints a class attribute via the 'cls' parameter.
        """
        # Accessing the class attribute using the 'cls' parameter
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

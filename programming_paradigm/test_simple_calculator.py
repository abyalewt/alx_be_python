import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        # Create a fresh calculator object for every test method
        self.calc = SimpleCalculator()

    # --- Test Addition ---
    def test_addition(self):
        """Test the add method with positive, negative, and zero values."""
        # Normal positive addition
        self.assertEqual(self.calc.add(10, 5), 15)

        # Addition with negative numbers
        self.assertEqual(self.calc.add(-1, -1), -2)

        # Adding zero
        self.assertEqual(self.calc.add(0, 7), 7)

        # Addition resulting in zero
        self.assertEqual(self.calc.add(-5, 5), 0)

    # --- Test Subtraction ---
    def test_subtraction(self):
        """Test the subtract method with various combinations."""
        # Normal positive subtraction
        self.assertEqual(self.calc.subtract(10, 5), 5)

        # Subtraction resulting in negative
        self.assertEqual(self.calc.subtract(5, 10), -5)

        # Subtracting a negative number (e.g., 5 - (-2) = 7)
        self.assertEqual(self.calc.subtract(5, -2), 7)

        # Subtracting zero
        self.assertEqual(self.calc.subtract(8, 0), 8)

    # --- Test Multiplication ---
    def test_multiplication(self):
        """Test the multiply method with positive, negative, and zero values."""
        # Normal positive multiplication
        self.assertEqual(self.calc.multiply(4, 5), 20)

        # Multiplying by zero (edge case)
        self.assertEqual(self.calc.multiply(100, 0), 0)

        # Multiplication with negative numbers (negative * positive)
        self.assertEqual(self.calc.multiply(-5, 3), -15)

        # Multiplication with two negative numbers (negative * negative = positive)
        self.assertEqual(self.calc.multiply(-2, -4), 8)

    # --- Test Division ---
    def test_division(self):
        """Test the divide method with normal values and floating point results."""
        # Normal division resulting in a whole number
        self.assertEqual(self.calc.divide(10, 5), 2.0)

        # Division resulting in a float
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.3333333333333335)

        # Division of negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5.0)

    def test_division_by_zero(self):
        """Test the critical edge case: division by zero."""
        # The SimpleCalculator specification requires returning None on division by zero
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))


if __name__ == "__main__":
    unittest.main()

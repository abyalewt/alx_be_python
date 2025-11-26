def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Attempt the division
        result = num / denom

        # If successful, return the result message
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # This runs if the user tries to divide by 0
        return "Error: Cannot divide by zero."

    except ValueError:
        # This runs if the user enters text (like "ten") instead of numbers
        return "Error: Please enter numeric values only."

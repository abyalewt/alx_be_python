# temp_conversion_tool.py

# 🌍 Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global factor.
    Formula: (F - 32) * (5/9)
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global factor.
    Formula: (C * (9/5)) + 32
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    try:
        # Ask the user for a temperature
        temp_input = input("Enter the temperature to convert: ")

        # Validate numeric input
        if not temp_input.replace(".", "", 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        temperature = float(temp_input)

        # Ask the user for the unit
        unit = (
            input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
            .strip()
            .upper()
        )

        if unit == "F":
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result}°C")
        elif unit == "C":
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")
        else:
            print("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()

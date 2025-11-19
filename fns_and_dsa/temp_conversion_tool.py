# explore_datetime.py

from datetime import datetime, timedelta


def display_current_datetime():
    """
    Obtains and displays the current date and time in "YYYY-MM-DD HH:MM:SS" format.
    """
    # Part 1: Display the Current Date and Time

    # Get the current date and time object
    current_date = datetime.now()

    # Format the datetime object into the specified string format
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print(f"Current date and time: {formatted_date}")

    # Return the datetime object for potential further use in main()
    return current_date


def calculate_future_date(current_date):
    """
    Prompts the user for a number of days, calculates the future date,
    and displays it in "YYYY-MM-DD" format.

    Parameters:
        current_date (datetime.datetime): The starting date/time object.
    """
    # Part 2: Calculate a Future Date

    while True:
        try:
            # Prompt the user for the number of days
            days_to_add = int(
                input("Enter the number of days to add to the current date: ")
            )
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Use timedelta to represent the duration
    time_difference = timedelta(days=days_to_add)

    # Calculate the future date by adding the timedelta
    future_date = current_date + time_difference

    # Format the future date to show only the date part
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    print(f"Future date: {formatted_future_date}")

    # Return the future datetime object
    return future_date


def main():
    # Execute Part 1 and store the result
    initial_date = display_current_datetime()

    # Execute Part 2 using the date/time returned from Part 1
    calculate_future_date(initial_date)


if __name__ == "__main__":
    main()

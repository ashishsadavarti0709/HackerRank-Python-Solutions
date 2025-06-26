# Name: Ashish Sadavarti
# Code: Calendar Module Date Finder
# Code Description: Takes a date as input and determines the corresponding day of the week.
# Copyright 2025

# This script uses Python's built-in `calendar` module to find the day of the week
# for a given date. The date is expected in 'MM DD YYYY' format.

import calendar # Import the calendar module, which provides functions for calendar-related tasks.

if __name__ == '__main__':
    try:
        # Prompt the user to enter the date in the specified format.
        # .strip() removes any leading or trailing whitespace from the input string.
        date_input = input("Enter the date in 'MM DD YYYY' format (e.g., '08 14 2024'): ").strip()
        
        # Split the input string by spaces and convert each part to an integer.
        # This unpacks the values directly into month, day, and year variables.
        month_str, day_str, year_str = date_input.split()
        month = int(month_str)
        day = int(day_str)
        year = int(year_str)

        # Use the calendar.weekday() function to get the day of the week.
        # This function returns an integer where Monday is 0, Tuesday is 1, ..., Sunday is 6.
        # calendar.weekday(year, month, day)
        day_of_week_index = calendar.weekday(year, month, day)

        # Define a list of day names corresponding to the integer indices returned by calendar.weekday().
        days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

        # Print the day of the week using the calculated index to access the 'days' list.
        print(days[day_of_week_index])

    except ValueError:
        # Handle cases where the input is not in the correct format or not valid integers.
        print("Invalid input format or values. Please ensure the date is in 'MM DD YYYY' format and contains valid numbers.")
    except IndexError:
        # This might occur if date_input.split() doesn't produce exactly 3 parts.
        print("Input error: Please provide month, day, and year separated by spaces.")
    except Exception as e:
        # Catch any other unexpected errors.
        print(f"An unexpected error occurred: {e}")


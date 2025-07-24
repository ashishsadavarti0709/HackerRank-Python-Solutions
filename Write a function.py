# Name: Ashish Sadavarti
# Code: LeapYearChecker
# Code Description: Implements a function to determine if a given year is a leap year
#                   according to the Gregorian calendar rules.
# Copyright 2025

def is_leap(year):
    """
    Determines if a given year is a leap year according to the Gregorian calendar rules.

    Leap year rules:
    1. A year is a leap year if it is evenly divisible by 400.
    2. Otherwise, if it is evenly divisible by 100, it is NOT a leap year.
    3. Otherwise, if it is evenly divisible by 4, it IS a leap year.
    4. Otherwise (not divisible by 4), it is NOT a leap year.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    # Rule 1: Divisible by 400 (e.g., 2000, 2400 are leap years)
    if (year % 400 == 0):
        return True
    
    # Rule 2: Divisible by 100 but NOT by 400 (e.g., 1900, 2100 are NOT leap years)
    # This 'elif' ensures that if it's divisible by 400 (caught by the first if),
    # this condition is skipped.
    elif (year % 100 == 0):
        return False
    
    # Rule 3: Divisible by 4 but NOT by 100 (e.g., 2004, 2008 are leap years)
    # This 'elif' ensures that if it was caught by the 400 or 100 rule, this is skipped.
    elif (year % 4 == 0):
        return True
    
    # Rule 4: Not divisible by 4 (e.g., 2001, 2003 are NOT leap years)
    else:
        return False

if __name__ == '__main__':
    # Read the year from user input.
    year = int(input())
    
    # Call the is_leap function and print its boolean result.
    print(is_leap(year))

    # Example Test Cases:
    # Input: 1990
    # Expected: False (not divisible by 4)

    # Input: 1992
    # Expected: True (divisible by 4, not by 100)

    # Input: 1900
    # Expected: False (divisible by 100, but not by 400)

    # Input: 2000
    # Expected: True (divisible by 400)

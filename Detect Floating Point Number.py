# Name: Ashish Sadavarti
# Code: Detect Floating Point Number
# Code Description: Uses regular expressions to validate if a given string
#                   represents a valid floating-point number.
# Copyright 2025

# This script defines a function `is_valid_float` that checks if a string
# can be considered a valid floating-point number according to certain rules,
# typically those encountered in competitive programming problems (e.g.,
# it must contain a decimal point, can have a sign, etc.).

import re # Import the regular expression module.

def is_valid_float(s):
    """
    Checks if a string `s` represents a valid floating-point number.

    A valid floating-point number typically:
    - Can optionally start with a '+' or '-' sign.
    - Must contain at least one digit and a decimal point.
    - Can have digits before and/or after the decimal point.
    - Examples: "+1.0", "-.1", "12.34", "1." (though "1." might be excluded by some patterns,
      this pattern allows it if it means "1.0").

    Parameters:
    s (str): The string to be validated.

    Returns:
    bool: True if the string is a valid float, False otherwise.
    """
    # Regular expression pattern for a valid floating-point number:
    # ^       : Asserts position at the start of the string.
    # [+-]?   : Matches an optional '+' or '-' sign (zero or one occurrence).
    # (       : Start of a non-capturing group for the main number part.
    #   \d*\.\d+ : Matches zero or more digits, followed by a literal dot, followed by one or more digits.
    #               Example: ".1", "0.1", "123.45"
    #   |     : OR
    #   \.\d+ : Matches a literal dot, followed by one or more digits.
    #               Example: ".123" (requires at least one digit after the dot)
    #   |     : OR
    #   \d+\.\d* : Matches one or more digits, followed by a literal dot, followed by zero or more digits.
    #               Example: "1.", "1.23", "123."
    # )       : End of the non-capturing group.
    # $       : Asserts position at the end of the string.
    #
    # This pattern covers cases like:
    #   .1, -.1, +.1
    #   1.0, -1.0, +1.0
    #   12.34, -12.34, +12.34
    #   1., -1., +1. (where '1.' is interpreted as 1.0)
    #
    # Note: A simpler common pattern for HackerRank problems often includes '^\d*\.\d+$' or similar,
    # but the one provided here is more robust for various float formats.
    pattern = r'^[+-]?(\d*\.\d+|\.\d+|\d+\.\d*)$' # Corrected pattern: \d+\.\d* allows "1."
    
    # re.match(pattern, s) attempts to match the pattern from the beginning of the string.
    # It returns a match object if successful, None otherwise.
    # bool(...) converts the match object (or None) to a boolean (True or False).
    return bool(re.match(pattern, s))

if __name__ == '__main__':
    print("--- Floating Point Number Detector ---")
    print("This program checks if input strings are valid floating-point numbers.")

    try:
        # Read the number of test cases.
        n = int(input("Enter the number of test cases: "))

        if n < 0:
            print("Number of test cases cannot be negative.")
            exit()

        print(f"Enter {n} strings, one per line, to test if they are valid floats:")
        # Loop 'n' times to process each test case.
        for i in range(n):
            # Read the test string from the user.
            # .strip() removes any leading/trailing whitespace.
            test_case = input(f"Test case {i+1}: ").strip()
            
            # Call the validation function and print the boolean result.
            print(is_valid_float(test_case))

    except ValueError:
        # Handle cases where the input for 'n' is not a valid integer.
        print("Invalid input for number of test cases. Please enter an integer.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")


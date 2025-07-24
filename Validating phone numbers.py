# Name: Ashish Sadavarti
# Code: PhoneNumberValidator
# Code Description: Validates Indian mobile phone numbers based on specific rules:
#                   1. Must start with 7, 8, or 9.
#                   2. Must be exactly 10 digits long.
#                   It uses a regular expression for validation.
# Copyright 2025

import re # Import the regular expression module

if __name__ == '__main__':
    # Define the regular expression pattern for validating phone numbers.
    # ^: Asserts the start of the string.
    # [789]: Matches a single digit that is either 7, 8, or 9. This specifies
    #        the valid starting digits for an Indian mobile number.
    # \d{9}: Matches exactly 9 digits (0-9). Combined with the first digit,
    #        this ensures the total length is 10 digits.
    # $: Asserts the end of the string.
    # This pattern ensures the number is exactly 10 digits long and starts correctly.
    regex_pattern = r'^[789]\d{9}$'

    # Read the number of phone numbers to validate.
    n = int(input())

    # Loop 'n' times to process each phone number.
    for _ in range(n):
        # Read a phone number string from the user.
        # .strip() removes any leading/trailing whitespace.
        number = input().strip()
        
        # Use re.match() to check if the entire 'number' string matches the 'regex_pattern'
        # from the beginning.
        # re.match() returns a Match object if a match is found at the beginning of the string,
        # otherwise it returns None.
        if re.match(regex_pattern, number):
            # If the number matches the pattern, it is considered valid.
            print("YES")
        else:
            # If the number does not match the pattern, it is considered invalid.
            print("NO")

    # Example Usage:
    # Input:
    # 5
    # 9999999999
    # 999999999
    # 8795462130
    # 919875641230
    # 1234567890

    # Expected Output:
    # YES (9999999999 - valid)
    # NO (999999999 - too short)
    # YES (8795462130 - valid)
    # NO (919875641230 - too long)
    # NO (1234567890 - starts with 1, not 7, 8, or 9)

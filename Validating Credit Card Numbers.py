# Name: Ashish Sadavarti
# Code: CreditCardValidator
# Code Description: Validates credit card numbers based on a set of rules:
#                   1. Starts with 4, 5, or 6.
#                   2. Is exactly 16 digits long OR 16 digits separated by hyphens
#                      in groups of four (e.g., XXXX-XXXX-XXXX-XXXX).
#                   3. Must only consist of digits and hyphens (if present).
#                   4. Must not have 4 or more consecutive repeated digits (e.g., 1111, 2222).
# Copyright 2025

import re

def validate_credit_card(credit_number_string):
    """
    Validates a credit card number string based on specific rules.

    Args:
        credit_number_string (str): The potential credit card number as a string.

    Returns:
        str: "Valid" if the credit card number meets all criteria, "Invalid" otherwise.
    """
    # Rule 1 & 2: Check for valid length and starting digit, and optional hyphen format.
    # regex for 16 digits: ^[4-6]\d{15}$
    #   - ^[4-6]: Starts with a digit 4, 5, or 6.
    #   - \d{15}: Followed by exactly 15 digits.
    #   - $: Ends the string.
    is_length_16_digits = bool(re.match(r'^[4-6]\d{15}$', credit_number_string))

    # regex for 19 characters (16 digits + 3 hyphens): ^[4-6]\d{3}-\d{4}-\d{4}-\d{4}$
    #   - ^[4-6]: Starts with 4, 5, or 6.
    #   - \d{3}-: Followed by 3 digits and a hyphen.
    #   - \d{4}-: Followed by 4 digits and a hyphen (repeated twice).
    #   - \d{4}$: Followed by 4 digits and ends the string.
    is_length_19_hyphens = bool(re.match(r'^[4-6]\d{3}-\d{4}-\d{4}-\d{4}$', credit_number_string))

    # Determine if the credit card number adheres to one of the two valid formats.
    is_valid_format = is_length_16_digits or is_length_19_hyphens

    # Rule 3: Ensure no 4 or more consecutive repeated digits.
    # First, remove all hyphens to get a purely digit string for this check.
    credit_digits_only = credit_number_string.replace('-', '')

    # regex to find 4 or more consecutive repeating digits: r'(\d)\1\1\1'
    #   - (\d): Captures any digit (e.g., '1').
    #   - \1\1\1: Matches three more occurrences of the *same* captured digit.
    #             So, it looks for patterns like '1111', '2222', etc.
    # re.search(): Returns a Match object if the pattern is found anywhere in the string, else None.
    # bool(...): Converts the Match object (or None) to True/False.
    has_four_consecutive_repeats = bool(re.search(r'(\d)\1\1\1', credit_digits_only))

    # Final validation logic:
    # A credit card is "Valid" if it matches one of the accepted formats
    # AND it does NOT contain any four or more consecutive repeating digits.
    if is_valid_format and not has_four_consecutive_repeats:
        return 'Valid'
    else:
        return 'Invalid'

if __name__ == '__main__':
    # Read the number of credit card numbers to validate.
    n = int(input())

    # Process each credit card number.
    for _ in range(n):
        # Read the credit card number string for the current test case.
        credit_input = input().strip()
        
        # Call the validation function and print its result.
        print(validate_credit_card(credit_input))

    # Example Test Cases:
    # Input:
    # 6
    # 4123456789123456
    # 5123-4567-8912-3456
    # 61234-567-8912-3456
    # 41234567891234567
    # 4123-4567-8912-3456-7890
    # 4123456789123456
    # 5123-4444-4444-3456
    # 4123-4567-8912-3456

    # Expected Output:
    # Valid (4123456789123456)
    # Valid (5123-4567-8912-3456)
    # Invalid (61234-567-8912-3456 - incorrect hyphen placement/length)
    # Invalid (41234567891234567 - incorrect length)
    # Invalid (4123-4567-8912-3456-7890 - incorrect hyphen count/length)
    # Valid (4123456789123456 - no 4 consecutive repeats)
    # Invalid (5123-4444-4444-3456 - has 4 consecutive repeats)
    # Valid (4123-4567-8912-3456)

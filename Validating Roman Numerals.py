# Name: Ashish Sadavarti
# Code: RomanNumberValidator
# Code Description: Validates if a given string is a valid Roman numeral
#                   using a regular expression that covers numbers from 1 to 3999.
# Copyright 2025

import re

# Define the regular expression pattern for validating Roman numerals.
# This pattern is designed to validate numbers from 1 to 3999.
# It breaks down the Roman numeral into thousands, hundreds, tens, and units places,
# validating each part independently.
#
# ^: Asserts the start of the string.
#
# (M{0,3}): Validates the thousands place.
#   - M: Matches the Roman numeral for 1000.
#   - {0,3}: Allows 0 to 3 occurrences of 'M' (i.e., "", "M", "MM", "MMM").
#            This covers 0 to 3000.
#
# (CM|CD|D?C{0,3}): Validates the hundreds place.
#   - CM: Matches 900 (special case).
#   - |: OR operator.
#   - CD: Matches 400 (special case).
#   - |: OR operator.
#   - D?C{0,3}: Matches 500 to 800 or 0 to 300.
#     - D?: Allows an optional 'D' (500).
#     - C{0,3}: Allows 0 to 3 'C's (100, 200, 300).
#     This combination covers "D", "DC", "DCC", "DCCC", and "C", "CC", "CCC", "".
#
# (XC|XL|L?X{0,3}): Validates the tens place. (Similar logic to hundreds)
#   - XC: Matches 90 (special case).
#   - |: OR operator.
#   - XL: Matches 40 (special case).
#   - |: OR operator.
#   - L?X{0,3}: Matches 50 to 80 or 0 to 30.
#     - L?: Allows an optional 'L' (50).
#     - X{0,3}: Allows 0 to 3 'X's (10, 20, 30).
#
# (IX|IV|V?I{0,3}): Validates the units place. (Similar logic to hundreds/tens)
#   - IX: Matches 9 (special case).
#   - |: OR operator.
#   - IV: Matches 4 (special case).
#   - |: OR operator.
#   - V?I{0,3}: Matches 5 to 8 or 0 to 3.
#     - V?: Allows an optional 'V' (5).
#     - I{0,3}: Allows 0 to 3 'I's (1, 2, 3).
#
# $: Asserts the end of the string.
regex_pattern = r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

if __name__ == '__main__':
    # Read the string to be validated as a Roman numeral.
    roman_numeral = input("Enter a Roman numeral string: ")

    # Use re.match() to check if the entire string matches the regex_pattern from the beginning.
    # re.match() returns a Match object if successful, None otherwise.
    # The bool() conversion simplifies checking for a match.
    is_valid = bool(re.match(regex_pattern, roman_numeral))

    # Print "True" if the Roman numeral is valid, "False" otherwise.
    print(is_valid)

    # Example Test Cases:
    # Input: IV -> Output: True
    # Input: VII -> Output: True
    # Input: MCMXCIV -> Output: True (1994)
    # Input: MMMCMXCIX -> Output: True (3999)
    # Input: IIII -> Output: False (invalid repetition)
    # Input: IM -> Output: False (invalid order)
    # Input: CMXCVC -> Output: False (invalid structure)
    # Input: MMMM -> Output: False (exceeds 3999)

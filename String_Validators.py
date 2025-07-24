# Name: Ashish Sadavarti
# Code: StringValidationChecks
# Code Description: Demonstrates various string validation methods in Python
#                   using the any() built-in function to check for the presence
#                   of specific character types in an input string.
# Copyright 2025

if __name__ == '__main__':
    # Read the input string from the user.
    s = input()

    # Check if the string contains any alphanumeric characters.
    # c.isalnum(): Returns True if character 'c' is an alphabet letter (a-z, A-Z)
    #              or a digit (0-9).
    # any(... for c in s): Returns True if at least one character 'c' in the string 's'
    #                      satisfies the condition (i.e., is alphanumeric).
    print(any(c.isalnum() for c in s))

    # Check if the string contains any alphabetic characters.
    # c.isalpha(): Returns True if character 'c' is an alphabet letter (a-z, A-Z).
    #              It returns False for digits, spaces, and special characters.
    print(any(c.isalpha() for c in s))

    # Check if the string contains any digit characters.
    # c.isdigit(): Returns True if character 'c' is a digit (0-9).
    print(any(c.isdigit() for c in s))

    # Check if the string contains any lowercase alphabetic characters.
    # c.islower(): Returns True if character 'c' is a lowercase alphabet letter.
    #              Returns False for uppercase letters, digits, and non-alphabetic characters.
    print(any(c.islower() for c in s))

    # Check if the string contains any uppercase alphabetic characters.
    # c.isupper(): Returns True if character 'c' is an uppercase alphabet letter.
    #              Returns False for lowercase letters, digits, and non-alphabetic characters.
    print(any(c.isupper() for c in s))

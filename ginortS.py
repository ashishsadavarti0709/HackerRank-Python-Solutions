# Name: Ashish Sadavarti
# Code: ginortS String Sorter
# Code Description: Sorts a string based on specific criteria: lowercase letters,
#                   uppercase letters, odd digits, and even digits, with
#                   sub-sorting alphabetically/numerically.
# Copyright 2025

# This script implements a custom sorting logic for a given string.
# The sorting order is defined by a complex key function:
# 1. Lowercase letters come first (sorted alphabetically).
# 2. Uppercase letters come next (sorted alphabetically).
# 3. Odd digits come after uppercase letters (sorted numerically).
# 4. Even digits come last (sorted numerically).

if __name__ == '__main__':
    print("--- ginortS String Sorter ---")
    
    try:
        # Read the input string from the user.
        # .strip() removes any leading or trailing whitespace.
        s = input("Enter a string (e.g., 'Sorting1234'): ").strip()

        # Handle empty string case
        if not s:
            print("Input string is empty. Nothing to sort.")
            print("") # Print empty line as output, typical for HackerRank
            exit()

        # Sort the string `s` using a custom `key` function.
        # The `key` function returns a tuple for each character `x`.
        # Python's `sorted()` function sorts tuples lexicographically (element by element).
        # This creates a multi-level sort order:

        # Logic for the key tuple `(x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x)`:

        # First level of sorting (x.isdigit()):
        # - `x.isdigit()`: Returns False for letters, True for digits.
        #   Since False < True, all letters will come before all digits.

        # Second level of sorting (if x.isdigit() is True, i.e., it's a digit):
        # - `x.isdigit() and int(x) % 2 == 0`: This part is evaluated only if x is a digit.
        #   - If x is an odd digit (e.g., '1', '3'): `int(x) % 2 == 0` is False.
        #   - If x is an even digit (e.g., '2', '4'): `int(x) % 2 == 0` is True.
        #   Since False < True, odd digits will come before even digits.

        # Third level of sorting (if x is a letter):
        # - `x.isupper()`: Returns False for lowercase letters, True for uppercase letters.
        #   Since False < True, lowercase letters will come before uppercase letters.
        #   (This is the third element in the tuple for characters that are NOT digits).

        # Fourth level of sorting (the character itself 'x'):
        # - `x`: For elements that are equal in all prior sorting levels (e.g., same type, same odd/even status),
        #   they are then sorted by their ASCII/Unicode value.
        #   This means lowercase letters are sorted alphabetically (a-z),
        #   uppercase letters are sorted alphabetically (A-Z),
        #   odd digits are sorted numerically (1, 3, 5, ...),
        #   and even digits are sorted numerically (0, 2, 4, ...).

        sorted_characters = sorted(s, key=lambda x: (
            x.isdigit(),                    # False for letters (comes first), True for digits (comes later)
            x.isdigit() and int(x) % 2 == 0, # Among digits: False for odd (comes first), True for even (comes later)
            x.isupper(),                    # Among letters: False for lowercase (comes first), True for uppercase (comes later)
            x                               # Finally, sort by the character itself (alphabetical/numerical)
        ))

        # Join the sorted characters back into a single string.
        result_string = ''.join(sorted_characters)
        
        # Print the sorted string.
        print(result_string)

    except ValueError:
        # This might occur if int(x) is called on a non-digit character,
        # though the key logic for x.isdigit() should prevent this.
        print("Error: Input string contains non-digit characters where digit conversion was attempted.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")


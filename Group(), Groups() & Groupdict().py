# Name: Ashish Sadavarti
# Code: Regex Group(), Groups(), & Groupdict() Demo
# Code Description: Demonstrates finding the first occurrence of a character or digit
#                   that immediately repeats in a string using regular expressions,
#                   and showcases `group()`, `groups()`, and `groupdict()`.
# Copyright 2025

# This script utilizes Python's `re` module to find patterns in a string.
# Specifically, it looks for any alphanumeric character (a-z, A-Z, 0-9) that
# is immediately followed by one or more occurrences of itself.
# It then prints the repeating character using `match.group(1)`.
# If no such repetition is found, it prints -1.
# It also includes commented examples to illustrate `groups()` and `groupdict()`.

import re # Import the regular expression module.

if __name__ == '__main__':
    print("--- Regex Group(), Groups(), & Groupdict() Demo ---")
    
    try:
        # Read the input string from the user.
        s = input("Enter a string (e.g., 'abccdeefghhhiii12234'): ")

        # Regular expression pattern:
        # r'([a-zA-Z0-9])\1+'
        # - `[a-zA-Z0-9]`: Matches any single alphanumeric character.
        # - `()`: This creates a capturing group. The character matched by `[a-zA-Z0-9]`
        #         will be captured in group 1.
        # - `\1`: This is a backreference. It matches exactly the same text that was
        #         captured by the first capturing group.
        # - `+`: Matches one or more occurrences of the preceding character (which is `\1` here).
        # So, the pattern looks for an alphanumeric character followed by one or more
        # repetitions of *that exact same character*.
        
        # re.search(pattern, string)
        # - Searches for the first location where the regular expression pattern produces a match.
        # - Returns a match object if successful, None otherwise.
        match = re.search(r'([a-zA-Z0-9])\1+', s)

        # Check if a match was found.
        if match:
            # `match.group(0)` or `match.group()`: Returns the entire matched string (e.g., "cc" for "abccde").
            # `match.group(1)`: Returns the content of the first capturing group (e.g., "c" for "abccde").
            # This is what the problem typically asks for: the repeating character itself.
            print(match.group(1))

            # --- Additional Demonstrations for Groups() and Groupdict() ---
            # These are commented out as they are not part of the problem's direct output,
            # but illustrate the usage of other methods.

            # print(f"Full match: {match.group(0)}") # Prints the entire matched substring (e.g., 'cc')
            # print(f"Captured groups (tuple): {match.groups()}") # Prints a tuple of captured groups (e.g., ('c',))

            # If the pattern had named groups (e.g., r'(?P<char>[a-zA-Z0-9])(?P=char)+'):
            # named_match = re.search(r'(?P<char>[a-zA-Z0-9])(?P=char)+', s)
            # if named_match:
            #     print(f"Captured named groups (dict): {named_match.groupdict()}") # Prints a dictionary {'char': 'c'}

        else:
            # If no match is found, print -1.
            print(-1)

    except Exception as e:
        # Catch any unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")


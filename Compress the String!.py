# Name: Ashish Sadavarti
# Code: Compress the String
# Code Description: Compresses a string by grouping consecutive identical characters
#                   and representing them as (count, character) pairs.
# Copyright 2025

# This script takes a string composed of digits as input and compresses it
# by identifying consecutive runs of the same character. For each run,
# it outputs a tuple (count, character), where 'count' is the number of
# consecutive occurrences and 'character' is the digit itself.
# The `itertools.groupby` function is crucial for this task.

from itertools import groupby # Import the groupby function from the itertools module.

if __name__ == '__main__':
    try:
        # Read the input string from the user.
        # .strip() removes any leading or trailing whitespace.
        # It's assumed the input string will contain only digits as per common problem constraints.
        s = input("Enter a string of digits (e.g., '1222311'): ").strip()

        # Handle empty string case
        if not s:
            print("Input string is empty. No compression to perform.")
            # Print an empty line as output, matching typical HackerRank behavior for empty input
            print("")
            exit()

        # Use itertools.groupby() to group consecutive identical characters.
        # groupby(s) returns an iterator that yields (key, group) pairs.
        # 'key' (k) is the character itself.
        # 'group' (g) is an iterator over the consecutive occurrences of that character.
        # For example, for "1222311":
        # 1st group: k='1', g=['1']
        # 2nd group: k='2', g=['2', '2', '2']
        # 3rd group: k='3', g=['3']
        # 4th group: k='1', g=['1', '1']

        # The list comprehension then processes each (k, g) pair:
        # len(list(g)): Converts the group iterator 'g' to a list and gets its length (count).
        # int(k): Converts the character key 'k' (which is a string digit) to an integer.
        # The result is a list of tuples, e.g., [(1, 1), (3, 2), (1, 3), (2, 1)] for "1222311".
        compressed_data = [(len(list(g)), int(k)) for k, g in groupby(s)]

        # Format the compressed data into the desired output string.
        # ' '.join(...) joins the formatted tuples with a space.
        # f'({count}, {char})' uses an f-string to format each (count, char) tuple as "(count, char)".
        output_string = ' '.join(f'({count}, {char})' for count, char in compressed_data)

        # Print the final compressed string.
        print(output_string)

    except ValueError:
        # Catch errors if the input string contains non-digit characters
        # that cannot be converted to int(k).
        print("Invalid input. Please ensure the string contains only digits.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")


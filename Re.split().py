# Name: Ashish Sadavarti
# Code: RegexSplit
# Code Description: Demonstrates the use of re.split() to split a string
#                   by commas (,) or periods (.).
# Copyright 2025

import re

if __name__ == '__main__':
    # Define the regular expression pattern for splitting.
    # r"[,.]" means:
    # r'' : Raw string literal, prevents backslashes from being interpreted as escape sequences.
    # []  : Defines a character set.
    # ,.  : Matches either a comma (,) or a period (.).
    regex_pattern = r"[,.]"

    # Read the input string from the user.
    # Example input: "This,is.a,test.string"
    s = input("Enter a string to split (e.g., 'Hello,World.How,are.you?'): ")

    # Use re.split() to split the string 's' wherever the 'regex_pattern' is found.
    # re.split(pattern, string):
    #   - Splits the string by occurrences of the pattern.
    #   - Returns a list of strings resulting from the splits.
    #   - Empty strings might appear in the list if delimiters are consecutive
    #     or at the beginning/end of the string (depending on exact pattern).
    split_parts = re.split(regex_pattern, s)

    print("\nSplit parts:")
    # Iterate through the list of split parts and print each one.
    # The filter(None, ...) part is used to remove any empty strings
    # that might result from consecutive delimiters (e.g., "word,,another"
    # would produce an empty string between the two commas).
    for part in filter(None, split_parts):
        print(part)


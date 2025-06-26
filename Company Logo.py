# Name: Ashish Sadavarti
# Code: Company Logo Character Frequency Analyzer
# Code Description: Takes a string as input, counts character frequencies,
#                   sorts them by frequency (descending) and then alphabetically (ascending),
#                   and prints the top 3 most common characters with their counts.
# Copyright 2025

# This script is designed to find the top 3 most occurring characters in a given string.
# In case of a tie in frequency, characters are sorted alphabetically.
# It leverages Python's `collections.Counter` for efficient counting and
# `sorted()` with a custom `lambda` function for the specific sorting order.

import math   # Not used in this specific code.
import os     # Not used in this specific code.
import random # Not used in this specific code.
import re     # Not used in this specific code.
import sys    # Not used in this specific code directly, but implicit for input/output.
from collections import Counter # Import the Counter class for counting hashable objects.

if __name__ == '__main__':
    try:
        # Read the input string from the user.
        # .strip() removes any leading or trailing whitespace.
        s = input("Enter a string (e.g., 'aabbbccde'): ").strip()

        # Handle empty string case
        if not s:
            print("Input string is empty. No characters to count.")
            sys.exit(0) # Exit gracefully if string is empty

        # Create a Counter object from the input string.
        # This will count the occurrences of each character.
        # Example: Counter("aabbbccde") -> {'a': 2, 'b': 3, 'c': 2, 'd': 1, 'e': 1}
        counter = Counter(s)

        # Sort the items (character, count) from the Counter.
        # The 'key' argument is a lambda function that specifies the sorting criteria:
        # 1. `-x[1]`: Sorts by the count (x[1]) in descending order.
        #    By negating the count, we make higher counts appear first when sorting in ascending order.
        # 2. `x[0]`: If counts are tied (i.e., -x[1] values are equal),
        #    it then sorts by the character (x[0]) in ascending alphabetical order.
        # Example: {'a': 2, 'b': 3, 'c': 2} will be sorted as [('b', 3), ('a', 2), ('c', 2)]
        # because 'a' comes before 'c' alphabetically when counts (2) are tied.
        most_common = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

        # Iterate through the first 3 elements of the sorted list (top 3 most common characters).
        # If there are fewer than 3 unique characters, it will iterate through all available.
        print("\nTop 3 Most Common Characters:")
        for char, count in most_common[:3]:
            # Print the character and its count, space-separated.
            print(f"{char} {count}")

    except Exception as e:
        # Catch any unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")


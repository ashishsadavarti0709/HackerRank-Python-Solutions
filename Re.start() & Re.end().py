# Name: Ashish Sadavarti
# Code: RegexStartEndIndices
# Code Description: Demonstrates how to find all occurrences (including overlapping ones)
#                   of a substring 'k' within a string 's' using regex lookaheads,
#                   and print their start and end indices.
# Copyright 2025

import re

if __name__ == '__main__':
    # Read the main string 's' from standard input.
    # This is the string in which we will search for occurrences of 'k'.
    s = input()
    
    # Read the substring 'k' from standard input.
    # This is the pattern we are looking for within 's'.
    k = input()

    # Compile a regular expression pattern using a positive lookahead.
    # (?=...) is a positive lookahead assertion. It asserts that the pattern inside
    # the lookahead must match, but it *does not consume* any characters.
    # This is essential here because it allows us to find overlapping matches.
    # For example, if s = "ababab" and k = "aba", a simple re.finditer("aba", s)
    # would only find the first "aba". Using (?=aba) allows finding both "aba" at index 0
    # and "aba" at index 2 (even though the first "aba" conceptually "overlaps" with it).
    # The f-string dynamically inserts the value of 'k' into the regex pattern.
    pattern = re.compile(f"(?={k})")

    # Use pattern.finditer(s) to get an iterator of MatchObject instances.
    # Each MatchObject represents a single match found by the pattern.
    # Convert the iterator to a list for easier checking of emptiness.
    matches = list(pattern.finditer(s))

    # Check if any matches were found.
    if not matches:
        # If no matches are found, print (-1, -1) as per the requirement.
        print((-1, -1))
    else:
        # Iterate through each MatchObject found.
        for match in matches:
            # match.start() returns the starting index of the match.
            # Because we used a positive lookahead (?=k), match.start() will be
            # the index where 'k' *begins* in the string 's'.
            start_index = match.start()
            
            # Calculate the end index.
            # The end index is the starting index plus the length of 'k' minus 1
            # (because indices are zero-based).
            end_index = start_index + len(k) - 1
            
            # Print the (start_index, end_index) tuple for the current match.
            print((start_index, end_index))

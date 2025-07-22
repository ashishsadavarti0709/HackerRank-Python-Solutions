# Name: Ashish Sadavarti
# Code: RegexFindOperations
# Code Description: Demonstrates the use of re.findall() and re.finditer() to find
#                   sequences of 2 or more vowels flanked by consonants in a string.
# Copyright 2025

import re

if __name__ == '__main__':
    # Read the input string from STDIN.
    s = input()

    # Define the regular expression pattern.
    # Explanation of the pattern:
    # r'...' defines a raw string, which is good for regex to avoid backslash issues.
    # (?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])
    #   - This is a positive lookbehind assertion.
    #   - It asserts that the preceding character must be a consonant (case-insensitive).
    #   - It does NOT include the consonant in the match itself.
    # ([aeiouAEIOU]{2,})
    #   - This is the main capturing group.
    #   - It matches two or more (,{2,}) occurrences of a vowel (case-insensitive).
    # (?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])
    #   - This is a positive lookahead assertion.
    #   - It asserts that the following character must be a consonant (case-insensitive).
    #   - It does NOT include the consonant in the match itself.
    pattern = r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])([aeiouAEIOU]{2,})(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])'

    # --- Using re.findall() ---
    # re.findall() returns a list of all non-overlapping matches of the pattern in the string.
    # If the pattern contains capturing groups, it returns a list of tuples or strings
    # containing only the captured groups. In this case, since there's one capturing group
    # for the vowels, it returns a list of strings (the vowel sequences).
    print("--- Using re.findall() ---")
    matches_findall = re.findall(pattern, s)

    if matches_findall:
        for match in matches_findall:
            print(match)
    else:
        print("-1")

    print("\n--- Using re.finditer() ---")
    # --- Using re.finditer() ---
    # re.finditer() returns an iterator yielding MatchObject instances over all
    # non-overlapping matches for the pattern in the string.
    # Each MatchObject contains more information about the match, like its start and end indices.
    matches_finditer = re.finditer(pattern, s)

    found_finditer = False
    for match_obj in matches_finditer:
        # match_obj.group(0) or match_obj.group() returns the entire match.
        # Since our pattern uses lookarounds, group(0) will be the same as group(1)
        # (the captured vowel sequence), as the lookarounds are zero-width assertions.
        # match_obj.start() returns the starting index of the match.
        # match_obj.end() returns the ending index of the match.
        print(f"Match: {match_obj.group(1)}, Start: {match_obj.start()}, End: {match_obj.end()}")
        found_finditer = True
    
    if not found_finditer:
        print("-1")


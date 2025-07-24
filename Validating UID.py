# Name: Ashish Sadavarti
# Code: UIDValidator
# Code Description: Validates a user ID (UID) string based on a set of criteria
#                   including character types, unique characters, and length.
# Copyright 2025

import re

if __name__ == '__main__':
    # Read the number of UIDs to process from the user.
    for _ in range(int(input())):
        # Read the UID string, sort its characters alphabetically, and join them back.
        # Sorting helps in easily detecting duplicate characters using regex later.
        u = ''.join(sorted(input()))
        
        try:
            # Rule 1: It must contain at least 2 uppercase English alphabet characters.
            # re.search(r'[A-Z]{2}', u): Looks for any two consecutive uppercase letters.
            #   - [A-Z]: Matches any uppercase letter.
            #   - {2}: Matches exactly two occurrences of the preceding character set.
            # If re.search finds a match, it returns a Match object (truthy), otherwise None (falsy).
            # assert: If the condition is False, an AssertionError is raised.
            assert re.search(r'[A-Z]{2}', u)
            
            # Rule 2: It must contain at least 3 digits (0-9).
            # re.search(r'\d\d\d', u): Looks for any three consecutive digits.
            #   - \d: Matches any digit (0-9).
            #   - \d\d\d: Simply three consecutive \d (could also be written as \d{3}).
            assert re.search(r'\d\d\d', u)
            
            # Rule 3: It should only contain alphanumeric characters (a-z, A-Z, 0-9).
            # assert not re.search(r'[^a-zA-Z0-9]', u):
            #   - [^a-zA-Z0-9]: Matches any character that is *not* an alphanumeric character.
            #   - The 'not' checks that such a non-alphanumeric character is *not* found.
            # If any non-alphanumeric character is found, re.search returns a Match object,
            # 'not' makes it False, causing the assert to fail.
            assert not re.search(r'[^a-zA-Z0-9]', u)
            
            # Rule 4: No character should repeat.
            # (This rule is often interpreted as "no consecutive repeated characters"
            # or "no more than 10 unique characters". Given `sorted(input())` and `(.)\1`,
            # this check specifically targets *any* repeated characters because sorting
            # brings identical characters next to each other).
            # assert not re.search(r'(.)\1', u):
            #   - (.): Captures any single character (except newline). This is Group 1.
            #   - \1: Matches the content of Group 1 (the same character again).
            #   - This pattern looks for any character followed immediately by itself (e.g., 'aa', 'bb', '11').
            # Since the string 'u' is sorted, if any character repeats, they will be adjacent,
            # so this regex effectively checks for *any* duplicate characters in the original UID.
            assert not re.search(r'(.)\1', u)
            
            # Rule 5: It must be exactly 10 characters in length.
            # len(u) == 10: Checks if the length of the sorted string is 10.
            # Since sorting doesn't change length, this checks the original UID's length.
            assert len(u) == 10
        
        except AssertionError:
            # If any of the assert conditions fail, an AssertionError is caught here.
            # In that case, the UID is considered "Invalid".
            print('Invalid')
        else:
            # If all assert conditions pass (no AssertionError is raised),
            # the UID is considered "Valid".
            print('Valid')


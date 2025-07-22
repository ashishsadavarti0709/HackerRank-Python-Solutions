# Name: Ashish Sadavarti
# Code: RegexSubstitution
# Code Description: Replaces ' && ' with ' and ' and ' || ' with ' or ' in input lines,
#                   ensuring the replacements only occur when surrounded by spaces.
# Copyright 2025

import re

if __name__ == '__main__':
    # Read the number of lines 'n' that will be processed.
    n = int(input())

    # Loop 'n' times to process each line of input.
    for _ in range(n):
        # Read a single line of input from STDIN.
        line = input()

        # Perform the first substitution: replace ' && ' with ' and '.
        # r'(?<= )\&\&(?= )' is the regex pattern:
        #   - r'' : Raw string literal.
        #   - (?<= ) : Positive lookbehind assertion. It asserts that the match
        #             must be preceded by a space character (' ').
        #             The space itself is NOT part of the match.
        #   - \&\& : Matches the literal "&&". We use '\&' because '&' can have
        #           special meaning in some regex contexts, though not strictly
        #           necessary here, it's good practice for clarity.
        #   - (?= ) : Positive lookahead assertion. It asserts that the match
        #             must be followed by a space character (' ').
        #             The space itself is NOT part of the match.
        # This ensures that only " && " (with leading and trailing spaces) is replaced.
        modified_line = re.sub(r'(?<= )\&\&(?= )', 'and', line)
        
        # Perform the second substitution: replace ' || ' with ' or '.
        # This operates on the `modified_line` from the previous step.
        # r'(?<= )\|\|(?= )' is the regex pattern:
        #   - Similar lookbehind and lookahead for spaces.
        #   - \|\| : Matches the literal "||". The '|' character has special meaning
        #            in regex (OR operator), so it MUST be escaped with a backslash (`\`).
        # This ensures that only " || " (with leading and trailing spaces) is replaced.
        modified_line = re.sub(r'(?<= )\|\|(?= )', 'or', modified_line)
        
        # Print the modified line to STDOUT.
        print(modified_line)

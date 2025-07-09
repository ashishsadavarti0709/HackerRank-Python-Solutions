# Name: Ashish Sadavarti
# Code: Regex Syntax Validator
# Code Description: Checks if a given string is a syntactically valid regular expression.
#                   Includes specific checks for certain 'invalid' patterns (like '++')
#                   that might pass `re.compile` but are considered invalid by a problem.
# Copyright 2025

# This script helps validate regular expression syntax.
# It uses Python's `re.compile()` function, which attempts to compile a regex pattern.
# If the pattern has a syntax error, `re.compile()` raises an `re.error` exception.
# Additionally, it includes a specific check for patterns like '++', '*+', or '?+'
# which, while sometimes technically valid in specific regex engines (or might not
# immediately throw an `re.error` in `re.compile` depending on context), are
# often considered syntactically incorrect or problematic in common competitive
# programming challenges.

import re # Import the regular expression module.

if __name__ == '__main__':
    print("--- Regex Syntax Validator ---")
    print("Enter the number of test cases (regular expression strings).")
    print("For each, the program will determine if it's a valid regex.")

    try:
        # Read the number of test cases.
        num_test_cases = int(input("Enter the number of regex strings to test: "))

        if num_test_cases < 0:
            print("Number of test cases cannot be negative.")
            exit()

        print(f"\nEnter {num_test_cases} regex strings, one per line:")
        # Loop through each test case.
        for i in range(num_test_cases):
            S = input(f"Regex string {i+1}: ").strip() # Read the regex string and remove whitespace.
            
            is_valid = True # Assume valid initially.

            try:
                # Attempt to compile the regular expression.
                # If `re.compile()` succeeds, the basic syntax is generally correct.
                re.compile(S)
                
                # Additional specific checks as per common problem constraints:
                # Some problems define specific sequences as invalid even if `re.compile` doesn't strictly fail.
                # `++`, `*+`, `?+` are common examples of "invalid" patterns in such contexts.
                # These patterns are often invalid because they represent redundant or ambiguous quantifiers.
                if '++' in S or '*+' in S or '?+' in S:
                    is_valid = False # Considered invalid by this specific rule.

            except re.error:
                # If `re.compile()` raises an `re.error`, it means the regex syntax is fundamentally incorrect.
                is_valid = False # Set to False because of a regex compilation error.
            
            # Print the result (True if valid, False if invalid based on the checks).
            print(is_valid)

    except ValueError:
        # Handle cases where the input for `num_test_cases` is not an integer.
        print("Invalid input for number of test cases. Please enter an integer.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")


# Name: Ashish Sadavarti
# Code: itertools.combinations_with_replacement() Demo
# Code Description: Generates all unique combinations of a string's characters
#                   with replacement, sorted alphabetically, of a specified length.
#                   Utilizes `itertools.combinations_with_replacement`.
# Copyright 2025

# This script demonstrates the use of `itertools.combinations_with_replacement`.
# This function allows for combinations where elements can be repeated and
# the order of elements within a combination does not matter (e.g., 'AA' is
# the same as 'AA' if characters are sorted, and if 'A' is selected, it can be
# selected again). The input string's characters are first sorted to ensure
# the output combinations are also in lexicographical order.

from itertools import combinations_with_replacement # Import the function.

if __name__ == '__main__':
    print("--- itertools.combinations_with_replacement() Demo ---")
    print("This program generates combinations with replacement from a string.")

    try:
        # Read the input string 's' and the integer 'k' (length of combinations).
        # input().split() reads a line like "HACK 2" and splits into ['HACK', '2'].
        s_str, k_str = input("Enter a string and an integer K (e.g., 'HACK 2'): ").split()
        k = int(k_str) # Convert K to an integer.

        # Validate k
        if k < 0:
            print("Error: K must be a non-negative integer.")
            exit()
        
        # Sort the characters of the input string 's'.
        # This is crucial for ensuring that the combinations generated are in
        # lexicographical (alphabetical) order, as `combinations_with_replacement`
        # itself produces combinations in sorted order if the input iterable is sorted.
        # Example: s="BAC", sorted(s) -> ['A', 'B', 'C']
        s_sorted_chars = sorted(s_str)

        # Generate combinations with replacement.
        # `combinations_with_replacement(iterable, r)`:
        # - `iterable`: The collection from which to draw elements (e.g., ['A', 'B', 'C']).
        # - `r`: The length of the combinations (e.g., k=2).
        # Yields tuples like ('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), etc.
        
        print(f"\nCombinations of length {k} from '{s_str}' (with replacement, sorted):")
        for comb_tuple in combinations_with_replacement(s_sorted_chars, k):
            # Join the characters in each combination tuple to form a string.
            # Example: ('A', 'A') -> "AA"
            print(''.join(comb_tuple))

    except ValueError:
        # Handle cases where K is not a valid integer.
        print("Invalid input. Please ensure K is an integer.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")


# Name: Ashish Sadavarti
# Code: itertools.combinations() Demo
# Code Description: Generates all unique combinations of a string's characters
#                   (without replacement), for lengths from 1 up to a specified K,
#                   and prints them in lexicographical order.
#                   Utilizes `itertools.combinations`.
# Copyright 2025

# This script demonstrates the use of `itertools.combinations`.
# This function generates all unique combinations of elements from an iterable,
# where elements cannot be repeated within a single combination, and the order
# of elements within a combination does not matter. The input string's characters
# are sorted first to ensure the output combinations are also in lexicographical order.

from itertools import combinations # Import the combinations function.

if __name__ == '__main__':
    print("--- itertools.combinations() Demo ---")
    print("This program generates combinations of various lengths from a string.")

    try:
        # Read the input string 's' and the integer 'k' (maximum length of combinations).
        # input().split() reads a line like "HACK 2" and splits into ['HACK', '2'].
        s_str, k_str = input("Enter a string and an integer K (e.g., 'HACK 2'): ").split()
        k = int(k_str) # Convert K to an integer.

        # Validate k
        if k < 0:
            print("Error: K must be a non-negative integer.")
            exit()
        
        # Sort the characters of the input string 's'.
        # This is crucial for ensuring that the combinations generated are in
        # lexicographical (alphabetical) order, as `combinations`
        # itself produces combinations in sorted order if the input iterable is sorted.
        # Example: s="BAC", sorted(s_str) -> ['A', 'B', 'C']
        s_sorted_chars = sorted(s_str)

        print(f"\nGenerating combinations for '{s_str}' from length 1 to {k}:")
        # Iterate through possible combination lengths, from 1 up to 'k' (inclusive).
        for current_length in range(1, k + 1):
            # Generate combinations of `s_sorted_chars` of `current_length`.
            # `combinations(iterable, r)` yields tuples.
            # Example: for s_sorted_chars=['A','C'], current_length=2: ('A','C')
            for comb_tuple in combinations(s_sorted_chars, current_length):
                # Join the characters in each combination tuple to form a string.
                # Example: ('A', 'B') -> "AB"
                print(''.join(comb_tuple))

    except ValueError:
        # Handle cases where K is not a valid integer.
        print("Invalid input. Please ensure K is an integer.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")


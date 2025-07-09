# Name: Ashish Sadavarti
# Code: itertools.permutations() Demo
# Code Description: Generates all unique permutations of a string's characters
#                   of a specified length, sorted alphabetically,
#                   and prints them in lexicographical order.
#                   Utilizes `itertools.permutations`.
# Copyright 2025

# This script demonstrates the use of `itertools.permutations`.
# This function generates all possible ordered arrangements (permutations)
# of a specified length from elements of an iterable. Unlike combinations,
# the order of elements *does* matter in permutations (e.g., 'AB' is different from 'BA').
# The input string's characters are first sorted to ensure the output permutations
# are also in lexicographical order.

from itertools import permutations # Import the permutations function.

def generate_permutations(s_raw, k):
    """
    Generates and prints all unique permutations of characters from a string
    of a specified length 'k', in lexicographical order.

    Parameters:
    s_raw (str): The input string from which to generate permutations.
    k (int): The length of each permutation.
    """
    # Convert the input string into a list of characters and sort it.
    # Sorting the input iterable is crucial for `itertools.permutations`
    # to generate results in lexicographical order.
    # Example: If s_raw="BAC", sorted(s_raw) becomes ['A', 'B', 'C'].
    s_sorted_chars = sorted(s_raw)
    
    # Generate all permutations of length 'k' from the sorted characters.
    # `permutations(iterable, r)`:
    # - `iterable`: The collection from which to draw elements (e.g., ['A', 'B', 'C']).
    # - `r`: The length of the permutations (e.g., k=2).
    # Yields tuples like ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), etc.
    perms = permutations(s_sorted_chars, k)
    
    # Iterate through each generated permutation tuple.
    for perm_tuple in perms:
        # Join the characters in the permutation tuple to form a string.
        # Example: ('A', 'B') -> "AB"
        print(''.join(perm_tuple))
                                
if __name__ == '__main__':
    print("--- itertools.permutations() Demo ---")
    print("This program generates permutations of a string's characters.")

    try:
        # Read the input string 's' and the integer 'k' (length of permutations).
        # input().split() reads a line like "HACK 2" and splits into ['HACK', '2'].
        s_str, k_str = input("Enter a string and an integer K (e.g., 'HACK 2'): ").split()
        k = int(k_str) # Convert K to an integer.

        # Validate k
        if k < 0:
            print("Error: K must be a non-negative integer.")
            exit()
        if k > len(s_str):
            print(f"Error: K ({k}) cannot be greater than the length of the string ({len(s_str)}).")
            exit()
        
        print(f"\nGenerating permutations of length {k} from '{s_str}' (sorted):")
        # Call the function to generate and print permutations.
        generate_permutations(s_str, k)

    except ValueError:
        # Handle cases where K is not a valid integer or input split fails.
        print("Invalid input. Please ensure you enter a string and an integer K, space-separated.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")


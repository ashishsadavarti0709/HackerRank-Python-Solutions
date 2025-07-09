# Name: Ashish Sadavarti
# Code: itertools.product() Demo (Cartesian Product)
# Code Description: Computes the Cartesian product of two input iterables (lists of integers)
#                   and prints the result as space-separated tuples.
#                   Utilizes `itertools.product`.
# Copyright 2025

# This script demonstrates the use of `itertools.product`.
# This function calculates the Cartesian product of input iterables.
# The Cartesian product of two sets A and B (A × B) is the set of all ordered pairs (a, b)
# where a is in A and b is in B. `itertools.product` generates these pairs efficiently.

from itertools import product # Import the product function.

if __name__ == '__main__':
    print("--- itertools.product() Demo (Cartesian Product) ---")
    print("This program calculates the Cartesian product of two lists.")

    try:
        # Read elements for list A (space-separated integers).
        A_str = input("Enter space-separated integers for List A (e.g., '1 2'): ").strip()
        A = list(map(int, A_str.split()))

        # Read elements for list B (space-separated integers).
        B_str = input("Enter space-separated integers for List B (e.g., '3 4'): ").strip()
        B = list(map(int, B_str.split()))

        # Handle empty lists gracefully
        if not A or not B:
            print("One or both input lists are empty. The Cartesian product will be empty.")
            # Print an empty line as per common HackerRank behavior for empty products
            print("") 
            exit()

        # Compute the Cartesian product of A and B.
        # `product(A, B)` returns an iterator that yields tuples (a, b) for each pair.
        result_iterator = product(A, B)

        # Convert the iterator to a list of strings, then join them with spaces.
        # map(str, result_iterator) converts each tuple (e.g., (1, 3)) to its string representation "(1, 3)".
        # ' '.join(...) then concatenates these strings with spaces in between.
        final_output = ' '.join(map(str, result_iterator))

        # Print the final result.
        print("\nCartesian Product of A and B:")
        print(final_output)

    except ValueError:
        # Handle cases where input elements cannot be converted to integers.
        print("Invalid input. Please ensure all elements are space-separated integers.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")


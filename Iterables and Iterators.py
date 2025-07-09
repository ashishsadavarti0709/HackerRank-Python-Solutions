# Name: Ashish Sadavarti
# Code: Iterables & Iterators: Combination Probability
# Code Description: Calculates the probability of selecting 'k' items from 'n' items,
#                   such that at least one 'a' is present in the selection.
#                   Utilizes `itertools.combinations`.
# Copyright 2025

# This script demonstrates the use of iterables and iterators, specifically
# `itertools.combinations`, to solve a probability problem.
# It reads a list of letters, a count 'k', and then calculates the probability
# that a randomly chosen combination of 'k' letters from the list will contain
# at least one instance of the letter 'a'.

from itertools import combinations # Import the combinations function.

if __name__ == '__main__':
    print("--- Combinations Probability Calculator ---")
    print("This program calculates the probability of picking 'k' letters that include 'a'.")

    try:
        # Read the total number of letters.
        n = int(input("Enter the total number of letters (N): "))

        # Validate n
        if n < 0:
            print("Error: N cannot be negative.")
            exit()
        
        # Read the space-separated letters.
        # .split() creates a list of strings (letters).
        letters_str = input(f"Enter {n} space-separated lowercase letters (e.g., 'a b c d'): ")
        letters = letters_str.split()
        
        # Ensure the actual number of letters matches N.
        if len(letters) != n:
            print(f"Warning: Expected {n} letters but received {len(letters)}. Proceeding anyway.")

        # Read the size of the combination (k).
        k = int(input("Enter the size of the combination (K): "))

        # Validate k
        if k < 0 or k > n:
            print(f"Error: K ({k}) must be between 0 and N ({n}) inclusive.")
            exit()

        # Generate all possible combinations of 'k' indices from 'n' total indices.
        # `range(n)` gives numbers from 0 to n-1, representing indices.
        # `combinations(iterable, r)` generates all unique combinations of length 'r'.
        # We convert it to a list to get its length.
        total_combinations = list(combinations(range(n), k))
        
        # Handle case where no combinations are possible (e.g., k=0 or n<k but handled by k>n check)
        if not total_combinations:
            print("No combinations possible (e.g., K=0 or K > N). Probability is 0.0000.")
            print("0.0000") # Print expected HackerRank output format for this edge case
            exit()

        # Filter for "valid" combinations: those that contain at least one 'a'.
        # For each 'comb' (a tuple of indices), we check if `letters[i]` is 'a' for any 'i' in 'comb'.
        valid_combinations = [comb for comb in total_combinations if any(letters[i] == 'a' for i in comb)]

        # Calculate the probability.
        # Probability = (Number of valid combinations) / (Total number of combinations)
        probability = len(valid_combinations) / len(total_combinations)
        
        # Print the probability formatted to four decimal places.
        print(f"{probability:.4f}")

    except ValueError:
        # Handle cases where input for n, k, or elements are not valid.
        print("Invalid input. Please ensure N, K are integers and letters are space-separated.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")


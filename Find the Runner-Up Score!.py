# Name: Ashish Sadavarti
# Code: Find the Runner-Up Score
# Code Description: Finds the second highest unique score (runner-up score)
#                   from a list of numbers.
# Copyright 2025

# This script finds the runner-up (second largest) score from a given list of numbers.
# It handles duplicate scores by first converting the list to a set to get unique scores,
# then sorting these unique scores, and finally selecting the second-to-last element.

if __name__ == '__main__':
    print("--- Find the Runner-Up Score ---")
    
    try:
        # Read 'n', the number of scores.
        # This input is often given but not strictly used to constrain list length in Python.
        n = int(input("Enter the number of scores (N): "))

        # Validate n
        if n <= 0:
            print("Error: Number of scores (N) must be a positive integer.")
            exit()

        # Read the space-separated scores and convert them to a list of integers.
        scores_str = input("Enter the scores space-separated (e.g., '2 3 6 6 5'): ")
        arr = list(map(int, scores_str.split()))

        # Check if the actual number of scores matches 'n' (optional but good practice)
        if len(arr) != n:
            print(f"Warning: Expected {n} scores but received {len(arr)}. Proceeding with available scores.")

        # Convert the list to a set to remove duplicate scores.
        # Example: [2, 3, 6, 6, 5] -> {2, 3, 5, 6}
        unique_scores_set = set(arr)

        # Check if there are at least two unique scores to find a runner-up.
        if len(unique_scores_set) < 2:
            print("Error: Not enough unique scores to determine a runner-up (need at least two unique scores).")
            exit()

        # Convert the set back to a list and sort it.
        # Since sets are unordered, converting to list and sorting ensures order.
        # Example: {2, 3, 5, 6} -> [2, 3, 5, 6]
        sorted_unique_scores = sorted(unique_scores_set)

        # The runner-up score is the second-to-last element in the sorted list.
        # Access with index -2.
        runner_up_score = sorted_unique_scores[-2]
        
        # Print the runner-up score.
        print("\nThe runner-up score is:", runner_up_score)

    except ValueError:
        # Handle cases where input cannot be converted to integers.
        print("Invalid input. Please ensure scores are space-separated integers.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")


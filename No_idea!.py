# Name: Ashish Sadavarti
# Code: No Idea! (Sets and Happiness Calculation)
# Code Description: Calculates a 'happiness' score based on elements present in
#                   a main array and two special sets (A and B).
# Copyright 2025

# This script demonstrates the efficient use of Python sets for membership testing.
# It simulates a "happiness" calculation problem:
# - You are given a main array of integers.
# - You are also given two sets of integers, Set A and Set B.
# - For each integer in the main array:
#   - If it's present in Set A, your happiness increases by 1.
#   - If it's present in Set B, your happiness decreases by 1.
#   - If it's in neither, or in both (though problem usually implies mutual exclusion),
#     your happiness remains unchanged based on that element.

if __name__ == '__main__':
    print("--- No Idea! (Happiness Calculator) ---")
    print("This program calculates happiness based on element presence in sets A and B.")

    try:
        # Read n (length of array) and m (length of sets A and B, though not strictly used for set input size).
        n_str, m_str = input("Enter N (array size) and M (set sizes), space-separated: ").split()
        n = int(n_str)
        m = int(m_str)

        # Validate n and m (often N and M are constraints for input size, not content validation)
        if n < 0 or m < 0:
            print("Error: N and M must be non-negative integers.")
            exit()

        # Read the main array of integers.
        # `list(map(int, input().split()))` reads a line of space-separated numbers
        # and converts them into a list of integers.
        array_elements_str = input(f"Enter {n} space-separated integers for the main array: ")
        array = list(map(int, array_elements_str.split()))

        # Read elements for set A and convert them directly to a set.
        # Sets provide O(1) average-case time complexity for membership testing (`in` operator).
        set_A_elements_str = input(f"Enter {m} space-separated integers for Set A: ")
        A = set(map(int, set_A_elements_str.split()))

        # Read elements for set B and convert them directly to a set.
        set_B_elements_str = input(f"Enter {m} space-separated integers for Set B: ")
        B = set(map(int, set_B_elements_str.split()))

        happiness = 0 # Initialize the happiness score to 0.

        # Iterate through each element in the `array`.
        for element in array:
            # Check if the current `element` is in Set A.
            # Set lookup is very fast.
            if element in A:
                happiness += 1 # Increase happiness if found in A.
            
            # Check if the current `element` is in Set B.
            # Note: If an element can be in both A and B, and the problem implies
            # the effects are cumulative, this `elif` should be an `if` to apply both.
            # However, for "No Idea!" problem, it's typically mutually exclusive,
            # so `elif` is correct: if it's in A, it's handled, otherwise check B.
            elif element in B:
                happiness -= 1 # Decrease happiness if found in B (and not in A).

        # Print the final calculated happiness score.
        print("\nFinal Happiness Score:")
        print(happiness)

    except ValueError:
        # Handle cases where input elements are not valid integers.
        print("Invalid input. Please ensure all numbers are space-separated integers.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")


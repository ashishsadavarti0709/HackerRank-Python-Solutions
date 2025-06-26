# Name: Ashish Sadavarti
# Code: Strict Superset Checker
# Code Description: Determines if a given set A is a strict superset of 'n' other sets.
# Copyright 2025

# This script takes a main set 'A' and a number 'n' as input.
# It then reads 'n' more sets and checks if 'A' is a strict superset
# of ALL of those 'n' sets.

if __name__ == '__main__':
    try:
        # Prompt the user to enter elements for set A, space-separated.
        # input().split() reads the line and splits it into a list of strings.
        # set(...) converts this list into a set, which automatically handles unique elements.
        A_elements_str = input("Enter elements for set A, space-separated (e.g., '1 2 3 4 5 6'): ")
        A = set(A_elements_str.split())

        # Prompt the user to enter the number of other sets to check against.
        n = int(input("Enter the number of other sets (n) to check: "))

        # Initialize a list to store boolean results for each comparison.
        # We assume True until proven False by a condition.
        is_strict_superset_of_all = True

        # Loop 'n' times to read each of the other sets.
        for i in range(n):
            # Prompt for elements of the current subset.
            B_elements_str = input(f"Enter elements for subset {i+1}, space-separated (e.g., '1 2 3'): ")
            B = set(B_elements_str.split())

            # Check if set A is a strict superset of set B.
            # A > B means A is a strict superset of B.
            # This means all elements of B are in A, AND A has at least one element not in B.
            if not (A > B):
                is_strict_superset_of_all = False
                # If A is not a strict superset of even one B, we can stop checking.
                break
        
        # Print the final result: True if A was a strict superset of all 'n' sets, False otherwise.
        print(is_strict_superset_of_all)

    except ValueError:
        # Handle cases where 'n' is not a valid integer.
        print("Invalid input. Please ensure 'n' is an integer and set elements are correctly formatted.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")


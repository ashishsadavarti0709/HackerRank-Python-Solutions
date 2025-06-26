# Name: Ashish Sadavarti
# Code: Check if Subset
# Code Description: This script checks if one set (A) is a subset of another set (B)
#                   for multiple test cases.
# Copyright 2025

# This script is designed for problems where you need to determine if a given set
# is a subset of another set. It handles multiple test cases, reading two sets
# for each case and printing True if the first set is a subset of the second,
# and False otherwise.

if __name__ == '__main__':
    try:
        # Read the number of test cases.
        # This 't' variable determines how many pairs of sets will be compared.
        t = int(input("Enter the number of test cases: "))

        # Loop through each test case.
        for i in range(t):
            print(f"\n--- Test Case {i+1} ---")
            
            # Read the size of set A (though not strictly used for validation here).
            # This is often included in problem statements for HackerRank-style inputs.
            a_size = int(input(f"Enter the size of set A for test case {i+1}: "))
            
            # Read elements for set A.
            # input().split() reads a line of space-separated values.
            # map(int, ...) converts these string values to integers.
            # set(...) converts the map object into a set.
            a_elements_str = input(f"Enter {a_size} space-separated integers for set A: ")
            a = set(map(int, a_elements_str.split()))

            # Read the size of set B.
            b_size = int(input(f"Enter the size of set B for test case {i+1}: "))
            
            # Read elements for set B, similar to set A.
            b_elements_str = input(f"Enter {b_size} space-separated integers for set B: ")
            b = set(map(int, b_elements_str.split()))
            
            # Check if set 'a' is a subset of set 'b'.
            # The .issubset() method returns True if all elements of 'a' are present in 'b'.
            # It returns False otherwise.
            print(a.issubset(b))

    except ValueError:
        # Handle cases where input is not a valid integer.
        print("Invalid input. Please ensure all sizes and set elements are integers.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")


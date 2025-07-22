# Name: Ashish Sadavarti
# Code: Maximize It! (Sum of Squares Modulo M)
# Code Description: Finds the maximum value of (X1^2 + X2^2 + ... + XK^2) % M,
#                   where Xi is chosen from the i-th input list.
#                   Utilizes `itertools.product` for combinations.
# Copyright 2025

# This script solves a maximization problem involving modular arithmetic and combinations.
# It reads K (number of lists) and M (modulus). Then, it reads K lists of numbers.
# For each list, the first element (size) is ignored, and the remaining elements are used.
# The goal is to select exactly one number from each of the K lists (forming a combination),
# calculate the sum of the squares of these selected numbers, take the result modulo M,
# and find the maximum possible value among all such combinations.

from itertools import product # Import the product function for Cartesian product.

if __name__ == '__main__':
    print("--- Maximize It! (Sum of Squares Modulo M) ---")
    print("This program finds the max of (sum of squares) % M across combinations.")

    try:
        # Read K (number of lists) and M (modulus).
        # Example: "3 1000"
        K_str, M_str = input("Enter K (number of lists) and M (modulus), space-separated: ").split()
        K = int(K_str)
        M = int(M_str)

        # Validate K and M
        if K <= 0 or M <= 0:
            print("Error: K and M must be positive integers.")
            exit()

        lists = [] # Initialize an empty list to hold the K input lists of numbers.

        print(f"\nEnter {K} lines for the lists. Each line starts with N_i (count), then N_i numbers.")
        print("Example for 3 lists: (N1 X1 X2..), (N2 Y1 Y2..), (N3 Z1 Z2..)")
        # Loop K times to read each of the K lists.
        for i in range(K):
            # Read a line of numbers.
            # Example: "3 1 2 3" (N_i = 3, numbers are 1, 2, 3)
            # `input().split()` splits the string into parts.
            # `list(map(int, ...))` converts parts to integers and makes a list.
            # `[1:]` slices the list to *exclude the first element* (which is N_i, the count).
            # This ensures only the actual numbers are stored.
            current_list_str = input(f"List {i+1} (starts with count, then numbers): ").split()
            
            if not current_list_str:
                print(f"Error: List {i+1} is empty. It must contain at least a count.")
                exit()
            
            # Extract N_i (the count) to check consistency, but only use elements from index 1.
            N_i = int(current_list_str[0])
            numbers = list(map(int, current_list_str[1:]))

            if N_i != len(numbers):
                print(f"Warning: Stated count {N_i} for list {i+1} does not match actual numbers provided ({len(numbers)}). Using provided numbers.")
            
            if not numbers:
                print(f"Error: List {i+1} contains no numbers after its count. Each list must have at least one element to select.")
                exit()

            lists.append(numbers)

        max_value = 0 # Initialize the maximum S_max value found so far to 0.

        # Generate the Cartesian product of all the input lists.
        # `product(*lists)`: The `*` unpacks the `lists` list into separate arguments
        # for `product`. So, if `lists = [[1,2], [3,4]]`, it becomes `product([1,2], [3,4])`.
        # This yields tuples, where each tuple is a combination containing one element
        # from each of the K input lists.
        # Example: if lists = [[1, 2], [3, 4]], combinations will be:
        # (1, 3), (1, 4), (2, 3), (2, 4)
        print("\nCalculating max (sum of squares) % M...")
        for combination in product(*lists):
            # For each combination (e.g., (1, 3)):
            # Calculate the sum of squares of its elements.
            # `sum(x**2 for x in combination)` uses a generator expression for efficiency.
            # Example: (1**2 + 3**2) = 1 + 9 = 10
            sum_of_squares = sum(x**2 for x in combination)
            
            # Take the sum of squares modulo M.
            current_value = sum_of_squares % M
            
            # Update `max_value` if the `current_value` is greater.
            max_value = max(max_value, current_value)

        # Print the final maximum value found.
        print("\nMaximum (Sum of Squares) % M:", max_value)

    except ValueError:
        # Handle cases where input elements are not valid integers.
        print("Invalid input. Please ensure all numbers are integers and formats are correct.")
    except IndexError:
        # This can happen if an empty line is entered for a list and split() results in empty.
        print("Input error: Each list line must contain at least a count and one number.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")


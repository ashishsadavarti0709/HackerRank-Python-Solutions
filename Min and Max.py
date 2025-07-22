# Name: Ashish Sadavarti
# Code: NumPy Min and Max Operations
# Code Description: Finds the minimum value along each row of a 2D NumPy array,
#                   and then finds the maximum of those minimums.
# Copyright 2025

# This script demonstrates a common pattern in competitive programming problems
# involving NumPy arrays: performing operations along specific axes and then
# combining the results. Specifically, it finds the minimum value in each row
# of a 2D matrix and then determines the maximum among these row-wise minimums.

import numpy # Import the NumPy library.

if __name__ == '__main__':
    print("--- NumPy Min and Max Operations ---")
    print("This program finds the maximum of the minimums of rows in a matrix.")

    try:
        # Read the dimensions: N (rows) and M (columns).
        N_str, M_str = input("Enter dimensions N (rows) and M (columns), space-separated (e.g., '2 2'): ").split()
        N = int(N_str)
        M = int(M_str)

        # Validate N and M
        if N <= 0 or M <= 0:
            print("Error: N and M must be positive integers.")
            exit()

        matrix_rows = [] # Initialize an empty list to store matrix rows.
        print(f"\nEnter {N} rows for the matrix (each with {M} space-separated integers):")
        # Read 'N' rows of data for the array.
        for i in range(N):
            row_str = input(f"Row {i+1}: ").split()
            
            # Validate row length.
            if len(row_str) != M:
                print(f"Error: Row {i+1} has {len(row_str)} elements, but {M} were expected. Please re-enter the matrix.")
                exit()
            
            matrix_rows.append(list(map(int, row_str))) # Convert row elements to integers.
        
        # Convert the list of lists into a NumPy array of integers.
        array = numpy.array(matrix_rows)

        print("\nOriginal Array:")
        print(array)

        # Step 1: Find the minimum value along `axis=1`.
        # `axis=1` refers to the columns. So, `numpy.min(array, axis=1)`
        # finds the minimum value in each row.
        # The result will be a 1-D array (a vector) where each element is
        # the minimum of its corresponding row.
        # Example: if array is [[1, 2, 3], [4, 5, 6]]
        # min_along_rows would be [1, 4]
        min_along_rows = numpy.min(array, axis=1)
        print("\nMinimum values along each row:")
        print(min_along_rows)

        # Step 2: Find the maximum value from the result of Step 1.
        # `numpy.max(min_along_rows)` finds the maximum value within the 1-D array
        # containing the row minimums.
        # Example: if min_along_rows is [1, 4], then max of these is 4.
        result = numpy.max(min_along_rows)

        print("\nMaximum of the minimums (result):")
        # Print the final result.
        print(result)

    except ValueError:
        # Handle cases where input for N, M, or array elements are not valid integers.
        print("Invalid input. Please ensure N, M, and array elements are space-separated integers.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")


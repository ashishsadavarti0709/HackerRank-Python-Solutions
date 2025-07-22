# Name: Ashish Sadavarti
# Code: NumPy Mean, Variance, and Standard Deviation
# Code Description: Calculates the mean along rows, variance along columns,
#                   and overall standard deviation of a 2D NumPy array.
# Copyright 2025

# This script demonstrates the use of NumPy functions for common statistical calculations
# on a 2D array (matrix):
# - `np.mean()`: Calculates the arithmetic mean.
# - `np.var()`: Calculates the variance.
# - `np.std()`: Calculates the standard deviation.
# It showcases how these functions can be applied along specific axes (rows or columns)
# or across the entire array.

import numpy as np # Import the NumPy library.

if __name__ == '__main__':
    print("--- NumPy Mean, Variance, and Standard Deviation ---")
    print("This program calculates statistics for a 2D array.")

    try:
        # Read the dimensions: n (rows) and m (columns).
        n_str, m_str = input("Enter dimensions N (rows) and M (columns), space-separated (e.g., '2 2'): ").split()
        n = int(n_str)
        m = int(m_str)

        # Validate N and M
        if n <= 0 or m <= 0:
            print("Error: N and M must be positive integers.")
            exit()

        matrix_rows = [] # Initialize an empty list to store matrix rows.
        print(f"\nEnter {n} rows for the matrix (each with {m} space-separated integers):")
        # Read 'n' rows of data for the array.
        for i in range(n):
            row_str = input(f"Row {i+1}: ").split()
            
            # Validate row length
            if len(row_str) != m:
                print(f"Error: Row {i+1} has {len(row_str)} elements, but {m} were expected. Please re-enter the matrix.")
                exit()
            
            matrix_rows.append(row_str)
        
        # Convert the list of lists of strings into a NumPy array of integers.
        array = np.array(matrix_rows, dtype=int)

        print("\nOriginal Array:")
        print(array)

        # Calculate the mean along `axis=1`.
        # `axis=1` means the mean is computed across columns for each row.
        # The result will be a 1-D array with `n` elements (one mean per row).
        # Example: if array is [[1, 2], [3, 4]], mean(axis=1) -> [1.5, 3.5]
        mean_along_rows = np.mean(array, axis=1)
        print("\nMean along rows (axis=1):")
        print(mean_along_rows)

        # Calculate the variance along `axis=0`.
        # `axis=0` means the variance is computed across rows for each column.
        # The result will be a 1-D array with `m` elements (one variance per column).
        # Example: if array is [[1, 2], [3, 4]], var(axis=0) -> [var(1,3), var(2,4)] = [1.0, 1.0]
        var_along_columns = np.var(array, axis=0)
        print("\nVariance along columns (axis=0):")
        print(var_along_columns)

        # Calculate the standard deviation of the entire array.
        # When no 'axis' is specified, the standard deviation is computed over the flattened array.
        # `round(..., 11)` rounds the result to 11 decimal places, which is often required
        # for precision in competitive programming problems.
        std_overall = round(np.std(array), 11)
        print("\nStandard Deviation of the entire array (rounded to 11 decimal places):")
        print(std_overall)

    except ValueError:
        # Handle cases where input for N, M, or array elements are not valid integers.
        print("Invalid input. Please ensure N, M, and array elements are space-separated integers.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")


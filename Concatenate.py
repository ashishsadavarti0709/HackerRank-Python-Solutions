# Name: Ashish Sadavarti
# Code: NumPy Array Concatenation
# Code Description: Reads two 2D arrays (matrices) and concatenates them along axis 0
#                   (row-wise), then prints the resulting array.
# Copyright 2025

# This script demonstrates the use of NumPy's `concatenate` function.
# It takes two arrays as input, which are treated as matrices.
# The arrays are concatenated vertically (along axis 0), meaning the rows
# of the second array are appended below the rows of the first array.
# The number of columns must be the same for both arrays for this operation.

import numpy as np # Import the NumPy library, commonly aliased as 'np'.

if __name__ == '__main__':
    try:
        # Read three space-separated integers:
        # n: number of rows for the first array
        # m: number of rows for the second array
        # p: number of columns for both arrays (must be consistent)
        n_str, m_str, p_str = input("Enter dimensions (N rows for Array 1, M rows for Array 2, P columns): ").split()
        n = int(n_str)
        m = int(m_str)
        p = int(p_str)

        # Validate input dimensions for clarity
        if n <= 0 or m <= 0 or p <= 0:
            print("Error: N, M, and P must be positive integers.")
            exit()

        print(f"\nEnter {n} rows for Array 1 (each with {p} space-separated integers):")
        # Read data for the first array (array_1).
        # A list comprehension iterates 'n' times to read each row.
        # input().split() reads a line and splits it into strings.
        # np.array(..., int) converts the list of lists of strings into a NumPy array of integers.
        array_1_rows = []
        for i in range(n):
            row_str = input(f"Row {i+1} of Array 1: ").split()
            if len(row_str) != p:
                print(f"Warning: Row {i+1} has {len(row_str)} columns, expected {p}. Adjusting if possible.")
                # Basic handling: either pad or truncate if needed, or raise error.
                # For this problem, usually input guarantees correct `p`.
                # If problem strictly requires `p` columns, you might want to raise an error.
            array_1_rows.append(row_str)
        array_1 = np.array(array_1_rows, int)

        print(f"\nEnter {m} rows for Array 2 (each with {p} space-separated integers):")
        # Read data for the second array (array_2), similar to array_1.
        array_2_rows = []
        for i in range(m):
            row_str = input(f"Row {i+1} of Array 2: ").split()
            if len(row_str) != p:
                print(f"Warning: Row {i+1} has {len(row_str)} columns, expected {p}. Adjusting if possible.")
            array_2_rows.append(row_str)
        array_2 = np.array(array_2_rows, int)

        # Before concatenation, it's good practice to ensure column compatibility.
        # NumPy's concatenate will raise a ValueError if shapes are incompatible.
        if array_1.shape[1] != array_2.shape[1]:
            print(f"Error: Number of columns mismatch. Array 1 has {array_1.shape[1]} columns, Array 2 has {array_2.shape[1]}.")
            print("Concatenation along axis 0 requires matching number of columns.")
            exit()

        # Concatenate the two arrays along `axis=0`.
        # axis=0 means concatenation along rows (stacking vertically).
        # The first array's rows are followed by the second array's rows.
        result = np.concatenate((array_1, array_2), axis=0)

        print("\nResulting concatenated array:")
        # Print the resulting concatenated NumPy array.
        print(result)

    except ValueError:
        # Handles errors if input cannot be converted to integers, or if shapes are incompatible.
        print("Invalid input. Please ensure dimensions and array elements are space-separated integers.")
    except IndexError:
        # Catches issues if split() does not produce enough elements for map(int, ...)
        print("Input error: Not enough elements provided for dimensions or array rows.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")


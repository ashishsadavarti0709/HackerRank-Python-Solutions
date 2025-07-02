# Name: Ashish Sadavarti
# Code: NumPy Matrix Dot Product
# Code Description: Reads two square matrices (NumPy arrays) of size n x n,
#                   performs matrix multiplication (dot product), and prints the result.
# Copyright 2025

# This script demonstrates matrix multiplication (dot product) using the NumPy library.
# It reads the dimension 'n' for square matrices, then takes 'n' rows of 'n'
# space-separated integers for two matrices (A and B). Finally, it computes
# their dot product (matrix multiplication) and prints the resulting matrix.

import numpy as np # Import the NumPy library, commonly aliased as 'np'.

if __name__ == '__main__':
    print("--- NumPy Matrix Dot Product ---")
    
    try:
        # Read the dimension 'n' for the square matrices (n x n).
        n = int(input("Enter the dimension (n) for the square matrices (e.g., 2 for 2x2): "))

        # Validate n
        if n <= 0:
            print("Error: Dimension 'n' must be a positive integer.")
            exit()

        print(f"\nEnter elements for Matrix A ({n}x{n}, each row space-separated integers):")
        # Read elements for Matrix A.
        # It iterates 'n' times to read each row.
        # input().split() reads a line and splits it into strings.
        # map(int, ...) converts these string values to integers.
        # list(...) converts the map object to a list for each row.
        # np.array(...) converts the list of lists into a NumPy array.
        matrix_A_rows = []
        for i in range(n):
            row_elements_str = input(f"Row {i+1} of A: ").split()
            if len(row_elements_str) != n:
                print(f"Warning: Row {i+1} of A has {len(row_elements_str)} elements, expected {n}. Adjusting if possible.")
                # For strict problems, you might raise an error here.
            matrix_A_rows.append(list(map(int, row_elements_str)))
        A = np.array(matrix_A_rows)

        print(f"\nEnter elements for Matrix B ({n}x{n}, each row space-separated integers):")
        # Read elements for Matrix B in the same way as Matrix A.
        matrix_B_rows = []
        for i in range(n):
            row_elements_str = input(f"Row {i+1} of B: ").split()
            if len(row_elements_str) != n:
                print(f"Warning: Row {i+1} of B has {len(row_elements_str)} elements, expected {n}. Adjusting if possible.")
            matrix_B_rows.append(list(map(int, row_elements_str)))
        B = np.array(matrix_B_rows)

        # Perform matrix multiplication (dot product).
        # For 2D arrays, np.dot(A, B) performs matrix multiplication.
        # For 1D arrays, it performs the inner product of vectors.
        # For N-D arrays, it is a sum product over the last axis of a and the second-to-last of b.
        result = np.dot(A, B)

        print("\nResult of Matrix A dot Matrix B:")
        # Print the resulting matrix.
        print(result)

    except ValueError:
        # Handle cases where input cannot be converted to integers or invalid dimensions.
        print("Invalid input. Please ensure 'n' is an integer and matrix elements are space-separated integers.")
    except Exception as e:
        # Catch any other unexpected errors during execution (e.g., dimension mismatch issues
        # that NumPy might raise if inputs are not strictly n x n despite parsing).
        print(f"An unexpected error occurred: {e}. Ensure matrices are square and compatible.")


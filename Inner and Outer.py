# Name: Ashish Sadavarti
# Code: NumPy Inner and Outer Products
# Code Description: Calculates and prints the inner product and outer product
#                   of two 1-D NumPy arrays (vectors).
# Copyright 2025

# This script demonstrates how to compute the inner (dot) product and the
# outer product of two 1-dimensional NumPy arrays (vectors).
# It takes two lines of space-separated integers as input, converts them
# into NumPy arrays, and then performs the respective operations.

import numpy as np # Import the NumPy library.

if __name__ == '__main__':
    print("--- NumPy Inner and Outer Products ---")
    
    try:
        # Read the first line of space-separated integers for array A.
        # .strip() removes leading/trailing whitespace.
        # .split() splits the string into a list of string elements.
        # dtype=int converts these elements to integers when creating the NumPy array.
        A_str = input("Enter space-separated integers for Array A (e.g., '0 1'): ").strip()
        A = np.array(A_str.split(), dtype=int)

        # Read the second line of space-separated integers for array B.
        B_str = input("Enter space-separated integers for Array B (e.g., '2 3'): ").strip()
        B = np.array(B_str.split(), dtype=int)

        # Validate that arrays are 1-D. These operations are typically for 1-D arrays.
        if A.ndim != 1 or B.ndim != 1:
            print("Error: Input arrays must be 1-dimensional for these operations.")
            exit()
        
        # Calculate the inner product (dot product) of A and B.
        # For 1-D arrays (vectors), np.inner(A, B) is equivalent to the dot product.
        # If A = [a1, a2, ..., an] and B = [b1, b2, ..., bn],
        # inner product = a1*b1 + a2*b2 + ... + an*bn
        # Example: A=[0, 1], B=[2, 3] => (0*2) + (1*3) = 0 + 3 = 3
        inner_product = np.inner(A, B)

        # Calculate the outer product of A and B.
        # For 1-D arrays A (shape m,) and B (shape n,),
        # np.outer(A, B) results in an m x n 2-D array where
        # result[i, j] = A[i] * B[j].
        # Example: A=[0, 1], B=[2, 3] =>
        # [[0*2, 0*3],
        #  [1*2, 1*3]]
        # = [[0, 0],
        #    [2, 3]]
        outer_product = np.outer(A, B)

        print("\nInner Product:")
        print(inner_product)

        print("\nOuter Product:")
        print(outer_product)

    except ValueError:
        # Handle cases where input elements cannot be converted to integers.
        print("Invalid input. Please ensure elements are space-separated integers.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")


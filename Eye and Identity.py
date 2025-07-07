# Name: Ashish Sadavarti
# Code: NumPy Eye and Identity Matrix
# Code Description: Creates an N x M identity-like matrix using NumPy's eye() function
#                   and sets printing options for specific formatting.
# Copyright 2025

# This script demonstrates the use of NumPy's `eye()` function to create
# an identity-like 2-D array (matrix) with ones on the diagonal and zeros elsewhere.
# It also includes `numpy.set_printoptions(legacy='1.13')` which is often
# used in competitive programming contexts to ensure that array output matches
# specific historical formatting requirements (e.g., in HackerRank).

import numpy # Import the NumPy library.

if __name__ == '__main__':
    print("--- NumPy Eye and Identity Matrix Generator ---")
    print("This program generates an N x M matrix with ones on the diagonal.")

    try:
        # Set print options to 'legacy' mode.
        # This is often important in online judges like HackerRank where output
        # format of floating point numbers (e.g., trailing zeros) might be strict.
        # It ensures compatibility with older NumPy versions' printing behavior.
        numpy.set_printoptions(legacy='1.13')

        # Read two space-separated integers for the dimensions: N (rows) and M (columns).
        N_str, M_str = input("Enter dimensions N (rows) and M (columns), space-separated (e.g., '3 3'): ").split()
        N = int(N_str)
        M = int(M_str)

        # Validate N and M
        if N <= 0 or M <= 0:
            print("Error: Dimensions N and M must be positive integers.")
            exit()

        # Create an N x M 2-D array (matrix) with ones on the diagonal and zeros elsewhere.
        # numpy.eye(N, M) creates a matrix where:
        # - The main diagonal elements are 1.
        # - All other elements are 0.
        # If N == M, it's a square identity matrix. If N != M, it's a rectangular matrix
        # with ones on the main diagonal extending as far as possible.
        result_matrix = numpy.eye(N, M)

        print(f"\nGenerated {N}x{M} identity-like matrix:")
        # Print the resulting matrix.
        print(result_matrix)

    except ValueError:
        # Handle cases where input cannot be converted to integers.
        print("Invalid input. Please ensure N and M are space-separated integers.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")


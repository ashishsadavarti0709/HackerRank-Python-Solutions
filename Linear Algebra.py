# Name: Ashish Sadavarti
# Code: NumPy Linear Algebra: Matrix Determinant
# Code Description: Calculates the determinant of a square matrix using NumPy's linear algebra module,
#                   and prints the result rounded to two decimal places.
# Copyright 2025

# This script demonstrates how to compute the determinant of a square matrix
# using the `numpy.linalg.det()` function. It takes the dimension 'n' as input,
# then reads 'n' rows of 'n' space-separated floating-point numbers to form the matrix.

import numpy as np # Import the NumPy library, commonly aliased as 'np'.

if __name__ == '__main__':
    print("--- NumPy Linear Algebra: Matrix Determinant ---")
    print("This program calculates the determinant of a square matrix.")

    try:
        # Read the dimension 'n' for the square matrix (n x n).
        n_str = input("Enter the dimension (n) for the square matrix (e.g., '2' for a 2x2 matrix): ").strip()
        n = int(n_str)

        # Validate n
        if n <= 0:
            print("Error: Dimension 'n' must be a positive integer.")
            exit()

        matrix = [] # Initialize an empty list to store the rows of the matrix.

        print(f"\nEnter {n} rows for the matrix (each with {n} space-separated floating-point numbers):")
        # Loop 'n' times to read each row of the matrix.
        for i in range(n):
            # Read a line of input, split it by spaces, and convert elements to floats.
            row_elements_str = input(f"Row {i+1}: ").strip().split()
            
            # Validate that the number of elements in the row matches 'n'.
            if len(row_elements_str) != n:
                print(f"Error: Row {i+1} has {len(row_elements_str)} elements, but {n} were expected. Please re-enter the matrix.")
                exit() # Exit if an invalid row is found, as it affects matrix shape.
                
            row = list(map(float, row_elements_str))
            matrix.append(row)

        # Convert the list of lists into a NumPy array.
        # This creates the 2D matrix structure required by NumPy functions.
        np_matrix = np.array(matrix)

        # Calculate the determinant of the matrix.
        # `np.linalg.det()` computes the determinant of a square matrix.
        determinant = np.linalg.det(np_matrix)

        print("\nOriginal Matrix:")
        print(np_matrix)
        
        print("\nCalculated Determinant (rounded to 2 decimal places):")
        # Print the determinant rounded to two decimal places.
        print(round(determinant, 2))

    except ValueError:
        # Handle cases where input for 'n' or matrix elements are not valid numbers.
        print("Invalid input. Please ensure 'n' is an integer and matrix elements are space-separated numbers.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")


# Name: Ashish Sadavarti
# Code: Array Mathematics
# Code Description: Performs element-wise arithmetic operations (addition, subtraction, multiplication,
#                   integer division, modulus, and power) on two NumPy arrays.
# Copyright 2025

# This script utilizes the NumPy library to perform various element-wise
# mathematical operations on two arrays of the same dimensions.
# It reads the dimensions (rows 'n' and columns 'm') first,
# then reads 'n' lines for each array 'a' and 'b', where each line
# contains 'm' space-separated integers.

import numpy as np # Import the NumPy library, commonly aliased as 'np'

if __name__ == '__main__':
    try:
        # Get the dimensions of the arrays (n rows, m columns)
        # input().split() reads a line of space-separated values (e.g., "3 3")
        # map(int, ...) converts these string values to integers.
        # n, m = ... unpacks the two integers into variables n and m.
        n_str, m_str = input("Enter the dimensions (rows columns, e.g., '3 3'): ").split()
        n = int(n_str)
        m = int(m_str)

        print(f"Enter {n} rows with {m} space-separated integers for array A:")
        # Read data for array 'a'.
        # A list comprehension is used to iterate 'n' times (for each row).
        # Inside, input().split() reads each row, map(int, ...) converts values to integers,
        # and list(...) creates a list for the row.
        # np.array(...) then converts this list of lists into a NumPy array.
        a = np.array([list(map(int, input().split())) for _ in range(n)])

        print(f"Enter {n} rows with {m} space-separated integers for array B:")
        # Read data for array 'b' in the same manner as array 'a'.
        b = np.array([list(map(int, input().split())) for _ in range(n)])

        print("\nResults of Element-wise Operations:")

        # Element-wise addition
        # If a = [[1, 2], [3, 4]] and b = [[5, 6], [7, 8]], then a + b = [[6, 8], [10, 12]]
        print("A + B:")
        print(a + b)

        # Element-wise subtraction
        # a - b = [[-4, -4], [-4, -4]]
        print("\nA - B:")
        print(a - b)

        # Element-wise multiplication
        # This is NOT matrix multiplication. It multiplies corresponding elements.
        # a * b = [[5, 12], [21, 32]]
        print("\nA * B (Element-wise Product):")
        print(a * b)

        # Element-wise integer division (floor division)
        # This performs division and floors the result to the nearest integer.
        # It handles division by zero by raising a ZeroDivisionError (or by producing inf/nan for floats)
        # In integer arrays, it typically results in a ZeroDivisionError if any element in b is 0.
        print("\nA // B (Element-wise Floor Division):")
        print(a // b)

        # Element-wise modulus (remainder of division)
        # Similar to integer division, it can raise a ZeroDivisionError if any element in b is 0.
        print("\nA % B (Element-wise Modulus):")
        print(a % b)

        # Element-wise power operation (a to the power of b)
        # Each element a[i][j] is raised to the power of b[i][j].
        print("\nnp.power(A, B) (Element-wise Power):")
        print(np.power(a, b))

    except ValueError:
        # Catches errors if the input cannot be converted to integers (e.g., non-numeric input)
        print("Invalid input. Please ensure all inputs are space-separated integers.")
    except ZeroDivisionError:
        # Catches errors specifically if any element in array B is zero during division or modulus.
        print("ZeroDivisionError: Cannot perform division or modulus by zero. Check array B for zero values.")
    except Exception as e:
        # Catch any other unexpected errors during execution (e.g., mismatched dimensions, other NumPy errors)
        print(f"An unexpected error occurred: {e}")


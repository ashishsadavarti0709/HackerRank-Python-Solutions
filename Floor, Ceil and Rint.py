# Name: Ashish Sadavarti
# Code: NumPy Floor, Ceil, and Rint Operations
# Code Description: Demonstrates NumPy functions for element-wise floor, ceil,
#                   and rint (round to nearest integer) operations on an array of floats.
# Copyright 2025

# This script utilizes NumPy to perform three common rounding-related operations
# on an input array of floating-point numbers:
# 1. `floor()`: Rounds down to the nearest integer.
# 2. `ceil()`: Rounds up to the nearest integer.
# 3. `rint()`: Rounds to the nearest integer. For values exactly halfway between
#    two integers (e.g., X.5), it rounds to the nearest even integer.

import numpy # Import the NumPy library.

if __name__ == '__main__':
    print("--- NumPy Floor, Ceil, and Rint Operations ---")
    
    try:
        # Set print options to 'legacy' mode.
        # This is often important in online judges to ensure that array output
        # formatting (e.g., trailing zeros for floats) matches specific requirements.
        numpy.set_printoptions(legacy='1.13')

        # Read a line of space-separated floating-point numbers.
        # input().split() reads the line and splits it into a list of strings.
        # map(float, ...) converts these string values to floats.
        # list(...) converts the map object to a list.
        # numpy.array(...) converts the list into a NumPy array of floats.
        input_floats_str = input("Enter space-separated floating-point numbers (e.g., '1.1 2.2 3.3 4.4 5.5 -1.1 -2.5'): ")
        A = numpy.array(list(map(float, input_floats_str.split())))

        # Handle empty input case
        if A.size == 0:
            print("No numbers entered. Exiting.")
            exit()

        print("\nOriginal Array:")
        print(A)

        print("\nFloor (rounds down to the nearest integer):")
        # numpy.floor(A) computes the floor of each element in array A.
        # Example: floor(2.7) = 2.0, floor(-2.3) = -3.0
        print(numpy.floor(A))

        print("\nCeil (rounds up to the nearest integer):")
        # numpy.ceil(A) computes the ceiling of each element in array A.
        # Example: ceil(2.3) = 3.0, ceil(-2.7) = -2.0
        print(numpy.ceil(A))

        print("\nRint (rounds to the nearest integer, halfway to even):")
        # numpy.rint(A) rounds elements to the nearest integer.
        # For numbers exactly halfway between two integers (e.g., X.5),
        # it rounds to the nearest even integer (e.g., 2.5 -> 2.0, 3.5 -> 4.0).
        print(numpy.rint(A))

    except ValueError:
        # Handle cases where input cannot be converted to floats.
        print("Invalid input. Please ensure numbers are space-separated floating-point numbers.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")


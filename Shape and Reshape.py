# Name: Ashish Sadavarti
# Code: NumPyArrayReshape
# Code Description: Demonstrates how to create a NumPy array from space-separated
#                   integer input and then reshape it into a 3x3 matrix.
# Copyright 2025

import numpy

if __name__ == '__main__':
    # Read a line of input from the user.
    # Assumes input will be space-separated integers, e.g., "1 2 3 4 5 6 7 8 9".
    # .strip(): Removes any leading or trailing whitespace from the input string.
    # .split(): Splits the string into a list of substrings based on whitespace.
    # map(int, ...): Converts each string in the list to an integer.
    # numpy.array(...): Creates a NumPy array from the list of integers.
    # The 'int' argument ensures the elements are of integer type.
    arr = numpy.array(input().strip().split(), int)
    
    # Reshape the 1D array into a 2D array (matrix).
    # arr.reshape(3, 3): This method attempts to change the shape of the array
    # into a new shape. Here, it transforms the 1D array into a 3-row, 3-column matrix.
    # The total number of elements must remain the same (e.g., 9 elements for a 3x3 matrix).
    reshaped_arr = arr.reshape(3, 3)
    
    # Print the reshaped 2D array.
    # NumPy arrays are printed in a structured, readable format.
    print(reshaped_arr)

    # Example:
    # If user input is:
    # 1 2 3 4 5 6 7 8 9
    #
    # 'arr' will be: [1 2 3 4 5 6 7 8 9]
    # 'reshaped_arr' will be:
    # [[1 2 3]
    #  [4 5 6]
    #  [7 8 9]]
